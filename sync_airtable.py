#!/usr/bin/env python3
"""
Airtable Structure Documentation Generator
Supports multiple Airtable bases
"""

import os
import sys
import requests
import argparse
from datetime import datetime

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Generate Airtable documentation')
    parser.add_argument('--output', default='database-structure.md',
                       help='Output filename (default: database-structure.md)')
    parser.add_argument('--base', choices=['default', 'aulas'], default='default',
                       help='Which Airtable base to sync (default: default)')
    
    return parser.parse_args()

def get_configuration(args):
    """Get configuration based on arguments"""
    # Determine which environment variables to use
    if args.base == 'aulas':
        token_var = 'AIRTABLE_TOKEN_AULAS'
        base_id_var = 'AIRTABLE_BASE_ID_AULAS'
        base_display_name = 'Aulas'
    else:
        token_var = 'AIRTABLE_TOKEN'
        base_id_var = 'AIRTABLE_BASE_ID'
        base_display_name = 'Default'
    
    # Get values from environment
    airtable_token = os.environ.get(token_var)
    airtable_base_id = os.environ.get(base_id_var)
    
    return {
        'token': airtable_token,
        'base_id': airtable_base_id,
        'token_var': token_var,
        'base_id_var': base_id_var,
        'output_file': args.output,
        'base_name': args.base,
        'display_name': base_display_name
    }

def log(message, level="INFO"):
    """Simple logging function"""
    colors = {
        "INFO": "\033[94m",
        "SUCCESS": "\033[92m", 
        "ERROR": "\033[91m",
        "WARNING": "\033[93m",
        "RESET": "\033[0m"
    }
    color = colors.get(level, colors["INFO"])
    print(f"{color}[{level}] {message}{colors['RESET']}")

def validate_config(config):
    """Validate configuration"""
    log("=" * 50, "INFO")
    log(f"SYNC CONFIGURATION FOR: {config['display_name']}", "INFO")
    log("=" * 50, "INFO")
    
    log(f"Base selection: {config['base_name']}", "INFO")
    log(f"Token variable: {config['token_var']}", "INFO")
    log(f"Base ID variable: {config['base_id_var']}", "INFO")
    log(f"Output file: {config['output_file']}", "INFO")
    
    # Check if environment variables are set
    if not config['token']:
        log(f"❌ ERROR: {config['token_var']} is not set", "ERROR")
        log("💡 Solution: Add this secret in GitHub: Settings → Secrets → Actions", "ERROR")
        return False
    
    if not config['base_id']:
        log(f"❌ ERROR: {config['base_id_var']} is not set", "ERROR")
        log("💡 Solution: Add this secret in GitHub: Settings → Secrets → Actions", "ERROR")
        return False
    
    # Validate token format (starts with 'pat' or 'key')
    if not (config['token'].startswith('pat') or config['token'].startswith('key')):
        log(f"⚠️  WARNING: Token doesn't start with 'pat' or 'key'", "WARNING")
    
    # Validate base ID format (starts with 'app')
    if not config['base_id'].startswith('app'):
        log(f"⚠️  WARNING: Base ID doesn't start with 'app'", "WARNING")
    
    log(f"✅ Base ID: {config['base_id'][:10]}...", "SUCCESS")
    log(f"✅ Token: {'*' * 10}{config['token'][-5:] if len(config['token']) > 5 else ''}", "SUCCESS")
    
    return True

def fetch_airtable_data(config):
    """Fetch data from Airtable API"""
    log("📡 Fetching data from Airtable API...", "INFO")
    
    url = f"https://api.airtable.com/v0/meta/bases/{config['base_id']}/tables"
    headers = {"Authorization": f"Bearer {config['token']}"}
    
    try:
        log(f"URL: {url}", "INFO")
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            tables = data.get('tables', [])
            log(f"✅ Found {len(tables)} tables", "SUCCESS")
            return tables
        elif response.status_code == 401:
            log(f"❌ ERROR 401: Unauthorized - Invalid token", "ERROR")
            log("💡 Generate a new token at: https://airtable.com/create/tokens", "ERROR")
            return None
        elif response.status_code == 404:
            log(f"❌ ERROR 404: Base not found - Check Base ID", "ERROR")
            log(f"💡 Current Base ID: {config['base_id']}", "ERROR")
            return None
        else:
            log(f"❌ API Error {response.status_code}: {response.text[:200]}", "ERROR")
            return None
            
    except requests.exceptions.Timeout:
        log("❌ ERROR: Request timeout - Airtable API took too long", "ERROR")
        return None
    except Exception as e:
        log(f"❌ Connection error: {e}", "ERROR")
        return None

def generate_documentation(tables, config):
    """Generate markdown documentation"""
    log("📝 Generating documentation...", "INFO")
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Start building markdown
    lines = []
    
    # Header
    lines.append(f"# 🗂️ Airtable Database Structure - {config['display_name']}")
    lines.append("")
    lines.append(f"> **Last update**: {timestamp}")
    lines.append(f"> **Base**: {config['base_name']} ({config['display_name']})")
    lines.append("> **Auto-generated** - Do not edit manually")
    lines.append("")
    
    # Summary
    total_fields = sum(len(table.get('fields', [])) for table in tables)
    
    # Count field types
    field_types = {}
    for table in tables:
        for field in table.get('fields', []):
            field_type = field.get('type', 'unknown')
            field_types[field_type] = field_types.get(field_type, 0) + 1
    
    lines.append("## 📊 Summary")
    lines.append("")
    lines.append(f"- **Tables**: {len(tables)}")
    lines.append(f"- **Total fields**: {total_fields}")
    lines.append(f"- **Base ID**: `{config['base_id']}`")
    lines.append("")
    
    # Common field types
    common_types = ['singleSelect', 'multipleSelects', 'text', 'number', 'date', 'formula', 'lookup']
    for field_type in common_types:
        if field_type in field_types:
            lines.append(f"- **{field_type} fields**: {field_types[field_type]}")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Tables
    for idx, table in enumerate(tables, 1):
        table_name = table.get('name', f'Unnamed Table {idx}')
        table_id = table.get('id', '')
        fields = table.get('fields', [])
        
        lines.append(f"## 📋 {idx}. {table_name}")
        lines.append("")
        lines.append(f"*Table ID: `{table_id}`*")
        lines.append(f"*Fields: {len(fields)}*")
        lines.append("")
        
        if not fields:
            lines.append("*No fields in this table*")
            lines.append("")
        else:
            lines.append("| Field | Type | Description | Options |")
            lines.append("|-------|------|-------------|---------|")
            
            for field in fields:
                field_name = field.get('name', 'Unnamed Field')
                field_type = field.get('type', 'unknown')
                field_id = field.get('id', '')
                
                # Field description based on type
                type_descriptions = {
                    'singleSelect': 'Single choice dropdown',
                    'multipleSelects': 'Multiple choice dropdown',
                    'text': 'Text field',
                    'multilineText': 'Multi-line text',
                    'richText': 'Rich text with formatting',
                    'number': 'Numeric field',
                    'currency': 'Currency amount',
                    'percent': 'Percentage',
                    'date': 'Date',
                    'dateTime': 'Date and time',
                    'checkbox': 'True/False checkbox',
                    'rating': 'Star rating',
                    'formula': 'Calculated field',
                    'lookup': 'Reference to another table',
                    'rollup': 'Rollup from linked records',
                    'url': 'URL link',
                    'email': 'Email address',
                    'phoneNumber': 'Phone number',
                    'attachment': 'File attachment',
                    'barcode': 'Barcode/QR code',
                    'button': 'Action button',
                    'createdTime': 'Auto-generated creation time',
                    'lastModifiedTime': 'Auto-generated modification time',
                    'createdBy': 'Auto-generated creator',
                    'lastModifiedBy': 'Auto-generated last editor',
                }
                
                description = type_descriptions.get(field_type, f'Type: {field_type}')
                
                # Get options for select fields
                options = ""
                if field_type in ['singleSelect', 'multipleSelects']:
                    choices = field.get('options', {}).get('choices', [])
                    if choices:
                        option_names = [choice.get('name', '') for choice in choices[:5]]
                        options = ", ".join([f"`{name}`" for name in option_names if name])
                        if len(choices) > 5:
                            options += f" *(+{len(choices)-5} more)*"
                
                # For formula fields, show the formula if available
                elif field_type == 'formula':
                    formula = field.get('options', {}).get('formula', '')
                    if formula:
                        options = f"Formula: `{formula[:50]}{'...' if len(formula) > 50 else ''}`"
                
                lines.append(f"| **{field_name}**<br>`{field_id}` | `{field_type}` | {description} | {options} |")
        
        lines.append("")
        lines.append("---")
        lines.append("")
    
    # Footer with detailed information
    lines.append("## 🔄 About This Documentation")
    lines.append("")
    lines.append("### 📋 Source Information")
    lines.append(f"- **Base**: {config['display_name']} (`{config['base_name']}`)")
    lines.append(f"- **Base ID**: `{config['base_id']}`")
    lines.append(f"- **Generated**: {timestamp}")
    lines.append("")
    
    lines.append("### 🛠️ Field Type Legend")
    lines.append("- **singleSelect**: Dropdown with single choice")
    lines.append("- **multipleSelects**: Dropdown with multiple choices")
    lines.append("- **formula**: Automatically calculated value")
    lines.append("- **lookup**: References records from another table")
    lines.append("- **rollup**: Aggregates data from linked records")
    lines.append("")
    
    lines.append("### 🔧 Usage Notes")
    lines.append("1. **API Usage**: Always use the exact field names and IDs shown above")
    lines.append("2. **Select Fields**: Use only the options listed for select fields")
    lines.append("3. **Formula Fields**: Read-only, cannot be modified via API")
    lines.append("4. **Linked Fields**: lookup and rollup fields reference other tables")
    lines.append("")
    
    lines.append("### ⚡ Automation")
    lines.append("This document is auto-generated by GitHub Actions.")
    lines.append("**Update schedule**: Daily at 8:00 AM UTC")
    lines.append(f"**Last sync**: {timestamp}")
    lines.append("")
    
    lines.append("---")
    lines.append(f"*Documentation for {config['display_name']} base - Generated {timestamp}*")
    
    return "\n".join(lines)

def save_file(content, filename):
    """Save content to file"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        file_size = os.path.getsize(filename)
        line_count = content.count('\n') + 1
        
        log(f"✅ File saved: {filename}", "SUCCESS")
        log(f"   📏 Size: {file_size:,} bytes", "INFO")
        log(f"   📄 Lines: {line_count}", "INFO")
        
        # Show preview
        log("   👁️  Preview (first 5 lines):", "INFO")
        for i, line in enumerate(content.split('\n')[:5]):
            log(f"      {i+1:2}. {line[:80]}{'...' if len(line) > 80 else ''}", "INFO")
        
        return True
        
    except Exception as e:
        log(f"❌ Error saving file: {e}", "ERROR")
        return False

def main():
    """Main function"""
    print("\n" + "="*60)
    print("🚀 AIRTABLE DOCUMENTATION GENERATOR (MULTI-BASE)")
    print("="*60 + "\n")
    
    # Parse arguments
    args = parse_arguments()
    
    # Get configuration
    config = get_configuration(args)
    
    # 1. Validate configuration
    if not validate_config(config):
        sys.exit(1)
    
    # 2. Fetch data from Airtable
    tables = fetch_airtable_data(config)
    if tables is None:
        sys.exit(1)
    
    # 3. Generate documentation
    documentation = generate_documentation(tables, config)
    
    # 4. Save to file
    if save_file(documentation, config['output_file']):
        # 5. Show final summary
        print("\n" + "="*60)
        log("✅ DOCUMENTATION GENERATED SUCCESSFULLY", "SUCCESS")
        print("="*60)
        
        log(f"📊 Base: {config['display_name']} ({config['base_name']})", "INFO")
        log(f"📊 Tables processed: {len(tables)}", "INFO")
        log(f"📁 Output file: {config['output_file']}", "INFO")
        log(f"🔐 Token variable used: {config['token_var']}", "INFO")
        log(f"🔑 Base ID variable used: {config['base_id_var']}", "INFO")
        
        # Count select fields
        select_fields = 0
        for table in tables:
            for field in table.get('fields', []):
                if field.get('type') in ['singleSelect', 'multipleSelects']:
                    select_fields += 1
        
        if select_fields > 0:
            log(f"🎯 Select fields (single/multiple): {select_fields}", "INFO")
        
        print("\n" + "="*60)
        return 0
    else:
        log("\n❌ DOCUMENTATION GENERATION FAILED", "ERROR")
        return 1

if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
Airtable Structure Sync - GUARANTEED WORKING VERSION
Generates database-structure.md from Airtable API
"""

import os
import sys
import requests
import json
from datetime import datetime
from pathlib import Path

# ================= CONFIGURATION =================
AIRTABLE_TOKEN = os.environ.get('AIRTABLE_TOKEN')
AIRTABLE_BASE_ID = os.environ.get('AIRTABLE_BASE_ID')
OUTPUT_FILE = 'database-structure.md'

# ================= VALIDATION =================
def validate_environment():
    """Validate all required environment variables"""
    errors = []
    
    if not AIRTABLE_TOKEN:
        errors.append("❌ AIRTABLE_TOKEN is not set")
    elif len(AIRTABLE_TOKEN) < 20:
        errors.append("❌ AIRTABLE_TOKEN appears to be invalid (too short)")
    
    if not AIRTABLE_BASE_ID:
        errors.append("❌ AIRTABLE_BASE_ID is not set")
    elif not AIRTABLE_BASE_ID.startswith('app'):
        errors.append("❌ AIRTABLE_BASE_ID should start with 'app'")
    
    if errors:
        print("\n".join(errors))
        print("\n💡 Solution:")
        print("1. Go to GitHub repo → Settings → Secrets → Actions")
        print("2. Add AIRTABLE_TOKEN and AIRTABLE_BASE_ID")
        return False
    
    print("✅ Environment validation passed")
    print(f"   Base ID: {AIRTABLE_BASE_ID}")
    print(f"   Token: {'*' * 10}{AIRTABLE_TOKEN[-5:]}")
    return True

# ================= AIRTABLE API =================
def fetch_airtable_structure():
    """Fetch table structure from Airtable API"""
    url = f"https://api.airtable.com/v0/meta/bases/{AIRTABLE_BASE_ID}/tables"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_TOKEN}",
        "Content-Type": "application/json"
    }
    
    print(f"\n📡 Fetching from Airtable API...")
    print(f"   URL: {url}")
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        tables = data.get('tables', [])
        
        print(f"✅ Successfully fetched {len(tables)} tables")
        return tables
        
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
        if e.response.status_code == 401:
            print("   🔑 Invalid token. Generate new one at: https://airtable.com/create/tokens")
        elif e.response.status_code == 404:
            print(f"   🔍 Base not found. Check BASE_ID: {AIRTABLE_BASE_ID}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Connection Error: {e}")
        sys.exit(1)

# ================= MARKDOWN GENERATION =================
def generate_markdown(tables):
    """Generate comprehensive markdown documentation"""
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    
    lines = []
    
    # Header
    lines.append("# 🗂️ Airtable Database Structure")
    lines.append("")
    lines.append(f"> **Last automated update**: {timestamp}")
    lines.append("> ")
    lines.append("> ⚠️ **This file is auto-generated. Do not edit manually.**")
    lines.append("")
    
    # Summary
    total_fields = sum(len(table.get('fields', [])) for table in tables)
    lines.append("## 📊 Overview")
    lines.append("")
    lines.append(f"- **Total tables**: {len(tables)}")
    lines.append(f"- **Total fields**: {total_fields}")
    lines.append(f"- **Base ID**: `{AIRTABLE_BASE_ID}`")
    lines.append("- **Auto-update**: Daily at 8:00 AM UTC")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Table details
    for table_idx, table in enumerate(tables, 1):
        table_name = table.get('name', f'Table {table_idx}')
        table_id = table.get('id', '')
        fields = table.get('fields', [])
        
        lines.append(f"## 📋 {table_name}")
        lines.append("")
        lines.append(f"*Table ID: `{table_id}`*")
        lines.append("")
        
        if not fields:
            lines.append("*No fields in this table*")
            lines.append("")
        else:
            lines.append("| Field | Type | Description | Options |")
            lines.append("|-------|------|-------------|---------|")
            
            for field in fields:
                field_name = field.get('name', 'Unnamed')
                field_type = field.get('type', 'unknown')
                field_id = field.get('id', '')
                
                # Type description
                type_descriptions = {
                    'singleSelect': 'Single choice',
                    'multipleSelects': 'Multiple choices',
                    'text': 'Text',
                    'number': 'Number',
                    'date': 'Date',
                    'checkbox': 'True/False',
                    'formula': 'Calculated',
                    'lookup': 'Reference',
                    'rollup': 'Rollup',
                    'url': 'URL',
                    'email': 'Email',
                    'attachment': 'File'
                }
                
                description = type_descriptions.get(field_type, field_type)
                
                # Options for select fields
                options = ""
                if field_type in ['singleSelect', 'multipleSelects']:
                    choices = field.get('options', {}).get('choices', [])
                    if choices:
                        option_list = [f"`{c.get('name')}`" for c in choices[:3]]
                        options = ", ".join(option_list)
                        if len(choices) > 3:
                            options += f" *(+{len(choices)-3} more)*"
                
                lines.append(f"| **{field_name}**<br>`{field_id}` | `{field_type}` | {description} | {options} |")
            
            lines.append("")
        
        lines.append("---")
        lines.append("")
    
    # Footer
    lines.append("## 🔄 About This Documentation")
    lines.append("")
    lines.append("This documentation is automatically generated by:")
    lines.append("- **GitHub Actions** workflow")
    lines.append("- **Airtable Metadata API**")
    lines.append("- **Python script** (`sync_airtable.py`)")
    lines.append("")
    lines.append("### 📅 Update Schedule")
    lines.append("- Automatic: Daily at 8:00 AM UTC")
    lines.append("- Manual: Via GitHub Actions interface")
    lines.append("")
    lines.append(f"*Documentation generated on {timestamp}*")
    
    return "\n".join(lines)

# ================= FILE OPERATIONS =================
def save_to_file(content, filename):
    """Save content to file with validation"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Verify
        file_size = os.path.getsize(filename)
        line_count = len(content.split('\n'))
        
        print(f"\n💾 File saved: {filename}")
        print(f"   📏 Size: {file_size:,} bytes")
        print(f"   📄 Lines: {line_count}")
        print(f"\n📋 Preview (first 5 lines):")
        print("-" * 40)
        for i, line in enumerate(content.split('\n')[:5]):
            print(f"  {i+1:2}. {line}")
        print("-" * 40)
        
        return True
        
    except Exception as e:
        print(f"❌ Error saving file: {e}")
        return False

# ================= MAIN =================
def main():
    print("=" * 60)
    print("🚀 AIRTABLE DOCUMENTATION SYNC")
    print("=" * 60)
    
    # Step 1: Validate
    if not validate_environment():
        sys.exit(1)
    
    # Step 2: Fetch data
    tables = fetch_airtable_structure()
    
    if not tables:
        print("⚠️ No tables found. Creating minimal documentation...")
        tables = []
    
    # Step 3: Generate markdown
    markdown = generate_markdown(tables)
    
    # Step 4: Save file
    if save_to_file(markdown, OUTPUT_FILE):
        print(f"\n{'='*60}")
        print("✅ SYNC COMPLETED SUCCESSFULLY")
        print(f"{'='*60}")
        print(f"\n📊 Summary:")
        print(f"  • Tables processed: {len(tables)}")
        print(f"  • File: {OUTPUT_FILE}")
        print(f"  • Timestamp: {datetime.utcnow().strftime('%H:%M:%S UTC')}")
        return 0
    else:
        print("\n❌ SYNC FAILED")
        return 1

if __name__ == "__main__":
    sys.exit(main())

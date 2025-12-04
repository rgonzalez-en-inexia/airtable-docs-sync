# sync_airtable.py
import requests
import json
from datetime import datetime

# CONFIGURA AQUÍ TUS DATOS
AIRTABLE_API_KEY = "tu_token_aquí"  # El token que copiaste
BASE_ID = "tu_base_id_aquí"         # El ID de tu base

def get_airtable_structure():
    """Obtiene la estructura de Airtable"""
    
    url = f"https://api.airtable.com/v0/meta/bases/{BASE_ID}/tables"
    
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}"
    }
    
    print("🔍 Conectando con Airtable...")
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("✅ Estructura obtenida correctamente")
        return response.json()
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)
        return None

def create_markdown_documentation(metadata):
    """Crea un documento Markdown con la estructura"""
    
    output = f"""# 🗂️ Estructura de Base de Airtable
*Última actualización: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*

Esta documentación se genera automáticamente. **NO EDITAR MANUALMENTE**.

## 📊 Tablas Disponibles

"""
    
    for table in metadata['tables']:
        output += f"### 📋 {table['name']}\n"
        output += f"*ID de tabla: `{table['id']}`*\n\n"
        
        output += "| Campo | Tipo | Opciones | Descripción |\n"
        output += "|-------|------|----------|-------------|\n"
        
        for field in table['fields']:
            # Descripción simple basada en el tipo
            if field['type'] == 'singleSelect':
                description = "Selección única"
                options = format_select_options(field)
            elif field['type'] == 'multipleSelects':
                description = "Selección múltiple"
                options = format_select_options(field)
            elif field['type'] == 'formula':
                description = "Campo calculado"
                options = "-"
            elif field['type'] == 'lookup':
                description = "Referencia a otra tabla"
                options = "-"
            elif field['type'] == 'text':
                description = "Texto libre"
                options = "-"
            elif field['type'] == 'number':
                description = "Número"
                options = "-"
            elif field['type'] == 'date':
                description = "Fecha"
                options = "-"
            else:
                description = field['type']
                options = "-"
            
            output += f"| **{field['name']}** | `{field['type']}` | {options} | {description} |\n"
        
        output += "\n---\n\n"
    
    return output

def format_select_options(field):
    """Formatea las opciones de selección"""
    if 'choices' in field.get('options', {}):
        choices = [f"`{c['name']}`" for c in field['options']['choices']]
        return ", ".join(choices[:5]) + ("..." if len(choices) > 5 else "")
    return "-"

def save_to_file(content, filename="database-structure.md"):
    """Guarda el contenido en un archivo"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Documentación guardada en: {filename}")

def main():
    print("🚀 Iniciando sincronización de documentación...")
    
    # 1. Obtener datos de Airtable
    metadata = get_airtable_structure()
    
    if metadata:
        # 2. Generar documentación
        print("📝 Generando documentación...")
        docs = create_markdown_documentation(metadata)
        
        # 3. Guardar archivo
        save_to_file(docs)
        
        print(f"\n🎉 ¡Documentación actualizada!")
        print(f"📅 Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"📊 Tablas procesadas: {len(metadata['tables'])}")
        
        # Mostrar resumen
        for table in metadata['tables']:
            print(f"  • {table['name']}: {len(table['fields'])} campos")
    else:
        print("❌ No se pudo obtener la estructura")

if __name__ == "__main__":
    main()
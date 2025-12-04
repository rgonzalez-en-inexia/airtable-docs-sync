# sync_airtable.py
import requests
import json
from datetime import datetime
import os
import sys

# Configuración
AIRTABLE_API_KEY = os.getenv('AIRTABLE_TOKEN')
BASE_ID = os.getenv('AIRTABLE_BASE_ID')

def get_airtable_structure():
    """Obtiene la estructura de Airtable"""
    
    if not AIRTABLE_API_KEY or not BASE_ID:
        print("❌ ERROR: Faltan variables de entorno")
        print(f"AIRTABLE_TOKEN: {'✅' if AIRTABLE_API_KEY else '❌'}")
        print(f"AIRTABLE_BASE_ID: {'✅' if BASE_ID else '❌'}")
        sys.exit(1)
    
    url = f"https://api.airtable.com/v0/meta/bases/{BASE_ID}/tables"
    
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}"
    }
    
    print("🔍 Conectando con Airtable...")
    print(f"URL: {url}")
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            print("✅ Estructura obtenida correctamente")
            data = response.json()
            print(f"📊 Tablas encontradas: {len(data.get('tables', []))}")
            return data
        elif response.status_code == 401:
            print("❌ ERROR 401: Token inválido o sin permisos")
            print("Solución: Genera un nuevo token en https://airtable.com/create/tokens")
        elif response.status_code == 404:
            print("❌ ERROR 404: Base no encontrada")
            print(f"Base ID: {BASE_ID}")
            print("Solución: Verifica el ID de tu base")
        else:
            print(f"❌ Error HTTP {response.status_code}")
            print(f"Respuesta: {response.text[:200]}...")
            
        return None
        
    except requests.exceptions.Timeout:
        print("❌ Timeout: La API de Airtable tardó demasiado")
        return None
    except Exception as e:
        print(f"❌ Error inesperado: {str(e)}")
        return None

def create_markdown_documentation(metadata):
    """Crea un documento Markdown con la estructura"""
    
    update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    output = f"""# 🗂️ Estructura de Base de Airtable

> **Última actualización automática**: {update_time}
> 
> ⚠️ **Este archivo se genera automáticamente. NO EDITAR MANUALMENTE.**

## 📊 Tablas Disponibles

"""
    
    if 'tables' not in metadata or not metadata['tables']:
        return output + "\n\n❌ No se encontraron tablas en la base de datos\n"
    
    for table in metadata['tables']:
        table_name = table.get('name', 'Sin nombre')
        table_id = table.get('id', '')
        
        output += f"## 📋 Tabla: {table_name}\n"
        output += f"*ID: `{table_id}`*\n\n"
        
        output += "| Campo | Tipo | Descripción | Opciones |\n"
        output += "|-------|------|-------------|----------|\n"
        
        fields = table.get('fields', [])
        
        if not fields:
            output += "| *No hay campos* | | | |\n"
        else:
            for field in fields:
                field_name = field.get('name', 'Sin nombre')
                field_type = field.get('type', 'desconocido')
                field_id = field.get('id', '')
                
                # Descripción según tipo
                descriptions = {
                    'singleSelect': 'Selección única (elige una opción)',
                    'multipleSelects': 'Selección múltiple (elige varias)',
                    'formula': 'Campo calculado automáticamente',
                    'lookup': 'Referencia a otra tabla',
                    'rollup': 'Agregación de datos relacionados',
                    'date': 'Fecha (puede incluir hora)',
                    'dateTime': 'Fecha y hora',
                    'number': 'Número (entero o decimal)',
                    'currency': 'Valor monetario',
                    'percent': 'Porcentaje',
                    'text': 'Texto corto',
                    'multilineText': 'Texto largo (varias líneas)',
                    'richText': 'Texto con formato',
                    'url': 'Enlace web',
                    'email': 'Dirección de email',
                    'phoneNumber': 'Número telefónico',
                    'checkbox': 'Casilla de verificación (Sí/No)',
                    'rating': 'Calificación con estrellas',
                    'barcode': 'Código de barras/QR',
                    'button': 'Botón con acción',
                    'createdTime': 'Fecha/hora de creación (automático)',
                    'lastModifiedTime': 'Fecha/hora de modificación (automático)',
                    'createdBy': 'Usuario creador (automático)',
                    'lastModifiedBy': 'Último editor (automático)',
                    'attachment': 'Archivos adjuntos',
                    'externalSyncSource': 'Sincronizado externamente',
                    'aiText': 'Texto generado por IA',
                }
                
                description = descriptions.get(field_type, f'Tipo: {field_type}')
                
                # Opciones para campos de selección
                options = "-"
                if field_type in ['singleSelect', 'multipleSelects']:
                    choices = field.get('options', {}).get('choices', [])
                    if choices:
                        option_names = [f"`{choice.get('name', '')}`" for choice in choices[:8]]
                        options = ", ".join(option_names)
                        if len(choices) > 8:
                            options += f" *(y {len(choices)-8} más)*"
                
                # Para otros tipos con opciones
                elif field_type in ['checkbox', 'rating', 'number']:
                    options = "Ver configuración en Airtable"
                
                output += f"| **{field_name}**<br>`{field_id}` | `{field_type}` | {description} | {options} |\n"
        
        output += "\n---\n\n"
    
    # Agregar sección de resumen
    total_tables = len(metadata.get('tables', []))
    total_fields = sum(len(t.get('fields', [])) for t in metadata.get('tables', []))
    
    output += f"""
## 📈 Resumen

- **Total de tablas**: {total_tables}
- **Total de campos**: {total_fields}
- **Base ID**: `{BASE_ID}`
- **Actualización automática**: Diaria a las 8:00 AM UTC

---

## 🔧 Cómo usar esta documentación

1. **Para desarrolladores**: Usa los nombres exactos de campos al escribir código
2. **Para consultas**: Revisa las opciones disponibles en campos de selección
3. **Para integraciones**: Los tipos de campo determinan el formato de datos

## 🔄 Sincronización automática

Esta documentación se actualiza automáticamente mediante:
- **GitHub Actions**: Ejecuta diariamente
- **Script**: `sync_airtable.py`
- **Trigger**: Cambios en la estructura de Airtable

*Última ejecución exitosa: {update_time}*
"""
    
    return output

def save_to_file(content, filename="database-structure.md"):
    """Guarda el contenido en un archivo"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Verificar que se guardó correctamente
        import os
        file_size = os.path.getsize(filename)
        print(f"✅ Documentación guardada en: {filename}")
        print(f"   Tamaño: {file_size} bytes")
        print(f"   Líneas: {len(content.split(chr(10)))}")
        
        return True
    except Exception as e:
        print(f"❌ Error al guardar archivo: {str(e)}")
        return False

def main():
    print("=" * 60)
    print("🚀 INICIANDO SINCRONIZACIÓN DE DOCUMENTACIÓN AIRTABLE")
    print("=" * 60)
    
    # 1. Obtener datos de Airtable
    print("\n1️⃣  Obteniendo estructura de Airtable...")
    metadata = get_airtable_structure()
    
    if not metadata:
        print("❌ No se pudo obtener la estructura. Saliendo...")
        sys.exit(1)
    
    # 2. Generar documentación
    print("\n2️⃣  Generando documentación en Markdown...")
    docs = create_markdown_documentation(metadata)
    
    # 3. Guardar archivo
    print("\n3️⃣  Guardando archivo...")
    if save_to_file(docs):
        print("\n🎉 ¡DOCUMENTACIÓN ACTUALIZADA EXITOSAMENTE!")
        print("=" * 60)
        
        # Mostrar resumen
        tables = metadata.get('tables', [])
        print(f"📊 RESUMEN FINAL:")
        print(f"   • Tablas procesadas: {len(tables)}")
        
        for i, table in enumerate(tables, 1):
            table_name = table.get('name', f'Tabla {i}')
            field_count = len(table.get('fields', []))
            print(f"   {i}. {table_name}: {field_count} campos")
        
        print(f"\n📅 Fecha de actualización: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        
        return True
    else:
        print("❌ Error al guardar la documentación")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

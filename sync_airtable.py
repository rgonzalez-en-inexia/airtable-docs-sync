# sync_airtable.py - VERSIÓN CORREGIDA PARA GITHUB ACTIONS
import requests
import json
from datetime import datetime
import os
import sys

def log_message(message, level="INFO"):
    """Mensajes de log formateados"""
    colors = {
        "INFO": "\033[94m",    # Azul
        "SUCCESS": "\033[92m", # Verde
        "WARNING": "\033[93m", # Amarillo
        "ERROR": "\033[91m",   # Rojo
        "RESET": "\033[0m"     # Reset
    }
    color = colors.get(level, colors["INFO"])
    print(f"{color}[{level}] {message}{colors['RESET']}")

def check_environment():
    """Verificar que las variables de entorno estén configuradas"""
    log_message("Verificando variables de entorno...", "INFO")
    
    airtable_token = os.getenv('AIRTABLE_TOKEN')
    airtable_base_id = os.getenv('AIRTABLE_BASE_ID')
    
    if not airtable_token:
        log_message("ERROR: AIRTABLE_TOKEN no está configurado", "ERROR")
        log_message("Solución: Añade AIRTABLE_TOKEN como secreto en GitHub", "ERROR")
        return False
        
    if not airtable_base_id:
        log_message("ERROR: AIRTABLE_BASE_ID no está configurado", "ERROR")
        log_message("Solución: Añade AIRTABLE_BASE_ID como secreto en GitHub", "ERROR")
        return False
    
    log_message(f"✅ AIRTABLE_TOKEN: {'*' * 10}{airtable_token[-5:]}", "SUCCESS")
    log_message(f"✅ AIRTABLE_BASE_ID: {airtable_base_id}", "SUCCESS")
    return True

def fetch_airtable_metadata():
    """Obtener metadata de Airtable"""
    airtable_token = os.getenv('AIRTABLE_TOKEN')
    airtable_base_id = os.getenv('AIRTABLE_BASE_ID')
    
    url = f"https://api.airtable.com/v0/meta/bases/{airtable_base_id}/tables"
    headers = {"Authorization": f"Bearer {airtable_token}"}
    
    log_message(f"Conectando a Airtable API...", "INFO")
    log_message(f"URL: {url}", "INFO")
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            log_message("✅ Metadata obtenida exitosamente", "SUCCESS")
            return response.json()
        else:
            log_message(f"❌ Error {response.status_code} de Airtable", "ERROR")
            log_message(f"Respuesta: {response.text[:200]}", "ERROR")
            return None
            
    except requests.exceptions.RequestException as e:
        log_message(f"❌ Error de conexión: {str(e)}", "ERROR")
        return None

def generate_markdown_docs(metadata):
    """Generar documentación en Markdown"""
    if not metadata or 'tables' not in metadata:
        return "# ❌ Error: No se pudo obtener metadata de Airtable"
    
    update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
    
    docs = f"""# 🗂️ Estructura de Base de Airtable

> **Última actualización automática**: {update_time}
> 
> ⚠️ **Este archivo se genera automáticamente. NO EDITAR MANUALMENTE.**

## 📊 Resumen General

"""
    
    # Resumen de tablas
    tables = metadata.get('tables', [])
    total_fields = sum(len(table.get('fields', [])) for table in tables)
    
    docs += f"""
- **Total de tablas**: {len(tables)}
- **Total de campos**: {total_fields}
- **Base ID**: `{os.getenv('AIRTABLE_BASE_ID')}`
- **Actualizado automáticamente**: Diariamente a las 8:00 AM UTC

---

## 📋 Tablas Detalladas

"""
    
    for table in tables:
        table_name = table.get('name', 'Sin nombre')
        table_id = table.get('id', '')
        fields = table.get('fields', [])
        
        docs += f"### 🗃️ {table_name}\n"
        docs += f"*ID: `{table_id}`* | *Campos: {len(fields)}*\n\n"
        
        if not fields:
            docs += "*No hay campos en esta tabla*\n\n"
        else:
            docs += "| Campo | Tipo | Descripción | Opciones |\n"
            docs += "|-------|------|-------------|----------|\n"
            
            for field in fields:
                field_name = field.get('name', 'Sin nombre')
                field_type = field.get('type', 'unknown')
                field_id = field.get('id', '')
                
                # Descripción simple
                type_descriptions = {
                    'singleSelect': 'Selección única',
                    'multipleSelects': 'Selección múltiple',
                    'text': 'Texto',
                    'number': 'Número',
                    'date': 'Fecha',
                    'checkbox': 'Verdadero/Falso',
                    'formula': 'Campo calculado',
                    'rollup': 'Agregación',
                    'lookup': 'Referencia',
                    'url': 'Enlace web',
                    'email': 'Correo electrónico',
                    'phoneNumber': 'Teléfono',
                    'rating': 'Calificación',
                    'attachment': 'Archivo adjunto',
                }
                
                description = type_descriptions.get(field_type, field_type)
                
                # Opciones para campos select
                options = "-"
                if field_type in ['singleSelect', 'multipleSelects']:
                    choices = field.get('options', {}).get('choices', [])
                    if choices:
                        option_names = [f"`{c.get('name')}`" for c in choices[:5]]
                        options = ", ".join(option_names)
                        if len(choices) > 5:
                            options += f" *(+{len(choices)-5} más)*"
                
                docs += f"| **{field_name}**<br>`{field_id}` | `{field_type}` | {description} | {options} |\n"
        
        docs += "\n---\n\n"
    
    # Pie de documento
    docs += f"""
## 🔄 Sobre esta documentación

Esta documentación se genera automáticamente mediante:
1. **GitHub Actions** - Ejecuta diariamente
2. **Airtable API** - Obtiene la estructura actual
3. **Script Python** - Genera este archivo Markdown

### 📅 Historial de actualizaciones
- {update_time} - Actualización automática
- La próxima actualización: Mañana a las 8:00 AM UTC

### 🔧 Solución de problemas
Si esta documentación no se actualiza:
1. Verifica que los secretos de GitHub estén configurados
2. Revisa los logs en GitHub Actions
3. Ejecuta manualmente el workflow

---
*Documentación generada automáticamente - {update_time}*
"""
    
    return docs

def save_documentation(content, filename="database-structure.md"):
    """Guardar documentación en archivo"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Verificar que se escribió correctamente
        import os
        file_size = os.path.getsize(filename)
        line_count = len(content.split('\n'))
        
        log_message(f"✅ Documentación guardada en: {filename}", "SUCCESS")
        log_message(f"   📏 Tamaño: {file_size} bytes", "INFO")
        log_message(f"   📄 Líneas: {line_count}", "INFO")
        
        return True
        
    except Exception as e:
        log_message(f"❌ Error al guardar archivo: {str(e)}", "ERROR")
        return False

def main():
    """Función principal"""
    log_message("=" * 60, "INFO")
    log_message("🚀 INICIANDO SINCRONIZACIÓN AIRTABLE", "INFO")
    log_message("=" * 60, "INFO")
    
    # 1. Verificar entorno
    if not check_environment():
        sys.exit(1)
    
    # 2. Obtener metadata de Airtable
    log_message("\n📡 Obteniendo metadata de Airtable...", "INFO")
    metadata = fetch_airtable_metadata()
    
    if not metadata:
        log_message("❌ No se pudo obtener metadata", "ERROR")
        sys.exit(1)
    
    # 3. Generar documentación
    log_message("\n📝 Generando documentación Markdown...", "INFO")
    documentation = generate_markdown_docs(metadata)
    
    # 4. Guardar archivo
    log_message("\n💾 Guardando archivo...", "INFO")
    if save_documentation(documentation):
        # 5. Mostrar resumen
        tables = metadata.get('tables', [])
        log_message("\n" + "=" * 60, "SUCCESS")
        log_message("🎉 SINCRONIZACIÓN COMPLETADA EXITOSAMENTE", "SUCCESS")
        log_message("=" * 60, "SUCCESS")
        
        log_message("\n📊 RESUMEN FINAL:", "INFO")
        log_message(f"   • Tablas procesadas: {len(tables)}", "INFO")
        
        for i, table in enumerate(tables, 1):
            table_name = table.get('name', f'Tabla {i}')
            field_count = len(table.get('fields', []))
            log_message(f"   {i}. {table_name}: {field_count} campos", "INFO")
        
        log_message(f"\n🕐 Hora de finalización: {datetime.now().strftime('%H:%M:%S')}", "INFO")
        log_message("✅ Listo para commit en GitHub", "SUCCESS")
        
        return True
    else:
        log_message("❌ Error en el proceso", "ERROR")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

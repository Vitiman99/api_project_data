import json

# Cargar el archivo JSON desde tu PC
with open('flattened_data1.json', 'r') as file:
    json_data = json.load(file)

# Lista para almacenar los proyectos aplanados
projects_flattened = []

# Función recursiva para aplanar los atributos del proyecto
def flatten_project(project, flattened):
    flattened_project = {
        'id': project.get('id', -1),
        'name': project.get('name', ''),
        'identifier': project.get('identifier', ''),
        'description': project.get('description', ''),
        'status': project.get('status', -1),
        'is_public': project.get('is_public', False),
        'inherit_members': project.get('inherit_members', False),
        'created_on': project.get('created_on', ''),
        'updated_on': project.get('updated_on', ''),
        'custom_fields_id': project.get('custom_fields_id', -1),
        'custom_fields_name': project.get('custom_fields_name', ''),
        'custom_fields_value': project.get('custom_fields_value', ''),
        'parent_id': project.get('parent_id', -1),
        'parent_name': project.get('parent_name', '')
    }
    flattened.append(flattened_project)

# Aplanar cada proyecto en el JSON
for project in json_data:
    flatten_project(project, projects_flattened)

# Guardar el JSON aplanado en otro archivo
with open('flattenedProjectData.json', 'w') as file:
    json.dump(projects_flattened, file, indent=4)

print(projects_flattened)
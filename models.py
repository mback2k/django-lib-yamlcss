import django.template
if not django.template.libraries.get('yamlcss.filters', None):
    django.template.add_to_builtins('yamlcss.filters')
if not django.template.libraries.get('yamlcss.tags', None):
    django.template.add_to_builtins('yamlcss.tags')

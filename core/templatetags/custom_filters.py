from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, "")

@register.filter
def endswith(value, suffix):
    return str(value).lower().endswith(suffix.lower())

@register.filter
def is_pdf(file):
    return file.name.lower().endswith('.pdf')

@property
def thumbnail_url(self):
    return self.get_or_generate_thumbnail()

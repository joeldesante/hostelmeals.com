import datetime
from django import template

register = template.Library()

@register.simple_tag
def display_published_or_updated(published_date, updated_date):
    
    published_date = published_date.replace(microsecond=0)
    updated_date = updated_date.replace(microsecond=0)
    
    if published_date == updated_date:
        return "Published on " + published_date.strftime("%B %d, %Y")
    else:
        return "Updated on " + updated_date.strftime("%B %d, %Y")
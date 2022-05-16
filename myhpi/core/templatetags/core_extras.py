from django import template

register = template.Library()

# logic for this was moved to context.py

# @register.filter
# def menu_children(page):
#    return page.get_children().in_menu().specific()

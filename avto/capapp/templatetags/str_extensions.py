from django import template

register = template.Library()

def capitalize(inputstr):
    return inputstr.capitalize()

register.filter('capitalize', capitalize)
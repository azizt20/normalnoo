from django import template

register = template.Library()

@register.filter()
def leng(value):
    return len(value)/2

@register.filter()
def cost(value):
    return value*1000000

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()




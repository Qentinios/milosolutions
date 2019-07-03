from datetime import datetime

from django import template

register = template.Library()


@register.simple_tag
def eligibletag(date):
    if date and datetime.today().year-date.year > 13:
        return 'allowed'
    return 'blocked'


@register.simple_tag
def bizzfuzztag(value):
    bizzfuzz = ''
    if value % 3 == 0:
        bizzfuzz = 'Bizz'

    if value % 5 == 0:
        bizzfuzz += 'Fuzz'

    return bizzfuzz
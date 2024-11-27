from django import template
register = template.Library()

@register.filter(name='split')
def split(list_, split_size):
    split_result = []
    split_temp = []
    i = 0

    for item in list_:
        split_temp.append(item)
        i += 1

        if i == split_size:
            yield split_temp
            split_temp = []
            i = 0
    yield split_temp


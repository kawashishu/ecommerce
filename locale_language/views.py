from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

def home(request):
    trans = _('hello')
    return render(request, 'translate.html', {'trans': trans})

def item(request):
    trans = _('hello')
    return render(request, 'item.html', {'trans': trans})

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text
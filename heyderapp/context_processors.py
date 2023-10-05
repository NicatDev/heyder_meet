from heyderapp.models import *

def extras(request):
    context={}
    context['general_settings'] = GeneralSettings.objects.all()

    return context
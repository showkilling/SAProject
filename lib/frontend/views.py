from django.conf import settings
from django.template import Context
from django.views.generic.base import TemplateView

from lib.frontend.api import get_api_data

class FeTemplateView(TemplateView):
    '''
    A view with more convience request data from api.
    '''

    context_data = {} # data use for context
    context = None

    def __init__(self, *args, **kwargs):
        self.context = self.__get_default_context__()

    def get_data(self, request, url, method, data, obj_name):
        self.context_data[obj_name] = get_api_data(request.user.username, url, method, data)  
        self.context.update(self.context_data)               
                
    def __get_default_context__(self):
        default_context_data = Context()
        default_context_data['ENVIRONMENT'] = settings.FRONT_END['ENVIRONMENT']
        return default_context_data
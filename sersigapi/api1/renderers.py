from rest_framework import renderers
import json

class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'
    
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = {}
        if isinstance(data, dict) and 'errors' in data:
            response = {'errors': data['errors']}
        elif isinstance(data, dict) and 'detail' in data:
            response = {'errors': data['detail']}
        else:
            response = data
        return json.dumps(response, ensure_ascii=False)

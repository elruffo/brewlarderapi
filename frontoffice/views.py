from django.shortcuts import render_to_response
from django.template import RequestContext


# ===========================================================================
# HOME
# ===========================================================================
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def home(request, template_name="frontoffice/home.html"):
    return render_to_response(template_name, {
        'session': request.session.keys(),
    }, context_instance=RequestContext(request))


# ===========================================================================
# API
# ===========================================================================
@api_view(['GET'])
def search_beer(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        data = {
            'test_search': 1,
        }
        return Response(data, status=status.HTTP_200_OK)

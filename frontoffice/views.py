from brewlarderapi.settings import BREWERYDB_API_KEY
from django.shortcuts import render_to_response
from django.template import RequestContext
from brewerydb import *
import os
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# ===========================================================================
# HOME
# ===========================================================================
def home(request, template_name="frontoffice/home.html"):
    return render_to_response(template_name, {
        'session': request.session.keys(),
    }, context_instance=RequestContext(request))


# ===========================================================================
# API
# ===========================================================================
@api_view(['GET'])
def search(request):
    bd_type = request.GET.get('type')
    bd_query = request.GET.get('q')

    if bd_type not in ['beer', 'brewery', ]:
        return Response({"error": "Bad Request: invalid type in GET request"},
                        status=status.HTTP_400_BAD_REQUEST)

    if not request.method == 'GET' or not bd_query or not bd_type:
        return Response({"error": "Bad Request: verify you provided both type and query string to the GET request"},
                        status=status.HTTP_400_BAD_REQUEST)

    BreweryDb.configure(BREWERYDB_API_KEY)
    beers = BreweryDb.search({'type': bd_type, 'q': bd_query, })

    return Response(beers, status=status.HTTP_200_OK)

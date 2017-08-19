from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as a function',
            'It is similar to traditional Django view',
            'Gives you the msot control over your logic',
            'It is mapped manually to URLs'
        ]

        return Response({'message':"hello!", 'an_apiview':an_apiview})

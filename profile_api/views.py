from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Hello api view"""
    def get(self, request, format=None):
        api_view = ['Hello world', 'Hello You']
        apiResponse = {'message': 'Hello APi View', 'apiView': api_view}
        return Response(apiResponse)

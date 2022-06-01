from email import message
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = """
            You're done!
            """
            return Response(message)
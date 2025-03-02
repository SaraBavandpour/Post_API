from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from .serializer import UserProfileSerializer

class GetAllUsersView(APIView):

    #def get(self, request):
        #users = UserProfile.objects.all()
        #serializer = UserProfileSerializer(users, many=True)
        #return Response(serializer.data)

    def post(self, request):
        age = request.data.get('age', None)
        if age is not None:
            all_users = UserProfile.objects.filter(age=age)
            serializer = UserProfileSerializer(all_users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Age is required"}, status=status.HTTP_400_BAD_REQUEST)
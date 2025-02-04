from rest_framework.views import APIView
from .serializers import actorSerializers
from .models import Actor
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ActorsList(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        serialize = actorSerializers(actors, many=True)
        return Response(serialize.data)
    
    def post(self, request):
        serializer = actorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ActorByID(APIView):
    def get_object(self, pk):
        return Actor.objects.get(pk=pk)
    
    def get(self, request, pk):
        actor_obj = self.get_object(pk)
        serialize_obj = actorSerializers(actor_obj)
        return Response(serialize_obj.data)
    
    def put(self, request, pk):
        actor_obj = self.get_object(pk)
        serialize_obj = actorSerializers(actor_obj, data=request.data)
        if serialize_obj.is_valid():
            serialize_obj.save()
            return Response(serialize_obj.data, status=status.HTTP_200_OK)
        return Response(serialize_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        actor_obj = self.get_object(pk)
        actor_obj.delete()
        return Response(status=status.HTTP_200_OK)
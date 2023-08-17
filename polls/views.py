from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Poll
from .serializers import PollSerializer

# Create your views here.


class PollView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            serializers = PollSerializer(Poll.objects.all(), many=True)
            response = {"polls": serializers.data}
            return Response(response, status=status.HTTP_200_OK)

        else:
            poll = get_object_or_404(Poll.objects, id=pk)
            serializer = PollSerializer(poll)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(Self, request, format=None):
        data = request.data
        serializer = PollSerializer(data=data)
        if serializer.is_valid():
            poll = serializer.save()
            response = serializer.data
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        serializer = PollSerializer()  # Instantiate serializer

        try:
            poll = Poll.objects.get(pk=pk)
        except Poll.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PollSerializer(poll, data=request.data)

        if serializer.is_valid():
            updated_poll = serializer.save()
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            poll = Poll.objects.get(pk=pk)
        except Poll.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        poll.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

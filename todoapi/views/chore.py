"""View module for handling requests about chores"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers


class ChoreView(ViewSet):
    """To-Do Chores"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized chore instance
        """
        user = User.objects.get(user=request.auth.user)

        chore = Chore()
        chore.title = request.data["title"]
        chore.description = request.data["description"]
        chore.user = user

        weekday = Weekday.objects.get(pk=request.data["weekdayId"])
        chore.weekday = weekday

    def retrieve(self, request, pk=None):
        """Handle GET requests for single chore

        Returns:
            Response -- JSON serialized chore instance
        """
        try:
            chore = Chore.objects.get(pk=pk)
            serializer = ChoreSerializer(chore, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

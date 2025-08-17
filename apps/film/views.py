from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.film.models import Film
from apps.film.serializers import FilmSerializer


class FilmListView(APIView):
    def get(self, request):
        try:
            films = Film.objects.all()
            return Response(FilmSerializer(films,many=True).data)
        except Film.DoesNotExist:
            return Response(
                {
                    "message": "NOT FOUND",
                    "status": 400
                },
                status=status.HTTP_400_BAD_REQUEST
            )



from rest_framework import generics
from .models import Verse
from .serializers import VerseSerializer

class VerseList(generics.ListAPIView):
    queryset = Verse.objects.all()
    serializer_class = VerseSerializer
        
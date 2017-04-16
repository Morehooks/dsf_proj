from rest_framework import generics
from .models import Question
from .serializers import QuestionSerializer
import django_filters


class QuestionFilter(django_filters.FilterSet):
    class Meta:
        model = Question
        fields = ['page_seq', 'question_seq']


class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('page_seq', 'question_seq')

# from django.shortcuts import render
# from django.http import Http404

from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from rest_framework import generics
from polls.models import Question, Choice
from polls.serializers import QuestionSerializer, ChoiceSerializer



def index(request):
    question_list = Question.objects.all()
    output = ' !!!!! '.join([q.question_text for q in question_list])
    return HttpResponse(output)

def index_other(request):
    return HttpResponse("Hello, OTHER world. You're at the polls index.")


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = QuestionSerializer

    def get_object(self):
        obj = get_object_or_404(Question, pk=self.kwargs.get('question_id'))
        return obj


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = ChoiceSerializer

    def get_object(self):
        obj = get_object_or_404(Choice, pk=self.kwargs.get('choice_id'))

        return obj


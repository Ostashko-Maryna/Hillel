# from django.shortcuts import render
from polls.models import Question#, Choice
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return HttpResponse("You're looking at question: {}.".format(question))

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	# print(dir(question))
	# choices = Choice.objects.filter(question=question)
	choises = question.choices.all()
	output = ', '.join([str(c) for c in choises])
	return HttpResponse(output)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def vote_user(request, question_id, user_id):
    return HttpResponse("You're voting on question {} for user {}.".format(question_id, user_id) )


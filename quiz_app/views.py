# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User

from quiz_app.models import Question, Answer, Tenant

class DashboardView(View):

	def get(self, request):
		total_users = User.objects.all().count()
		total_answers = Answer.objects.all().count()
		total_questions = Question.objects.all().count()
		tenants = Tenant.objects.all()
		return render(request, "dashboard.html", {'total_users': total_users,
												  'total_answers': total_answers,
												  'total_questions': total_questions,
												  'tenants': tenants})
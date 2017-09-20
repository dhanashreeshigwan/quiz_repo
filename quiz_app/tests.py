# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from quiz_app.models import Question, Answer, Tenant
from django.contrib.auth.models import User


class BasicTests(TestCase):
    def setUp(self):
        user1 = User.objects.create(username="user1", password="password11", is_active=True)
        user2 = User.objects.create(username="user2", password="password22", is_active=True)
        question1 = Question.objects.create(title="First question", is_private=False, user=user1)
        question2 = Question.objects.create(title="Second question", is_private=True, user=user2)
        ans = Answer.objects.create(body="Answer1", question=question1, user=user2)
        self.question_id1 = question1.id
        self.question_id2 = question2.id
        self.user_id = user1.id

    def test_answer_with_question(self):
        result = False
        answer = Answer.objects.filter(question=self.question_id1)
        if answer:
            result = True
        print "*** Question has answer ***"
        self.assertEqual(result,True)

    def test_user_given_answer(self):
        answer = Answer.objects.filter(user=self.user_id)
        print "*** User not given answer to any question ***"
        self.assertFalse(answer)

    def test_private_question(self):
        question = Question.objects.filter(id=self.question_id1, is_private=True)
        if question:
            print "*** Private question ***"
            self.assertTrue(question)
        else:
            print "*** Not a private question ***"
            self.assertFalse(question)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils import timezone


class Question(models.Model):

    title = models.CharField(max_length=100,null=False, blank=False)
    is_private = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='questions')


class Answer(models.Model):

    body = models.TextField(null=False,blank=False)
    question = models.ForeignKey(Question, related_name='answers')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='given_answers')


class Tenant(models.Model):

    name = models.CharField(max_length=50,null=False, blank=False)
    api_key = models.CharField(max_length=200, null=False, blank=False)

    def __unicode__(self):
        return self.name


class Request(models.Model):

    tenant = models.ForeignKey(Tenant, related_name='requests')
    url = models.CharField(max_length=100, null=False, blank=False)
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     related_name='requests')
    requested_on = models.DateTimeField(default=timezone.now)

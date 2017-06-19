# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class post(models.Model):
    #Set the author field to be constrained to a key from another table that has the authenticated username
    author = models.ForeignKey('auth.User')
    #Set the title field to a character field with the max length of 200 characters
    title = models.CharField(max_length=200)
    # set the text to the text field type
    text = models.TextField()
    # set created_date to the current time using the datetimefield method
    created_date = models.DateTimeField(default=timezone.now)
    # set the published_date to the current time using the datetimefield method
    published_date = models.DateTimeField(blank=True, null=True)

    # create a function that takes a "self" meaning the "caller" and sets that model to the current time
    # this will be called when the form is submitted
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

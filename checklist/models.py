""" 
Contains models for ToDo lists and sublist management. 
"""


from django.db import models
import datetime

"""
Checklist is a table
Step is a table. 
"""

class Checklist(models.Model):
    """
    Encapsulate multiple steps that constitute the completion of a procedure. 
    """
    title = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    ordering = models.IntegerField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['ordering']


class Step(models.Model):
    """
    Items to do, tasks to complete; A single item in a To Do list.
    Used code from a tutorial by James Bennett at sitepoint.com.

    """

    PRIORITY_CHOICES = (
        (1, 'Low'),
        (2, 'Normal'),
        (3, 'High'),
    )
    checklist = models.ForeignKey(Checklist, related_name="steps")    #related_name allows for reverse lookup from 1 to Many
    title = models.CharField(max_length=250)
    ordering = models.PositiveSmallIntegerField()
    created_date = models.DateTimeField(default=datetime.datetime.now)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    tag = models.CharField(max_length=1024)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)


    def complete(self):
        """
        Convenience method for completing a Step. 
        """
        self.completed = True

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['ordering']

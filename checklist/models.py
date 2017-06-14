from django.db import models

import datetime


class ListItem(models.Model):
    """
    Items to do, tasks to complete; A single item in a To Do list.
    Used code from a tutorial by James Bennett at sitepoint.com.

    """

    PRIORITY_CHOICES = (
        (1, 'Low'),
        (2, 'Normal'),
        (3, 'High'),
    )

    title = models.CharField(maxlength=250)
    created_date = models.DateTimeField(default=datetime.datetime.now)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-priority', 'title']

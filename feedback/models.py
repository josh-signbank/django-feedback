from django.db import models


class SubmitFeedback(models.Model):
    your_name = models.CharField(max_length=100,)
    your_feedback = models.TextField()
    your_email = models.EmailField(blank=True)
    your_file = models.FileField(blank=True)
    date = models.DateTimeField()
    your_subject = models.CharField(max_length=25,)
       
    has_been_read = models.BooleanField(default=False)

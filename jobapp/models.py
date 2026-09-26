from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    salary = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=200)

    email = models.EmailField()

    resume = models.FileField(
        upload_to='resumes/'
    )

    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Shortlisted', 'Shortlisted'),
            ('Rejected', 'Rejected'),
        ],
        default='Pending'
    )

    def __str__(self):
        return self.name
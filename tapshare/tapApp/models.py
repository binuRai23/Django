from django.db import models

class File(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class CodeSnippet(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

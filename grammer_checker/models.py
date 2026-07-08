from django.db import models
from django.contrib.auth.models import User


class Grammer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    input=models.TextField()
    corrected_text=models.TextField(null=True)
    mistakes=models.JSONField(null=True)
    explanation=models.JSONField(null=True)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name
    

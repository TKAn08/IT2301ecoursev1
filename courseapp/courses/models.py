from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class BaseView(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Category(BaseView):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

class Course(BaseView):
    subject = models.CharField(max_length=255, null=False)
    description = models.TextField()
    image = models.CharField(max_length=100, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
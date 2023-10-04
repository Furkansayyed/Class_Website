from django.db import models
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=123)
    is_finished = models.BooleanField(default=False)


    def __str__(self):
        return self.title

class ModelCategory(models.Model):
    category = models.CharField(max_length=100)
    description = models.TextField()
    preview_img = models.ImageField(upload_to="preview_image")

    def __str__(self) -> str:
        return self.category

class PhysicsModels(models.Model):
    category = models.ForeignKey(ModelCategory,  on_delete=models.CASCADE)
    title = models.CharField(max_length=150, default="Physics Model")
    img_3d = models.FileField(upload_to="3d_images")

    def __str__(self) -> str:
        return str(self.category)
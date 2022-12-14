from django.db import models

# Create your models here.
class Task(models.Model):
    task_name=models.CharField(max_length=100)
    task_desc=models.CharField(max_length=300)
    date=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    image=models.ImageField(upload_to='image/',default='image/none.jpg')
    
    def __str__(self):
        return self.task_name
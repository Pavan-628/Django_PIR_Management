from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Project(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('not_started', 'Not Started'),
    ]
        
    project_number = models.CharField(max_length=100, unique=True)
    project_title = models.CharField(max_length=200)
    project_leader = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    scope_of_work = models.TextField()
    approved_hours = models.IntegerField()
    product_number = models.CharField(max_length=100)
    trigger = models.CharField(max_length=200)
    client_name = models.CharField(max_length=200)
    status= models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
    
    
    def save(self, *args, **kwargs):
        # Custom save logic goes here
        # For example, you can add logging or data validation
        super(Project, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.project_title


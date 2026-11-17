from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Service(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to="projects/", blank=True)
    is_published=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class ContactRequest(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(blank=False)
    phone=models.CharField(max_length=20, blank=False)
    message=models.TextField(blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    is_read=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class SiteSettings(models.Model):
    company_name=models.CharField(max_length=100)
    tagline=models.CharField(max_length=200, blank=True)
    logo=models.ImageField(upload_to="logos/", blank=True)
    about=models.TextField(blank=False)
    email=models.EmailField(blank=False)
    phone=models.CharField(max_length=20, blank=False)
    address=models.CharField(max_length=255, blank=True)
    whatsapp=models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return self.company_name
    
class Testimonial(models.Model):
    client_name=models.CharField(max_length=50)
    company=models.CharField(max_length=100)
    text=models.TextField(blank=False)
    rating=models.PositiveSmallIntegerField(default=5,validators=[MinValueValidator(1),MaxValueValidator(5),])
    is_published=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.client_name
    
class FAQ(models.Model):
    question=models.TextField(blank=False)
    answer=models.TextField(blank=False)
    order=models.PositiveIntegerField(default=0)
    is_active=models.BooleanField(default=True)
    
    class Meta:
         ordering = ["order"]
    
    def __str__(self):
        return self.question
    
    
from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class About(models.Model):
    bio = models.TextField()
    photo = models.ImageField(upload_to='about_photos/', blank=True, null=True)
    cv = models.FileField(upload_to='about_cvs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Skill(models.Model):
    skill = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Qualification(models.Model):
    diploma = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

class Service(models.Model):
    service = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Testimonial(models.Model):
    author = models.CharField(max_length=255)
    testimonial = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

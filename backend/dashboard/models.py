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
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    profession = models.CharField(max_length=255, default='')
    years_experience = models.IntegerField(default=0)
    completed_projects = models.IntegerField(default=0)
    address = models.TextField(default='')
    email = models.EmailField(default='')
    phone = models.CharField(max_length=20, default='')
    company_name = models.CharField(max_length=255, default='')
    bio = models.TextField(default='')
    photo = models.ImageField(upload_to='about_photos/', blank=True, null=True)
    cv = models.FileField(upload_to='about_cvs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Skill(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]
    
    skill = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')
    years_experience = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.skill} - {self.get_level_display()}"

class Qualification(models.Model):
    QUALIFICATION_TYPES = [
        ('education', 'Education'),
        ('work', 'Work'),
    ]
    
    type = models.CharField(max_length=20, choices=QUALIFICATION_TYPES, default='education')
    diploma = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.diploma} - {self.institution}"

class Service(models.Model):
    service = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Testimonial(models.Model):
    author = models.CharField(max_length=255)
    testimonial = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

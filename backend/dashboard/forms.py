from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Portfolio, About, Skill, Qualification, Service, Testimonial

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username or len(username) < 3:
            raise forms.ValidationError("Le nom d'utilisateur doit contenir au moins 3 caractères.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email or '@' not in email:
            raise forms.ValidationError("Veuillez entrer une adresse email valide.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and len(password1) < 6:
            self.add_error('password1', "Le mot de passe doit contenir au moins 6 caractères.")
        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Les mots de passe ne correspondent pas.")
        return cleaned_data

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'url', 'description', 'image']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title or len(title) < 3:
            raise forms.ValidationError("Le titre doit contenir au moins 3 caractères.")
        return title

    def clean_url(self):
        url = self.cleaned_data.get('url')
        if url and not url.startswith('http'):
            raise forms.ValidationError("Le lien doit commencer par http ou https.")
        return url

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description or len(description) < 10:
            raise forms.ValidationError("La description doit contenir au moins 10 caractères.")
        return description

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError("L'image du projet est requise.")
        return image

# Example AboutForm
class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['bio', 'photo', 'cv']

# Example SkillsForm
class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill', 'level']

# Example QualificationsForm
class QualificationsForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = ['diploma', 'institution', 'year']

# Example ServicesForm
class ServicesForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service', 'description']

# Example TestimonialsForm
class TestimonialsForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['author', 'testimonial'] 
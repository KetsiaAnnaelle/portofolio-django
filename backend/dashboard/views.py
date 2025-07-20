from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.models import User
from .forms import PortfolioForm, RegisterForm, AboutForm, SkillsForm, QualificationsForm, ServicesForm, TestimonialsForm
from .models import Portfolio, About, Skill, Qualification, Service, Testimonial
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.forms.models import model_to_dict

# Create your views here.

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

@csrf_exempt
def api_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def api_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Stateless: do NOT call login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': {'__all__': ['Nom d’utilisateur ou mot de passe incorrect.']}}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def api_about(request):
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            about = form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    elif request.method == 'GET':
        abouts = About.objects.all().order_by('-created_at')
        data = []
        for a in abouts:
            d = model_to_dict(a)
            if a.photo:
                d['photo'] = request.build_absolute_uri(a.photo.url)
            if a.cv:
                d['cv'] = request.build_absolute_uri(a.cv.url)
            data.append(d)
        return JsonResponse({'success': True, 'data': data})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def api_portfolio(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    elif request.method == 'GET':
        portfolios = Portfolio.objects.all().order_by('-created_at')
        data = []
        for p in portfolios:
            d = model_to_dict(p)
            if p.image:
                d['image'] = p.image.url
            data.append(d)
        return JsonResponse({'success': True, 'data': data})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def api_skills(request):
    if request.method == 'POST':
        form = SkillsForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    elif request.method == 'GET':
        skills = Skill.objects.all().order_by('-created_at')
        data = [model_to_dict(s) for s in skills]
        return JsonResponse({'success': True, 'data': data})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def api_qualifications(request):
    if request.method == 'POST':
        form = QualificationsForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    elif request.method == 'GET':
        qualifications = Qualification.objects.all().order_by('-created_at')
        data = [model_to_dict(q) for q in qualifications]
        return JsonResponse({'success': True, 'data': data})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def api_services(request):
    if request.method == 'POST':
        form = ServicesForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    elif request.method == 'GET':
        services = Service.objects.all().order_by('-created_at')
        data = [model_to_dict(s) for s in services]
        return JsonResponse({'success': True, 'data': data})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def api_testimonials(request):
    if request.method == 'POST':
        form = TestimonialsForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    elif request.method == 'GET':
        testimonials = Testimonial.objects.all().order_by('-created_at')
        data = [model_to_dict(t) for t in testimonials]
        return JsonResponse({'success': True, 'data': data})
    return JsonResponse({'error': 'Invalid method'}, status=405)

def logout_view(request):
    logout(request)
    return redirect('login')

#@login_required
def dashboard_home(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard_home')
    else:
        form = PortfolioForm()
    portfolios = Portfolio.objects.all().order_by('-created_at')
    return render(request, 'dashboard_home.html', {'form': form, 'portfolios': portfolios})

def public_index(request):
    portfolios = Portfolio.objects.all().order_by('-created_at')
    return render(request, 'public_index.html', {'portfolios': portfolios})
 
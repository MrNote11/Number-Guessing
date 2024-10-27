from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm, WordInputForm, YourForm  # Ensure this form can handle numbers
from .utils import generate_number_grid
from .models import Number, Profile, Achievement
import random

def home(request):
    message = ''
    grid_size = 10
    # Fetch a random number from the database
    number_of_the_day = Number.objects.order_by('?').first()  # Corrected the name from word_of_the_day

    if request.method == 'POST':
        form = YourForm(request.POST)
        if form.is_valid():
            difficulty = form.cleaned_data['difficulty']
            number_input = form.cleaned_data['number']  # Assuming form handles number input

            # Check if the number exists in the Number model
            if Number.objects.filter(value=number_input).exists():
                message = f'Correct! {number_input} is a valid number.'
                request.user.profile.score += 1
                request.user.profile.save()
                check_achievements(request.user.profile)
            else:
                message = f'Sorry, {number_input} is not in the number list.'

            # Adjust grid size based on difficulty
            if difficulty == 'easy':
                grid_size = 8
            elif difficulty == 'medium':
                grid_size = 10
            elif difficulty == 'hard':
                grid_size = 12

        elif 'request_hint' in request.POST:
            # Ensure the Number table has at least one record to avoid potential errors
            count = Number.objects.count()
            if count > 0:
                random_number = Number.objects.all()[random.randint(0, count - 1)]
                message = f'Hint: The number starts with {str(random_number.value)[:2]}...'
            else:
                message = "No numbers available for hints."
    else:
        form = YourForm()

    # Generate the number grid and prepare the context
    grid = generate_number_grid(size=grid_size)

    # Render the home template with all variables passed to the template
    return render(request, 'game/home.html', {
        'grid': grid,
        'form': form,
        'message': message,
        'number_of_the_day': number_of_the_day,
        'time_limit': 120 # Time limit in seconds
    })

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'game/register.html', {'form': form})

def leaderboard(request):
    profiles = Profile.objects.order_by('-score')[:10]
    return render(request, 'game/leaderboard.html', {'profiles': profiles})

def contact_us(request):
    return render(request, 'game/contact_us.html')

def submit_feedback(request):
    message = ''
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        # Process the feedback as needed
        message = "Thank you for your feedback!"
    return render(request, 'game/submit_feedback.html', {'message': message})

def check_achievements(profile):
    achievements = Achievement.objects.all()
    for achievement in achievements:
        if achievement.name == 'Score 10 Points' and profile.score >= 10:
            profile.achievements.add(achievement)
        # Add more achievement checks as needed

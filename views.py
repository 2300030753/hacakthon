from django.contrib.auth.hashers import make_password
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import Feedback


def home(request):
    return render(request, 'eventapp/home.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Additional fields here

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Please choose another one.")
            return render(request, 'eventapp/register.html')

        # Create user if the username is unique
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Account created successfully!")
        return redirect('login')  # Update this with the correct URL name
    return render(request, 'eventapp/register.html')


# View for registration success page
def register_success(request):
    return render(request, 'eventapp/registerSuccess.html')  # Render registerSuccess page

# eventapp/views.py
from django.shortcuts import render

def events_view(request):
    return render(request, 'eventapp/events.html')

from django.shortcuts import render

# Create your views here.
def companies_view(request):
    return render(request, 'eventapp/companies.html')


# views.py
from django.shortcuts import render, redirect
from .forms import BookingForm

def book_event(request, event_name):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'eventapp/booking_success.html', {'event_name': event_name})
    else:
        form = BookingForm(initial={'event_name': event_name})
    return render(request, 'eventapp/book_event.html', {'form': form, 'event_name': event_name})

from django.shortcuts import render

# Contact page view
def contact(request):
    return render(request, 'eventapp/contact.html')
# eventapp/views.py

def loginpagecall(request):
    return render(request,'eventapp/loginpage.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import check_password

def loginpagelogic(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Attempt to get the user by email
        try:
            user = User.objects.get(email=email)

            # Check if the password matches the one stored in the database
            if check_password(password, user.password):
                login(request, user)  # Log the user in
                messages.success(request, 'Login successful!')
                return redirect('home')  # Redirect to home after login
            else:
                messages.error(request, 'Invalid email or password.')
                return redirect('home')  # Redirect back to login page
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
            return redirect('home')  # Redirect back to login page if user doesn't exist

    return render(request, 'eventapp/loginpage.html')

def logoutpagecall(request):
    return render(request, 'eventapp/logout.html')

from django.shortcuts import redirect
from django.contrib import auth

def logoutpagelogic(request):
    auth.logout(request)  # Logs out the user
    return redirect('home')  # Redirect to the homepage or desired URL


from django.shortcuts import render, redirect
from django.contrib import messages

def feedbackpagecall(request):
    return render(request, 'eventapp/feedback.html')
def feedback(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')

        Feedback.objects.create(user=request.user, rating=rating, comments=comments)
        messages.success(request, 'Thank you for your feedback!')
        return redirect('feedback')

    return render(request, 'eventapp/feedback.html')
import matplotlib
import pytz
from django.contrib.auth.models import User
import random
import string
from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib import messages, auth
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.utils import timezone
from datetime import datetime
from datetime import timedelta


def projecthomepage(request):
    return render(request,'adminapp/ProjectHomePage.html')

def pagedivcall(request):
    return render(request,'adminapp/pagediv.html')
# Create your views here.

def pagedivlogic(request):
    if request.method=="POST":
        user_input = request.POST['user_input']
        print(f'user input:{user_input}')
    a1={'user_input':user_input}
    return render(request,'adminapp/pagediv.html',a1)


def exceptionpagecall(request):
    return render(request,'adminapp/ExceptionExample.html')

def exceptionpagelogic(request):
    if request.method=="POST":
        user_input=request.POST['user_input']
        result=None
        error_message=None
        try:
            num=int(user_input)
            result=10/num
        except Exception as e:
            error_message=str(e)
        return render(request,'adminapp/ExceptionExample.html',{'result':result, 'error': error_message})
    return render(request,'adminapp/ExceptionExample.html')


def randompagecall(request):
    return render(request,'adminapp/random.html')

def randompagelogic(request):
    if request.method=="POST":
        n=int(request.POST['n'])
        ran=''.join(random.sample(string.ascii_uppercase+string.digits,k=n))
    a1={'ran':ran}
    return render(request,'adminapp/random.html',a1)

def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'calc/calculator.html', {'result': result})





def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminapp:add_task')

    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'adminapp/add_task.html', {'form': form,'tasks':tasks})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('adminapp:add_task')




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'OOPS! Username already taken.')
                return redirect('adminapp:register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'OOPS! Email already registered.')
                return redirect('adminapp:register')
            else:
                # Create the user and log them in
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request, user)
                messages.success(request, f'Account created for {username}!')
                return redirect('adminapp:projecthomepage')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('adminapp:register')
    else:
        return render(request, 'adminapp/register.html')




def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)  # Make sure to log in the user
            print(f"User {user.username} is logged in.")  # Debugging statement
            # Check the length of the username
            if len(username) == 10:
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:StudentHomePage')  # Update with actual student homepage URL name
            elif len(username) == 4:
                messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:FacultyHomePage')  # Update with actual faculty homepage URL name
            else:
                messages.error(request, 'Username length does not match student or faculty criteria.')
        else:
            messages.error(request, 'Invalid username or password.')

        # Return the login page if any validation or authentication fails
        return render(request, 'adminapp/login.html')

    # Render the login page for GET requests
    return render(request, 'adminapp/login.html')



def log_out(request):
    # Use Django's built-in logout function
    auth.logout(request)
    # Redirect to a specific page after logging out
    return redirect(reverse('adminapp:projecthomepage'))



def get_time_details(request):
    timezones = pytz.all_timezones
    timezone_time = None
    error_message = None
    timezone_name = None

    if request.method == 'POST':
        timezone_name = request.POST.get('timezone')
        try:
            # Get the current time in UTC
            utc_now = datetime.utcnow()

            # Convert UTC time to the selected timezone
            selected_timezone = pytz.timezone(timezone_name)
            timezone_time = utc_now.replace(tzinfo=pytz.utc).astimezone(selected_timezone)

            # Format the timezone_time for better readability (optional)
            timezone_time = timezone_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')

        except pytz.UnknownTimeZoneError:
            error_message = "Invalid timezone selected. Please select a valid timezone."
        except Exception as e:
            error_message = f"An unexpected error occurred: {str(e)}"

    return render(request, 'adminapp/timezones.html', {
        'timezones': timezones,
        'timezone_time': timezone_time,
        'timezone_name': timezone_name,
        'error_message': error_message,
    })

def calculate_future_date(request):
    future_date = None
    if request.method == "POST":
        days_input = int(request.POST.get('days_input'))
        # Add the number of days to the current date
        current_time = timezone.now()
        future_date = current_time + timedelta(days=days_input)

    return render(request, 'adminapp/calculate_future_date.html', {
        'future_date': future_date
    })


from .forms import StudentForm
from .forms import StudentList

# def add_student(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('adminapp:student_list')
#     else:
#         form = StudentForm()
#     return render(request, 'adminapp/add_student.html', {'form': form})

from django.contrib.auth.models import User
from .models import StudentList
from .forms import StudentForm
from django.shortcuts import redirect, render
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                student.user = user  # Assign the matching User to the student
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'adminapp/add_student.html', {'form': form})
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form': form})


def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/student_list.html', {'students': students})





import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from django.shortcuts import render
matplotlib.use('Agg')

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        # Read the CSV file
        df = pd.read_csv(file, parse_dates=['Date'], dayfirst=True)

        # Calculate total and average sales
        total_sales = df['Sales'].sum()
        average_sales = df['Sales'].mean()

        # Add a 'Month' column and calculate monthly sales
        df['Month'] = df['Date'].dt.month
        monthly_sales = df.groupby('Month')['Sales'].sum()

        # Month names for labels
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        monthly_sales.index = monthly_sales.index.map(lambda x: month_names[x - 1])

        # Plot the pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(monthly_sales, labels=monthly_sales.index, autopct='%1.1f%%', startangle=90)
        plt.title('Sales Distribution Per Month')

        # Save the plot to a buffer
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        # Convert to base64 to send to the template
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        plt.close()

        # Pass data to the template
        context = {
            'total_sales': total_sales,
            'average_sales': average_sales,
            'monthly_sales': monthly_sales.to_dict(),
            'chart': image_data,
        }
        return render(request, 'adminapp/chart.html', context)

    return render(request, 'adminapp/chart.html')


# contacts/views.py
from django.shortcuts import render, redirect
from .models import Contact
from django.db.models import Q


def contact_list(request):
    query = request.GET.get('q')
    if query:
        contacts = Contact.objects.filter(Q(name__icontains=query) | Q(email__icontains=query))
    else:
        contacts = Contact.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        Contact.objects.create(name=name, email=email, phone=phone, address=address)
        return redirect('contact_list')

    return render(request, 'adminapp/contact_list.html', {'contacts': contacts})


def delete_contact(request, pk):
    Contact.objects.get(id=pk).delete()
    return redirect('adminapp:contact_list')

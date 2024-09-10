
from django.http import HttpResponse,FileResponse, Http404
from .models import Resume

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .github_utils import get_github_repositories, get_github_user

# Create your views here.
def home(request):
    return render(request, "index2.html")

def resume(request):
    return render(request, "resume.html")
def projects(request):
    return render(request, "projects.html")

def download_resume(request):
    try:
        resume = Resume.objects.latest('uploaded_at')
        return FileResponse(resume.file.open('rb'), as_attachment=True, filename='Vansh_Khatri_Resume.pdf')
    except Resume.DoesNotExist:
        raise Http404("Resume not found")
    






def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        subject = f"Contact Form Submission from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        from_email = 'VanshKhatri@sandboxa3de31781d7345ce8ad9bda39e5c72f4.mailgun.org'
        recipient_list = ['khatrivansh43@gmail.com']  # Your email address
        
        try:
            send_mail(subject, body, from_email, recipient_list)
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, "An error occurred. Please try again later.")
        
        return redirect('/')  # Redirect back to the home page or wherever you prefer
    
    return render(request, 'contact.html')





def github_profile(request):
    username = "vanshxo"  # Your GitHub username
    repos = get_github_repositories(username)
    user = get_github_user(username)
    
    context = {
        'user': user,
        'repos': repos
    }
    return render(request, 'github_profile.html', context)
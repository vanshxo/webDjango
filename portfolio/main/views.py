from django.shortcuts import render
from django.http import HttpResponse,FileResponse, Http404
from .models import Resume

# Create your views here.
def home(request):
    return render(request, "index.html")



def download_resume(request):
    try:
        resume = Resume.objects.latest('uploaded_at')
        return FileResponse(resume.file.open('rb'), as_attachment=True, filename='Vansh_Khatri_Resume.pdf')
    except Resume.DoesNotExist:
        raise Http404("Resume not found")
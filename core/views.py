from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('projects:dashboard')
    else:
        return render(request,'core/index.html')

def about(request):
    return render(request,'core/about.html')
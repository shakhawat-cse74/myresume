from django.shortcuts import render

# Create your views here.
def education(request):
    context={'education':'active'}
    return render(request, 'edu/education.html', context)
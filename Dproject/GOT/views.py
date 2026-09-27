from django.shortcuts import render

# Create your views here.
def all_got(request):
    return render(request, 'GOT/all_got.html')
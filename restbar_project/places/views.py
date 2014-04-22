from django.shortcuts import render, render_to_response

def home(request):
    # return render('index.html')
    return render_to_response('index.html')


# Create your views here.
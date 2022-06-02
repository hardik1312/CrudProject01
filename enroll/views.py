from django.shortcuts import render

# Create your views here.
def add_show(requests):
    return render(requests, 'enroll/addandshow.html')
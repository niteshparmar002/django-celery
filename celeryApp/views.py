from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse  
# importing task from tasks.py file  
from .tasks import test_func  
  
# Create your views here.  
  
def test(request):  
    # call the test_function using delay, calling task  
    test_func.delay()  
    return HttpResponse("Done")  
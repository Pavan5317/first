from django.shortcuts import render
from  django.http import  HttpResponse
# Create your views here.
def welcome(request):
    return HttpResponse("""<html><body bgcolor=gray><h1><center>Welcome to my new website</center></h1></body></html>""")
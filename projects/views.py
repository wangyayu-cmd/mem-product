from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("大家好，我叫亚宇")

# def project(request):
#     return HttpResponse("<h1>项目1</>")
def get_project(request):
    return HttpResponse("<h1>获取项目</>")
def create_project(request):
    return HttpResponse("<h1>创建项目</>")
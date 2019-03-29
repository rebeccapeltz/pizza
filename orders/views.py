from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    "menu":["item1", "item2"]
  }
  # return render(request, "orders/index.html", context)
  return HttpResponse("Project 3: TODO")

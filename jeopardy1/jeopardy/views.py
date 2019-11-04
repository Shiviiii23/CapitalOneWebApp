from django.shortcuts import render
import requests
from django.http import HttpResponse
from .forms import SearchForm
from django.views.generic import TemplateView, ListView
import json
from jeopardy.models import Category
from django.core import serializers
from django.db import models
# from models import Category
# int val;
from django.http import JsonResponse

def search(request):
#	SaveCats(request)
	return render(request, 'jeopardy.html', {})


def val(request):
	val = request.GET.get('value') #int returned
	resulturl = "http://jservice.io/api/clues?" + "value=" + val 
	result = requests.get(resulturl) #returns RESPONSE object 
	data = result.json()
	

	yes = json.dumps(data)
	
	#newresult = JsonResponse(result)
	if result.status_code == 200:
		return render(request, 'results.html', context={'val' : yes})
	return HttpResponse(data)



def min2(request):
	val = request.GET.get('min') #int returned
	resulturl = "http://jservice.io/api/clues?" + "min_date=" + val 
	result = requests.get(resulturl) #returns RESPONSE object 
	data = result.json()
	

	yes = json.dumps(data)
	
	#newresult = JsonResponse(result)
	if result.status_code == 200:
		return render(request, 'results.html', context={'val' : yes})
	return HttpResponse(data)






	# def display(request):
	# 	return render(request, 'jeopardy.html', {})
# Create your views here.

# class HomePageView(TemplateView):
# 	template_name = 'home.html'

# class SearchResultViews(ListView):
# 	template_name = 'search_results.html'
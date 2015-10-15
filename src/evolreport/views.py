from django.shortcuts import render
from django.http import HttpResponse
import requests

from .utils import ACKLEY_TEX

# Create your views here.
def index(request):
	context = {
		'page_title':'Evolutives Report',
		'ackley_src': ACKLEY_TEX,
	}
	
	if request.GET.get('fitness-selection'):
		request.session['fitness-selection'] = request.GET.get('fitness-selection')
	else:
		return render(request, 'report.html', context)
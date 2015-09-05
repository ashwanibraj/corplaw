from django.http import HttpResponseRedirect
from django.shortcuts import redirect

def home(request):
	return HttpResponseRedirect('/forum/')

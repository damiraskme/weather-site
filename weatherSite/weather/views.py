from django.shortcuts import render
from django.http import HttpResponse
from .weather import *
from .forms import locForm

def weather(request):
  current = {}
  forecast = {}
  if request.method == 'POST':
      form = locForm(request.POST)
      if form.is_valid():
          location = form.cleaned_data['location']  
          current = current_weather(location)
          forecast = forecast_weather(location)
  else:
    form = locForm()
    
  return render(request, 'weather/weather.html', {
        'form': form,
        'current_weather': current,
        'forecast_weather': forecast,
    })
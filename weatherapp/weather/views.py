import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
	appid = '1fcd611729e1bf0b6b437655669d15af'
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

	#city = 'Kiev'
	if(request.method == 'POST'):
		form = CityForm(request.POST)
		form.save()

	form = CityForm()

	cities = City.objects.all()
	#print(res.text)

	all_cities = []

	for city in cities:
		res = requests.get(url.format(city.name)).json()
		city_info = {
			'city': city.name,
			'temp': res["main"]["temp"],
			'icon': res["weather"][0]["icon"]
		}
		all_cities.append(city_info)

	context = {'all_info': all_cities, 'form': form }

	return render(request, 'weather/index.html', context)
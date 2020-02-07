from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    appid = '82b797b6ebc625032318e16f1b42c016'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    cities = City.objects.all()
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        try:
            city_info = {
                'city': city.name,
                'temp': res["main"]["temp"],
                'humidity': res["main"]["humidity"],
                'wind': res["wind"]["speed"],
                'winde': res["wind"]["deg"],
                'icon': res["weather"][0]["icon"]
            }
            all_cities.append(city_info)
        except KeyError:
            print()


    context = {'all_info': all_cities, 'form': form}
    return render(request, 'pogg/index.html', context)
# Create your  views here.

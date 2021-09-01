import requests
from django.shortcuts import render
from .models import City


# Create your views here.

def index(request):
    # url for the display of the weather added by the admin 
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c77fbdf4c887f4c8840ac496686fa7c4'
 
    city = 'New York'
   # for cities added by admin only
    cities = City.objects.all().order_by('?')
    # if you need to filter and limit the number [:3] , to order by id order_by('id')
    weather_data = []
    #itirate the cities to query the weather
    for city in cities:  
     
        r = requests.get(url.format(city.city_name)).json()

        city_weather = {
            'city' : city.city_name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    
    

     # url for the display of the weather that will not be saved into the database to minimize api request
     #  since it is free subscription with limitations on request

    url2 = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c77fbdf4c887f4c8840ac496686fa7c4'

    
    if request.method  == 'POST':
            city = request.POST.get('city') # or request.Post['city']
            city = city.capitalize()
    p = requests.get(url2.format(city)).json()
    
        

    city_weather_user = {
        'city' : city,
        'temperature' : p['main']['temp'],
        'description' : p['weather'][0]['description'],
        'icon' : p['weather'][0]['icon'],
    }     

    context = {'weather_data': weather_data, 'city_weather_user':city_weather_user}
    print(weather_data , city_weather_user)
    return render(request,'weather/index.html',context)

 
    

#   if request.method  == 'POST':
#             city = request.POST.get('city') # or request.Post['city']
#             new_city = City(city_name=city)
#             new_city.save()
    
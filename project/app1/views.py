from django.shortcuts import render
import urllib.request
import json

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+
                                     '&appid=ad8a600eae0614b391b62745648429a3').read()
        jason_data = json.loads(res)
        data = {
            'country_code':str(jason_data['sys']['country']),
            'coordinate': str(jason_data['coord']['lon'])+"\n"+str(jason_data['coord']['lat']),
            'temp': str(jason_data['main']['temp']),
            'pressure':str(jason_data['main']['pressure']),
            'humidity':str(jason_data['main']['humidity'])
        }
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city':city, 'data':data})
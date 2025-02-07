from django.shortcuts import render
import folium
from folium.plugins import FastMarkerCluster
from core.models import EVChargingLocation
from django.db.models import Avg


# Create your views here.
def index(request):
    avg_lat = EVChargingLocation.objects.aggregate(avg=Avg('latitude'))['avg']
    print(avg_lat)
    # stations = EVChargingLocation.objects.all()

    stations = EVChargingLocation.objects.filter(latitude__gt=avg_lat)

    #Create a folium map centered on Connecticut
    m = folium.Map(location=[41.5025,-72.699997], zoom_start=9)


    #Use FastmarkerCluster to generate the clusters on the map
    latitudes = [station.latitude for station in stations]
    longitudes = [station.longitude for station in stations]

    FastMarkerCluster(data=list(zip(latitudes, longitudes))).add_to(m)

    # #Add a marker to the map for each station
    # for station in stations:
    #     coordinates = (station.latitude, station.longitude)
    #     folium.Marker(coordinates, popup=station.station_name).add_to(m)

    context = {'map': m._repr_html_(),'stations':stations}
    return render(request, 'index.html', context)
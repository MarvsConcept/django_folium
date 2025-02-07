from django.shortcuts import render
import folium
from folium.plugins import FastMarkerCluster
from core.models import EVChargingLocation


# Create your views here.
def index(request):
    stations = EVChargingLocation.objects.all()

    #Create a folium map centered on Connecticut
    m = folium.Map(location=[41.5025,-72.699997], zoom_start=9)


    #Use FastmarkerCluster to generate the clusters on the map
    latitudes = [station.latitude for station in stations]
    longitudes = [station.longitude for station in stations]

    FastMarkerCluster(data=list(zip(latitudes, longitudes))).add_to(m)

    context = {'map': m._repr_html_(),'stations':stations}
    return render(request, 'index.html', context)
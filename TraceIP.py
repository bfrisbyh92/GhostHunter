import requests
from gmplot import *
import webbrowser
from colorama import init, Fore, Style, Back

init(autoreset=True)

R = Fore.RED
G = Fore.GREEN
C = Fore.CYAN
Y = Fore.YELLOW


def read_multiple_ip():
    print(Y + Back.BLACK +
          "Note : This tool requires api key please configure the api key and use it.")
    ip_file = input(G + Back.BLACK + "Enter the file path >>")
    lats = []
    lons = []
    f = open(ip_file, "r")
    f1 = f.readlines()
    for line in f1:
        r = requests.get("http://ip-api.com/json/"+line.strip('\n'))
        resp = r.json()
        if resp['lat'] and resp['lon']:
            lats.append(resp['lat'])
            lons.append(resp['lon'])
    heat_map(lats, lons)


def heat_map(lats, lons):
    gmap3 = gmplot.GoogleMapPlotter(20.5937, 78.9629, 5)
    gmap3.heatmap(lats, lons)
    gmap3.scatter(lats, lons, '#FF0000', size=50, marker=False)

    gmap3.plot(lats, lons, 'cornflowerblue', edge_width=3.0)
    gmap3.apikey = "--Your API KEY--"
    save_location = input(G+"Enter a location to save : ")
    location = save_location + "/heatmap.html"
    gmap3.draw(location)
    print(C+"Heatmap saved at " + location)
    openWeb = input(Y+"Open Heatmap in web broser? (Y/N) : ")
    if openWeb.upper() == 'Y':
        webbrowser.open

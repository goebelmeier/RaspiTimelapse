__author__ = 'theissenbuettel'

import ephem
import time
import subprocess
import sys


## Konfiguration
# Geographische Breite
conf_lat = '53.200493'

# Geographische Laenge
conf_lon = '8.580344'

# Name fuer die Bilderreihe
tl_name = 'Hausbau'

# Kamera Einstellungen (siehe raspistill Manpage fuer genauere Infos)
photo_ex  = 'night'
photo_awb = 'off'

# EV Level.
photo_ev = 1

# Aufloesung und Qualitaet
photo_width  = 1280
photo_height = 720
photo_quality = 75

photo_sharpness = 50
photo_contrast = 10

## Code
location = ephem.Observer()
location.lat = conf_lat
location.lon = conf_lon

print "Aktuelle UTC-Zeit:       ", location.date
print "Letzter Sonnenaufgang:   ", location.previous_rising(ephem.Sun())
print "Letzter Sonnenuntergang: ", location.previous_setting(ephem.Sun())

# Wenn der letzte Sonnenaufgang spaeter war als der letzte Sonnenuntergang, wird es Tag sein
if location.previous_rising(ephem.Sun()) > location.previous_setting(ephem.Sun()):
    print "Es ist im Moment Tag"
else:
    print "Es ist im Moment Nacht"
    sys.exit("Es ist Nacht, kein Foto erstellen")

filename = (tl_name + "_" + time.strftime("%Y-%m-%d-%H-%M"))
print filename

cmd = ('raspistill -t 100 -w ' + str(photo_width) +
    ' -h ' + str(photo_height) +
    ' -q ' + str(photo_quality) +
    ' -sh ' + str(photo_sharpness) +
    ' -co ' + str(photo_contrast) +
    ' -awb ' + photo_awb +
    ' -ev ' + str(photo_ev) +
    ' -ex ' + photo_ex +
    ' -o ' + filename)

#pid = subprocess.call(cmd, shell=True)
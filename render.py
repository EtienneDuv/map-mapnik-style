#!/usr/bin/env python
import mapnik
import datetime

stylesheet = 'style.xml'
image = 'render'
srs="+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs"

m = mapnik.Map(8000, 8000)
mapnik.load_map(m, stylesheet)
m.srs = srs
m.zoom_all() 

now = str(datetime.datetime.now())
now = now[:10] + '-' + now[20:]

mapnik.render_to_file(m, "render/" + image + '-' +now + ".png")
mapnik.render_to_file(m, "render/" + image + '-' +now + ".svg")

print "rendered image to '%s'" % image
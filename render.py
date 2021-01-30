#!/usr/bin/env python
import mapnik

stylesheet = 'style.xml'
image = 'render'
srs="+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs"

m = mapnik.Map(8000, 8000)
mapnik.load_map(m, stylesheet)
m.srs = srs
m.zoom_all() 
mapnik.render_to_file(m, image+".png")
mapnik.render_to_file(m, image+".svg")

print "rendered image to '%s'" % image
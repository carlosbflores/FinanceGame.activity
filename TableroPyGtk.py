#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import operator
import time
import string

class TableroPyGtk:
    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Actividad Educacion Financiera")
        window.resize(1220, 820)
        window.connect("destroy", lambda w: gtk.main_quit())

        self.area = gtk.DrawingArea()
        self.area.set_size_request(1200, 800)

        window.add(self.area)
        self.area.set_events(gtk.gdk.POINTER_MOTION_MASK |
                             gtk.gdk.POINTER_MOTION_HINT_MASK )
        self.area.connect("expose-event", self.drawing_area_expose)

        self.area.show()
        window.show()
 
    def drawing_area_expose(self, area, event):
        self.style = self.area.get_style()
        self.gc = self.style.fg_gc[gtk.STATE_NORMAL]
        self.draw_pixmap(0, 0)
        return True

    def draw_pixmap(self, x, y):

        # gtk.gdk.pixmap_create_from_xpm(window, transparent_color, filename)
        #pixmap, mask = gtk.gdk.pixmap_create_from_xpm(self.area.window, self.style.bg[gtk.STATE_NORMAL], "gtk.xpm")

        # gtk.gdk.Pixmap(drawable, width, height, depth=-1)
        pixmap = gtk.gdk.Pixmap(self.area.window, 1200, 800, -1)

        # tablero
        pixbuf = gtk.gdk.pixbuf_new_from_file('images/tablero.png') #one way to load a pixbuf
        # draw_pixbuf(gc, pixbuf, src_x, src_y, dest_x, dest_y, width=-1, height=-1, dither=gtk.gdk.RGB_DITHER_NORMAL, x_dither=0, y_dither=0)
        pixmap.draw_pixbuf(None, pixbuf, 0, 0, 0, 0, -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)

        # casa del chico
        pixbuf_home = gtk.gdk.pixbuf_new_from_file('images/casa-alpha.png')
        pixmap.draw_pixbuf(None, pixbuf_home, 0, 0, 190, 610, -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)

        # el chico
        pixbuf_home = gtk.gdk.pixbuf_new_from_file('images/chico-alpha-der.png')
        pixmap.draw_pixbuf(None, pixbuf_home, 0, 0, 350, 670, -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)

        # casa de la chica
        pixbuf_home = gtk.gdk.pixbuf_new_from_file('images/casa-alpha.png')
        pixmap.draw_pixbuf(None, pixbuf_home, 0, 0, 920, 610, -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)

        # la chica
        pixbuf_home = gtk.gdk.pixbuf_new_from_file('images/chica-alpha-izq.png')
        pixmap.draw_pixbuf(None, pixbuf_home, 0, 0, 830, 670, -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)

        # el hospital
        pixbuf_home = gtk.gdk.pixbuf_new_from_file('images/hospital-alpha.png')
        pixmap.draw_pixbuf(None, pixbuf_home, 0, 0, 150, 50, -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)

        # el almacen
        pixbuf_home = gtk.gdk.pixbuf_new_from_file('images/almacen-alpha.png')
        pixmap.draw_pixbuf(None, pixbuf_home, 0, 0, 5, 380, -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)

        # el banco
        pixbuf_home = gtk.gdk.pixbuf_new_from_file('images/banco-alpha.png')
        pixmap.draw_pixbuf(None, pixbuf_home, 0, 0, 890, 0, -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)

        # la escuela
        pixbuf_home = gtk.gdk.pixbuf_new_from_file('images/escuela-alpha.png')
        pixmap.draw_pixbuf(None, pixbuf_home, 0, 0, 1020, 150, -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)



        # drawable.draw_drawable(gc, src, xsrc, ysrc, xdest, ydest, width, height)
        self.area.window.draw_drawable(self.gc, pixmap, 0, 0, x+10, y+10, -1, -1)

        #drawable.draw_drawable(gc, src, xsrc, ysrc, xdest, ydest, width, height)
        #drawable.draw_image(gc, image, xsrc, ysrc, xdest, ydest, width, height)

        #self.area.window.drawable.draw_image(self.gc, image, 0, 0, x+15, y+25, -1, -1)

        return

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    TableroPyGtk()
    main()

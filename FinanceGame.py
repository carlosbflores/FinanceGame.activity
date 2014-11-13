from sugar.activity import activity
import logging

import sys, os
import gtk

class FinanceGame(activity.Activity):
    def hello(self, widget, data=None):
        logging.info('Hello World')

    def __init__(self, handle):
        print "running activity init", handle
        activity.Activity.__init__(self, handle)
        print "activity running"

        # Creates the Toolbox. It contains the Activity Toolbar, which is the
        # bar that appears on every Sugar window and contains essential
        # functionalities, such as the 'Collaborate' and 'Close' buttons.

        toolbox = activity.ActivityToolbox(self)
        self.set_toolbox(toolbox)
        toolbox.show()

        # Creates a new button with the label "Hello World".
        self.button = gtk.Button("Hola Finance Game")
    
        # When the button receives the "clicked" signal, it will call the
        # function hello() passing it None as its argument.  The hello()
        # function is defined above.
        self.button.connect("clicked", self.hello, None)
    
        # Set the button to be our canvas. The canvas is the main section of
        # every Sugar Window. It fills all the area below the toolbox.

        #self.set_canvas(self.button)
    
        # The final step is to display this newly created widget.

        #self.button.show()
    
        print "AT END OF THE CLASS"


        self.area = gtk.DrawingArea()
        self.area.set_size_request(1200, 800)

        self.add(self.area)
        self.area.set_events(gtk.gdk.POINTER_MOTION_MASK |
                             gtk.gdk.POINTER_MOTION_HINT_MASK )
        self.area.connect("expose-event", self.drawing_area_expose)

        self.area.show()


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
#	pixmap = gtk.gdk.Pixmap(self.get_window(), 1200, 800, -1)

	pixbuf = gtk.gdk.pixbuf_new_from_file('board.png') #one way to load a pixbuf
	# draw_pixbuf(gc, pixbuf, src_x, src_y, dest_x, dest_y, width=-1, height=-1, dither=gtk.gdk.RGB_DITHER_NORMAL, x_dither=0, y_dither=0)
	pixmap.draw_pixbuf(None, pixbuf, 0, 0, 0, 0, -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)

	# drawable.draw_drawable(gc, src, xsrc, ysrc, xdest, ydest, width, height)
        self.area.window.draw_drawable(self.gc, pixmap, 0, 0, x+15, y+25, -1, -1)
#        self.get_window().draw_drawable(self.gc, pixmap, 0, 0, x+15, y+25, -1, -1)

	#drawable.draw_drawable(gc, src, xsrc, ysrc, xdest, ydest, width, height)
	#drawable.draw_image(gc, image, xsrc, ysrc, xdest, ydest, width, height)


        return



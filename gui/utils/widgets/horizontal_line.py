import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class HorizontalLine(Gtk.DrawingArea):
    def __init__(self):
        super().__init__()

        # Set the size of the drawing area
        self.set_size_request(-1, 1)

    def do_draw(self, cr):
        # Set the line color
        cr.set_source_rgb(0, 0, 0)  # Black color

        # Set the line width
        cr.set_line_width(1)

        padding = 10
        start_x = padding
        end_x = self.get_allocated_width() - padding

        y = self.get_allocated_height() / 2



        # Draw the line
        cr.move_to(start_x, y)
        cr.line_to(end_x, y)
        cr.stroke()

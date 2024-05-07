import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from utils.widgets.horizontal_line import HorizontalLine
from screens.modem.modem_home import ModemWindow


class MyApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Deku Linux App")

        self.connect("destroy", Gtk.main_quit)
        self.set_default_size(800, 600)

        # Create the main container
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.add(main_box)

        # Create the navigation bar
        nav_bar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        nav_bar.set_size_request(-1, 50)
        nav_bar.set_homogeneous(False)
        # nav_bar.set_border_width(10)
        nav_bar.set_name("nav-bar")  # Set the CSS class name

        main_box.pack_start(nav_bar, False, False, 0)

        # Create a box for the left side of the navigation bar
        left_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        left_box.set_homogeneous(True)
        nav_bar.pack_start(left_box, False, False, 0)

        # Adjusting navbar
        title_label = Gtk.Label()
        title_label.set_text("Deku Linux")
        title_label.set_name("title-label")  # Set a custom CSS name for the label
        left_box.pack_start(title_label, False, False, 20)

        # Create a box for the right side of the navigation bar
        right_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        right_box.set_homogeneous(True)
        nav_bar.pack_end(right_box, False, False, 0)

        # icon
        nav_icon = Gtk.Image.new_from_icon_name("preferences-system-symbolic", Gtk.IconSize.SMALL_TOOLBAR)
        right_box.pack_end(nav_icon, False, False, 20)

        # Horizontal line widget
        line = HorizontalLine()
        main_box.pack_end(line, False, False, 0)

        # Container 2
        container2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        container2.set_vexpand(True)
        container2.set_homogeneous(False)
        container2.set_border_width(10)

        # Event box
        event_box = Gtk.EventBox()
        event_box.connect("button-press-event", self.on_modem_1_click)
        container2.pack_start(event_box, False, False, 0)

        # text box
        modem_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        container2.pack_start(modem_container, False, False, 0)

        # modem text
        modem_1 = Gtk.Label()
        modem_1.set_text("Modem MTN 4.2")
        modem_1.set_name("modem_label")
        event_box.add(modem_1)
        modem_container.pack_start(modem_1, False, False, 0)

        modem_2 = Gtk.Label()
        modem_2.set_text("Modem Orange 33")
        modem_2.set_name("modem_label")
        modem_container.pack_end(modem_2, False, False, 0)

        main_box.pack_end(container2, True, True, 0)

        # # Horizontal line widget
        line = HorizontalLine()
        main_box.pack_end(line, False, False, 0)
        

        # Container 1
        container1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        container1.set_vexpand(True)
        container1.set_homogeneous(False)
        container1.set_border_width(10)

        # text box
        text_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        container1.pack_start(text_box, False, False, 0)

        # Welcome text
        welcome_label = Gtk.Label()
        welcome_label.set_text("Welcome to Deku Linux\nLorem ipsum dolor set eid adoi adihl eiha diuhad.\n Diahe, ihad a akldiv i dau ekdhuc.")
        welcome_label.set_line_wrap(True)
        text_box.pack_start(welcome_label, False, False, 0)

        # center box
        center_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        center_box.set_halign(Gtk.Align.CENTER)
        center_box.set_name("center-box")
        container1.pack_start(center_box, False, False, 0)

        # device label
        device_label = Gtk.Label()
        device_label.set_text("2 devices")
        center_box.pack_start(device_label, False, False, 30)
    
        main_box.pack_end(container1, True, True, 0)

        # Apply custom CSS styling
        self.apply_css()

        self.show_all()

        screen = self.get_screen()
        max_width = screen.get_width()
        self.set_size_request(max_width, -1)



    def on_modem_1_click(self, widget, event):
        print("Modem 1 clicked!")

        modem_window = ModemWindow()
        modem_window.show_all()

    def apply_css(self):
        css_provider = Gtk.CssProvider()
        css_path = "gui/utils/styles/styles.css"

       # Load the CSS rules into the provider
        css_provider.load_from_path(css_path)

        # Apply the CSS provider to the window
        screen = Gdk.Screen.get_default()
        style_context = self.get_style_context()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def run(self):
        Gtk.main()

if __name__ == "__main__":
    app = MyApp()
    app.run()
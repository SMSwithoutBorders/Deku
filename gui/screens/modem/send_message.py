import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from utils.widgets.horizontal_line import HorizontalLine
from screens.modem.outgoing_message import OutgoingMessageWindow
from screens.modem.message_forwarding import MessageForwardingWindow
from screens.modem.incoming_message import IncomingMessageWindow
from screens.modem.failed_message import FailedMessageWindow
from screens.modem.export_message import ExportMessageWindow
from screens.modem.encrypted_message import EncryptedMessageWindow



class SendMessageWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Deku Linux App")

        self.connect("destroy", Gtk.main_quit)
        self.set_default_size(800, 600)

        # Create the main container
        main_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.add(main_box)

        # Create the sidebar
        sidebar = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        sidebar.set_size_request(150, -1)
        sidebar.set_homogeneous(False)
        sidebar.set_border_width(0)
        sidebar.set_name("sidebar")
        main_box.pack_start(sidebar, False, False, 0)

        # Sidebar content
        sidebar_top = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        sidebar.pack_start(sidebar_top, False, False, 0)

        home_modem_label = Gtk.Label()
        home_modem_label.set_text("Home Modem")
        home_modem_label.set_name("side_label")
        home_modem_label.set_margin_bottom(8)
        home_modem_label.set_margin_top(60)
        sidebar_top.pack_start(home_modem_label, False, False, 0)

        line = HorizontalLine()
        sidebar_top.pack_start(line, False, False, 0)

        # send
        send_label = Gtk.Label()
        send_label.set_text("Send")
        send_label.set_name("side_label")
        send_label.set_name("active")
        send_label.set_margin_bottom(8)
        send_label.set_margin_top(8)
        # send_event_box = Gtk.EventBox()
        # send_event_box.add(send_label)
        # send_event_box.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        # send_event_box.connect("button-press-event", self.send_label_clicked)
        sidebar_top.pack_start(send_label, False, False, 0)

        line = HorizontalLine()
        sidebar_top.pack_start(line, False, False, 0)

        # incoming
        incoming_label = Gtk.Label()
        incoming_label.set_text("Incoming")
        incoming_label.set_name("side_label")
        incoming_label.set_margin_bottom(8)
        incoming_label.set_margin_top(8)
        incoming_event_box = Gtk.EventBox()
        incoming_event_box.add(incoming_label)
        incoming_event_box.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        incoming_event_box.connect("button-press-event", self.incoming_label_clicked)
        sidebar_top.pack_start(incoming_event_box, False, False, 0)


        line = HorizontalLine()
        sidebar_top.pack_start(line, False, False, 0)

        # Outgoing
        outgoing_label = Gtk.Label()
        outgoing_label.set_text("Outgoing ")
        outgoing_label.set_name("side_label")
        outgoing_label.set_margin_bottom(8)
        outgoing_label.set_margin_top(8)
        sidebar_top.pack_start(outgoing_label, False, False, 0)


        line = HorizontalLine()
        sidebar_top.pack_start(line, False, False, 0)

        # Failed
        failed_label = Gtk.Label()
        failed_label.set_text("Failed ")
        failed_label.set_name("side_label")
        failed_label.set_margin_bottom(8)
        failed_label.set_margin_top(8)
        sidebar_top.pack_start(failed_label, False, False, 0)


        line = HorizontalLine()
        sidebar_top.pack_start(line, False, False, 0)

        # encrypted
        encrypted_label = Gtk.Label()
        encrypted_label.set_text("Encrypted")
        encrypted_label.set_name("side_label")
        encrypted_label.set_margin_bottom(40)
        encrypted_label.set_margin_top(8)
        sidebar_top.pack_start(encrypted_label, False, False, 0)

        line = HorizontalLine()
        sidebar_top.pack_start(line, False, False, 0)
        line = HorizontalLine()
        sidebar_top.pack_start(line, False, False, 0)


        # message_forwarding
        message_forwarding_label = Gtk.Label()
        message_forwarding_label.set_text("Message Forwarding")
        message_forwarding_label.set_name("side_label")
        message_forwarding_label.set_margin_bottom(8)
        message_forwarding_label.set_margin_top(15)
        sidebar_top.pack_start(message_forwarding_label, False, False, 0)


        line = HorizontalLine()
        sidebar_top.pack_start(line, False, False, 0)

        # export
        export_label = Gtk.Label()
        export_label.set_text("Export")
        export_label.set_name("side_label")
        export_label.set_margin_bottom(8)
        export_label.set_margin_top(8)
        sidebar_top.pack_start(export_label, False, False, 0)
    

        line = HorizontalLine()
        sidebar_top.pack_start(line, False, False, 0)

        # About
        about_label = Gtk.Label()
        about_label.set_text("About ")
        about_label.set_name("side_label")
        about_label.set_margin_bottom(8)
        about_label.set_margin_top(8)
        sidebar_top.pack_start(about_label, False, False, 0)

        # Create the main content area
        content_area = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        main_box.pack_start(content_area, True, True, 0)

        # Create the navigation bar
        nav_bar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        nav_bar.set_size_request(-1, 50)
        nav_bar.set_homogeneous(False)
        # nav_bar.set_border_width(10)
        nav_bar.set_name("nav-bar")
        content_area.pack_start(nav_bar, False, False, 0)

        # Create a box for the left side of the navigation bar
        left_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        left_box.set_homogeneous(True)
        nav_bar.pack_start(left_box, False, False, 0)

        # Adjusting navbar
        title_label = Gtk.Label()
        title_label.set_text("Deku Linux")
        title_label.set_name("title-label")
        left_box.pack_start(title_label, False, False, 20)

        # Create a box for the right side of the navigation bar
        right_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        right_box.set_homogeneous(True)
        nav_bar.pack_end(right_box, False, False, 20)

        # Icon
        nav_icon = Gtk.Image.new_from_icon_name("preferences-system-symbolic", Gtk.IconSize.SMALL_TOOLBAR)
        right_box.pack_end(nav_icon, False, False, 0)

        # Container 1
        container1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        # container1.set_vexpand(True)
        container1.set_hexpand(True)
        container1.set_halign(Gtk.Align.FILL)
        container1.set_homogeneous(False)
        container1.set_border_width(5)
        content_area.pack_start(container1, True, True, 0)

        # container1 main
        center_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        center_box.set_halign(Gtk.Align.CENTER)
        center_box.set_name("center-box-message")
        container1.pack_start(center_box, True, True, 0)

        # message label
        message_label = Gtk.Label()
        message_label.set_text("NEW MESSAGE")
        center_box.pack_start(message_label, False, False, 5)

        # Horizontal line widget
        line = HorizontalLine()
        center_box.pack_start(line, False, False, 0)

        # Text entry for phone number
        number_entry = Gtk.Entry()
        number_entry.set_placeholder_text("Number:")
        center_box.pack_start(number_entry, False, False, 0)

        # compose message
        text_area = Gtk.Entry()
        text_area.set_placeholder_text("Compose message...")
        text_area.set_size_request(600, 400)
        center_box.pack_start(text_area, False, False, 0 )

        # Send button with label and logo
        send_button = Gtk.Button()
        send_button.set_margin_top(10)
        send_button.set_label("Send")
        send_button.set_name("send_btn")
        send_button.set_image(Gtk.Image.new_from_icon_name("mail-send", Gtk.IconSize.BUTTON))
        center_box.pack_start(send_button, False, False, 10)

        # Adjusting container size
        screen = Gdk.Screen.get_default()
        container1.set_size_request(-1, int(screen.get_height() * 0.55))

        # Apply custom CSS styling
        self.apply_css()

        self.show_all()

    def apply_css(self):
        css_provider = Gtk.CssProvider()
        css_path = "gui/utils/styles/styles.css"
        # Load the CSS rules into the provider
        css_provider.load_from_path(css_path)

        # Apply the CSS provider to the window
        screen = Gdk.Screen.get_default()
        style_context = self.get_style_context()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def send_label_clicked(self, widget, event):
        print("send label click")
        send_window = SendMessageWindow()
        send_window.show_all()

    def incoming_label_clicked(self, widget, event):
        incoming_window = IncomingMessageWindow()
        incoming_window.show_all()

        
    def run(self):
        Gtk.main()

if __name__ == "__main__":
    app = ModemWindow()
    app.run()
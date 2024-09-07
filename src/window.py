
from gi.repository import Adw
from gi.repository import Gtk

@Gtk.Template(resource_path='/org/gnome/Example/window.ui')
class ScpiPowersupplyControlWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'ScpiPowersupplyControlWindow'

    label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

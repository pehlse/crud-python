import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess
class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Menu")

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)

        self.button1 = Gtk.Button(label="Adiconar nova pessoa")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.add(self.button1)

 
    def on_button1_clicked(self, widget):
        subprocess.Popen(["python", "newPerson.py"])


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
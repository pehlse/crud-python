import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.test
class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Nova pessoa")
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)

        box = Gtk.Box()
        self.name_entry = Gtk.Entry()
        self.l1 = Gtk.Label("Nome")
        box.add(self.l1)
        box.add(self.name_entry)
        self.box.add(box)

        box = Gtk.Box()
        self.salary = Gtk.Entry()
        self.l1 = Gtk.Label("Salario")
        box.add(self.l1)
        box.add(self.salary)
        self.box.add(box)

        self.button1 = Gtk.Button(label="Guardar")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.add(self.button1)
#        self.box.pack_start(self.button1, True, True, 0)

 
    def on_button1_clicked(self, widget):
        if self.name_entry.get_text!="":
            contact = (self.name_entry.get_text(),int(self.salary.get_text()))
            col = db.person
            col.insert_one(
                {
                    "name": self.name_entry.get_text(),
                    'salary': int(self.salary.get_text()),
                }
            )
            print(Gtk)

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Pango
import locale
import gettext

_ = gettext.gettext
N_ = gettext.ngettext

class View:
    @classmethod
    def main(cls):
        Gtk.main()

    @classmethod
    def main_quit(cls, w, e):
        Gtk.main_quit()

    def build_view(self):
        w = Gtk.Window(title=_("Musical Searcher"))
        w.set_default_size(500, 1000)

        self.declare_buttons()
        self.declare_labels()
        self.interval = ""
        self.interval_type= ""
        sel_interval = Gtk.Label()
        sel_interval.set_text(_("Select an interval"))
        sel_interval.set_line_wrap(True)

        sel_type = Gtk.Label()
        sel_type.set_text(_("Select interval type"))

        hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10, margin=10)
        hbox1.pack_start(self.i2m, False, False, 0)
        hbox1.pack_start(self.i2M, False, False, 0)
        hbox1.pack_start(self.i3m, False, False, 0)

        hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10, margin=10)
        hbox2.pack_start(self.i3M, False, False, 0)
        hbox2.pack_start(self.i4j, False, False, 0)
        hbox2.pack_start(self.i4aum, False, False, 0)

        hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10, margin=10)
        hbox3.pack_start(self.i5j, False, False, 0)
        hbox3.pack_start(self.i6m, False, False, 0)
        hbox3.pack_start(self.i6M, False, False, 0)

        hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10, margin=10)
        hbox4.pack_start(self.i7m, False, False, 0)
        hbox4.pack_start(self.i7M, False, False, 0)
        hbox4.pack_start(self.i8a, False, False, 0)

        vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10, margin=40)

        vbox1.pack_start(sel_interval, False, False, 0)
        vbox1.pack_start(hbox1, False, False, 0)
        vbox1.pack_start(hbox2, False, False, 0)
        vbox1.pack_start(hbox3, False, False, 0)
        vbox1.pack_start(hbox4, False, False, 0)
        vbox1.pack_end(self.l_interval_type, False, False, 0)
        vbox1.pack_end(self.l_interval, False, False, 0) 

        vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10, margin=40)

        vbox2.pack_start(sel_type, False, False, 0)
        vbox2.pack_start(self.asc, False, False, 0)
        vbox2.pack_start(self.desc, False, False, 0)
        vbox2.pack_end(self.search, False, False, 0)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10, margin=40)

        hbox.pack_start(vbox1, False, False, 0)
        hbox.pack_start(vbox2, False, False, 0)

        w.add(hbox)

        self.w = w

    def declare_buttons(self):
        self.i2m = Gtk.Button(label=("2m"), use_underline=True)
        self.i2M = Gtk.Button(label=("2M"), use_underline=True)
        self.i3m = Gtk.Button(label=("3m"), use_underline=True)
        self.i3M = Gtk.Button(label=("3M"), use_underline=True)
        self.i4j = Gtk.Button(label=("4j"), use_underline=True)
        self.i4aum = Gtk.Button(label=("4aum"), use_underline=True)
        self.i5j = Gtk.Button(label=("5j"), use_underline=True)
        self.i6m = Gtk.Button(label=("6m"), use_underline=True)
        self.i6M = Gtk.Button(label=("6M"), use_underline=True)
        self.i7m = Gtk.Button(label=("7m"), use_underline=True)
        self.i7M = Gtk.Button(label=("7M"), use_underline=True)
        self.i8a = Gtk.Button(label=("8a"), use_underline=True)

        self.asc = Gtk.Button(label=("ASC"), use_underline=True)
        self.desc = Gtk.Button(label=("DESC"), use_underline=True)
        self.search = Gtk.Button(label=(_("Search")), use_underline=True)
    
    def declare_labels(self):
        self.l_interval = Gtk.Label()
        self.l_interval.set_text(_("Chosen interval:"))
        self.l_interval_type = Gtk.Label()
        self.l_interval_type.set_text(_("Chosen interval type:"))

    def show_all(self):
        self.w.show_all()
    
    def connect_delete_event(self, fun):
        self.w.connect('delete-event', fun)
    
    def connect_i2m_clicked(self, fun):
        self.i2m.connect('clicked', fun)

    def connect_i2M_clicked(self, fun):
        self.i2M.connect('clicked', fun)

    def connect_i3m_clicked(self, fun):
        self.i3m.connect('clicked', fun)

    def connect_i3M_clicked(self, fun):
        self.i3M.connect('clicked', fun)

    def connect_i4j_clicked(self, fun):
        self.i4j.connect('clicked', fun)

    def connect_i4aum_clicked(self, fun):
        self.i4aum.connect('clicked', fun)

    def connect_i5j_clicked(self, fun):
        self.i5j.connect('clicked', fun)

    def connect_i6m_clicked(self, fun):
        self.i6m.connect('clicked', fun)

    def connect_i6M_clicked(self, fun):
        self.i6M.connect('clicked', fun)

    def connect_i7m_clicked(self, fun):
        self.i7m.connect('clicked', fun)

    def connect_i7M_clicked(self, fun):
        self.i7M.connect('clicked', fun)

    def connect_i8a_clicked(self, fun):
        self.i8a.connect('clicked', fun)

    def connect_asc_clicked(self, fun):
        self.asc.connect('clicked', fun)

    def connect_desc_clicked(self, fun):
        self.desc.connect('clicked', fun)

    def connect_search_clicked(self, fun):
        self.search.connect('clicked', fun)

    def update_view(self, **kwargs):
        for name, value in kwargs.items():
            if name == 'show_interval':
                self.show_interval(value)
            elif name == 'show_interval_type':
                self.show_interval_type(value)
            elif name == 'show_song_list':
                self.show_song_list(value)
            elif name == 'invalid_arguments':
                self.show_error(_("Invalid arguments"), _("Please select an interval and an interval type"))
            elif name == 'http_error':
                self.show_error(_("The server couldn't fulfill the request."), str(value)+" "+_(self.http_error_code(value)))
            else:
                raise TypeError(f"update_view() got an unexpected keyword argument '{name}'")

    def show_interval(self, interval):
        self.interval = interval
        str = "Chosen interval: " + interval
        self.l_interval.set_text(_(str))
    
    def show_interval_type(self, interval_type):
        self.interval_type = interval_type
        str = "Chosen interval type: " + interval_type
        self.l_interval_type.set_text(_(str))

    def show_song_list(self, songList):
        if songList._list == []:
            self.show_error(_("The server has not returned anything"), "")
        else:
            return SongsView(self.w, _("Musical searcher"), songList, _(self.interval), _(self.interval_type))

    @classmethod
    def semitones_from_interval(self, interval):
        semitones = {
            "2m":1,
            "2M":2,
            "3m":3,
            "3M":4,
            "4j":5,
            "4aum":6,
            "5j":7,
            "6m":8,
            "6M":9,
            "7m":10,
            "7M":11,
            "8a":12
        }
        return semitones[interval]

    @classmethod
    def search_example(self, semitones, interval_type):
        notes = [_("C"), _("C♯/D♭"), _("D"), _("D♯/E♭"), _("E"), _("F"), _("F♯/G♭"), _("G"), _("G♯/A♭"), _("A"), _("A♯/B♭"), _("B")]
        import random
        i = random.randint(0, 11)
        note1 = notes[i]
        if interval_type == "ascending":
            note2 = notes[(i+semitones)%12]
        else:
            note2 = notes[(i-semitones)%12]
        return note1, note2
        
    def http_error_code(self, code):
        responses = {
            400: 'Bad request syntax or unsupported method',
            401: 'Unauthorized: No permission -- see authorization schemes',
            402: 'Payment Required: No payment -- see charging schemes',
            403: 'Forbidden: Request forbidden -- authorization will not help',
            404: 'Not Found: Nothing matches the given URI',
            405: 'Method Not Allowed: Specified method is invalid for this server.',
            406: 'Not Acceptable: URI not available in preferred format.',
            407: 'Proxy Authentication Required:You must authenticate with this proxy before proceeding.',
            408: 'Request Timeout: Request timed out; try again later.',
            409: 'Conflict: Request conflict.',
            410: 'Gone: URI no longer exists and has been permanently removed.',
            411: 'Length Required: Client must specify Content-Length.',
            412: 'Precondition Failed: Precondition in headers is false.',
            413: 'Request Entity Too Large: Entity is too large.',
            414: 'Request-URI Too Long: URI is too long.',
            415: 'Unsupported Media Type: Entity body in unsupported format.',
            416: 'Requested Range Not Satisfiable: Cannot satisfy request range.',
            417: 'Expectation Failed: Expect condition could not be satisfied.',
            500: 'Internal Server Error: Server got itself in trouble',
            501: 'Not Implemented: Server does not support this operation',
            502: 'Bad Gateway: Invalid responses from another server/proxy.',
            503: 'Service Unavailable: The server cannot process the request due to a high load',
            504: 'Gateway Timeout: The gateway server did not receive a timely response',
            505: 'HTTP Version Not Supported: Cannot fulfill request.',
        }
        return responses[code]

    def show_error(self, text, text_2):
        dialog = Gtk.MessageDialog(parent= self.w,
                                message_type= Gtk.MessageType.ERROR,
                                buttons= Gtk.ButtonsType.CLOSE,
                                text= text)
        dialog.format_secondary_text(text_2)
        dialog.run()
        dialog.destroy()

class SongsView:

    def __init__(self, parent, title, _song_list, interval, interval_type):
        self.songsView = Gtk.Dialog(title, parent, Gtk.DialogFlags.DESTROY_WITH_PARENT)
        self.songsView.set_default_response(Gtk.ResponseType.CANCEL)
        self.songsView.set_default_size(250, 500)
        new_search = Gtk.Button(label=(_("NEW SEARCH")), use_underline=True)
        new_search.connect('clicked', self.on_new_search_clicked)
        _interval = Gtk.Label()
        _interval.set_markup(_("<b>INTERVAL:</b>     ")+interval)
        _interval_type = Gtk.Label()
        _interval_type.set_markup(_("<b>Interval type:</b>     ")+interval_type) 
        note1, note2 = View.search_example(View.semitones_from_interval(interval), interval_type)
        example = Gtk.Label()
        example.set_markup(_("<b>Example:</b>     ")+note1+_(" <big>-</big> ")+note2)


        song_list = Gtk.ListStore(str, str, str)
        
        for song in _song_list.get_list():
            song_list.append((song.title, song.url, song.fav))

        treeview = Gtk.TreeView(model=song_list)
        columns = [_("Title"), _("URL"), _("Favourite")]
        for i, column in enumerate(columns):
            cell = Gtk.CellRendererText()
            if i == 0:
                cell.props.weight_set = True
                cell.props.weight = Pango.Weight.BOLD
            col = Gtk.TreeViewColumn(column, cell, text=i)
            treeview.append_column(col)

        grid = Gtk.Grid()
        grid.attach(treeview, 0, 0, 1, 1)


        box = self.songsView.get_content_area()
        box.pack_start(grid, True, True, 0)
        box.pack_end(new_search, True, True, 0)
        box.pack_end(example, True, True, 0)
        box.pack_end(_interval_type, True, True, 0)
        box.pack_end(_interval, True, True, 0)
        self.songsView.show_all()
        selection = treeview.get_selection().connect("changed", self.on_changed) 
    
    def on_new_search_clicked(self, button):
        self.songsView.destroy()

    def on_changed(self, selection):
        (model, iter) = selection.get_selected()
        import webbrowser
        webbrowser.open(model[iter][1], new=1, autoraise=False)
        return True


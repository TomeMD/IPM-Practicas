#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import base64
import threading
import model
from types import SimpleNamespace
import locale
import gettext

_ = gettext.gettext
N_ = gettext.ngettext


class Controller:
    def set_view(self, view):
        self.view = view
        self.view.build_view()
        self.view.connect_delete_event(self.view.main_quit)
        self.view.connect_i2m_clicked(self.on_i2m_clicked)
        self.view.connect_i2M_clicked(self.on_i2M_clicked)
        self.view.connect_i3m_clicked(self.on_i3m_clicked)
        self.view.connect_i3M_clicked(self.on_i3M_clicked)
        self.view.connect_i4j_clicked(self.on_i4j_clicked)
        self.view.connect_i4aum_clicked(self.on_i4aum_clicked)
        self.view.connect_i5j_clicked(self.on_i5j_clicked)
        self.view.connect_i6m_clicked(self.on_i6m_clicked)
        self.view.connect_i6M_clicked(self.on_i6M_clicked)
        self.view.connect_i7m_clicked(self.on_i7m_clicked)
        self.view.connect_i7M_clicked(self.on_i7M_clicked)
        self.view.connect_i8a_clicked(self.on_i8a_clicked)
        self.view.connect_asc_clicked(self.on_asc_clicked)
        self.view.connect_desc_clicked(self.on_desc_clicked)
        self.view.connect_search_clicked(self.on_search_clicked)

    def set_model(self, model):
        self.model = model
        self.model.controller = self

    def main(self):
        self.view.show_all()
        self.view.main()

    # Intervalos
    def on_i2m_clicked(self, w):
        self.model.interval = "2m"
        self._update_view(show_interval= "2m")

    def on_i2M_clicked(self, w):
        self.model.interval = "2M"
        self._update_view(show_interval= "2M")

    def on_i3m_clicked(self, w):
        self.model.interval = "3m"
        self._update_view(show_interval= "3m")

    def on_i3M_clicked(self, w):
        self.model.interval = "3M"
        self._update_view(show_interval= "3M")

    def on_i4j_clicked(self, w):
        self.model.interval = "4j"
        self._update_view(show_interval= "4j")

    def on_i4aum_clicked(self, w):
        self.model.interval = "4aum"
        self._update_view(show_interval= "4aum")

    def on_i5j_clicked(self, w):
        self.model.interval = "5j"
        self._update_view(show_interval= "5j")

    def on_i6m_clicked(self, w):
        self.model.interval = "6m"
        self._update_view(show_interval= "6m")

    def on_i6M_clicked(self, w):
        self.model.interval = "6M"
        self._update_view(show_interval= "6M")

    def on_i7m_clicked(self, w):
        self.model.interval = "7m"
        self._update_view(show_interval= "7m")

    def on_i7M_clicked(self, w):
        self.model.interval = "7M"
        self._update_view(show_interval= "7M")

    def on_i8a_clicked(self, w):
        self.model.interval = "8a"
        self._update_view(show_interval= "8a")

    # Tipo de intervalo
    def on_asc_clicked(self, w):
        self.model.interval_type = "asc"
        self._update_view(show_interval_type= _("ascending"))

    def on_desc_clicked(self, w):
        self.model.interval_type = "des"
        self._update_view(show_interval_type= _("descending"))
    
    def on_search_clicked(self, w):
        thr1 = threading.Thread(target=self.model.search_thread,args=(model.SongList(),), daemon=True)
        thr1.start()
    
    def _update_view(self, **kwargs):
        self.view.update_view(**kwargs)
    
    def update_answer(self, songList, state, error):
        if state == "valid_args":
            self.view.update_view(show_song_list=songList)
        elif state == "invalid_args":
            self.view.update_view(invalid_arguments=None)
        elif state == "http_error":
            self.view.update_view(http_error=error)
        

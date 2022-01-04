#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
#from types import SimpleNamespace
import urllib.parse
import urllib.request
from urllib.error import URLError, HTTPError
import requests
import json
import time
import controller


class Model:

    def __init__(self):
        self.controller = None
        self.interval = ""
        self.interval_type = ""

    def _update_answer(self, songList, state, error):
        self.controller.update_answer(songList, state, error)


    def search_thread(self, song_list):

        if self.interval != "" and self.interval_type != "":
            # Hacer peticion al servidor
            pet='http://127.0.0.1:5000/songs/'+self.interval+'/'+self.interval_type

            # Respuesta del server en formato json
            req=requests.get(pet)
            if req.status_code == requests.codes.ok:
                res = req.json()       
                # Parsear el json
                i=0
                while i < len(res['data']):
            	    data = res['data']
            	    d = data[i]
            	    song = Song(d[0],d[1],d[2])
            	    song_list.add_song(song) # Añadimos las canciones a la lista
            	    i+=1
                # Comprobación de que es concurrente    
                #time.sleep(5)
                GLib.idle_add(self._update_answer, song_list, "valid_args", None) 
            else: 
                GLib.idle_add(self._update_answer, song_list, "http_error", req.status_code)

        else:
            GLib.idle_add(self._update_answer, song_list, "invalid_args", None)


class SongList:
    def __init__(self):
        self._list = []


    def add_song(self, song):
        self._list.append(song)

    def get_list(self):
        return self._list

    def del_song(self, song):
        for s in self._list:
            if  (s._title == song._title) and (s._url == song._url):
                self._list.remove(s)
    
    def print_songs(self):
        for s in self._list:
            print(s)
    

class Song:
    
    def __init__(self, title, url, fav):
        self._title = title
        self._url = url
        self._fav = fav

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def fav(self):
        return self._fav

    @fav.setter
    def fav(self, value):
        self._fav = valuelue

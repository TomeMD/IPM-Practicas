#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from controller import Controller
from view import View
from model import Model
import locale
from pathlib import Path
import gettext


if __name__ == '__main__':

    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    locale.setlocale(locale.LC_ALL, '')

    LOCALE_DIR = Path(__file__).parent / "locale"
    gettext.bindtextdomain('MusicalSearcher', LOCALE_DIR)
    gettext.bindtextdomain('MusicalSearcher', LOCALE_DIR)
    gettext.textdomain('MusicalSearcher')


    controller = Controller()
    controller.set_view(View())
    controller.set_model(Model())
    controller.main()


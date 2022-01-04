import subprocess
import time
import sys
import random

import gi
gi.require_version('Atspi', '2.0')
from gi.repository import Atspi

def get_app(name):
    desktop = Atspi.get_desktop(0)
    start = time.time()
    timeout = 5
    app = None
    while app is None and (time.time() - start) < timeout:
        gen = (child for _i, child in children(desktop) if child and child.get_name() == name)
        app = next(gen, None)
        if app is None:
            time.sleep(0.6)
    return app

def get_obj(parent, role= None, name= None):
    def _check(obj):
        return role is None or obj.get_role_name() == role and \
            name is None or obj.get_name() == name
    return next((obj for _, obj in tree(parent) if _check(obj)), None)

def run(path, name= None):
    name = name or f"{path}-test-{str(random.randint(0, 100000000))}"
    process = subprocess.Popen([path, '--name', name])
    app = get_app(name)
    return (process, app, name)

def stop(process):
    if process is not None:
        process.kill()


def children(obj):
    for i in range(0, obj.get_child_count()):
        yield i, obj.get_child_at_index(i)

def tree(object, path= ()):
    yield path, object
    for i, child in children(object):
        yield from tree(child, path + (i,))

def do_action(obj, name):
    for i in range(0, obj.get_n_actions()):
        if obj.get_action_name(i) == name:
            obj.do_action(i)
            return
    raise RuntimeError(f"{obj} no tiene una acción {name}")

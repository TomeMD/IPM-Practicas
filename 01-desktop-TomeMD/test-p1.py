#!/usr/bin/env python3

import sys
import textwrap
from collections import namedtuple
import time
import subprocess

import e2e

"""
    Histories:

    GIVEN he lanzado la aplicación
    THEN veo el texto "Chosen interval:"
    AND veo el texto "Chosen interval type:"

    GIVEN he lanzado la aplicacion
    WHEN pulso el botón "3M"
    THEN veo el texto "Chosen interval: 3M"
    WHEN pulso el botón "asc"
    THEN veo el texto "Chosen interval type: ascending"

    GIVEN he lanzado la aplicacion
    WHEN pulso el botón "3M"
    THEN veo el texto "Chosen interval: 3M"
    WHEN pulso el botón "asc"
    THEN veo el texto "Chosen interval type: ascending"
    WHEN pulso el boton search
    THEN veo la canción "La primavera (Vivaldi)"
    THEN veo la canción "Oh when the saints go marching in"
    THEN veo la canción "Blister in the sun (Violent Femmes)"
    THEN veo la canción "Blue Danube"
    THEN veo la canción "Ob-la-di Ob-la-da (The Beatles)"
    THEN veo la canción "Sweet Child O'Mine - Bass riff intro (Guns N' Roses)"

"""

# Funciones de ayuda

def show(text):
    print(textwrap.dedent(text))

def show_passed():
    print('\033[92m', "   Passed", '\033[0m')

def show_not_passed(e):
    print('\033[91m', "   Not Passed", '\033[0m')
    print(textwrap.indent(str(e),"   "))

# Contexto de las pruebas

Ctx = namedtuple("Ctx", "path process app")

# Implementación de los pasos

def given_he_lanzado_la_aplicacion(ctx):
    process, app, name = e2e.run(ctx.path)
    assert app is not None
    return Ctx(path = ctx.path, process = process, app = app), name

def then_veo_el_texto_chosen_interval(ctx, interval):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'label'
    and node.get_text(0, -1).startswith("Chosen interval:"))
    label = next(gen, None)
    assert label and label.get_text(0, -1) == "Chosen interval:"+interval, label.get_text(0, -1)
    return ctx

def then_veo_el_texto_chosen_interval_type(ctx, interval_type):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'label'
    and node.get_text(0, -1).startswith("Chosen interval type:"))
    label = next(gen, None)
    assert label and label.get_text(0, -1) == "Chosen interval type:"+interval_type, label.get_text(0, -1)
    return ctx

def when_pulso_el_boton(ctx, button_name):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'push button'
    and node.get_name() == button_name)
    boton = next(gen, None)
    assert boton is not None
    e2e.do_action(boton, 'click')
    return ctx

def then_veo_la_cancion(ctx, cancion):
    gen = (node for _path, node in e2e.tree(ctx.app) if node.get_role_name() == 'table cell'
    and node.get_name() == cancion)
    cell = next(gen, None)
    assert cell is not None
    assert cell.get_name() == cancion
    return ctx


if __name__ == '__main__':
    sut_path = sys.argv[1]
    initial_ctx = Ctx(path= sut_path, process= None, app= None)

    show("""
    GIVEN he lanzado la aplicacion
    THEN veo el texto "Chosen interval:"
    AND veo el texto "Chosen interval type:"
    """)

    ctx = initial_ctx
    try:
        ctx, name = given_he_lanzado_la_aplicacion(ctx)
        ctx = then_veo_el_texto_chosen_interval(ctx, "")
        ctx = then_veo_el_texto_chosen_interval_type(ctx, "")
        show_passed()
    except Exception as e:
        show_not_passed(e)
    e2e.stop(ctx.process)


    show("""
    GIVEN he lanzado la aplicacion
    WHEN pulso el botón "3M"
    THEN veo el texto "Chosen interval: 3M"
    WHEN pulso el botón "asc"
    THEN veo el texto "Chosen interval type: ascending"
    """)

    ctx = initial_ctx
    try:
        ctx, name = given_he_lanzado_la_aplicacion(ctx)
        ctx = when_pulso_el_boton(ctx, '3M')
        ctx = then_veo_el_texto_chosen_interval(ctx, " 3M")
        ctx = when_pulso_el_boton(ctx, 'ASC')
        ctx = then_veo_el_texto_chosen_interval_type(ctx, " ascending")
        show_passed()
    except Exception as e:
        show_not_passed(e)
    e2e.stop(ctx.process)


    show("""
    GIVEN he lanzado la aplicacion
    WHEN pulso el botón "3M"
    THEN veo el texto "Chosen interval: 3M"
    WHEN pulso el botón "asc"
    THEN veo el texto "Chosen interval type: ascending"
    WHEN pulso el boton search
    THEN veo la canción "La primavera (Vivaldi)"
    THEN veo la canción "Oh when the saints go marching in"
    THEN veo la canción "Blister in the sun (Violent Femmes)"
    THEN veo la canción "Blue Danube"
    THEN veo la canción "Ob-la-di Ob-la-da (The Beatles)"
    THEN veo la canción "Sweet Child O'Mine - Bass riff intro (Guns N' Roses)"
    """)

    ctx = initial_ctx
    try:
        ctx, name = given_he_lanzado_la_aplicacion(ctx)
        ctx = when_pulso_el_boton(ctx, '3M')
        ctx = then_veo_el_texto_chosen_interval(ctx, " 3M")
        ctx = when_pulso_el_boton(ctx, 'ASC')
        ctx = then_veo_el_texto_chosen_interval_type(ctx, " ascending")
        ctx = when_pulso_el_boton(ctx, 'Search')
        """
        A veces la comprobación de las canciones se ejecuta antes de que la petición al
        servidor termine y el diálogo esté disponible, metemos un pequeño delay para asegurarnos
        de que la comprobación es correcta
        """
        time.sleep(0.2) 
        ctx = then_veo_la_cancion(ctx, "La primavera (Vivaldi)")
        ctx = then_veo_la_cancion(ctx, "Oh when the saints go marching in")
        ctx = then_veo_la_cancion(ctx, "Blister in the sun (Violent Femmes)")
        ctx = then_veo_la_cancion(ctx, "Blue Danube")
        ctx = then_veo_la_cancion(ctx, "Ob-la-di Ob-la-da (The Beatles)")
        ctx = then_veo_la_cancion(ctx, "Kumbaya")
        ctx = then_veo_la_cancion(ctx, "Sweet Child O'Mine - Bass riff intro (Guns N' Roses)")
        show_passed()
    except Exception as e:
        show_not_passed(e)

    e2e.stop(ctx.process)
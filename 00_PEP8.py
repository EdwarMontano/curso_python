#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Línea resumen del docstring de este módulo.

Se trata de una docstring multilínea. Los párrafos están separados por líneas en blanco.
Las líneas se ajustan al límite de 79 columnas.

Los nombres de los módulos y paquetes deben ser cortos, en minúsculas con guión bajo.
Fíjate que esto no es PEP8-cheatsheet.py

En serio, usa flake8. Atom.io con https://atom.io/packages/linter-flake8
¡es genial!

Ver http://www.python.org/dev/peps/pep-0008/ para más detalles sobre PEP-8
"""

import re  # comentario de 1 línea (2 espacios antes de #)
import os  # librerías STD primero
import sys  # ordenados alfabeticamente

import some_third_party_lib  # Librerías de terceros después
import some_third_party_other_lib  # ordenados alfabeticamente

import local_stuff  # último las librerías locales
import more_local_stuff



_a_global_var = 2  # convención: _ para variables globales "privadas"
_b_global_var = 3

A_CONSTANT = 'ugh.' # convención: mayúsculas para constantes


# 2 líneas en blanco entre funciones y clases
def naming_convention():
    """escribir docstrings para TODAS las clases públicas, funcs y métodos.
    Las funciones utilizan snake_case.
    """
    if x == 4:  
        x, y = y, x  
    c = (a + b) * (a - b)  # los espacios alrededor de los operadores
    dict['key'] = dict[0] = {'x': 2, 'cat': 'not a dog'}


class NamingConvention(object):
    """La primera línea de un docstring es corta y está junto a las comillas.
    Los nombres de clases y excepciones son CapWords.
    Las comillas de cierre están en su propia línea
    """
    # nunca use variables de una sola letra, excepto en bucles para contar
    a = 2
    b = 4
    _internal_variable = 3
    class_ = 'foo'  # convención: _ para evitar conflictos con palabras clave

    # this will trigger name mangling to further discourage use from outside
    # this is also very useful if you intend your class to be subclassed, and
    # the children might also use the same var name for something else; e.g.
    # for simple variables like 'a' above. Name mangling will ensure that
    # *your* a and the children's a will not collide.
    __internal_var = 4

    # NUNCA utilice guiones bajos dobles iniciales y finales para nombra variables.
    # Son reservados para Python.
    __nooooooodontdoit__ = 0


    # algunos ejemplos de cómo ajustar el código al límite de 79 columnas:
    def __init__(self, width, height,
                 color='black', emphasis=None, highlight=0):
        if width == 0 and height == 0 and \
           color == 'red' and emphasis == 'strong' or \
           highlight > 100:
            raise ValueError('sorry, you lose')
        if width == 0 and height == 0 and (color == 'red' or
                                           emphasis is None):
            raise ValueError("I don't think so -- values are %s, %s" %
                             (width, height))
        Blob.__init__(self, width, height,
                      color, emphasis, highlight)

    # líneas vacías dentro del método para mejorar la legibilidad;
    short_foo_dict = {'loooooooooooooooooooong_element_name': 'cat',
                      'other_element': 'dog'}

    long_foo_dict_with_many_elements = {
        'foo': 'cat',
        'bar': 'dog'
    }

   
    def foo_method(self, x, y=None):
        """Los nombres de métodos y funciones se escriben en minúsculas con guión bajo.
        Utilice siempre self como primer argumento.
        """
        pass

    @classmethod
    def bar(cls):
        """Use cls!"""
        pass

# a 79-char ruler:
# 34567891123456789212345678931234567894123456789512345678961234567897123456789

"""
Common naming convention names:
snake_case
MACRO_CASE
camelCase
CapWords
"""

# Newline at end of file
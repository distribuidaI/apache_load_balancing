#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Script para simular visitas al proxy reverso y ver cómo balancea
#UNDAV - Programación Distribuida I
import sys
import pycurl
from StringIO import StringIO

times_default = 10

buffer = StringIO()
times = sys.argv[1]

c = pycurl.Curl()
c.setopt(c.URL, 'http://localhost/')
c.setopt(c.WRITEDATA, buffer)
c.perform()

body = buffer.getvalue()

print "Body: " + body

c.close()

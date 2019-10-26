#!/usr/bin/env python

import os
import re
import shutil
from waflib import Configure, Logs, Utils

SOURCE    = [ 'grbl/main.c', 'grbl/motion_control.c', 'grbl/gcode.c', 'grbl/spindle_control.c', 'grbl/coolant_control.c',
              'grbl/serial.c', 'grbl/protocol.c', 'grbl/stepper.c', 'grbl/eeprom.c', 'grbl/settings.c', 'grbl/planner.c',
              'grbl/nuts_bolts.c', 'grbl/limits.c', 'grbl/print.c', 'grbl/probe.c', 'grbl/report.c', 'grbl/system.c' ]

def options(opt):
    opt.load('c cxx')
    opt.load('avrdude')

def configure(conf):
    conf.load('avr-gcc') 
    conf.load('avr-gxx') 
    conf.load('avrdude')

def build(bld):
    b = bld()
    b.env.CFLAGS += ['-Wall', '-MMD', '-Os', '-DARDUINO=100', '-mmcu=atmega328p', '-ffunction-sections', '-fdata-sections', '-I.']
    b.defines = 'F_CPU=16000000'
    b.includes = 'avr-libc-2.0.0/include/'
    b.source = SOURCE
    b.target='cnc.elf'
    b.linkflags=['-Os', '-mmcu=atmega328p', '-lm']
    b.features='c cxx cprogram avr-gcc'




#!/usr/bin/python
import aprs

def p(x): 
	print "Source: %-10s Dest: %-10s Path: %-50s Text: %s" % (x.source, x.destination, x.path, x.text)

a = aprs.TCP('nocall', '-1', None, 'r/0/0/65535')
a.start()

a.receive(callback=p)


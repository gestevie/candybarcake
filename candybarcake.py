#!/usr/bin/python

import argparse
import math


def calcring(diameter, barwidth):
	"""
	Calculates the diameter of the ring and how many candybars are necessary for it
	:param diameter: diameter of the ring
	:param barwidth: width of the candy bar
	:return: tuple of perimeter of ring and number of candybars
	"""
	perimeter = math.ceil(math.pi * diameter)
	ncb = math.ceil(perimeter / barwidth * 10)  # number of candybars
	perimeter = ncb * barwidth / 10
	return (perimeter, ncb, diameter)

def calcvolumering(diameter, barheight):
	"""
	returns volume of a ring
	:param diameter: diameter of the ring
	:param barheigth: height of the candy bar
	:return: volume in dm^3 = l
	"""
	radius = diameter/2.0
	return math.ceil(math.pi * radius * radius * barheight/10)/1000


parser = argparse.ArgumentParser(description='Calculations for a candybar cake')
parser.add_argument('-r', '-rings', help='number of levels of the cake, default is 2', default=2, metavar='<n>', type=int)
parser.add_argument('-bw', '-barwidth', help='width of the candy bar in mm, default is 23mm', default=23, metavar='<mm>', type=int)
parser.add_argument('-bh', '-barheight', help='height of the candy bar in mm, default is 100mm', default=100, metavar='<mm>', type=int)
parser.add_argument('-c', '-cake', help='diameter of the cake in cm, default is 25cm', default=25, metavar='<cm>', type=int)

args = parser.parse_args()
# check for minimums and maximums
if args.c < 10:
	print 'diameter of cake must be at least 10cm!'
	exit(0)
t = (args.c - 10) / (args.r - 1)
gaprings = ((args.c - 10) / (args.r - 1))/2.0
if args.r > 1 and gaprings < 7.5:
	print 'too many rings for the diameter. gap between rings should be at least 7,5cm but you have ' + str(gaprings) + 'cm'
	exit(0)

leveldiameters = list()
leveldiameters.append(10)
ringdims = list()
ringvols = list()
if args.r > 1:
	for i in range(0, args.r-1):
		diameter = args.c - i*2*gaprings
		ringdims.append(calcring(diameter, args.bw))
		ringvols.append(calcvolumering(diameter, args.bh))
ringdims.append(calcring(10, args.bw))
ringvols.append(calcvolumering(10, args.bh))

fullvolume = 0
for i, e in enumerate(ringvols):
	if i == 1:
		fullvolume += e
	else:
		fullvolume += e/2.0
fullncb = 0
fulllength = 0
for e in ringdims:
	fullncb += e[1]
	fulllength += e[0]

print 'For a candybar cake with a diameter of ' + str(args.c) + 'cm and ' + str(args.r) + ' levels you need the following:'
print '\t- ' + str(fullncb) + ' candybars'
print '\t- ' + str(fulllength) + 'cm long paper strip ( +' + str(args.r) + ' overlaps for each ring) to glue the candybars on'
print '\t- ' + str(fullvolume) + 'dm^3 (or l) of candy to fill the cake at full height'
print 'For each ring the parameters are:'
for i, e in enumerate(ringdims):
	info = 'Ring ' + str(i+1) + ' (diameter: ' + str(e[2]) + '): '
	info += str(e[1]) + ' candybars and a strip of paper of length ' + str(e[0]) + 'cm (+some overlap)'
	print info
print 'HAPPY BAKING!'
#!/usr/bin/env python2.7

import sys
import os

stdinrules = raw_input("Please input the rules file: ")		# Getting the rules file
stdininput = raw_input("Please input the input file: ")		# Gettint the input file

rules = open(stdinrules)		# open the rules file
#input= '110000'

title = rules.readline()
title = title.strip()

print title


a = rules.readline()
alpha=[x.strip() for x in a.split(',')]		# parsing the alphabet and putting them into an array


s = rules.readline()
states=[y.strip() for y in s.split(',')]	# parsing the states and putting into an array


first = rules.readline()
first = first.strip()						# getting the first initial state into a variable


l = rules.readline()
last=[z.strip() for z in l.split(',')]		# parsing the last(accepted) state and putting into array



transition = []

for line in rules:
	transition.append([str(w.strip()) for w in line.split(',')])		# parsing and putting transitions
																		#into list of lists
input = open(stdininput)	# open the input file



for inputlines in input.readlines():
	step = 0							# counter for steps
	ruleno = 0							# count for the current rulenumber
	statern = first						#variable to keep track of current state
	inputlines = inputlines.strip()
	print 'String: ', inputlines
	for inputc in inputlines:		#looping through the characters of each input line
		if inputc not in alpha:		# checking for correct inputs
			print "an input character was not in the specified alphabet provided",
			sys.exit()
		else:
			ruleno = 0
			foundrule = 0
			for transc in transition:		#loop through each rule in the list of rules
					ruleno = ruleno + 1
					if statern == transc[0] and inputc == transc[1]:	# if we find the current state and 
						statern = transc[2]								# the input, we set current state
						step = step + 1									# equal to the next state and loop
						foundrule = foundrule + 1
						print "Step", step, '#', "Rule", ruleno, ":", transc[0], ',',
						print transc[1], ',', transc[2]
						break
			if foundrule < 1:		# this statement checks to see if there is a relevant transition rule
				print "there was no rule found that covered the current state and input"
				sys.exit()
	#	print statern
	if statern in last:		#once all the rules are complete, we check to see if we're on the last state
		print 'Accepted'
	else:
		print 'Rejected'
	print '\n'

input.close()		# close the files we opened
rules.close()


#print alpha
#print states
#print first
#print last
#print transition
#print input

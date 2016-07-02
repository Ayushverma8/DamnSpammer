###############################################################################
#
#                          2015 (C) Ayush Verma
#                        ayush_verma@srmuniv.edu.in
#
#                           Licensed under WTFPL
#               Do What the Fuck You Want to Public License
#                          http://www.wtfpl.net/
#
#              Author is nor liable for misuse; Use carefully!
#
###############################################################################
#
#	A cool py script to spam a google or any other  form.
#
#	What it can spam?	
#
#		- Mostly Single page forms   (Not sure about all)
#		- The following controls :
#			- text
#			- textarea
#			- select
#			- radio
#			- checkbox
#
#	What it cannot spam?
#
#		
#	
#		- A google form which has stuff not mentioned in (duh)
#
###############################################################################


import os
import random
import string
import sys
import mechanize

def fill(control):

	""" Gonna Fill up radio and other options with random numbers """

	total = len(control.get_items())
	value_to_set = str(control.get_items()[random.randint(1,total - 1)])
	control.value = [value_to_set]

def random_text(control, length):

	""" Gonna Fill up the text control with any length -->>"length" """

	control.value = ''.join(random.choice(string.ascii_uppercase + string.digits)
					for _ in range(length))

def new_browser():

	""" Gonaa Return  a new mechanize browser instance     Imp stuff starts up here """

	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.set_handle_refresh(False)

	return browser

def fill_form(form):

	""" Fills up the form with random bs """

	for control in form.controls:

		if control.type == "text":
			random_text(control, 20)

		elif control.type == "textarea":
			random_text(control, 200)		

		elif control.type == "radio":
			fill(control)

		elif control.type == "checkbox":
			fill(control)

		elif control.type == "select":
			fill(control)

		else:
			"Damn Shit happens! Please Go and Sleep ..this won't be working :-P"

def spam_form(url, times = 1):

	""" Spams a google form at url "times" number of times """

	browser = new_browser()
	total = times
	while times:

		""" Open form """
		browser.open(url)

		""" The form has no name by default, but luckily for 
			us only one form on the page so simply select the 
			first one.
		"""
		browser.form = list(browser.forms())[0]

		""" Mess it Fuck up and and submit it ASAP""
		fill_form(browser.form)
		browser.submit()

		times -= 1

		print "%d. Filled form" % (total - times)


if __name__ == "__main__":

	if len(sys.argv) < 3:
		print "run script as\n'python %s 'url' (in quotes) number_of_times_you_want_to_spam'\n" %(__file__)
		exit()

	url = sys.argv[1]
	times = int(sys.argv[2])
	spam_form(url, times)


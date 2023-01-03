#!/usr/bin/python3

# Name: search.py Purpose: A simply python3 CGI script to receive and
# output data from the html-css-datepicker.html page.

import cgi, cgitb
cgitb.enable()

print("Content-type: text/html")
print()

print("<title>CGI script search.py</title>")
print("<h1>HTML Datepicker output</h1>")

form = cgi.FieldStorage()
print("<p>search-from:", form["search-from"].value)
print("<p>search-to:", form["search-to"].value)

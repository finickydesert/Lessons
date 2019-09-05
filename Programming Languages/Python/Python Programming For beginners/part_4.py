#!/usr/bin/env python3
"""cannot explicitly convert int to str"""
import webbrowser
import urllib.parse
try:
   print("I {} python".format("love"))
   print({0} {1} {2} {3}.format("I", "love", "you", 3000))
except Exception as e:
    url = 'http://stackoverflow.com/search?q=' + urllib.parse.quote('[python-3.x] %s' % e)
    print(url)
    webbrowser.open(url)
#i got the original from: https://twitter.com/wittrup/status/697059127256817667
#i modifyed it to point to tagged post for python 3 
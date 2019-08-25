import webbrowser
import urllib.parse
try:
    myfile = open(filename.txt)
    print(myfile)
    input()

except Exception as e:
    url = 'http://stackoverflow.com/search?q=' + urllib.parse.quote('[python-3.x] %s' % e)
    print(url)
    webbrowser.open(url)
#i got this from: https://twitter.com/wittrup/status/697059127256817667 

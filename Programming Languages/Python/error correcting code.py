import webbrowser
import urllib.parse
try:
    10/0 #something
except Exception as e:
    url = 'http://stackoverflow.com/search?=' + urllib.parse.quote('Python %s' % e)
    print(url)
    webbrowser.open(url)
#i got this from: https://twitter.com/wittrup/status/697059127256817667

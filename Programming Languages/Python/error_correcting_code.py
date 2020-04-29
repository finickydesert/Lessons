import webbrowser
import urllib.parse
def error_catcher():
    try:
        10/0 #something
    except Exception as e:
        url = 'http://stackoverflow.com/search?q=' + urllib.parse.quote('[python-3.x] %s' % e)
        print(url)
    webbrowser.open(url)
#i got the original from: https://twitter.com/wittrup/status/697059127256817667
#i modifyed it to point to tagged post for python 3 

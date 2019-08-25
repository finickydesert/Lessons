import webbrowser
import urllib.parse

path = 'C:\Users\richa\Google Drive\code\Github\Lessons\Programming Languages\Python\filename.txt'

try:
    myfile = open(path, 'r')
    print(myfile)
    input('yo')

except Exception as e:
    url = 'http://stackoverflow.com/search?q=' + urllib.parse.quote('[python-3.x] %s' % e)
    print(url)
    webbrowser.open(url)
#i got this from: https://twitter.com/wittrup/status/697059127256817667 

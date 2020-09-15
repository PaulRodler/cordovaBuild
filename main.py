
import sys
from general import *

def main(url = None, build = None):
    #print('main: ' + url)
    appName = getName()
    url = validetUrl(url)

    if(url == None):
        print('[ **error**] url is None')
        exit(1)

    removeProjectFiles()

    if(build == 'android'):
        startAndroid()
    elif(build == 'ios'):
        startIOs()
    else:
        startAndroid()
        startIOs()

    print("HUHUHUHUHUUUUUUUUUUUUUUUUUUUUUUUU")
    print("[ ! ] Alles ist fertig gebuildet [ ! ]")
    cpAppToResult(appName)

if __name__ == '__main__':
    url = str(sys.argv[1])
    build = str(sys.argv[2])
    main(url, build)
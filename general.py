import os
from MyThread import *
import xml.etree.ElementTree as ET


def getName():
    tree = ET.parse('ios/config.xml')
    root = tree.getroot()
    return root[0].text

def validetUrl(url):
    try:
        print('main: ' + url.split('/')[1].split(' ')[0])
        return url.split('/')[1].split(' ')[0]
    except:
        print('[ i ] url is already valid')
        return url


def removeProjectFiles():
    try:
        os.system('rm -r android/www android/platforms android/plugins android/build.json '
                  'android/google-services.json android/GoogleService-Info.plist android/config.xml '
                  'android/android.keystore > /dev/null')
    except:
        print('[ i ] nothing removed')

    try:
        os.system('rm -r ios/www ios/platforms ios/plugins ios/build.json '
                  'ios/google-services.json ios/GoogleService-Info.plist ios/config.xml > /dev/null')
    except:
        print('[ i ] nothing removed')

    # os.system('curl -O ' + url)
    os.system('rm -r __MACOSX > /dev/null')
    os.system('rm -r kompr > /dev/null')
    filename = os.path.splitext("kompr.zip")[0]
    os.system('unzip -q ' + filename)
    os.system(
        'cp -r ' + filename + '/www ' + filename + '/ios/config.xml ' + filename + '/build.json ' + filename + '/google-services.json ' + filename + '/GoogleService-Info.plist ios')
    os.system(
        'cp -r ' + filename + '/www ' + filename + '/android/config.xml ' + filename + '/build.json ' + filename + '/google-services.json ' + filename + '/GoogleService-Info.plist android')
    os.system('rm -r __MACOSX')
    os.system('rm -r kompr')
    print('[ i ] FILES SUCCESSFULLY COPIED')


def cpAppToResult(appName):
    os.chdir('/Users/dancecloud/PycharmProjects/cordovaBuild > /dev/null')
    os.system('cp ios/platforms/ios/build/device/'+appName+'.ipa result/ > /dev/null')
    os.system('cp android/platforms/android/app/build/outputs/apk/debug/app-debug.apk result > /dev/null')
    os.system('mv result/app-debug.apk result/'+appName+'.apk')
    print('[ i ] app dateien in result')


def startAndroid():
    android = MyThread('android')
    android.start()
    android.join()

def startIOs():
    ios = MyThread('ios')
    ios.start()
    ios.join()
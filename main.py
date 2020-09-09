from MyThread import *
import os, sys

"""
    TODO url with :)
    TODO xcode edit build path :)
    TODO upload to appstores ----------
    TODO listener (python server) :)
    """

def main(url):
    #print('main: ' + url)
    try:
        print('main: ' + url.split('/')[1].split(' ')[0])
        url = url.split('/')[1].split(' ')[0]
    except:
        print('[ i ] mybe')

    if(url == None):
        print('[ **error**] url is None')
        exit(1)

    try:
        os.system('rm -r android/www android/platforms android/plugins android/build.json android/google-services.json android/GoogleService-Info.plist android/config.xml android/android.keystore')
    except:
        print('[ i ] nothing removed')

    try:
        os.system('rm -r ios/www ios/platforms ios/plugins ios/build.json ios/google-services.json ios/GoogleService-Info.plist ios/config.xml')
    except:
        print('[ i ] nothing removed')


    #os.system('curl -O ' + url)
    os.system('rm -r __MACOSX')
    os.system('rm -r kompr')
    filename = os.path.splitext("kompr.zip")[0]
    os.system('unzip -q '+filename)
    os.system('cp -r ' + filename + '/www ' + filename + '/ios/config.xml ' + filename + '/build.json ' + filename + '/google-services.json ' + filename + '/GoogleService-Info.plist ios')
    os.system('cp -r ' + filename + '/www ' + filename + '/android/config.xml ' + filename + '/build.json ' + filename + '/google-services.json ' + filename + '/GoogleService-Info.plist android')
    os.system('rm -r __MACOSX')
    os.system('rm -r kompr')

    print('[ i ] FILES SUCCESSFULLY COPIED')

    android = MyThread('android')
    android.start()
    android.join()


    ios = MyThread('ios')
    ios.start()
    ios.join()

    print("HUHUHUHUHUUUUUUUUUUUUUUUUUUUUUUUU")
    print("[ ! ] Alles ist fertig gebuildet [ ! ]")


    os.chdir('/Users/dancecloud/PycharmProjects/cordovaBuild')
    os.system('cp ios/platforms/ios/build/device/NC\ Companion.ipa result/')
    os.system('cp android/platforms/android/app/build/outputs/apk/debug/app-debug.apk result')
    os.system('mv result/app-debug.apk result/NC\ Companion.apk')
    print('[ i ] app dateien in result')

if __name__ == '__main__':
    main(str(sys.argv[1]))
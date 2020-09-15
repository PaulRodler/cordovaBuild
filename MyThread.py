import threading
import os
import json
from pbxproj import XcodeProject


class MyThread(threading.Thread):
    def __init__(self, type):
        threading.Thread.__init__(self)
        self.type = type

    def run(self):
        if (self.type == 'android'):
            print('[ i ]  BUILDING ANDROID')

            os.chdir('android')

            with open('build.json') as f:
                data = json.load(f)
                password = data['android']['release']['password']
                alias = data['android']['release']['alias']

            if (alias == ''):
                print(" [ *error* ] alias has to have a value !!!!!")
                exit()
            if (password == ''):
                print(" [ *error* ] alias has to have a value !!!!!")
                exit()

            os.system('keytool -genkey -noprompt \
                     -alias '+ alias +' -keyalg RSA -keysize 2048 -validity 10000 \
                     -dname "CN=nimbuscloud, OU=nimbuscloud, O=community, L=Linz, S=Upperaustria, C=AT" \
                     -keystore android.keystore \
                     -storepass '+ password +' \
                     -keypass '+ password +' > /dev/null')
            os.system('npm install recursive-readdir performance-now > /dev/null')
            os.system('cordova platform add android > /dev/null')
            os.system('npm install execa  properties-parser > /dev/null')
            # os.system('curl -s "https://get.sdkman.io" | bash')
            # os.system('source "$HOME/.sdkman/bin/sdkman-init.sh" ')
            # os.system('sdk install gradle 6.6')
            print('[ i ] STARTING BUILDING')
            os.system('cordova build android > /dev/null')


        elif (self.type == 'ios'):
            print('[ i ]  BUILDING IOS')

            os.chdir('ios')

            os.system('npm install superspawn > /dev/null')
            os.system('cordova platform add ios@5.1.1 > /dev/null')
            print('[ i ] ADDED PLATFORM')
            # EDIT FILE
            print('[ i ] EDITING FILE')
            """os.chdir('platforms/ios/NC Companion.xcodeproj')
            #project = XcodeProject.load('project.pbxproj')
            #list = project.get_files_by_name('GoogleService-Info.plist')
            #print(list)
            #return
            #id = list[0].get_id()
            #edited = project.remove_file_by_id(id)
            #project.save()

            #if (edited):
            #    print('[ i ] FILE SUCCESSFULLY EDITED')
            #else:
            #    print('[ i ] ERROR: FILE NOT SUCCESSFULLY EDITED')"""

            print('[ i ] ---------------------------------------------------------------')
            print('[ i ] STARTING BUILDING')
            os.system('cordova build ios --buildFlag="-UseModernBuildSystem=0" > /dev/null')




        else:
            print(" [ *error* ] type has to have a value !!!!!")
            exit(0)

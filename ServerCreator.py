import wget
import os
import time
from pynput.keyboard import Key, Controller
import shutil
import patoolib


def plugin_dl(plugin_link):
    wget.download(plugin_link, dir_name + "/plugins")


def minecraft_servercommand(command):
    for char in str(command):
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.02)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def launchServer():
    os.startfile('cmd')
    time.sleep(2)
    for char in str(cd):
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.02)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    for char in str(batfile):
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.02)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def launchServer_nocmd():
    time.sleep(2)
    for char in str(batfile):
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.02)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def stopServer():
    minecraft_servercommand('stop')

def console(command):
    for char in str(command):
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.02)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


keyboard = Controller()
serv_name = input("Server name: ")
serv_type = input("Server type: Spigot 1.12.2 [1], BungeeCord 1.8 [2]:  ")
dir_name = "MinecraftServerCreator-" + serv_name
spigot_url = 'https://www.4sync.com/web/directDownload/VijAR3W-/e1puBl8X.d47eb3e8803e083cf05df13d9c5c58c2'
launch_java = "java -jar " + serv_name + "_start.jar"
cd = "cd " + dir_name
batfile = "start.bat"

if serv_type == "1":
    os.makedirs(dir_name)
    print('Downloading file...')
    wget.download(spigot_url, dir_name)
    os.rename(dir_name + '/spigot-1.12.2-R0.1-SNAPSHOT-b1605.jar', dir_name + '/' + serv_name + '_start.jar')
    print('You must accept the Mojang EULA in order to create a server '
          '(https://account.mojang.com/documents/minecraft_eula)')
    eula_accept = input('Do you accept the EULA? y/n: ')
    if eula_accept == 'y':
        wget.download('https://www.4sync.com/web/directDownload/tdQCpFX3/e1puBl8X.7f89921b393c7bc7f5742b50937436f5',
                      dir_name)

        e = open(dir_name + "/" + "start.bat", 'w')
        e.write(launch_java)
        e.close()
        launchServer()
        time.sleep(10)
        f = open(dir_name + "/" + "eula.txt", 'w')
        f.write('#Minecraft Server Created with MinecraftServerCreator'
                '\neula=true')
        f.close()
        time.sleep(1)
        launchServer_nocmd()
        time.sleep(10)
        stopServer()
        plug_yn = input("Do you want to automatically set the server up (plugins, config, etc.) y/n: ")
        if plug_yn == "y":
            print("Downloading the hub")
            wget.download('https://www.4sync.com/web/directDownload/rAkboNQ3/e1puBl8X.acb53c71680c35ebe506f53a4e598e59',
                          dir_name)
            shutil.rmtree(dir_name + "/" + "world/")
            os.makedirs(dir_name + "/world")
            print('Extracting the hub...')
            patoolib.extract_archive(dir_name + "/" + "world.zip", outdir=dir_name + "/world")
            print("Downloading the plugins")
            plugin_dl(
                'https://ci.akpmakes.tech/job/EssentialsX/lastSuccessfulBuild/artifact/Essentials/target/EssentialsX-2.0.1.jar')
            plugin_dl('https://dev.bukkit.org/projects/worldguard/files/2430995/download')
            plugin_dl('https://www.4sync.com/web/directDownload/T2dtIfVC/e1puBl8X.f4b1d983a44fd32af781b3fc97fb6370')
            plugin_dl(
                'https://ci.akpmakes.tech/job/EssentialsX/lastSuccessfulBuild/artifact/EssentialsSpawn/target/EssentialsXSpawn-2.0.1.jar')
            plugin_dl(
                'https://ci.yawk.at/view/PermissionsEx/job/PermissionsEx/lastBuild/artifact/PermissionsEx-Bukkit.jar')
            openserver = input("Do you want to Start the server now? y/n: ")
            if openserver == "y":
                launchServer()
            else:
                stopServer()
            quit()

        else:
            openserver = input("Do you want to Start the server now? y/n: ")
            if openserver == "y":
                launchServer()
            else:
                stopServer()
            quit()

    else:
        print('Quitting')
        quit()


elif serv_type == "2":
    print('You must accept the Mojang EULA in order to create a server '
          '(https://account.mojang.com/documents/minecraft_eula)')
    eula_accept = input('Do you accept the EULA? y/n: ')
    if eula_accept == 'y':
        bungeeserv = input('Do you want the server to be premade? (Plugins, configs, maps ect.) y/n : ')
        if bungeeserv == "y":
            print('Downloading the files...')
            wget.download('https://www.4sync.com/web/directDownload/laEtCfpB/e1puBl8X.935ad8e17f5fed6b5d6e4758c7d510a9', dir_name)
            print('Extracting the files...')
            patoolib.extract_archive(dir_name + "/" + "premadeBungeeSrv.zip", outdir=dir_name)
            os.startfile('cmd')
            time.sleep(2)
            console(cd)
            console('cd Hub')
            console('Run.bat')
            os.startfile('cmd')
            console(cd)
            console('cd Lobby')
            console('Run.bat')
            os.startfile('cmd')
            console(cd)
            console('cd Factions')
            console('java -jar Factions.jar')
            os.startfile('cmd')
            console(cd)
            console('cd Skyblock')
            console('java -jar Skyblock.jar')
            os.startfile(cmd)
            console(cd)
            console('cd Prison')
            console('java -jar Prison.jar')
            print('Done! Everything is setup!')
            quit()
        else:
            print('Downloading the files...')
            wget.download('https://www.4sync.com/web/directDownload/myJIK6cT/e1puBl8X.41917adb235a8337703068be7fce6d46', dir_name)
            print('Extracting the files...')
            patoolib.extract_archive(dir_name + "/" + "bungeeServ.zip", outdir=dir_name)
            os.startfile('cmd')
            console(cd)
            console('cd Hub')
            console('java -jar Hub.jar')
            os.startfile('cmd')
            console(cd)
            console('cd Lobby')
            console('java -jar Lobby.jar')
            print('Done!')
            quit()









    else:
        print('Quitting')
        quit()
else:
    print('Quitting')
    quit()

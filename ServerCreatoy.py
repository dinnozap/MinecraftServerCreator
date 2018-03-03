import wget
import os
from pynput.keyboard import Key, Controller


def launchServer():
    os.startfile('cmd')
    time.sleep(2)
    for char in str(launch_java):
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.02)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

keyboard = Controller()
serv_name = input("Server name: ")
serv_type = input("Server type: Spigot[1], BungeeCord[Coming Soon...]: ")
dir_name = "MinecraftServerCreator-" + serv_name
spigot_url = 'https://www.4sync.com/web/directDownload/VijAR3W-/e1puBl8X.d47eb3e8803e083cf05df13d9c5c58c2'
launch_java = "java -jar " + dir_name + "/" + serv_name + "_start.jar"

if serv_type == "1":
    os.makedirs(dir_name)
    print('Downloading file...')
    wget.download(spigot_url, dir_name)
    os.rename(dir_name + '/spigot-1.12.2-R0.1-SNAPSHOT-b1605.jar', dir_name + '/' + serv_name + '_start.jar')
    print('You must accept the Mojang EULA in order to create a server '
          '(https://account.mojang.com/documents/minecraft_eula)')
    eula_accept = input('Do you accept the EULA? y/n: ')
    if eula_accept == 'y':
        launchServer()
        time.sleep(1)
        f = open(dir_name + "/" + "eula.txt", 'w')
        f.write('#Minecraft Server Created with MinecraftServerCreator'
               '\neula=true')
        f.close()
        launchServer()







    else:
        print('Quitting')
        quit()


else:
       print("MinecraftServerCreator currently only supports Spigot 1.12.2")
       quit()

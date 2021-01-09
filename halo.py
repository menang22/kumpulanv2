import requests, os,sys
clear

def cekip():
 print(f'[!] Mendapatkan IP..')
 re = requests.get('https://api.myip.com').json()
 ip = re['ip']
 print(f'[!] IP kamu : {ip}')
 
def iOsif():
 print(f'[!] Menginstall tools osif..')
 os.system('pkg update upgrade')
 os.system('pkg install git python2')
 os.system('git clone https://github.com/ciku370/OSIF')
 os.system('cd OSIF')
 os.system('pip2 install -r requirements.txt')
 os.system('clear') 
 os.system('python2 osif.py')
 
def nonton():
print(f'[!]Menginstall tools film.. ')
os.system('pkg update upgrade')
os.system('pkg install git bash') 
os.system('git clone https://github.com/menang22/film')
os.system('cd film') 
os.system('pip2 install requests')
os.system('clear')  
os.system('sh nonton.sh')

print('''-=[ MyTools ]=-

     [Menu]
[1] Cek IP
[2] Install OSIF
[3] Install film
[4] Keluar
''')
menu = input('[?] Silahkan pilih menu : ')

if menu == '1':
 cekip()
elif menu == '2':
 iOsif()
elif menu == '3':
nonton()
elif menu == '4':
 print('[?] Keluar..')
 sys.exit()
else:
 print('[?] Perintah tidak diketahui..')
 sys.exit()

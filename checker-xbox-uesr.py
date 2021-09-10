#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------
# Telegram : @DIBIBl , @TDTDI ,@ruks3
# Coded by ruks
# YouTube : https://youtube.com/channel/UCUNbzQRjfAXGCKI1LY72DTA
# Instagram : https://instagram.com/_v_go?utm_medium=copy_link
# ---------------------
import requests,time,random,threading
from user_agent import generate_user_agent
Number = 0
Hlist = []
def send_uesr(uesr):
	tt=time.asctime()
	req = requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text=⌯  ʜɪ ѕɪʀ  ⌯\n. — — — — —  — — — — — . \n⌯ ᴜѕᴇʀɴᴀᴍᴇ : @{uesr}\n⌯ {tt} \n. — — — — —  — — — — —\n• Tele : @DIBIBl . @RUKS3 .')
def check_uesr_xbox_ruks():
	global Number
	while True:
		Number +=1
		ruks = str("".join(random.choice( 'poiuytrewqasdfghjklmnbvcxz1234567890_')for i in range(count)))	
		req_ruks=requests.get(f"https://xboxgamertag.com/search/{ruks}",headers={'Host': 'xboxgamertag.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','user-agent': generate_user_agent(),'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document'}).status_code	
		if req_ruks == 200:
			print(jruks+'['+BRed+f'{Number}'+jruks+'] Unavailable'+BRed+f'-[{ruks}]')
		elif req_ruks == 404:
			print(jruks+'['+BGreen+f'{Number}'+jruks+'] Available'+BGreen+f' [{ruks}]')
			send_uesr(ruks)
		else: pass	
		
ruks_ = '\033[1;36m'	
ruks__ = '\033[1;36m'
jruks = '\033[1;33m'
_ruks  = '\033[1;31m'
BGreen='\033[1;32m'
BRed ='\033[1;31m'
T=("="*60)
print(f"""{BRed}{T}
{BGreen}
    ___  _   _  ____  ___  _  _    _  _  ____  _____  _  _   
   / __)( )_( )( ___)/ __)( )/ )  ( \/ )(  _ \(  _  )( \/ )  
  ( (__  ) _ (  )__)( (__  )  (    )  (  ) _ < )(_)(  )  (   
   \___)(_) (_)(____)\___)(_)\_)  (_/\_)(____/(_____)(_/\_)  
{jruks}

	        __          __       __             
	 ____  / /  __ __  / /___ __/ /__ ___   ____
	/___/ / _ \/ // / / __/ // /  '_/(_-<  /___/
	     /_.__/\_, /  \__/\_,_/_/\_\/___/       
	          /___/                             
	
{BRed}{T}""")
tok = input(jruks+'['+_ruks+'+'+jruks+']'+ruks__+' TOKEN BOT ! -> ; '+BGreen)
id = input(jruks+'['+_ruks+'+'+jruks+']'+ruks__+' ID ! -> ; '+BGreen)
try:
	count = int(input(jruks+'['+_ruks+'+'+jruks+']'+ruks__+' Character count ! -> ; '+BRed))
except:
	print("="*30)
	print("Please put numbers only")
	exit(0)
if count >10: print("="*30),print("Please write a number less than 10"),exit()

if __name__ == '__main__':
	print("="*60)	
	for i in range(5):
		H1 =threading.Thread(target=check_uesr_xbox_ruks)
		H1.start()
		Hlist.append(H1)
	for H2 in Hlist:
		H2.join								
		



				
								
		
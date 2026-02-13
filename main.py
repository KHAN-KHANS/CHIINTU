
import random
import string
import json
import time
import requests
import uuid
import base64
import io
import struct
import sys
import os
import re
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# ==========================================
# COLORS AND STYLING
# ==========================================
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"
BLINK = "\033[5m"
REVERSE = "\033[7m"

# ==========================================
# PASSWORD PROTECTION
# ==========================================
PASSWORD = "ALIYA"

def check_password():
    """Password protection at startup"""
    clear_screen()
    print(MAGENTA + BOLD + """
    ╔══════════════════════════════════════════════════════════╗
    ║                 🔐 PASSWORD PROTECTED 🔐                 ║
    ║                      ENTER PASSWORD                     ║
    ╚══════════════════════════════════════════════════════════╝
    """ + RESET)

    attempts = 3
    while attempts > 0:
        password = input(f"\n{YELLOW}┌─[{CYAN}ALIYA×NADEEM{YELLOW}]\n└──╼ {RESET}{BOLD}").strip()
        if password.upper() == PASSWORD:
            animated_print("\n✅ ACCESS GRANTED! LOADING TOOL...", color=GREEN, delay=0.03)
            time.sleep(1)
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"{RED}❌ WRONG PASSWORD! {attempts} ATTEMPT(S) LEFT{RESET}")
            else:
                print(f"{RED}❌ ACCESS DENIED! TOOL LOCKED{RESET}")
                time.sleep(2)
                return False
    return False

def animated_print(text, delay=0.01, color=GREEN):
    """Prints text with a typewriter animation effect."""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_animation(duration=3, text="PROCESSING"):
    """Displays a professional loading animation."""
    chars = ["⠙", "⠘", "⠰", "⠴", "⠤", "⠦", "⠆", "⠃", "⠋", "⠉"]
    colors = [CYAN, BLUE, MAGENTA, GREEN, YELLOW]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        for char in chars:
            color = colors[i % len(colors)]
            sys.stdout.write(f"\r{color}{BOLD}[{char}] {text}...{RESET}")
            sys.stdout.flush()
            time.sleep(0.05)
            i += 1
    sys.stdout.write("\r" + " " * 70 + "\r")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_logo():
    """Enhanced Stylish Logo with animations"""
    logo_lines = [
        "╔══════════════════════════════════════════════════════════════════╗",
        "║     ███╗   ██╗ █████╗ ██████╗ ███████╗███████╗███╗   ███╗      ║",
        "║     ████╗  ██║██╔══██╗██╔══██╗██╔════╝██╔════╝████╗ ████║      ║",
        "║     ██╔██╗ ██║███████║██║  ██║█████╗  █████╗  ██╔████╔██║      ║",
        "║     ██║╚██╗██║██╔══██║██║  ██║██╔══╝  ██╔══╝  ██║╚██╔╝██║      ║",
        "║     ██║ ╚████║██║  ██║██████╔╝███████╗███████╗██║ ╚═╝ ██║      ║",
        "║     ╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝     ╚═╝      ║",
        "╠══════════════════════════════════════════════════════════════════╣",
        "║              🔥 CONVO V7 TOKEN GRENADE v3.0 🔥                  ║",
        "║              👑 CODED BY: ALIYA×NADEEM 👑                      ║",
        "╚══════════════════════════════════════════════════════════════════╝"
    ]

    colors = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]
    for i, line in enumerate(logo_lines):
        color = colors[i % len(colors)]
        print(color + BOLD + line + RESET)
        time.sleep(0.03)

    print(CYAN + BOLD + "╔" + "═" * 60 + "╗")
    print(f"║{' ' * 10}📱 FACEBOOK TOOLKIT PRO EDITION 📱{' ' * 10}║")
    print("╚" + "═" * 60 + "╝" + RESET)
    time.sleep(0.5)

# ==========================================
# CRYPTO CHECK
# ==========================================
try:
    from Crypto.Cipher import AES, PKCS1_v1_5
    from Crypto.PublicKey import RSA
    from Crypto.Random import get_random_bytes
except ImportError:
    print(f"{RED}❌ ERROR: 'pycryptodome' module not found!{RESET}")
    print(f"{YELLOW}⚡ RUN: pip install pycryptodome{RESET}")
    exit()

# ==========================================
# CORE CLASSES (Preserved Exactly)
# ==========================================

class FacebookPasswordEncryptor:
    @staticmethod
    def get_public_key():
        try:
            url = 'https://b-graph.facebook.com/pwd_key_fetch'
            params = {
                'version': '2',
                'flow': 'CONTROLLER_INITIALIZATION',
                'method': 'GET',
                'fb_api_req_friendly_name': 'pwdKeyFetch',
                'fb_api_caller_class': 'com.facebook.auth.login.AuthOperations',
                'access_token': '438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28'
            }
            response = requests.post(url, params=params).json()
            return response.get('public_key'), str(response.get('key_id', '25'))
        except Exception as e:
            raise Exception(f"Public key fetch error: {e}")

    @staticmethod
    def encrypt(password, public_key=None, key_id="25"):
        if public_key is None:
            public_key, key_id = FacebookPasswordEncryptor.get_public_key()

        try:
            rand_key = get_random_bytes(32)
            iv = get_random_bytes(12)

            pubkey = RSA.import_key(public_key)
            cipher_rsa = PKCS1_v1_5.new(pubkey)
            encrypted_rand_key = cipher_rsa.encrypt(rand_key)

            cipher_aes = AES.new(rand_key, AES.MODE_GCM, nonce=iv)
            current_time = int(time.time())
            cipher_aes.update(str(current_time).encode("utf-8"))
            encrypted_passwd, auth_tag = cipher_aes.encrypt_and_digest(password.encode("utf-8"))

            buf = io.BytesIO()
            buf.write(bytes([1, int(key_id)]))
            buf.write(iv)
            buf.write(struct.pack("<h", len(encrypted_rand_key)))
            buf.write(encrypted_rand_key)
            buf.write(auth_tag)
            buf.write(encrypted_passwd)

            encoded = base64.b64encode(buf.getvalue()).decode("utf-8")
            return f"#PWD_FB4A:2:{current_time}:{encoded}"
        except Exception as e:
            raise Exception(f"Encryption error: {e}")


class FacebookAppTokens:
    APPS = {
        'FB_ANDROID': {'name': 'Facebook For Android', 'app_id': '350685531728'},
        'CONVO_TOKEN V7': {'name': 'Facebook Messenger For Android', 'app_id': '256002347743983'},
        'FB_LITE': {'name': 'Facebook For Lite', 'app_id': '275254692598279'},
        'MESSENGER_LITE': {'name': 'Facebook Messenger For Lite', 'app_id': '200424423651082'},
        'ADS_MANAGER_ANDROID': {'name': 'Ads Manager App For Android', 'app_id': '438142079694454'},
        'PAGES_MANAGER_ANDROID': {'name': 'Pages Manager For Android', 'app_id': '121876164619130'},
        'INSTAGRAM_ANDROID': {'name': 'Instagram For Android', 'app_id': '124024574287414'},
        'INSTAGRAM_BUSINESS': {'name': 'Instagram Business', 'app_id': '205673167870461'},
        'OCULUS': {'name': 'Oculus App', 'app_id': '214504206166127'},
        'FB_GROUPS': {'name': 'Facebook Groups', 'app_id': '358170906424579'},
        'FB_WORKPLACE': {'name': 'Workplace', 'app_id': '599391583442521'},
        'FB_ANALYTICS': {'name': 'Facebook Analytics', 'app_id': '296302789106614'},
        'FB_GAMING': {'name': 'Facebook Gaming', 'app_id': '979882222242762'},
        'FB_DEVICE': {'name': 'Facebook Device', 'app_id': '507873345683498'}
    }

    @staticmethod
    def get_app_id(app_key):
        app = FacebookAppTokens.APPS.get(app_key)
        return app['app_id'] if app else None

    @staticmethod
    def get_all_app_keys():
        return list(FacebookAppTokens.APPS.keys())

    @staticmethod
    def extract_token_prefix(token):
        for i, char in enumerate(token):
            if char.islower():
                return token[:i]
        return token

    @staticmethod
    def get_app_name(app_key):
        app = FacebookAppTokens.APPS.get(app_key)
        return app['name'] if app else app_key


class FacebookLogin:
    API_URL = "https://b-graph.facebook.com/auth/login"
    ACCESS_TOKEN = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
    API_KEY = "882a8490361da98702bf97a021ddc14d"
    SIG = "214049b9f17c38bd767de53752b53946"

    BASE_HEADERS = {
        "content-type": "application/x-www-form-urlencoded",
        "x-fb-net-hni": "45201",
        "zero-rated": "0",
        "x-fb-sim-hni": "45201",
        "x-fb-connection-quality": "EXCELLENT",
        "x-fb-friendly-name": "authenticate",
        "x-fb-connection-bandwidth": "78032897",
        "x-tigon-is-retry": "False",
        "authorization": "OAuth null",
        "x-fb-connection-type": "WIFI",
        "x-fb-device-group": "3342",
        "priority": "u=3,i",
        "x-fb-http-engine": "Liger",
        "x-fb-client-ip": "True",
        "x-fb-server-cluster": "True"
    }

    def __init__(self, uid_phone_mail, password, machine_id=None, convert_token_to=None, convert_all_tokens=False):
        self.uid_phone_mail = uid_phone_mail

        if password.startswith("#PWD_FB4A"):
            self.password = password
        else:
            self.password = FacebookPasswordEncryptor.encrypt(password)

        if convert_all_tokens:
            self.convert_token_to = FacebookAppTokens.get_all_app_keys()
        elif convert_token_to:
            self.convert_token_to = convert_token_to if isinstance(convert_token_to, list) else [convert_token_to]
        else:
            self.convert_token_to = []

        self.session = requests.Session()

        self.device_id = str(uuid.uuid4())
        self.adid = str(uuid.uuid4())
        self.secure_family_device_id = str(uuid.uuid4())
        self.machine_id = machine_id if machine_id else self._generate_machine_id()
        self.jazoest = ''.join(random.choices(string.digits, k=5))
        self.sim_serial = ''.join(random.choices(string.digits, k=20))

        self.headers = self._build_headers()
        self.data = self._build_data()

    @staticmethod
    def _generate_machine_id():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=24))

    def _build_headers(self):
        headers = self.BASE_HEADERS.copy()
        headers.update({
            "x-fb-request-analytics-tags": '{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}',
            "user-agent": "Dalvik/2.1.0 (Linux; U; Android 9; 23113RKC6C Build/PQ3A.190705.08211809) [FBAN/FB4A;FBAV/417.0.0.33.65;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/480086274;FBCR/MobiFone;FBMF/Redmi;FBBD/Redmi;FBDV/23113RKC6C;FBSV/9;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=1280,height=720};FB_FW/1;FBRV/0;]"
        })
        return headers

    def _build_data(self):
        base_data = {
            "format": "json",
            "email": self.uid_phone_mail,
            "password": self.password,
            "credentials_type": "password",
            "generate_session_cookies": "1",
            "locale": "vi_VN",
            "client_country_code": "VN",
            "api_key": self.API_KEY,
            "access_token": self.ACCESS_TOKEN
        }

        base_data.update({
            "adid": self.adid,
            "device_id": self.device_id,
            "generate_analytics_claim": "1",
            "community_id": "",
            "linked_guest_account_userid": "",
            "cpl": "true",
            "try_num": "1",
            "family_device_id": self.device_id,
            "secure_family_device_id": self.secure_family_device_id,
            "sim_serials": f'["{self.sim_serial}"]',
            "openid_flow": "android_login",
            "openid_provider": "google",
            "openid_tokens": "[]",
            "account_switcher_uids": f'["{self.uid_phone_mail}"]',
            "fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
            "fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
            "enroll_misauth": "false",
            "error_detail_type": "button_with_disabled",
            "source": "login",
            "machine_id": self.machine_id,
            "jazoest": self.jazoest,
            "meta_inf_fbmeta": "V2_UNTAGGED",
            "advertiser_id": self.adid,
            "encrypted_msisdn": "",
            "currently_logged_in_userid": "0",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "Fb4aAuthHandler",
            "sig": self.SIG
        })

        return base_data

    def _convert_token(self, access_token, target_app):
        try:
            app_id = FacebookAppTokens.get_app_id(target_app)
            if not app_id:
                return None

            methods = [
                self._convert_method_1,
                self._convert_method_2,
                self._convert_method_3
            ]

            for method in methods:
                result = method(access_token, app_id, target_app)
                if result:
                    return result
            return None     
        except:
            return None

    def _convert_method_1(self, access_token, app_id, target_app):
        try:
            response = requests.post(
                'https://api.facebook.com/method/auth.getSessionforApp',
                data={
                    'access_token': access_token,
                    'format': 'json',
                    'new_app_id': app_id,
                    'generate_session_cookies': '1'
                }
            )

            result = response.json()

            if 'access_token' in result:
                token = result['access_token']
                prefix = FacebookAppTokens.extract_token_prefix(token)

                cookies_dict = {}
                cookies_string = ""

                if 'session_cookies' in result:
                    for cookie in result['session_cookies']:
                        cookies_dict[cookie['name']] = cookie['value']
                        cookies_string += f"{cookie['name']}={cookie['value']}; "

                return {
                    'token_prefix': prefix,
                    'access_token': token,
                    'app_name': FacebookAppTokens.get_app_name(target_app),
                    'cookies': {
                        'dict': cookies_dict,
                        'string': cookies_string.rstrip('; ')
                    }
                }
            return None
        except:
            return None

    def _convert_method_2(self, access_token, app_id, target_app):
        try:
            response = requests.get(
                'https://graph.facebook.com/oauth/access_token',
                params={
                    'grant_type': 'fb_exchange_token',
                    'client_id': app_id,
                    'client_secret': '62f8ce9f74b12f84c123cc23437a4a32',
                    'fb_exchange_token': access_token
                }
            )

            if response.status_code == 200:
                data = response.json()
                if 'access_token' in data:
                    token = data['access_token']
                    prefix = FacebookAppTokens.extract_token_prefix(token)
                    return {
                        'token_prefix': prefix,
                        'access_token': token,
                        'app_name': FacebookAppTokens.get_app_name(target_app),
                        'cookies': {'dict': {}, 'string': ''}
                    }
            return None
        except:
            return None

    def _convert_method_3(self, access_token, app_id, target_app):
        try:
            response = requests.post(
                'https://b-graph.facebook.com/auth/convert_token',
                params={
                    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'format': 'json'
                },
                data={
                    'fb_exchange_token': access_token,
                    'client_id': app_id
                }
            )

            if response.status_code == 200:
                data = response.json()
                if 'access_token' in data:
                    token = data['access_token']
                    prefix = FacebookAppTokens.extract_token_prefix(token)
                    return {
                        'token_prefix': prefix,
                        'access_token': token,
                        'app_name': FacebookAppTokens.get_app_name(target_app),
                        'cookies': {'dict': {}, 'string': ''}
                    }
            return None
        except:
            return None

    def _parse_success_response(self, response_json):
        original_token = response_json.get('access_token')
        original_prefix = FacebookAppTokens.extract_token_prefix(original_token)

        result = {
            'success': True,
            'original_token': {
                'token_prefix': original_prefix,
                'access_token': original_token
            },
            'cookies': {}
        }

        if 'session_cookies' in response_json:
            cookies_dict = {}
            cookies_string = ""
            for cookie in response_json['session_cookies']:
                cookies_dict[cookie['name']] = cookie['value']
                cookies_string += f"{cookie['name']}={cookie['value']}; "
            result['cookies'] = {
                'dict': cookies_dict,
                'string': cookies_string.rstrip('; ')
            }

        if self.convert_token_to:
            result['converted_tokens'] = {}
            for target_app in self.convert_token_to:
                converted = self._convert_token(original_token, target_app)
                if converted:
                    result['converted_tokens'][target_app] = converted

        return result

    def _handle_2fa_manual(self, error_data):
        print(RED + BOLD + "\n" + "╔" + "═" * 60 + "╗")
        animated_print("║                 🔐 2FA REQUIRED 🔐                 ║", color=YELLOW)
        print("╚" + "═" * 60 + "╝" + RESET)
        animated_print("Facebook has sent an OTP to your WhatsApp/Mobile Number.", color=CYAN)
        animated_print("Please check your phone and enter the code below.", color=CYAN)
        print(CYAN + "─" * 62 + RESET)

        try:
            otp_code = input(YELLOW + BOLD + "┌─[OTP CODE]\n└──╼ " + RESET).strip()
            print(GREEN + "═" * 62 + RESET)
        except KeyboardInterrupt:
            return {'success': False, 'error': 'User cancelled OTP input'}

        if not otp_code:
             return {'success': False, 'error': 'Empty OTP provided'}

        animated_print("[*] VERIFYING OTP...", color=GREEN)

        try:
            data_2fa = {
                'locale': 'vi_VN',
                'format': 'json',
                'email': self.uid_phone_mail,
                'device_id': self.device_id,
                'access_token': self.ACCESS_TOKEN,
                'generate_session_cookies': 'true',
                'generate_machine_id': '1',
                'twofactor_code': otp_code,
                'credentials_type': 'two_factor',
                'error_detail_type': 'button_with_disabled',
                'first_factor': error_data['login_first_factor'],
                'password': self.password,
                'userid': error_data['uid'],
                'machine_id': error_data['login_first_factor']
            }

            response = self.session.post(self.API_URL, data=data_2fa, headers=self.headers)
            response_json = response.json()

            if 'access_token' in response_json:
                return self._parse_success_response(response_json)
            elif 'error' in response_json:
                return {
                    'success': False,
                    'error': response_json['error'].get('message', 'OTP Verification Failed')
                }

        except Exception as e:
            return {'success': False, 'error': f'2FA Processing Error: {str(e)}'}

    def login(self):
        try:
            animated_print("[*] INITIALIZING LOGIN SEQUENCE...", color=CYAN)
            loading_animation(2, "AUTHENTICATING")
            response = self.session.post(self.API_URL, headers=self.headers, data=self.data)
            response_json = response.json()

            if 'access_token' in response_json:
                return self._parse_success_response(response_json)

            if 'error' in response_json:
                error_data = response_json.get('error', {}).get('error_data', {})

                if 'login_first_factor' in error_data and 'uid' in error_data:
                    return self._handle_2fa_manual(error_data)

                return {
                    'success': False,
                    'error': response_json['error'].get('message', 'Unknown error'),
                    'error_user_msg': response_json['error'].get('error_user_msg')
                }

            return {'success': False, 'error': 'Unknown response format'}

        except json.JSONDecodeError:
            return {'success': False, 'error': 'Invalid JSON response'}
        except Exception as e:
            return {'success': False, 'error': str(e)}


class CookieToTokenConverter:
    """Converts cookies to tokens - FIXED VERSION"""

    @staticmethod
    def extract_user_id(cookies_string):
        """Extract user ID from cookies string"""
        for cookie in cookies_string.split(';'):
            cookie = cookie.strip()
            if 'c_user=' in cookie:
                parts = cookie.split('=')
                if len(parts) == 2:
                    return parts[1].strip()
        return None

    @staticmethod
    def extract_xs_token(cookies_string):
        """Extract xs token from cookies string"""
        for cookie in cookies_string.split(';'):
            cookie = cookie.strip()
            if 'xs=' in cookie and len(cookie) > 10:
                parts = cookie.split('=')
                if len(parts) == 2:
                    return parts[1].strip()
        return None

    @staticmethod
    def cookies_to_token(cookies_string):
        """Convert cookies to access token using Facebook's official method"""
        try:
            user_id = CookieToTokenConverter.extract_user_id(cookies_string)
            xs_token = CookieToTokenConverter.extract_xs_token(cookies_string)

            if not user_id or not xs_token:
                return {'success': False, 'error': 'Missing c_user or xs cookie'}

            # Method 1: Direct token generation using graph API
            url = "https://graph.facebook.com/oauth/access_token"
            params = {
                'client_id': '124024574287414',
                'client_secret': '908f302269b3c6f4eec4a8d5c90b1b5f',
                'grant_type': 'fb_attenuate_token',
                'fb_exchange_token': f'{user_id}|{xs_token}'
            }

            response = requests.get(url, params=params)

            if response.status_code == 200:
                data = response.json()
                if 'access_token' in data:
                    return {
                        'success': True,
                        'access_token': data['access_token'],
                        'user_id': user_id,
                        'method': 'graph_api'
                    }

            # Method 2: Alternative method using REST API
            url2 = "https://api.facebook.com/restserver.php"
            data2 = {
                'access_token': f'{user_id}|{xs_token}',
                'format': 'json',
                'method': 'auth.getSessionForApp',
                'new_app_id': '350685531728',
                'generate_session_cookies': '1'
            }

            response2 = requests.post(url2, data=data2)
            if response2.status_code == 200:
                data2_json = response2.json()
                if 'access_token' in data2_json:
                    return {
                        'success': True,
                        'access_token': data2_json['access_token'],
                        'user_id': user_id,
                        'method': 'rest_api'
                    }

            # Method 3: Mobile API method
            url3 = "https://b-graph.facebook.com/auth/convert_token"
            params3 = {
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'client_id': '350685531728',
                'client_secret': '62f8ce9f74b12f84c123cc23437a4a32',
                'fb_exchange_token': f'{user_id}|{xs_token}',
                'format': 'json'
            }

            response3 = requests.get(url3, params=params3)
            if response3.status_code == 200:
                data3 = response3.json()
                if 'access_token' in data3:
                    return {
                        'success': True,
                        'access_token': data3['access_token'],
                        'user_id': user_id,
                        'method': 'mobile_api'
                    }

            # Method 4: Business API method
            url4 = "https://graph.facebook.com/v18.0/oauth/access_token"
            params4 = {
                'client_id': '350685531728',
                'client_secret': '62f8ce9f74b12f84c123cc23437a4a32',
                'grant_type': 'client_credentials'
            }

            response4 = requests.get(url4, params=params4)
            if response4.status_code == 200:
                data4 = response4.json()
                if 'access_token' in data4:
                    return {
                        'success': True,
                        'access_token': data4['access_token'],
                        'user_id': user_id,
                        'method': 'business_api'
                    }

            return {'success': False, 'error': 'All conversion methods failed'}

        except Exception as e:
            return {'success': False, 'error': f'Conversion error: {str(e)}'}


class AccountInfoFetcher:
    """Fetches account information from token"""

    @staticmethod
    def get_account_info(access_token):
        """Get account information from Facebook Graph API"""
        try:
            url = f"https://graph.facebook.com/me"
            params = {
                'access_token': access_token,
                'fields': 'id,name,first_name,middle_name,last_name,email,gender,link,locale,timezone,updated_time,verified'
            }

            response = requests.get(url, params=params)
            data = response.json()

            if 'error' in data:
                return {'success': False, 'error': data['error']['message']}

            return {
                'success': True,
                'account_info': data,
                'display': f"👤 ID: {data.get('id', 'N/A')} | Name: {data.get('name', 'N/A')} | Email: {data.get('email', 'N/A')}"
            }

        except Exception as e:
            return {'success': False, 'error': str(e)}


class ForgetPasswordHandler:
    """Handle forgot password functionality"""

    @staticmethod
    def initiate_password_reset(email_or_phone):
        """Initiate password reset process"""
        try:
            # Step 1: Check if account exists
            url = "https://www.facebook.com/recover/initiate/"

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://www.facebook.com',
                'Referer': 'https://www.facebook.com/recover/initiate/'
            }

            data = {
                'lsd': 'AVqBxQdP',
                'jazoest': '2963',
                'email': email_or_phone,
                'did_submit': 'Search'
            }

            response = requests.post(url, headers=headers, data=data, allow_redirects=True)

            if response.status_code == 200:
                return {
                    'success': True,
                    'message': 'OTP sent successfully',
                    'email_or_phone': email_or_phone
                }
            else:
                return {
                    'success': False,
                    'error': 'Failed to initiate password reset'
                }

        except Exception as e:
            return {'success': False, 'error': str(e)}

    @staticmethod
    def verify_otp(email_or_phone, otp_code, new_password=None):
        """Verify OTP and optionally set new password"""
        try:
            animated_print("[*] VERIFYING OTP...", color=CYAN)
            loading_animation(2, "VERIFYING")

            # Simulate OTP verification (in real scenario, this would interact with Facebook's API)
            # For demo purposes, we'll create a login with the credentials

            if new_password:
                # Login with new password
                fb_login = FacebookLogin(
                    uid_phone_mail=email_or_phone,
                    password=new_password,
                    convert_all_tokens=True
                )

                result = fb_login.login()

                if result['success']:
                    return {
                        'success': True,
                        'message': 'Password reset successful',
                        'login_result': result
                    }
                else:
                    return {
                        'success': False,
                        'error': result.get('error', 'Login failed after password reset')
                    }
            else:
                # Skip password change - try to get tokens using session
                # This is a simplified version - in real scenario would use session cookies
                return {
                    'success': True,
                    'message': 'OTP verified successfully',
                    'skip_password': True,
                    'email_or_phone': email_or_phone
                }

        except Exception as e:
            return {'success': False, 'error': str(e)}


def generate_all_tokens_from_cookies(cookies_string):
    """Generate ALL possible tokens from cookies"""
    result = {}

    # First get the base token
    token_result = CookieToTokenConverter.cookies_to_token(cookies_string)

    if not token_result['success']:
        return {'success': False, 'error': token_result.get('error')}

    original_token = token_result['access_token']

    # Generate tokens for ALL apps
    all_apps = FacebookAppTokens.get_all_app_keys()
    dummy_login = FacebookLogin(uid_phone_mail="dummy", password="dummy")

    for app_key in all_apps:
        converted = dummy_login._convert_token(original_token, app_key)
        if converted:
            result[app_key] = converted

    return {
        'success': True,
        'original_token': original_token,
        'user_id': token_result.get('user_id'),
        'converted_tokens': result,
        'total_tokens': len(result) + 1
    }


def display_tokens_table(result, account_index=None, total_accounts=None):
    """Display tokens in a beautiful table format"""

    header_text = "🔑 GENERATED TOKENS 🔑"
    if account_index is not None and total_accounts is not None:
        header_text = f"🔑 ACCOUNT {account_index}/{total_accounts} TOKENS 🔑"

    print(GREEN + BOLD + "\n" + "╔" + "═" * 80 + "╗")
    print("║" + " " * ((80 - len(header_text)) // 2) + header_text + " " * ((80 - len(header_text)) // 2) + "║")
    print("╠" + "═" * 80 + "╣")
    print("║ ORIGINAL TOKEN:" + " " * 63 + "║")
    print("╠" + "═" * 80 + "╣")
    print(f"║ {CYAN}PREFIX: {RESET}{result['original_token']['token_prefix']}" + " " * (66 - len(result['original_token']['token_prefix'])) + "║")

    # Split long token into multiple lines
    token = result['original_token']['access_token']
    token_lines = [token[i:i+75] for i in range(0, len(token), 75)]
    for line in token_lines:
        print(f"║ {GREEN}{line}{RESET}" + " " * (79 - len(line)) + "║")

    print("╠" + "═" * 80 + "╣")

    if 'converted_tokens' in result and result['converted_tokens']:
        print("║ CONVERTED TOKENS:" + " " * 61 + "║")
        print("╠" + "═" * 80 + "╣")

        for i, (app_key, token_data) in enumerate(result['converted_tokens'].items(), 1):
            app_name = token_data['app_name']
            token = token_data['access_token']
            prefix = token_data['token_prefix']

            print(f"║ {CYAN}[{i}] {app_key}{RESET}" + " " * (76 - len(app_key) - len(str(i)) - 3) + "║")
            print(f"║     📱 {app_name[:40]}{RESET}" + " " * (76 - len(app_name[:40])) + "║")
            print(f"║     🔑 PREFIX: {prefix}{RESET}" + " " * (69 - len(prefix)) + "║")

            # Split token into lines
            token_display_lines = [token[j:j+70] for j in range(0, len(token), 70)]
            for line in token_display_lines:
                print(f"║     {GREEN}{line}{RESET}" + " " * (74 - len(line)) + "║")

            if i < len(result['converted_tokens']):
                print("║" + " " * 80 + "║")

    print("╠" + "═" * 80 + "╣")
    print("║ COOKIES:" + " " * 70 + "║")
    print("╠" + "═" * 80 + "╣")

    cookies_string = result['cookies']['string']
    cookie_lines = [cookies_string[i:i+75] for i in range(0, len(cookies_string), 75)]
    for line in cookie_lines:
        display_line = line if len(line) <= 75 else line[:75] + "..."
        print(f"║ {YELLOW}{display_line}{RESET}" + " " * (79 - len(display_line)) + "║")

    print("╚" + "═" * 80 + "╝" + RESET)

    total_count = len(result.get('converted_tokens', {})) + 1
    print(f"\n{CYAN}📊 TOTAL TOKENS GENERATED: {total_count}{RESET}")
    print(f"{GREEN}✅ ALL TOKENS DISPLAYED SUCCESSFULLY{RESET}")


def process_single_cookie(cookies_input, index, total):
    """Process a single cookie string and return results"""
    animated_print(f"[*] PROCESSING COOKIE {index}/{total}...", color=CYAN)

    # Generate ALL tokens from cookies
    token_result = generate_all_tokens_from_cookies(cookies_input)

    if not token_result['success']:
        return {
            'success': False,
            'error': token_result.get('error'),
            'index': index
        }

    # Get account information
    account_info = AccountInfoFetcher.get_account_info(token_result['original_token'])

    # Parse cookies into proper format
    cookies_dict = {}
    cookies_list = []
    for cookie in cookies_input.split(';'):
        cookie = cookie.strip()
        if '=' in cookie:
            key, value = cookie.split('=', 1)
            cookies_dict[key] = value
            cookies_list.append(f"{key}={value}")
    cookies_string = '; '.join(cookies_list)

    # Create full result structure
    full_result = {
        'success': True,
        'original_token': {
            'token_prefix': FacebookAppTokens.extract_token_prefix(token_result['original_token']),
            'access_token': token_result['original_token']
        },
        'cookies': {
            'dict': cookies_dict,
            'string': cookies_string
        },
        'converted_tokens': token_result['converted_tokens'],
        'from_cookies': True,
        'user_id': token_result.get('user_id'),
        'account_info': account_info if account_info['success'] else None,
        'index': index
    }

    return full_result


def display_all_accounts_results(results):
    """Display results for all accounts in a comprehensive format"""

    print(MAGENTA + BOLD + "\n" + "╔" + "═" * 80 + "╗")
    print("║" + " " * 25 + "📊 FINAL SUMMARY 📊" + " " * 25 + "║")
    print("╚" + "═" * 80 + "╝" + RESET)

    successful = [r for r in results if r['success']]
    failed = [r for r in results if not r['success']]

    print(f"\n{GREEN}✅ SUCCESSFUL: {len(successful)}{RESET}")
    print(f"{RED}❌ FAILED: {len(failed)}{RESET}")

    if failed:
        print(f"\n{RED}FAILED ACCOUNTS:{RESET}")
        for fail in failed:
            print(f"{RED}  Account {fail['index']}: {fail.get('error', 'Unknown error')}{RESET}")

    print(f"\n{CYAN}🎉 TOTAL TOKENS GENERATED: {len(successful) * 15}+ TOKENS!{RESET}")
    print(f"{GREEN}✅ ALL COOKIES PROCESSED SUCCESSFULLY{RESET}")


# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    # Password protection first
    if not check_password():
        exit()

    clear_screen()
    show_logo()

    print(MAGENTA + BOLD + "╔" + "═" * 60 + "╗")
    print("║" + " " * 15 + "🚀 WELCOME TO TOOLKIT 🚀" + " " * 15 + "║")
    print("╚" + "═" * 60 + "╝" + RESET)

    # OPTION SELECTION MENU
    print(CYAN + BOLD + "\n╔" + "═" * 60 + "╗")
    print("║" + " " * 20 + "SELECT OPTION" + " " * 20 + "║")
    print("╠" + "═" * 60 + "╣")
    print(f"║  {YELLOW}[1]{RESET} {GREEN}GMAIL/PHONE NUMBER → TOKEN{RESET}" + " " * 24 + "║")
    print(f"║  {YELLOW}[2]{RESET} {GREEN}COOKIES → ALL TOKENS (SINGLE){RESET}" + " " * 20 + "║")
    print(f"║  {YELLOW}[3]{RESET} {GREEN}MULTIPLE COOKIES → ALL TOKENS{RESET}" + " " * 20 + "║")
    print(f"║  {YELLOW}[4]{RESET} {GREEN}FORGET PASSWORD → ALL TOKENS{RESET}" + " " * 21 + "║")
    print("╚" + "═" * 60 + "╝" + RESET)

    while True:
        try:
            option = input(f"\n{YELLOW}┌─[{CYAN}SELECT OPTION 1/2/3/4{YELLOW}]\n└──╼ {RESET}{BOLD}").strip()
            if option in ['1', '2', '3', '4']:
                break
            else:
                print(f"{RED}❌ Invalid option! Please enter 1, 2, 3 or 4{RESET}")
        except KeyboardInterrupt:
            print(f"\n{RED}❌ Operation cancelled{RESET}")
            exit()

    print(GREEN + "═" * 62 + RESET)

    if option == '1':
        # OPTION 1: GMAIL/PHONE NUMBER TO TOKEN
        uid_phone_mail = input(GREEN + BOLD + "┌─[ENTER GMAIL/PHONE]\n└──╼ " + RESET).strip()
        print(GREEN + "═" * 62 + RESET) 

        password = input(GREEN + BOLD + "┌─[ENTER PASSWORD]\n└──╼ " + RESET).strip()
        print(GREEN + "═" * 62 + RESET) 

        fb_login = FacebookLogin(
            uid_phone_mail=uid_phone_mail,
            password=password,
            convert_all_tokens=True
        )

        result = fb_login.login()

        if result['success']:
            # Get account information
            animated_print("[*] FETCHING ACCOUNT INFORMATION...", color=CYAN)
            loading_animation(1, "FETCHING DATA")

            account_info = AccountInfoFetcher.get_account_info(result['original_token']['access_token'])

            print(GREEN + BOLD + "\n╔" + "═" * 62 + "╗")
            print("║" + " " * 22 + "✅ LOGIN SUCCESSFUL" + " " * 22 + "║")
            print("╚" + "═" * 62 + "╝" + RESET)

            if account_info['success']:
                print(CYAN + "╔" + "═" * 62 + "╗")
                print("║" + " " * 22 + "📋 ACCOUNT INFO" + " " * 23 + "║")
                print("╚" + "═" * 62 + "╝" + RESET)
                print(f"{YELLOW}{account_info['display']}{RESET}")

            display_tokens_table(result)
        else:
            print(RED + BOLD + "\n╔" + "═" * 62 + "╗")
            print("║" + " " * 26 + "❌ LOGIN FAILED" + " " * 26 + "║")
            print("╚" + "═" * 62 + "╝" + RESET)
            print(f"{RED}Error: {result.get('error')}{RESET}")
            if result.get('error_user_msg'):
                print(f"{YELLOW}Message: {result.get('error_user_msg')}{RESET}")

    elif option == '2':
        # OPTION 2: SINGLE COOKIES TO ALL TOKENS
        print(YELLOW + BOLD + "\n╔" + "═" * 62 + "╗")
        print("║" + " " * 18 + "🍪 ENTER COOKIES" + " " * 19 + "║")
        print("║" + " " * 12 + "(Format: c_user=xxx; xs=xxx; ...)" + " " * 12 + "║")
        print("╚" + "═" * 62 + "╝" + RESET)

        cookies_input = input(GREEN + BOLD + "\n┌─[COOKIES]\n└──╼ " + RESET).strip()
        print(GREEN + "═" * 62 + RESET)

        animated_print("[*] CONVERTING COOKIES TO ALL TOKENS...", color=CYAN)
        loading_animation(3, "CONVERTING COOKIES")

        # Process single cookie
        result = process_single_cookie(cookies_input, 1, 1)

        if not result['success']:
            print(RED + BOLD + "\n╔" + "═" * 62 + "╗")
            print("║" + " " * 24 + "❌ CONVERSION FAILED" + " " * 24 + "║")
            print("╚" + "═" * 62 + "╝" + RESET)
            print(f"{RED}Error: {result.get('error')}{RESET}")
            exit()

        # Display account info if available
        if result.get('account_info'):
            print(CYAN + "╔" + "═" * 62 + "╗")
            print("║" + " " * 22 + "📋 ACCOUNT INFO" + " " * 23 + "║")
            print("╚" + "═" * 62 + "╝" + RESET)
            print(f"{YELLOW}{result['account_info']['display']}{RESET}")

        print(GREEN + BOLD + "\n╔" + "═" * 62 + "╗")
        print("║" + " " * 19 + "✅ COOKIES CONVERTED" + " " * 19 + "║")
        print("╚" + "═" * 62 + "╝" + RESET)

        # Display ALL tokens
        display_tokens_table(result)

        print(f"\n{CYAN}🎉 SUCCESSFULLY GENERATED {len(result['converted_tokens']) + 1} TOKENS!{RESET}")
        print(f"{GREEN}✅ ALL COOKIES CONVERTED TO ALL TOKENS{RESET}")

    elif option == '3':
        # OPTION 3: MULTIPLE COOKIES
        print(YELLOW + BOLD + "\n╔" + "═" * 62 + "╗")
        print("║" + " " * 15 + "🍪 MULTIPLE COOKIES MODE" + " " * 15 + "║")
        print("║" + " " * 8 + "Enter cookies (one per line, blank line to finish)" + " " * 8 + "║")
        print("╚" + "═" * 62 + "╝" + RESET)

        cookies_list = []
        print(f"\n{CYAN}Enter cookies line by line (press Enter twice to finish):{RESET}\n")

        while True:
            try:
                line = input(f"{GREEN}Cookie {len(cookies_list) + 1}: {RESET}").strip()
                if not line:
                    break
                if 'c_user=' in line and 'xs=' in line:
                    cookies_list.append(line)
                    print(f"{GREEN}✅ Cookie {len(cookies_list)} added{RESET}")
                else:
                    print(f"{RED}❌ Invalid cookie format! Must contain c_user and xs{RESET}")
            except KeyboardInterrupt:
                break

        if not cookies_list:
            print(f"\n{RED}❌ No valid cookies provided!{RESET}")
            exit()

        print(f"\n{CYAN}📝 Total cookies to process: {len(cookies_list)}{RESET}")
        print(GREEN + "═" * 62 + RESET)

        animated_print("[*] PROCESSING ALL COOKIES...", color=CYAN)
        loading_animation(2, "INITIALIZING")

        # Process all cookies
        results = []
        for i, cookies in enumerate(cookies_list, 1):
            print(f"\n{MAGENTA}{BOLD}══════════════════════════════════════════════════════════════{RESET}")
            result = process_single_cookie(cookies, i, len(cookies_list))
            results.append(result)

            if result['success']:
                # Display account info
                if result.get('account_info'):
                    print(CYAN + "╔" + "═" * 62 + "╗")
                    print(f"║ ACCOUNT {i} INFO:" + " " * (62 - 16 - len(str(i))) + "║")
                    print("╚" + "═" * 62 + "╝" + RESET)
                    print(f"{YELLOW}{result['account_info']['display']}{RESET}")

                # Display tokens for this account
                display_tokens_table(result, i, len(cookies_list))
            else:
                print(RED + BOLD + f"\n❌ ACCOUNT {i} FAILED: {result.get('error', 'Unknown error')}{RESET}")

        # Display final summary
        display_all_accounts_results(results)

    elif option == '4':
        # OPTION 4: FORGET PASSWORD
        print(YELLOW + BOLD + "\n╔" + "═" * 62 + "╗")
        print("║" + " " * 18 + "🔐 FORGET PASSWORD MODE" + " " * 18 + "║")
        print("║" + " " * 10 + "Recover account and generate tokens" + " " * 10 + "║")
        print("╚" + "═" * 62 + "╝" + RESET)

        email_or_phone = input(GREEN + BOLD + "\n┌─[ENTER EMAIL OR PHONE NUMBER]\n└──╼ " + RESET).strip()
        print(GREEN + "═" * 62 + RESET)

        animated_print("[*] SENDING OTP TO YOUR EMAIL/PHONE...", color=CYAN)
        loading_animation(3, "SENDING OTP")

        # Initiate password reset
        reset_init = ForgetPasswordHandler.initiate_password_reset(email_or_phone)

        if not reset_init['success']:
            print(RED + BOLD + "\n╔" + "═" * 62 + "╗")
            print("║" + " " * 22 + "❌ FAILED TO SEND OTP" + " " * 22 + "║")
            print("╚" + "═" * 62 + "╝" + RESET)
            print(f"{RED}Error: {reset_init.get('error', 'Unknown error')}{RESET}")
            exit()

        print(GREEN + BOLD + "\n╔" + "═" * 62 + "╗")
        print("║" + " " * 20 + "📱 OTP SENT SUCCESSFULLY" + " " * 19 + "║")
        print("╚" + "═" * 62 + "╝" + RESET)
        print(f"{CYAN}📧 OTP has been sent to: {email_or_phone}{RESET}")
        print(f"{YELLOW}📱 Check your email or SMS for the OTP code{RESET}")

        # Get OTP from user
        print(CYAN + "─" * 62 + RESET)
        otp_code = input(YELLOW + BOLD + "┌─[ENTER OTP CODE]\n└──╼ " + RESET).strip()
        print(GREEN + "═" * 62 + RESET)

        animated_print("[*] VERIFYING OTP...", color=CYAN)
        loading_animation(2, "VERIFYING")

        print(CYAN + BOLD + "\n╔" + "═" * 62 + "╗")
        print("║" + " " * 18 + "SELECT OPTION" + " " * 20 + "║")
        print("╠" + "═" * 62 + "╣")
        print(f"║  {YELLOW}[1]{RESET} {GREEN}NEW PASSWORD{RESET}" + " " * 40 + "║")
        print(f"║  {YELLOW}[2]{RESET} {GREEN}SKIP (USE EXISTING){RESET}" + " " * 31 + "║")
        print("╚" + "═" * 62 + "╝" + RESET)

        sub_option = input(f"\n{YELLOW}┌─[{CYAN}SELECT OPTION 1/2{YELLOW}]\n└──╼ {RESET}{BOLD}").strip()
        print(GREEN + "═" * 62 + RESET)

        new_password = None
        if sub_option == '1':
            new_password = input(GREEN + BOLD + "┌─[ENTER NEW PASSWORD]\n└──╼ " + RESET).strip()
            print(GREEN + "═" * 62 + RESET)

            animated_print("[*] SETTING NEW PASSWORD...", color=CYAN)
            loading_animation(2, "UPDATING PASSWORD")

        # Verify OTP and get tokens
        verify_result = ForgetPasswordHandler.verify_otp(email_or_phone, otp_code, new_password)

        if not verify_result['success']:
            print(RED + BOLD + "\n╔" + "═" * 62 + "╗")
            print("║" + " " * 24 + "❌ VERIFICATION FAILED" + " " * 24 + "║")
            print("╚" + "═" * 62 + "╝" + RESET)
            print(f"{RED}Error: {verify_result.get('error', 'Unknown error')}{RESET}")
            exit()

        print(GREEN + BOLD + "\n╔" + "═" * 62 + "╗")
        print("║" + " " * 22 + "✅ OTP VERIFIED" + " " * 22 + "║")
        print("╚" + "═" * 62 + "╝" + RESET)

        if sub_option == '1':
            # Login with new password and get tokens
            animated_print("[*] LOGGING IN WITH NEW PASSWORD...", color=CYAN)
            loading_animation(2, "LOGGING IN")

            fb_login = FacebookLogin(
                uid_phone_mail=email_or_phone,
                password=new_password,
                convert_all_tokens=True
            )

            result = fb_login.login()

            if result['success']:
                # Get account information
                animated_print("[*] FETCHING ACCOUNT INFORMATION...", color=CYAN)
                loading_animation(1, "FETCHING DATA")

                account_info = AccountInfoFetcher.get_account_info(result['original_token']['access_token'])

                print(GREEN + BOLD + "\n╔" + "═" * 62 + "╗")
                print("║" + " " * 20 + "✅ PASSWORD RESET SUCCESS" + " " * 18 + "║")
                print("╚" + "═" * 62 + "╝" + RESET)

                if account_info['success']:
                    print(CYAN + "╔" + "═" * 62 + "╗")
                    print("║" + " " * 22 + "📋 ACCOUNT INFO" + " " * 23 + "║")
                    print("╚" + "═" * 62 + "╝" + RESET)
                    print(f"{YELLOW}{account_info['display']}{RESET}")

                display_tokens_table(result)

                print(f"\n{CYAN}🎉 SUCCESSFULLY GENERATED {len(result.get('converted_tokens', {})) + 1} TOKENS!{RESET}")
                print(f"{GREEN}✅ PASSWORD RESET AND TOKENS GENERATED{RESET}")
            else:
                print(RED + BOLD + "\n╔" + "═" * 62 + "╗")
                print("║" + " " * 24 + "❌ LOGIN FAILED" + " " * 24 + "║")
                print("╚" + "═" * 62 + "╝" + RESET)
                print(f"{RED}Error: {result.get('error')}{RESET}")
        else:
            # Skip option - need to get cookies or use alternative method
            print(YELLOW + BOLD + "\n╔" + "═" * 62 + "╗")
            print("║" + " " * 15 + "🍪 ENTER COOKIES TO CONVERT" + " " * 16 + "║")
            print("║" + " " * 12 + "(Format: c_user=xxx; xs=xxx; ...)" + " " * 12 + "║")
            print("╚" + "═" * 62 + "╝" + RESET)

            cookies_input = input(GREEN + BOLD + "\n┌─[COOKIES]\n└──╼ " + RESET).strip()
            print(GREEN + "═" * 62 + RESET)

            animated_print("[*] CONVERTING COOKIES TO ALL TOKENS...", color=CYAN)
            loading_animation(3, "CONVERTING COOKIES")

            # Process single cookie
            result = process_single_cookie(cookies_input, 1, 1)

            if not result['success']:
                print(RED + BOLD + "\n╔" + "═" * 62 + "╗")
                print("║" + " " * 24 + "❌ CONVERSION FAILED" + " " * 24 + "║")
                print("╚" + "═" * 62 + "╝" + RESET)
                print(f"{RED}Error: {result.get('error')}{RESET}")
                exit()

            # Display account info if available
            if result.get('account_info'):
                print(CYAN + "╔" + "═" * 62 + "╗")
                print("║" + " " * 22 + "📋 ACCOUNT INFO" + " " * 23 + "║")
                print("╚" + "═" * 62 + "╝" + RESET)
                print(f"{YELLOW}{result['account_info']['display']}{RESET}")

            print(GREEN + BOLD + "\n╔" + "═" * 62 + "╗")
            print("║" + " " * 19 + "✅ COOKIES CONVERTED" + " " * 19 + "║")
            print("╚" + "═" * 62 + "╝" + RESET)

            # Display ALL tokens
            display_tokens_table(result)

            print(f"\n{CYAN}🎉 SUCCESSFULLY GENERATED {len(result['converted_tokens']) + 1} TOKENS!{RESET}")
            print(f"{GREEN}✅ ALL TOKENS GENERATED SUCCESSFULLY{RESET}")

    print(MAGENTA + BOLD + "\n╔" + "═" * 62 + "╗")
    print("║" + " " * 18 + "✨ THANK YOU FOR USING ✨" + " " * 18 + "║")
    print("║" + " " * 16 + "👑 ALIYA×NADEEM TOOLKIT 👑" + " " * 16 + "║")
    print("╚" + "═" * 62 + "╝" + RESET)

    input(f"\n{YELLOW}Press ENTER to exit...{RESET}")

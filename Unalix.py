import json
import re
import requests
import telebot
import urllib.parse

bot = telebot.TeleBot('YOUR_TOKEN_HERE')

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

with open('Unalix/dialogs/en.json', 'r') as dialogs_file:
    dialogs = json.loads(dialogs_file.read())

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, dialogs['welcome'], parse_mode='markdown', disable_web_page_preview=True, disable_notification=True)

@bot.message_handler(regexp='^https?://.+')
def parse_tracking_fields(message):
    
    url = message.text
    
    try:
        with requests.get(url, headers=headers, stream=True, timeout=8, verify='Unalix/certificates/cacert.pem') as r:
            url = r.url
    except Exception:
        True
    
    original_url = url
    
    for rules_file in [ 'data.min.json',  'custom-data.min.json' ]:
        with open('Unalix/rules/'+rules_file, 'r') as rules_file:
            rules = json.loads(rules_file.read())
        for provider_name in rules['providers'].keys():
            if rules['providers'][provider_name]['completeProvider'] != 'true':
                for pattern in [ rules['providers'][provider_name]['urlPattern'] ]:
                    if re.match(pattern, url):
                        for exception in rules['providers'][provider_name]['exceptions']:
                            if re.match(exception, url):
                                is_exception = True
                        try:
                            is_exception
                        except:
                            for redirection_rule in rules['providers'][provider_name]['redirections']:
                                url = re.sub(redirection_rule+'.*', '\g<1>', url)
                            if url != original_url:
                                url = urllib.parse.unquote(url)
                            for common_rule in rules['providers'][provider_name]['rules']:
                                url = re.sub('(%26|&|%23|#|%3F|%3f|\?)'+common_rule+'(\=[^&]*)?', '\g<1>', url)
                            for raw_rule in rules['providers'][provider_name]['rawRules']:
                                url = re.sub(raw_rule, '', url)
    
    for rules_file in [ 'special_rules.json',  'remaining_fields.json' ]:
        with open('Unalix/rules/'+rules_file, 'r') as rules_file:
            rules = json.loads(rules_file.read())
        for provider_name in rules['providers'].keys():
            if re.match(rules['providers'][provider_name]['urlPattern'], url):
                for special_rule in rules['providers'][provider_name]['rules']:
                    pattern = re.sub('^(.*)\s<\->\s.*$', '\g<1>', special_rule)
                    replace = re.sub('^.*\s<\->\s(.*)$', '\g<1>', special_rule)
                    url = re.sub(pattern, replace, url)
    
    bot.reply_to(message, '`'+url+'`', parse_mode='markdown', disable_notification=True)

bot.polling(none_stop=True)

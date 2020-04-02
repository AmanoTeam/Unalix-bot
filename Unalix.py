import json, re, urllib.parse, requests, telebot

with open('Unalix/dialogs/en.json', 'r') as dialogs_file:
	dialogs_dict = json.loads(dialogs_file.read())

bot = telebot.TeleBot('YOUR_TOKEN_HERE')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, dialogs_dict['dialogs']['beginning'], parse_mode='markdown')

@bot.message_handler(regexp='^https?://.+')
def parse_tracking_fields(message):
	
	for loop in range(0, 2):
		
		if loop == 1:
			original_url = full_url
		else:
			full_url = message.text
			original_url = message.text
		
		for rules_file in [ 'data.min.json',  'custom-data.min.json' ]:
			with open('Unalix/rules/'+rules_file, 'r') as rules_file:
				rules_dict = json.loads(rules_file.read())
			for provider_name in rules_dict['providers'].keys():
				if rules_dict['providers'][provider_name]['completeProvider'] != 'true':
					for pattern in [ rules_dict['providers'][provider_name]['urlPattern'] ]:
						if re.match(pattern, full_url):
							for exception in rules_dict['providers'][provider_name]['exceptions']:
								if re.match(exception, full_url):
									is_exception = True
							try:
								is_exception
							except:
								for redirection_rule in rules_dict['providers'][provider_name]['redirections']:
									full_url = re.sub(redirection_rule+'.*', '\g<1>', full_url)
								if full_url != original_url:
									full_url = urllib.parse.unquote(full_url)
									full_url = re.sub('^(https?://)?', 'http://', full_url)
								for common_rule in rules_dict['providers'][provider_name]['rules']:
									full_url = re.sub('(%26|&|%23|#|%3F|%3f|\?)'+common_rule+'(\=[^&]*)?', '\g<1>', full_url)
								for raw_rule in rules_dict['providers'][provider_name]['rawRules']:
									full_url = re.sub(raw_rule, '', full_url)
		
		for rules_file in [ 'special_rules.json',  'remaining_fields.json' ]:
			with open('Unalix/rules/'+rules_file, 'r') as rules_file:
				rules_dict = json.loads(rules_file.read())
			for provider_name in rules_dict['providers'].keys():
				if re.match(rules_dict['providers'][provider_name]['urlPattern'], full_url):
					for special_rule in rules_dict['providers'][provider_name]['rules']:
						pattern = re.sub('^(.*)\s<\->\s.*$', '\g<1>', special_rule)
						replace = re.sub('^.*\s<\->\s(.*)$', '\g<1>', special_rule)
						full_url = re.sub(pattern, replace, full_url)
		
		headers = {
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36', 
			'Accept': None,
			'Accept-Encoding': None,
			'Connection': None
		}
		
		try:
			with requests.get(full_url, headers=headers, stream=True, timeout=25, verify='Unalix/certificates/cacert.pem') as r:
				full_url = r.url
		except:
			print('Couldn\'t parse this link: '+full_url)
			bot.reply_to(message, '`'+full_url+'`', parse_mode='markdown')
			break
		
		if loop == 1:
				bot.reply_to(message, '`'+full_url+'`', parse_mode='markdown')
				break
		
bot.polling()
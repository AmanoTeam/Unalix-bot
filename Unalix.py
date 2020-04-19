from json import loads
from telebot import TeleBot, types
from unalix import clear_url

bot = TeleBot('YOUR_TOKEN_HERE')

with open('Unalix/dialogs/en.json', 'r') as dialogs_file:
    dialogs = loads(dialogs_file.read())

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, dialogs['welcome'], parse_mode='markdown', disable_web_page_preview=True, disable_notification=True)

@bot.inline_handler(lambda query: re.match('https?://.+', query.query))
def query_handler(inline_query):
    
    url = clear_url(inline_query.query)
    
    result = types.InlineQueryResultArticle('1', url, types.InputTextMessageContent(url))
    
    bot.answer_inline_query(inline_query.id, [result])

@bot.message_handler(regexp='^https?://.+')
def url_handler(message):
    
    url = clear_url(message.text)
    
    bot.reply_to(message, url, disable_notification=True)

bot.polling(none_stop=True)

from settings import bot
from telebot.types import InlineQueryResultArticle, InputTextMessageContent
from dialogs import dialogs
import re
import unalix

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message, dialogs['welcome'], parse_mode='markdown', disable_web_page_preview=True
    )

@bot.inline_handler(lambda query: re.match('https?://.+', query.query))
def query_handler(inline_query):
    
    try:
        url = unalix.clear_url(inline_query.query)
    except Exception as e:
        result = InlineQueryResultArticle('1', 'An error has occurred', InputTextMessageContent(dialogs['error'].format(e), parse_mode='markdown'))
    else:
        result = InlineQueryResultArticle('1', url, InputTextMessageContent(url))
    
    bot.answer_inline_query(inline_query.id, [result])

@bot.message_handler(regexp='^https?://.+')
def url_handler(message):
    
    try:
        url = unalix.clear_url(message.text)
    except Exception as e:
        bot.reply_to(
            message, dialogs['error'].format(e), parse_mode='markdown'
        )
    else:
        bot.reply_to(
            message, '`{}`'.format(url), parse_mode='markdown'
        )
    
bot.polling(none_stop=True)

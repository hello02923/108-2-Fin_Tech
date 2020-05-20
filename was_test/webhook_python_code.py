#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import configparser
import telegram
from flask import Flask, request
from telegram.ext import Dispatcher, MessageHandler, Filters, CommandHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from fugle_realtime import intraday


# In[2]:


config = configparser.ConfigParser()
config.read('config.ini')


# In[3]:


config['TELEGRAM']['ACCESS_TOKEN']


# In[4]:


config['TELEGRAM']['WEBHOOK_URL']


# In[5]:


access_token = config['TELEGRAM']['ACCESS_TOKEN']
webhook_url = config['TELEGRAM']['WEBHOOK_URL']


# ## delete webhook url

# In[6]:


requests.post('https://api.telegram.org/bot'+access_token+'/deleteWebhook').text


# ## set webhook url

# In[7]:


import requests


# In[8]:


requests.post('https://api.telegram.org/bot'+access_token+'/setWebhook?url='+webhook_url+'/hook').text


# In[9]:


r = requests.get('http://127.0.0.1:8050/')
print(r.status_code)


# In[10]:


import pandas as pd
df= pd.read_excel("/Users/lai/symbol_info.xlsx")
symbol_ID=[]
for i in df["symbol_id"]:
    symbol_ID.append(i)


# In[ ]:


# Initial Flask app
app = Flask(__name__)

# Initial bot by Telegram access token
bot = telegram.Bot(token=config['TELEGRAM']['ACCESS_TOKEN'])
api_token = "3e8308228d40d8e6253efc485aae7777"


@app.route('/hook', methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        # Update dispatcher process that handler to process this message
        dispatcher.process_update(update)
        print(1)
    return 'ok'

# def help_handler(bot, update):
#     update.message.reply_text('''您好 {},請輸入以下代碼
#     /link : 參考網站
#     /best5 :最佳五檔
#     /priceReference :開盤參考價'''.format(update.message.from_user.name))
#     print(4)
    
    
def start_handler(bot, update):
    user_id = update.message.from_user.name
    update.message.reply_text('''您好 {},請輸入股票代碼'''.format(update.message.from_user.name))
    print(0)

def link(bot, update):
    keyboard = [[InlineKeyboardButton('fugle', url = 'https://www.fugle.tw', callback_data='1'),
                 InlineKeyboardButton('yahoo 股市', url = 'https://tw.stock.yahoo.com', callback_data='2'),]]


    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('參考資料:', reply_markup=reply_markup)
    print(6)


a = []
b = []
c = []
d = []
def best5(bot, update):

    s = intraday.quote(apiToken=api_token,symbolId=str(aa[0]),output="raw")['order'] 
    s1 = s['bestAsks']
    s2 = s['bestBids']
    
    for i in range(0,len(s1)):  
        a.append(s1[i]['price'])
        b.append(s1[i]['unit'])
    for i in range(0,len(s2)):  
        c.append(s2[i]['price'])
        d.append(s2[i]['unit'])

    aaa = "bestAsks"+"\n"+"price"+ str(a)+"\n"+"unit"+str(b)
    bbb = 'bestBids'+"\n"+"price"+str(c)+"\n"+"unit"+str(d)
    
    update.message.reply_text(aaa)
    update.message.reply_text(bbb)
    
    
    
    
    



def priceReference(bot, update):
    
    q_data = intraday.meta(apiToken=api_token,symbolId=str(aa[0]),output="raw")['priceReference']
    qq_data = intraday.meta(apiToken=api_token,symbolId=str(aa[0]),output="raw")['priceHighLimit']
    qqq_data = intraday.meta(apiToken=api_token,symbolId=str(aa[0]),output="raw")['priceLowLimit']
    qq = 'priceReference'+ str(q_data)
    qq1 = 'priceHighLimit'+ str(qq_data)
    qq2 = 'priceLowLimit'+ str(qqq_data)
#     print(qq)
    update.message.reply_text(qq)
    update.message.reply_text(qq1)
    update.message.reply_text(qq2)
    
    print(qq)


def open_close(bot, update):
    a_data=intraday.chart(apiToken=api_token,symbolId=str(aa[0]))
    
    aaa=str(a_data.tail(1)["open"])
    bb=aaa.split(sep='    ')[1]
    o=bb.split(sep="N")[0]
    
    aab=str(a_data.tail(1)["close"])
    bb1=aab.split(sep='    ')[1]
    o1=bb.split(sep="N")[0]
    
    oc="開盤價:"+ o 
    oc1="收盤價:"+ o1
    print(oc)
    print(oc1)

    update.message.reply_text(oc)
    update.message.reply_text(oc1)

    
## reply message
aa = []
def reply_handler(bot, update):
    text = update.message.text
    user_id = update.message.from_user.name
    if str(text) in symbol_ID:
        qq='''請輸入
        /best5 : 最佳五檔
        /priceReference :開盤參考價
        /open_close : 開盤、收盤價
        /link :相關網站'''
        update.message.reply_text(qq)
        print(33)
        aa.append(text)

    else:
        kk="請再輸入一遍"
        update.message.reply_text(kk)
        print(22)



# q_data = intraday.meta(apiToken=api_token,symbolId="1216",output="raw")['priceReference']
# qq = 'priceReference'+ str(q_data)
# print(qq)

        
        
    

    
    
# This class dispatches all kinds of updates to its registered handlers.
dispatcher = Dispatcher(bot, None)
##dispatcher.add_handler(CommandHandler('help', help_handler))
dispatcher.add_handler(CommandHandler("start", start_handler))
dispatcher.add_handler(CommandHandler("link", link))
dispatcher.add_handler(CommandHandler("priceReference", priceReference))
dispatcher.add_handler(CommandHandler("best5", best5))
dispatcher.add_handler(CommandHandler("open_close", open_close))

dispatcher.add_handler(MessageHandler(Filters.text, reply_handler))

if __name__ == '__main__':
    app.run()


# In[ ]:





# In[ ]:





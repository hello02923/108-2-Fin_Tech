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
from tensorflow.keras.models import load_model


# In[2]:


api_token = "3e8308228d40d8e6253efc485aae7777"
model = load_model('test.h5')
# TOKEN = '1194508394:AAGzL92ltDZkr4UWPvLZ9fxGMaxvEzUOFoM'


# In[ ]:


recommend_button = ReplyKeyboardMarkup([['推薦']],
                                     one_time_keyboard = True,
                                     selective = True)


def webhook_handler():
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        # Update dispatcher process that handler to process this message
        updater.dispatcher.process_update(update)
        print(1)
    return 'ok'


def start_handler(bot, update):
    user_id = update.message.from_user.name
    update.message.reply_text('''您好 {},'''.format(update.message.from_user.name))
    print(0)
    

def recommend_handler(bot, update):
    update.message.reply_text(recommend, reply_markup = recommend_button)
        



## reply message
def reply_handler(bot, update):
    text = update.message.text
    user_id = update.message.from_user.name
    y_pred = model.predict([[x_val[0]]])
    array = np.concatenate(y_pred, axis=None)
    df = pd.DataFrame(dataset.columns[-70:])
    merge = pd.DataFrame(pd.np.column_stack([df, array]))
    s = merge.sort_index()
    s = s.sort_values(1, ascending=False)[:5]
    update.message.reply_text(s)
    
    

updater = Updater(token='1194508394:AAHTqtFhwgis8sJoAQwctGu4xQ1D5Z6DWSI')
updater.dispatcher.add_handler(CommandHandler("start", start_handler))
updater.dispatcher.add_handler(CommandHandler("recommend", recommend_handler))
updater.dispatcher.add_handler(MessageHandler(Filters.text, reply_handler))


# if __name__ == '__main__':
#     app.run(port=5000)
updater.start_polling()
updater.idle()


# In[ ]:





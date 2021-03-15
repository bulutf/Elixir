# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 01:46:51 2021

@author: bulut
"""
from telegram.ext import Updater
from bs4 import BeautifulSoup
import requests


def start_command(update, context):
    
    message = "Hey, wanna make a potion ?"
    
    return update.message.reply_text(message)


def wrong_command(update, context):
    
    message = "Hey come on gimme a break ! Just use /start /news and /market for now..."
    
    return update.message.reply_text(message)

def get_news(update, context):
    
    link="https://www.coinkolik.com/kripto-para-haberleri/"  
    
    r=requests.get(link)
    soup=BeautifulSoup(r.content, "lxml")
    
    news=soup.find_all("article")
    
    for new in news[:]:
    
        link=new.find('a').get("href")
        text=new.find("p").text
        title=new.find("h2").text
    
        my_news="{}\n\n{}\n\nLink  :   {}\n\n".format(title,text,link)
    
        update.message.reply_text(my_news)

        
def get_coins(update, context):
    
    link="https://www.coingecko.com/tr?utm_source=www.coinkolik.com&utm_medium=coin_converter_widget&utm_content=bitcoin"

    r=requests.get(link)
    soup=BeautifulSoup(r.content, "lxml")
    
    coins=soup.find_all("tr")
    
    for coin in coins[0:20]:
    
        middle=coin.find_all('td', attrs={"class": "td-price price text-right"})
        
        for x in middle[:]:
            
            span=x.find("span").get("data-coin-symbol").upper()
            price=x.get("data-sort")
            
            market="{:<5}: {} $".format(span,price[0:6])
            
        
            update.message.reply_text(market)


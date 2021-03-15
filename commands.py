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
    
    message = "Hey come on gimme a break ! Just use /start for now..."
    
    return update.message.reply_text(message)

def get_news(update, context):
    
    link="https://www.haberler.com/son-dakika/"
    
    r=requests.get(link)
    soup=BeautifulSoup(r.content, "lxml")

    news=soup.find_all('div', attrs={'class': "hblnBox"})
    
    for new in news[:5]:
        
        time=new.find('div', attrs={'class': "hblnTime"}).text
        title=new.find("a", attrs={"class": "hblnTitle"}).get("title")   # başlığı çek
        link=new.find("a", attrs={"class": "hblnTitle"}).get("href")     # linki çek
        
    
        my_news="Time    : {}\n\nTitle   : {}\n\nLink    : {}\n\n".format(time,title,link)
        
        update.message.reply_text(my_news)


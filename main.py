from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import commands as c

TOKEN = "1669288994:AAGkYYdY5bwRC441oBLdSgJRx59M-m3hXaU"

print("Bot is working")

def main():
    
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    # start command
    dp.add_handler(CommandHandler("start", c.start_command))
    # news
    dp.add_handler(CommandHandler("news", c.get_news))
        
    #wrong command
    dp.add_handler(MessageHandler(Filters.text, c.wrong_command))
    

    
    
    updater.start_polling()
    updater.idle()
                 
if __name__ == "__main__":
    main()
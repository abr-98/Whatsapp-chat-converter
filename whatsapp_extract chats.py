

import sys
from scrape import *

chat_name=input("Enter the chat name  ")
print("Enter 1 if you want to extract full chat")
print("Enter 2 if you want to get just recent chats")

option=input("enter your choice     ")

chat_name_2='\"'+chat_name+'\"'
#chat_name = "" #sys.argv[-1] #'\xe0\xa4\xac\xe0\xa5\x80\xe0\xa4\x9c\xe0\xa5\x87\xe0\xa4\xaa\xe0\xa5\x80 \xe0\xa4\xae\xe0\xa5\x80\xe0\xa4\xa1\xe0\xa4\xbf\xe0\xa4\xaf\xe0\xa4\xbe \xe0\xa4\xb0\xe0\xa5\x80\xe0\xa4\xb5\xe0\xa4\xbe'


if option=='1':
    locate_chat(chat_name_2)
    all_chats = scroll_to_top()

    run_scraper(chat_name)

if option=='2':
    date=input("Enter date in m/dd/yyyy if single character month or mm/dd/yyyy     ")
    locate_chat(chat_name_2)
    all_chats = scroll_to_top()

    run_scraper(chat_name,date)

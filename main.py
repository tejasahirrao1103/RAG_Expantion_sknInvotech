import dataenjection
import random 

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
END_COLOR = '\033[0m'

colr =['\033[91m','\033[92m','\033[93m','\033[94m']


print(colr[0]+"""
███████╗██╗   ██╗██████╗ ███████╗██████╗      █████╗ ██╗
██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗    ██╔══██╗██║
███████╗██║   ██║██████╔╝█████╗  ██████╔╝    ███████║██║
╚════██║██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗    ██╔══██║██║
███████║╚██████╔╝██║     ███████╗██║  ██║    ██║  ██║██║
╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝
                                            
"""+ END_COLOR)

option = input(colr[3]+"""
      Select Option:
      for Webpage type -->> wp
      for pdf type --> pdf
      for text type --> txt
      for audio type --> aud
      for video type -->> vid
      for docx type -->> doc

      enter option:
      """+ END_COLOR)

match option.strip():
    case 'wp':
        dataenjection.webpage()
    case 'pdf':
        dataenjection.pdfloader()  
    case 'txt':
        dataenjection.textloader()
    case 'aud':
        dataenjection.audvid()
    case 'vid':
        dataenjection.audvid()
    case 'doc':
        dataenjection.doc()
    case _:
        print("enter valid input")  
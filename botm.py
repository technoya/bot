import requests
import time

# list of quotes
quotes = [
  'BOT UNDER MAINTENCE WAIT !!'
]

# loop through the quotes
for quote in quotes:
    url = 'https://api.telegram.org/bot1848805395:AAHaacRzz3vDJ8vrQqVZ4vMPTqY1OBOQ12Q/sendMessage?chat_id=CHAT_ID&text="{}"'.format(quote)
    requests.get(url)
    # sends new quotes every 20seconds
    time.sleep(20)

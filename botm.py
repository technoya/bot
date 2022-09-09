import requests
import time

# list of quotes
quotes = [
  'BOT UNDER MAINTENCE WAIT !!'
]

# loop through the quotes
for quote in quotes:
    url = 'https://api.telegram.org/bot5721627024:AAHtBmuJMMtKtM-JTo3VecF9jYvS1_S0_N8/sendMessage?chat_id=CHAT_ID&text="{}"'.format(quote)
    requests.get(url)
    # sends new quotes every 20seconds
    time.sleep(2000000)

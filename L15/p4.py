import requests
import time
try:
	wa = "https://api.coindesk.com/v1/bpi/currentprice.json"
	res = requests.get(wa)
	data = res.json()
	msg = data["bpi"]["USD"]["rate"]
	print("usd : ",msg)
except Exception as e:
	print("issue: ",e)
 
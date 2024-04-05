import requests

try:
	wa = "https://ipinfo.io/"
	res = requests.get(wa)
	print(res)
	data = res.json()
	print(data)
	city_name = data["city"]
	state_name = data["region"]
	print("city = ",city_name)
	print("state_name = ",state_name)
	loc = data["loc"]
	info = loc.split(",")
	lat = info[0] 
	lon = info[1]
	print("lat = ",lat)
	print("lon = ",lon)
except Exception as e:
	print("issue: ",e)
 
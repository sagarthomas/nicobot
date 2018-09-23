import requests

payload = "Longbeach Filter King-Size Hard Pack 30's/40's"

r = requests.post("https://mysterious-inlet-47286.herokuapp.com/send", data=payload)
print(r.text)
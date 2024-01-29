import requests
import time
import uuid
import random

url = "https://api.discord.gx.games/v1/direct-fulfillment"
headers = {
            "Content-Type": "application/json",
            "Sec-Ch-Ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
        }
data = {
            "partnerUserId": str(uuid.uuid4())
        }

for x in range(1000):     
    response = requests.post(url, json=data,headers=headers, timeout=5)
    response_json = response.json()
    token = response_json.get('token')
    link = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}"
    print(link)

    time.sleep(0.1)
    with open("nitro-code.txt", "a") as f:
        f.write(f"{link}\n")


x = input()
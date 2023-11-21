import requests as requestslib, os
requests = requestslib.Session()
os.system("title skibidi v1")


IOSTOKEN = "Basic MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE="

def Get_Cookie(exchange_ref):
    requests.get(f"https://www.epicgames.com/id/api/csrf")
    xsrf = requests.cookies.get("XSRF-TOKEN")
    res = requests.post(
        f"https://www.epicgames.com/id/api/exchange",
        headers={
            'x-xsrf-token': f"{xsrf}"
        },
        json={
          "exchangeCode": f"{exchange_ref}"
        }
    )
    sessionap_ref = res.cookies.get("EPIC_SESSION_AP")
    return sessionap_ref


def Log_In():
    Authcode = input("AuthCode -> ")
    r = requests.post("https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token", headers={"Authorization": IOSTOKEN, "Content-Type": "application/x-www-form-urlencoded"}, data="grant_type=authorization_code&code=" + Authcode)
    if r.status_code != 200:
        return os.system("echo Invalid Authcode! Exiting... && exit")
    return r.json()

def get_exchange(jsonn):
    r = requests.get("https://account-public-service-prod.ol.epicgames.com/account/api/oauth/exchange", headers={"Content-Type": "application/json", "Authorization": "Bearer " + jsonn["access_token"]})
    if r.status_code == 200:
        return r.json()["code"]
    else: return None


def Get_Redirect(cookie):
    r = requests.get("https://www.epicgames.com/id/api/redirect?redirectUrl=https%3A%2F%2Fapi.maestro.io%2Fauth%2Fv2%2Flogin%2Foauth&state=N4IgTgpgJglpDGAXA%2BgVzDEAuEALRiADgM5YD0ZAhoTAHQC2lExiYA9rTG1aormQDcATGQA2bAOYwAdmTaVeuEABpwEROmnY8BEuTLw29QupiIYAiLQBmbMImlmrh%2BmVxGIKkMQhgBMeE8cCBp4Lx9iYi5pABUYegg2XgBlCENpKGJsIQBWAE4hAAZi1SjECABJKG0cqAA2HKZrQso6gBYoACMADmLKHMLO%2BuaQAF8gA&responseType=code&clientId=xyza7891oL6OtsGfOEEprZv2WcfMWDGy&scope=basic_profile", headers={
        "Cookie": "EPIC_SESSION_AP="+ cookie
    })
    if r.status_code == 200:
        rr = requests.get(r.json()['redirectUrl'], allow_redirects=False)
        if rr.status_code == 307:
            texttoparse = rr.headers.get("location")
            exchangeToken = texttoparse.split("=")[1]
            return exchangeToken
        
def GetJWT(exchangetoken):
    headers = {
        'authority': 'api.maestro.io',
        'method': 'POST',
        'path': '/auth/v2/exchange',
        'scheme': 'https',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Length': '60',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://competitive.fortnite.com',
        'Originpath': '/home',
        'Referer': 'https://competitive.fortnite.com/',
        'Sec-Ch-Ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
      }
    r = requests.post("https://api.maestro.io/auth/v2/exchange", json={"token": exchangetoken}, headers=headers)
    return r.json()['jwt']
        
def main():
    os.system("cls")
    print(GetJWT(
        Get_Redirect(
           Get_Cookie(
            get_exchange(
                Log_In()
            )
        )
    ))
)

main()

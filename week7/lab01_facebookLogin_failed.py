import requests
import bs4

login_url = "https://www.facebook.com"
my_email  = "YOUR_EMAIL"
my_passws = "YOUR_PASSWD"

response = requests.get(login_url);

with open("week7/fb1.html", "w", encoding="utf-8") as fp: # <meta charset="utf-8">
    fp.write(response.text)

# action="/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjI3Njk3OTY1LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D" 
# jazoest="2850"
# lsd="AVoY36mAANM"
# email="dyuamdl@yahoo.com.tw"
# login_source="comet_headerless_login"
# next=""
# pass => encpass

soup = bs4.BeautifulSoup(response.text, 'lxml')
form = soup.select_one('form[data-testid="royal_login_form"]')
url = form.attrs["action"]
# print(url)


submit_data = {
    "jazoest": form.select_one('input[name="jazoest"]').attrs["value"],
    "lsd": form.select_one('input[name="lsd"]').attrs["value"],
    "email": my_email,
    "pass" : my_pass,
    "login_source": form.select_one('input[name="login_source"]').attrs["value"],
    "next": form.select_one('input[name="next"]').attrs["value"],
}
print(submit_data)

response = requests.post(login_url + url, submit_data);
# 結果: 失敗，可能是因為 pass 加密的問題

with open("week7/fb2.html", "w", encoding="utf-8") as fp: # <meta charset="utf-8">
    fp.write(response.text)

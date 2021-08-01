import requests
import bs4

login_url = "https://www.facebook.com"
my_email  = "YOUR_EMAIL"
my_pass   = "#PWD_BROWSER:5:1627700136:AbVQAOb2jQhwmwFbY9TYIe3D0scZvOwBZcotdJ2iz+fFB8Zol6MUNtp2nn4up6MjJHFyJVz71nlSDYwb0QBLfqf0n6kNvDQ5fgs57ZKnMHZGyfx9cA7MmSIhWHUFrtoE8Z1LloN+fYVMdFtAdrk="

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
    "encpass" : my_pass,
    "login_source": form.select_one('input[name="login_source"]').attrs["value"],
    "next": form.select_one('input[name="next"]').attrs["value"],
}
print(submit_data)


session = requests.session();
response = session.post(login_url + url, submit_data, allow_redirects=False);

# 使用 session 也是失敗，submit 最後表單出現的 pass 似乎被改為 encpass
# 而且 encpass 應該是前端 javascript 寫出來的，而且每次都會不同
# 因此這個範例還是會失敗

with open("week7/fb2.html", "w", encoding="utf-8") as fp: # <meta charset="utf-8">
    fp.write(response.text)

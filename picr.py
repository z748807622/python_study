from PIL import Image
from PIL import ImageGrab
import time
import requests, os
im = ImageGrab.grab()
im.save("./lalalalalajijijiji.jpeg",'jpeg')
#im.show()
#Image = Image.open('./9.png')
#text = pytesseract.image_to_string(im,lang='chi_sim')
print type(im)
from requests_toolbelt import MultipartEncoder

url = 'http://182.61.168.164:8080/upload'
headers = {
    'Cookie': '_ga=GA1.2.1129292549.1536032342; _gid=GA1.2.420614154.1536808513; access_token=5c524351-f27a-48c0-a902-eea42d8284cc; JSESSIONID=14EA319C98E4FA91C74B44A066D49431',
    'Host': 'afo.xiaojukeji.com',
    'Origin': 'localhost',
    'Referer': 'localhost',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.16 Safari/537.36'
    }
f = open("./lalalalalajijijiji.jpeg",'rb')
file = {'file':('./lalalalalajijijiji,jpeg',f,"image/jpeg")}
html = requests.post(url,files=file, headers=headers)
#time.sleep(5)
f.close()
os.remove("./lalalalalajijijiji.jpeg")

#print text
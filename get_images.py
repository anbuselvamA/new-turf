import urllib.request
import re
try:
    req = urllib.request.Request('https://schloss-freudenfels.ch/', headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    images = re.findall(r'https?://[^\s\"\'<>]+?\.(?:jpg|jpeg|png|webp)', html)
    for img in set(images):
        print(img)
except Exception as e:
    print(e)

import os
import re
import glob
from urllib.parse import unquote

html_files = glob.glob('*.html')

for h in html_files:
    content = open(h, encoding='utf-8').read()
    for m in re.finditer(r'(src|href)="([^"]+)"', content):
        path = m.group(2)
        if path.startswith(('http', '#', 'data:')):
            continue
            
        decoded_path = unquote(path)
        if not os.path.exists(decoded_path):
            print(f"[{h}] Missing locally: {path} (decoded: {decoded_path})")

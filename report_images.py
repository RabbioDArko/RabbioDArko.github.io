import os
import re
import glob
from urllib.parse import unquote

html_files = glob.glob('*.html')

for h in html_files:
    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()

    for m in re.finditer(r'(src|href)="([^"]+)"', content):
        path = m.group(2)
        if path.startswith(('http', 'mailto:', 'data:', '#')):
            continue
            
        decoded_path = unquote(path)
        print(f"[{h}] Found: {path}")
        if not os.path.exists(decoded_path):
            print(f"   !!! Does not exist: {decoded_path}")

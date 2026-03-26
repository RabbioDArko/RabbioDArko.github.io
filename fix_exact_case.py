import os
import re
import glob
from urllib.parse import unquote, quote

html_files = glob.glob('*.html')

def get_exact_case_path(path):
    # Returns the exact case of this path if it exists, else None
    parts = path.replace('\\', '/').split('/')
    current = '.'
    result = []
    
    for part in parts:
        if part == '' or part == '.':
            continue
        try:
            items = os.listdir(current)
            match = next((item for item in items if item.lower() == part.lower()), None)
            if not match:
                return None
            result.append(match)
            current = os.path.join(current, match)
        except OSError:
            return None
    return '/'.join(result)

for h in html_files:
    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content = content
    # Find all src="...", href="..."
    
    def replacer(match):
        attr = match.group(1)
        path = match.group(2)
        
        if path.startswith(('http', 'mailto:', 'data:', '#')):
            return match.group(0)
            
        decoded_path = unquote(path)
        exact_case = get_exact_case_path(decoded_path)
        
        if exact_case and exact_case != decoded_path:
            print(f"[{h}] Case mismatch: {path} -> {exact_case}")
            encoded_exact = quote(exact_case, safe='/')
            if encoded_exact != path:
                print(f"   -> Fixing to: {encoded_exact}")
                return f'{attr}="{encoded_exact}"'
                
        if exact_case:
            encoded_exact = quote(exact_case, safe='/')
            if encoded_exact != path:
                print(f"[{h}] Encoding space/special chars: {path} -> {encoded_exact}")
                return f'{attr}="{encoded_exact}"'
        
        return match.group(0)

    new_content = re.sub(r'(src|href)="([^"]+)"', replacer, content)
    
    if new_content != content:
        with open(h, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {h}")

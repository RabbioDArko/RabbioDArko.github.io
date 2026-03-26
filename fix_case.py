import os
import re
import glob

html_files = glob.glob('*.html')

# We need a function that given a path like "files/poolheroes/image.png", returns the true case of the path if it exists on windows
def get_true_case_path(path):
    if not os.path.exists(path):
        return None
    # normalize path separators
    path = os.path.normpath(path)
    parts = path.split(os.sep)
    
    true_parts = []
    current_path = '.'
    for part in parts:
        if part == '.':
            continue
        # get directory listing
        try:
            items = os.listdir(current_path)
            # find the true case item
            true_item = next((item for item in items if item.lower() == part.lower()), None)
            if true_item is None:
                return None
            true_parts.append(true_item)
            current_path = os.path.join(current_path, true_item)
        except OSError:
            return None
    
    return '/'.join(true_parts)

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all src="...", href="..."
    
    def replacer(match):
        attr = match.group(1)
        path = match.group(2)
        # We only care about local paths, e.g. starting with "Files/" or "files/" or other local folders
        # ignore http, https, #, data:
        if path.startswith(('http', 'https', '#', 'data:')):
            return match.group(0)
        
        # sometimes path contains URL encoding like %20, let's try to unquote it
        from urllib.parse import unquote
        decoded_path = unquote(path)
        
        true_case = get_true_case_path(decoded_path)
        if true_case and true_case != path:
            print(f"[{html_file}] Fixing: {path} -> {true_case}")
            # we need to re-encode spaces if they were encoded, or just use true_case as is (browsers handle spaces in src fine, or we can use quote)
            # looking at how it was, let's keep the encoding if it had any? No, let's just use true_case and quote it properly, wait it's inside quotes, 
            # maybe we just replace it exactly.
            from urllib.parse import quote
            # quote the parts
            return f'{attr}="{true_case}"'
        
        return match.group(0)

    new_content = re.sub(r'(src|href)="([^"]+)"', replacer, content)
    
    if new_content != content:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {html_file}")

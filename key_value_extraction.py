import re

def extract_key_value_pairs(text):
    key_value_pairs = {}
    pattern = r"(?m)^\s*([^:\n]+?)\s*:\s*(.+?)\s*$"  
    matches = re.findall(pattern, text)
    for match in matches:
        key = match[0].strip().lower() 
        value = match[1].strip()  
        key_value_pairs[key] = value  
    return key_value_pairs


#!/usr/bin/env python3
"""Merge generated questions into index.html — simple approach."""
import json, os

BASE = '/Users/ke/WorkBuddy/2026-06-11-15-53-41'

# Target new questions to add
TARGETS = {'math': 350, 'logic': 350, 'writing': 80, 'english': 560}

# Load and trim generated questions
new_qs = {}
for subj, count in TARGETS.items():
    with open(os.path.join(BASE, f'gen_{subj}.json'), 'r', encoding='utf-8') as f:
        new_qs[subj] = json.load(f)[:count]
    print(f"  {subj}: {len(new_qs[subj])} new questions loaded")

# Read HTML
html_path = os.path.join(BASE, 'index.html')
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find QUESTIONS block boundaries
q_start = html.find('const QUESTIONS = {')
if q_start == -1:
    raise ValueError("QUESTIONS not found")

# Find matching closing };
brace_start = html.find('{', q_start)
depth = 0
q_end = -1
for i in range(brace_start, len(html)):
    if html[i] == '{': depth += 1
    elif html[i] == '}':
        depth -= 1
        if depth == 0:
            q_end = i + 1
            # Include trailing semicolon if present
            if q_end < len(html) and html[q_end] == ';':
                q_end += 1
            break

print(f"QUESTIONS block: {q_start} to {q_end} ({q_end - q_start} chars)")

# Find each subject's array boundaries within the QUESTIONS block
block = html[q_start:q_end]

def find_array_end(text, start_bracket):
    """Find matching ] for [ at start_bracket."""
    depth = 0
    for i in range(start_bracket, len(text)):
        if text[i] == '[': depth += 1
        elif text[i] == ']':
            depth -= 1
            if depth == 0:
                return i
    return -1

def esc(s):
    """Escape a string for JS single-quoted string literal."""
    return s.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')

# Build new question JS text
def qs_to_js(questions):
    """Convert list of question dicts to JS array text."""
    items = []
    for q in questions:
        parts = []
        parts.append(f"id:'{q['id']}'")
        parts.append(f"type:'{q['type']}'")
        parts.append(f"diff:'{q['diff']}'")
        if q.get('src'):
            parts.append(f"src:'{q['src']}'")
        parts.append(f"q:'{esc(q['q'])}'")
        opts_str = ','.join(f"'{esc(o)}'" for o in q['opts'])
        parts.append(f"opts:[{opts_str}]")
        parts.append(f"ans:'{q['ans']}'")
        parts.append(f"exp:'{esc(q['exp'])}'")
        if 'sampleAnswer' in q:
            parts.append(f"sampleAnswer:'{esc(q['sampleAnswer'])}'")
        items.append('{' + ','.join(parts) + '}')
    return ',\n  '.join(items)

# Process each subject
result_block = block
for subj in ['math', 'logic', 'writing', 'english']:
    # Find subject array in the current text
    # Look for pattern: subject:[ or subject: [
    import re
    match = re.search(subj + r'\s*:\s*\[', result_block)
    if not match:
        print(f"  WARNING: Could not find {subj} array, skipping")
        continue
    
    arr_start = result_block.find('[', match.start())
    arr_end_char = find_array_end(result_block, arr_start)
    if arr_end_char == -1:
        print(f"  WARNING: Could not find end of {subj} array, skipping")
        continue
    
    old_array_text = result_block[arr_start:arr_end_char + 1]
    existing_count = old_array_text.count("{id:")
    
    # Build new items text
    new_items = qs_to_js(new_qs[subj])
    
    # Replace the array: keep old content, append new items before closing ]
    new_array = old_array_text.rstrip()
    if new_array.endswith(']'):
        inner = new_array[:-1].rstrip()
        if inner.endswith(','):
            new_array = inner + '\n  ' + new_items + '\n]'
        else:
            new_array = inner + ',\n  ' + new_items + '\n]'
    
    result_block = result_block[:arr_start] + new_array + result_block[arr_end_char + 1:]
    print(f"  {subj}: {existing_count} existing + {len(new_qs[subj])} new = {existing_count + len(new_qs[subj])}")

# Replace the old QUESTIONS block with the new one
html_new = html[:q_start] + result_block + html[q_end:]

# Write back
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_new)

# Verify
total = result_block.count("{id:")
print(f"\nDone! Total questions: {total}")
print(f"File size: {os.path.getsize(html_path)} bytes")

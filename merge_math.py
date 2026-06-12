#!/usr/bin/env python3
"""Merge math questions into index.html — quote-aware bracket matching."""
import json, re, os

BASE = '/Users/ke/WorkBuddy/2026-06-11-15-53-41'

# Load math questions
with open(os.path.join(BASE, 'gen_math.json'), 'r', encoding='utf-8') as f:
    new_math = json.load(f)[:350]

def esc(s):
    return s.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')

# Build JS text for new math questions
items = []
for q in new_math:
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
    items.append('{' + ','.join(parts) + '}')

new_math_text = ',\n  '.join(items)
print(f"Generated {len(items)} math question JS objects")

# Read HTML
html_path = os.path.join(BASE, 'index.html')
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find math array using quote-aware bracket matching
match = re.search(r'math\s*:\s*\[', html)
if not match:
    raise ValueError("math array not found")

abs_bracket_start = html.find('[', match.start())
print(f"Math array opening [ at position {abs_bracket_start}")

# Quote-aware bracket matching to find closing ]
in_single = False
in_double = False
depth = 0
abs_bracket_end = -1
i = abs_bracket_start
while i < len(html):
    ch = html[i]
    # Handle escape sequences inside strings
    if in_single and ch == '\\' and i + 1 < len(html):
        i += 2
        continue
    if in_double and ch == '\\' and i + 1 < len(html):
        i += 2
        continue
    # Toggle string state
    if ch == "'" and not in_double:
        in_single = not in_single
    elif ch == '"' and not in_single:
        in_double = not in_double
    # Count brackets only outside strings
    elif not in_single and not in_double:
        if ch == '[':
            depth += 1
        elif ch == ']':
            depth -= 1
            if depth == 0:
                abs_bracket_end = i
                break
    i += 1

if abs_bracket_end == -1:
    raise ValueError("Could not find end of math array")

print(f"Math array closing ] at position {abs_bracket_end}")
print(f"Math array spans {abs_bracket_end - abs_bracket_start} chars")

# Verify: the character after the closing ] should be a comma (followed by next subject)
# or end of QUESTIONS
after = html[abs_bracket_end:abs_bracket_end+20]
print(f"After closing ]: {repr(after[:20])}")

# Now insert new questions before the closing ]
# Find the last } before the closing ], skipping whitespace and commas
content_before = html[abs_bracket_start+1:abs_bracket_end].rstrip()
# Remove trailing commas and whitespace
while content_before and content_before[-1] in ',\n\r \t':
    content_before = content_before[:-1].rstrip()

# Rebuild: existing content + comma + new items + ]
new_array_content = content_before + ',\n  ' + new_math_text + '\n'

# Replace
html_new = html[:abs_bracket_start+1] + new_array_content + html[abs_bracket_end:]

# Write
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_new)

# Verify counts
math_start = html_new.find('math:')
logic_start = html_new.find('logic:')
math_section = html_new[math_start:logic_start]
math_count = math_section.count("{id:")

total = html_new.count("{id:")
print(f"\nMath questions: {math_count}")
print(f"Total questions: {total}")
print(f"File size: {len(html_new)} bytes")

import sys

with open(r"c:\Users\Dell\Documents\AntiG Proj\Portfolio\Files\code.html", "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    # Growtopia
    (
        '<div class="md:col-span-3 rounded-lg ink-shadow hover:scale-[1.005] transition-all group overflow-hidden flex flex-col md:flex-row h-auto bg-transparent relative">',
        '<a href="growtopia.html" class="md:col-span-3 rounded-lg ink-shadow hover:scale-[1.005] transition-all group overflow-hidden flex flex-col md:flex-row h-auto bg-transparent relative">'
    ),
    (
        '</div>\n</div>\n<!-- Clash of Beasts -->',
        '</div>\n</a>\n<!-- Clash of Beasts -->'
    ),
    # COB
    (
        '<!-- Clash of Beasts -->\n<div class="bg-surface-container-lowest rounded-lg ink-shadow hover:scale-[1.01] transition-all flex flex-col group overflow-hidden">',
        '<!-- Clash of Beasts -->\n<a href="COB.html" class="bg-surface-container-lowest rounded-lg ink-shadow hover:scale-[1.01] transition-all flex flex-col group overflow-hidden">'
    ),
    (
        '</div>\n</div>\n<!-- MyWhoosh -->',
        '</div>\n</a>\n<!-- MyWhoosh -->'
    ),
    # MyWhoosh
    (
        '<!-- MyWhoosh -->\n<div class="bg-surface-container-lowest rounded-lg ink-shadow hover:scale-[1.01] transition-all flex flex-col group overflow-hidden">',
        '<!-- MyWhoosh -->\n<a href="MyWhoosh.html" class="bg-surface-container-lowest rounded-lg ink-shadow hover:scale-[1.01] transition-all flex flex-col group overflow-hidden">'
    ),
    (
        '</div>\n</div>\n<!-- Hideout -->',
        '</div>\n</a>\n<!-- Hideout -->'
    ),
    # Hideout
    (
        '<!-- Hideout -->\n<div class="bg-surface-container-lowest rounded-lg ink-shadow hover:scale-[1.01] transition-all flex flex-col group overflow-hidden">',
        '<!-- Hideout -->\n<a href="Hideout.html" class="bg-surface-container-lowest rounded-lg ink-shadow hover:scale-[1.01] transition-all flex flex-col group overflow-hidden">'
    ),
    (
        '</div>\n</div>\n<!-- Pool Heroes -->',
        '</div>\n</a>\n<!-- Pool Heroes -->'
    ),
    # PoolHeroes
    (
        '<!-- Pool Heroes -->\n<div class="bg-surface-container-lowest rounded-lg ink-shadow hover:scale-[1.01] transition-all flex flex-col group overflow-hidden">',
        '<!-- Pool Heroes -->\n<a href="poolheroes.html" class="bg-surface-container-lowest rounded-lg ink-shadow hover:scale-[1.01] transition-all flex flex-col group overflow-hidden">'
    ),
    (
        '</div>\n</div>\n<!-- Bug Battle -->',
        '</div>\n</a>\n<!-- Bug Battle -->'
    ),
    # BugBattle
    (
        '<!-- Bug Battle -->\n<div class="bg-surface-container-lowest rounded-lg ink-shadow hover:scale-[1.01] transition-all flex flex-col group overflow-hidden">',
        '<!-- Bug Battle -->\n<a href="Bugbattle.html" class="bg-surface-container-lowest rounded-lg ink-shadow hover:scale-[1.01] transition-all flex flex-col group overflow-hidden">'
    ),
    (
        '</div>\n</div>\n</div>\n</section>',
        '</div>\n</a>\n</div>\n</section>'
    )
]

for old, new in replacements:
    old_crlf = old.replace('\\n', '\\r\\n')
    if old in content:
        content = content.replace(old, new)
    elif old_crlf in content:
        content = content.replace(old_crlf, new.replace('\\n', '\\r\\n'))
    else:
        print(f"Error: Could not find:\\n{old}\\n")

with open(r"c:\Users\Dell\Documents\AntiG Proj\Portfolio\index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Replacement Complete")

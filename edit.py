import os, sys
import subprocess

replace=[("table", "Table"),
         ("figure", "Figure"),
         ("equation", "Equation"),
         ("graph", "Graph"),
         ("apendix", "Apendix"),
         ("chapter", "Chapter"),
         ("section", "Section"),
         ("subsection", "Subsection"),
         ("subsubsection", "Subsubsection"),
         ("subsubsection", "Subsubsection"),
         ("listing", "Listing"),
        ]


for root, dirs, files in os.walk("."):
    for filename in files:
        if filename[-3:] == 'tex':
            for item in replace:

                what_word, with_word = item

                bash_command = f'vim -c %s/{what_word}/{with_word}/gc {filename}'
                subprocess.run(bash_command.split())
                
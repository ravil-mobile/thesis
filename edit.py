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

#replace=[("definition", "Definition"),]

def replace_in_file(file_path, replace):
    for item in replace:

        what_word, with_word = item
        bash_command = f'vim -c "%s/{what_word}/{with_word}/gc" {file_path}'
        print(bash_command)
        os.system(f'{bash_command}')
            


#for root, dirs, files in os.walk("."):
#    for filename in files:
#        if filename[-3:] == 'tex':
#            replace_in_file(f'{root}/{filename}', replace)

replace_in_file(file_path="./chapters/part-2/part-2-hybrid-method-description.tex",
                replace=replace)
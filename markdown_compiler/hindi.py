# Author : Colton Smith
# Email  : colton.smith.ai@gmail.com
# Github : https://github.com/colton-smith-ai
# Date   : January 2022

####################################
# STEP 1 --> Read Dictionary Words #
####################################

# Hashmap holding first letter of hindi word as key,
# and value a list of tuples representing
# (hindi word, english definition)
# i.e. {'B':[('bhai','bro'), ('badiya','great')],
#       'N':[('namaste','hello')]}
organizer = {}

# Open txt file with definitions
file = open(r'hindi.txt','r')

# Iterate through each line
for line in file:

    # Avoid comments
    if line[0] != "#":

        # Parse line
        hindi, english = line.split('-')

        # Extract key
        first_letter = hindi[0].capitalize()

        # Update hashmap
        if first_letter in organizer:

            # Append to tuple list
            organizer[first_letter].append((hindi.strip(), english[:-1].strip()))

        # Create new key
        else:
            # Create new list for tupples
            organizer[first_letter] = []

            # Append to tuple list
            organizer[first_letter].append((hindi.strip(), english[:-1].strip()))

# Close file buffer
file.close()

#######################################
# STEP 2 --> Write Organized Markdown #
#######################################

# String alias
nl = '\n'
nln = '\n\n'
hi = 'hindi'
eng = 'english'

# Markdown header
md_head = ('# Hindi Dictionary' +
nl + 'Learn Hindi :india: by compiling organized Markdown dictionary ' +
'from text file.' + nln +
'## Table of Contents' + nln +
'- [Contributors Needed](#contribute)' + nl +
'- [Hindi Words](#hindi--word)' + nl +
'- [Hindi Phrases](#hindi--phrase)' + nl +
'- [English Words](#english--word)' + nln +
'### Contributors Needed' + nl +
'Hindi contributors needed to edit the following words:' + nln +
'### Hindi Words' + nln +
'#### Hindi Index' + nln)

# Create Markdown file
md = open("Hindi.md", "w")

# Write header to markdown
md.write(md_head)

# Placeholder for hindi words
hindi_words = ''

# Add Hindi index to markdown
for first_char in sorted(organizer.keys()):

    # Add link to first letters
    md.write('[' + first_char + '](#' + hi + '--' + first_char.lower() + ') ~ ')

    # Add char link
    hindi_words = hindi_words + nl + '##### ' + first_char + nl

    # Retrieve list of tupples
    tups = organizer[first_char]

    # Alphabetize tupples
    tups.sort(key = lambda tup : tup[0])

    # Iterate through tupples
    for hindi, english in tups:

        # Concat all words per firs letter index
        hindi_words = (hindi_words +
        hindi.capitalize() + ' - ' + english.capitalize() + nl)

# Add Hindi dictionary
md.write(nln + '#### Hindi Dictionary' + nl + hindi_words)

# Close markdown buffer
md.close()

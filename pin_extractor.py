# ============================================
# Python Basics - PIN Extractor using Loops
# FreeCodeCamp Python Course
# Author: Om Patel
# ============================================

def pin_extractor(poems):
    """
    Extracts secret PIN codes from poems.
    Each digit = length of the word at position matching line index.
    """
    secret_codes = []

    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')

        # Loop through each line with its index
        for line_index, line in enumerate(lines):
            words = line.split()

            # Get word at position matching line index
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'

        secret_codes.append(secret_code)

    return secret_codes


# Test poems
poem1 = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

# Extract and print PIN codes
print(pin_extractor([poem1, poem2, poem3]))

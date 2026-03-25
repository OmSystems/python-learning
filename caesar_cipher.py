# ============================================
# Python Basics - Build a Caesar Cipher
# FreeCodeCamp Python Course
# Author: Om Patel
# ============================================

def caesar(text, shift, encrypt=True):
    """
    Core Caesar Cipher function.
    Encrypts or decrypts text by shifting alphabets.
    """

    # Validate shift is an integer
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    # Validate shift is within valid range
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    # Define alphabet and apply shift direction
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = -shift

    # Create shifted alphabet and translation table
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    # Translate and return result
    encrypted_text = text.translate(translation_table)
    return encrypted_text


def encrypt(text, shift):
    """Encrypt text using Caesar Cipher."""
    return caesar(text, shift)


def decrypt(text, shift):
    """Decrypt text using Caesar Cipher."""
    return caesar(text, shift, encrypt=False)


# Test the cipher
encrypted_text = encrypt('freeCodeCamp', 3)
print('Encrypted:', encrypted_text)

decrypted_text = decrypt(encrypted_text, 3)
print('Decrypted:', decrypted_text)

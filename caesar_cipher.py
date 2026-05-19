"""
Caesar Cipher
-------------
Encrypts and decrypts text using the Caesar cipher technique —
a simple substitution cipher that shifts each letter by a fixed amount.
"""


def caesar(text, shift, encrypt=True):
    """
    Core cipher function.

    Args:
        text     (str)  : The text to encrypt or decrypt
        shift    (int)  : Number of positions to shift (1–25)
        encrypt  (bool) : True to encrypt, False to decrypt

    Returns:
        str: The transformed text, or an error message if input is invalid
    """
    if not isinstance(shift, int):
        return "Error: shift must be an integer."

    if not 1 <= shift <= 25:
        return "Error: shift must be between 1 and 25."

    if not encrypt:
        shift = -shift

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted = alphabet[shift:] + alphabet[:shift]

    table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted + shifted.upper()
    )
    return text.translate(table)


def encrypt(text, shift):
    """Encrypt text using Caesar cipher."""
    return caesar(text, shift, encrypt=True)


def decrypt(text, shift):
    """Decrypt text using Caesar cipher."""
    return caesar(text, shift, encrypt=False)


# --- Demo ---
if __name__ == "__main__":
    original  = "Courage is found in unlikely places."
    shift_val = 13

    encrypted = encrypt(original, shift_val)
    decrypted = decrypt(encrypted, shift_val)

    print("=" * 42)
    print("         CAESAR CIPHER DEMO")
    print("=" * 42)
    print(f"  Original  : {original}")
    print(f"  Shift     : {shift_val}")
    print(f"  Encrypted : {encrypted}")
    print(f"  Decrypted : {decrypted}")
    print("=" * 42)
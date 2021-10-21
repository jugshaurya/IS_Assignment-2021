## GOAL : Write a program that can encrypt and decrypyt using the Additive Cipher (Caesar Cypher)

# =======================================
## By Shaurya Singhal - MCA-2ndYr-3rdSem
## Date: 16-10-2021
# =======================================

## IDEA:
""" 
Encryption using (X + shift) mod 26
Decryption using (Y - shift) mod 26
"""

# class to use Additive Encryption and Decryption
class AdditiveEncDec:
    def __init__(self, shift = 6):
        # Crux: Additive Cipher Encyption is based on mapping characters to `(ax+b) % m`
        # key is [A,B,M]
        self.shift = shift
        self.M = 26

    def encrypt(self, text):
        """
        Ans = (X + shift) mod 26, where X is the character in text.
        """
        maskedText = text.upper().replace(" ", "")
        # convert text into all letter and without spaces.
        return "".join(
            [
                chr(((ord(letter) - ord("A")) + self.shift) % self.M + ord("A"))
                for letter in maskedText
            ]
        )

    def decrypt(self, cipher):
        """
        And = (Y - shift) mod 26, where Y is the character in text
        """
        return "".join(
            [
                chr(((ord(letter) - ord("A")) - self.shift + self.M) % self.M + ord("A"))
                for letter in cipher 
            ]
        )

def main():

    print("Enter the text to be decoded: ")
    text = input()

    additive = AdditiveEncDec()

    # Encryption
    encryptedText = additive.encrypt(text)
    print("Encrypted Text: ", encryptedText)

    # Decryption
    decryptedText = additive.decrypt(encryptedText)
    print("Decrypted Text: ", decryptedText)


if __name__ == "__main__":
    main()

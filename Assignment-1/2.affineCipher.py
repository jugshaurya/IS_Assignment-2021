## GOAL : Write a program that can encrypt and decrypyt using the Affine Cipher 

# =======================================
## By Shaurya Singhal - MCA-2ndYr-3rdSem
## Date: 16-10-2021
# =======================================

# class to use Affine Encryption and Decryption
class AffineEncDec:
    def __init__(self, A=3, B=7):
        # Crux: Affine Cipher Encyption is based on mapping characters to `(ax+b) % m`
        # key is [A,B,M]
        self.A = A
        self.B = B
        self.M = 26  # because in total there are 26 characters(all characters will be considered in Uppercase)
        # Note: a & m are coprime. Hence inv(a) exist -> will be required in decryptint the text later on.

    # Helper Functions
    # Extended Euclidean Algorithm for finding modular inverse
    def egcd(self, a, b):
        x, y, u, v = 0, 1, 1, 0
        while a != 0:
            q, r = b // a, b % a
            m, n = x - u * q, y - v * q
            b, a, x, y, u, v = a, r, u, v, m, n
        gcd = b
        return gcd, x, y

    # function to find modulo inverse i.e `a mod m ~= 1 mod m`
    def modinv(self, a, m):
        gcd, x, y = self.egcd(a, m)
        if gcd != 1:
            return None  # modular inverse does not exist
        else:
            return x % m

    def encrypt(self, text):
        """
        Ans = (A*x + B) % M, where x is the character in text
        """
        maskedText = text.upper().replace(" ", "")
        # convert text into all letter and without spaces.
        return "".join(
            [
                chr(((self.A * (ord(letter) - ord("A")) + self.B) % self.M) + ord("A"))
                for letter in maskedText
            ]
        )

    def decrypt(self, cipher):
        """
        And = (A^-1 * (x - B)) % M, where x is the character in text
        """
        return "".join(
            [
                chr(
                    ((self.modinv(self.A, self.M) * (ord(letter) - ord("A") - self.B)) % self.M)
                    + ord("A")
                )
                for letter in cipher
            ]
        )


def main():

    print("Enter the text to be decoded: ")
    text = input()

    affine = AffineEncDec()

    # Encryption
    encryptedText = affine.encrypt(text)
    print("Encrypted Text: ", encryptedText)

    # Decrpyption
    decryptedText = affine.decrypt(encryptedText)
    print("Decrypted Text: ", decryptedText)


if __name__ == "__main__":
    main()

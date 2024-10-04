x=input("\nDo you want to use a ceaser cypher encryptor program or a decrypter program to see all permutations of possible encryptions:\n"
        " type 'encrypt' (assignment requirement) for encryptor or 'decrypt' for decryptor")

if x.lower()=="encrypt":
    plainText = input("\nWhat is your plaintext? ")
    shift = int(input("\nWhat is your desired shift? "))
    def Encrypt(plainText, shift):
        encrypted = ""
        for PT in plainText:
            if PT.isalpha():
                Alphabet = ord(PT) + shift % 26
                if PT.islower():
                    if Alphabet > ord('z'):
                        Alphabet -= 26
                    elif Alphabet < ord('a'):
                        Alphabet += 26
                elif PT.isupper():
                    if Alphabet > ord('Z'):
                        Alphabet -= 26
                    elif Alphabet < ord('A'):
                        Alphabet += 26
                finalLetter = chr(Alphabet)
                encrypted += finalLetter
            else:
                encrypted += PT

        print ("Encrypted message is:",encrypted,",shift for decoding is,", shift)

        return encrypted

    Encrypt(plainText, shift)

    y=input("\nyou want to see how easy Ceaser Cypher is broken? type 'yes' to continue").lower()

    if y=="yes":
        Mencrypted = input("\nwrite the encrypted message just recived")

        def decryption(Mencrypted, Reshift):
            decrypted_text = ""
            for PT in Mencrypted:
                if PT.isalpha():
                    if PT.islower():
                        decrypted_PT = chr(((ord(PT) - ord('a') - Reshift) % 26) + ord('a'))
                    elif PT.isupper():
                        decrypted_PT = chr(((ord(PT) - ord('A') - Reshift) % 26) + ord('A'))
                else:
                    decrypted_PT = PT
                decrypted_text += decrypted_PT
            return decrypted_text

        def force_break(Mencrypted):
            for Reshift in range(26):
                decrypted_message = decryption(Mencrypted, Reshift)
                print(f"Shift {Reshift}: {decrypted_message}")

        force_break(Mencrypted)

        print("\n As seen above, all permutations shown are the 26 only available shifts in the ceaser cypher encryption program.\n"
              "in essence, this means that you have a", (1/26)*100,"%", "chance of guessing the correct shift\n"
                                                                        "moreover to break the encryption one only has to shift the encryption by 1, 26 times, and one of these is bound to be it\n"
                                                                        "in this case, the shift is", shift, "or", 26+shift, "meaning the message is",plainText)
        print("\n Let's try One Time Pad next time")
    else:
        print("\nyou lack curiosity")

if x=="decrypt":
    Mencrypted = (input("\nEnter encrypted message"))
    Hreshift = int(input("\nWhat do you think the shift is?"))

    def decryption(Mencrypted, shift):
        decrypted_text = ""
        for PT in Mencrypted:
            if PT.isalpha():
                if PT.islower():
                    decrypted_PT = chr(((ord(PT) - ord('a') - shift) % 26) + ord('a'))
                elif PT.isupper():
                    decrypted_PT = chr(((ord(PT) - ord('A') - shift) % 26) + ord('A'))
            else:
                decrypted_PT = PT
            decrypted_text += decrypted_PT
        return decrypted_text

    def force_break(Mencrypted):
        for shift in range(26):
            decrypted_message = decryption(Mencrypted, shift)
            print(f"Shift {shift}: {decrypted_message}")

    force_break(Mencrypted)



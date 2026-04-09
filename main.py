# ============================================
# ENIGMA MACHINE PROJECT (CAESAR CIPHER)
# ============================================


# Function to clean input
def format_text(text):
    return text.strip()


# Function to encrypt message
def encrypt(message_list, shift):
    result = []

    # Loop through each character
    for char in message_list:

        # Check if character is a letter
        if char.isalpha():

            # Shift character forward
            new_char = chr(ord(char) + shift)

            # Wrap around alphabet
            if char.islower() and new_char > "z":
                new_char = chr(ord(new_char) - 26)
            elif char.isupper() and new_char > "Z":
                new_char = chr(ord(new_char) - 26)

            result.append(new_char)

        else:
            result.append(char)

    return "".join(result)


# Function to decrypt message
def decrypt(message_list, shift):
    result = []

    for char in message_list:

        if char.isalpha():

            new_char = chr(ord(char) - shift)

            if char.islower() and new_char < "a":
                new_char = chr(ord(new_char) + 26)
            elif char.isupper() and new_char < "A":
                new_char = chr(ord(new_char) + 26)

            result.append(new_char)

        else:
            result.append(char)

    return "".join(result)


# Main program
def main():

    print("===========================")
    print(" ENIGMA MACHINE SIMULATOR ")
    print("===========================")


# Run the program
if __name__ == "__main__":
    main()

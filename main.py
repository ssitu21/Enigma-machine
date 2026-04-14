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

    while True:

        choice = input("\nEncrypt or Decrypt? (e/d): ").lower().strip()

        if choice not in ["e", "d"]:
            print("Invalid choice. Try again.")
            continue

        message = input("Enter your message: ")
        message = format_text(message)

        message_list = list(message)

        shift = input("Enter shift number (e.g. 3): ").strip()

        # Check if shift is valid
        if not shift.isdigit():
            print("Shift must be a number.")
            continue

        shift = int(shift)

        # Check shift range
        if shift < 1 or shift > 25:
            print("Shift must be between 1 and 25.")
            continue

        # Call correct function
        if choice == "e":
            result = encrypt(message_list, shift)
            print("\nEncrypted message:")
            print(result)

        else:
            result = decrypt(message_list, shift)
            print("\nDecrypted message:")
            print(result)


# Run the program
if __name__ == "__main__":
    main()

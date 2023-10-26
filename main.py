
def decode(encode):
    decodedInput = ''
    for num in encode:
        if int(num) >= 7:
            newDecode = int(num) + 3 - 10
            decodedInput += str(newDecode)
        else:
            newDecode = int(num) + 3
            decodedInput += str(newDecode)
    return decodedInput


if __name__ == '__main__':


    while True:
        print('Main Menu')
        print('-'*9)
        print('1. Encode\n2. Decode\n3. Quit\n')

        userInput = int(input("Please enter an option:"))
        if userInput == 1:
            encodeInput = input("Please enter your password to encode: ")
            print('Your password has been encoded and stored!')
        if userInput == 2:
            print(f"The encoded password is {decode(encodeInput)}, and the original password is {encodeInput}.\n")
        if userInput == 3:
            break
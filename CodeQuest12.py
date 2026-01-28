class Testcase:
    def __init__(self, encoder, decoder, encoded_message, message_toEncode):
        self.encoder = encoder
        self.decoder = decoder
        self.encoded_message = encoded_message
        self.message_toEncode = message_toEncode

amount_of_testcases = int(input("").strip())
testcases = []

for t in range(amount_of_testcases):
    encoder_dict = {}
    decoder_dict = {}
    for i in range(26):
        key = input("").strip()
        encoder_dict[key[0]] = key[2:]
        decoder_dict[key[2:]] = key[0]
    unencoded_message = input("").strip()
    encoded = input("").strip()
    case = Testcase(encoder_dict, decoder_dict, encoded, unencoded_message)
    testcases.append(case)

for x in testcases:
    unencoded_message = x.message_toEncode
    encoded_message = x.encoded_message
    encoder_dict = x.encoder
    decoder_dict = x.decoder
    finished_encoded_message = ""
    for char in unencoded_message:
        if char == ' ':
            finished_encoded_message += (" " * 7)
        else:
            finished_encoded_message += encoder_dict[char] + "   "

    words = encoded_message.split("       ")
    revealed_message = ""

    for word in words:
        letter_list = word.split("   ")
        for letter in letter_list:
            revealed_message += decoder_dict[letter]
        revealed_message += ' '
    print(finished_encoded_message)
    print(revealed_message)
    

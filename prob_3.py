import sys

def find_frequency(a_string):

    freq_dict = {}
    freq_list = []
    for letter in a_string:
        if letter not in freq_dict:
            freq_dict[letter] = 1
        else:
            freq_dict[letter] += 1

    for key, value in freq_dict.items():
        freq_list.append((value, key))

    return sorted(freq_list)

def huffman_encoding(data):
    freq = find_frequency(data)
    #while list lasts
    #add slow lowest numbers
    


result = huffman_encoding('good morning')


def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

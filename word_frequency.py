def word_frequency(text):
    word_list = text.split()
    frequency_dict = {}
    for word in word_list:
        word = word.lower()  # Convert word to lowercase to treat uppercase and lowercase as the same
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    return frequency_dict

def get_word_occureence(str):
    final_list = dict ()
    x = input ("Send me the list")
    words = str.split(" ")
    for word in words:
        if word in final_list:
            final_list[word] += 1
        else:
            final_list[word] =1

    return final_list
print (get_word_occureence("the quick brown fox jumps over the lazy dog."))
def sort_word(str):

   word = [word for word in str.split(",")]
   print(",".join(list(set(word))))


#input_1=input ("Input command separated sequene of words")
sort_word("black,green,pink,red,green,pink,red")
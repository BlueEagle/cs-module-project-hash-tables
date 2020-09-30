import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
# ig = ["?", "!", "\"", "'", ":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]
# for c in ig:
#         words = words.replace(c, "")
sp = ["\n", "\t", "\r"]
for c in sp:
    words = words.replace(c, " ")
words = words.split(" ")

# print(words)
follower_dict = {}
keys = []
for i in range(0, len(words)):
    w = words[i]
    keys.append(w)

    if len(w) > 0: # the current word is not an empty string
        if w in follower_dict: # there is an entry for that word
            if i+1 < len(words): # the next word exists
                next_word = words[i+1]
                if len(next_word) > 0: # the next word is not empty
                    follower_dict[w].append(next_word)
        else:
            if i+1 < len(words): # the next word exists
                next_word = words[i+1]
                if len(next_word) > 0: # the next word is not empty
                    follower_dict[w] = [next_word]
    
# print(follower_dict)



# TODO: construct 5 random sentences
# Your code here

def is_valid_start_word(word):
    return (word[0] == "\"" and word[1].isupper()) or word[0].isupper()

def is_valid_end_word(word):
    last_index = -1
    if word[last_index] == "\"":
        last_index = -2
    
    return word[last_index] == "." or word[last_index] == "?" or word[last_index] == "!"

def markov():
    start_word = 'yo'
    while not is_valid_start_word(start_word):
        start_word = random.choice(keys)

    print(start_word)
markov()
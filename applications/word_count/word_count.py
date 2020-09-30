def word_count(s):
    # Your code here
    ig = ["\"", ":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]

    for c in ig:
        s = s.replace(c, "")

    sp = ["\n", "\t", "\r"]
    for c in sp:
        s = s.replace(c, " ")
    s = s.split(" ")

    d = {}
    for w in s:
        if len(w) > 0:
            w_low = w.lower()
            if w_low in d:
                d[w_low] += 1
            else:
                d[w_low] = 1
    return d



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
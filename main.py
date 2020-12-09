
def alphabet_position(text):
    alphabets = {chr(n): n-96 for n in range(97,123)}
    new_string = []
    text = text.lower()
    for i in text:
        if i in alphabets.keys():
            new_string.append(alphabets.get(i))
        else:
            return ''
    string_position = ' '.join(map(str,new_string))
    return str(string_position)

print(alphabet_position('abAc'))
# output '1 2 1 3'
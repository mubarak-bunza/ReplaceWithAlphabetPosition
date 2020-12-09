
alphabets = {chr(n): n-96 for n in range(97,123)}

sentence = 'abcAdz'.lower()
new_sentence = []
for i in sentence:
  if i in alphabets.keys():
    new_sentence.append(alphabets.get(i))

new = ''.join(map(str,new_sentence))
print(new)
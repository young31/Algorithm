# young 121ms, 165
letter = list(input())
 
for i in range(0,len(letter)) :
    if letter[i].islower() :
        letter[i] = letter[i].upper()
 
letter2 = "".join(letter)
 
print(letter2)
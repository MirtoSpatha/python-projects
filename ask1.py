'''βρίσκει τις πέντε μεγαλύτερες λέξεις ενός κειμένου το οποίο διαβάζει από αρχείο 
και τις εκτυπώνει ανάποδα, έχοντας αφαιρέσει τα φωνήεντα'''
file = open ("ask1.txt", "r")
text = file.read()
text = text.split()
print (text)
longestWords=[] 

for j in range (0,5):
    max = 0
    biggestWord = ""
    for i in range (0,len(text)):
        if len(text[i]) > max:
            biggestWord = text[i]
            max = len(text[i])
            position = i  
    longestWords.append(biggestWord)
    text.pop(position)
print(longestWords)
vowels = "aeyuio"
print(list(vowels))

for word in longestWords:
    List = []
    for letter in word:
        if letter not in list(vowels):
            List.append (letter)
    print(List[::-1])
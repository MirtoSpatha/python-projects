'''παίρνει ένα κείμενο από ένα αρχείο και το σπάει σε λεξεις.
 Αν οι λέξεις έχουν μήκος πάνω από 3 γράμματα, 
 αφαιρέστε το πρώτο γράμμα και προσθέστε το γράμμα στο τέλος μαζί με το ay.'''
openfile=open("ask5.txt", "r")
file=openfile.read ()
file=file.split()
print(file)
word=[]
for word in file:
    bigWord = ""
    if len(word)>3:
        bigWord += word[1::]
        kataliksi = word[0] + "ay"
        bigWord += kataliksi
        print(bigWord)

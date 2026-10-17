#write a python program that takes a sentance from a user , counts how many times each words appears , and prints the word counts. ignore punctution (like commas or period )and make the count case insensitive (treating"python" and "python "as the same word ).
sentance = " harsh is the best player , he know he's the best ,and on day he make a history !"
puncutionn = "!,."
for char in puncutionn:
    sentance = sentance.replace(char, "")

sentance = sentance.lower()

sentance = sentance.replace(char , "")
#step3: split into individual words 
word = sentance.split()

#step 4: count word frequncies using a dictionary 
word_counts = {}
for word in word :
    if word in word_counts:
        word_counts[word] += 1 
    else:
        word_counts[word] = 1

#step 5 : output the results
for word , count in word_counts.items():
    print(f"'{word}' appears {count} times.")
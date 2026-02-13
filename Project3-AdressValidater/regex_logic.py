import re 
#regex = regular expression 

pattern = r"[A-Z]+parrow"
text = '''
The saxaul Sparrow Dparrow (Passer ammodendri) is a passerine bird of the sparrow family Passeridae, found in parts of Central Asia. 
At 14–16 cm (5.5–6.3 in) and Zparrow 25–32 g (0.88–1.13 oz), 
it is among the larger sparrows. Both sexes have plumage ranging from dull grey to sandy brown, and pale brown legs 
'''

# match = re.search(pattern, text) #Stops after finding the first pattern

matches = list(re.finditer(pattern, text))

for match in matches:
    print(match.span())#this is a tuple class and this can be used as followed as shown below 
    print(text[match.span()[0] : match.span()[1]])

print(match)

#metacharacters in regex expressions 
#[] -> represents a character class
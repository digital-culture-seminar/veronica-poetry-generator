# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 10:50:11 2018

@author: Veronica Ly
"""

# lists of words
nouns = ["high chair", "throne", "toilet", "power"]
adjectives = ["soiled", "wasted", "decayed", "untouched", "contaminated"]
verbs = ["Sit", "Flop", "Collapse", "Perch", "Rest", "Sink"]

listA = "What is (your) right?"
listB = "Nowadays..."
listC = "It's all just"

# select random words from lists
noun = random.choice(nouns)
adjective = random.choice(adjectives)
verb = random.choice(verbs)
#adverb = random.choice(adverbs)

print "The {noun} sits empty.".format(adjective=adjective, noun=noun, adverb=adverb, verb=verb)
print "but at the base,"
print "at the root"
print "the soil is {adjective}.""\r\n".format(adjective=adjective, noun=noun, adverb=adverb, verb=verb)
print "{verb} down.".format(adjective=adjective, noun=noun, adverb=adverb, verb=verb)
print "Stand up."
print listA, "\r\n", listB, listC, "\r\n"
for listD in ["Take", "Snatch", "Grab", "\r\n"]:
    print(listD)


#The High Chair sits empty. 

#But at the base
#at the root
#the soil is soiled. 

#Sit down.
#Stand up
#What is (your) right?

#Nowadays 
#It’s all just take, take, take.
print "Take the stand."
print "Take a knee." 
print "Take a seat.""\r\n"

A = "Who is she to say?"
B = "Who is he to judge?"

C = "In this cult of culture"
D = "I move"
E = "the aggrieved approach the bench"
F = "Better still"
G = "In this overgrown schoolyard"
H = "I motion"
I = "For a recess..."

J = "Everyone"
K = "Have several seats."

print A, B, C, D, E, F, G, H, I, J, K


   
# print a sentence with random words from the lists
#print "The {adjective} {noun} {adverb} {verb}.".format(adjective=adjective, noun=noun, adverb=adverb, verb=verb)

# shuffle the list of adjectives
#random.shuffle(adjectives)
#random.shuffle(nouns)

i = 0
for nouns in nouns:
   i = i + 1
    #print "The {adjective} {noun} {adverb} {verb}.".format(adjective=random.choice(adjectives), noun=noun, adverb=adverb, verb=verb)
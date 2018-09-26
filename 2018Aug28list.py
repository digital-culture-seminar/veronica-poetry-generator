# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import random

# set the random seed
random.seed()

# lists of words
nouns = ["sailor", "ship", "sloth", "helper", "alien", "sorceror", "python", "bug"]
verbs = ["laughed out loud", "rolled on the floor laughing", "slept", "read", "declaimed", "roared", "glittered"]
adjectives = ["giant", "raucous", "playful", "sparkling", "sleepy", "scornful", "arrogant", "stealthy", "mechanical", "magical"]
adverbs = ["loudly", "silently", "playfully", "sneakily", "proudly", "tearfully", "mindfully", "boldly", "gently", "disdainfully"]

# select random words from lists
noun = random.choice(nouns)
verb = random.choice(verbs)
adjective = random.choice(adjectives)
adverb = random.choice(adverbs)
   
# print a sentence with random words from the lists
print "The {adjective} {noun} {adverb} {verb}.".format(adjective=adjective, noun=noun, adverb=adverb, verb=verb)

# shuffle the list of adjectives
random.shuffle(adjectives)
random.shuffle(nouns)

i = 0
for nouns in nouns:
    i = i + 1
    print "The {adjective} {noun} {adverb} {verb}.".format(adjective=random.choice(adjectives), noun=noun, adverb=adverb, verb=verb)


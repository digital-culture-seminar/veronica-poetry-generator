# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 20:15:25 2018

@author: Veronica and Camille

"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import random

#print "The {adjective} {noun} {adverb} {verb}.".format(adjective=adjective, noun=noun, adverb=adverb, verb=verb)

# set the random seed
random.seed()

# lists of words
nouns = ["shadows", "sailor", "ship", "sloth", "helper", "alien", "sorceror", "python", "bug"]
verbs = ["laughed out loud", "rolled on the floor laughing", "slept", "read", "declaimed", "roared", "glittered"]
adjectives = ["giant", "raucous", "playful", "sparkling", "sleepy", "scornful", "arrogant", "stealthy", "mechanical", "magical"]
adverbs = ["loudly", "silently", "playfully", "sneakily", "proudly", "tearfully", "mindfully", "boldly", "gently", "disdainfully"]

# select random words from lists
noun = random.choice(nouns)
verb = random.choice(verbs)
adjective = random.choice(adjectives)
adverb = random.choice(adverbs)

print "Dark Cloud"   
# print a sentence with random words from the lists
# shuffle the list of adjectives
random.shuffle(adjectives)
random.shuffle(nouns)

# i = 0
# for nouns in nouns:
#    i = i + 1
#    print "The {adjective} {noun} {adverb} {verb}.".format(adjective=random.choice(adjectives), noun=noun, adverb=adverb, verb=verb)

#Dark cloud
#When shadows hang overhead,
#Darkness falls.
#A heaviness slows his breathing and his body,
#And his mind screams obstructive, cynical thoughts.
#Attempting to reject the fateful calls, 
#He fill his head with reminders of those he holds dear.  
#Sadness engulfs deep within his soul.
#Latching onto him and not letting him go.
    
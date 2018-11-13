# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 19:31:18 2018

@author: Veronica
"""

# import libraries

import markovify 




# get raw text as string

with open("../readings/poem2.txt") as f:

    lovecraft = f.read()



with open("../readings/satyricon.txt") as f:

    satyricon = f.read()



# build and combine the models

lovecraft_model = markovify.Text(lovecraft)

satyricon_model = markovify.Text(satyricon)

model_synthesis = markovify.combine([lovecraft_model, satyricon_model], 

    [ 1.5, 1 ])



# print five randomly-generated sentences

for i in range(5):

    print model_synthesis.make_sentence()
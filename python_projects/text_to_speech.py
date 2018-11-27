# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:29:38 2018

@author: Veronica 


"""

# import libraries

from playsound import playsound

from gtts import gTTS

import markovify



# get raw text as string

with open("poem_2") as f:

    text = f.read()



# build the markov model

text_model = markovify.NewlineText(text)



# print a randomly-generated sentence of no more than 140 characters

markov_poem = text_model.make_short_sentence(140)



# text to speech

tts = gTTS(text=markov_poem, lang='en')



# write audio file

tts.save("markovified-poem_2.mp3")



# play audio file

playsound("markovified-poem.mp3")
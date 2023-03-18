#example code in Python using NLTK to calculate the average sentence length in a given text:
#Need to install natural language toolkit to proceed; here's the link https://www.nltk.org/data.html
import nltk
from nltk.tokenize import sent_tokenize

# Define a function to calculate the average sentence length
def avg_sentence_length(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Calculate the total number of words and sentences
    num_words = sum(len(sentence.split()) for sentence in sentences)
    num_sentences = len(sentences)
    
    # Calculate the average sentence length
    avg_length = num_words / num_sentences
    
    return avg_length

#You can use this function by passing in a string of text as an argument:
text = "More and more people use computers, but not everyone agrees that this benefits society. Those who support advances in technology believe that computers have a positive effect on people. They teach hand-eye coordination, give people the ability to learn about faraway places and people, and even allow people to talk online with other people. Others have different ideas. Some experts are concerned that people are spending too much time on their computers and less time exercising, enjoying nature, and interacting with family and friends."

avg_length = avg_sentence_length(text)
print("Average sentence length:", avg_length)

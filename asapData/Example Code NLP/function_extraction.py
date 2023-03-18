#This code defines a function extract_features that takes a text as input and returns a dictionary of features that could be characteristic of text generated by AI. 
#In this example, the function checks for features related to sentence structure and syntax, distinctive vocabulary and word choice, overall coherence and flow, and use of examples and evidence.
#Need to install nltk before we can proceed
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# Define a function to extract features from a given text
def extract_features(text):
    features = {}
    
    # Tokenize the text into sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]
    
    # Check for sentence structure and syntax patterns
    if any('.' in sentence for sentence in sentences):
        features['uses_period'] = True
    if any('!' in sentence for sentence in sentences):
        features['uses_exclamation'] = True
    if any('?' in sentence for sentence in sentences):
        features['uses_question'] = True
        
    # Check for distinctive vocabulary and word choice
    common_words = ['computer', 'technology', 'internet']
    common_word_count = sum(1 for word in words if word.lower() in common_words)
    if common_word_count > 2:
        features['uses_common_words'] = True
        
    # Check for overall coherence and flow
    if len(sentences) > 3:
        sentence_lengths = [len(sentence) for sentence in sentences]
        if max(sentence_lengths) > 100:
            features['long_sentences'] = True
    
    # Check for use of examples and evidence
    if any('for example' in sentence for sentence in sentences):
        features['uses_example'] = True
    if any('according to' in sentence for sentence in sentences):
        features['uses_evidence'] = True
    
    return features
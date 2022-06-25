# Converting present continuous sentences into simple present tense 
# For active voice sentences only

# Importing libraries

import nltk
from nltk.tokenize import word_tokenize as wt
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer as wnl
lem = wnl()

# Function to convert POS tags of verbs into WordNet

def verb_to_wordnet(verb_tag):
    if verb_tag.startswith('V'):
        return 'v'

# Function to correct singular and plural

def correct_singular_plural(cont_sent_tag, cont_sent_lem):
    index = 0;

    for i in range(len(cont_sent_lem)):
        if cont_sent_lem[i]=='be':
            index = i


    if cont_sent_tag[index-1][1] == 'NN' or cont_sent_tag[index-1][1] == 'NNP' or cont_sent_tag[index-1][0].capitalize() == 'He' or cont_sent_tag[index-1][0].capitalize() == 'She' or cont_sent_tag[index-1][0].capitalize() == 'It':
    
        if cont_sent_lem[index+1][-1] == 'o' or cont_sent_lem[index+1][-1] == 's' or cont_sent_lem[index+1][-2:] == 'ss' or cont_sent_lem[index+1][-1] == 'z' or cont_sent_lem[index+1][-2:] == 'ch' or cont_sent_lem[index+1][-2:] == 'sh' or cont_sent_lem[index+1][-1] == 'x':
            cont_sent_lem[index+1]+='es'
        
        elif cont_sent_lem[index+1][-1] == 'y':
            if cont_sent_lem[index+1][-2] == 'a' or cont_sent_lem[index+1][-2] == 'e' or cont_sent_lem[index+1][-2] == 'i' or cont_sent_lem[index+1][-2] == 'o' or cont_sent_lem[index+1][-2] == 'u':
                cont_sent_lem[index+1]+='s'
            else:
                cont_sent_lem[index+1] = cont_sent_lem[index+1].replace(cont_sent_lem[index+1][-1],'ies')
        
        elif cont_sent_lem[index+1] == 'have':
            cont_sent_lem[index+1] = cont_sent_lem[2].replace('have','has')
        
        else:
            cont_sent_lem[index+1]+='s'
            
    return cont_sent_lem
    


# Function for the conversion

def prescont_to_simpress(prescont):
    
    # Tokenizing
    cont_sent_token = wt(prescont)
    cont_sent_tag = nltk.pos_tag(cont_sent_token)
    
    # Lemmatizing
    cont_sent_lem = []

    for i in cont_sent_tag:
        wordnet_verb = verb_to_wordnet(i[1])
    
        if wordnet_verb is not None:
            cont_sent_lem.append(lem.lemmatize(i[0], wordnet_verb))
        else:
            cont_sent_lem.append(i[0])
       
    # Correcting singular and plural
    cont_sent_lem = correct_singular_plural(cont_sent_tag, cont_sent_lem)
    
    cont_sent_lem.remove('be')
    
    # Simple present tense form
    print(' '.join(cont_sent_lem))


# Calling the function, for different present continuous active voice sentences

prescont_to_simpress("I am going home")
prescont_to_simpress("She is staying at a hotel")
prescont_to_simpress("He is watching TV")
prescont_to_simpress("They are studying for the exam")
prescont_to_simpress("Harry Potter is coming to Hogwarts")
prescont_to_simpress("South Africans are winning the match")
prescont_to_simpress("John is waiting for the bus")
prescont_to_simpress("The king is kissing the queen")
prescont_to_simpress("Bees are buzzing")
prescont_to_simpress("We are enjoying ourselves")


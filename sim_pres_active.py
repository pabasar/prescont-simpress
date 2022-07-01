# Converting present continuous sentences into simple present tense 
# For active voice sentences only

# Importing libraries

import nltk
from nltk.tokenize import word_tokenize as wt
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lem = WordNetLemmatizer()

# Function to convert POS tags of verbs into WordNet

def verb_to_wordnet(verb_tag):
    if verb_tag.startswith('V') or verb_tag.startswith('JJ'):
        return 'v'


# Function to correct singular/plural and positive/negative

def correct_singular_plural(cont_sent_tag, cont_sent_lem):
    
    index = 0;

    for i in range(len(cont_sent_lem)):
        if cont_sent_lem[i]=='be':
            index = i

    if 'not' in cont_sent_lem:
        pos_neg = 'neg'
    else:
        pos_neg = 'pos'
        

    if cont_sent_tag[index-1][1] == 'NN' or cont_sent_tag[index-1][1] == 'NNP' or cont_sent_tag[index-1][1] == 'JJ' or cont_sent_tag[index-1][0].capitalize() == 'He' or cont_sent_tag[index-1][0].capitalize() == 'She' or cont_sent_tag[index-1][0].capitalize() == 'It':
    
        if pos_neg == 'pos':
        
            if cont_sent_lem[index+1][-1] == 'o' or cont_sent_lem[index+1][-1] == 's' or cont_sent_lem[index+1][-1] == 'z' or cont_sent_lem[index+1][-2:] == 'ch' or cont_sent_lem[index+1][-2:] == 'sh' or cont_sent_lem[index+1][-1] == 'x':
                cont_sent_lem[index+1]+='es'
        
            elif cont_sent_lem[index+1][-1] == 'y':
                if cont_sent_lem[index+1][-2] == 'a' or cont_sent_lem[index+1][-2] == 'e' or cont_sent_lem[index+1][-2] == 'i' or cont_sent_lem[index+1][-2] == 'o' or cont_sent_lem[index+1][-2] == 'u':
                    cont_sent_lem[index+1]+='s'
                else:
                    cont_sent_lem[index+1] = cont_sent_lem[index+1].replace(cont_sent_lem[index+1][-1],'ies')
        
            elif cont_sent_lem[index+1] == 'have':
                cont_sent_lem[index+1] = cont_sent_lem[index+1].replace('have','has')
        
            else:
                cont_sent_lem[index+1]+='s'
            
            cont_sent_lem.remove('be')
    
        else:
        
            cont_sent_lem = ['does' if word == 'be' else word for word in cont_sent_lem]
        
    else:
        if pos_neg == 'pos':
            cont_sent_lem.remove('be')
        else:
            cont_sent_lem = ['do' if word == 'be' else word for word in cont_sent_lem]
            
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
    
    # Simple present tense form
    print(' '.join(cont_sent_lem))


# Calling the function, for different present continuous active voice sentences

prescont_to_simpress("I am doing my homework")
prescont_to_simpress("She is studying for the exam")
prescont_to_simpress("John is not watching TV")
prescont_to_simpress("They are not staying today")
prescont_to_simpress("An Indian is arriving in India")
prescont_to_simpress("South Africans are winning the match")
prescont_to_simpress("He is waiting for the bus")
prescont_to_simpress("The king is kissing the queen gently")
prescont_to_simpress("Bees are buzzing around the honeycomb")
prescont_to_simpress("Parrots are flying around the village peacefully")
prescont_to_simpress("A carpenter is building a bookcase")
prescont_to_simpress("We are enjoying ourselves")
prescont_to_simpress("The pianist is playing Fur Elise softly")


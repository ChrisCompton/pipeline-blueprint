#%%
#pip install -U 'spacy[transformers,lookups,apple]'
import pandas as pd
from tqdm import tqdm
import spacy

from spacy.tokens import DocBin 

#%%
nlp = spacy.blank("en")
db = DocBin()

TEST_DATA = [
    ("navigate home to get some sleep.", {"entities": [(9,13, "LOCATION")]}),
    ("navigate to office", {"entities": [(12,18, "LOCATION")]}),
    ("navigate", {"entities": []}),
    ("navigate to Oxford Street", {"entities": [(12, 25, "LOCATION")]})
]

#%%
for text, annot in tqdm(TEST_DATA): # data in previous format
    doc = nlp.make_doc(text) # create doc object from text
    ents = [] 
    for start, end, label in annot["entities"]: # add character indexes
        span = doc.char_span(start, end, label=label, alignment_mode="contract") 
        if span is None: 
            print(f"Skipping entity for {text}") 
        else: 
            ents.append(span) 
            doc.ents = ents # label the text with the ents
    db.add(doc) 

#%%

db.to_disk("./test_data.spacy") # save the docbin object
# %%

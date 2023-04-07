# python -m spacy init fill-config base_config.cfg config.cfg
# python -m spacy train config.cfg --output ./output --paths.train ./training_data.spacy --paths.dev ./test_data.spacy
#%%
import spacy

#%%
nlp1 = spacy.load(R"output/model-last")
doc = nlp1("Navigate to the office")

#%%
spacy.displacy.render(doc, style="ent", jupyter=True)

#%%
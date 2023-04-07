# pipeline-blueprint

This is a sample SpaCy pipeline.

> WARNING: This is just for establishing the workflow.  This is NOT an example of how to train and test a model.

What this DOES do, is show how to:

- create a training and test spacy file
- execute spacy to train the model and produce the output directory
- load the trained model and attempt to name an entity

test and training data should not be the same, and needs more of it.

## Steps

```
pip install -r requirements.txt
cd src
python -m spacy init fill-config base_config.cfg config.cfg
python pipeline_training_data.py
python pipeline_test_data.py
python -m spacy train config.cfg --output ./output --paths.train ./training_data.spacy --paths.dev ./test_data.spacy
python pipeline.py
```
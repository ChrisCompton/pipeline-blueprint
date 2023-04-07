# pipeline-blueprint

This is a sample SpaCy pipeline.

## Steps

```
python -m spacy init fill-config base_config.cfg config.cfg
python pipeline_training_data.py
python pipeline_test_data.py
python -m spacy train config.cfg --output ./output --paths.train ./training_data.spacy --paths.dev ./test_data.spacy
python pipeline.py
```
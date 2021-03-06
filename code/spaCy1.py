"""---------------------------------------------------
	SpaCy : 
		Utterance classification with SpaCy
		by comparing complete sentences
-------------------------------------------------------"""

import pandas as pd
import numpy as np

from preprocessing import *
from vectorization_spaCy import *

"""
NLP: class in .csv file
	0. Dyads
	1. Participant
	2. Id
	3. EAT	
	4. StartTime 
	5. EndTime
	6. Duration
	7. Utterances
	8. Subcategories	
	9. Categories
"""

""" Step 1: Extract data from file """

dataFile='collaborativeActs.csv'

df = pd.read_csv(dataFile,delimiter="\t",header=None,error_bad_lines=False, encoding="utf8")

#categories, classification of the utterances of the file according to their type
categories = ["Interaction management", "Social relation", "Task management", "Information", "Transactivity", "Tool", "Other"]
ut_by_categ=[[x for x, t in zip (df[7], df[9]) if t == c] for c in categories]

utterances=df[7]
subcategories=df[8]
categories=df[9]


""" Step 2: Preprocessing of data """
utterances_norm=[normalization(utterance) for utterance in utterances]

""" Step 3: Vectorization of sentences """
vect = [ vectorization1(utterance) for utterance in utterances_norm]


""" Step 4: Classification """
# WARNING !!!! Fix SpaCy warning [W007] before this step : a model has to be loaded : https://spacy.io/usage/vectors-similarity
# it might be possible to use .similarity with kNN or clustering but it costs lot of memory

"""ModelsWarning: [W007] The model you're using has no word vectors loaded, so the result of the
Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity
judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship
with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one
of the larger models instead if available"""



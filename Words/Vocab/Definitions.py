"""
Script to automate defining a bunch of vocab words I want to study
"""

# imports
from PyDictionary import PyDictionary
import csv

# dictionary of words I want to know
dictionary = PyDictionary(
    "gregarious",
    "obsequious",
    "ascetic",
    "pander",
    "maudlin",
    "wanton",
    "effette",
    "patronize",
    "expiate",
    "importune",
    "scintilate",
    "adonis",
    "sycophant",
    "benevolence",
    "compunction",
    "supercilious",
    "imbroglio",
    "peccadilio",
    "panacea",
    "diffident",
    "effervescent",
    "quixotic",
    "inane",
    "adroit",
    "didactic",
    "glibly",
    "parsimonious",
    "philistine",
    "uxorious",
    "persiflage",
    "epigram",
    "poignant",
    "specious",
    "unctuous",
    "gumption"
)

pd2 = PyDictionary(
    'derision', ' Priapus', 'eructation', 'assay', 'incantation', 'perfidy', 'precocious', 'cantankerous', 'garlands',
    'abject', 'fallow', 'tunic', 'coquetry',  'sallow', 'codicils', 'doltish', 'paregoric', 'reveille', 'stolid',
    'inimical', 'ersatz', 'accoutred', 'elixir', 'treacle', 'odious', 'embedment', 'atavistic',
    'concertinaed', 'arbiter'
)

dd = pd2.getMeanings()
print(dd)

with open('defs.csv', 'w') as f:
    for key in dd.keys():
        f.write("%s,%s\n"%(key,dd[key]))

# end of script

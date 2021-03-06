import json
# from os.path import join, dirname
from watson_developer_cloud import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
    username='',
    password='')

classifiers = natural_language_classifier.list()
print(json.dumps(classifiers, indent=2))


# create a classifier
with open('./trainingData.csv', 'rb') as training_data:
     print(json.dumps(natural_language_classifier.create(training_data=training_data, name='weather'), indent=2))
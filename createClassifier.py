import json
# from os.path import join, dirname
from watson_developer_cloud import NaturalLanguageClassifierV1

# create a classifier
with open('../resources/weather_data_train.csv', 'rb') as training_data:
     print(json.dumps(natural_language_classifier.create(training_data=training_data, name='weather'), indent=2))
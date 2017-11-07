import json
# from os.path import join, dirname
from watson_developer_cloud import NaturalLanguageClassifierV1
import credentials

natural_language_classifier = NaturalLanguageClassifierV1(
    username= credentials.USER_ID,
    password= credentials.PASSWORD)


# replace 2374f9x68-nlc-2697 with your classifier id
status = natural_language_classifier.status(credentials.classifier_id)
print(json.dumps(status, indent=2))

if status['status'] == 'Available':
    with open('./trainingData.csv', 'rb') as training_data:
        for row in training_data:
            row = row.split(',')
            row[0] = row[0].strip()
            classes = natural_language_classifier.classify(credentials.classifier_id, row[0])
            assert str(classes["top_class"]) == str(row[1]).strip()
            #print(json.dumps(classes, indent=2))

# delete = natural_language_classifier.remove('2374f9x68-nlc-2697')
# print(json.dumps(delete, indent=2))

# example of raising a WatsonException
# print(json.dumps(
#     natural_language_classifier.create(training_data='', name='weather3'),
#     indent=2))
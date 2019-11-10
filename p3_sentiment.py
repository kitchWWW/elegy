import unicodedata
import argparse
import os
import json
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def write_result(annotations):
    print(annotations)
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    with open("sentence_sentiment.json","a") as f:
        f.write("{\n")        
        f.write("\t\"sentences\": [\n")
        for index, sentence in enumerate(annotations.sentences):
            sentence_sentiment = sentence.sentiment.score
            f.write("\t\t{\n")
            f.write("\t\t\t\"text\": \""+str(sentence.text.content)+"\",\n")
            f.write("\t\t\t\"sentiment\": "+str(sentence_sentiment)+"\n")
            if index == len(annotations.sentences)-1:
                f.write("\t\t}\n")
            else:
                f.write("\t\t},\n")
        f.write("\t]\n")
        f.write("}\n")
 

    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    return 0


def analyze(radiolab_filename):
    """Run a sentiment analysis request on text within a passed filename."""
    fd = open("sentence_sentiment.json","w")
    fd.write("")
    fd.truncate()
    fd.close()
    
    client = language.LanguageServiceClient()

    with open(radiolab_filename, 'r') as review_file:
        # Instantiates a plain text document.
        content = review_file.read()
    unicodedata.normalize('NFKD', unicode(content, "utf-8")).encode('ascii','ignore')

    sentences_scores = []
    bit = content.split(". ")
    for b in bit:
        document = types.Document(
            content=b,
            type=enums.Document.Type.PLAIN_TEXT)
        sent_annotations = client.analyze_sentiment(document=document)
        ent_annotations  = client.analyze_entity_sentiment(document=document)
        write_result(sent_annotations);
        # Print the results
        print(sent_annotations)
        sentences_scores.append(sent_annotations.document_sentiment.score)
        sentences_scores.append(sent_annotations.document_sentiment.score)
    # outfd = open("sentence_sentiment.json",'w')
    # outfd.write(json.dumps(sentences_scores))
    # outfd.close()

def get_sentiment(transcript_filename):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'auth.json'
    analyze(transcript_filename)


get_sentiment("text.txt")







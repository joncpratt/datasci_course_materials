import sys
import json

#sent_file = dictionary sentiments file
#tweet_file = raw twitter stream output

def lines(fp):
    print str(len(fp.readlines()))
    json.loads(fp.read())


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    print scores.items()

    tweets = {}
    for line in tweet_file:
        #print type(line)
        tweet = json.loads(line)
        if 'text' in tweets.keys():
            text = tweet['text']
            text = text.encode('utf-8')
            print text
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
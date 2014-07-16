import sys
import json
#sent is short for sentiment
"""
instead of printing the number of lines in the AFINN file, read it into a dictionary structure
instead of printing the number of lines in the output.txt file, iterate over each line
parse each json line and check for the availability of the item in this dictionary that contains the actual tweet
calculate the score for this item, multiple strategies may apply (cherry picking languages, discarding unwanted characters, different splitting techniques etc.). 
You will essentially compare entries of the sentiment file and parts of the tweet.
"""

def main():
	sent_file = open('AFINN-111.txt')
	tweet_file = open('problem_1_submission.txt')
	
	scores = {}
	for line in sent_file:
		term, score = line.split("\t")
		scores[term] = int(score)
	#print scores.items()
	
	#tweet = {}	
	#tweet=json.load(tweet_file)
	
	
	
	tweet={}
	json_tweets = []
	for line in tweet_file:
		tweet = json.loads(unicode(line))
		json_tweets.append(tweet)
	#print json_tweets
	
	#for line in tweet_file:
	#	tweet = json.load(tweet_file)
	#if not 'text' in tweets:
	#	continue  # skip over tweet without text body
	if 'text' in tweet:
		text = tweet['text']
		text = text.encode('utf-8')	


	#except KeyError:
	#	pass
	print tweet.keys()

if __name__ == '__main__':
    main()
	


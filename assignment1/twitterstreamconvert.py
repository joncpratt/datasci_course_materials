import sys
import json

twitterstream = open("output1.txt")
line = {} # initialize an empty dictionary
for line in twitterstream:
 # term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    result = (json.loads(line)).get('text',"")
#print scores.items() # Print every (term, score) pair in the dictionary
#print result
print text.items()
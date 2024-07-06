from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# function to print sentiments
# of the sentence.

def sentiment_scores(user,sentence):

	# Create a SentimentIntensityAnalyzer object.
	sid_obj = SentimentIntensityAnalyzer()

	# polarity_scores method of SentimentIntensityAnalyzer
	# object gives a sentiment dictionary.
	# which contains pos, neg, neu, and compound scores.
	f1=0
	f2=0
	f3=0
	for sen in sentence:
		sentiment_dict = sid_obj.polarity_scores(sen)
		f1=f1+sentiment_dict['neg']*100
		f2=f2+sentiment_dict['neu']*100
		f3=f3+sentiment_dict['pos']*100
	if sentence!=[]:
		final1=f1/len(sentence)
		final2=f2/len(sentence)
		final3=f3/len(sentence)
		if sentiment_dict['compound'] >= 0.05 :
			Overall="Positive"

		elif sentiment_dict['compound'] <= - 0.05 :
			Overall= "Negative"

		else :
			Overall= "Neutral"
	else:
		final1='NaN'
		final2='NaN'
		final3='NaN'
		Overall='NaN'

	final_dict={'Username':user,'Positive':final3,'Negative':final1,'Neutral':final2,'Overall':Overall}	
	return final_dict
	print("Overall sentiment dictionary is : ", sentiment_dict)
	print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
	print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
	print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")

	print("Sentence Overall Rated As", end = " ")

	# decide sentiment as positive, negative and neutral
	if sentiment_dict['compound'] >= 0.05 :
		return	sentiment_dict['pos']*100, "Positive"

	elif sentiment_dict['compound'] <= - 0.05 :
		return sentiment_dict['neg']*100, "Negative"

	else :
		return sentiment_dict['neu']*100, "Neutral"
		
'''

# Driver code
if __name__ == "__main__" :

	print("\n1st statement :")
	sentence = "Geeks For Geeks is the best portal for \
				the computer science engineering students."

	# function calling
	sentiment_scores(sentence)

	print("\n2nd Statement :")
	sentence = "study is going on as usual"
	sentiment_scores(sentence)

	print("\n3rd Statement :")
	sentence = "I am very sad today."
	sentiment_scores(sentence)'''

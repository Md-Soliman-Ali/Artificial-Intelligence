def sortedSentence(Sentence): 
	 
	words = Sentence.split(" ") 
	
	words.sort() 
	
	newSentence = " ".join(words) 
	
	return newSentence 


Sentence = "My Name Is Khan And I'm Not A Terrorist"
print("\n",Sentence)
print(sortedSentence(Sentence)) 

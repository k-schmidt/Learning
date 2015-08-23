"""
Python Test Script for Naive Bayes on spam data provided by Spam Assassin

By: Kyle Schmidt
Date: 2015/02/22
"""

import os

files = os.listdir(r"/Users/kyleschmidt/Projects/spam")
#files = os.listdir(r"/Users/kyleschmidt/Projects/easy_ham")

with open("Spam.out", "a") as out:
#with open("dataSpam.out", "a") as out:

	n = 0
	for fname in files:
		with open("/Users/kyleschmidt/Projects/spam/" + fname) as f:
		#with open("/Users/kyleschmidt/Projects/easy_ham/" + fname) as f:
			data = f.readlines()
			for line in data:
				if line.startswith("Subject:"):
					n += 1
					print(n)
					line.replace(",", "")
					print(line)
					out.write("{0}, spam \n".format(line[8:-1]))
					#  out.write("{0}, nospam \n".format(line[8:-1]))
			print(fname)

def list_words(text):
	words = []
	words_tmp = text.lower().split()
	for w in words_tmp:
		if w not in words and len(w) > 3:
			words.append(w)
	return words

def training(texts):
	c_words = {}
	c_categories = {}
	c_texts = 0
	c_total_words = 0
	#add the classes to the categories
	for t in texts:
		c_texts += 1
		if t[1] not in c_categories:
			c_categories[t[1]] = 1
		else:
			c_categories[t[1]] += 1

	#add the words with list_words() function
	for t in texts:
		words = list_words(t[0])

	for p in words:
		if p not in c_words:
			c_total_words += 1
			c_words[p] = {}
			for c in c_categories:
				c_words[p][c] = 0
		c_words[p][t[1]] += 1
	return (c_words, c_categories, c_texts, c_total_words)


def classifier(subject_line, c_words, c_categories, c_texts, c_total_words):
	category = ""
	category_prob = 0

	for c in c_categories:

		prob_c = float(c_categories[c])/float(c_texts)
		words = list_words(subject_line)
		prob_total_c = prob_c
		for p in words:

			if p in c_words:
				prob_p = float(c_words[p][c])/float(c_total_words)
				prob_cond = prob_p/prob_c
				prob = (prob_cond * prob_p) / prob_c
				prob_total_c = prob_total_c * prob

			if category_prob < prob_total_c:
				category = c
				category_prob = prob_total_c
	return (category, category_prob)


if __name__ == "__main__":

	with open('training.csv') as f:
		subjects = dict(csv.reader(f, delimiter = ','))
		p,c,t,tp = training(subjects.items())

		#First Test
		clase = classifier("Available on Term Life - Free", p, c, t, tp)
		print("Result: {0} ".format(clase))

	#Second Test
	with open("test.csv") as f:
		correct = 0
		tests = csv.reader(f)
		for subject in tests:
			clase = classifier(subject[0], p, c, t, tp)
			if clase [0] == subject[1]:
				correct += 1
		print("Efficiency {0} of 10".format(correct))
					
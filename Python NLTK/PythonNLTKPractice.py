import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

text = "Google News is a free news aggregator provided and operated by Google, selecting news from thousands of news websites. A beta version was launched in September 2002, and released officially in January 2006."
tokenized_sentence = sent_tokenize(text)
print('------------------Sentence Tokenizer------------------')
print('sent_tokenize() returns a ' + str(type(tokenized_sentence)) +
      ' of tokens which are individual sentences.')
for i in tokenized_sentence:
    print(i)

print('------------------Word Tokenizer------------------')
tokenized_words = word_tokenize(text)
print('word_tokenize() returns a ' + str(type(tokenized_sentence)) +
      ' of tokens which are individual words.')
for i in tokenized_words:
    print(i)

print('------------------Stop words------------------')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Fetch the stopwords that are in ENGLISH only
stopwords = set(stopwords.words("english"))

# Let's have a look at these stopwords
print('Stopwords in nltk.corpus for English language:')
print(stopwords)

text = "Google News is a free news aggregator provided and operated by Google, selecting news from thousands of news websites."
words = word_tokenize(text)

filtered_sentence = [w for w in words if w not in stopwords]
print('Sentence after removing stopwords:')
print(filtered_sentence)
print('We were able to remove: \'' + '-'.join(i for i in words if i in stopwords) +
      '\' stopwords after filtration.')

print('------------------Stemming------------------')
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
text = "Google News is a free news aggregator provided and operated by Google, selecting news from thousands of news websites."
print()
words = word_tokenize(text)
print('Before stemming: ' + ','.join(i for i in words))
print('After stemming:  ' + ','.join(ps.stem(i) for i in words))
# Thus Stemming may or may not be useful

print('------------------POS Tagging------------------')
text = "Google News is a free news aggregator provided and operated by Google, selecting news from thousands of news websites."
print()
words = word_tokenize(text)

print('-'.join(i for i in words))
tagged_words = nltk.pos_tag(words)
print('-'.join(str(i) for i in tagged_words))
print('nltk.pos_tag() returns a ' + str(type(tagged_words))
      + ' of ' + str(type(tagged_words[0])))
print('Basically it returns a list of tuples. First value in the tuple is the WORD and second is it\'s POS TAG.')
# Get list of all possible POS tags available in nltk by uncommenting following next line
# print(nltk.help.upenn_tagset())


print('------------------Chunking------------------')
# Chunking = grouping of words
# Chunking helps in defining chunks. For example the sentence might be
sentence = "Mr. James Hetfield is the lead vocalis of metallica."
# we tokenize it
tokenized_sentence = word_tokenize(sentence)
# we tag these tokens (words)
tagged_words = nltk.pos_tag(tokenized_sentence)
print(tagged_words)
# Suppose we want to define "Mr. James Hetfield as a chunk"
# For that we define the structure of the chunk using RegExp

chunkGram = r"""ChunkForHetfieldLikeStructure: {<NNP><NNP><NNP>}"""
chunkParser = nltk.RegexpParser(chunkGram)
chunked_words = chunkParser.parse(tagged_words)
print(chunked_words)
# Get a tree diagram for this
# chunked_words.draw()
# Basically chunking helps in chhunking/grouping words with the help of RegExp


print('------------------Chinking------------------')
# Chinking = removal of certain stuff from a chunks
# Supposse we want everything from the following text except Nouns
text = "Mr. James Hetfield is the lead vocalis of metallica."
# tokenize
tokenized_words = word_tokenize(text)
# tagging
tagged_words = nltk.pos_tag(tokenized_words)
# Chinking from a Chunk
chunkGram = r"""Chunk:{<.*>+}
            }<NNP>+{"""  # Chinking RegExp between '}' and '{'
chunkParser = nltk.RegexpParser(chunkGram)
chunked = chunkParser.parse(tagged_words)
print(chunked)
# Draw the tree diagram
# chunked.draw()

print('------------------Named Entity Recognition------------------')
# Named Entity Recognition groups/taggs popular named entities as per their tags.
# for ex INDIA is a named entity with tag COUNTRY

text = "Hetfield is not an Indian. He's an American. India is a country."
# Tokenize
tokens = word_tokenize(text)
# Tagging
tagged_words = nltk.pos_tag(tokens)
# Named Entities
namedEnt = nltk.ne_chunk(tagged_words)
print(namedEnt)
# namedEnt.draw()

print('------------------Lemmatizing------------------')
# Lametizing is similar to stemming but the result is sensible. It is the actual root
# or a synonym that has a similar meaning

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('piegons'))
print(lemmatizer.lemmatize('dogs'))
print(lemmatizer.lemmatize('cats'))
# Default value for POS TAG is n = NOUN
print(lemmatizer.lemmatize('faster'))  # 2nd parameter - POS tag = n by default
print(lemmatizer.lemmatize('faster', 'a'))  # 2nd parameter - POS tag = a = adjective

print('------------------WordNet------------------')
from nltk.corpus import wordnet
syn = wordnet.synsets("good")
print(syn)
print(syn[0])
print(syn[0].lemmas())
print(syn[0].lemmas()[0])
# just the word
print(syn[0].lemmas()[0].name())

# Definition
print(syn[0].definition())

# Examples
print(syn[0].examples())

import docx
import string
from collections import Counter

# specify the path to your Word document
doc_path = "Word\samplepdf97.docx"

# load the document
doc = docx.Document(doc_path)

# initialize an empty list to store sentences
sentences = []

# iterate through each paragraph in the document
for paragraph in doc.paragraphs:
    # split the paragraph into sentences
    for sentence in paragraph.text.split(". "):
        # remove punctuation and convert to lowercase
        sentence = sentence.translate(str.maketrans("", "", string.punctuation)).lower()
        # strip any leading or trailing whitespace
        sentence = sentence.strip()
        # add the sentence to the list if it's not blank
        if sentence:
            sentences.append(sentence)

# count the frequency of each sentence and get the most common one
most_common_sentence = Counter(sentences).most_common(1)[0][0]

# print the most common sentence
print(most_common_sentence)

import scipy.spatial
import numpy as np
import re

with open("sent.txt", "r") as f:
    sentences = f.readlines()

i = 0
for sentence in sentences:
    sentence = re.split('[^a-z]', sentence.lower())

    # Rewrite sentence with removed empty strings '' after splitting
    sentences[i] = filter(None, sentence)
    i += 1

word_index = dict()
i = 0
for sentence in sentences:
    for word in sentence:
        if word not in word_index:
            word_index[word] = i
            i += 1

matrix = []
for sent_i in range(0, len(sentences)):
    matrix.append([0 for x in word_index])

    for word in sentences[sent_i]:
        word_i = word_index[word]
        matrix[sent_i][word_i] += 1

np_matrix = np.array(matrix)

distances = list()
for i in range(1, len(sentences)):
    distance = scipy.spatial.distance.cosine(np_matrix[0], np_matrix[i])
    distances.append((i, distance))

sorted_list = sorted(distances, key=lambda tup: tup[1])

print (sorted_list[1][0], sorted_list[2][0])

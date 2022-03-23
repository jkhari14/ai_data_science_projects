import math
import re


def review_cleaner(word_arr):

    words = word_arr
    baddies = [',', '.', '/', ':', ';', "#", "*", "&", "$", "@", "(", ")", "[", "]", "{", "}", "-"]
    for word_list in words:
        for word in word_list:
            ind = word_list.index(word)  # could change start index to make index() method faster
            for char in word:
                if char in baddies:
                    word_list[ind] = word_list[ind].replace(char, "")
            word_list[ind] = word_list[ind].lower()  # are the words not being changed?
    return words


class Bayes_Classifier:

    def __init__(self):
        self.pos_bucket = {}
        self.neg_bucket = {}

    def train(self, lines):
        for line in lines:  # assume for loop accurately goes from line to line
            line_arr = line.replace('\n','')
            line_arr = line_arr.split('|')
            if line_arr[0] == '1':
                review = line_arr[2].split(' ')  # makes list of words that can be fed to algo
                review_superset = []
                for i in range(len(review)):
                    review_superset.append([review[i]])
                for i in range(len(review)-1):
                    review_superset.append([review[i], review[i+1]])
                clean_review = review_cleaner(review_superset)
                self.update(clean_review, self.neg_bucket)
            elif line_arr[0] == '5':  # how does this boolean work?
                review = line_arr[2].split(' ')
                review_superset = []
                for i in range(len(review)):
                    review_superset.append([review[i]])
                for i in range(len(review) - 1):
                    review_superset.append([review[i], review[i + 1]])
                clean_review = review_cleaner(review_superset)
                self.update(clean_review, self.pos_bucket)

    def update(self, words, review_dict):
        for word in words:
            if not(' '.join(word) in review_dict):
                review_dict[' '.join(word)] = 1
            else:
                if len(word) == 1:
                    review_dict[' '.join(word)] += 1
                else:
                    not_good_clause = 10000000
                    review_dict[' '.join(word)] += not_good_clause

    def classify(self, lines):
        sum_pos = 0
        sum_neg = 0
        predict_array = []

        for key in self.pos_bucket:
            sum_pos += self.pos_bucket[key]
        for key in self.neg_bucket:
            sum_neg += self.neg_bucket[key]

        for line in lines:
            line_arr = line.replace('\n', '')
            line_arr = line_arr.split('|')
            pos_prob = 0
            neg_prob = 0
            review = line_arr[2].split(' ')
            review_superset = []
            for i in range(len(review)):
                review_superset.append([review[i]])
            for i in range(len(review) - 1):
                review_superset.append([review[i], review[i + 1]])
            clean_review = review_cleaner(review_superset)
            for word in clean_review:
                if not (' '.join(word) in self.pos_bucket):
                    numerator_pos = 1
                else:
                    numerator_pos = (self.pos_bucket[' '.join(word)] + 1)  # +1 is a smoothing method
                pos_prob += math.log(numerator_pos / sum_pos)

                if not (' '.join(word) in self.neg_bucket):
                    numerator_neg = 1
                else:
                    numerator_neg = (self.neg_bucket[' '.join(word)] + 1)
                neg_prob += math.log(numerator_neg / sum_neg)

            if neg_prob > pos_prob:
                predict_array.append('1')

            else:
                predict_array.append('5')

        return predict_array

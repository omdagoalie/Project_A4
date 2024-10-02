# Comp 1020
# 10/01/2024
# Om Soni
# Project A4
import random


class Spinner:
    def __init__(self, file):
        self.synonyms = {}
        self.find_synonyms(file)
    def find_synonyms(self, file):
        with open(file, 'r') as file_read:
            for line in file_read:
                line = line.strip()
                words, synonyms = line.split(':')
                synonyms_list = synonyms.split(',')
                self.synonyms[words] = synonyms_list


    def spinnn(self, text):
        words = text.split()
        spun = []
        for word in words:
            if word in self.synonyms:
                if random.randint(1, 100) > 50:
                    synonym = random.choice(self.synonyms[word])
                    spun.append(synonym)
                else:
                    spun.append(word)
            else:
                spun.append(word)

        return ' '.join(spun)





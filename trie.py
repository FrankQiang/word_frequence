#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


class Node:
    def __init__(self):
        self.value = None
        self.children = {}    # children is of type {char, Node}


class Trie:
    def __init__(self):
        self.root = Node()
        self.words_weight = {}

    def insert(self, key):
        # key is of type string
        # key should be a low-case string, this must be check
        key = key.lower()
        node = self.root
        for char in key:
            if char not in node.children:
                child = Node()
                node.children[char] = child
                node = child
            else:
                node = node.children[char]
        node.value = key

    def search(self, key):
        node = self.root
        for char in key:
            if char in node.children:
                node = node.children[char]
        if node.value and (len(node.value) == len(key)):
            # entire right
            return True
        else:
            print('trie no {0} this word'.format(key))
            return False

    def create_trie(self):
        with open("words.txt", 'r') as f:
            lines = f.readlines()
        for line in lines:
            self.insert(re.sub(r'\n', '', line))

    def generate_basic_word_weight(self):
        with open("words.txt", 'r') as f:
            lines = f.readlines()
            with open("frequence.txt", 'w') as f:
                for line in lines:
                    word = re.sub(r'\n', '', line)
                    f.write('{0},0\n'.format(word))

    def get_word_weight(self):
        with open("frequence.txt", 'r') as f:
            lines = f.readlines()
        for line in lines:
            line = re.sub(r'\n', '', line)
            line = line.split(',')
            word = line[0].lower()
            weight = line[1]
            self.words_weight[word] = int(weight)

    def generate_word_weight(self):
        with open("text.txt", 'r') as f:
            lines = f.readlines()
        for line in lines:
            word = re.sub(r'\n', '', line)
            if self.search(word):
                self.words_weight[word] += 1
        with open("frequence.txt", 'w') as f:
            for word in self.words_weight:
                f.write('{0},{1}\n'.format(word, self.words_weight[word]))

    def main(self):
        self.create_trie()
        self.generate_basic_word_weight()
        self.get_word_weight()
        self.generate_word_weight()


if __name__ == '__main__':
    trie = Trie()
    trie.main()

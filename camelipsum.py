#!/usr/bin/env python
#-*-coding: utf-8

# Camel Ipsum Generator

import sys, os, random, argparse

if __name__ != '__main__':
    print("Not a module!")
    sys.exit(1)

parser = argparse.ArgumentParser(description='To tell me how many paragraphs')
parser.add_argument('length', type=int, help='Paragraph count to generate')
args = parser.parse_args()

PLENGTH = args.length

BASE = ['consectetur', 'adipisicing', 'elit', 'sed', 'do', 'eiusmod', 'tempor',
        'incididunt', 'ut', 'labore', 'et', 'dolore', 'magna', 'aliqua', 'ut', 'enim', 'ad',
        'minim', 'veniam', 'quis', 'nostrud', 'at', 'exercitation', 'ullamco', 'laboris', 'nisi',
        'ut', 'aliquip', 'ex', 'ea', 'commodo', 'consequat', 'duis', 'aute', 'irure',
        'dolor', 'in', 'reprehenderit', 'in', 'voluptate', 'velit', 'esse', 'cillum', 'dolore',
        'eu', 'fugiat', 'nulla', 'pariatur', 'excepteur', 'sint', 'occaecat', 'cupidatat', 'non',
        'proident', 'sunt', 'in', 'culpa', 'qui', 'officia', 'deserunt', 'mollit', 'anim', 'id',
        'est', 'laborum']

CAMEL = ['camel', 'arab', 'pyramid', 'sun', 'desert', 'toe', 'hump', 'egypt', 'cornivore', 'two-humped',
         'llama', 'alpaca', 'guanaco', 'at', 'muslim', 'brown', 'lady fantasy', 'amber', 'camel light', 'camel soft',
         'mammal', 'fat', 'fatty', 'bear grylls', 'kabab']

SENTENCE_LENGTH_MIN = 8
SENTENCE_LENGTH_MAX = 20
STARTS_WITH = "camel ipsum dolor sit ahmet "

def shuffle():
    camel_count = len(CAMEL) - 1
    for i in range(0, camel_count):
        rnd = random.randint(0, camel_count)
        BASE.append(CAMEL[rnd])
        del(CAMEL[rnd])
        camel_count = camel_count - 1
    base_count = len(BASE) - 1
    for i in range(0, base_count):
        rnd = random.randint(0, base_count)
        tmp = BASE[i]
        BASE[i] = BASE[rnd]
        BASE[rnd] = tmp
        
def merge():
    shuffle()
    
def get_camel_ipsum():
    rnd = random.randint(0, len(BASE) - 1)
    result = ""
    for i in range(0, rnd):
        shuffle()
    sentence_length = random.randint(SENTENCE_LENGTH_MIN, SENTENCE_LENGTH_MAX)
    for i in range(0, sentence_length):
        rnd = random.randint(0, len(BASE) - 1)
        result += BASE[rnd] + " "
    return result

def generate_camel_ipsum():
    result = STARTS_WITH
    for i in range(0, int(PLENGTH)):
        if (i < int(PLENGTH) - 1):
            result += get_camel_ipsum() + "\n"
        else:
            result += get_camel_ipsum()
    print(result)
        
print(">> Camel Ipsum Generator")
generate_camel_ipsum()
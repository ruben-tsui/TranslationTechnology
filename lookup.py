#!/usr/bin/env python
# coding: utf-8

from multivec.cython.multivec import BilingualModel, MonolingualModel

corpora = [b"./un16m.bin", b'./un4m.lemma.bin']
corpus = corpora[0]
model = BilingualModel(corpus)
en_model = model.src_model
zh_model = model.trg_model
print(f"Model dimension = {model.dimension}")


def analogy(w1, w2, w3):
    '''
    Solves problems of the type:
    w1 : w2 :: w3 : __
    '''
    closest_words = []
    try:
        w1v = model.src_model.word_vec(w1.encode())
        w2v = model.src_model.word_vec(w2.encode())
        w3v = model.trg_model.word_vec(w3.encode())
        w4v = w3v + (w2v - w1v)
        closest_words = [w.decode() for (w, d) in model.trg_model.closest_to_vec(w4v, n=15)]
        closest_words = [w for w in closest_words if w not in [w1, w2, w3]]
    except:
        pass
    if len(closest_words) == 0:
        print(':-(')
    else:
        print('{} : {} :: {} : {}'.format(w1, w2, w3, closest_words[0]))
        print(closest_words)


def analogy2(w1, w2, w3):
    '''
    Solves problems of the type:
    w1 : w2 :: w3 : __
    '''
    closest_words = []
    try:
        w1v = model.trg_model.word_vec(w1.encode())
        w2v = model.trg_model.word_vec(w2.encode())
        w3v = model.src_model.word_vec(w3.encode())
        w4v = w3v + (w2v - w1v)
        closest_words = [w.decode() for (w, d) in model.src_model.closest_to_vec(w4v, n=15)]
        closest_words = [w for w in closest_words if w not in [w1, w2, w3]]
    except:
        pass
    if len(closest_words) == 0:
        print(':-(')
    else:
        print('{} : {} :: {} : {}'.format(w1, w2, w3, closest_words[0]))
        print(closest_words)


def collocate(w1, w2, w3):
    '''
    Given:
        Chinese base w1 and Chinese collocate w2
    Find:
        candidates for collocate to English base w3
    '''
    closest_words = []
    try:
        w1v = model.trg_model.word_vec(w1.encode())
        w2v = model.trg_model.word_vec(w2.encode())
        w3v = model.src_model.word_vec(w3.encode())
        w4v = w3v + (w2v - w1v)
        closest_words = [w.decode() for (w, d) in model.src_model.closest_to_vec(w4v, n=15)]
        closest_words = [w for w in closest_words if w not in [w1, w2, w3]]
    except:
        pass
    if len(closest_words) == 0:
        print(':-(')
    else:
        print('{} : {} :: {} : {}'.format(w1, w2, w3, closest_words[0]))
        print(closest_words)


def collocate2(w1, w2, w3):
    '''
    Given:
        Chinese base w1 and Chinese collocate w2
    Find:
        candidates for collocate to English base w3
    '''
    closest_words = []
    try:
        w1v = model.src_model.word_vec(w1.encode())
        w2v = model.src_model.word_vec(w2.encode())
        w3v = model.trg_model.word_vec(w3.encode())
        w4v = w3v + (w2v - w1v)
        closest_words = [w.decode() for (w, d) in model.trg_model.closest_to_vec(w4v, n=15)]
        closest_words = [w for w in closest_words if w not in [w1, w2, w3]]
    except:
        pass
    if len(closest_words) == 0:
        print(':-(')
    else:
        print('{} : {} :: {} : {}'.format(w1, w2, w3, closest_words[0]))
        print(closest_words)


def en2zh(txt, n=5):
    retval = []
    for (x,s) in model.trg_closest(txt.encode(), n):
        retval.append(x.decode())
    return retval

def zh2en(txt, n=5):
    retval = []
    for (x,s) in model.src_closest(txt.encode(), n):
        retval.append(x.decode())
    return retval


def enSynonyms(txt, n=5):
    retval = []
    for (x,s) in model.src_model.closest(txt.encode(), n):
        retval.append(x.decode())
    return retval

def zhSynonyms(txt, n=5):
    retval = []
    for (x,s) in model.trg_model.closest(txt.encode(), n):
        retval.append(x.decode())
    return retval


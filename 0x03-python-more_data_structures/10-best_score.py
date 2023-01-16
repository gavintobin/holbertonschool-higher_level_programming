#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        for maxx in a_dictionary:
            maxx = max(a_dictionary, key=lambda x: a_dictionary[x])
        return maxx

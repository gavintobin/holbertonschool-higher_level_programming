#!/usr/bin/python3
def multiple_returns(sentence):
    c, slen = 0, len(sentence)
    if slen == 0:
        c = None
    elif slen > 0:
        c = sentence[0]
        return (slen, c)

#! /usr/bin/python3

import q

class File:
    def write(self, x):
        pass

file = File()

prefix = "prefix"
sep = "sep"
items = ["1", "2", "3"]

file.write(prefix + q(sep or '').join(items))
file.write(q/prefix + (sep or '').join(items))
file.write(q|prefix + (sep or '').join(items))

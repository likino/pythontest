# -*-coding: utf-8-*-
from sys import argv
from os.path import exists

script, from_file, to_file = argv

# 拷贝from_file内容到to_file
open(to_file, 'w').write(open(from_file).read())
#!/usr/bin/python

from argparse import ArgumentParser

def get_args():
	parser = ArgumentParser(description = 'Get Arguments')
	parser.add_argument("-f", "--file", required=True, dest="filename", help="file name to parse", metavar="FILE")
	args = parser.parse_args()
	filename = args.filename
	return filename

def openandreadfile():
	global filename
	bigstring = open(filename)
	stringline = bigstring.readlines()
	bigstring.close()
	return stringline


def findreplaceinit():
	newline = ""
	global stringline
	for stringline in stringline:
		newline = newline + stringline.replace(",", "|")
	return newline

filename = get_args()
stringline = openandreadfile()
newline = findreplaceinit()
print filename
print newline

if __name__ == '__main__':
	get_args()
	openandreadfile()
	findreplaceinit()

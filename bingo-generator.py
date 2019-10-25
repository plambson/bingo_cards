#!/usr/bin/env python

import random

# read in the bingo terms
in_file = open('nightmare_quotes.txt', 'r')
terms = [line.strip() for line in in_file.readlines()]
# terms = filter(lambda x: x != "", terms)
in_file.close()

# XHTML4 Strict, y'all!
head = ("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">\n"
        "<html lang=\"en\">\n<head>\n"
        "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n"
        "<title>Bingo Cards</title>\n"
        "<style type=\"text/css\">\n"
        "\tbody { font-size: 12px; }\n"
        "\ttable { margin: 40px auto; border-spacing: 2px; }\n"
        "\t.newpage { page-break-after:always; }\n"
        "\ttr { height: 60px; }\n"
        "\ttd { text-align: center; border: thin black solid; padding: 10px; width: 85px; }\n"
        "</style>\n</head>\n<body>\n")

header_repeat = ("<h1 align=center>Nightmare Before Christmas Bingo</h1>\n"
                 "<h2 align=center>Westcehster Stake Mega Mutual</h2>\n"
                 "<p align=center>Pay attention to the dialogue in the movie</p>\n"
                 "<p align=center>when you hear a line said mark that square</p>\n"
                 "<p align=center>when you complete a line shout out BINGO</p>")
list_repeat = ("""<ul align=center>\n"""
               "<li align=center>HI</li>\n"
               "<li align=center>Tea</li>\n"
               "<li align=center>Milk</li>\n"
               "</ul>")

# Generates an HTML table representation of the bingo card for terms
def generateTable(terms, pagebreak = True):
    ts = terms[:12] + ["FREE SPACE"] + terms[12:24]
    if pagebreak:
        res = "<table class=\"newpage\">\n"
    else:
        res = "<table>\n"
    for i, term in enumerate(ts):
        if i % 5 == 0:
            res += "\t<tr>\n"
        res += "\t\t<td>" + term + "</td>\n"
        if i % 5 == 4:
            res += "\t</tr>\n"
    res += "</table>\n"
    return res

out_file = open('out.html', 'w')
out_file.write(head)
cards = int(100)
for i in range(cards):
    random.shuffle(terms)
    out_file.write(header_repeat)
    #out_file.write(list_repeat)
    if i != cards - 1:
        out_file.write(generateTable(terms))
    else:
        out_file.write(generateTable(terms, False))

out_file.write("</body></html>")

out_file.close()

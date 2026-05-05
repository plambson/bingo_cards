#!/usr/bin/env python3

import random
import os

def generateTable(terms):
    ts = terms[:12] + ["FREE SPACE"] + terms[12:24]
    res = "<table>\n"
    for i, term in enumerate(ts):
        if i % 5 == 0:
            res += "\t<tr>\n"
        res += "\t\t<td>" + term + "</td>\n"
        if i % 5 == 4:
            res += "\t</tr>\n"
    res += "</table>\n"
    return res

def generate_bingo_cards(infile, outfile='out.html', cards=100):
    with open(infile, 'r') as f:
        terms = [line.strip() for line in f.readlines()]

    list_name = os.path.splitext(os.path.basename(infile))[0]

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

    header_repeat = ("<h1 align=center>Cinco De Mayo Bingo</h1>\n"
                     "<h2 align=center>Amherst Ward Youth Activity</h2>\n"
                     "<p align=center>When you complete a line shout out BINGO</p>")

    out_file = open(outfile, 'w')
    out_file.write(head)
    for i in range(cards):
        random.shuffle(terms)
        div_class = "newpage" if i != cards - 1 else ""
        out_file.write(f'<div class="{div_class}">\n')
        out_file.write(header_repeat)
        out_file.write(generateTable(terms))
        out_file.write(f"<p align=center>{list_name}</p>\n")
        out_file.write("</div>\n")

    out_file.write("</body></html>")
    out_file.close()

generate_bingo_cards('list1.txt', 'list1.html',cards=50)
print('testing')
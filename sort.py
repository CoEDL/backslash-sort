#!/usr/bin/env python3
"""
Copyright Ben Foley 2021

Usage:
python sort.py -k lx -i bilinarra_lex.txt -o bilinarra_lex_output.txt

Uses NLTK to read SFM backslash dictionary data, convert to XML,
then sort on the lx value of the record elements.
Saves the result as a new SFM file.

    <toolbox_data>
        <header>
            <_sh>v3.0  400  Rotokas Dictionary</_sh>
            <_DateStampHasFourDigitYear/>
        </header>

        <record>
            <lx>kaa</lx>
            <ps>V.A</ps>
            <ge>gag</ge>
            <gp>nek i pas</gp>
        </record>
        ...

TODO: sort by custom alphabet

Gurindji
a, i, j, k, l, m, n, ng, ny, p, r, rl, rn, rt, rr, t, u, y

Bilinarra
a, b, d, g, i, j, l, m, n, ng, ny, r, rd, rl, rn, rr, u, y

Mudburra
a, b, d, i, j, k, l, m, n, ng, ny, r, rd, rl, rn, rr, u, y

"""

import argparse
from nltk import toolbox
from xml.etree.ElementTree import Element, tostring


def get_key(node):
    # print(node[0].tag, node[0].text)
    return node[0].text


def save_lexicon(lexicon, records, output_filename):
    new_lexicon = Element("toolbox_data")
    # Add the old header
    new_lexicon.insert(0, lexicon[0])
    # Num records is used to ensure records are always inserted after the previous one
    num_records = len(lexicon.findall('record'))
    for record in records:
        new_lexicon.insert(num_records, record)
    # Save the new data to a file in standard format marker mode
    with open(output_filename, 'w', encoding='utf-8') as sfm:
        sfm.write(toolbox.to_sfm_string(new_lexicon))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-k", "--key", help='backslash code for key (lx)', default='lx')
    ap.add_argument("-i", "--input_filename", help='input filename, include path', default='input.txt')
    ap.add_argument("-o", "--output_filename", help='Output filename, exclude path', default='output.txt')
    opts = ap.parse_args()

    # Get dictionary data using nltk's toolbox parser (to save writing our own parser)
    lexicon = toolbox.ToolboxData(opts.input_filename, 'utf8').parse(key=opts.key)

    # Sort the records based on the child lx text
    records = sorted(lexicon.findall('record'), key=lambda child: get_key(child))

    # Build a new XML file and convert to SFM using NLTK
    save_lexicon(lexicon=lexicon, records=records, output_filename=opts.output_filename)
    print("done")

#!/usr/bin/env python3
"""
Copyright Ben Foley 2021

Usage:
python sort.py -a alphabet.txt s-i bilinarra_lex.txt -o bilinarra_lex_output.txt -d True -k lx

This script uses NLTK to read SFM backslash dictionary data (converts to XML format),
sorts on the lx value of the record elements,
and saves the result as a new SFM file.

Can sort on a custom alphabet specified in comma-sep format from an external text file, eg:
a, i, j, k, l, m, n, ng, ny, p, r, rl, rn, rt, rr, t, u, y

Note that the alphabet file must include all letters that appear in the headwords.

The input lexicon should be in standard toolbox-style format, eg:
\lx anyan
\ge cute

\lx bada
\ge ground

The XML format NLTK uses is like this:
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
"""

import argparse
from nltk import toolbox
from xml.etree.ElementTree import Element, tostring


def get_key(node, ignore_dashes):
    """
    Get the text of a backslash entry from the first node.
    Strip off leading hyphens if sorting should ignore hyphens.
    Return the cleaned text.
    """
    if ignore_dashes is True:
        return node[0].text.lower().replace('-', '')
    else:
        return node[0].text.lower()


def save_lexicon(old_lexicon, new_records, output_filename):
    """
    Build a new standard format marker (SFM) file using the header from the input file,
    and the newly sorted records.
    Saves to file
    """
    new_lexicon = Element("toolbox_data")
    # Add the old header
    new_lexicon.insert(0, old_lexicon[0])
    # Num records is used to ensure records are always inserted after the previous one
    num_records = len(old_lexicon.findall('record'))
    for record in new_records:
        new_lexicon.insert(num_records, record)
    # Save the new data to a file in standard format marker mode
    with open(output_filename, 'w', encoding='utf-8') as sfm:
        sfm.write(toolbox.to_sfm_string(new_lexicon))
    print("Saved sorted file as", output_filename)


if __name__ == '__main__':
    # Get script arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-a", "--alphabet_filename", help='Filename of alphabet for sorting', default='gurindji_alphabet.txt')
    ap.add_argument("-i", "--input_filename", help='Input filename', default='gurindji_lex.txt')
    ap.add_argument("-o", "--output_filename", help='Output filename', default='gurindji_output.txt')
    ap.add_argument("-d", "--ignore_dashes", help='Does sort ignore hyphens?', default=True)
    ap.add_argument("-k", "--key", help='Backslash code for headword', default='lx')
    opts = ap.parse_args()

    # Get dictionary data using nltk's toolbox parser (to save writing our own parser)
    print("Getting lexicon from", opts.input_filename)
    lexicon = toolbox.ToolboxData(opts.input_filename, 'utf8').parse(key=opts.key)

    # Get the alphabet that we are sorting by
    print("Using alphabet from", opts.alphabet_filename)
    with open(opts.alphabet_filename, 'r', encoding='utf-8') as alphabet_file:
        alphabet_raw = alphabet_file.read()

    # Sort the records using custom alphabet
    alphabet = [x.strip() for x in alphabet_raw.split(',')]
    # Include hyphen even if we aren't sorting on hyphen as a character,
    # otherwise sorted will fail later on.
    alphabet.extend(['-', '.', ' '])

    # Get the record elements that are in the parsed data
    records = lexicon.findall('record')
    print(f"Found {len(records)} records")
    # Make a dict like {a:0, b:1, c:2} from the alphabet list for the sort ordering
    order = {letter: index for index, letter in enumerate(alphabet)}
    # Do the sorting
    print("Sorting...")
    records_sorted = sorted(records, key=lambda child: [order[c] for c in get_key(child, opts.ignore_dashes)])

    # Build a new XML file and convert to SFM using NLTK
    save_lexicon(old_lexicon=lexicon, new_records=records_sorted, output_filename=opts.output_filename)
    print("Done")

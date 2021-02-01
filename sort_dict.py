# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:37:28 2020

@author: WL
"""

import pandas as pd
import re


def sort_dict(input_filename, output_filename):
        
    # specify the file directory, dict files
    # read text dic in
    f = open(input_filename, 'r', encoding="utf-8")
    lines = f.readlines() 
    f.close()
    
    line = ''.join(lines)
    line_reg = re.sub(r'\n\\', r'#\\', line)  # replace new line with #
    reg_split = line_reg.split('\n')
    reg_split = list(filter(lambda x: not re.match(r'^\s*$', x), reg_split))  # del empty lines
    
    # add # at the start of each line
    for idx, content in enumerate(reg_split):
       reg_split[idx] = re.sub(r'^[\s#]*\\lx', r'#\\lx', content)
    
    mark_dash = [0]*len(reg_split)
    for idx, content in enumerate(reg_split):
        print(len(content))

        if content[5] == '-':
            mark_dash[idx] = 1  # mark '-' sign line
            reg_split[idx] = content[0:5] + content[6:]  # delete '-' sign for later sorting
    
    wd=[0]*len(reg_split)
    for idx, content in enumerate(reg_split):
        wd_match = re.match(r'(#\\lx) .+(#\\)',content)
        if wd_match is not None:
            wd[idx] = wd_match[0][5:25]
        
    tab = pd.DataFrame.from_dict(list(zip(reg_split,mark_dash,wd)))
    tab.columns = ['content','dash_mark','wd']
    tab["wd.lower"] = tab["wd"].str.lower()
    tab = tab.sort_values(by="wd.lower")
    tab = tab.reset_index(drop=True)
    x = []
    tab["new_content"] = tab["content"]
    for index, row in tab.iterrows():
        if row.dash_mark == 1:
            # x[index]=row.content[0:5]+'-'+row.content[5:]
            x.append(row.content[0:5] + '-' + row.content[5:])
        else:
            x.append(row.content)
    for idx, content in enumerate(x):
        x[idx] = re.sub(r'#\\lx', r'\n\\lx', content)  # replace new line with #
    for idx, content in enumerate(x):
        x[idx] = re.sub(r'#\\', r'\n\\', content)
    # export file
    with open(output_filename, 'w', encoding="utf-8") as f:
        for item in x:
            f.write("%s\n" % item)
    f.close()


if __name__ == '__main__':
    import argparse 
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input_filename", help='Input filename, include path', default='input.txt')
    ap.add_argument("-o", "--output_filename", help='Output filename, exclude path', default='output.txt')
    opts = ap.parse_args()
       
    sort_dict(input_filename=opts.input_filename, output_filename=opts.output_filename)



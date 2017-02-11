#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# requires https://pypi.python.org/pypi/PyContracts

import logging
import argparse
import os
import shutil
from collections import defaultdict
import re

import clones
import sourcemarkers


logging.basicConfig(filename='nearduplicates2html.log', level=logging.INFO)
logger = logging

def initargs():
    global args
    argpar = argparse.ArgumentParser()
    argpar.add_argument("-sx", "--source-xml", help="Source XML")
    argpar.add_argument("-od", "--output-directory", help="Report output directory")
    argpar.add_argument("-oui", "--only-ui",
                        help="Only generate data needed by standalone [Qt] UI", default="no")
    args = argpar.parse_args()


_wre = re.compile("\w+", re.UNICODE)

def words(text):
    return " ".join(_wre.findall(text))

def extract_near_duplicates(src, logger):
    intervals = sourcemarkers.find_marked_intervals(src)
    id2clones = defaultdict(lambda: [])

    for ob, ce, mt in intervals:
        if mt == 'ACCEPT':
            oe = ob + sourcemarkers.markerlen
            cb = ce - sourcemarkers.markerlen
            mi = sourcemarkers.open_marker_id(src[ob:ob + sourcemarkers.markerlen])
            id2clones[mi].append((oe, cb))

    cnt = 0
    fgrps = []
    for ndi in id2clones.keys():
        cnt += 1
        fclns = []
        fclntexts = []
        fclnwords = []

        intervals = id2clones[ndi]
        for b, e in intervals:
            fclns.append((0, b, e))
            fclntexts.append(src[b:e])
            fclnwords.append(words(src[b:e]))
        fgrps.append(clones.FuzzyCloneGroup(str(cnt), fclns, fclntexts, fclnwords))

    return fgrps


def loadfuzzyinputs(logger):
    global args

    # default required settings for fuzzy groups
    clones.write_reformatted_sources = False
    clones.checkmarkup = False
    clones.only_generate_for_ui = args.only_ui == "yes"

    inputfile = clones.InputFile(args.source_xml)
    with open(args.source_xml + ".reformatted", "w", encoding='utf-8') as rf:
        rf.write(inputfile.text)

    fgrps = extract_near_duplicates(inputfile.text, logger)

    clones.initdata([inputfile], fgrps)

def report(logger):
    global args
    import clones

    fuzzygroups = [clones.VariativeElement([cg]) for cg in clones.clonegroups]
    cohtml = clones.VariativeElement.summaryhtml(fuzzygroups, clones.ReportMode.fuzzyclones)

    outdir = args.output_directory
    with open(os.path.join(outdir, "pyvarelements.html"), 'w', encoding='utf-8') as htmlfile:
        htmlfile.write(cohtml)

    shutil.copyfile(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'js', 'interactivity.js'),
        os.path.join(outdir, "interactivity.js")
    )
    shutil.copyfile(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'js', 'jquery-2.0.3.min.js'),
        os.path.join(outdir, "jquery-2.0.3.min.js")
    )

if __name__ == '__main__':
    initargs()
    loadfuzzyinputs(logger)
    report(logger)

---
layout: default
title: Duplicate Finder
description: Duplicate finder is a tool for discovering and tracking near and exact duplicates in documents
---

Duplicate Finder
================

Duplicate finder is a tool for discovering and tracking near and exact duplicates in documents.
This tool is a part of [DocLine project](http://www.math.spbu.ru/user/kromanovsky/docline/index_en.html).

Quick Guide
-----------

### Reuse Map (Re)Generation and Pattern Search

If you have a software document for duplicate search you should convert it to plain text
and wrap into two XML tags before (see [Examples](#examples)). For many document formats
you can do this using [Pandoc](http://pandoc.org/) utility and `wrap-into-xml.py` Python
script which is located in the [tool source code](#source-code) folder.
See example command line (both Windows and UNiX) below:

    pandoc -t plain MyDocument.docx | python wrap-into-xml.py >MyDocument.pxml

After that you can launch Duplicate Finder using its `duplicate-finder.py` startup script.
You can select input document file (`MyDocument.pxml` above) and adjust following options:

* minimal and maximal duplicate size (in tokens) the tool should consider;
* minimal duplicate number the tool should consider.

Roughly speaking, *token* stands wor a word here.

Then you can get a visualized document reuse map in the browser (brief reuse map in the right panel and
source document in the left panel). After clicking right panel, left one scrolls to the corresponding place in the source.
Places colored with more saturated red color repeat more times in the document and are more interesting.

Then you can select interesting text fragment with mouse, hit any key and confirm searching for it.
This text fragment is a search pattern.

Next step will search near duplicates from the document  which correspond to search pattern selected.
Searching can take some time on large fragments and documents. When it is complete, duplicate browser is launched.
With this browser, you can select duplicates found, correct their boundaries and mark them as useful
or useless ones for future analysis and then save source document with duplicates marked. To mark fragments usable or
useless and to save source document, source document context menu is used.

When running the tool next time, known duplicates will not affect reuse map, so reuse map will get cleaner and cleaner.

### Duplicate Report

Using a checkbox, you can select to display already marked duplicates
instead of building reuse map, and then export report with *File* menu if needed.

Source Code
===========

Source code is available in [Git repository](https://github.com/spbu-se/duplicate-finder),
under the [`tool`](https://github.com/spbu-se/duplicate-finder/tree/master/tool) subfolder.

Examples
========

Here are examples of open source projects documentation available. Reuse maps and duplicate lists are created using Duplicate Finder toolkit.

| Project         | Document      | Source (plain text)                                    | Clean reuse map                                                            | Reuse map with duplicates marked                                            | (Near) Duplicates                                        |
|-----------------|---------------|--------------------------------------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------|
| [GIMP](https://gimp.org/)            | User Manual   | [Download, 1574K](GIMP/user_guide.pxml)        | [Browse](GIMP/clean-heat-map/densitybrowser.html){:target="_blank"}       | [Browse](GIMP/marked-heat-map/densitybrowser.html){:target="_blank"}       | [Browse 17 groups](GIMP/near_dups.html){:target="_blank"}       |
| [Python Requests](http://python-requests.org/) | API Reference | [Download, 36K](PyRequests/api_reference.pxml) | [Browse](PyRequests/clean-heat-map/densitybrowser.html){:target="_blank"} | [Browse](PyRequests/marked-heat-map/densitybrowser.html){:target="_blank"} | [Browse 11 groups](PyRequests/near_dups.html){:target="_blank"} |

System Requirements
===================

Python
------

* [Python 3.4.x](https://www.python.org/downloads/release/python-344/)
* [PyQt5 5.5.x](https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.5.1/)
* [LXML](https://pypi.python.org/pypi/lxml/3.6.0)
* PyContracts, pygments, NumPy, intervaltree, bottle — `pip install PyContracts pygments NumPy intervaltree bottle`

Package versions -- most recent ones compatible with Python 3.4.

*Note: newer PyQt and Python can also be used in case your distribution contains `QtWebkit` as in PyQt 5.5.x*

Operating System
----------------

* `x86` or `x86_64` architecture PC to run Clone Miner, Windows or UN*X
* on UN*Xes:
    * [Wine](https://www.winehq.org/)


Recent publications
===================

1. D. V. Luciv, D. V. Koznov, H. A. Basit, A. N. Terekhov. [On Fuzzy Repetitions Detection in Documentation Reuse](http://www.math.spbu.ru/user/kromanovsky/docline/pdf/luciv.koznov.basit.terekhov_2016_en.pdf). In Programming and Computer Software, 2016, Vol. 42, No. 4, pp. 216–224.
2. D. Koznov, D. Luciv, H. Basit, O. Lieh, M. Smirnov. [Clone Detection in Reuse of Software Technical Documentation](http://www.math.spbu.ru/user/kromanovsky/docline/pdf/koznov.luciv.basit.lieh.smirnov_2016.pdf). In Lecture Notes in Computer Science, Vol. 9609, 2016, pp. 170-185 (10th International Andrei Ershov Informatics Conference on Perspectives of System Informatics, PSI 2015)

License
=======

Sources with PyQt mentioned are licensed under GPL v3.
Documentation in tests folder is licensed under the terms of its initial sources licenses.
Everything other is licensed under LGPL v3.

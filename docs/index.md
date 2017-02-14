---
layout: default
title: Duplicate Finder
description: Duplicate finder is a tool for discovering and tracking near and exact duplicates in documents
---

Duplicate Finder
================

Duplicate finder is a tool for discovering and tracking near and exact duplicates in documents.
This tool is part of [DocLine project](http://www.math.spbu.ru/user/kromanovsky/docline/index_en.html).

Quick Guide
-----------

### Reuse Map (Re)Generation and Pattern Search

You can choose:

* arbitrary XML (HTML, DocBook) or plain text document to analyze;
* minimal and maximal repetition sizes (in words) the tool should consider;
* minimal repetiotion number the tool should consider.

Then you can get a visualized document reuse map in the browser (brief heat map in the right panel and
source document in the left panel). After clicking right panel, left one scrolls to the corresponding place in the source.
Places colored with more saturated red color repeat more times in the document and are more interesting.

Then you can select interesting text fragment with mouse, hit any key and confirm searching for it.

Searching can take some time on large fragments and documents. When it is complete, repetition browser is shown. With
this browser, you can select instances found in document source text, correct their boundaries and mark them as useful
or useless ones for future analysis and then save source document with repetitions marked. To mark fragments usable or
useless and to save source document, source document context menu is used.

When running the tool next time, known repetitions will not affect heat map, so heat map will get cleaner and cleaner.

### Duplicate Report

Using a checkbox, you can select to display already marked duplicates
instead of building heat map, and then export report with File menu if needed.

Source Code
===========

Source code is available in [Git repository](https://github.com/spbu-se/duplicate-finder),
under the [`tool`](https://github.com/spbu-se/duplicate-finder/tree/master/tool) subfolder.

Examples
========

Here are examples of open source projects documentation available. Heat maps and duplicate lists are created using Duplicate Finder toolkit.

| Project         | Document      | Source (plain text)                                    | Clean heat map                                                            | Heat map with duplicates marked                                            | (Near) Duplicates                                        |
|-----------------|---------------|--------------------------------------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------|
| GIMP            | User Manual   | [1574K](GIMP/user_guide.pxml){:target="_blank"}        | [Browse](GIMP/clean-heat-map/densitybrowser.html){:target="_blank"}       | [Browse](GIMP/marked-heat-map/densitybrowser.html){:target="_blank"}       | [17 groups](GIMP/near_dups.html){:target="_blank"}       |
| Python Requests | API Reference | [36K](PyRequests/api_reference.pxml){:target="_blank"} | [Browse](PyRequests/clean-heat-map/densitybrowser.html){:target="_blank"} | [Browse](PyRequests/marked-heat-map/densitybrowser.html){:target="_blank"} | [11 groups](PyRequests/near_dups.html){:target="_blank"} |

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

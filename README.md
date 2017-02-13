Duplicate Finder
================

Duplicate finder is a tool allowing finding and tracking inexact (fuzzy) repetitions in documents.

Quick Guide
-----------

User can choose:

* arbitrary XML (HTML, DocBook) or plain text document to analyze;
* minimal and maximal repetition sizes (in words) the tool should consiider.

Then (s)he can get a visualized document repetition heat map in the browser (brief map in right panel and
source document in left panel). After clicking right panel, left one scrolls to the corresponding place in the source.
Places colored with ьore saturated color repeat more times in the document and are more interesting.

Then user can select interesting text fragment with mouse, hit any key and confirm searching for it.

Searching can take some time on large fragments and documents. When it is complete, repetition browser is shown. With
this browser, user can select instances found in document source text, correct their boundaries and mark them as useful
or useless ones for future analysis. Then (s)he can save document with repetitions marked.

When running the tool next time, known repetitions will not affect heat map, so heat map will get cleaner and cleaner.

Examples
========

| Project | Document    | Source (plain text) | Clean heat map | Heat map with duplicates marked | (Near) Duplicates |
|---------|-------------|---------------------|----------------|---------------------------------|-------------------|
| GIMP    | User Manual | >>                    >>               >>                                >>

System Requirements
===================

Python
------

* [Python 3.4.x](https://www.python.org/downloads/release/python-344/)
* [PyQt5 5.5.x](https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.5.1/)
* [LXML](https://pypi.python.org/pypi/lxml/3.6.0)
* PyContracts, pygments, NumPy, intervaltree, bottle — `pip install PyContracts pygments NumPy intervaltree bottle`

Package versions -- most recent ones compatible with Python 3.4

Operating System
----------------

* `x86` or `x86_64` architecture PC to run Clone Miner, Windows or UN*X
* on UN*Xes:
    * [Wine](https://www.winehq.org/)

GTranslate
==========

GTranslate is a quick interface to translation tools.
In particular it was made to interface a specific tool
from Weboob (http://www.weboob.org). Weboob is a collection
of applications able to interact with websites without a
browser and mostly with command line interfaces. This allows
GTranslate to use web translation services such as Google-Translate.
However it can also be used with others translation tools as long
as they offer a simple command-line way to translate a text from
one language to another. It can also be easily adapted to any
tool to provide an interactive conversion from one type to another.

Requirements
------------

- Python 2.6
- PyGTK2
- GTK-3

- Weboob (optional)

Installation
------------

Simply run:

> sudo python setup.py install

If the translaboob command from weboob is configured then it should work out of the box.
Otherwise you could either change the wrapper script in /usr/local/lib/sh/translate.sh or
change the translation tool with the --translate option or TRANSLATE_TOOL environnement variable.


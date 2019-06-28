Usage
=====

This project currently has two main parts:

1. Command-line tool :code:`app.py`
2. Command-line tool :code:`utils.py`

Their usage details are described below.

:code:`app.py`
++++++++++++++

:code:`app.py` is the main tool that provides an interface to each vowel-harmony pattern's
FST you can use to generate output words in those VH patterns.

Once you run :code:`python3 app.py`, it presents a list of all the VH patterns
recorded and functional so far, and you can select your desired one by its number.

After selecting a VH pattern to run, you will be provided with another interface
that accepts words in the chosen VH pattern that you want to get the IPA representation
for. The tool at this point takes space-delimited words as inputs.

For example, if you have a word :code:`tilarobila` where :code:`til-` is the prefix,
:code:`arob` is the stem, and `-ila` is the suffix, you can input this word as
:code:`t i l + a r o b - i l a`. Internally, the tool looks for :code:`+` and :code:`-`
in the word and divides prefixes and suffixes as described. After that, it runs the
required part through the FST, and combines all the parts of the word before showing you
the finalized output word.

You can also enter a word with its characters represented as unicode variables, as
per the instructions pointed at :doc:`unicodevars`. For example, you can express
'tsomilɑ' as 't s o m i l B_L_U_NT' where B_L_U_NT stands for the IPA symbol ɑ,
the Back, Low, Unrounded, lax (Not Tense) vowel.

You can use the command :code:`--help` inside any VH pattern tool to get a generic
help interface. This help interface shows you how to input a word as described in the
instructions here, and also gives you the ability to check the :doc:`unicodevars` that
you can use to construct a word.

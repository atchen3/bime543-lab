"""
main.py

.. module:: Main
   :synopsis: Main module. Calls the code to perform the text processing functions for preparing the data.

.. moduleauthor:: Annie T. Chen (atchen@uw.edu)

You can use a pound sign (#) to comment out any section you don't need.

For example, if you only want to prepare an extract for Atlas.ti, the code below might look like this:

#creates FileProcessor instance
FP = FileProcessor("diabetes.csv")

#prepares input file for Metamap
#FP.PrepMetamap("diabetes.txt")

#prepares input file for Atlas.ti
FP.ExtractConstruct("insulin")

#constructs dataset based on symptoms extracted using the Diabetes Mellitus Treatment Ontology (DMTO)
#FP.ExtractSymptoms()

"""
from processing import FileProcessor

#creates FileProcessor instance -- enter the source filename.
FP = FileProcessor("diabetes.csv")

#prepares input file for Metamap -- enter the desired filename.
FP.PrepMetamap("diabetes.txt")

#prepares input file for Atlas.ti -- enter the keyword that you want to filter on.
FP.ExtractConstruct("insulin")

#constructs dataset based on symptoms extracted using the Diabetes Mellitus Treatment Ontology (DMTO)
FP.ExtractSymptoms()


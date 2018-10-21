### BIME 543 Consumer Health and Informatics Lab Activities Supporting Code ###

This module provides supporting code for the BIME 543 lab activities assignment.  The code takes the data
found in the /data directory and subsets it for subsequent analysis in MetaMap, Atlas.ti, or some other
application.  The subsets are exported into the data directory for review.

Methods for subsetting include:

1. keyword extraction (ExtractConstruct)
2. extraction of symptoms based on the Diabetes Mellitus Treatment Ontology (ExtractSymptoms)

Developed using Python version 3.6.

### Datasets ###

Includes three datasets: 23andme.csv, ChineseMedicine.csv, and diabetes.csv, based on the subreddits of
the same names.

### Derivative Files ###

This code creates the following derivative files:

MetaMap input files: [sometopic].txt (where sometopic = ChineseMedicine.txt, diabetes.txt, 23andme.txt)
Atlas.ti input file: insulin.txt
Symptoms extract files: DiabetesSymptoms.txt

### Instructions for Use ###

1. Edit directory names as needed in "config.py".
2. Edit the code as needed in "main.py". (See instructions in "main.py" on how to do this.)
3. Run "main.py".

### Dependencies ###

Dependencies: pandas, csv, pronto

### Other ###

This code uses the Diabetes Mellitus Diagnosis Ontology, which is available at:
http://bioportal.bioontology.org//ontologies/DDO

### Contact ###

Contact: Annie T. Chen (atchen@uw.edu)


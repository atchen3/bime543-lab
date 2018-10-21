"""
processing.py

.. module:: FileProcessor
   :synopsis: Module that contains text processing functions to prepare the Reddit dataset.

.. moduleauthor:: Annie T. Chen (atchen@uw.edu)

"""
import config

class FileProcessor(object):

    def __init__(self, datafile):
        """
        Constructor.

        :param datafile: file containing the original data
        """
        import pandas as pd

        #ingest files
        self.data = pd.read_csv(config.datadir + datafile, low_memory=False)

        #processes the text of the Reddit comment to remove carriage returns and end-of-line characters so that
        #the data is processed correctly in subsequent steps
        self.data["body"] = self.data["body"].apply(lambda x: str(x).replace("\r\n"," ").replace("\r"," ").replace("\n"," ").\
                                          replace("\t"," "))

    def PrepMetamap(self, destfile):
        """
        Extracts Reddit comments, one per line, for use with the batch version of Metamap.

        :param destfile: name of the destination file
        :return: data
        """
        import csv
        destfile = config.datadir + destfile

        #subset the data to include only the text of the comments
        data = self.data
        data = data[["body"]]

        #export to a file for analysis using Metamap
        data.to_csv(destfile, index=False, header=False, sep='\t', quoting=csv.QUOTE_NONE)

        return data

    def ExtractConstruct(self, construct):
        """
        Extracts Reddit comments relating to a given construct for analysis in Atlas.ti.
        Inserts a carriage return between each comment for readability.

        :param construct: construct of interest
        :return: data
        """
        import csv

        data = self.data[["body","author"]].copy()

        #add brackets around the author
        data["author"] = data["author"].apply(lambda x: "[" + str(x) + "]")

        #subset based on supplied keyword
        data = data[data['body'].str.contains(construct)]

        #output the text, along with author information, into a file
        #adds an extra end-of-line character for readability
        data.to_csv(config.datadir + construct + '.txt', index=False, header=False, sep='\t', line_terminator='\n\n', \
                    quoting=csv.QUOTE_NONE)

        return data

    def ExtractSymptoms(self):
        """
        Extracts Reddit comments that contain diabetes symptoms, based on the diabetes symptoms class
        (DDO:0006288) in the Diabetes Mellitus Treatment Ontology (DMTO).

        :return:
        """
        import pronto
        import pandas as pd

        #create a pronto ontology instance based on the ontology we're using
        onto = pronto.Ontology(config.ontodir + config.diabetesontofile)

        #class of interest in the ontology
        focus = 'DDO:0006288'

        #create an empty dataframe
        master = pd.DataFrame()

        #loop through the terms in the ontology
        for term in onto:

            #if the term is a diabetes symptom, then extract any Reddit comments containing it
            if term in onto[focus].children:
                subset = self.data[self.data['body'].str.contains(term.name)].copy()
                subset['term'] = term.name
                master = master.append(subset)


        #keep only the data fields that we plan to include in the destination file
        master = master[["term","body"]]

        #export to destination file
        master.to_csv(config.datadir + 'DiabetesSymptoms.txt', index=False, header=False, sep='\t')


import os
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud


class FileMetaData:
    '''
    Class to contain meta data on the files. To restrict the amount of data the program has to search 
    through there is a bit of redundency here. This allow filtering by tag to be done easier. Probably
    reinventing the wheel a little. Maybe I will implement a proper database system later. 
    '''
    def __init__(self, DirectoryPath):
        self.FileList = []
        self.Tags = []
        self.TagLoc = []
        self.TagFreq = []
        i = 0
        for (dirpath, dirnames, filenames) in os.walk(DirectoryPath):
            for file in filenames:
                TagTemp = file.split('.')[0] # we trim the file extension
                TagTemp = TagTemp.split('#')[1:] # extract the tags from the files 
                
                self.FileList.append( # we store the complete information in a dictionary
                    {
                        'dirpath' : dirpath,
                        'FileName' : file,
                        'tags' : TagTemp,
                    }
                )

                for tag in TagTemp:
                    # looks to see if  tag has been encountered before and handles it accordingly
                    if tag in self.Tags:
                        loc = self.Tags.index(tag)
                        self.TagLoc[loc].append(i)
                        self.TagFreq[loc] += 1
                    else:
                        self.Tags.append(tag)
                        self.TagLoc.append([i])
                        self.TagFreq.append(1)
                i += 1

    def filter(self, mytags):
        '''
        These if statements are not so elegant but anyway
        '''

        notags = len(mytags)
        # at some point I will support more sophisticated tag logic but for now it is just AND
        
        if notags == 0: 
            self.FilterIDs = range(len(self.FileList))
        else :
            self.FilterIDs = set(self.TagLoc[ self.Tags.index(mytags[0])])
            if notags > 1:
                for tag in mytags[1:]:
                    FilterIDsTemp = set(self.TagLoc[ self.Tags.index(tag) ])
                    self.FilterIDS = FilterIDs & FilterIDsTemp

        # takes a list of tags and find the  asociated files
        self.FilteredFiles = []
        for ID in list(self.FilterIDs):
            File = self.FileList[ID]
            #FilteredFiles.append(os.path.join(File['dirpath'], File['FileName']))
            self.FilteredFiles.append(File) 
            
        return sorted([File['FileName'] for File in self.FilteredFiles]) 
    
    def PlotTagCloud(self):
        #freq = [len(item) for item in self.TagLoc] 
        words = ''
        for Locs, Tag in zip(self.TagLoc, self.Tags):
            for i in range(len(Locs)):
                words = words + ' ' + Tag 

        wordcloud = WordCloud(width = 800, height = 800, 
                        #background_color ='white', 
                        min_font_size = 10).generate(words)
        
        #plt.figure()
        plt.imshow(wordcloud)
        plt.show()
        #plt.show(block=False) 



        
         







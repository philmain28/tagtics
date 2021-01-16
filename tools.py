import os

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
                
                self.FileList.append( # we store the complete information in a directory
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
            FilterIDs = range(len(self.FileList))
        else :
            FilterIDs = set(self.TagLoc[ self.Tags.index(mytags[0])])
            if notags > 1:
                for tag in mytags[1:]:
                    FilterIDsTemp = set(self.TagLoc[ self.Tags.index(tag) ])
                    FilterIDS = FilterIDs & FilterIDsTemp

        # takes a list of tags and find the  asociated files
        FilteredFiles = []
        for ID in list(FilterIDs):
            File = self.FileList[ID]
            #FilteredFiles.append(os.path.join(File['dirpath'], File['FileName']))
            FilteredFiles.append(File['FileName']) 
            
            
        return sorted(FilteredFiles)
            







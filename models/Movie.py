class Movie:
    def __init__(self, title, year, summary, runtime, rating):
        self.__title = title
        self.__year = year
        self.__summary = summary
        self.__runtime = runtime
        self.__rating = rating

    def getTitle(self):
        return self.__title
    
    def getYear(self):
        return self.__year
    
    def getSummary(self):
        return self.__summary
    
    def getRuntime(self):
        return self.__runtime
    
    def getRating(self):
        return self.__rating
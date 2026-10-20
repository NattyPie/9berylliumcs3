class PublicationInformation:
  def __init__(self, PItitle, PIauthor):
    self.title = PItitle
    self.author = PIauthor  
  def display_info(self):
        print("\nPublic Information")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

    
class BookInformation:
    def __init__(self, BItitle, BIauthor, pageno):
        self.title = BItitle
        self.author = BIauthor
        self._pages = pageno

    def getPages(self):
      return self.pages
  
    def setPages(self, pageno):
      if pageno < 0:
          print("Number of pages must be positive")
      else:
        self.__pages = pageno
    def display_info(self):
      print("\nBook Information:")
      print(f"Title: {self.title}")
      print(f"Author: {self.author}")
      print(f"Number of pages: {self._pages}")
    
class MagazineInformation:
    def __init__(self, MItitle, MIauthor, MIissuenumber):
        self.title = MItitle
        self.author = MIauthor
        self._issuenumber = MIissuenumber 
    def display_info(self):
        print("\nMagazine Information:")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Issue number: {self._issuenumber}")
        
#sample objects

pub1 = PublicationInformation("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = BookInformation("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = MagazineInformation("National Geographic", "Various Authors", 202)

#Printing the information
print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.setPages(-310) #setting invalid value on attribute
book1.display_info()
print(book1.getPages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.getissuenumber())

# Class to represent an Article with attributes for author, magazine, and title
class Article:
# Class variable to store all instances of Article:
    all = []
    
    # Constructor to initialize an Article object
    def __init__(self, author, magazine, title):
        # Attribute to store the author of the article
        self.author = author
        # Attribute to store the magazine iin which the article is published
        self.magazine = magazine
        # Attribute to store the title of the article
        self.title = title
        # Add the article to the list of all instances of Article
        self.__class__.all.append(self)
      
      
# Class to represent an Author with attributes for name
class Author:
    # Class variable to store all instances of Author
    all = []
    
    # Constructor to initialize an Author object
    def __init__(self, name):
        # Check if the name is a string and has a length greater than 0
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        # Attribute to store the name of the author
        self._name = name
        # Add the newly created Author object to the class variable all
        self.__class__.all.append(self)
        
     # Property to get the name of the author
    @property
    def name(self):
        return self._name

    # Method to return all articles written by the author
    def articles(self):
        return [article for article in Article.all if article.author == self]

    # Method to return all magazines in which the author has published articles
    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    # Method to add a new article to the author's list of articles
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    # Method to return all topic areas in which the author has published articles
    def topic_areas(self):
        categories = {article.magazine.category for article in Article.all if article.author == self}
        return list(categories) if categories else None


# Class to represent a Magazine with attributes for name and category
class Magazine:
    # Class variable to store all instances of Magazine
    all = []    
    # Constructor to initialize a Magazine object
    def __init__(self, name, category):
        # Check if the name is a string and has a length between 2 and 16 characters
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
        # Check if the category is a non-empty string
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Magazine category must be a non-empty string.")
        # Attribute to store the name of the magazine
        self._name = name
        # Attribute to store the category of the magazine
        self._category = category
        # Add the newly created Magazine object to the class variable all
        self.__class__.all.append(self)

     # Property to get the name of the magazine
    @property
    def name(self):
        return self._name

    # Property setter to set the name of the magazine
    @name.setter
    def name(self, value):
        # Check if the value is a string and has a length between 2 and 16 characters
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
        # Set the name of the magazine to the new value
        self._name = value

    # Property to get the category of the magazine
    @property
    def category(self):
        return self._category
    
    # Property setter to set the category of the magazine
    @category.setter
    def category(self, value):
        # Check if the value is a non-empty string
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Magazine category must be a non-empty string.")
        # Set the category of the magazine to the new value
        self._category = value
        
    # Method to return all articles published in the magazine
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    # Method to return all authors who have published articles in the magazine
    def contributors(self):
         return list(set(article.author for article in self.articles()))
     
    # Method to return all topic areas in which the magazine has published articles
    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None
    
    # Method to get all the contributing authors of the articles in the magazine
    def contributing_authors(self):
        # Create a dictionary to store the count of articles for each author
        author_article_count = {}
        # Iterate over all articles in the magazine
        for article in self.articles():
            # Get the name of the author of the current article
            author_name = article.author.name
            # Check if the author is already in the dictionary
            # If the author is already in the dictionary, there will be increment in their article count by 1
            if author_name in author_article_count:
                author_article_count[author_name] += 1
                # If the author is not in the dictionary, there will be a new entry with an article count of 1
            else:
                author_article_count[author_name] = 1
                
        # Create a list of authors who have contributed more than 2 articles
        authors = [author for author in self.contributors() if author_article_count[author.name] > 2]
        # Return the list of contributing authors, or None if the list is empty
        return authors if authors else None
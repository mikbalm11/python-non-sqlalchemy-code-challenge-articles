class Article:
    
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.all.append(self)
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise Exception("Author should be an instance of Author.")
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise Exception("Magazine should be an instance of Magazine.")
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if isinstance(value, str) and 5 <= len(value) <= 50 and not hasattr(self, 'title'):
            self._title = value
        else:
            raise Exception("Title should be between 5 and 50 characters.")
        
class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0 and not hasattr(self, 'name'):
            self._name = value
        else:
            raise Exception("Author name should be a non-empty string.")

    def articles(self):
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list({article.magazine.category for article in self.articles()}) or None

class Magazine:
    
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 16 >= len(value) >= 2:
            self._name = value
        else:
            raise Exception("Magazine name should be a non-empty string between 2 to 16 characters.")
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise Exception("Magazine category should be a non-empty string.")

    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        return [article.title for article in self.articles()] or None

    def contributing_authors(self):
        return [author for author in self.contributors() if sum(1 for article in author.articles() if article.magazine is self) > 2] or None

    def total_publishments(self):
        return len(self.articles())

    @classmethod
    def top_publisher(self):
        if self.all:
            mag = max(self.all, key=lambda magazine: magazine.total_publishments())
            if mag.total_publishments() == 0:
                return None
            return mag
        else:
            return None
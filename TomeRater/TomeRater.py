#premiere question : create a book
class User(object):


    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.book = {}

    def get_email(self):
        return self.email

    def change_email(self, address):

        if address != self.email:
            self.email = address
            print("this user’s email has been updated")


    def read_book(book, rating = "None"):
        self.books.update({book : rating})
        return self.books


    def get_average_rating(self):
        total = 0
        for values in self.books:
            total += values
            return total
        average = total / len(total)
        return average


    def __repr__(self):
        return "User %s, email : %s, books read : %s" % (self.name, self.email, self.book)

    def __eq__(self, other_user):
	    if self.name == other_user.name and self.email  == other_user.email:
		    return true
	    return false


#deuxieme question : create a book
class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
    def get_title (self):
        return self.title
    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
	     if self.isbn != new_isbn:
		      self.isbn = new_isbn
		      print ("this book's ISBN has been updated")


    def add_rating(self, ratingToAdd):

	    if type(ratingToAdd) != "<class 'int'>" or ratingToAdd < 0 or ratingToAdd > 4  :
		    print("Invalid Rating")
	    else:

                self.ratings.append(ratingToAdd)


    def get_average_rating (self):
        total1 = 0
        nbr=0
        for values in self.ratings:
          total1 += values
          nbr+=1
        return total1 / nbr


    def __hash__(self):
        return hash(self.title, self.isbn)

    def __eq__(self, other_book):
        if self.title == other_user.title and self.isbn  == other_user.isbn:
          return true
        return false
#troisieme question : Make a Fiction Subclass of Book
class Fiction (Book):
    def __init__(self, title, author, isbn):
        super(Fiction,self).__init__(title,isbn)
        self.author = author

    def get_author (self):
        return self.author

    def __repr__(self):
        return repr("%s by %s") % (self.title, self.author)

#quatrime question = Make a Non-Fiction Subclass of Book

class Non_Fiction (Book):
    def __init__(self, title, subject, level, isbn):
        super(Non_Fiction,self).__init(title, isbn)
        self.subject = subject
        self.level = level
    def get_subject (self):
        return self.subject
    def get_level (self):
        return self.level
    def __repr__(self):
        return repr("%s, a %s manual on %s") % (self.title, self.level, self.subject)

#create Tomerater
class Tomrater:
    def __init__(self):
        self.users = {}
        self.books = {}
    def create_book (self, title, isbn):
        new_book = Book(title , isbn)
        return new_book
    def create_novel (self, title, author, isbn):
        new_Fiction = Fiction(title,author,isbn)
        return new_Fiction
    def create_non_fiction (self, title, subject, level, isbn):
        new_Non_Fiction = Non_Fiction(title,author,isbn)
        return new_Non_Fiction
    def add_book_to_user(book, email, rating = None):
        if self.user[email] not in self.user:
            return print("No user with email %s") % (self.email)
        else:
            read_book(self, book, rating)
            add_rating(self, book, rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books.update(book, 1)
    def add_user(name, email, user_books = None):
        User_ = User(name, email)
        return User
        if user_books != None:
            add_book_to_user(book, email, rating = None)

    def print_catalog(self):
        for keys in self.books:
            print(keys)

    def print_users(self):
        for values in self.users:
            print(values)

    def most_read_book(self):
        max_value = ()
        for values in self.book:
            max_value.append(values)
        return max(max_value)

    def highest_rated_book(self):
        for book in self.books:
            return book.get_average_rating(book)

    def most_positive_user(self):
        for user in self.users:
            return user.get_average_rating(user)

Tome_Rater = Tomrater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
Tome_Rater.print_catalog()
# Tome_Rater.print_users()

# print("Most positive user:")
# print(Tome_Rater.most_positive_user())
# print("Highest rated book:")
# print(Tome_Rater.highest_rated_book())
# print("Most read book:")
# print(Tome_Rater.most_read_book())

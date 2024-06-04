class Author:   

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)
        # self.contracts_list = list()

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return list(set(contract.book for contract in self.contracts()))

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract 
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:

    all = []

    def __init__(self, title):
        self.title = title
        # self.contracts_list = list()

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return list(set(contract.author for contract in self.contracts()))


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception
        self.author = author
        if not isinstance(book, Book):
            raise Exception
        self.book = book
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        self.date = date 
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")
        Contract.all.append(self)
        self.royalties = royalties 
        # self.author.contracts_list.append(self)
        # self.book.contracts_list.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
    

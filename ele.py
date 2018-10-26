class Ele:

    name = ''
    price = ''
    number = ''
    url = ''

    def setName(self, n):
        self.name = n

    def setPrice(self, p):
        self.price = p

    def setUrl(self, u):
        self.url = u
    
    def setNumber(self, num):
        self.number = num;

    def prit(self, fLen, Len):
        print(self.name.ljust(fLen) + self.price.ljust(Len) + self.number.ljust(Len) + self.url.ljust(Len))



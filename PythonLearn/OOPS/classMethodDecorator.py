class Currency:
    def __init__(self, amount):
        self.amount=amount
        
    def __repr__(self):
        return f"Currency class ${self.amount}"

    @classmethod
    def changeCurrency(cls,todayAmount, dollarAmount):
        return cls(todayAmount+dollarAmount)


# class.chagen(10,20)
#class(30) 

#second class here
class YenCurrency(Currency):
    def __init__(self,amount):
        super().__init__(amount)
        self.symbol="¥"

    def __repr__(self):
        return f"Yen class {self.symbol}:{self.amount} "


print( Currency.changeCurrency(200,40))
print( YenCurrency.changeCurrency(200,40))


# y1=YenCurrency(50)
# print(y1)




# print( Currency.changeCurrency(200,80) )



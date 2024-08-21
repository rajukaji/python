#constructor
class PassValue:
    def __init__(self, key): #constructor
        self.key = key
        print(key)
    
value = PassValue(5)
print(value.key)


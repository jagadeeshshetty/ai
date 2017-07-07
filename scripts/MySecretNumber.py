
# subject + verb + object
# The product of the first two digits + is less than + 25

class MySecretNumber():
    def __init__(self):
        pass
        #print("init")  # never prints

    def createRule(self):
        self.subject = 'The product of the first two digits'
        self.verb = 'is less than'
        self.obj = 25

        self.selectedSubject = self.subject
        self.seletedVerb = self.verb
        self.selectedObj = self.obj

        rule = str(self.selectedSubject) + ' ' + str(self.seletedVerb) + ' ' + str(self.selectedObj)
        return rule

    def createNumber(self):
        if 'product'in self.selectedSubject:
            print(True)
        return self.selectedObj


p = MySecretNumber()
print(p.createRule())
print(p.createNumber())

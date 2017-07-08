
# My Secret Number Game.
# subject + verb + object
# The product of the first two digits + is less than + 25


class MySecretNumber:
    def __init__(self):
        self.number = [0, 0, 0]
        pass

    def create_rule(self):
        self.subject = 'The product of the first two digits'
        self.verb = 'is less than'
        self.obj = 25

        self.selected_subject = self.subject
        self.selected_verb = self.verb
        self.selected_obj = self.obj
        return str(self.selected_subject) + ' ' + str(self.selected_verb) + ' ' + str(self.selected_obj)

    def create_number(self):
        if 'first two' and 'product' in self.selected_subject:
            # if 'less' in self.selected_verb:
            #     product_of_first_two_number = self.product( self.number[0],  self.number[1])
            #     for first_digit in range(0, 10):
            #         for second_digit in range(0, 10):
            #             product_of_first_two_number = self.product(self.number[0],  self.number[1])
            #             if product_of_first_two_number < (self.selected_obj-1):
            #                 self.number[0] = first_digit
            #                 self.number[1] = second_digit
            if 'less' in self.selected_verb:
                product_of_first_two_number = self.product( self.number[0],  self.number[1])
                for first_digit in range(0, 10):
                    for second_digit in range(0, 10):
                        product_of_first_two_number = self.product(self.number[0],  self.number[1])
                        print('first_digit' + str(first_digit))
                        print('second_digit' + str(second_digit))
                        if product_of_first_two_number < (self.selected_obj-1):
                            self.number[0] = first_digit
                            self.number[1] = second_digit

        return self.number[0], self.number[1]

    def product(self, num1, num2):
        result = num1 * num2
        print("DEBUG: product of " + str(num1) + ' ' + str(num2) + ' is ' + str(result))
        return result

p = MySecretNumber()
p.create_rule()
print(p.create_number())
print(p.number)

class Calculator:
    def __init__(self):
        self.dic = {}
        self.commands = ['/exit', '/help']
        self.switch = True

    def user_input(self):
        while self.switch:
            user_input = input()
            if user_input.startswith('/'):
                self.command(user_input)
            elif '=' in user_input:
                self.assignment(user_input)
            elif len(user_input.split()) == 1:
                self.variable_check(user_input)
            elif '+' or '-' in user_input:
                self.calculate(user_input)
            elif user_input == '':
                pass

    def variable_check(self, i):
        #TODO: check if variable is in dictionary
        if i.isalpha():
            if i in self.dic:
                print(self.dic[i])
            else:
                print('Unknown Variable')
        else:
            print('Invalid Identifier')

    def assignment(self, i):
        #TODO: assign the variable to instance dictionary
        if i.count('=') != 1:
            print('Invalid Identifier')

        value_list = list(map(lambda x: x.replace(' ', ''), i.split('=')))

        if not value_list[0].isalpha():
            print('Invalid Identifier')
        elif value_list[1].isdigit():
            self.dic[value_list[0]] = value_list[1]
        elif value_list[1] in self.dic:
            self.dic[value_list[0]] = self.dic[value_list[1]]
        elif value_list[1].isalpha() and value_list[1] not in self.dic:
            print('Unknown Variable')
        else:
            print('Invalid assignment')

    def calculate(self, i):
        #TODO: calcualte user expression
        x = i.split()
        y = [str(self.dic[k]) if k in self.dic else k for k in x]

        try:
            print(eval(''.join(y)))
        except SyntaxError:
            print('Invalid expression')

    def command(self, i):
        #TODO: check for user command
        if i not in self.commands:
            print('Unknown command')
        elif i == self.commands[1]:
            print('The program calculates the sum of numbers')
        elif i == self.commands[0]:
            print('Bye!')
            self.switch = False


calculator_object = Calculator()
calculator_object.user_input()

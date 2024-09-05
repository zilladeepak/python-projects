import secrets
import string

class Password:
    def __init__(self, length:int, uppercase:bool, symbol:bool)->None:
        self.length = length
        self.use_uppercase = uppercase
        self.use_symbol = symbol

        #get chars using string module
        self.base_chars :str = string.ascii_lowercase + string.digits

        if self.use_uppercase:
            self.base_chars += string.ascii_uppercase
        if self.use_symbol:
            self.base_chars += string.punctuation
            
    def generate(self) ->str:
        password :list[str] = []
        
        for i in range(self.length):
            password.append(secrets.choice(self.base_chars))
            
        return ''.join(password)

def main() ->None:
    while True:
        n :int =int(input("No of Passwords required : "))
        N :int =int(input("Length of the password : "))
        uppercase :str =input("Need UpperCase letter (y/n) : ")
        symbol :str =input("Need Symbols (y/n) : ")
        uppercase_bool:bool = True if uppercase == 'y' else False
        symbol_bool:bool = True if symbol == 'y' else False
    
        password :Password = Password(N,uppercase_bool,symbol_bool)

        for i in range(n):
            generate = password.generate()
            print(f'{generate} ({len(generate)} chars)')

        restart :str = input("Want to generate again (y/n): ")
        if restart != 'y':
            exit()
                

if __name__ == '__main__':
    main()
    
    

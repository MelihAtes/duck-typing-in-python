class duck:
    def walk(self):
        print("this duck is walking")

    def talk(self):
        print("this duck is quacking")

class chicken:
    def walk(self):
        print("this chicken is walking")

    def talk(self):
        print("this chicken is barking")

class human:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("you caught the critter!")
        
duck = duck()
chicken = chicken()
human = human()

human.catch(chicken)

# duck typing, attributes is more important than object 
# if i delete dog's walk part, then there will be error.
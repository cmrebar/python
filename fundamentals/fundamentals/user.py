class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        import pprint
        pprint.pprint(vars(self))
    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print('User already a member')
    def spend_points(self,amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            print('Not enough points')
        

bob = User('Bob', 'Builder', 'bobdabuilder@gmail.com', '38')
mickey = User('Mickey', 'Mouse', 'mmouse1928@gmail.com', '94')
spongebob = User('Spongebob', 'Squarepants', 'ggoober1999@gmail.com', '50')
bob.enroll()
bob.spend_points(50)
mickey.enroll()
mickey.spend_points(80)
bob.display_info()
mickey.display_info()
spongebob.display_info()
bob.enroll()
spongebob.spend_points(40)

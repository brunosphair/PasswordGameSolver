from web_interact import Web
import random
import string

class Solver:
    def __init__(self):
        self.password = Password()

    def get_initial_password(self):

        initial_password = self.get_random_lowercase_password_len(5)
        index = -1
        self.password.insert_password_in_index(initial_password, index)
        return initial_password
    
    def get_random_lowercase_password_len(self, len):
        characters = string.ascii_lowercase
        random_characters = []
        for _ in range(len):
            random_charact = random.choice(characters)
            random_characters.append(random_charact)
        random_password = ''.join(random_characters)

        return random_password

    def update_password_for_rule_2(self):
        new_password_part = str(random.randint(0, 9))
        index = -1
        new_password_info = self.get_new_password_dict(new_password_part, index)
        self.password.insert_password_in_index(new_password_info['password'], index)

        return new_password_info
    
    def update_password_for_rule_3(self):
        new_password_part = self.get_random_uppercase_charact_not_roman()
        index = -1
        new_password_info = self.get_new_password_dict(new_password_part, index)
        self.password.insert_password_in_index(new_password_info['password'], index)

        return new_password_info
    
    def get_random_uppercase_charact_not_roman(self):
        '''The roman charact can increase difficulty in another rules'''
        roman_charact = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        characteres = string.ascii_uppercase
        while True:
            random_uppercase = random.choice(characteres)
            if random_uppercase not in roman_charact:
                return random_uppercase
    
    def update_password_for_rule_4(self):
        new_password_part = self.get_random_special_charact()
        index = -1
        new_password_info = self.get_new_password_dict(new_password_part, index)
        self.password.insert_password_in_index(new_password_info['password'], index)

        return new_password_info
    
    def get_random_special_charact(self):
        special_characters = ['!', '@', '#', '$', '%', '^', '&', '*']
        random_special_character = random.choice(special_characters)

        return random_special_character
    
    def update_password_for_rule_5(self):
        new_password_dict = self.get_str_to_add_up_25()
        new_password_part = new_password_dict['part']
        index = new_password_dict['index']
        replace = new_password_dict['replace']
        new_password_info = self.get_new_password_dict(new_password_part, index, replace)
        self.password.insert_password_in_index(new_password_info['password'], index, replace=replace)

        return new_password_info
    
    def get_str_to_add_up_25(self):
        current_int_sum_in_password = self.get_current_password_int_sum()
        new_password_dict = {}
        
        if current_int_sum_in_password < 25:
            quantity_to_add = 25 - current_int_sum_in_password
            number_of_nines = quantity_to_add // 9
            other_number = 25 - number_of_nines * 9 - current_int_sum_in_password
            new_password_dict['part'] = number_of_nines * '9' + str(other_number)
            new_password_dict['index'] = -1
        else:
            quantity_to_subtract = current_int_sum_in_password - 25
            
        
        return new_password_dict


    def get_current_password_int_sum(self):
        sum = 0
        for character in self.password.current_password:
            if character.isdigit():
                sum += int(character)
        
        return sum
    
    def update_password_for_rule_6(self):
        new_password_part = self.get_random_month_of_year()
        index = -1
        protected = True
        new_password_info = self.get_new_password_dict(new_password_part, index)
        self.password.insert_password_in_index(new_password_info['password'], index, protected)

        return new_password_info

    def get_random_month_of_year(self):
        months_of_year = ['january', 'february', 'march', 'april', 'may',
                          'june', 'july', 'august', 'september', 'october',
                           'november', 'december']
        random_month_of_year = random.choice(months_of_year)

        return random_month_of_year
    
    def update_password_for_rule_7(self):
        new_password_part = 'XXXV'
        index = -1
        protected = True
        new_password_info = self.get_new_password_dict(new_password_part, index)
        self.password.insert_password_in_index(new_password_info['password'], index, protected)

        return new_password_info
    
    def update_password_for_rule_8(self):
        new_password_part = self.get_random_sponsor()
        index = -1
        protected = True
        new_password_info = self.get_new_password_dict(new_password_part, index)
        self.password.insert_password_in_index(new_password_info['password'], index, protected)

        return new_password_info

    def get_random_sponsor(self):
        sponsors = ['Pepsi', 'Starbucks', 'Shell']
        random_sponsor = random.choice(sponsors)

        return random_sponsor

    def update_password_for_rule_10(self, captcha_value):
        new_password_part = captcha_value
        index = -1
        new_password_info = self.get_new_password_dict(new_password_part, index)
        self.password.insert_password_in_index(new_password_info['password'], index, protected=True)

        return new_password_info

    def get_new_password_dict(self, new_password, index, replace=False):
        new_password_info = {}
        new_password_info['password'] = new_password
        new_password_info['index'] = index
        new_password_info['replace'] = replace

        return new_password_info
    
class Password:
    def __init__(self):
        self.current_password = ''
        self.character_status = []
    
    def get_current_password(self):
        return self.current_password

    def insert_password_in_index(self, new_password_part, index, protected=False, replace=False):
        if index == -1:
            new_password = self.current_password + new_password_part
        elif not replace:
            new_password = self.current_password[:index] + new_password_part + self.current_password[index:]
        else:
            #TODO: precisa continuar a escrever o código para substituir trechos da senha a partir daqui
        status_len = len(new_password_part)
        self.set_character_status(protected, index, status_len)
        self.current_password = new_password

    def set_character_status(self, protected, index, status_len):
        if protected:
            protected_status = [1]
            status_to_insert = protected_status * status_len
        else:
            non_protected_status = [0]
            status_to_insert = non_protected_status * status_len
        if index == -1:
            self.character_status.extend(status_to_insert)
        else:
            self.character_status[index: index] = status_to_insert
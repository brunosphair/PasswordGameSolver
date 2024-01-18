from web_interact import Web
from game_solver import Solver
import time

class InteractionsSolverWeb():
    def __init__(self):
        self.web = Web()
        self.solver = Solver()
    
    def initiate_password_game(self):
        self.web.open_password_game()

    def initial_password(self):
        self.type_initial_password()

    def type_initial_password(self):
        initial_password = self.solver.get_initial_password()
        self.web.type_password_in_index(initial_password, -1)

    def update_password(self, current_password, new_password):
        
        num_charact_current_password = len(current_password)
        new_final = new_password[num_charact_current_password:]
        self.web.type_password_in_index(new_final)

    def solve_the_game(self):
        new_password = 'new_password' # initiates with a arbitrary value
        while new_password:
            time.sleep(1)
            rule_to_be_solved = self.web.get_rule_to_be_solved()
            new_password = self.get_new_password_to_the_rule(rule_to_be_solved)
            
            if new_password and 'replace' in new_password:
                self.web.type_password_in_index(new_password['password'],
                                                new_password['index'],
                                                new_password['replace'])
            elif new_password:
                self.web.type_password_in_index(new_password['password'],
                                                new_password['index'])
    
    def get_new_password_to_the_rule(self, rule_number):
        if rule_number == '2':
            password = self.solver.update_password_for_rule_2()
        elif rule_number == '3':
            password = self.solver.update_password_for_rule_3()
        elif rule_number == '4':
            password = self.solver.update_password_for_rule_4()
        elif rule_number == '5':
            password = self.solver.update_password_for_rule_5()
        elif rule_number == '6':
            password = self.solver.update_password_for_rule_6()
        elif rule_number == '7':
            password = self.solver.update_password_for_rule_7()
        elif rule_number == '8':
            password = self.solver.update_password_for_rule_8()
        elif rule_number == '10':
            captcha_value = self.web.get_captcha_value()
            password = self.solver.update_password_for_rule_10(captcha_value)
        else:
            return None
        
        return password

    
    def wait_and_close_browser(self):
        self.web.wait_and_close_browser()


if __name__ == '__main__':
    interactions = InteractionsSolverWeb()
    interactions.initiate_password_game()
    interactions.initial_password()
    interactions.solve_the_game()

    interactions.wait_and_close_browser()
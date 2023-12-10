from web_interact import Web
from game_solver import Solver

class InteractionsSolverWeb():
    def __init__(self):
        self.web = Web()
        self.captcha = None
    
    def initiate_password_game(self):
        self.web.open_password_game()

    def initial_password(self):
        self.type_initial_password()

    def type_initial_password(self):
        initial_password = Solver.get_initial_password()
        self.web.type_password(initial_password)

    def update_password(self, current_password, new_password):
        
        num_charact_current_password = len(current_password)
        new_final = new_password[num_charact_current_password:]
        self.web.type_password(new_final)

    def solve_the_game(self):
        new_password = 'new_password' # initiates with a arbitrary value
        while new_password:
            rule_to_be_solved = self.web.get_rule_to_be_solved()
            current_password = self.web.get_current_password()
            new_password = self.get_new_password_to_the_rule(current_password,
                                                             rule_to_be_solved)
            
            if new_password:
                self.update_password(current_password, new_password)
    
    def get_new_password_to_the_rule(self, current_password, rule_number):
        if rule_number == '10':
            captcha_value = self.web.get_captcha_value()
            password = Solver.get_password_for_rule_10(current_password, captcha_value)
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
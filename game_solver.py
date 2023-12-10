from web_interact import Web

class Solver:
    def __init__(self):
        pass

    def get_initial_password():

        initial_password = "Senha@123991OctoberXXXVShell"
        return initial_password
    

    def get_password_for_rule_10(current_password, captcha_value):
        new_password = current_password + captcha_value

        return new_password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Web:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_password_game(self):
        self.driver.get('https://neal.fun/password-game/')

    def type_password_in_index(self, value, index,replace=False):
        text_box_element = self.driver.find_element(By.CLASS_NAME, 'ProseMirror')
        if index == -1:
            text_box_element.send_keys(value)
        elif not replace:
            text_box_element.send_keys(Keys.CONTROL + Keys.HOME)
            for i in range(index):
                text_box_element.send_keys(Keys.ARROW_RIGHT)
            text_box_element.send_keys(value)
        elif replace:
            text_box_element.send_keys(Keys.CONTROL + Keys.HOME)
            for i in range(index):
                text_box_element.send_keys(Keys.ARROW_RIGHT)
            value_len = len(value)
            if value_len > 0:
                for character_index in range(value_len):
                    text_box_element.send_keys(Keys.DELETE)
                    text_box_element.send_keys(value[character_index])
            else:
                text_box_element.send_keys(Keys.DELETE)

    def get_rule_to_be_solved(self):
        rule_class = 'rule-top'
        text_rule_to_be_solved = self.driver.find_element(By.CLASS_NAME, rule_class).text
        number_rule_to_be_solved = self.get_number_rule_from_text(text_rule_to_be_solved)
        
        return number_rule_to_be_solved
    
    @staticmethod
    def get_number_rule_from_text(text):
        number_rule = text[5:]

        return number_rule
    
    def get_current_password(self):
        current_password = self.driver.find_element(By.CLASS_NAME, 'ProseMirror').text
        return current_password
    
    def get_captcha_value(self):
        captcha_image_link = self.driver.find_element(By.CLASS_NAME, 'captcha-img').get_attribute('src')
        last_slash_index = captcha_image_link.rfind('/')
        captcha_value = captcha_image_link[last_slash_index + 1:-4]

        return captcha_value

    def wait_and_close_browser(self):
        input('Press Enter to close the web browser...')
        self.close_browser()

    def close_browser(self):
        self.driver.quit()
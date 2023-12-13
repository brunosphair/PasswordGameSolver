class Password:
    def __init__(self):
        self.current_password = ''
        self.character_status = []
    
    def get_current_password(self):
        return self.current_password

    def insert_password_in_index_or_append(self, new_password_part, index=None, protected=False):
        if index is not None:
            new_password = self.current_password[:index] + new_password_part + self.current_password[index:]
        else:
            new_password = self.current_password + new_password_part
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
        if index is not None:
            self.character_status[index: index] = status_to_insert
        else:
            self.character_status.extend(status_to_insert)


if __name__ == '__main__':
    password = Password()
    password.insert_password_in_index_or_append('abcde', 0)
    print(password.current_password, password.character_status)
    password.insert_password_in_index_or_append('123', protected=True)
    print(password.current_password, password.character_status)

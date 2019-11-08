class User:
    '''
    Class that generates new instances of users
    '''

    user_list = [] # Empty User List

    def __init__(self,first_name,last_name,phone_number,email,password):
        '''
        __init__ method that helps us define properties for our objects
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.password = password
    
    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)



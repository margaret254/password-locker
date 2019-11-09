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

    def delete_user(self):
        '''
        Method deletes a user from the user_list
        '''

        User.user_list.remove(self)


class Credentials:
    '''
    class that generates credentials for the user
    '''

    credential_list = [] #Empty Credential list
    user_credentials_list = []

    def __init__(self,user_name,account_name,password):
        '''
        Method where we define properties for our objects
        '''

        self.user_name = user_name
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
        '''
        function to save user credentials
        '''
        Credentials.credential_list.append(self)
    
    
    
    
    
    
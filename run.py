#!/usr/bin/env python3.6
import pyperclip
from main import User
from main import Credentials

def create_user(first_name,last_name,phone_number,email,user_name,password):
    '''
    function to create new user account
    '''
    new_user = (first_name,last_name,phone_number,email,user_name,password)
    return new_user

def create_credential(user_name,account_name,password):
    '''
    function to create a new user account
    '''
    new_credential = Credentials(user_name,account_name,password)
    return new_credential

def save_user(user):
    '''
    function to save a new user
    '''
    User.save_user(user)

def save_credentials(credential):
    '''
    function to save a new user account
    '''
    Credentials.save_credentials(credential)

def authenticate_user(username,password):
    '''
    Function that verifies the existence of the user before creating credentials
    '''
    checking_user = Credentials.check_user(user_name,password)
    return checking_user



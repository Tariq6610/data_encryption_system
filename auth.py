import json
import os
import streamlit as st

class Users:
    """This is a User authentication class, where we can add users to our 'user.json' file, every user users
    is a dictionary with name as key and password as value in a list of dictionaries and also we can add
    retieve user to streamli session storage"""
    
    def __init__(self, name, password):
        self._name = name
        self._password = password
    
    # save User into json file and also add user to st.session
    def save_user(self):
        new_data = {self._name : self._password}
        if os.path.exists("users.json"):
            with open("users.json", "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []
                if not isinstance(data, list):
                    data = [data]
        else:
            data = []
        
        def is_name_avalible():
            if self._name not in data:
                data.append(new_data)
                print("user added successfully")
                return True
            else:
                print("user failed to add")
                return False


        if is_name_avalible():
            with open("users.json", "w") as f:
                json.dump(data, f, indent = 4)

            self.go_to_home_page(self._name)
            return True
        else:
            return False
    
    # add user to session storage
    @classmethod
    def go_to_home_page(cls, name):
        st.query_params["page"] = "home"
        st.query_params["user"] =  name
        st.rerun()


    
    # check session storage for user if it exist return True else return False
    @classmethod
    def login(cls, name, password):
        current_user = st.session_state.current_user
        if name in current_user:
            if current_user["password"] == password:
                return True
            else:
                return False
        else:
            return False

    # check user if it exists in json file if True add that user to session storage
    @classmethod
    def get_user(cls, name, password):
        if os.path.exists("users.json"):
            with open("users.json", "r") as f:
                try:
                    data : list = json.load(f)
                    for user in data:
                        if name in user:
                            if user[name] == password:
                                print("Login successful")
                                cls.go_to_home_page(name) 
                                return True                                                            
                            else:
                                print("invalid password")
                                return False                              
                        
                    else:
                        print("No User Found")
                        return False
                except json.JSONDecodeError:
                    print("User not found")
                    return False

        else:
            print("User not Found")
            return False




                 
                

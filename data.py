import os
import json
class DataEncription:
    def __init__(self, name, passkey, data):
        self.__name = name
        self.__passkey = passkey
        self.__data = data

    def add_data(self):
        new_data = {}
        new_data[self.__passkey] = {"encrypted_text": self.__data, "passkey": self.__passkey}
        if os.path.exists("data.json"):
            with open("data.json", "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []

                if not isinstance(data, list):
                    data = [data]
        else:
            data = []

        data.append(new_data)

        with open("data.json", "w") as f:
            json.dump(data, f, indent = 4)

    @staticmethod
    def retreive_data(name, passkey):
        if os.path.exists("data.json"):
            with open("data.json", "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []
                    return "No data Found"
                if isinstance(data, list):
                    for user in data:
                        if passkey in user:
                            if user[passkey]["passkey"] == passkey:
                                return user[passkey]["encrypted_text"]
                            else:
                                return "Invalid passkey"
                    else:
                        return "No user found"
                        



           
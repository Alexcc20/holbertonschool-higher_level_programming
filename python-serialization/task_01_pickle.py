#!/usr/bin/env python3

import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the object's attributes.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance of the object and saves it to the provided filename.

        Parameters:
        filename (str): The filename to save the serialized object.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Object serialized and saved to '{filename}'.")
        except Exception as e:
            print(f"Serialization failed: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Loads and returns an instance of CustomObject from the provided filename.

        Parameters:
        filename (str): The filename to load the serialized object from.

        Returns:
        CustomObject: The deserialized instance of CustomObject.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            print(f"Object deserialized from '{filename}'.")
            return obj
        except Exception as e:
            print(f"Deserialization failed: {e}")
            return None

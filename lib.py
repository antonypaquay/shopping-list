import logging
import json
import os

from constants import DATA_DIR

LOGGER = logging.getLogger()

class ShoppingList(list):
    def __init__(self, name):
        self.name = name

    def add_item(self, element):
        if not isinstance(element, str):
            raise ValueError("You can only add strings!")

        if element in self:
            LOGGER.error(f"{element} already exists in the list.")
            return False

        self.append(element)
        return True

    def remove_item(self, element):
        if element in self:
            self.remove(element)
            return True
        return False

    def display_list(self):
        print(f"{self.name}({len(self)}):")
        for element in self:
            print(f"- {element}")

    def save_list(self):
        file_path = os.path.join(DATA_DIR, f"{self.name}.json")
        if not os.path.exists(file_path):
            os.makedirs(DATA_DIR)
        
        with open(file_path, "w") as file:
            json.dump(self, file, indent=4)
        
        return True

        
if __name__ == "__main__":
    my_list = ShoppingList("courses")
    my_list.add_item("Pasta")
    my_list.add_item("Beer")
    my_list.add_item("Cheese")
    my_list.save_list()
import sys
import tkinter as tk
from tkinter import simpledialog, messagebox

from diary_package.diaries import Diaries

import diary


class MainApp:
    def __init__(self):
        self.diary = diary.Diary("username", "password")
        self.diaries = Diaries()

    def run(self):
        self.main_menu()

    @staticmethod
    def input(prompt):
        return simpledialog.askstring("Input", prompt)

    @staticmethod
    def print_message(output):
        messagebox.showinfo("Output", output)

    def main_menu(self):
        return_value = self.input("""
            Welcome to Diary
            <><><><><><><><><><><><><><><><><>
            What would you like to do?
                Enter 1: Add diary
                Enter 2: Find diary by username
                Enter 3: Delete diary
                Enter 4: Exit diary
            <><><><><><><><><><><><><><><><><>""")
        self.option(return_value)

    def main_menu1(self):
        return_value = self.input("""
                    Enter 1: lock diary
                    Enter 2: unlock diary
                    Enter 3: create entry
                    Enter 4: find entry by id
                    Enter 5: update entry
                    Enter 6: delete entry
                    Enter 7: exit diary""")
        return return_value

    def option(self, option):
        try:
            option = int(option)
            if option == 1:
                self.add_diary()
                input(self.main_menu1())
                self.option_main_menu(option)

            elif option == 2:
                self.find_diary_by_username()
            elif option == 3:
                self.delete_diary()
            elif option == 4:
                self.exit_diary_app()
            else:
                self.print_message("Enter the correct option")
                self.input(self.main_menu())
        except ValueError:
            self.print_message("Enter a valid option")
            self.main_menu()

    def add_diary(self):
        try:
            username = self.input("Enter your username")
            password = self.input("Enter password")
            self.diaries.add_diary(username, password)
            self.print_message("Diary added successfully")
            option = input(self.main_menu1())
            self.option_main_menu(option)
        except Exception as e:
            self.print_message(str(e))
            option = input(self.main_menu())
            self.option(option)

    def find_diary_by_username(self):
        try:
            username = self.input("Enter your diary username")
            result = self.diaries.find_by_user_name(username)
            self.print_message(result)
            option = input(self.main_menu())
            self.option(option)
        except Exception as e:
            self.print_message("diary not found")
            option = input(self.main_menu())
            self.option(option)

    def delete_diary(self):
        try:
            username = self.input("Enter your diary username")
            password = self.input("Enter your diary password")
            self.diaries.delete_diary(username, password)
            self.print_message("Diary deleted successfully")
            option = input(self.main_menu())
            self.option(option)

        except Exception as e:
            self.print_message("diary not found")
            option = input(self.main_menu())
            self.option(option)

    def exit_diary_app(self):
        self.print_message("<><><><><> Thanks for using this diary <><><><><>")
        root.destroy()

    def option_main_menu(self, option):
        match option:
            case 1:
                self.lock_diary()
            case 2:
                self.unlock_diary()

            case 3:
                self.create_entry()

            case 4:
                self.find_entry_by_id()

            case 5:
                self.update_entry()

            case 6:
                self.delete_entry()

            case 7:
                self.method(option)

            case _:
                self.option_main_menu(option)

    def method(self,option):
        self.main_menu()
        self.option(option)

    def lock_diary(self):
        self.diary.lock_diary()
        print("diary locked successfully")
        option = input(self.main_menu1())
        self.option_main_menu(option)

    def unlock_diary(self):
        try:
            password = input("Enter password to unlock")
            self.diary.unlock(password)
            print("Diary unlocked successfully")
            option = input(self.main_menu1())
            self.option_main_menu(option)
        except Exception as e:
            self.print_message(str(e))
            option = input(self.main_menu1())
            self.option_main_menu(option)

    def create_entry(self):
        try:
            title = input("Enter title")
            body = input("Enter body")
            self.diary.create_entry(title, body)
            print("Entry created successfully")
            print(f'{title} \n {body}')
            print(f"your entry id is {self.diary.generate_id()}")
            option = input(self.main_menu1())
            self.option_main_menu(option)
        except Exception as e:
            self.print_message(str(e))
            option = input(self.main_menu1())
            self.option_main_menu(option)

    def find_entry_by_id(self):
        try:
            entry_id = input("Enter id")
            self.diary.find_entry_by_id(id)
            print(f"{entry_id} is found")
            option = input(self.main_menu1())
            self.option_main_menu(option)
        except Exception as e:
            self.print_message(str(e))
            option = input(self.main_menu1())
            self.option_main_menu(option)

    def update_entry(self):
        try:
            entry_id = int(input("Enter the id"))
            new_title = input("Enter new title")
            new_body = input("Enter new body")
            self.diary.update_entry(entry_id, new_title, new_body)
            print(f'{entry_id} \n {new_title} \n {new_body}')
            option = input(self.main_menu1())
            self.option_main_menu(option)
        except Exception as e:
            self.print_message(str(e))
            option = input(self.main_menu1())
            self.option_main_menu(option)

    def delete_entry(self):
        try:
            entry_id = input("Enter entry id")
            self.diary.delete_entry(entry_id)
            print(f'{entry_id} id deleted successfully')
            option = input(self.main_menu1())
            self.option_main_menu(option)
        except Exception as e:
            self.print_message(str(e))
            option = input(self.main_menu1())
            self.option_main_menu(option)

    def exit_diary(self):
        print("Thanks for using this diary")
        self.main_menu()
        sys.exit()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp()
    app.run()
    root.mainloop()

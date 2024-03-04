import sys

from diary_package.diary import Diary


class MainApplication:
    diary = Diary("username", "password")

    def main_menu(self):
        print("""
                Welcome to Dark Royal diary
                <><><><><><><><><><><><><><><><><><><><><><>
                Enter 1.lock diary
                Enter 2. unlock diary
                Enter 3. create entry
                Enter 4. find entry by id
                Enter 5. update entry
                Enter 6. delete entry
                Enter 7. exit diary  
                <><><><><><><><><><><><><><><><><><><><><><>
        """)
        self.option()

    def option(self):
        option = input("Enter your choice")
        if option == '1':
            self.lock_diary()
        elif option == '2':
            self.unlock_diary()
        elif option == '3':
            self.create_entry()
        elif option == '4':
            self.find_entry_by_id()
        elif option == '5':
            self.update_entry()
        elif option == '6':
            self.delete_entry()
        elif option == '7':
            self.exit_diary()

    def lock_diary(self):
        self.diary.lock_diary()
        print("Diary locked successfully")
        self.main_menu()

    def unlock_diary(self):
        try:
            password = input("Enter your desirable password")
            self.diary.unlock(password)
            print("<><><><><><><><>diary is unlocked successfully<><><><><><><>")
        except BaseException as error:
            print(error)

        finally:
            self.main_menu()

    def create_entry(self):
        try:
            title = input("Enter your desirable title")
            body = input("Enter your desirable body")
            entry_id = int(input("Enter your id"))
            self.diary.create_entry(title, body, entry_id)
            print("<><><><><><><>diary is created successfully<><><><><><><>")
            print(f"{title}\n {body}")
        except BaseException as error:
            print(error)
        finally:
            self.main_menu()

    def find_entry_by_id(self):
        try:
            entry_id = int(input("Enter entry id"))
            self.diary.find_entry_by_id(entry_id)
            print(f"<><><><><><><>{entry_id} is found<><><><><><><><>")
        except BaseException as error:
            print(error)
        finally:
            self.main_menu()

    def update_entry(self):
        try:
            entry_id = int(input("Enter id"))
            new_title = input("Enter new title")
            new_body = input("Enter new body")
            self.diary.update_entry(entry_id,new_title,new_body)
            print(f"{new_title}\n {new_body}")
            print("Diary have been updated")
        except BaseException as error:
            print(error)
        finally:
            self.main_menu()

    def delete_entry(self):
        pass

    @staticmethod
    def exit_diary():
        print("<><><<><><><><><><><>Thanks for using Dark Royal diary😍😍😍😍😍😍\n we hope to see you soon😍😍😍😍😍😍")
        sys.exit()


diary = MainApplication()
diary.main_menu()

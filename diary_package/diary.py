from diary_package.entry import Entry


class Invalid_password_exception(BaseException):
    pass


def generate_id(entry_id):
    entry_id += 1


class Diary:
    def __init__(self, user_name: str, password: str):
        self.user_name = user_name
        self.password = password
        self.entries = []
        self.is_locked = True

    def get_user_name(self):
        return self.user_name

    def unlock(self, password):
        self.validate_password(password)
        return False

    @staticmethod
    def lock_diary():
        is_locked = True

    def validate_password(self, password):
        if self.password is not password:
            raise Invalid_password_exception("incorrect password")
        return False

    def create_entry(self, title: str, body: str, entry_id):
        generate_id(entry_id)
        entry = Entry(entry_id, title, body)
        self.entries.append(entry)
        return entry

    def delete_entry(self, entry_id):
        entry = self.find_entry_by_id(entry_id)
        self.entries.remove(entry_id)

    def get_number_of_entry(self):
        return self.entries

    def find_entry_by_id(self, entry_id):
        for entry in self.entries:
            if entry.entry_id == entry_id:
                return entry_id

    def update_entry(self, entry_id: int, title: str, body: str):
        for entry in self.entries:
            if entry.get_id() == entry_id:
                entry._title = title
                entry._body = body



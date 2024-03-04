from diary_package.diary_is_locked_exception import DiaryIsLockedException
from diary_package.entry import Entry
from diary_package.id_not_found_exception import IdNotFoundException
from diary_package.invalid_id_exception import InvalidIdException
from diary_package.invalid_pin_exception import InvalidPinException


class Diary:
    def __init__(self, user_name: str, password: str):
        self.user_name = user_name
        self.password = password
        self.entries = []
        self.is_locked = True

    def get_user_name(self):
        return self.user_name

    def lock_diary(self):
        self.is_locked = True

    def unlock(self, password):
        if self.password == password:
            self.is_locked = False
        else:
            raise InvalidPinException("incorrect password")

    def create_entry(self, title: str, body: str, entry_id):
        if not self.is_locked:
            entry = Entry(entry_id, title, body)
            # entry_id += 1
            self.entries.append(entry)
            return entry
        else:
            raise DiaryIsLockedException("diary is locked")

    def find_entry_by_id(self, entry_id) -> Entry:
        for entry in self.entries:
            if entry.get_entry_id() == entry_id:
                return entry
        raise InvalidIdException("Id not found")

    def delete_entry(self, entry_id):
        self.entries.remove(self.find_entry_by_id(entry_id))
        len(self.entries) - 1

    def get_number_of_entry(self):
        return len(self.entries)

    def update_entry(self, entry_id: int, title: str, body: str):
        for entry in self.entries:
            if entry.get_entry_id() == entry_id:
                entry.title = title
                entry.body = body
            raise IdNotFoundException("id not found")



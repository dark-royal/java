from diary_package.no_diary_is_found_exception import NoSuchDiaryExistException


class Diaries:
    def __init__(self):
        self.diaries = []

    def add_diary(self, user_name, password):
        diary = Diary()
        self.diaries.append(diary)
        return diary

    def get_number_of_diaries(self):
        return len(self.diaries)

    def find_by_user_name(self, user_name):
        for diary in self.diaries:
            if diary.get_user_name() == user_name:
                return diary
            raise NoSuchDiaryExistException("No diary exist")

    def delete_diary(self,user_name,password):
        found_diary = self.find_by_user_name(user_name)
        if found_diary.get_user_name() == user_name & found_diary.get_password() == password:

            self.diaries.remove(found_diary)
        raise NoSuchDiaryExistException("No diary exist")




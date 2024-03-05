import datetime


class Entry:
    def __init__(self, entry_id: int, title: str, body: str):
        self._entry_id = entry_id
        self._title = title
        self._body = body
        self._date_time_created = datetime.date.today()

    def get_entry_id(self):
        return self._entry_id

    @property
    def title(self):
        return self._title

    @property
    def date_time_created(self):
        return self._date_time_created

    @property
    def body(self):
        return self._body

    # @entry_id.setter
    # def entry_id(self, value):
    #     self._entry_id = value

    @title.setter
    def title(self, title):
        self._title = title

    @body.setter
    def body(self, body):
        self._body = body

    def __repr__(self):
        return f'entry id:{self._entry_id}\nbody: {self._title}\n'

    @date_time_created.setter
    def date_time_created(self, value):
        self._date_time_created = value

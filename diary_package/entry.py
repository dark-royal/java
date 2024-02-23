import datetime


class Entry:
    def __init__(self, entry_id: int, title: str, body: str):
        self.entry_id = entry_id
        self.title = title
        self.body = body
        self.date_time_created = datetime.date.today()

    @property
    def entry_id(self):
        return self.entry_id

    @property
    def title(self):
        return self.title

    @property
    def date_time_created(self):
        return self.date_time_created


    @property
    def body(self):
        return self.body

    @entry_id.setter
    def entry_id(self, value):
        self._entry_id = value

    @title.setter
    def title(self,title):
        self._title = title

    @body.setter
    def body(self,body):
        self._body = body

    def __repr__(self):
        return f'entry id:{self._entry_id}\nbody: {self._title}\n' \
               f'Nin: {self._body}'







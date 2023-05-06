class TeacherDTO:
    def __init__(self, id: int, firstname: str, lastname: str):
        self._id = id
        self._firstname = firstname
        self._lastname = lastname

    def __str__(self):
        return f"({self._id}, {self._firstname}, {self._lastname})"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self._firstname = firstname

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, lastname: int):
        self._lastname = lastname
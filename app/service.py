from abc import ABC, abstractmethod
from dao import TeacherDAOImpl
from teacher_dto import TeacherDTO
from teacher import Teacher, TeacherIDNotFoundError, TeacherLastnameNotFoundError, TeacherListIsEmptyError

class ABCTeacherService(ABC):
    """ Defines the service layer"""
    @abstractmethod
    def insert_teacher(self, teacher_dto:TeacherDTO):
        raise NotImplementedError()
    
    @abstractmethod
    def update_teacher(self, teacher_dto:TeacherDTO):
        raise NotImplementedError()
    
    @abstractmethod
    def delete_teacher(self, id:int):
        raise NotImplementedError()
    
    @abstractmethod
    def get_teacher_by_lastname(self, lastname:str):
        raise NotImplementedError()
    
    @abstractmethod
    def get_teacher_by_id(self, id:int):
        raise NotImplementedError()
    
    @abstractmethod
    def get_all_teachers(self):
        raise NotImplementedError()

class TeacherServiceImpl(ABCTeacherService):
    def __init__(self):
        self.teacher_DAO = TeacherDAOImpl()

    def insert_teacher(self, teacher_dto:TeacherDTO):
        teacher = dto_to_entity(teacher_dto)
        try:
            self.teacher_DAO.insert(teacher)
            print("Success in inserting teacher!")
        except Exception as e:
            print("Error in inserting teacher, try another ID")

    def update_teacher(self, teacher_dto:TeacherDTO):
        self.teacher_DAO.update(teacher_dto.id, teacher_dto.firstname, teacher_dto.lastname)
        print("Teacher updated")

    def delete_teacher(self, id:int):
        self.teacher_DAO.delete(id)
        print("Teacher deleted")
        
    def get_teacher_by_lastname(self, lastname:str):
        try:
            teacherDTO = self.teacher_DAO.get_teacher_by_lastname(lastname)
        except TeacherLastnameNotFoundError as e:
            print(e)
            return None
        return teacherDTO 
    
    def get_teacher_by_id(self, id:int):
        try:
            teacherDTO = self.teacher_DAO.get_teacher_by_id(id)
        except TeacherIDNotFoundError as e:
            print(e)
            return None
        return teacherDTO 
    
    def get_all_teachers(self):
        return self.teacher_DAO.get_all_teachers()
    
def dto_to_entity(teacherDTO:TeacherDTO):
    return Teacher(teacherDTO.id, teacherDTO.firstname, teacherDTO.lastname)
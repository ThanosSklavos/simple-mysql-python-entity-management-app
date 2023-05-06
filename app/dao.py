from abc import ABC, abstractmethod
from teacher import Teacher, TeacherLastnameNotFoundError, TeacherIDNotFoundError, TeacherListIsEmptyError
from get_connection import get_mysql_conn

class ABCTeacherDAO(ABC):
    """ Defines the Teacher DAO API """

    @abstractmethod
    def insert(self, teacher:Teacher):
        raise NotImplementedError()
    
    @abstractmethod
    def update(self, teacher:Teacher):
        raise NotImplementedError()
    
    @abstractmethod
    def delete(self, teacher:Teacher):
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


class TeacherDAOImpl(ABCTeacherDAO):
    def insert(self, teacher):
        conn = get_mysql_conn()
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO TEACHERS (id, firstname, lastname) VALUES ({teacher.id}, '{teacher.firstname}' , '{teacher.lastname}')")
        conn.commit()
        conn.close()

    def update(self, id_to_update:int, new_firstname:str, new_lastname:str):
        conn = get_mysql_conn()
        cursor = conn.cursor()
        cursor.execute(f"UPDATE TEACHERS SET FIRSTNAME = '{new_firstname}', LASTNAME = '{new_lastname}' WHERE ID = {id_to_update}")
        conn.commit()
        conn.close()

    def delete(self, id_to_delete:int):
        conn = get_mysql_conn()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM TEACHERS WHERE ID = {id_to_delete}")
        conn.commit()
        conn.close()

    def get_teacher_by_lastname(self, lastname:str):
        conn = get_mysql_conn()
        cursor = conn.cursor()
        cursor.execute(f"SELECT ID, FIRSTNAME, LASTNAME FROM TEACHERS WHERE LASTNAME = '{lastname}'")
        result = cursor.fetchone()
        conn.close()

        if result == None:
            raise TeacherLastnameNotFoundError(lastname)
        
        teacher = Teacher(*result)
        return teacher
        
    def get_teacher_by_id(self, id: int):
        conn = get_mysql_conn()
        cursor = conn.cursor()
        cursor.execute(f"SELECT ID, FIRSTNAME, LASTNAME FROM TEACHERS WHERE ID = {id}")
        result = cursor.fetchone()
        conn.close()

        if result == None:
            raise TeacherIDNotFoundError(id)

        teacher = Teacher(*result)
        return teacher
    
    def get_all_teachers(self):
        conn = get_mysql_conn()
        cursor = conn.cursor()
        cursor.execute(f"SELECT ID, FIRSTNAME, LASTNAME FROM TEACHERS")
        results = cursor.fetchall()
        conn.close()
        
        list_of_teachers = []

        for result in results:
            id = result[0]
            firstname = result[1]
            lastname = result[2]

            list_of_teachers.append(Teacher(id, firstname, lastname))

        if len(list_of_teachers) == 0:
            raise TeacherListIsEmptyError
        return list_of_teachers

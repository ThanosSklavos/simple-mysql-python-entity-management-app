import teacher as t
from teacher import TeacherLastnameNotFoundError
import teacher_dto as td
import dao
import service

teacher_DAO = dao.TeacherDAOImpl()
teacher_service = service.TeacherServiceImpl()

def main():
    while True:
        choice = print_menu()
        if choice == "1":
            teacher_to_insert = td.TeacherDTO(0, "", "")
            teacher_to_insert.id = int(input("Please enter the id: "))
            teacher_to_insert.firstname = input("Please enter the firstname: ")
            teacher_to_insert.lastname = input("Please enter the lastname: ")
            try:
                teacher_service.insert_teacher(teacher_to_insert)
            except Exception as e:
                continue

        elif choice == "2":
            id_to_delete = int(input("Please enter the teacher's id to delete: "))
            teacher_service.delete_teacher(id_to_delete)

        elif choice == "3":
            teacher_to_update = td.TeacherDTO(0, "", "")
            teacher_to_update.id = int(input("Please enter the id of the teacher you want to update: "))
            teacher_to_update.firstname = input("Please enter the new firstname: ")
            teacher_to_update.lastname = input("Please enter the new lastname: ")
            teacher_service.update_teacher(teacher_to_update)

        elif choice == "4":
            lastname = input("Please enter a lastname to search: ")
            try:
                teacher = teacher_service.get_teacher_by_lastname(lastname)
            except TeacherLastnameNotFoundError as e:
                print(e)
                continue
            print(teacher)

        elif choice == "5":
            teacher_list = teacher_service.get_all_teachers()
            print("\n----------  Entries  -----------")
            print("ID     Firstname    Lastname")
            print("--------------------------------")
            for teacher in teacher_list:
                print(f"{teacher.id:<6} {teacher.firstname:<12} {teacher.lastname}")
            print("-------------------------------")
        elif choice.lower() in ["q", "quit"]:
            print("Goodbye!")
            break

        else:
            print("Please enter a valid choice.")

def print_menu():
    print("\n======================")
    print("Welcome to teachers management system")
    print("1. Insert a teacher")
    print("2. Delete a teacher")
    print("3. Update a teacher")
    print("4. Search a teacher by Lastname")
    print("5. Get all teachers")
    print("Q/q to quit")
    return input("Please enter the number of your choice: ")

if __name__ == '__main__':
    main()

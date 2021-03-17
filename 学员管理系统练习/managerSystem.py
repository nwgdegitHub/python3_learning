from student import *


class StudentManager(object):
    def __init__(self):
        self.student_list = []

        # 入口函数

    def run(self):

        self.load_student()

        while True:

            self.show_menu()

            menu_num = int(input('请输入您需要的功能序号: '))

            if menu_num == 1:

                self.add_student()

            elif menu_num == 2:

                self.del_student()

            elif menu_num == 3:

                self.modify_student()
            elif menu_num == 4:

                self.search_student()

            elif menu_num == 5:

                self.show_student()

            elif menu_num == 6:

                self.save_student()
            elif menu_num == 7:

                break

    @staticmethod
    def show_menu():
        print("请选择：")
        print("1.添加")
        print("2.删除")
        print("3.修改")
        print("4.查询")
        print("5.显示所有")
        print("6.保存")
        print("7.推出")

    def add_student(self):
        print("add_student")
        name = input("请输入姓名：")
        gender = input("请输入性别：")
        tel = input("请输入手机号：")

        student = Student(name, gender, tel)

        self.student_list.append(student)

        print(self.student_list)

        print(student)

    def del_student(self):
        print("del_student")
        del_name = input("请输入你想删除的姓名：")

        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                break
            else:
                print("查无此人")

        print(self.student_list)

    def modify_student(self):
        print("modify_student")
        modify_name = input("请输入你想修改的姓名：")
        for i in self.student_list:
            if i.name == modify_name:
                i.name = input("请输入姓名：")
                i.gender = input("请输入性别：")
                i.tel = input("请输入手机号：")

                print(f'修改完成,{self.name},{self.gender},{self.tel}')
            else:
                print("查无此人")

        print(self.student_list)

    def search_student(self):
        print("search_student")
        search_name = input("请输入你想删除的姓名：")

        for i in self.student_list:
            if i.name == search_name:
                print(f'查询完成,{self.name},{self.gender},{self.tel}')
                break
            else:
                print("查无此人")

    def show_student(self):
        print("show_student")
        for i in self.student_list:
            print(f'查询完成,{i.name},{i.gender},{i.tel}')

    def save_student(self):
        print("save_student")
        f = open('student.data', 'w')
        new_list = [i.__dict__ for i in self.student_list]
        print(new_list)

        f.write(str(new_list))

        f.close()

    def load_student(self):
        print("load_student")
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            content = f.read()
            new_list = eval(content)
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
            self.show_student()
        finally:
            f.close()

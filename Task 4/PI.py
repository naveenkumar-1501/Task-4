class Task:
    def __init__(self):
        self.__pi = 3.141
    def get_pi(self):
        return self.__pi
    def set_pi(self, new_pi):
        self.__pi = new_pi
my_task = Task()
print(f"Value of pi: {my_task.get_pi()}")
my_task.set_pi(3.14)
print(f"Updated value of pi: {my_task.get_pi()}")

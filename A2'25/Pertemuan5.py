from abc import ABC ,abstractclassmethod


# class Repository:
#     def add(self, value):
#         pass
    
#     def remove(self, value):
#         pass
    
# class UserRepository(Repository):
    
#     def add(self, value):
#         print("add user")
        
#     def remove(self, value):
#         print("remove user")
            

from abc import ABC, abstractmethod

class UserRepositor(ABC):
    @abstractmethod
    def add(self, value):
        pass
    
class UserRepositoryImplSql(UserRepositor):
    def add(self, value):
        print(f"add user sql {value}")
        
class UserRepositoryImplPortgreSql(UserRepositor):
    def add(self, value):
        print("add user postgresql")

class UserService():
    def __init__(self, user_repository):
        self.user_repository = UserRepositoryImplSql
    
    def add_user(self):
        self.user_repository.add("Eko")  
        
user_repo = UserRepositoryImplSql()
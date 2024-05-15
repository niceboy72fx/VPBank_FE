import abc

from type.result import Result
from type.general import Condition

class Account(abc.ABC):
    @abc.abstractmethod
    def get_tenant(self, condition: Condition) :
        pass
    
    @abc.abstractmethod
    def create_tenant(self, condition: Condition):
        pass
    
    @abc.abstractmethod
    def update_tenant(self, condition: Condition):
        pass
    
    @abc.abstractmethod
    def delete_tenant(self, condition: Condition) -> Result[list[int]]:
        pass
    
    @abc.abstractmethod
    def get_list_role(self, condition: Condition):
        pass
    
    @abc.abstractmethod
    def get_role(self, condition: Condition):
        pass
    
    @abc.abstractmethod
    def create_role(self, condition: Condition):
        pass
    
    @abc.abstractmethod
    def update_role(self, condition: Condition):
        pass
    
    @abc.abstractmethod
    def delete_role(self, condition: Condition) -> Result[list[int]]:
        pass
    
    @abc.abstractmethod
    def get_user(self, condition: Condition):
        pass
    
    @abc.abstractmethod
    def create_user(self, condition: Condition):
        pass
    
    @abc.abstractmethod
    def update_user(self, condition: Condition):
        pass
    
    @abc.abstractmethod
    def delete_user(self, condition: Condition):
        pass
    
    @abc.abstractmethod
    def get_list_pem(self, condition: Condition):
        pass
    
    @abc.abstractmethod
    def get_pem(self, condition: Condition):
        pass
    
    @abc.abstractmethod
    def create_pem(self, condition: Condition):
        pass
    
    @abc.abstractmethod
    def update_pem(self, condition: Condition):
        pass 
    
    @abc.abstractmethod
    def delete_pem(self, condition: Condition) -> Result[list[int]] :
        pass
    
    
class UserCrud(abc.ABC):
    @abc.abstractmethod
    def get_user_list_with_filter(
        self, condition: Condition, order: str, filter):
        pass


class RoleCrud(abc.ABC):
    @abc.abstractmethod
    def get_role_list_with_filter(
        self, condition: Condition, order: str, filter) :
        pass

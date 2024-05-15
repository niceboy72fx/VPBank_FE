import abc

from type.general import Token

class Auth(abc.ABC):
    @abc.abstractmethod
    def get_user_from_token(self, access_token):
        pass
    
    @abc.abstractmethod
    def update_last_login(self, user, refresh_token: Token) -> None :
        pass
    
    @abc.abstractmethod
    def update_refresh_token(self, user, refresh_token: str):
        pass
    
class BasicAuth(abc.ABC):
    @abc.abstractmethod
    def verify_username_password(self, username: str, password: str):
        pass
    
    @abc.abstractmethod
    def generate_token_pair(self, user):
        pass
    
    @abc.abstractmethod
    def get_group_permissions(self, user):
        pass 
    
    @abc.abstractmethod
    def update_pwd(self, user, password: str):
        pass 
    
    @abc.abstractmethod
    def get_profile(self, user):
        pass
    
    
    
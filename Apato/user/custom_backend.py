from django.contrib.auth.backends import ModelBackend
from .models import User

class CustomUserBackend(ModelBackend):
    """Define custom authenticate backend as we use email as login credentials"""
    
    def authenticate(self, email, password):
        """This is custom authenticate where email and password will be used to login"""
        login_user = User.objects.get(email = email) # gives the object with the respective email 

        if login_user is None:
            return None
        """If used "filter" returns querryset which may be multiple object. In our case email is uniquie so it will return 
        single object as querryset but still better to use "get" for future reference too. Also ".fileter().first()" can be 
        used to get the first object only """

        if login_user.check_password(password):
            return login_user

        return None
from django.contrib.auth.base_user import BaseUserManager

class CustomManager(BaseUserManager):
    """As we are customzing the login feature( email based login)"""

    def create_user(self, email, password = None, **extra_fields):
        """To create new user with email and password as credentials.
        The password is set None inorder to prevent directly inserting
        the password value while creating the user instance."""

        
        """Checking email"""
        if email is None:
            raise ValueError(f'From Custom Manager. The email is {email}')
        
        """Normalizing email : ayush@GMIAL.COM -> ayush@gmail.com"""
        email = self.normalize_email(email)

        """Creating the user instance (without password)"""
        user = self.model(email = email, **extra_fields)

        """Hashing and setting the user password"""
        user.set_password(password)

        """Saving in the database"""
        user.save(using = self._db)
        print("User is saved in the database")
        print(f"this is type: {type(user)}")
        return user
    

    """Creating Super User"""
    def create_superuser(self, email, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        # Validation - ensure required flags are set
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        # Using create_user method (DRY principle)
        # This ensures all the same validation and processing happens
        return self.create_user(email, password, **extra_fields)
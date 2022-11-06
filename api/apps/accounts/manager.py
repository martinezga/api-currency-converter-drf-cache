from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email):
        user = self.model(
            email=self.normalize_email(email),
        )
        password = self.make_random_password()
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.model(
            email=self.normalize_email(email),
            is_superuser=True,
            is_staff=True
        )
        password = self.make_random_password()
        user.set_password(password)
        user.save()
        return user
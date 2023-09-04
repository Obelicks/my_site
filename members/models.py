from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
        """
        Used by the admin/member page to give proper context for the object being administrated on. 
        Without this function the members object are listed as object.member(0-n)
        """
        return f'{self.firstname}  {self.lastname}'

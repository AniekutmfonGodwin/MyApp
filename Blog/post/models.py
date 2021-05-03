from django.db import models
import uuid






    



class Profile(models.Model):
    TYPES = (
        ("st","student"),
        ("th","teacher"),
    )
    user_type = models.CharField("type",choices=TYPES, max_length=50,help_text="select a use type",unique=True)





    def __str__(self):
        return self.user_type





    

    



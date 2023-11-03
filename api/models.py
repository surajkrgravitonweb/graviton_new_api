from django.db import models
import datetime
# Create your models here.
class WebinarContact(models.Model):
    Name=models.CharField(max_length=200,null=True,default="null")
    LastName = models.CharField(max_length=200,null=True,default="null")
    email=models.CharField(max_length=200,null=True,default="null")
    phone = models.IntegerField(max_length=12 ,null=True,default="null")
    message=models.CharField(max_length=200,null=True,default="null")
    date=models.CharField(max_length=322,null=True,default=datetime.datetime.now())


    def __str__(self):
        return self.Name
    

class FeedBack2(models.Model):
    title = models.CharField(max_length=255)
    first_Poor = models.BooleanField(default=False)
    first_Average = models.BooleanField(default=False)
    first_Excellent = models.BooleanField(default=False)

    Second_Poor = models.BooleanField(default=False)
    Second_Average = models.BooleanField(default=False)
    Second_Excellent = models.BooleanField(default=False)

    Third_Poor = models.BooleanField(default=False)
    Third_Average = models.BooleanField(default=False)
    Third_Excellent = models.BooleanField(default=False)


    def get_first_feedback(self):
        if self.first_Excellent:
            return "Excellent"
        elif self.first_Average:
            return "Average"
        elif self.first_Poor:
            return "Poor"
        else:
            return "Not set"

    def get_second_feedback(self):
        if self.Second_Excellent:
            return "Excellent"
        elif self.Second_Average:
            return "Average"
        elif self.Second_Poor:
            return "Poor"
        else:
            return "Not set"

    def get_third_feedback(self):
        if self.Third_Excellent:
            return "Excellent"
        elif self.Third_Average:
            return "Average"
        elif self.Third_Poor:
            return "Poor"
        else:
            return "Not set"


    


    def __str__(self):
        return self.title


class Feedback1(models.Model):
    firstName=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=200)
    phone=models.CharField(max_length=15)
    is_Check=models.BooleanField(default=False)
    textField=models.CharField(max_length=200)


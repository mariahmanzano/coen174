from django.db import models

class NewSessionForm(models.Model):
    sessionNum = models.CharField(max_length=10)
    roomNum = models.CharField(max_length=10)

    def __str__(self):
        return self.sessionNum

    def is_valid():
        return True;

class Group (models.Model):
    project_name= models.CharField(max_length=50)
    group_name= models.CharField(max_length=50)
    advisor_name= models.CharField(max_length=50)

    session = models.ForeignKey(NewSessionForm, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name

    def is_valid():
        return True;

class adminPermission(models.Model):
    adminPermission = "Permission for admin."
    
    class Meta:
        permissions = [
            ("is_admin", "This user is an admin")
        ]
    def _str_(self):
        return self.adminPermission

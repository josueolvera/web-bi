from django.db import models
from django.utils import timezone

# Create your models here.
class Roles(models.Model):
    id_Rol = models.IntegerField()
    role_Name = models.CharField(max_length = 200)
    creation_Date = models.DateTimeField(default = timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.role_Name

class CBranchs(models.Model):
    id_branch = models.IntegerField()
    branch_name = models.CharField(max_length = 500)
    branch_short = models.CharField(max_length = 100)
    creation_date = models.DateTimeField(default = timezone.now)

    def saveBranch(self):
        self.save()

    def __str__(self):
        return self.branch_name

class BranchsRoles(models.Model):
    id_branch_role = models.IntegerField()
    id_branch = models.ForeignKey('bidg.cBranchs', on_delete = models.CASCADE)
    id_Rol = models.ForeignKey('bidg.roles', on_delete = models.CASCADE)
    vacant_number = models.IntegerField()

    def assignRoltoBranch(self):
        self.save()

    def __str__(self):
        return str(self.id_branch) + " - Rol: " + str(self.id_Rol)
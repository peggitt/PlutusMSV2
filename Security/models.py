from django.db import models
import uuid
from datetime import datetime, timedelta
from django.utils import timezone
from SystemCode.models import Gender
from django.contrib.auth.models import User
from Bank.models import BankBranch


# Create your models here.
class Endpoint(models.Model):
    EndpointKey = models.CharField(max_length=30, primary_key=True)
    Address = models.CharField(max_length=100)
    SystemCode = models.CharField(max_length=100)
    EndpointStatus = models.CharField(max_length=100,default="")

# Create your models here. 
class SystemUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    UserName =  models.CharField(max_length=100)
    UserEmail =  models.CharField(max_length=100)
    EmailConfirmed = models.BooleanField(default=False)
    HashPassword =  models.CharField(max_length=4000)
    PhoneNumber =  models.CharField(max_length=100)
    OtpLogin = models.BooleanField(default=False)
    ChangePassword = models.BooleanField(default=True)
    Otp =  models.CharField(max_length=100,blank=True)
    AccessAllowed = models.BooleanField(default=False)
    AccessLocked = models.BooleanField(default=False)
    FirstName =  models.CharField(max_length=100)
    MiddleName =  models.CharField(max_length=100,blank=True)
    LastName =  models.CharField(max_length=100)
    IDNumber =  models.CharField(max_length=100)
    DOB =  models.DateField(default = timezone.now, blank=True ,null=True)
    Sex =  models.ForeignKey(Gender, on_delete=models.CASCADE)
    ResetDate =  models.DateField(default = timezone.now, blank=True ,null=True)
    CreatedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    CreatedOn = models.DateField(default = timezone.now, blank=True ,null=True)
    AccountActive = models.BooleanField(default=False)
    SuperAdminUser =  models.CharField(max_length=100,blank=True)

class SystemSession(models.Model):
    KeyChain = models.BigAutoField(primary_key=True)
    UserName = models.ForeignKey(SystemUser,on_delete=models.CASCADE)
    DataKey = models.IntegerField(blank=True, null=True)
    ActiveKey = models.BooleanField(default=True)
    KeyDate = models.DateTimeField(default=timezone.now,blank=True)

class SecurityRole(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    RoleName =  models.CharField(max_length=200)

    CreatedBy =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    CreatedOn =  models.DateField(default = timezone.now, blank=True ,null=True)
    ModifiedBy =  models.CharField(max_length=200, blank=True)
    ModifiedOn =  models.DateField(default = timezone.now, blank=True ,null=True)
    ApprovedBy =  models.CharField(max_length=200, blank=True)
    ApprovedOn =  models.DateField(default = timezone.now, blank=True ,null=True)
    DeactivatedBy =  models.CharField(max_length=200,blank=True ,null=True)
    DeactivatedOn =  models.DateField(default = timezone.now, blank=True ,null=True)

class UserRole(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    UserId =  models.ForeignKey(SystemUser, on_delete=models.CASCADE)
    UserRole =  models.ForeignKey(SecurityRole, on_delete=models.CASCADE)
    BranchId =  models.ForeignKey(BankBranch, on_delete=models.CASCADE)

    CreatedBy =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    CreatedOn =  models.DateField(default = timezone.now, blank=True ,null=True)
    ModifiedBy =  models.CharField(max_length=200, blank=True)
    ModifiedOn =  models.DateField(default = timezone.now, blank=True ,null=True)
    ApprovedBy =  models.CharField(max_length=200, blank=True)
    ApprovedOn =  models.DateField(default = timezone.now, blank=True ,null=True)
    DeactivatedBy =  models.CharField(max_length=200,blank=True ,null=True)
    DeactivatedOn =  models.DateField(default = timezone.now, blank=True ,null=True)








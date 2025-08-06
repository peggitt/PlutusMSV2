from django.db import models
import uuid
from datetime import datetime, timedelta
from django.utils import timezone
from SystemCode.models import Gender
from django.contrib.auth.models import User
from Bank.models import BankBranch
from Security.models import SecurityRole,SystemUser


# Create your models here.
class MainModule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    MenuName =  models.CharField(max_length=200,default='')
    ModuleLicense =  models.CharField(max_length=2000)
    ModuleName =  models.CharField(max_length=200)
    ModuleDescription =  models.CharField(max_length=200,default='')
    ModuleTable =  models.CharField(max_length=200)
    IsConfigured = models.BooleanField(default=False)
    HasView = models.BooleanField(default=False)
    HasAdd = models.BooleanField(default=False)
    HasEdit = models.BooleanField(default=False)
    HasDelete = models.BooleanField(default=False)
    HasSupervise = models.BooleanField(default=False)
    HasMakerChecker = models.BooleanField(default=False)
    HasWorkflow = models.BooleanField(default=False)
    HasMaxValues = models.BooleanField(default=False)
    HasCREDITPOSTINGLIMIT = models.BooleanField(default=False)
    HasCREDITSUPERVISIONLIMIT = models.BooleanField(default=False)
    HasDEBITPOSTINGLIMIT = models.BooleanField(default=False)
    HasDEBITSUPERVISIONLIMIT = models.BooleanField(default=False)
    HasEXCESSSUPERVISIONLIMIT = models.BooleanField(default=False)
    DefaultNumRecords =  models.IntegerField(default=10)
    DefaultShowMineOnly = models.BooleanField(default=False)
    ModuleGroup =  models.CharField(max_length=200,default='')
    ModuleView =  models.CharField(max_length=200,default='')
    IsMainModule = models.BooleanField(default=False)
    ParentModuleId =  models.CharField(max_length=200,default='',blank=True)
    IsSubModule = models.BooleanField(default=False)

class ModuleRight(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ModuleId = models.ForeignKey(MainModule, on_delete=models.CASCADE)
    UserRole =  models.ForeignKey(SecurityRole, on_delete=models.CASCADE)
    CanView = models.BooleanField(default=False)
    CanAdd = models.BooleanField(default=False)
    CanEdit = models.BooleanField(default=False)
    CanDelete = models.BooleanField(default=False)
    CanSupervise = models.BooleanField(default=False)
    CanMakerChecker = models.BooleanField(default=False)
    CanWorkflow = models.BooleanField(default=False)
    CanMaxValues = models.BooleanField(default=False)
    CREDITPOSTINGLIMIT = models.BooleanField(default=False)
    CREDITSUPERVISIONLIMIT = models.BooleanField(default=False)
    DEBITPOSTINGLIMIT = models.BooleanField(default=False)
    DEBITSUPERVISIONLIMIT = models.BooleanField(default=False)
    EXCESSSUPERVISIONLIMIT = models.BooleanField(default=False)
    Approved = models.BooleanField(default=False)
    UpdatedBy = models.ForeignKey(SystemUser,on_delete=models.CASCADE)
    UpdatedOn = models.DateField(default = timezone.now, blank=True ,null=True)
    SupervisedBy = models.CharField(max_length=2000)
    SupervisedOn = models.DateField(default = timezone.now, blank=True ,null=True)


class SystemControl(models.Model):
    id = models.AutoField(primary_key=True)
    ControlId = models.CharField(default='',max_length=200)
    Details =  models.CharField(max_length=200)



class SystemModuleConfigs(models.Model):
    id = models.AutoField(primary_key=True)
    ModuleId = models.ForeignKey(MainModule, on_delete=models.CASCADE)
    ColumnName =  models.CharField(max_length=200)
    ColumnType =  models.CharField(max_length=200)
    isMandatory = models.BooleanField(default=False)
    QuestionCaption = models.CharField(default='',max_length=200)
    isGridItem = models.BooleanField(default=False)
    QuestionOrder = models.IntegerField(default=0)
    GridOrder = models.IntegerField(default=0)
    isSearchItem = models.BooleanField(default=False)
    SearchProcedure = models.CharField(default='',max_length=200)
    isUnique = models.BooleanField(default=False)
    isAutoField = models.BooleanField(default=False)
    FunctionEvent = models.CharField(default='',max_length=4000)
    isLocked = models.BooleanField(default=False)
    ControlType = models.CharField(default='',max_length=200)


class SystemSubModuleConfigs(models.Model):
    id = models.AutoField(primary_key=True)
    SubModuleId = models.ForeignKey(MainModule, on_delete=models.CASCADE)
    ColumnName =  models.CharField(max_length=200)
    ColumnType =  models.CharField(max_length=200)
    isMandatory = models.BooleanField(default=False)
    QuestionCaption = models.CharField(default='',max_length=200)
    isGridItem = models.BooleanField(default=False)
    QuestionOrder = models.IntegerField(default=0)
    GridOrder = models.IntegerField(default=0)
    isSearchItem = models.BooleanField(default=False)
    SearchProcedure = models.CharField(default='',max_length=200)
    isUnique = models.BooleanField(default=False)
    isAutoField = models.BooleanField(default=False)
    FunctionEvent = models.CharField(default='',max_length=4000)
    isLocked = models.BooleanField(default=False)
    isCombo = models.BooleanField(default=False)
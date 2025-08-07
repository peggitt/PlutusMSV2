from django.db import models

# Create your models here.
class ProductType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class FrequencyType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class RoundingOption(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class ProductCategory(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class AccountType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class CustomerType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class YesNo(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class AccountOperatingMode(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class SystemUserType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)


class InterestRateType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class InterestRateCategory(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class DebitInterestCalcMethod(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class CreditInterestCalcMethod(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class BaseRateSpreadSign(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class BaseRateModule(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class InterestCalcBalanceType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class DayCountBasis(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class InterestType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class InterestCalcMethod(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class WorkflowDocumentCategory(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class WorkflowModule(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class FeeChargeEvent(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class FeeCalculatedOn(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class CreditTransactionDesc(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class DebitTransactionDesc(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class ChargeFeeCalc(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class ProductGLAccount(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class ProductAccountingEvent(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class DenominationType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class TillState(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class TransactionAccountType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class TillTransactionType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class CreditorDebit(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class CustomerAccountState(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class BranchHolidayHandling(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class LoanHolidayHandling(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class AccountOperationMode(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class TransactionDescription(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class IDGenerationModule(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class OfficerType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class InstallmentRecoveryComponent(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class LoanDisbursementMode(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class LoanDisbursementType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class FreezeType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class FDInterestApplicationFrequency(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class FDRenewalMode(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class FilterOperant(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class DocumentCopyorOriginal(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class TransactionType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class FeePaymentModule(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class TransactionChargeEvent(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class Weekdays(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class DepositCalculationType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class GroupCycleType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class GridExportType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class InterestDaysCalcBase(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class StandingInstructionType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class LoanDeliquencyLevel(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class LoanState(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class BankProcess(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class InstitutionType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class ReportViewOption(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class ReportFilterCriteria(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class InstrumentType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class QuickTransactionAmount(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class MemberTransferState(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class TellerDeclarationOption(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class GuaranteeComputationAmtComponent(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class PartnerBillState(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class WhoPayChargeOption(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class StatementdateType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class FeeReceiptFormat(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class CommisionSharingWith(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class CommisionPayableTo(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class NotificationType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class AgencyReportingPeriodType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class LoanAgreementFormat(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class NotificationTimeOption(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class EventNotificationConfig(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class FixedInstallmentDay(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class InvoiceSettlementState(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class InvoiceCategory(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class GoodsReceivedType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class LPODeliveryState(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class LPOType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class ContractState(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class TillTransferType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class CommisionShareOption(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class OneOffFeeChargeModel(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class ShareRedemptionOption(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class GroupLoanInstallmentPolicy(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class ApprovalAction(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class FixedAssetDisposalType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class FixedAssetTransferState(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class FixedAssetRevaluationState(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class AssetAquisitionType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class FixedAssetStatus(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class GroupTransferType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class GroupTransferState(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)

class Gender(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID', help_text='Unique identifier')
    CodeId = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage1 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage2 = models.CharField(max_length=4000,blank=False)
    CodeIdLanguage3 = models.CharField(max_length=4000,blank=False)


from django.contrib import admin

# Register your models here.
from .models import GroupTransferState,GroupTransferType,FixedAssetStatus,AssetAquisitionType
from .models import FixedAssetRevaluationState,FixedAssetTransferState,FixedAssetDisposalType
from .models import ApprovalAction,GroupLoanInstallmentPolicy,ShareRedemptionOption,OneOffFeeChargeModel
from .models import CommisionShareOption,TillTransferType,ContractState,LPOType,LPODeliveryState
from .models import GoodsReceivedType,InvoiceCategory,InvoiceSettlementState,FixedInstallmentDay
from .models import EventNotificationConfig,NotificationTimeOption,LoanAgreementFormat,AgencyReportingPeriodType
from .models import NotificationType,CommisionPayableTo,CommisionSharingWith,FeeReceiptFormat,StatementdateType
from .models import WhoPayChargeOption,PartnerBillState,GuaranteeComputationAmtComponent,TellerDeclarationOption
from .models import MemberTransferState,QuickTransactionAmount,InstrumentType,ReportFilterCriteria,ReportViewOption
from .models import InstitutionType,BankProcess,LoanState,LoanDeliquencyLevel,StandingInstructionType,InterestDaysCalcBase
from .models import GridExportType,GroupCycleType,DepositCalculationType,Weekdays,TransactionChargeEvent,FeePaymentModule
from .models import TransactionType,DocumentCopyorOriginal,FilterOperant,FDRenewalMode,FDInterestApplicationFrequency
from .models import FreezeType,LoanDisbursementType,LoanDisbursementMode,InstallmentRecoveryComponent,OfficerType
from .models import IDGenerationModule,TransactionDescription,AccountOperationMode,BranchHolidayHandling,CustomerAccountState
from .models import CreditorDebit,AccountType,TillTransactionType,TransactionAccountType,TillState,DenominationType
from .models import ProductAccountingEvent,ProductGLAccount,ChargeFeeCalc,DebitTransactionDesc,CreditTransactionDesc
from .models import FeeCalculatedOn,FeeChargeEvent,WorkflowModule,WorkflowDocumentCategory,InterestCalcMethod
from .models import InterestType,DayCountBasis,InterestCalcBalanceType,BaseRateModule,BaseRateSpreadSign,CreditInterestCalcMethod
from .models import DebitInterestCalcMethod,InterestRateCategory,InterestRateType,SystemUserType,AccountOperatingMode,YesNo
from .models import CustomerType,ProductCategory,RoundingOption,FrequencyType,ProductType,Gender,LoanHolidayHandling
from .models import InterestRateId

admin.site.register(GroupTransferState)
admin.site.register(GroupTransferType)
admin.site.register(FixedAssetStatus)
admin.site.register(AssetAquisitionType)
admin.site.register(FixedAssetRevaluationState)
admin.site.register(FixedAssetTransferState)
admin.site.register(FixedAssetDisposalType)
admin.site.register(ApprovalAction)
admin.site.register(GroupLoanInstallmentPolicy)
admin.site.register(ShareRedemptionOption)
admin.site.register(OneOffFeeChargeModel)
admin.site.register(CommisionShareOption)
admin.site.register(TillTransferType)
admin.site.register(ContractState)
admin.site.register(LPOType)
admin.site.register(LPODeliveryState)
admin.site.register(GoodsReceivedType)
admin.site.register(InvoiceCategory)
admin.site.register(InvoiceSettlementState)
admin.site.register(FixedInstallmentDay)
admin.site.register(EventNotificationConfig)
admin.site.register(NotificationTimeOption)
admin.site.register(LoanAgreementFormat)
admin.site.register(AgencyReportingPeriodType)
admin.site.register(NotificationType)
admin.site.register(CommisionPayableTo)
admin.site.register(CommisionSharingWith)
admin.site.register(FeeReceiptFormat)
admin.site.register(StatementdateType)
admin.site.register(WhoPayChargeOption)
admin.site.register(PartnerBillState)
admin.site.register(GuaranteeComputationAmtComponent)
admin.site.register(TellerDeclarationOption)
admin.site.register(MemberTransferState)
admin.site.register(QuickTransactionAmount)
admin.site.register(InstrumentType)
admin.site.register(ReportFilterCriteria)
admin.site.register(ReportViewOption)
admin.site.register(InstitutionType)
admin.site.register(BankProcess)
admin.site.register(LoanState)
admin.site.register(LoanDeliquencyLevel)
admin.site.register(StandingInstructionType)
admin.site.register(InterestDaysCalcBase)
admin.site.register(GridExportType)
admin.site.register(GroupCycleType)
admin.site.register(DepositCalculationType)
admin.site.register(Weekdays)
admin.site.register(TransactionChargeEvent)
admin.site.register(FeePaymentModule)
admin.site.register(TransactionType)
admin.site.register(DocumentCopyorOriginal)
admin.site.register(FilterOperant)
admin.site.register(FDRenewalMode)
admin.site.register(FDInterestApplicationFrequency)
admin.site.register(FreezeType)
admin.site.register(LoanDisbursementType)
admin.site.register(LoanDisbursementMode)
admin.site.register(InstallmentRecoveryComponent)
admin.site.register(OfficerType)
admin.site.register(IDGenerationModule)
admin.site.register(TransactionDescription)
admin.site.register(AccountOperationMode)
admin.site.register(BranchHolidayHandling)
admin.site.register(CustomerAccountState)
admin.site.register(CreditorDebit)
admin.site.register(AccountType)
admin.site.register(TillTransactionType)
admin.site.register(TransactionAccountType)
admin.site.register(TillState)
admin.site.register(DenominationType)
admin.site.register(ProductAccountingEvent)
admin.site.register(ProductGLAccount)
admin.site.register(ChargeFeeCalc)
admin.site.register(DebitTransactionDesc)
admin.site.register(CreditTransactionDesc)
admin.site.register(FeeCalculatedOn)
admin.site.register(FeeChargeEvent)
admin.site.register(WorkflowModule)
admin.site.register(WorkflowDocumentCategory)
admin.site.register(InterestCalcMethod)
admin.site.register(InterestType)
admin.site.register(DayCountBasis)
admin.site.register(InterestCalcBalanceType)
admin.site.register(BaseRateModule)
admin.site.register(BaseRateSpreadSign)
admin.site.register(CreditInterestCalcMethod)
admin.site.register(DebitInterestCalcMethod)
admin.site.register(InterestRateCategory)
admin.site.register(InterestRateType)
admin.site.register(SystemUserType)
admin.site.register(AccountOperatingMode)
admin.site.register(YesNo)
admin.site.register(CustomerType)
admin.site.register(ProductCategory)
admin.site.register(RoundingOption)
admin.site.register(FrequencyType)
admin.site.register(ProductType)
admin.site.register(Gender)
admin.site.register(LoanHolidayHandling)
admin.site.register(InterestRateId)

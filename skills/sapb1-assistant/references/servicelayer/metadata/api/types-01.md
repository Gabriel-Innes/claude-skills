<!-- source: Service Layer /b1s/v2/$metadata | version: SAP Business One 10.0 FP 2602 | verified: 2026-10-05 -->

# SAPB1.AccountCategory (EntityType)

Key: CategoryCode

## Properties

- CategoryCode : Edm.Int32 [required]
- CategoryName : Edm.String
- CategorySource : SAPB1.AccountCategorySourceEnum

## Navigation properties

- ChartOfAccounts : Collection(SAPB1.ChartOfAccount) [Partner=AccountCategory]

# SAPB1.AccountCategoryParams (ComplexType)

## Properties

- CategoryCode : Edm.Int32
- CategoryName : Edm.String

# SAPB1.AccountSegmentation (EntityType)

OpenType: true
Key: Numerator

## Properties

- Numerator : Edm.Int32 [required]
- Name : Edm.String
- Size : Edm.Int32
- Type : SAPB1.AccountSegmentationTypeEnum
- AccountSegmentationsCategories : Collection(SAPB1.AccountSegmentationsCategory)

## Navigation properties

- AccountSegmentationCategories : Collection(SAPB1.AccountSegmentationCategory) [Partner=AccountSegmentation]

# SAPB1.AccountSegmentationCategory (EntityType)

OpenType: true
Key: SegmentID, Code

## Properties

- SegmentID : Edm.Int32 [required]
- Code : Edm.String [required]
- Name : Edm.String
- ShortName : Edm.String

## Navigation properties

- AccountSegmentation : SAPB1.AccountSegmentation [Partner=AccountSegmentationCategories]

# SAPB1.AccountSegmentationCategoryParams (ComplexType)

## Properties

- SegmentID : Edm.Int32
- Code : Edm.String

# SAPB1.AccountSegmentationParams (ComplexType)

## Properties

- Numerator : Edm.Int32

# SAPB1.AccountSegmentationsCategory (ComplexType)

OpenType: true

## Properties

- SegmentID : Edm.Int32
- Code : Edm.String
- Name : Edm.String
- ShortName : Edm.String

# SAPB1.AccrualType (EntityType)

OpenType: true
Key: Code

## Properties

- Code : Edm.String [required]
- Name : Edm.String
- PostingAccount : Edm.String
- CalculationAccount : Edm.String
- InterimAccount : Edm.String

## Navigation properties

- ChartOfAccount : SAPB1.ChartOfAccount [Partner=AccrualTypes]

# SAPB1.AccrualTypeParams (ComplexType)

## Properties

- Code : Edm.String

# SAPB1.Activity (EntityType)

OpenType: true
Key: ActivityCode

## Properties

- ActivityCode : Edm.Int32 [required]
- CardCode : Edm.String
- Notes : Edm.String
- ActivityDate : Edm.DateTimeOffset
- ActivityTime : Edm.TimeOfDay
- StartDate : Edm.DateTimeOffset
- Closed : SAPB1.BoYesNoEnum
- CloseDate : Edm.DateTimeOffset
- Phone : Edm.String
- Fax : Edm.String
- Subject : Edm.Int32
- DocType : Edm.String
- DocNum : Edm.String
- DocEntry : Edm.String
- Priority : SAPB1.BoMsgPriorities
- Details : Edm.String
- ActivityProperty : SAPB1.BoActivities
- ActivityType : Edm.Int32
- Location : Edm.Int32
- StartTime : Edm.TimeOfDay
- EndTime : Edm.TimeOfDay
- Duration : Edm.Double
- DurationType : SAPB1.BoDurations
- SalesEmployee : Edm.Int32
- ContactPersonCode : Edm.Int32
- HandledBy : Edm.Int32
- Reminder : SAPB1.BoYesNoEnum
- ReminderPeriod : Edm.Double
- ReminderType : SAPB1.BoDurations
- City : Edm.String
- PersonalFlag : SAPB1.BoYesNoEnum
- Street : Edm.String
- ParentObjectId : Edm.Int32
- ParentObjectType : Edm.String
- Room : Edm.String
- InactiveFlag : SAPB1.BoYesNoEnum
- State : Edm.String
- PreviousActivity : Edm.Int32
- Country : Edm.String
- Status : Edm.Int32
- TentativeFlag : SAPB1.BoYesNoEnum
- EndDueDate : Edm.DateTimeOffset
- DocTypeEx : Edm.String
- AttachmentEntry : Edm.Int32
- RecurrencePattern : SAPB1.RecurrencePatternEnum
- EndType : SAPB1.EndTypeEnum
- SeriesStartDate : Edm.DateTimeOffset
- SeriesEndDate : Edm.DateTimeOffset
- MaxOccurrence : Edm.Int32
- Interval : Edm.Int32
- Sunday : SAPB1.BoYesNoEnum
- Monday : SAPB1.BoYesNoEnum
- Tuesday : SAPB1.BoYesNoEnum
- Wednesday : SAPB1.BoYesNoEnum
- Thursday : SAPB1.BoYesNoEnum
- Friday : SAPB1.BoYesNoEnum
- Saturday : SAPB1.BoYesNoEnum
- RepeatOption : SAPB1.RepeatOptionEnum
- BelongedSeriesNum : Edm.Int32
- IsRemoved : SAPB1.BoYesNoEnum
- AddressName : Edm.String
- AddressType : SAPB1.BoAddressType
- HandledByEmployee : Edm.Int32
- RecurrenceSequenceSpecifier : SAPB1.RecurrenceSequenceEnum
- RecurrenceDayInMonth : Edm.Int32
- RecurrenceMonth : Edm.Int32
- RecurrenceDayOfWeek : SAPB1.RecurrenceDayOfWeekEnum
- SalesOpportunityId : Edm.Int32
- SalesOpportunityLine : Edm.Int32
- HandledByRecipientList : Edm.Int32
- Office365EventId : Edm.String
- DataVersion : Edm.Int32
- UserSignature : Edm.Int32
- UserSignature2 : Edm.Int32
- EmailedFlag : SAPB1.BoYesNoEnum
- CheckInListParams : Collection(SAPB1.CheckInParams)
- ActivityMultipleRecipients : Collection(SAPB1.ActivityMultipleRecipient)

## Navigation properties

- BusinessPartner : SAPB1.BusinessPartner [Partner=Activities]
- ActivitySubject : SAPB1.ActivitySubject [Partner=Activities]
- ActivityType2 : SAPB1.ActivityType [Partner=Activities]
- ActivityLocation : SAPB1.ActivityLocation [Partner=Activities]
- SalesPerson : SAPB1.SalesPerson [Partner=Activities]
- User : SAPB1.User [Partner=Activities]
- Country2 : SAPB1.Country [Partner=Activities]
- ActivityStatus : SAPB1.ActivityStatus [Partner=Activities]
- EmployeeInfo : SAPB1.EmployeeInfo [Partner=Activities]
- ActivityRecipientList : SAPB1.ActivityRecipientList [Partner=Activities]

# SAPB1.ActivityInstanceParams (ComplexType)

## Properties

- ActivityCode : Edm.Int32
- InstanceDate : Edm.DateTimeOffset

# SAPB1.ActivityInstancesListParams (ComplexType)

## Properties

- StartDate : Edm.DateTimeOffset
- InstanceCount : Edm.Int32

# SAPB1.ActivityLocation (EntityType)

OpenType: true
Key: Code

## Properties

- Code : Edm.Int32 [required]
- Name : Edm.String

## Navigation properties

- Activities : Collection(SAPB1.Activity) [Partner=ActivityLocation]
- ServiceCalls : Collection(SAPB1.ServiceCall) [Partner=ActivityLocation]
- Contacts : Collection(SAPB1.Contact) [Partner=ActivityLocation]

# SAPB1.ActivityLocationParams (ComplexType)

## Properties

- Code : Edm.Int32

# SAPB1.ActivityMultipleRecipient (ComplexType)

OpenType: true

## Properties

- LineNumer : Edm.Int32
- RecipientType : SAPB1.ActivityRecipientObjTypeEnum
- RecipientCode : Edm.String

# SAPB1.ActivityParams (ComplexType)

## Properties

- ActivityCode : Edm.Int32
- CardCode : Edm.String
- Notes : Edm.String
- StartDate : Edm.DateTimeOffset
- Closed : SAPB1.BoYesNoEnum
- DocType : Edm.String
- DocNum : Edm.String
- DocEntry : Edm.String
- Priority : SAPB1.BoMsgPriorities
- Details : Edm.String
- Activity : SAPB1.BoActivities
- StartTime : Edm.TimeOfDay
- EndTime : Edm.TimeOfDay
- HandledBy : Edm.Int32
- City : Edm.String
- Street : Edm.String
- Room : Edm.String
- InactiveFlag : SAPB1.BoYesNoEnum
- State : Edm.String
- Country : Edm.String
- TentativeFlag : SAPB1.BoYesNoEnum
- EndDueDate : Edm.DateTimeOffset
- SalesOpportunityId : Edm.Int32
- SalesOpportunityLine : Edm.Int32
- EmailedFlag : SAPB1.BoYesNoEnum

# SAPB1.ActivityRecipient (ComplexType)

## Properties

- LineNumber : Edm.Int32
- RecipientType : SAPB1.RecipientTypeEnum
- RecipientCode : Edm.String

# SAPB1.ActivityRecipientList (EntityType)

Key: Code

## Properties

- Code : Edm.Int32 [required]
- Name : Edm.String
- Active : SAPB1.BoYesNoEnum
- IsMultiple : SAPB1.BoYesNoEnum
- ActivityRecipientCollection : Collection(SAPB1.ActivityRecipient)

## Navigation properties

- Activities : Collection(SAPB1.Activity) [Partner=ActivityRecipientList]

# SAPB1.ActivityRecipientListParams (ComplexType)

## Properties

- Code : Edm.Int32
- Name : Edm.String
- Active : SAPB1.BoYesNoEnum
- IsMultiple : SAPB1.BoYesNoEnum

# SAPB1.ActivityStatus (EntityType)

OpenType: true
Key: StatusId

## Properties

- StatusDescription : Edm.String
- StatusId : Edm.Int32 [required]
- StatusName : Edm.String

## Navigation properties

- Activities : Collection(SAPB1.Activity) [Partner=ActivityStatus]
- Contacts : Collection(SAPB1.Contact) [Partner=ActivityStatus]

# SAPB1.ActivityStatusParams (ComplexType)

## Properties

- StatusId : Edm.Int32

# SAPB1.ActivitySubject (EntityType)

Key: Code

## Properties

- Code : Edm.Int32 [required]
- Description : Edm.String
- ActivityType : Edm.Int32
- IsActive : SAPB1.BoYesNoEnum

## Navigation properties

- Activities : Collection(SAPB1.Activity) [Partner=ActivitySubject]
- ActivityType2 : SAPB1.ActivityType [Partner=ActivitySubjects]
- Contacts : Collection(SAPB1.Contact) [Partner=ActivitySubject]

# SAPB1.ActivitySubjectParams (ComplexType)

## Properties

- Code : Edm.Int32
- Description : Edm.String

# SAPB1.ActivityType (EntityType)

OpenType: true
Key: Code

## Properties

- Code : Edm.Int32 [required]
- Name : Edm.String

## Navigation properties

- Activities : Collection(SAPB1.Activity) [Partner=ActivityType2]
- ActivitySubjects : Collection(SAPB1.ActivitySubject) [Partner=ActivityType2]
- Contacts : Collection(SAPB1.Contact) [Partner=ActivityType2]

# SAPB1.ActivityTypeParams (ComplexType)

## Properties

- Code : Edm.Int32

# SAPB1.AdditionalExpense (EntityType)

OpenType: true
Key: ExpensCode

## Properties

- Name : Edm.String
- RevenuesAccount : Edm.String
- ExpenseAccount : Edm.String
- TaxLiable : SAPB1.BoYesNoEnum
- FixedAmountRevenues : Edm.Double
- FixedAmountExpenses : Edm.Double
- OutputVATGroup : Edm.String
- InputVATGroup : Edm.String
- DistributionMethod : SAPB1.BoAeDistMthd
- Includein1099 : SAPB1.BoYesNoEnum
- FreightOffsetAccount : Edm.String
- WTLiable : Edm.String
- ExpensCode : Edm.Int32 [required]
- ExpenseExemptedAccount : Edm.String
- RevenuesExemptedAccount : Edm.String
- DistributionRule : Edm.String
- DrawingMethod : SAPB1.DrawingMethodEnum
- FreightType : SAPB1.FreightTypeEnum
- Stock : SAPB1.BoYesNoEnum
- LastPurchasePrice : SAPB1.BoYesNoEnum
- Project : Edm.String
- DistributionRule2 : Edm.String
- DistributionRule3 : Edm.String
- DistributionRule4 : Edm.String
- DistributionRule5 : Edm.String
- DataVersion : Edm.Int32
- SAFTProductType : SAPB1.SAFTProductTypeEnum
- SAFTProductTypeEx : Edm.String

## Navigation properties

- ChartOfAccount : SAPB1.ChartOfAccount [Partner=AdditionalExpenses]
- VatGroup : SAPB1.VatGroup [Partner=AdditionalExpenses]
- DistributionRule6 : SAPB1.DistributionRule [Partner=AdditionalExpenses]
- Project2 : SAPB1.Project [Partner=AdditionalExpenses]

# SAPB1.AdditionalExpenseParams (ComplexType)

## Properties

- ExpensCode : Edm.Int32

# SAPB1.AddressExtension (ComplexType)

OpenType: true
Filtered properties: 4

## Properties

- ShipToStreet : Edm.String
- ShipToStreetNo : Edm.String
- ShipToBlock : Edm.String
- ShipToBuilding : Edm.String
- ShipToCity : Edm.String
- ShipToZipCode : Edm.String
- ShipToCounty : Edm.String
- ShipToState : Edm.String
- ShipToCountry : Edm.String
- ShipToAddressType : Edm.String
- BillToStreet : Edm.String
- BillToStreetNo : Edm.String
- BillToBlock : Edm.String
- BillToBuilding : Edm.String
- BillToCity : Edm.String
- BillToZipCode : Edm.String
- BillToCounty : Edm.String
- BillToState : Edm.String
- BillToCountry : Edm.String
- BillToAddressType : Edm.String
- ShipToGlobalLocationNumber : Edm.String
- BillToGlobalLocationNumber : Edm.String
- ShipToAddress2 : Edm.String
- ShipToAddress3 : Edm.String
- BillToAddress2 : Edm.String
- BillToAddress3 : Edm.String
- PlaceOfSupply : Edm.String
- PurchasePlaceOfSupply : Edm.String
- DocEntry : Edm.Int32
- GoodsIssuePlaceBP : Edm.String
- GoodsIssuePlaceCNPJ : Edm.String
- GoodsIssuePlaceCPF : Edm.String
- GoodsIssuePlaceStreet : Edm.String
- GoodsIssuePlaceStreetNo : Edm.String
- GoodsIssuePlaceBuilding : Edm.String
- GoodsIssuePlaceZip : Edm.String
- GoodsIssuePlaceBlock : Edm.String
- GoodsIssuePlaceCity : Edm.String
- GoodsIssuePlaceCounty : Edm.String
- GoodsIssuePlaceState : Edm.String
- GoodsIssuePlaceCountry : Edm.String
- GoodsIssuePlacePhone : Edm.String
- GoodsIssuePlaceEMail : Edm.String
- GoodsIssuePlaceDepartureDate : Edm.DateTimeOffset
- DeliveryPlaceBP : Edm.String
- DeliveryPlaceCNPJ : Edm.String
- DeliveryPlaceCPF : Edm.String
- DeliveryPlaceStreet : Edm.String
- DeliveryPlaceStreetNo : Edm.String
- DeliveryPlaceBuilding : Edm.String
- DeliveryPlaceZip : Edm.String
- DeliveryPlaceBlock : Edm.String
- DeliveryPlaceCity : Edm.String
- DeliveryPlaceCounty : Edm.String
- DeliveryPlaceState : Edm.String
- DeliveryPlaceCountry : Edm.String
- DeliveryPlacePhone : Edm.String
- DeliveryPlaceEMail : Edm.String
- DeliveryPlaceDepartureDate : Edm.DateTimeOffset
- ShipToStreetForReturn : Edm.String
- ShipToStreetNoForReturn : Edm.String
- ShipToBlockForReturn : Edm.String
- ShipToBuildingForReturn : Edm.String
- ShipToCityForReturn : Edm.String
- ShipToZipCodeForReturn : Edm.String
- ShipToCountyForReturn : Edm.String
- ShipToStateForReturn : Edm.String
- ShipToCountryForReturn : Edm.String
- ShipToAddressTypeForReturn : Edm.String
- ShipToGlobalLocationNumberForReturn : Edm.String
- ShipToAddress2ForReturn : Edm.String
- ShipToAddress3ForReturn : Edm.String

# SAPB1.AddressFormat (ComplexType)

## Properties

- Code : Edm.Int32
- Name : Edm.String
- Format : Edm.String

# SAPB1.AddressFormatParams (ComplexType)

## Properties

- Code : Edm.Int32
- Name : Edm.String

# SAPB1.AddressParams (ComplexType)

OpenType: true
Filtered properties: 4

## Properties

- Country : Edm.String
- State : Edm.String
- County : Edm.String
- ZipCode : Edm.String
- City : Edm.String
- Building : Edm.String
- Block : Edm.String
- Street : Edm.String
- StreetNo : Edm.String
- Address2 : Edm.String
- Address3 : Edm.String
- AddressType : Edm.String
- GlobalLocationNumber : Edm.String

# SAPB1.AddressReturnParams (ComplexType)

## Properties

- FullAddress : Edm.String

# SAPB1.AdminInfo (ComplexType)

## Properties

- Code : Edm.Int32
- CompanyName : Edm.String
- Address : Edm.String
- Country : Edm.String
- PrintingHeader : Edm.String
- PhoneNumber1 : Edm.String
- PhoneNumber2 : Edm.String
- FaxNumber : Edm.String
- eMail : Edm.String
- ManagingDirector : Edm.String
- ChartofAccountsTemplate : Edm.String
- LocalCurrency : Edm.String
- SystemCurrency : Edm.String
- CreditBalancewithMinusSign : SAPB1.BoYesNoEnum
- StandardUnitofLength : Edm.Int32
- WeightUnitDefault : Edm.Int32
- DirectIndirectRate : SAPB1.BoYesNoEnum
- MinimumAmountfor347Report : Edm.Double
- SetItemsWarehouses : SAPB1.BoYesNoEnum
- BankCountry : Edm.String
- FederalTaxID : Edm.String
- TaxOffice : Edm.String
- DeductionFileNo : Edm.String
- TaxCollection : SAPB1.BoYesNoEnum
- TaxDefinition : SAPB1.BoYesNoEnum
- TaxPercentage : Edm.Double
- AdvancesonCorpIncomeTax : Edm.Double
- WithTax : Edm.Double
- WithholdingTaxVendorDdct : SAPB1.BoYesNoEnum
- CustomersDeductionatSource : SAPB1.BoYesNoEnum
- WithholdingTaxTdctPercnt : Edm.Double
- WithholdingTaxDdctExpired : Edm.DateTimeOffset
- WithholdingTaxDdctOffice : Edm.String
- CommitmentRestriction : SAPB1.BoYesNoEnum
- CreditRestriction : SAPB1.BoYesNoEnum
- RestrictSales : SAPB1.BoYesNoEnum
- RestrictDelNotesPO : SAPB1.BoYesNoEnum
- RestrictOrders : SAPB1.BoYesNoEnum
- ConsiderDelNotesinSalesR : SAPB1.BoYesNoEnum
- CreditDepositType : SAPB1.BoYesNoEnum
- UseTax : SAPB1.BoYesNoEnum
- SplitPO : SAPB1.BoYesNoEnum
- AltNameForApInvoice : Edm.String
- AltNameforCreditMemo : Edm.String
- AltNameForGoodsReceipt : Edm.String
- AltNameForGoodsReturn : Edm.String
- AltNameForPurchase : Edm.String
- AlertTypeforWHStock : SAPB1.BoAlertTypeforWHStockEnum
- SetCommissionbyCustomer : SAPB1.BoYesNoEnum
- SetCommissionbyItem : SAPB1.BoYesNoEnum
- SetCommissionbySE : SAPB1.BoYesNoEnum
- DefaultCustomerPaymentTerms : Edm.Int32
- DefaultVendorPaymentTerms : Edm.Int32
- CalculateGrossProfitperTra : SAPB1.BoYesNoEnum
- PriceListforCostPrice : Edm.Int32
- GrossProfitAfterSale : SAPB1.BoYesNoEnum
- DisplayPriceforPriceOnly : SAPB1.BoYesNoEnum
- CalculateTaxinSalesQuotati : SAPB1.BoYesNoEnum
- BaseField : SAPB1.BoYesNoEnum
- AllowClosedSalesQuotations : SAPB1.BoYesNoEnum
- UserConversionCode : SAPB1.BoYesNoEnum
- CompanyColor : Edm.Int32
- TotalsAccuracy : Edm.Int32
- AccuracyofQuantities : Edm.Int32
- PriceAccuracy : Edm.Int32
- RateAccuracy : Edm.Int32
- PercentageAccuracy : Edm.Int32
- MeasuringAccuracy : Edm.Int32
- QueryAccuracy : Edm.Int32
- AddressinForeignLanguage : Edm.String
- DefaultTaxCode : Edm.String
- LetterHeaderinForeignLangu : Edm.String
- PhoneNumber1ForeignLang : Edm.String
- PhoneNumber2ForeignLang : Edm.String
- FaxNumberForeignLang : Edm.String
- ManagingDirectorForeignLan : Edm.String
- TimeTemplate : SAPB1.BoTimeTemplate
- DateTemplate : SAPB1.BoDateTemplate
- DateSeparator : Edm.String
- FCCheckAccount : SAPB1.BoCurrencyCheck
- ChangedExistingOrders : SAPB1.BoYesNoEnum
- MultiCurrencyCheck : SAPB1.BoCurrencyCheck
- ISRType : Edm.Int32
- DisplayRoundingRemark : SAPB1.BoYesNoEnum
- ISRBillerID : Edm.String
- BlockSystemCurrencyEditing : SAPB1.BoYesNoEnum
- BlockPostingDateEditing : SAPB1.BoYesNoEnum
- DefaultWarehouse : Edm.String
- BlockTaxDate : SAPB1.BoYesNoEnum
- TaxDefinitionforVatitem : Edm.String
- TaxDefinitionforVatservice : Edm.String
- TaxGroupforPurchaseItem : Edm.String
- TaxGroupforServicePurchase : Edm.String
- CalculateBudget : SAPB1.BoYesNoEnum
- CustomerIdNumber : Edm.String
- BlockBudget : SAPB1.BoBlockBudget
- BudgetAlert : SAPB1.BoBudgetAlert
- BlockPurchaseOrders : SAPB1.BoYesNoEnum
- BlockBookkeeping : SAPB1.BoYesNoEnum
- DefaultBudgetCostAssessMt : Edm.Int32
- ContinuousStockManagement : SAPB1.BoYesNoEnum
- ContinuousStockSystem : SAPB1.BoInventorySystem
- RoundTaxAmounts : SAPB1.BoYesNoEnum
- BlockDelNotesforPurchase : SAPB1.BoYesNoEnum
- FileNumberinIncomeTax : Edm.String
- DeferredTax : SAPB1.BoYesNoEnum
- DefaultBankNo : Edm.String
- DefaultBankAccount : Edm.String
- DefaultBranch : Edm.String
- UsePASystem : SAPB1.BoYesNoEnum
- ServiceCode : Edm.String
- ServicePassword : Edm.String
- ParamFolderPath : Edm.String
- ExcelFolderPath : Edm.String
- FederalTaxID2 : Edm.String
- FederalTaxID3 : Edm.String
- DecimalSeparator : Edm.String
- ThousandsSeparator : Edm.String
- DisplayCurrencyontheRight : SAPB1.BoYesNoEnum
- AlertbyWarehouse : SAPB1.BoYesNoEnum
- PriceSystem : SAPB1.BoYesNoEnum
- WholdingTaxDedHierarchy : SAPB1.BoYesNoEnum
- DocConfirmation : SAPB1.BoYesNoEnum
- DefaultforBatchStatus : SAPB1.BoDefaultBatchStatus
- GLMethod : SAPB1.BoGLMethods
- UniqueSerialNo : SAPB1.BoUniqueSerialNumber
- MaxHistory : Edm.Int32
- ChangeDefReconAPAccounts : SAPB1.BoYesNoEnum
- ChangeDefReconARAccounts : SAPB1.BoYesNoEnum
- BPTypeCode : Edm.String
- PBSNumber : Edm.String
- PBSGroupNumber : Edm.String
- OrganizationNumber : Edm.String
- AccountSegmentsSeparator : Edm.String
- DisplayBookkeepingWindow : SAPB1.BoYesNoEnum
- SHandleWT : SAPB1.BoYesNoEnum
- SDefaultWTCode : Edm.String
- WithholdingTaxPHandle : Edm.String
- PDefaultWTCode : Edm.String
- WTLiableExpense : SAPB1.BoYesNoEnum
- UseNegativeAmounts : SAPB1.BoYesNoEnum
- HolidaysName : Edm.String
- OrderBlock : Edm.String
- RoundingMethod : SAPB1.BoYesNoEnum
- AdressFromWH : SAPB1.BoYesNoEnum
- OrderingParty : Edm.String
- CertificateNo : Edm.String
- ExpirationDate : Edm.DateTimeOffset
- NationalInsuranceNo : Edm.String
- SalesOrderConfirmed : SAPB1.BoYesNoEnum
- PurchaseOrderConfirmed : SAPB1.BoYesNoEnum
- SDfltITWT : Edm.String
- PDfltITWT : Edm.String
- DefaultAccountCurrency : SAPB1.BoYesNoEnum
- DeferredTaxforVendors : SAPB1.BoYesNoEnum
- CreateAutoVATLineinJDT : SAPB1.BoYesNoEnum
- ConsumeForecast : SAPB1.BoYesNoEnum
- ConsumptionMethod : SAPB1.BoConsumptionMethod
- DaysBackward : Edm.Int32
- DaysForward : Edm.Int32
- DefaultDunningTerm : Edm.String
- DefaultBankAccountKey : Edm.Int32
- MultiLanguageSupportEnable : SAPB1.BoYesNoEnum
- AllowFuturePostingDate : SAPB1.BoYesNoEnum
- AdditionalIdNumber : Edm.String
- State : Edm.String
- CalculateRowDiscount : SAPB1.BoYesNoEnum
- BankStatementInstalled : SAPB1.BoYesNoEnum
- EnableDigitalPayments : SAPB1.BoYesNoEnum
- UniqueTaxPayerReference : Edm.String
- EmployerReference : Edm.String
- PeriodStatusAutoChange : SAPB1.BoYesNoEnum
- PeriodStatusChangeDelay : Edm.Int32
- GrossProfitPercentForServiceDocuments : Edm.Double
- XMLFileFolderPath : Edm.String
- PickList : SAPB1.BoYesNoEnum
- GeneralManager : Edm.String
- GeneralManagerForeignLanguage : Edm.String
- UseProductionProfitAndLossAccount : SAPB1.BoYesNoEnum
- WTAccumAmountAP : Edm.Double
- WTAccumAmountAR : Edm.Double
- CopyExchangeRateInCopyTo : SAPB1.BoYesNoEnum
- GTSOutboundFolder : Edm.String
- GTSInboundFolder : Edm.String
- GTSSeparateCode : Edm.String
- GTSDefaultChecker : Edm.Int32
- GTSDefaultPayee : Edm.Int32
- GTSMaxAmount : Edm.Double
- GTSResponseToExceeding : SAPB1.GTSResponseToExceedingEnum
- ApplicationOfIFRS : SAPB1.BoYesNoEnum
- StartingInFiscalYear : Edm.Int32
- ReportAccordingTo : Edm.Int32
- CopyOpenRowsToDelivery : SAPB1.BoYesNoEnum
- EnableApprovalProcedureInDI : SAPB1.BoYesNoEnum
- EnableUpdateDocAfterApproval : SAPB1.BoYesNoEnum
- EnableUpdateDraftDuringApproval : SAPB1.BoYesNoEnum
- EnableAuthorizerUpdatePendingDraft : SAPB1.BoYesNoEnum
- IssuePrimarilyBy : SAPB1.IssuePrimarilyByEnum
- IsRemoveUnpricedValue : SAPB1.BoYesNoEnum
- EnableAdvancedGLAccountDetermination : SAPB1.BoYesNoEnum
- CreateOnlineQuotation : SAPB1.BoYesNoEnum
- IsPrinterConnected : SAPB1.BoYesNoEnum
- EnableBranches : SAPB1.BoYesNoEnum
- IEMandatoryValidation : SAPB1.BoYesNoEnum
- EnablePaymentDueDates : SAPB1.BoYesNoEnum
- MaximumNumberOfDaysForDueDate : Edm.Int32
- AliasName : Edm.String
- EnableCentralizedIncomingPayments : SAPB1.BoYesNoEnum
- EnableCentralizedOutgoingPayments : SAPB1.BoYesNoEnum
- TaxRateDetermination : SAPB1.TaxRateDeterminationEnum
- BoletoFolderPath : Edm.String
- AllowMultipleBAOnSamePeriod : SAPB1.BoYesNoEnum
- BlockMultipleBAOnSameAPDocument : SAPB1.BoYesNoEnum
- BlockMultipleBAOnSameARDocument : SAPB1.BoYesNoEnum
- DisplayCancelDocInReport : SAPB1.BoYesNoEnum
- MaxDaysForCancel : Edm.Int32
- ReuseDocumentNum : SAPB1.BoYesNoEnum
- ReuseNotaFiscalNum : SAPB1.BoYesNoEnum
- AutoAddUoM : SAPB1.BoYesNoEnum
- AutoAddPackage : SAPB1.BoYesNoEnum
- DisplayInactivePriceListInReports : SAPB1.BoYesNoEnum
- DisplayInactivePriceListInDocuments : SAPB1.BoYesNoEnum
- DisplayInactivePriceListInSettings : SAPB1.BoYesNoEnum
- ApplyBaseInactiveStatusToSpecialPrices : SAPB1.BoYesNoEnum
- ApplyBaseInactiveStatusToPeriodVolumeDiscounts : SAPB1.BoYesNoEnum
- ApplyBaseInactiveStatusToPriceLists : SAPB1.BoYesNoEnum
- PriceProceedMethod : SAPB1.PriceProceedMethodEnum
- RemoveUpdatePricesBasedOnNonStandardPriceLists : SAPB1.BoYesNoEnum
- SirenNo : Edm.String
- InstitutionCode : Edm.String
- SetResourcesWarehouses : SAPB1.BoYesNoEnum
- BlockStockNegativeQuantity : SAPB1.BoYesNoEnum
- UseParentWIPInComponents : SAPB1.BoYesNoEnum
- EnableUpdateBAPriceAndPlannedAmount : SAPB1.BoYesNoEnum
- AutoAssignOnlyValidAPBA : SAPB1.BoYesNoEnum
- AutoAssignOnlyValidARBA : SAPB1.BoYesNoEnum
- ActionWhenDeviateFromBAForPO : SAPB1.BADivationAlertLevelEnum
- ActionWhenDeviateFromBAForGRPO : SAPB1.BADivationAlertLevelEnum
- ActionWhenDeviateFromBAForAccounting : SAPB1.BADivationAlertLevelEnum
- Series : Edm.Int32
- Account : Edm.String
- EnableMultipleSchedulings : Edm.String
- DisplayBatchQtyUoMBy : SAPB1.DisplayBatchQtyUoMByEnum
- AllowInBoundPostingWithZeroPrice : SAPB1.BoYesNoEnum
- InventoryPostingHighlightVariance : Edm.Double
- InventoryPostingReleaseOnlySerialAndBatch : SAPB1.BoYesNoEnum
- InventoryCountingHighlightVariance : Edm.Double
- InventoryCountingHighlightMaxVariance : Edm.Double
- InventoryCountingHighlightCountersDifference : Edm.Double
- CopySingleCounterToIndividualCounter : SAPB1.BoYesNoEnum
- CloseCountedRowsWithZeroDifference : SAPB1.BoYesNoEnum
- CloseCountedRowsWithoutConfirmation : SAPB1.BoYesNoEnum
- CalculateInWhseQtyBasedOnPostingDate : SAPB1.BoYesNoEnum
- RefreshInWhseQtyInDI : SAPB1.BoYesNoEnum
- SEPACreditorID : Edm.String
- DataOwnershipManageBy : SAPB1.BoDataOwnershipManageMethodEnum
- AllowBPWithNoOwner : SAPB1.BoYesNoEnum
- EnableSeparatePriceMode : SAPB1.BoYesNoEnum
- EnableExternalTax : SAPB1.BoYesNoEnum
- NumberOfCharInMonth : Edm.Int32
- SalesLnWTax : SAPB1.BoYesNoEnum
- SalesPostPaymentCategoryLnWTax : SAPB1.BoYesNoEnum
- SalesApplyExhRatesLnWTax : SAPB1.BoYesNoEnum
- PurchaseLnWTax : SAPB1.BoYesNoEnum
- PurchasePostPaymentCategoryLnWTax : SAPB1.BoYesNoEnum
- PurchaseApplyExhRatesLnWTaxWX : SAPB1.BoYesNoEnum
- UseDefaultPriceList : SAPB1.BoYesNoEnum
- DefaultCustomerPriceList : Edm.Int32
- DefaultVendorPriceList : Edm.Int32
- EORINumber : Edm.String
- CopyAttachmentsFromBaseToTarget : SAPB1.BoYesNoEnum
- CopyAttachmentsFromBOM : SAPB1.BoYesNoEnum
- DontOverwriteAtcWithSameName : SAPB1.BoYesNoEnum
- AttachmentEntryForFileStorage : Edm.Int32
- DontDuplicatwAttachment : SAPB1.BoYesNoEnum
- EnableWebhook : SAPB1.BoYesNoEnum
- MaxNumberOfWebHooks : Edm.Int32
- MessageTTL : Edm.Int32
- WebhookRetryTimes : Edm.Int32
- WebhookRetryInterval : Edm.Int32
- WebhookRequestTimeout : Edm.Int32
- MessageBatchLimit : Edm.Int32
- MessageRetentionTime : Edm.Int32
- ExtendedAdminInfo : SAPB1.ExtendedAdminInfo
- ElectronicReportInfo : SAPB1.ElectronicReportInfo

# SAPB1.AdvancedGLAccountParams (ComplexType)

## Properties

- ItemCode : Edm.String
- Warehouse : Edm.String
- BPCode : Edm.String
- FederalTaxID : Edm.String
- ShipToCountry : Edm.String
- ShipToState : Edm.String
- VatGroup : Edm.String
- PostingDate : Edm.DateTimeOffset
- AccountType : SAPB1.InventoryAccountTypeEnum
- Usage : Edm.Int32
- UDF1 : Edm.String
- UDF2 : Edm.String
- UDF3 : Edm.String
- UDF4 : Edm.String
- UDF5 : Edm.String

# SAPB1.AdvancedGLAccountReturnParams (ComplexType)

## Properties

- AccountCode : Edm.String

# SAPB1.AFEFceActionGetByFceID (ComplexType)

## Properties

- SrcObjType : Edm.String
- DocSubType : Edm.String
- SrcObjAbs : Edm.Int32
- AssignedID : Edm.String
- FCE_ID : Edm.Int32
- FCE_TotalVal : Edm.Double
- FCE_Currency : Edm.String
- FCE_DcApStat : Edm.String
- ActStatus : SAPB1.EcmActionStatusEnum
- FCE_DocType : Edm.Int32
- FCE_POI : Edm.String
- FCE_Folio : Edm.Int32
- FCE_RjRsnCod : Edm.String
- FCE_RjRsnDes : Edm.String
- GUID : Edm.String
- AbsEntry : Edm.Int32

# SAPB1.AFEFceActionGetPaymentData (ComplexType)

## Properties

- DocEntry : Edm.Int32
- CashSum : Edm.Double
- CreditSum : Edm.Double
- CheckSum : Edm.Double
- TrsfrSum : Edm.Double
- DocRate : Edm.Double

# SAPB1.AFEFceAPCheckECM2Entry (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- GUID : Edm.String
- Code : Edm.String

# SAPB1.AFEFceAPCheckECM2EntryParams (ComplexType)

## Properties

- assignedID : Edm.String
- docType : Edm.Int32
- poi : Edm.String
- folio : Edm.Int32

# SAPB1.AFEFceAPGetLatestAFIPDate (ComplexType)

## Properties

- max_FCE_DocDate : Edm.DateTimeOffset

# SAPB1.AFEFceARGetDateFromTo (ComplexType)

## Properties

- DateFrom : Edm.DateTimeOffset
- DateTo : Edm.DateTimeOffset

# SAPB1.AFEFceARGetDocuments (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- DocEntry : Edm.Int32
- ObjType : Edm.String
- DocSubType : Edm.String
- EDocType : Edm.String
- PTICode : Edm.String
- Letter : Edm.String
- FolNumFrom : Edm.Int32
- GUID : Edm.String

# SAPB1.AFEFceID (ComplexType)

## Properties

- FceID : Edm.Int32

# SAPB1.AFERenumberFolioParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- NewFolioNumber : Edm.Int32

# SAPB1.AFEUpdFceAPARGetDocuments (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- GUID : Edm.String
- ActType : Edm.Int32
- ActStatus : Edm.String
- FCE_DcApStat : Edm.String
- FCE_ApprStat : Edm.String
- FCE_ID : Edm.Int32
- FCE_DocType : Edm.Int32
- FCE_POI : Edm.String
- FCE_Folio : Edm.Int32
- UpdateDate : Edm.DateTimeOffset
- UpdateTS : Edm.Int32
- isAP : Edm.String

# SAPB1.AlertManagement (EntityType)

OpenType: true
Key: Code

## Properties

- Code : Edm.Int32 [required]
- Name : Edm.String
- Type : SAPB1.AlertManagementTypeEnum
- Priority : SAPB1.AlertManagementPriorityEnum
- Active : SAPB1.BoYesNoEnum
- Param : Edm.String
- QueryID : Edm.Int32
- FrequencyType : SAPB1.AlertManagementFrequencyType
- DayOfExecution : Edm.Int32
- ExecutionTime : Edm.TimeOfDay
- LastExecutionDate : Edm.DateTimeOffset
- LastExecutionTime : Edm.Int32
- NextExecutionDate : Edm.DateTimeOffset
- NextExecutionTime : Edm.TimeOfDay
- SaveHistory : SAPB1.BoYesNoEnum
- FrequencyInterval : Edm.Int32
- AlertManagementRecipients : Collection(SAPB1.AlertManagementRecipient)
- AlertManagementDocuments : Collection(SAPB1.AlertManagementDocument)

# SAPB1.AlertManagementDocument (ComplexType)

## Properties

- Document : SAPB1.AlertManagementDocumentEnum
- Active : SAPB1.BoYesNoEnum

# SAPB1.AlertManagementParams (ComplexType)

## Properties

- Code : Edm.Int32
- Type : SAPB1.AlertManagementTypeEnum
- Name : Edm.String

# SAPB1.AlertManagementRecipient (ComplexType)

## Properties

- UserCode : Edm.Int32
- SendEMail : SAPB1.BoYesNoEnum
- SendSMS : SAPB1.BoYesNoEnum
- SendFax : SAPB1.BoYesNoEnum
- SendInternal : SAPB1.BoYesNoEnum

# SAPB1.AlternateCatNum (EntityType)

OpenType: true
Key: ItemCode, CardCode, Substitute

## Properties

- ItemCode : Edm.String [required]
- CardCode : Edm.String [required]
- Substitute : Edm.String [required]
- DisplayBPCatalogNumber : SAPB1.BoYesNoEnum
- IsDefault : SAPB1.BoYesNoEnum
- Description : Edm.String

## Navigation properties

- Item : SAPB1.Item [Partner=AlternateCatNum]
- BusinessPartner : SAPB1.BusinessPartner [Partner=AlternateCatNum]

# SAPB1.AlternateCatNumParams (ComplexType)

## Properties

- ItemCode : Edm.String
- CardCode : Edm.String
- Substitute : Edm.String

# SAPB1.AlternativeItem (ComplexType)

## Properties

- AlternativeItemCode : Edm.String
- MatchFactor : Edm.Double
- Remarks : Edm.String

# SAPB1.ApprovalRequest (EntityType)

Key: Code

## Properties

- Code : Edm.Int32 [required]
- ApprovalTemplatesID : Edm.Int32
- ObjectType : Edm.String
- IsDraft : Edm.String
- ObjectEntry : Edm.Int32
- Status : SAPB1.BoApprovalRequestStatusEnum
- Remarks : Edm.String
- CurrentStage : Edm.Int32
- OriginatorID : Edm.Int32
- CreationDate : Edm.DateTimeOffset
- CreationTime : Edm.TimeOfDay
- DraftEntry : Edm.Int32
- DraftType : Edm.String
- ApprovalRequestLines : Collection(SAPB1.ApprovalRequestLine)
- ApprovalRequestDecisions : Collection(SAPB1.ApprovalRequestDecision)

## Navigation properties

- ApprovalTemplate : SAPB1.ApprovalTemplate [Partner=ApprovalRequests]
- ApprovalStage : SAPB1.ApprovalStage [Partner=ApprovalRequests]
- User : SAPB1.User [Partner=ApprovalRequests]

# SAPB1.ApprovalRequestDecision (ComplexType)

## Properties

- ApproverUserName : Edm.String
- ApproverPassword : Edm.String
- Status : SAPB1.BoApprovalRequestDecisionEnum
- Remarks : Edm.String

# SAPB1.ApprovalRequestLine (ComplexType)

## Properties

- StageCode : Edm.Int32
- UserID : Edm.Int32
- Status : SAPB1.BoApprovalRequestDecisionEnum
- Remarks : Edm.String
- UpdateDate : Edm.DateTimeOffset
- UpdateTime : Edm.TimeOfDay
- CreationDate : Edm.DateTimeOffset
- CreationTime : Edm.TimeOfDay

# SAPB1.ApprovalRequestParams (ComplexType)

## Properties

- Code : Edm.Int32
- Remarks : Edm.String
- Status : SAPB1.BoApprovalRequestStatusEnum

# SAPB1.ApprovalStage (EntityType)

Key: Code

## Properties

- Code : Edm.Int32 [required]
- Name : Edm.String
- NoOfApproversRequired : Edm.Int32
- Remarks : Edm.String
- ApprovalStageApprovers : Collection(SAPB1.ApprovalStageApprover)

## Navigation properties

- ApprovalRequests : Collection(SAPB1.ApprovalRequest) [Partner=ApprovalStage]

# SAPB1.ApprovalStageApprover (ComplexType)

## Properties

- UserID : Edm.Int32

# SAPB1.ApprovalStageParams (ComplexType)

## Properties

- Code : Edm.Int32
- Name : Edm.String

# SAPB1.ApprovalTemplate (EntityType)

Key: Code

## Properties

- Code : Edm.Int32 [required]
- Name : Edm.String
- Remarks : Edm.String
- UseTerms : SAPB1.BoYesNoEnum
- IsActive : SAPB1.BoYesNoEnum
- IsActiveWhenUpdatingDocuments : SAPB1.BoYesNoEnum
- ApprovalTemplateUsers : Collection(SAPB1.ApprovalTemplateUser)
- ApprovalTemplateStages : Collection(SAPB1.ApprovalTemplateStage)
- ApprovalTemplateDocuments : Collection(SAPB1.ApprovalTemplateDocument)
- ApprovalTemplateTerms : Collection(SAPB1.ApprovalTemplateTerm)
- ApprovalTemplateQueries : Collection(SAPB1.ApprovalTemplateQuery)

## Navigation properties

- ApprovalRequests : Collection(SAPB1.ApprovalRequest) [Partner=ApprovalTemplate]

# SAPB1.ApprovalTemplateDocument (ComplexType)

## Properties

- DocumentType : SAPB1.ApprovalTemplatesDocumentTypeEnum

# SAPB1.ApprovalTemplateParams (ComplexType)

## Properties

- Code : Edm.Int32
- Name : Edm.String

# SAPB1.ApprovalTemplateQuery (ComplexType)

## Properties

- QueryID : Edm.Int32

# SAPB1.ApprovalTemplateStage (ComplexType)

## Properties

- SortID : Edm.Int32
- ApprovalStageCode : Edm.Int32
- Remarks : Edm.String

# SAPB1.ApprovalTemplateTerm (ComplexType)

## Properties

- ConditionType : SAPB1.ApprovalTemplateConditionTypeEnum
- OperationType : SAPB1.ApprovalTemplateOperationTypeEnum
- Value : Edm.String

# SAPB1.ApprovalTemplateUser (ComplexType)

## Properties

- UserID : Edm.Int32

# SAPB1.AssetClass (EntityType)

Key: Code

## Properties

- Code : Edm.String [required]
- Description : Edm.String
- AssetType : SAPB1.AssetTypeEnum
- ValueLimitFrom : Edm.Double
- ValueLimitTo : Edm.Double
- BPLID : Edm.Int32
- AttributeGroup : Edm.Int32
- AssetClassCollection : Collection(SAPB1.AssetClassLine)

## Navigation properties

- BusinessPlace : SAPB1.BusinessPlace [Partner=AssetClasses]
- AttributeGroup2 : SAPB1.AttributeGroup [Partner=AssetClasses]
- Items : Collection(SAPB1.Item) [Partner=AssetClass2]

# SAPB1.AssetClassLine (ComplexType)

## Properties

- Code : Edm.String
- LineNumber : Edm.Int32
- DepreciationAreaID : Edm.String
- ActiveStatus : SAPB1.BoYesNoEnum
- AccountDetermination : Edm.String
- DepreciationTypeID : Edm.String
- UseLife : Edm.Int32

# SAPB1.AssetClassParams (ComplexType)

## Properties

- Code : Edm.String
- Description : Edm.String

# SAPB1.AssetDepreciationGroup (EntityType)

Key: Code

## Properties

- Code : Edm.String [required]
- Description : Edm.String
- Group : Edm.String

## Navigation properties

- Items : Collection(SAPB1.Item) [Partner=AssetDepreciationGroup]

# SAPB1.AssetDepreciationGroupParams (ComplexType)

## Properties

- Code : Edm.String
- Description : Edm.String

# SAPB1.AssetDocument (EntityType)

OpenType: true
Key: DocEntry

## Properties

- DocEntry : Edm.Int32 [required]
- DocNum : Edm.Int32
- Series : Edm.Int32
- PostingDate : Edm.DateTimeOffset
- DocumentDate : Edm.DateTimeOffset
- Status : SAPB1.AssetDocumentStatusEnum
- Remarks : Edm.String
- Reference : Edm.String
- Currency : Edm.String
- DocumentRate : Edm.Double
- DocumentTotal : Edm.Double
- DocumentTotalFC : Edm.Double
- DocumentTotalSC : Edm.Double
- AssetValueDate : Edm.DateTimeOffset
- DocumentType : SAPB1.AssetDocumentTypeEnum
- SummerizeByProjects : SAPB1.BoYesNoEnum
- SummerizeByDistributionRules : SAPB1.BoYesNoEnum
- ManualDepreciationType : Edm.String
- HandWritten : SAPB1.BoYesNoEnum
- CancellationDate : Edm.DateTimeOffset
- DepreciationArea : Edm.String
- BPLId : Edm.Int32
- Origin : Edm.Int32
- LowValueAssetRetirement : SAPB1.BoYesNoEnum
- CancellationOption : SAPB1.ClosingOptionEnum
- OriginalType : SAPB1.AssetOriginalTypeEnum
- BaseReference : Edm.String
- BPLName : Edm.String
- VATRegNum : Edm.String
- AssetDocumentLineCollection : Collection(SAPB1.AssetDocumentLine)
- AssetDocumentAreaJournalCollection : Collection(SAPB1.AssetDocumentAreaJournal)
- PTICode : Edm.String
- Letter : Edm.String
- FolNumFrom : Edm.Int32
- FolNumTo : Edm.Int32
- AssetDocumentNewLocCollection : Collection(SAPB1.AssetDocumentNewLoc)

## Navigation properties

- Currency2 : SAPB1.Currency [Partner=AssetRetirement]
- DepreciationType : SAPB1.DepreciationType [Partner=AssetRetirement]
- DepreciationArea2 : SAPB1.DepreciationArea [Partner=AssetRetirement]
- BusinessPlace : SAPB1.BusinessPlace [Partner=AssetRetirement]

# SAPB1.AssetDocumentAreaJournal (ComplexType)

## Properties

- DocEntry : Edm.Int32
- LineNumber : Edm.Int32
- DepreciationArea : Edm.String
- JournalRemarks : Edm.String
- TransactionNumber : Edm.Int32
- CancellationJournalRemarks : Edm.String
- CancellationTransactionNumber : Edm.Int32

# SAPB1.AssetDocumentLine (ComplexType)

OpenType: true

## Properties

- DocEntry : Edm.Int32
- LineNumber : Edm.Int32
- AssetNumber : Edm.String
- GLAccount : Edm.String
- Quantity : Edm.Double
- TotalLC : Edm.Double
- TotalFC : Edm.Double
- TotalSC : Edm.Double
- DepreciationArea : Edm.String
- Remarks : Edm.String
- NewAssetNumber : Edm.String
- Partial : SAPB1.BoYesNoEnum
- APC : Edm.Double
- NewAssetClass : Edm.String
- DistributionRule : Edm.String
- DistributionRule2 : Edm.String
- DistributionRule3 : Edm.String
- DistributionRule4 : Edm.String
- DistributionRule5 : Edm.String
- Project : Edm.String

# SAPB1.AssetDocumentNewLoc (ComplexType)

## Properties

- DocEntry : Edm.Int32
- LineNumber : Edm.Int32
- AssetNumber : Edm.String
- CurLocation : Edm.Int32
- NewLocation : Edm.Int32
- NBV : Edm.Double
- Quantity : Edm.Double

# SAPB1.AssetDocumentParams (ComplexType)

## Properties

- DocEntry : Edm.Int32
- CancellationOption : SAPB1.ClosingOptionEnum
- CancellationDate : Edm.DateTimeOffset

# SAPB1.AssetGroup (EntityType)

Key: Code

## Properties

- Code : Edm.String [required]
- Description : Edm.String

## Navigation properties

- Items : Collection(SAPB1.Item) [Partner=AssetGroup2]

# SAPB1.AssetGroupParams (ComplexType)

## Properties

- Code : Edm.String
- Description : Edm.String

# SAPB1.AssetRevaluation (EntityType)

Key: DocEntry

## Properties

- DocEntry : Edm.Int32 [required]
- DocNum : Edm.Int32
- Series : Edm.Int32
- PostingDate : Edm.DateTimeOffset
- AssetValueDate : Edm.DateTimeOffset
- Reference : Edm.String
- Remarks : Edm.String
- JournalRemarks : Edm.String
- DepreciationArea : Edm.String
- TransId : Edm.Int32
- HandWritten : SAPB1.BoYesNoEnum
- PeriodIndicator : Edm.String
- DocumentDate : Edm.DateTimeOffset
- BPLId : Edm.Int32
- BPLName : Edm.String
- VATRegNum : Edm.String
- RevaluationPercent : Edm.Double
- IfrsPosting : SAPB1.BoYesNoEnum
- SummerizeByProjects : SAPB1.BoYesNoEnum
- SummerizeByDistributionRules : SAPB1.BoYesNoEnum
- AssetRevaluationLineCollection : Collection(SAPB1.AssetRevaluationLine)

## Navigation properties

- DepreciationArea2 : SAPB1.DepreciationArea [Partner=AssetRevaluations]
- JournalEntry : SAPB1.JournalEntry [Partner=AssetRevaluations]
- BusinessPlace : SAPB1.BusinessPlace [Partner=AssetRevaluations]

# SAPB1.AssetRevaluationLine (ComplexType)

## Properties

- DocEntry : Edm.Int32
- LineNumber : Edm.Int32
- AssetNumber : Edm.String
- CurrentNBV : Edm.Double
- NewNBV : Edm.Double
- Remarks : Edm.String
- RevaluationPercent : Edm.Double
- DistributionRule : Edm.String
- DistributionRule2 : Edm.String
- DistributionRule3 : Edm.String
- DistributionRule4 : Edm.String
- DistributionRule5 : Edm.String
- Project : Edm.String

# SAPB1.AssetRevaluationParams (ComplexType)

## Properties

- DocEntry : Edm.Int32

# SAPB1.Attachments2 (EntityType)

OpenType: true
HasStream: true
Key: AbsoluteEntry

## Properties

- AbsoluteEntry : Edm.Int32 [required]
- Attachments2_Lines : Collection(SAPB1.Attachments2_Line)

## Navigation properties

- InventoryPostings : Collection(SAPB1.InventoryPosting) [Partner=Attachments2]
- Deposits : Collection(SAPB1.Deposit) [Partner=Attachments2]
- VendorPayments : Collection(SAPB1.Payment) [Partner=Attachments2]
- ProductionOrders : Collection(SAPB1.ProductionOrder) [Partner=Attachments2]
- PaymentDrafts : Collection(SAPB1.Payment) [Partner=Attachments2]
- BlanketAgreements : Collection(SAPB1.BlanketAgreement) [Partner=Attachments2]
- Campaigns : Collection(SAPB1.Campaign) [Partner=Attachments2]
- InventoryCountings : Collection(SAPB1.InventoryCounting) [Partner=Attachments2]
- InventoryCountingDrafts : Collection(SAPB1.InventoryCountingDraft) [Partner=Attachments2]
- InventoryPostingDrafts : Collection(SAPB1.InventoryPostingDraft) [Partner=Attachments2]
- InventoryOpeningBalances : Collection(SAPB1.InventoryOpeningBalance) [Partner=Attachments2]
- CustomerEquipmentCards : Collection(SAPB1.CustomerEquipmentCard) [Partner=Attachments2]
- ServiceContracts : Collection(SAPB1.ServiceContract) [Partner=Attachments2]
- ProjectManagements : Collection(SAPB1.PM_ProjectDocumentData) [Partner=Attachments2]
- ProjectManagementTimeSheet : Collection(SAPB1.PM_TimeSheetData) [Partner=Attachments2]
- JournalEntries : Collection(SAPB1.JournalEntry) [Partner=Attachments2]
- IncomingPayments : Collection(SAPB1.Payment) [Partner=Attachments2]
- ChecksforPayment : Collection(SAPB1.ChecksforPayment) [Partner=Attachments2]
- ProductTrees : Collection(SAPB1.ProductTree) [Partner=Attachments2]

# SAPB1.Attachments2_Line (ComplexType)

OpenType: true

## Properties

- AbsoluteEntry : Edm.Int32
- LineNum : Edm.Int32
- SourcePath : Edm.String
- FileName : Edm.String
- FileExtension : Edm.String
- AttachmentDate : Edm.DateTimeOffset
- UserID : Edm.Int32
- Override : SAPB1.BoYesNoEnum
- FreeText : Edm.String
- CopyToTargetDoc : SAPB1.BoYesNoEnum
- CopyToProductionOrder : SAPB1.BoYesNoEnum
- EDocSign : SAPB1.BoYesNoEnum
- TargetPath : Edm.String
- SubPath : Edm.String
- SendInMail : SAPB1.BoYesNoEnum
- FileSize : Edm.Int32
- CopyFile : Edm.String
- FileSuffix : SAPB1.BoYesNoEnum

# SAPB1.Attachments2Params (ComplexType)

## Properties

- AbsoluteEntry : Edm.Int32

# SAPB1.AttributeGroup (EntityType)

Key: Code

## Properties

- Code : Edm.Int32 [required]
- Name : Edm.String
- Locked : SAPB1.BoYesNoEnum
- AttributeGroupCollection : Collection(SAPB1.AttributeGroupLine)

## Navigation properties

- AssetClasses : Collection(SAPB1.AssetClass) [Partner=AttributeGroup2]

# SAPB1.AttributeGroupLine (ComplexType)

## Properties

- Code : Edm.Int32
- SortNumber : Edm.Int32
- AttributeID : Edm.Int32
- AttributeName : Edm.String
- FieldType : SAPB1.AttributeGroupFieldTypeEnum
- DefaultValue : Edm.String

# SAPB1.AttributeGroupParams (ComplexType)

## Properties

- Code : Edm.Int32
- Name : Edm.String

# SAPB1.AutoDistributionRuleLine (ComplexType)

## Properties

- LocationCode : Edm.Int32
- TaxAccount : Edm.String
- AllocatePercent : Edm.Double

# SAPB1.B1Session (EntityType)

Key: SessionId

## Properties

- Version : Edm.String
- SessionTimeout : Edm.Int32
- SessionId : Edm.String [required]

# SAPB1.Bank (EntityType)

OpenType: true
Key: AbsoluteEntry

## Properties

- BankCode : Edm.String
- BankName : Edm.String
- AccountforOutgoingChecks : Edm.String
- BranchforOutgoingChecks : Edm.String
- NextCheckNumber : Edm.Int32
- SwiftNo : Edm.String
- IBAN : Edm.String
- CountryCode : Edm.String
- PostOffice : SAPB1.BoYesNoEnum
- AbsoluteEntry : Edm.Int32 [required]
- DefaultBankAccountKey : Edm.Int32
- DigitalPayments : SAPB1.BoYesNoEnum

## Navigation properties

- HouseBankAccounts : Collection(SAPB1.HouseBankAccount) [Partner=Bank]
- EmployeesInfo : Collection(SAPB1.EmployeeInfo) [Partner=Bank]
- Country : SAPB1.Country [Partner=Banks]

# SAPB1.BankChargesAllocationCode (EntityType)

Key: Code

## Properties

- Code : Edm.String [required]
- Description : Edm.String

## Navigation properties

- PaymentRunExport : Collection(SAPB1.PaymentRunExport) [Partner=BankChargesAllocationCode]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=BankChargesAllocationCode2]

# SAPB1.BankChargesAllocationCodeParams (ComplexType)

## Properties

- Code : Edm.String
- Description : Edm.String

# SAPB1.BankPage (EntityType)

OpenType: true
Key: AccountCode, Sequence
Filtered properties: 9

## Properties

- AccountCode : Edm.String [required]
- Sequence : Edm.Int32 [required]
- AccountName : Edm.String
- Reference : Edm.String
- DueDate : Edm.DateTimeOffset
- Memo : Edm.String
- DebitAmount : Edm.Double
- CreditAmount : Edm.Double
- BankMatch : Edm.Int32
- DataSource : Edm.String
- UserSignature : Edm.Int32
- ExternalCode : Edm.String
- CardCode : Edm.String
- CardName : Edm.String
- StatementNumber : Edm.Int32
- InvoiceNumber : Edm.String
- PaymentCreated : SAPB1.BoYesNoEnum
- VisualOrder : Edm.Int32
- DocNumberType : SAPB1.BoBpsDocTypes
- PaymentReference : Edm.String
- InvoiceNumberEx : Edm.String
- BICSwiftCode : Edm.String

## Navigation properties

- ChartOfAccount : SAPB1.ChartOfAccount [Partner=BankPages]
- User : SAPB1.User [Partner=BankPages]
- BusinessPartner : SAPB1.BusinessPartner [Partner=BankPages]

# SAPB1.BankPageParams (ComplexType)

## Properties

- AccountCode : Edm.String
- Sequence : Edm.Int32

# SAPB1.BankParams (ComplexType)

## Properties

- AbsoluteEntry : Edm.Int32

# SAPB1.BankStatement (EntityType)

Key: InternalNumber

## Properties

- InternalNumber : Edm.Int32 [required]
- BankAccountKey : Edm.Int32
- StatementNumber : Edm.String
- StatementDate : Edm.DateTimeOffset
- Status : SAPB1.BankStatementStatusEnum
- Imported : SAPB1.BoYesNoEnum
- StartingBalanceF : Edm.Double
- EndingBalanceF : Edm.Double
- Currency : Edm.String
- StartingBalanceL : Edm.Double
- EndingBalanceL : Edm.Double
- BankStatementFileHash : Edm.String
- BankStatementGUID : Edm.String
- BankStatementRows : Collection(SAPB1.BankStatementRow)

## Navigation properties

- HouseBankAccount : SAPB1.HouseBankAccount [Partner=BankStatements]
- Currency2 : SAPB1.Currency [Partner=BankStatements]

# SAPB1.BankStatementParams (ComplexType)

## Properties

- InternalNumber : Edm.Int32
- BankAccountKey : Edm.Int32
- StatementNumber : Edm.String
- StatementDate : Edm.DateTimeOffset
- Status : SAPB1.BankStatementStatusEnum
- Imported : SAPB1.BoYesNoEnum
- StartingBalanceF : Edm.Double
- EndingBalanceF : Edm.Double
- Currency : Edm.String
- StartingBalanceL : Edm.Double
- EndingBalanceL : Edm.Double

# SAPB1.BankStatementRow (ComplexType)

OpenType: true
Filtered properties: 9

## Properties

- ExternalBankStatementNo : Edm.Int32
- AccountNumber : Edm.String
- SequenceNo : Edm.Int32
- AccountName : Edm.String
- Reference : Edm.String
- DueDate : Edm.DateTimeOffset
- Details : Edm.String
- DebitAmountFC : Edm.Double
- CreditAmountFC : Edm.Double
- CreditCurrency : Edm.String
- Balance : Edm.Double
- ReconciliationNo : Edm.Int32
- ExternalCode : Edm.String
- BPCode : Edm.String
- BPName : Edm.String
- StatementNumber : Edm.Int32
- RowStatus : Edm.String
- VisualOrder : Edm.Int32
- DocNumType : SAPB1.BoBpsDocTypes
- Details2 : Edm.String
- PaymentReferenceNo : Edm.String
- CreateMethod : SAPB1.CreateMethodEnum
- BankStmtLineDate : Edm.DateTimeOffset
- BankStmtDueDate : Edm.DateTimeOffset
- InternalBankOpCode : Edm.Int32
- BPBankAccount : Edm.String
- DebitAmountLC : Edm.Double
- CreditAmountLC : Edm.Double
- ExchangeRate : Edm.Double
- IBANofBPBankAccount : Edm.String
- FeeOnTheLine : Edm.Double
- VATAmountLC : Edm.Double
- VATAmountFC : Edm.Double
- JournalEntryID : Edm.Int32
- PaymentID : Edm.Int32
- DocumentType : SAPB1.BankStatementDocTypeEnum
- PostingMethod : SAPB1.PostingMethodEnum
- GLAccountforFee : Edm.String
- FeeProfitCenter : Edm.String
- FeeProject : Edm.String
- BPBankCode : Edm.String
- FeeDistributionRule : Edm.String
- FeeDistributionRule2 : Edm.String
- FeeDistributionRule3 : Edm.String
- FeeDistributionRule4 : Edm.String
- FeeDistributionRule5 : Edm.String
- BPBICSwiftCode : Edm.String
- Source : SAPB1.BankStatementRowSourceEnum
- FolioPrefixString : Edm.String
- FolioNumber : Edm.Int32
- MultiplePayments : Collection(SAPB1.MultiplePayment)

# SAPB1.BankStatementsFilter (ComplexType)

## Properties

- Country : Edm.String
- Bank : Edm.String
- Account : Edm.String

# SAPB1.BarCode (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- ItemNo : Edm.String
- UoMEntry : Edm.Int32
- Barcode : Edm.String
- FreeText : Edm.String

## Navigation properties

- Item : SAPB1.Item [Partner=BarCodes]
- UnitOfMeasurement : SAPB1.UnitOfMeasurement [Partner=BarCodes]

# SAPB1.BarCodeParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- ItemNo : Edm.String
- UoMEntry : Edm.Int32
- Barcode : Edm.String

# SAPB1.BatchNumber (ComplexType)

OpenType: true
Filtered properties: 29

## Properties

- BatchNumberProperty : Edm.String
- ManufacturerSerialNumber : Edm.String
- InternalSerialNumber : Edm.String
- ExpiryDate : Edm.DateTimeOffset
- ManufacturingDate : Edm.DateTimeOffset
- AddmisionDate : Edm.DateTimeOffset
- Location : Edm.String
- Notes : Edm.String
- Quantity : Edm.Double
- BaseLineNumber : Edm.Int32
- TrackingNote : Edm.Int32
- TrackingNoteLine : Edm.Int32
- ItemCode : Edm.String
- SystemSerialNumber : Edm.Int32

# SAPB1.BatchNumberDetail (EntityType)

OpenType: true
Key: DocEntry
Filtered properties: 29

## Properties

- DocEntry : Edm.Int32 [required]
- ItemCode : Edm.String
- ItemDescription : Edm.String
- Status : SAPB1.BatchDetailServiceStatusEnum
- Batch : Edm.String
- BatchAttribute1 : Edm.String
- BatchAttribute2 : Edm.String
- AdmissionDate : Edm.DateTimeOffset
- ManufacturingDate : Edm.DateTimeOffset
- ExpirationDate : Edm.DateTimeOffset
- Details : Edm.String
- SystemNumber : Edm.Int32

## Navigation properties

- Item : SAPB1.Item [Partner=BatchNumberDetails]

# SAPB1.BatchNumberDetailParams (ComplexType)

## Properties

- DocEntry : Edm.Int32

# SAPB1.BEMReplicationPeriod (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- ScopeKey : Edm.String
- ScopeName : Edm.String
- Periodic : SAPB1.BEMPeriodicTypeEnum
- StartDate : Edm.DateTimeOffset
- Status : SAPB1.BEMReplicationStatusEnum
- UpdateDate : Edm.DateTimeOffset
- LastRepId : Edm.String
- RepMessage : Edm.String

# SAPB1.BEMReplicationPeriodParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32

# SAPB1.BillOfExchange (ComplexType)

OpenType: true

## Properties

- BillOfExchangeNo : Edm.Int32
- BillOfExchangeDueDate : Edm.DateTimeOffset
- Details : Edm.String
- ReferenceNo : Edm.String
- Remarks : Edm.String
- PaymentMethodCode : Edm.String
- BPBankCode : Edm.String
- BPBankAct : Edm.String
- BPBankCountry : Edm.String
- ControlKey : Edm.String
- PaymentEngineStatus1 : Edm.String
- PaymentEngineStatus2 : Edm.String
- PaymentEngineStatus3 : Edm.String
- StampTaxCode : Edm.String
- StampTaxAmount : Edm.Double
- FolioNumber : Edm.Int32
- FolioPrefixString : Edm.String
- InterestAmount : Edm.Double
- DiscountAmount : Edm.Double
- FineAmount : Edm.Double
- InterestDate : Edm.DateTimeOffset
- DiscountDate : Edm.DateTimeOffset
- FineDate : Edm.DateTimeOffset
- IOFAmount : Edm.Double
- ServiceFeeAmount : Edm.Double
- OtherExpensesAmount : Edm.Double
- OtherIncomesAmount : Edm.Double
- LastPageFolioNumber : Edm.Int32

# SAPB1.BillOfExchangeTransaction (EntityType)

OpenType: true
Key: BOETransactionkey

## Properties

- StatusFrom : SAPB1.BoBOTFromStatus
- StatusTo : SAPB1.BoBOTToStatus
- TransactionDate : Edm.DateTimeOffset
- TransactionTime : Edm.TimeOfDay
- IsBoeReconciled : SAPB1.BoYesNoEnum
- TransactionNumber : Edm.Int32
- PostingDate : Edm.DateTimeOffset
- TaxDate : Edm.DateTimeOffset
- BOETransactionkey : Edm.Int32 [required]
- BillOfExchangeTransactionLines : Collection(SAPB1.BillOfExchangeTransactionLine)
- BillOfExchangeTransDeposits : Collection(SAPB1.BillOfExchangeTransDeposit)
- BillOfExchangeTransBankPages : Collection(SAPB1.BillOfExchangeTransBankPage)

## Navigation properties

- JournalEntry : SAPB1.JournalEntry [Partner=BillOfExchangeTransactions]

# SAPB1.BillOfExchangeTransactionLine (ComplexType)

OpenType: true

## Properties

- BillOfExchangeNo : Edm.Int32
- BillOfExchangeType : SAPB1.BoBOETypes
- BillOfExchangeDueDate : Edm.DateTimeOffset

# SAPB1.BillOfExchangeTransactionParams (ComplexType)

## Properties

- BOETransactionkey : Edm.Int32

# SAPB1.BillOfExchangeTransBankPage (ComplexType)

OpenType: true
Filtered properties: 9

## Properties

- AccountCode : Edm.String
- Sequence : Edm.Int32

# SAPB1.BillOfExchangeTransDeposit (ComplexType)

OpenType: true

## Properties

- DepositNorm : Edm.String
- PostingType : SAPB1.BoDepositPostingTypes
- BankCountry : Edm.String
- BankAccount : Edm.String
- BankDepositAccount : Edm.String
- BankBranch : Edm.String

# SAPB1.BinLocation (EntityType)

OpenType: true
Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- Warehouse : Edm.String
- Sublevel1 : Edm.String
- Sublevel2 : Edm.String
- Sublevel3 : Edm.String
- Sublevel4 : Edm.String
- BinCode : Edm.String
- Inactive : SAPB1.BoYesNoEnum
- Description : Edm.String
- AlternativeSortCode : Edm.String
- BarCode : Edm.String
- Attribute1 : Edm.String
- Attribute2 : Edm.String
- Attribute3 : Edm.String
- Attribute4 : Edm.String
- Attribute5 : Edm.String
- Attribute6 : Edm.String
- Attribute7 : Edm.String
- Attribute8 : Edm.String
- Attribute9 : Edm.String
- Attribute10 : Edm.String
- RestrictedItemType : SAPB1.BinRestrictItemEnum
- SpecificItem : Edm.String
- SpecificItemGroup : Edm.Int32
- BatchRestrictions : SAPB1.BinRestrictionBatchEnum
- RestrictedTransType : SAPB1.BinRestrictTransactionEnum
- RestrictionReason : Edm.String
- DateRestrictionChanged : Edm.DateTimeOffset
- MinimumQty : Edm.Double
- MaximumQty : Edm.Double
- IsSystemBin : SAPB1.BoYesNoEnum
- ReceivingBinLocation : SAPB1.BoYesNoEnum
- ExcludeAutoAllocOnIssue : SAPB1.BoYesNoEnum
- MaximumWeight : Edm.Double
- MaximumWeight1 : Edm.Double
- MaximumWeightUnit : Edm.Int32
- MaximumWeightUnit1 : Edm.Int32
- RestrictedUoMType : SAPB1.BinRestrictUoMEnum
- SpecificUoM : Edm.Int32
- SpecificUoMGroup : Edm.Int32

## Navigation properties

- Warehouse2 : SAPB1.Warehouse [Partner=BinLocations]
- Item : SAPB1.Item [Partner=BinLocations]
- ItemGroups : SAPB1.ItemGroups [Partner=BinLocations]
- WeightMeasure : SAPB1.WeightMeasure [Partner=BinLocations]
- UnitOfMeasurement : SAPB1.UnitOfMeasurement [Partner=BinLocations]
- UnitOfMeasurementGroup : SAPB1.UnitOfMeasurementGroup [Partner=BinLocations]
- Warehouses : Collection(SAPB1.Warehouse) [Partner=BinLocation]

# SAPB1.BinLocationAttribute (EntityType)

Key: AbsEntry

## Properties

- Attribute : Edm.Int32
- Code : Edm.String
- AbsEntry : Edm.Int32 [required]

## Navigation properties

- BinLocationField : SAPB1.BinLocationField [Partner=BinLocationAttributes]

# SAPB1.BinLocationAttributeParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- Attribute : Edm.Int32
- Code : Edm.String

# SAPB1.BinLocationField (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- FieldType : SAPB1.BinLocationFieldTypeEnum
- FieldNumber : Edm.Int32
- Name : Edm.String
- Activated : SAPB1.BoYesNoEnum
- DefaultFieldName : Edm.String

## Navigation properties

- BinLocationAttributes : Collection(SAPB1.BinLocationAttribute) [Partner=BinLocationField]
- WarehouseSublevelCodes : Collection(SAPB1.WarehouseSublevelCode) [Partner=BinLocationField]

# SAPB1.BinLocationFieldParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32

# SAPB1.BinLocationParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- BinCode : Edm.String

# SAPB1.BlanketAgreement (EntityType)

OpenType: true
Key: AgreementNo
Filtered properties: 23

## Properties

- AgreementNo : Edm.Int32 [required]
- BPCode : Edm.String
- BPName : Edm.String
- ContactPersonCode : Edm.Int32
- StartDate : Edm.DateTimeOffset
- EndDate : Edm.DateTimeOffset
- TerminateDate : Edm.DateTimeOffset
- Description : Edm.String
- AgreementType : SAPB1.BlanketAgreementTypeEnum
- Status : SAPB1.BlanketAgreementStatusEnum
- Owner : Edm.Int32
- IgnorePricesInAgreement : SAPB1.BoYesNoEnum
- Renewal : SAPB1.BoYesNoEnum
- RemindUnit : SAPB1.BoRemindUnits
- RemindTime : Edm.Int32
- Remarks : Edm.String
- AttachmentEntry : Edm.Int32
- SettlementProbability : Edm.Double
- AgreementMethod : SAPB1.BlanketAgreementMethodEnum
- PaymentTerms : Edm.Int32
- PriceList : Edm.Int32
- SigningDate : Edm.DateTimeOffset
- AmendmentTo : Edm.Int32
- Series : Edm.Int32
- DocNum : Edm.Int32
- HandWritten : SAPB1.BoYesNoEnum
- PeriodIndicator : Edm.String
- PaymentMethod : Edm.String
- ExchangeRate : Edm.Double
- ShippingType : Edm.Int32
- NumAtCard : Edm.String
- Project : Edm.String
- PriceMode : SAPB1.PriceModeEnum
- BPCurrency : Edm.String
- BPType : SAPB1.BlanketAgreementBPTypeEnum
- SAPPassport : Edm.String
- BlanketAgreements_ItemsLines : Collection(SAPB1.BlanketAgreements_ItemsLine)

## Navigation properties

- VendorPayments : Collection(SAPB1.Payment) [Partner=BlanketAgreement2]
- PaymentDrafts : Collection(SAPB1.Payment) [Partner=BlanketAgreement2]
- BusinessPartner : SAPB1.BusinessPartner [Partner=BlanketAgreements]
- EmployeeInfo : SAPB1.EmployeeInfo [Partner=BlanketAgreements]
- Attachments2 : SAPB1.Attachments2 [Partner=BlanketAgreements]
- PaymentTermsType : SAPB1.PaymentTermsType [Partner=BlanketAgreements]
- PriceList2 : SAPB1.PriceList [Partner=BlanketAgreements]
- WizardPaymentMethod : SAPB1.WizardPaymentMethod [Partner=BlanketAgreements]
- ShippingType2 : SAPB1.ShippingType [Partner=BlanketAgreements]
- Project2 : SAPB1.Project [Partner=BlanketAgreements]
- Currency : SAPB1.Currency [Partner=BlanketAgreements]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=BlanketAgreement]
- JournalEntries : Collection(SAPB1.JournalEntry) [Partner=BlanketAgreement]
- IncomingPayments : Collection(SAPB1.Payment) [Partner=BlanketAgreement2]

# SAPB1.BlanketAgreementParams (ComplexType)

## Properties

- AgreementNo : Edm.Int32

# SAPB1.BlanketAgreements_DetailsLine (ComplexType)

OpenType: true

## Properties

- AgreementNo : Edm.Int32
- AgreementRowNumber : Edm.Int32
- AgreementEffectiveRowNumber : Edm.Int32
- Frequency : SAPB1.BlanketAgreementDatePeriodsEnum
- From : Edm.DateTimeOffset
- To : Edm.DateTimeOffset
- ReleaseInformation : Edm.String
- Quantity : Edm.Double
- Warehouse : Edm.String
- FreeText : Edm.String
- ConsumeSalesForecast : SAPB1.BoYesNoEnum
- PlannedAmountLC : Edm.Double
- PlannedAmountFC : Edm.Double

# SAPB1.BlanketAgreements_ItemsLine (ComplexType)

OpenType: true
Filtered properties: 21

## Properties

- AgreementNo : Edm.Int32
- AgreementRowNumber : Edm.Int32
- ItemNo : Edm.String
- ItemDescription : Edm.String
- ItemGroup : Edm.Int32
- PlannedQuantity : Edm.Double
- UnitPrice : Edm.Double
- PriceCurrency : Edm.String
- CumulativeQuantity : Edm.Double
- CumulativeAmountLC : Edm.Double
- CumulativeAmountFC : Edm.Double
- FreeText : Edm.String
- InventoryUoM : Edm.String
- PortionOfReturns : Edm.Double
- EndOfWarranty : Edm.DateTimeOffset
- PlannedAmountLC : Edm.Double
- PlannedAmountFC : Edm.Double
- LineDiscount : Edm.Double
- UoMEntry : Edm.Int32
- UoMCode : Edm.String
- UnitsOfMeasurement : Edm.Double
- UndeliveredCumulativeQuantity : Edm.Double
- UndeliveredCumulativeAmountLC : Edm.Double
- UndeliveredCumulativeAmountFC : Edm.Double
- ShippingType : Edm.Int32
- Project : Edm.String
- TaxCode : Edm.String
- TAXRate : Edm.Double
- PlannedVATAmountLC : Edm.Double
- PlannedVATAmountFC : Edm.Double
- CumulativeVATAmountLC : Edm.Double
- CumulativeVATAmountFC : Edm.Double
- BlanketAgreements_DetailsLines : Collection(SAPB1.BlanketAgreements_DetailsLine)

# SAPB1.BlanketAgreementsDocument (ComplexType)

## Properties

- AgreementRowNumber : Edm.Int32
- DocumentType : SAPB1.BlanketAgreementDocTypeEnum
- DocumentNo : Edm.Int32
- DocumentRowNumber : Edm.Int32
- DocumentDate : Edm.DateTimeOffset
- ItemNo : Edm.String
- ItemDescription : Edm.String
- UnitPrice : Edm.Double
- Quantity : Edm.Double
- Discount : Edm.Double
- UoM : Edm.String
- RowStatus : SAPB1.BoStatus
- UoMCode : Edm.String
- UnitsOfMeasurement : Edm.Double
- DocStatus : SAPB1.BADocumentStatus

# SAPB1.Blob (ComplexType)

## Properties

- Content : Edm.String

# SAPB1.BlobParams (ComplexType)

## Properties

- Table : Edm.String
- Field : Edm.String
- FileName : Edm.String
- BlobTableKeySegments : Collection(SAPB1.BlobTableKeySegment)

# SAPB1.BlobTableKeySegment (ComplexType)

## Properties

- Name : Edm.String
- Value : Edm.String

# SAPB1.BOEDocumentType (EntityType)

Key: DocEntry

## Properties

- DocEntry : Edm.Int32 [required]
- DocType : Edm.String
- DocDescription : Edm.String

# SAPB1.BOEDocumentTypeParams (ComplexType)

## Properties

- DocEntry : Edm.Int32
- DocType : Edm.String

# SAPB1.BOEInstruction (EntityType)

Key: InstructionEntry

## Properties

- InstructionEntry : Edm.Int32 [required]
- InstructionCode : Edm.String
- InstructionDesc : Edm.String
- IsCancelInstruction : SAPB1.BoYesNoEnum

# SAPB1.BOEInstructionParams (ComplexType)

## Properties

- InstructionEntry : Edm.Int32
- InstructionCode : Edm.String

# SAPB1.BOELine (ComplexType)

## Properties

- BOEKey : Edm.Int32
- BOENumber : Edm.Int32
- DueDate : Edm.DateTimeOffset
- Bank : Edm.String
- Branch : Edm.String
- AccountNumber : Edm.String
- Amount : Edm.Double
- BOEStatus : SAPB1.BoBoeStatus
- Transferred : SAPB1.BoYesNoEnum

# SAPB1.BOELineParams (ComplexType)

## Properties

- BOEKey : Edm.Int32

# SAPB1.BOEPortfolio (EntityType)

Key: PortfolioEntry

## Properties

- PortfolioEntry : Edm.Int32 [required]
- PortfolioID : Edm.String
- PortfolioCode : Edm.String
- PortfolioNum : Edm.String
- PortfolioDescription : Edm.String

# SAPB1.BOEPortfolioParams (ComplexType)

## Properties

- PortfolioEntry : Edm.Int32
- PortfolioID : Edm.String
- PortfolioCode : Edm.String

# SAPB1.Boxes1099Item (ComplexType)

OpenType: true

## Properties

- FormCode : Edm.Int32
- Box1099 : Edm.String
- BoxDescription : Edm.String
- Minimum1099Amount : Edm.Double

# SAPB1.BPAccountReceivablePayble (ComplexType)

OpenType: true

## Properties

- AccountType : SAPB1.BoBpAccountTypes
- AccountCode : Edm.String
- BPCode : Edm.String

# SAPB1.BPAddress (ComplexType)

OpenType: true
Filtered properties: 2

## Properties

- AddressName : Edm.String
- Street : Edm.String
- Block : Edm.String
- ZipCode : Edm.String
- City : Edm.String
- County : Edm.String
- Country : Edm.String
- State : Edm.String
- FederalTaxID : Edm.String
- TaxCode : Edm.String
- BuildingFloorRoom : Edm.String
- AddressType : SAPB1.BoAddressType
- AddressName2 : Edm.String
- AddressName3 : Edm.String
- TypeOfAddress : Edm.String
- StreetNo : Edm.String
- BPCode : Edm.String
- RowNum : Edm.Int32
- GlobalLocationNumber : Edm.String
- Nationality : Edm.String
- TaxOffice : Edm.String
- GSTIN : Edm.String
- GstType : SAPB1.BoGSTRegnTypeEnum
- CreateDate : Edm.DateTimeOffset
- CreateTime : Edm.TimeOfDay
- MYFType : SAPB1.BoMYFTypeEnum
- TaasEnabled : SAPB1.BoYesNoEnum

# SAPB1.BPBankAccount (ComplexType)

OpenType: true

## Properties

- LogInstance : Edm.Int32
- UserNo4 : Edm.String
- BPCode : Edm.String
- County : Edm.String
- State : Edm.String
- UserNo2 : Edm.String
- IBAN : Edm.String
- ZipCode : Edm.String
- City : Edm.String
- Block : Edm.String
- Branch : Edm.String
- Country : Edm.String
- Street : Edm.String
- ControlKey : Edm.String
- UserNo3 : Edm.String
- BankCode : Edm.String
- AccountNo : Edm.String
- UserNo1 : Edm.String
- InternalKey : Edm.Int32
- BuildingFloorRoom : Edm.String
- BIK : Edm.String
- AccountName : Edm.String
- CorrespondentAccount : Edm.String
- Phone : Edm.String
- Fax : Edm.String
- CustomerIdNumber : Edm.String
- ISRBillerID : Edm.String
- ISRType : Edm.Int32
- BICSwiftCode : Edm.String
- ABARoutingNumber : Edm.String
- MandateID : Edm.String
- SignatureDate : Edm.DateTimeOffset
- MandateExpDate : Edm.DateTimeOffset
- SEPASeqType : SAPB1.SEPASequenceTypeEnum

# SAPB1.BPBlockSendingMarketingContent (ComplexType)

## Properties

- CardCode : Edm.String
- CommunicationMediaId : Edm.Int32
- Choose : SAPB1.BoYesNoEnum

# SAPB1.BPBranchAssignmentItem (ComplexType)

OpenType: true

## Properties

- BPCode : Edm.String
- BPLID : Edm.Int32
- DisabledForBP : SAPB1.BoYesNoEnum

# SAPB1.BPCode (ComplexType)

## Properties

- Code : Edm.String
- DueDate : Edm.DateTimeOffset
- Debit : Edm.Double
- Credit : Edm.Double
- SystemDebit : Edm.Double
- SystemCredit : Edm.Double
- ForeignDebit : Edm.Double
- ForeignCredit : Edm.Double
- ForeignCurrency : Edm.String
- BpCtrlAcct : Edm.String

# SAPB1.BPCurrencies (ComplexType)

OpenType: true

## Properties

- CurrencyCode : Edm.String
- Include : SAPB1.BoYesNoEnum

# SAPB1.BPFiscalRegistryID (EntityType)

OpenType: true
Key: Numerator

## Properties

- Numerator : Edm.Int32 [required]
- CNAECode : Edm.String
- Description : Edm.String

## Navigation properties

- BusinessPlaces : Collection(SAPB1.BusinessPlace) [Partner=BPFiscalRegistryID]

# SAPB1.BPFiscalRegistryIDParams (ComplexType)

## Properties

- Numerator : Edm.Int32

# SAPB1.BPFiscalTaxID (ComplexType)

OpenType: true

## Properties

- Address : Edm.String
- CNAECode : Edm.Int32
- TaxId0 : Edm.String
- TaxId1 : Edm.String
- TaxId2 : Edm.String
- TaxId3 : Edm.String
- TaxId4 : Edm.String
- TaxId5 : Edm.String
- TaxId6 : Edm.String
- TaxId7 : Edm.String
- TaxId8 : Edm.String
- TaxId9 : Edm.String
- TaxId10 : Edm.String
- TaxId11 : Edm.String
- BPCode : Edm.String
- AddrType : SAPB1.BoAddressType
- TaxId12 : Edm.String
- TaxId13 : Edm.String
- AToRetrNFe : SAPB1.BoYesNoEnum
- TaxId14 : Edm.String

# SAPB1.BPIntrastatExtension (ComplexType)

## Properties

- CardCode : Edm.String
- TransportMode : Edm.Int32
- Incoterms : Edm.Int32
- NatureOfTransactions : Edm.Int32
- StatisticalProcedure : Edm.Int32
- CustomsProcedure : Edm.Int32
- PortOfEntryOrExit : Edm.Int32
- DomesticOrForeignID : Edm.String
- IntrastatRelevant : SAPB1.BoYesNoEnum

# SAPB1.BPPaymentDate (ComplexType)

OpenType: true

## Properties

- PaymentDate : Edm.String
- BPCode : Edm.String

# SAPB1.BPPaymentMethod (ComplexType)

OpenType: true

## Properties

- PaymentMethodCode : Edm.String
- RowNumber : Edm.Int32
- BPCode : Edm.String

# SAPB1.BPPriority (EntityType)

OpenType: true
Key: Priority

## Properties

- Priority : Edm.Int32 [required]
- PriorityDescription : Edm.String

## Navigation properties

- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=BPPriority]

# SAPB1.BPPriorityParams (ComplexType)

## Properties

- Priority : Edm.Int32

# SAPB1.BPVatExemptions (EntityType)

Key: AbsoluteEntry

## Properties

- AbsoluteEntry : Edm.Int32 [required]
- BPCode : Edm.String
- Remarks : Edm.String
- BPVatExemptionsLines : Collection(SAPB1.BPVatExemptionsLine)

## Navigation properties

- BusinessPartner : SAPB1.BusinessPartner [Partner=BPVatExemptions]

# SAPB1.BPVatExemptionsLine (ComplexType)

## Properties

- AbsoluteEntry : Edm.Int32
- LineNumber : Edm.Int32
- ExemptionDocNum : Edm.String
- IssueDate : Edm.DateTimeOffset
- IssueTime : Edm.TimeOfDay
- ExemptionType : Edm.Int32
- ApplyAllItems : SAPB1.BoYesNoEnum
- ItemCode : Edm.String
- ItemDescription : Edm.String
- VATRate : Edm.Double
- TaxCode : Edm.String
- AuthoritiesName : Edm.String
- ValidFrom : Edm.DateTimeOffset
- ValidTo : Edm.DateTimeOffset
- VisualOrder : Edm.Int32

# SAPB1.BPVatExemptionsParams (ComplexType)

## Properties

- AbsoluteEntry : Edm.Int32
- BPCode : Edm.String

# SAPB1.BPWithholdingTax (ComplexType)

OpenType: true

## Properties

- WTCode : Edm.String
- BPCode : Edm.String

# SAPB1.Branch (EntityType)

Key: Code

## Properties

- Code : Edm.Int32 [required]
- Name : Edm.String
- Description : Edm.String

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=Branch]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=Branch]
- Drafts : Collection(SAPB1.Document) [Partner=Branch]
- Users : Collection(SAPB1.User) [Partner=Branch2]
- CreditNotes : Collection(SAPB1.Document) [Partner=Branch]
- Invoices : Collection(SAPB1.Document) [Partner=Branch]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=Branch]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=Branch]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=Branch]
- Orders : Collection(SAPB1.Document) [Partner=Branch]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=Branch]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=Branch]
- Returns : Collection(SAPB1.Document) [Partner=Branch]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=Branch]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=Branch]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=Branch]
- EmployeesInfo : Collection(SAPB1.EmployeeInfo) [Partner=Branch2]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=Branch]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=Branch]
- DownPayments : Collection(SAPB1.Document) [Partner=Branch]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=Branch]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=Branch]
- ReturnRequest : Collection(SAPB1.Document) [Partner=Branch]
- Quotations : Collection(SAPB1.Document) [Partner=Branch]
- SelfInvoices : Collection(SAPB1.Document) [Partner=Branch]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=Branch]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=Branch]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=Branch]

# SAPB1.BranchParams (ComplexType)

## Properties

- Code : Edm.Int32
- Name : Edm.String

# SAPB1.BrazilBeverageIndexer (EntityType)

Key: BeverageID

## Properties

- BeverageGroupCode : Edm.String
- BeverageTableCode : Edm.String
- BeverageCommercialBrandCode : Edm.Int32
- BeverageID : Edm.Int32 [required]

## Navigation properties

- BrazilStringIndexer : SAPB1.BrazilStringIndexer [Partner=BrazilBeverageIndexers]
- BrazilNumericIndexer : SAPB1.BrazilNumericIndexer [Partner=BrazilBeverageIndexers]

# SAPB1.BrazilBeverageIndexerParams (ComplexType)

## Properties

- BeverageID : Edm.Int32

# SAPB1.BrazilFuelIndexer (EntityType)

Key: FuelID

## Properties

- FuelID : Edm.Int32 [required]
- FuelGroupCode : Edm.Int32
- FuelCode : Edm.String
- Description : Edm.String

## Navigation properties

- Items : Collection(SAPB1.Item) [Partner=BrazilFuelIndexer]

# SAPB1.BrazilFuelIndexerParams (ComplexType)

## Properties

- FuelID : Edm.Int32
- FuelGroupCode : Edm.Int32
- FuelCode : Edm.String
- Description : Edm.String

# SAPB1.BrazilMultiIndexer (EntityType)

Key: ID

## Properties

- ID : Edm.Int32 [required]
- IndexerType : SAPB1.BrazilMultiIndexerTypes
- Code : Edm.String
- Description : Edm.String
- FirstRefIndexerCode : Edm.String
- SecondRefIndexerCode : Edm.String
- ThirdRefIndexerCode : Edm.String

# SAPB1.BrazilMultiIndexerParams (ComplexType)

## Properties

- ID : Edm.Int32

# SAPB1.BrazilNumericIndexer (EntityType)

Key: ID

## Properties

- IndexerType : SAPB1.BrazilNumericIndexerTypes
- Code : Edm.Int32
- Description : Edm.String
- ID : Edm.Int32 [required]

## Navigation properties

- BusinessPlaces : Collection(SAPB1.BusinessPlace) [Partner=BrazilNumericIndexer]
- Items : Collection(SAPB1.Item) [Partner=BrazilNumericIndexer]
- VatGroups : Collection(SAPB1.VatGroup) [Partner=BrazilNumericIndexer]
- BrazilBeverageIndexers : Collection(SAPB1.BrazilBeverageIndexer) [Partner=BrazilNumericIndexer]

# SAPB1.BrazilNumericIndexerParams (ComplexType)

## Properties

- ID : Edm.Int32

# SAPB1.BrazilStringIndexer (EntityType)

Key: ID

## Properties

- IndexerType : SAPB1.BrazilStringIndexerTypes
- Code : Edm.String
- Description : Edm.String
- ID : Edm.Int32 [required]

## Navigation properties

- WithholdingTaxCodes : Collection(SAPB1.WithholdingTaxCode) [Partner=BrazilStringIndexer]
- BusinessPlaces : Collection(SAPB1.BusinessPlace) [Partner=BrazilStringIndexer]
- Items : Collection(SAPB1.Item) [Partner=BrazilStringIndexer]
- BrazilBeverageIndexers : Collection(SAPB1.BrazilBeverageIndexer) [Partner=BrazilStringIndexer]

# SAPB1.BrazilStringIndexerParams (ComplexType)

## Properties

- ID : Edm.Int32

# SAPB1.Budget (EntityType)

OpenType: true
Key: Numerator

## Properties

- FutureAnnualExpensesCreditSys : Edm.Double
- FutureAnnualExpensesCreditLoc : Edm.Double
- FutureAnnualExpensesDebitSys : Edm.Double
- FutureAnnualExpensesDebitLoc : Edm.Double
- FutureAnnualRevenuesCredit : Edm.Double
- FutureAnnualRevenuesDebit : Edm.Double
- FutureRevenuesDebitSys : Edm.Double
- FutureRevenuesDebitLoc : Edm.Double
- ParentAccPercent : Edm.Double
- StartofFiscalYear : Edm.DateTimeOffset
- ParentAccountKey : Edm.String
- TotalAnnualBudgetDebitSys : Edm.Double
- BudgetBalanceDebitSys : Edm.Double
- BudgetBalanceDebitLoc : Edm.Double
- TotalAnnualBudgetDebitLoc : Edm.Double
- TotalAnnualBudgetCreditSys : Edm.Double
- TotalAnnualBudgetCreditLoc : Edm.Double
- BudgetBalanceCreditSys : Edm.Double
- BudgetBalanceCreditLoc : Edm.Double
- DivisionCode : Edm.Int32
- AccountCode : Edm.String
- Numerator : Edm.Int32 [required]
- BudgetScenario : Edm.Int32
- BudgetLines : Collection(SAPB1.BudgetLine)
- BudgetCostAccountingLines : Collection(SAPB1.BudgetCostAccountingLine)

## Navigation properties

- BudgetDistribution : SAPB1.BudgetDistribution [Partner=Budgets]
- BudgetScenario2 : SAPB1.BudgetScenario [Partner=Budgets]

# SAPB1.BudgetCostAccountingLine (ComplexType)

OpenType: true

## Properties

- DistrRuleCode : Edm.String
- Dimension : Edm.Int32
- DistrRuleDebitLC : Edm.Double
- DistrRuleDebitSC : Edm.Double
- DistrRuleCreditLC : Edm.Double
- DistrRuleCreditSC : Edm.Double

# SAPB1.BudgetDistribution (EntityType)

OpenType: true
Key: DivisionCode

## Properties

- September : Edm.Double
- August : Edm.Double
- July : Edm.Double
- June : Edm.Double
- May : Edm.Double
- April : Edm.Double
- March : Edm.Double
- February : Edm.Double
- December : Edm.Double
- November : Edm.Double
- October : Edm.Double
- January : Edm.Double
- BudgetAmount : Edm.Double
- Description : Edm.String
- DivisionCode : Edm.Int32 [required]

## Navigation properties

- Budgets : Collection(SAPB1.Budget) [Partner=BudgetDistribution]

# SAPB1.BudgetDistributionParams (ComplexType)

## Properties

- DivisionCode : Edm.Int32

# SAPB1.BudgetLine (ComplexType)

OpenType: true

## Properties

- PrecentOfAnnualBudgetAmount : Edm.Double
- RowDetails : Edm.String
- RowNumber : Edm.Int32
- FutExpenSysDebit : Edm.Double
- FutExpenDebit : Edm.Double
- FutExpenSysCredit : Edm.Double
- FutExpenCredit : Edm.Double
- FutIncomesSysCredit : Edm.Double
- FutIncomesSysDebit : Edm.Double
- FutIncomesCredit : Edm.Double
- BudgetSysTotDebit : Edm.Double
- BalSysTotDebit : Edm.Double
- BalTotDebit : Edm.Double
- BudgetTotCredit : Edm.Double
- BudgetSysTotCredit : Edm.Double
- BudgetTotDebit : Edm.Double
- BalSysTotCredit : Edm.Double
- BalTotCredit : Edm.Double
- BudgetKey : Edm.Int32
- AccountCode : Edm.String
- FutureIncomeDeb : Edm.Double

# SAPB1.BudgetParams (ComplexType)

## Properties

- Numerator : Edm.Int32

# SAPB1.BudgetScenario (EntityType)

OpenType: true
Key: Numerator
Filtered properties: 2

## Properties

- Name : Edm.String
- InitialRatioPercentage : Edm.Double
- StartofFiscalYear : Edm.DateTimeOffset
- BasicBudget : Edm.Int32
- Numerator : Edm.Int32 [required]
- RoundingMethod : SAPB1.BoRoundingMethod
- Project : Edm.String
- DistributionRule : Edm.String
- DistributionRule2 : Edm.String
- DistributionRule3 : Edm.String
- DistributionRule4 : Edm.String
- DistributionRule5 : Edm.String

## Navigation properties

- Project2 : SAPB1.Project [Partner=BudgetScenarios]
- DistributionRule6 : SAPB1.DistributionRule [Partner=BudgetScenarios]
- Budgets : Collection(SAPB1.Budget) [Partner=BudgetScenario2]

# SAPB1.BudgetScenarioParams (ComplexType)

## Properties

- Numerator : Edm.Int32

# SAPB1.BusinessPartner (EntityType)

OpenType: true
Key: CardCode
Filtered properties: 16

## Properties

- CardCode : Edm.String [required]
- CardName : Edm.String
- CardType : SAPB1.BoCardTypes
- GroupCode : Edm.Int32
- Address : Edm.String
- ZipCode : Edm.String
- MailAddress : Edm.String
- MailZipCode : Edm.String
- Phone1 : Edm.String
- Phone2 : Edm.String
- Fax : Edm.String
- ContactPerson : Edm.String
- Notes : Edm.String
- PayTermsGrpCode : Edm.Int32
- CreditLimit : Edm.Double
- MaxCommitment : Edm.Double
- DiscountPercent : Edm.Double
- VatLiable : SAPB1.BoVatStatus
- FederalTaxID : Edm.String
- DeductibleAtSource : SAPB1.BoYesNoEnum
- DeductionPercent : Edm.Double
- DeductionValidUntil : Edm.DateTimeOffset
- PriceListNum : Edm.Int32
- IntrestRatePercent : Edm.Double
- CommissionPercent : Edm.Double
- CommissionGroupCode : Edm.Int32
- FreeText : Edm.String
- SalesPersonCode : Edm.Int32
- Currency : Edm.String
- RateDiffAccount : Edm.String
- Cellular : Edm.String
- AvarageLate : Edm.Int32
- City : Edm.String
- County : Edm.String
- Country : Edm.String
- MailCity : Edm.String
- MailCounty : Edm.String
- MailCountry : Edm.String
- EmailAddress : Edm.String
- Picture : Edm.String
- DefaultAccount : Edm.String
- DefaultBranch : Edm.String
- DefaultBankCode : Edm.String
- AdditionalID : Edm.String
- Pager : Edm.String
- FatherCard : Edm.String
- CardForeignName : Edm.String
- FatherType : SAPB1.BoFatherCardTypes
- DeductionOffice : Edm.String
- ExportCode : Edm.String
- MinIntrest : Edm.Double
- CurrentAccountBalance : Edm.Double
- OpenDeliveryNotesBalance : Edm.Double
- OpenOrdersBalance : Edm.Double
- OpenChecksBalance : Edm.Double
- VatGroup : Edm.String
- ShippingType : Edm.Int32
- Password : Edm.String
- Indicator : Edm.String
- IBAN : Edm.String
- CreditCardCode : Edm.Int32
- CreditCardNum : Edm.String
- CreditCardExpiration : Edm.DateTimeOffset
- DebitorAccount : Edm.String
- OpenOpportunities : Edm.Int32
- Valid : SAPB1.BoYesNoEnum
- ValidFrom : Edm.DateTimeOffset
- ValidTo : Edm.DateTimeOffset
- ValidRemarks : Edm.String
- Frozen : SAPB1.BoYesNoEnum
- FrozenFrom : Edm.DateTimeOffset
- FrozenTo : Edm.DateTimeOffset
- FrozenRemarks : Edm.String
- Block : Edm.String
- BillToState : Edm.String
- ShipToState : Edm.String
- ExemptNum : Edm.String
- Priority : Edm.Int32
- FormCode1099 : Edm.Int32
- Box1099 : Edm.String
- PeymentMethodCode : Edm.String
- BackOrder : SAPB1.BoYesNoEnum
- PartialDelivery : SAPB1.BoYesNoEnum
- BlockDunning : SAPB1.BoYesNoEnum
- BankCountry : Edm.String
- HouseBank : Edm.String
- HouseBankCountry : Edm.String
- HouseBankAccount : Edm.String
- ShipToDefault : Edm.String
- DunningLevel : Edm.Int32
- DunningDate : Edm.DateTimeOffset
- CollectionAuthorization : SAPB1.BoYesNoEnum
- DME : Edm.String
- InstructionKey : Edm.String
- SinglePayment : SAPB1.BoYesNoEnum
- ISRBillerID : Edm.String
- PaymentBlock : SAPB1.BoYesNoEnum
- ReferenceDetails : Edm.String
- HouseBankBranch : Edm.String
- OwnerIDNumber : Edm.String
- PaymentBlockDescription : Edm.Int32
- TaxExemptionLetterNum : Edm.String
- MaxAmountOfExemption : Edm.Double
- ExemptionValidityDateFrom : Edm.DateTimeOffset
- ExemptionValidityDateTo : Edm.DateTimeOffset
- LinkedBusinessPartner : Edm.String
- LastMultiReconciliationNum : Edm.Int32
- DeferredTax : SAPB1.BoYesNoEnum
- Equalization : SAPB1.BoYesNoEnum
- SubjectToWithholdingTax : SAPB1.BoYesNoNoneEnum
- CertificateNumber : Edm.String
- ExpirationDate : Edm.DateTimeOffset
- NationalInsuranceNum : Edm.String
- AccrualCriteria : SAPB1.BoYesNoEnum
- WTCode : Edm.String
- BillToBuildingFloorRoom : Edm.String
- DownPaymentClearAct : Edm.String
- ChannelBP : Edm.String
- DefaultTechnician : Edm.Int32
- BilltoDefault : Edm.String
- CustomerBillofExchangDisc : Edm.String
- Territory : Edm.Int32
- ShipToBuildingFloorRoom : Edm.String
- CustomerBillofExchangPres : Edm.String
- ProjectCode : Edm.String
- VatGroupLatinAmerica : Edm.String
- DunningTerm : Edm.String
- Website : Edm.String
- OtherReceivablePayable : Edm.String
- BillofExchangeonCollection : Edm.String
- CompanyPrivate : SAPB1.BoCardCompanyTypes
- LanguageCode : Edm.Int32
- UnpaidBillofExchange : Edm.String
- WithholdingTaxDeductionGroup : Edm.Int32
- ClosingDateProcedureNumber : Edm.Int32
- Profession : Edm.String
- BankChargesAllocationCode : Edm.String
- TaxRoundingRule : SAPB1.BoTaxRoundingRuleTypes
- Properties1 : SAPB1.BoYesNoEnum
- Properties2 : SAPB1.BoYesNoEnum
- Properties3 : SAPB1.BoYesNoEnum
- Properties4 : SAPB1.BoYesNoEnum
- Properties5 : SAPB1.BoYesNoEnum
- Properties6 : SAPB1.BoYesNoEnum
- Properties7 : SAPB1.BoYesNoEnum
- Properties8 : SAPB1.BoYesNoEnum
- Properties9 : SAPB1.BoYesNoEnum
- Properties10 : SAPB1.BoYesNoEnum
- Properties11 : SAPB1.BoYesNoEnum
- Properties12 : SAPB1.BoYesNoEnum
- Properties13 : SAPB1.BoYesNoEnum
- Properties14 : SAPB1.BoYesNoEnum
- Properties15 : SAPB1.BoYesNoEnum
- Properties16 : SAPB1.BoYesNoEnum
- Properties17 : SAPB1.BoYesNoEnum
- Properties18 : SAPB1.BoYesNoEnum
- Properties19 : SAPB1.BoYesNoEnum
- Properties20 : SAPB1.BoYesNoEnum
- Properties21 : SAPB1.BoYesNoEnum
- Properties22 : SAPB1.BoYesNoEnum
- Properties23 : SAPB1.BoYesNoEnum
- Properties24 : SAPB1.BoYesNoEnum
- Properties25 : SAPB1.BoYesNoEnum
- Properties26 : SAPB1.BoYesNoEnum
- Properties27 : SAPB1.BoYesNoEnum
- Properties28 : SAPB1.BoYesNoEnum
- Properties29 : SAPB1.BoYesNoEnum
- Properties30 : SAPB1.BoYesNoEnum
- Properties31 : SAPB1.BoYesNoEnum
- Properties32 : SAPB1.BoYesNoEnum
- Properties33 : SAPB1.BoYesNoEnum
- Properties34 : SAPB1.BoYesNoEnum
- Properties35 : SAPB1.BoYesNoEnum
- Properties36 : SAPB1.BoYesNoEnum
- Properties37 : SAPB1.BoYesNoEnum
- Properties38 : SAPB1.BoYesNoEnum
- Properties39 : SAPB1.BoYesNoEnum
- Properties40 : SAPB1.BoYesNoEnum
- Properties41 : SAPB1.BoYesNoEnum
- Properties42 : SAPB1.BoYesNoEnum
- Properties43 : SAPB1.BoYesNoEnum
- Properties44 : SAPB1.BoYesNoEnum
- Properties45 : SAPB1.BoYesNoEnum
- Properties46 : SAPB1.BoYesNoEnum
- Properties47 : SAPB1.BoYesNoEnum
- Properties48 : SAPB1.BoYesNoEnum
- Properties49 : SAPB1.BoYesNoEnum
- Properties50 : SAPB1.BoYesNoEnum
- Properties51 : SAPB1.BoYesNoEnum
- Properties52 : SAPB1.BoYesNoEnum
- Properties53 : SAPB1.BoYesNoEnum
- Properties54 : SAPB1.BoYesNoEnum
- Properties55 : SAPB1.BoYesNoEnum
- Properties56 : SAPB1.BoYesNoEnum
- Properties57 : SAPB1.BoYesNoEnum
- Properties58 : SAPB1.BoYesNoEnum
- Properties59 : SAPB1.BoYesNoEnum
- Properties60 : SAPB1.BoYesNoEnum
- Properties61 : SAPB1.BoYesNoEnum
- Properties62 : SAPB1.BoYesNoEnum
- Properties63 : SAPB1.BoYesNoEnum
- Properties64 : SAPB1.BoYesNoEnum
- CompanyRegistrationNumber : Edm.String
- VerificationNumber : Edm.String
- DiscountBaseObject : SAPB1.DiscountGroupBaseObjectEnum
- DiscountRelations : SAPB1.DiscountGroupRelationsEnum
- TypeReport : SAPB1.AssesseeTypeEnum
- ThresholdOverlook : SAPB1.BoYesNoEnum
- SurchargeOverlook : SAPB1.BoYesNoEnum
- Remark1 : Edm.Int32
- ConCerti : Edm.String
- DownPaymentInterimAccount : Edm.String
- OperationCode347 : SAPB1.OperationCode347Enum
- InsuranceOperation347 : SAPB1.BoYesNoEnum
- HierarchicalDeduction : SAPB1.BoYesNoEnum
- ShaamGroup : SAPB1.ShaamGroupEnum
- WithholdingTaxCertified : SAPB1.BoYesNoEnum
- BookkeepingCertified : SAPB1.BoYesNoEnum
- PlanningGroup : Edm.String
- Affiliate : SAPB1.BoYesNoEnum
- Industry : Edm.Int32
- VatIDNum : Edm.String
- DatevAccount : Edm.String
- DatevFirstDataEntry : SAPB1.BoYesNoEnum
- UseShippedGoodsAccount : SAPB1.BoYesNoEnum
- GTSRegNo : Edm.String
- GTSBankAccountNo : Edm.String
- GTSBillingAddrTel : Edm.String
- ETaxWebSite : Edm.Int32
- HouseBankIBAN : Edm.String
- VATRegistrationNumber : Edm.String
- RepresentativeName : Edm.String
- IndustryType : Edm.String
- BusinessType : Edm.String
- Series : Edm.Int32
- AutomaticPosting : SAPB1.AutomaticPostingEnum
- InterestAccount : Edm.String
- FeeAccount : Edm.String
- CampaignNumber : Edm.Int32
- AliasName : Edm.String
- DefaultBlanketAgreementNumber : Edm.Int32
- EffectiveDiscount : SAPB1.DiscountGroupRelationsEnum
- NoDiscounts : SAPB1.BoYesNoEnum
- EffectivePrice : SAPB1.EffectivePriceEnum
- EffectivePriceConsidersPriceBeforeDiscount : SAPB1.BoYesNoEnum
- GlobalLocationNumber : Edm.String
- EDISenderID : Edm.String
- EDIRecipientID : Edm.String
- ResidenNumber : SAPB1.ResidenceNumberTypeEnum
- RelationshipCode : Edm.String
- RelationshipDateFrom : Edm.DateTimeOffset
- RelationshipDateTill : Edm.DateTimeOffset
- UnifiedFederalTaxID : Edm.String
- AttachmentEntry : Edm.Int32
- TypeOfOperation : SAPB1.TypeOfOperationEnum
- EndorsableChecksFromBP : SAPB1.BoYesNoEnum
- AcceptsEndorsedChecks : SAPB1.BoYesNoEnum
- OwnerCode : Edm.Int32
- BlockSendingMarketingContent : SAPB1.BoYesNoEnum
- AgentCode : Edm.String
- PriceMode : SAPB1.PriceModeEnum
- EDocGenerationType : SAPB1.EDocGenerationTypeEnum
- EDocStreet : Edm.String
- EDocStreetNumber : Edm.String
- EDocBuildingNumber : Edm.Int32
- EDocZipCode : Edm.String
- EDocCity : Edm.String
- EDocCountry : Edm.String
- EDocDistrict : Edm.String
- EDocRepresentativeFirstName : Edm.String
- EDocRepresentativeSurname : Edm.String
- EDocRepresentativeCompany : Edm.String
- EDocRepresentativeFiscalCode : Edm.String
- EDocRepresentativeAdditionalId : Edm.String
- EDocPECAddress : Edm.String
- IPACodeForPA : Edm.String
- UpdateDate : Edm.DateTimeOffset
- UpdateTime : Edm.TimeOfDay
- ExemptionMaxAmountValidationType : SAPB1.ExemptionMaxAmountValidationTypeEnum
- ECommerceMerchantID : Edm.String
- UseBillToAddrToDetermineTax : SAPB1.BoYesNoEnum
- CreateDate : Edm.DateTimeOffset
- CreateTime : Edm.TimeOfDay
- DefaultTransporterEntry : Edm.Int32
- DefaultTransporterLineNumber : Edm.Int32
- FCERelevant : SAPB1.BoYesNoEnum
- FCEValidateBaseDelivery : SAPB1.BoYesNoEnum
- MainUsage : Edm.Int32
- EBooksVATExemptionCause : Edm.Int32
- LegalText : Edm.String
- DataVersion : Edm.Int32
- ExchangeRateForIncomingPayment : SAPB1.BoYesNoEnum
- ExchangeRateForOutgoingPayment : SAPB1.BoYesNoEnum
- CertificateDetails : Edm.String
- DefaultCurrency : Edm.String
- EORINumber : Edm.String
- FCEAsPaymentMeans : SAPB1.BoYesNoEnum
- NotRelevantForMonthlyInvoice : SAPB1.BoYesNoEnum
- NaturalPer : SAPB1.BoYesNoEnum
- SirenNumber : Edm.String
- SiretNumber : Edm.String
- VATExemptionReason : Edm.String
- RoutingCode : Edm.String
- PublicDirectoryStatus : SAPB1.BoPublicDirectoryStatusTypes
- ElectronicProtocols : Collection(SAPB1.ElectronicProtocol)
- BPAddresses : Collection(SAPB1.BPAddress)
- ContactEmployees : Collection(SAPB1.ContactEmployee)
- BPAccountReceivablePaybleCollection : Collection(SAPB1.BPAccountReceivablePayble)
- BPPaymentMethods : Collection(SAPB1.BPPaymentMethod)
- BPWithholdingTaxCollection : Collection(SAPB1.BPWithholdingTax)
- BPPaymentDates : Collection(SAPB1.BPPaymentDate)
- BPBranchAssignment : Collection(SAPB1.BPBranchAssignmentItem)
- BPBankAccounts : Collection(SAPB1.BPBankAccount)
- BPFiscalTaxIDCollection : Collection(SAPB1.BPFiscalTaxID)
- DiscountGroups : Collection(SAPB1.DiscountGroup)
- BPIntrastatExtension : SAPB1.BPIntrastatExtension
- BPBlockSendingMarketingContents : Collection(SAPB1.BPBlockSendingMarketingContent)
- BPCurrenciesCollection : Collection(SAPB1.BPCurrencies)

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=BusinessPartner]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=BusinessPartner]
- Drafts : Collection(SAPB1.Document) [Partner=BusinessPartner]
- StockTransferDrafts : Collection(SAPB1.StockTransfer) [Partner=BusinessPartner]
- Activities : Collection(SAPB1.Activity) [Partner=BusinessPartner]
- PartnersSetups : Collection(SAPB1.PartnersSetup) [Partner=BusinessPartner]
- DeductionTaxHierarchies : Collection(SAPB1.DeductionTaxHierarchy) [Partner=BusinessPartner]
- VendorPayments : Collection(SAPB1.Payment) [Partner=BusinessPartner]
- MaterialRevaluation : Collection(SAPB1.MaterialRevaluation) [Partner=BusinessPartner]
- ProductionOrders : Collection(SAPB1.ProductionOrder) [Partner=BusinessPartner]
- PaymentDrafts : Collection(SAPB1.Payment) [Partner=BusinessPartner]
- InventoryTransferRequests : Collection(SAPB1.StockTransfer) [Partner=BusinessPartner]
- BlanketAgreements : Collection(SAPB1.BlanketAgreement) [Partner=BusinessPartner]
- CreditNotes : Collection(SAPB1.Document) [Partner=BusinessPartner]
- Invoices : Collection(SAPB1.Document) [Partner=BusinessPartner]
- ExportDeterminations : Collection(SAPB1.ExportDetermination) [Partner=BusinessPartner2]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=BusinessPartner]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=BusinessPartner]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=BusinessPartner]
- DepreciationAreas : Collection(SAPB1.DepreciationArea) [Partner=BusinessPartner]
- GLAccountAdvancedRules : Collection(SAPB1.GLAccountAdvancedRule) [Partner=BusinessPartner]
- Orders : Collection(SAPB1.Document) [Partner=BusinessPartner]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=BusinessPartner]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=BusinessPartner]
- Returns : Collection(SAPB1.Document) [Partner=BusinessPartner]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=BusinessPartner]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=BusinessPartner]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=BusinessPartner]
- EmployeesInfo : Collection(SAPB1.EmployeeInfo) [Partner=BusinessPartner]
- CustomerEquipmentCards : Collection(SAPB1.CustomerEquipmentCard) [Partner=BusinessPartner]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=BusinessPartner]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=BusinessPartner]
- ServiceContracts : Collection(SAPB1.ServiceContract) [Partner=BusinessPartner]
- ServiceCalls : Collection(SAPB1.ServiceCall) [Partner=BusinessPartner]
- BusinessPartnerGroup : SAPB1.BusinessPartnerGroup [Partner=BusinessPartners]
- PaymentTermsType : SAPB1.PaymentTermsType [Partner=BusinessPartners]
- PriceList : SAPB1.PriceList [Partner=BusinessPartners]
- CommissionGroup : SAPB1.CommissionGroup [Partner=BusinessPartners]
- SalesPerson : SAPB1.SalesPerson [Partner=BusinessPartners]
- Currency2 : SAPB1.Currency [Partner=BusinessPartners]
- ChartOfAccount : SAPB1.ChartOfAccount [Partner=BusinessPartners]
- Country2 : SAPB1.Country [Partner=BusinessPartners]
- VatGroup2 : SAPB1.VatGroup [Partner=BusinessPartners]
- ShippingType2 : SAPB1.ShippingType [Partner=BusinessPartners]
- FactoringIndicator : SAPB1.FactoringIndicator [Partner=BusinessPartners]
- CreditCard : SAPB1.CreditCard [Partner=BusinessPartners]
- BPPriority : SAPB1.BPPriority [Partner=BusinessPartners]
- Forms1099 : SAPB1.Forms1099 [Partner=BusinessPartners]
- WizardPaymentMethod : SAPB1.WizardPaymentMethod [Partner=BusinessPartners]
- DunningLetter : SAPB1.DunningLetter [Partner=BusinessPartners]
- PaymentBlock2 : SAPB1.PaymentBlock [Partner=BusinessPartners]
- WithholdingTaxCode : SAPB1.WithholdingTaxCode [Partner=BusinessPartners]
- EmployeeInfo : SAPB1.EmployeeInfo [Partner=BusinessPartners]
- Territory2 : SAPB1.Territory [Partner=BusinessPartners]
- Project : SAPB1.Project [Partner=BusinessPartners]
- SalesTaxCode : SAPB1.SalesTaxCode [Partner=BusinessPartners]
- DunningTerm2 : SAPB1.DunningTerm [Partner=BusinessPartners]
- UserLanguage : SAPB1.UserLanguage [Partner=BusinessPartners]
- DeductionTaxGroup : SAPB1.DeductionTaxGroup [Partner=BusinessPartners]
- ClosingDateProcedure : SAPB1.ClosingDateProcedure [Partner=BusinessPartners]
- BankChargesAllocationCode2 : SAPB1.BankChargesAllocationCode [Partner=BusinessPartners]
- Industry2 : SAPB1.Industry [Partner=BusinessPartners]
- TaxWebSite : SAPB1.TaxWebSite [Partner=BusinessPartners]
- Campaign : SAPB1.Campaign [Partner=BusinessPartners]
- BlanketAgreement : SAPB1.BlanketAgreement [Partner=BusinessPartners]
- EWBTransporter : SAPB1.EWBTransporter [Partner=BusinessPartners]
- DownPayments : Collection(SAPB1.Document) [Partner=BusinessPartner]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=BusinessPartner]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=BusinessPartner]
- ReturnRequest : Collection(SAPB1.Document) [Partner=BusinessPartner]
- Quotations : Collection(SAPB1.Document) [Partner=BusinessPartner]
- ProjectManagements : Collection(SAPB1.PM_ProjectDocumentData) [Partner=BusinessPartner2]
- BPVatExemptions : Collection(SAPB1.BPVatExemptions) [Partner=BusinessPartner]
- IncomingPayments : Collection(SAPB1.Payment) [Partner=BusinessPartner]
- SpecificWTHAmountsService : Collection(SAPB1.SpecificWTHAmounts) [Partner=BusinessPartner]
- SalesOpportunities : Collection(SAPB1.SalesOpportunities) [Partner=BusinessPartner]
- BusinessPlaces : Collection(SAPB1.BusinessPlace) [Partner=BusinessPartner]
- SelfInvoices : Collection(SAPB1.Document) [Partner=BusinessPartner]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=BusinessPartner]
- LandedCosts : Collection(SAPB1.LandedCost) [Partner=BusinessPartner]
- Contacts : Collection(SAPB1.Contact) [Partner=BusinessPartner]
- SalesTaxInvoices : Collection(SAPB1.SalesTaxInvoice) [Partner=BusinessPartner]
- PurchaseTaxInvoices : Collection(SAPB1.PurchaseTaxInvoice) [Partner=BusinessPartner]
- BankPages : Collection(SAPB1.BankPage) [Partner=BusinessPartner]
- Items : Collection(SAPB1.Item) [Partner=BusinessPartner]
- RecurringTransactionTemplates : Collection(SAPB1.RecurringTransactionTemplate) [Partner=BusinessPartner]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=BusinessPartner]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=BusinessPartner]
- Warehouses : Collection(SAPB1.Warehouse) [Partner=BusinessPartner]
- StockTransfers : Collection(SAPB1.StockTransfer) [Partner=BusinessPartner]
- SpecialPrices : Collection(SAPB1.SpecialPrice) [Partner=BusinessPartner]
- AlternateCatNum : Collection(SAPB1.AlternateCatNum) [Partner=BusinessPartner]
- UserDefaultGroups : Collection(SAPB1.UserDefaultGroup) [Partner=BusinessPartner]

# SAPB1.BusinessPartnerGroup (EntityType)

OpenType: true
Key: Code

## Properties

- Code : Edm.Int32 [required]
- Name : Edm.String
- Type : SAPB1.BoBusinessPartnerGroupTypes

## Navigation properties

- GLAccountAdvancedRules : Collection(SAPB1.GLAccountAdvancedRule) [Partner=BusinessPartnerGroup]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=BusinessPartnerGroup]

# SAPB1.BusinessPartnerGroupParams (ComplexType)

## Properties

- Code : Edm.Int32

# SAPB1.BusinessPartnerParams (ComplexType)

## Properties

- CardCode : Edm.String

# SAPB1.BusinessPartnerProperty (EntityType)

OpenType: true
Key: PropertyCode

## Properties

- PropertyCode : Edm.Int32 [required]
- PropertyName : Edm.String

# SAPB1.BusinessPartnerPropertyParams (ComplexType)

## Properties

- PropertyCode : Edm.Int32
- PropertyName : Edm.String

# SAPB1.BusinessPlace (EntityType)

OpenType: true
Key: BPLID

## Properties

- BPLID : Edm.Int32 [required]
- BPLName : Edm.String
- BPLNameForeign : Edm.String
- VATRegNum : Edm.String
- RepName : Edm.String
- Industry : Edm.String
- Business : Edm.String
- Address : Edm.String
- Addressforeign : Edm.String
- MainBPL : SAPB1.BoYesNoEnum
- TaxOfficeNo : Edm.String
- Disabled : SAPB1.BoYesNoEnum
- DefaultCustomerID : Edm.String
- DefaultVendorID : Edm.String
- DefaultWarehouseID : Edm.String
- DefaultTaxCode : Edm.String
- TaxOffice : Edm.String
- FederalTaxID : Edm.String
- FederalTaxID2 : Edm.String
- FederalTaxID3 : Edm.String
- AdditionalIdNumber : Edm.String
- NatureOfCompanyCode : Edm.Int32
- EconomicActivityTypeCode : Edm.Int32
- CreditContributionOriginCode : Edm.String
- IPIPeriodCode : Edm.String
- CooperativeAssociationTypeCode : Edm.Int32
- ProfitTaxationCode : Edm.Int32
- CompanyQualificationCode : Edm.Int32
- DeclarerTypeCode : Edm.Int32
- PreferredStateCode : Edm.String
- AddressType : Edm.String
- Street : Edm.String
- StreetNo : Edm.String
- Building : Edm.String
- ZipCode : Edm.String
- Block : Edm.String
- City : Edm.String
- State : Edm.String
- County : Edm.String
- Country : Edm.String
- AliasName : Edm.String
- CommercialRegister : Edm.String
- DateOfIncorporation : Edm.DateTimeOffset
- SPEDProfile : Edm.String
- EnvironmentType : Edm.Int32
- Opting4ICMS : SAPB1.BoYesNoEnum
- PaymentClearingAccount : Edm.String
- GlobalLocationNumber : Edm.String
- DefaultResourceWarehouseID : Edm.String
- BusinessPlaceIENumbers : Collection(SAPB1.BusinessPlaceIENumber)
- BusinessPlaceTributaryInfos : Collection(SAPB1.BusinessPlaceTributaryInfo)

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=BusinessPlace]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=BusinessPlace]
- Drafts : Collection(SAPB1.Document) [Partner=BusinessPlace]
- StockTransferDrafts : Collection(SAPB1.StockTransfer) [Partner=BusinessPlace]
- InventoryPostings : Collection(SAPB1.InventoryPosting) [Partner=BusinessPlace]
- AssetManualDepreciation : Collection(SAPB1.AssetDocument) [Partner=BusinessPlace]
- Deposits : Collection(SAPB1.Deposit) [Partner=BusinessPlace]
- VendorPayments : Collection(SAPB1.Payment) [Partner=BusinessPlace]
- PaymentDrafts : Collection(SAPB1.Payment) [Partner=BusinessPlace]
- AssetClasses : Collection(SAPB1.AssetClass) [Partner=BusinessPlace]
- InventoryTransferRequests : Collection(SAPB1.StockTransfer) [Partner=BusinessPlace]
- AssetRevaluations : Collection(SAPB1.AssetRevaluation) [Partner=BusinessPlace]
- ISDRecipientInvoices : Collection(SAPB1.ISDRecipientInvoice) [Partner=BusinessPlace]
- CreditNotes : Collection(SAPB1.Document) [Partner=BusinessPlace]
- Invoices : Collection(SAPB1.Document) [Partner=BusinessPlace]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=BusinessPlace]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=BusinessPlace]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=BusinessPlace]
- AssetCapitalization : Collection(SAPB1.AssetDocument) [Partner=BusinessPlace]
- AssetCapitalizationCreditMemo : Collection(SAPB1.AssetDocument) [Partner=BusinessPlace]
- Orders : Collection(SAPB1.Document) [Partner=BusinessPlace]
- InventoryCountings : Collection(SAPB1.InventoryCounting) [Partner=BusinessPlace]
- AssetTransfer : Collection(SAPB1.AssetDocument) [Partner=BusinessPlace]
- AssetRetirement : Collection(SAPB1.AssetDocument) [Partner=BusinessPlace]
- InventoryCountingDrafts : Collection(SAPB1.InventoryCountingDraft) [Partner=BusinessPlace]
- InventoryPostingDrafts : Collection(SAPB1.InventoryPostingDraft) [Partner=BusinessPlace]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=BusinessPlace]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=BusinessPlace]
- Returns : Collection(SAPB1.Document) [Partner=BusinessPlace]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=BusinessPlace]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=BusinessPlace]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=BusinessPlace]
- InventoryOpeningBalances : Collection(SAPB1.InventoryOpeningBalance) [Partner=BusinessPlace]
- EmployeesInfo : Collection(SAPB1.EmployeeInfo) [Partner=BusinessPlace]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=BusinessPlace]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=BusinessPlace]
- DownPayments : Collection(SAPB1.Document) [Partner=BusinessPlace]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=BusinessPlace]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=BusinessPlace]
- ReturnRequest : Collection(SAPB1.Document) [Partner=BusinessPlace]
- Quotations : Collection(SAPB1.Document) [Partner=BusinessPlace]
- ISDDocuments : Collection(SAPB1.ISDDocument) [Partner=BusinessPlace]
- IncomingPayments : Collection(SAPB1.Payment) [Partner=BusinessPlace]
- BusinessPartner : SAPB1.BusinessPartner [Partner=BusinessPlaces]
- Warehouse : SAPB1.Warehouse [Partner=BusinessPlaces]
- BPFiscalRegistryID : SAPB1.BPFiscalRegistryID [Partner=BusinessPlaces]
- BrazilNumericIndexer : SAPB1.BrazilNumericIndexer [Partner=BusinessPlaces]
- BrazilStringIndexer : SAPB1.BrazilStringIndexer [Partner=BusinessPlaces]
- County2 : SAPB1.County [Partner=BusinessPlaces]
- Country2 : SAPB1.Country [Partner=BusinessPlaces]
- ChartOfAccount : SAPB1.ChartOfAccount [Partner=BusinessPlaces]
- ISDInvoices : Collection(SAPB1.ISDInvoice) [Partner=BusinessPlace]
- ISDCreditMemos : Collection(SAPB1.ISDCreditMemo) [Partner=BusinessPlace]
- ISDRecipientCreditMemos : Collection(SAPB1.ISDRecipientCreditMemo) [Partner=BusinessPlace]
- SelfInvoices : Collection(SAPB1.Document) [Partner=BusinessPlace]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=BusinessPlace]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=BusinessPlace]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=BusinessPlace]
- StockTransfers : Collection(SAPB1.StockTransfer) [Partner=BusinessPlace]
- UserDefaultGroups : Collection(SAPB1.UserDefaultGroup) [Partner=BusinessPlace]

# SAPB1.BusinessPlaceIENumber (ComplexType)

OpenType: true

## Properties

- BPLID : Edm.Int32
- State : Edm.String
- IENumber : Edm.String

# SAPB1.BusinessPlaceParams (ComplexType)

## Properties

- BPLID : Edm.Int32

# SAPB1.BusinessPlaceTributaryInfo (ComplexType)

OpenType: true

## Properties

- BPLID : Edm.Int32
- TributaryID : Edm.Int32
- TributaryType : Edm.Int32
- TTStartDate : Edm.DateTimeOffset
- TTEndDate : Edm.DateTimeOffset
- TributaryRegimeCode : Edm.Int32
- TRCStartDate : Edm.DateTimeOffset
- TRCEndDate : Edm.DateTimeOffset

# SAPB1.CallArgument (ComplexType)

## Properties

- Name : Edm.String
- Value : Edm.String

# SAPB1.CallMessage (ComplexType)

## Properties

- ID : Edm.Int32
- Type : SAPB1.CallMessageTypeEnum
- ErrorCode : Edm.String
- MessageBody : Edm.String
- Status : SAPB1.CallMessageStatusEnum
- CreationDate : Edm.DateTimeOffset
- CreationTime : Edm.Int32
- CallMessageArguments : Collection(SAPB1.CallMessageArgument)

# SAPB1.CallMessageArgument (ComplexType)

## Properties

- Name : Edm.String
- Value : Edm.String

# SAPB1.Campaign (EntityType)

OpenType: true
Key: CampaignNumber

## Properties

- CampaignNumber : Edm.Int32 [required]
- CampaignName : Edm.String
- CampaignType : SAPB1.CampaignTypeEnum
- TargetGroup : Edm.String
- Owner : Edm.Int32
- Status : SAPB1.CampaignStatusEnum
- StartDate : Edm.DateTimeOffset
- FinishDate : Edm.DateTimeOffset
- Remarks : Edm.String
- GeneratedByWizard : SAPB1.BoYesNoEnum
- AttachementsEntry : Edm.Int32
- TargetGroupType : SAPB1.TargetGroupTypeEnum
- CampaignBusinessPartners : Collection(SAPB1.CampaignBusinessPartner)
- CampaignItems : Collection(SAPB1.CampaignItem)
- CampaignPartners : Collection(SAPB1.CampaignPartner)

## Navigation properties

- TargetGroup2 : SAPB1.TargetGroup [Partner=Campaigns]
- EmployeeInfo : SAPB1.EmployeeInfo [Partner=Campaigns]
- Attachments2 : SAPB1.Attachments2 [Partner=Campaigns]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=Campaign]

# SAPB1.CampaignBusinessPartner (ComplexType)

OpenType: true

## Properties

- CampaignNumber : Edm.Int32
- CampaignLineNumber : Edm.Int32
- BPCode : Edm.String
- BPName : Edm.String
- BPGroupName : Edm.String
- BPIndustryName : Edm.String
- BPStatus : Edm.String
- ContactCode : Edm.String
- ContactTitle : Edm.String
- ContactPosition : Edm.String
- ContactEmail : Edm.String
- ContactTelephone : Edm.String
- ContactMobile : Edm.String
- ContactFax : Edm.String
- ContactAddress : Edm.String
- Response : SAPB1.BoYesNoEnum
- RelatedSalesOpportunity : Edm.Int32
- Street : Edm.String
- Block : Edm.String
- City : Edm.String
- ZipCode : Edm.String
- County : Edm.String
- State : Edm.String
- Country : Edm.String
- Building : Edm.String
- DocType : SAPB1.LinkedDocTypeEnum
- IsShowLinkedDoc : SAPB1.BoYesNoEnum
- DocNumber : Edm.Int32
- DocEntry : Edm.Int32
- FirstName : Edm.String
- MiddleName : Edm.String
- LastName : Edm.String
- AddressID : Edm.String
- AddressType : Edm.String
- AddressName2 : Edm.String
- AddressName3 : Edm.String
- FederalTaxID : Edm.String
- StreetNo : Edm.String
- CreateActivity : SAPB1.BoYesNoEnum
- AssignTo : SAPB1.CampaignAssignToEnum
- AssignName : Edm.Int32
- ResponseType : Edm.String

# SAPB1.CampaignItem (ComplexType)

OpenType: true

## Properties

- CampaignNumber : Edm.Int32
- CampaignLineNumber : Edm.Int32
- ItemCode : Edm.String
- ItemName : Edm.String
- ItemType : SAPB1.CampaignItemTypeEnum
- ItemGroup : Edm.String

# SAPB1.CampaignParams (ComplexType)

## Properties

- CampaignNumber : Edm.Int32
- CampaignName : Edm.String

# SAPB1.CampaignPartner (ComplexType)

OpenType: true

## Properties

- CampaignNumber : Edm.Int32
- CampaignLineNumber : Edm.Int32
- PartnerID : Edm.Int32
- RelationshipCode : Edm.Int32
- RelatedBP : Edm.String
- Details : Edm.String

# SAPB1.CampaignResponseType (EntityType)

Key: ResponseType

## Properties

- ResponseTypeDescription : Edm.String
- ResponseType : Edm.String [required]
- IsActive : SAPB1.BoYesNoEnum

# SAPB1.CampaignResponseTypeParams (ComplexType)

## Properties

- ResponseType : Edm.String
- ResponseTypeDescription : Edm.String
- IsActive : SAPB1.BoYesNoEnum

# SAPB1.CancelCheckRowParams (ComplexType)

## Properties

- DepositID : Edm.Int32
- CheckID : Edm.Int32

# SAPB1.CashDiscount (EntityType)

Key: Code

## Properties

- Code : Edm.String [required]
- Name : Edm.String
- ByDate : SAPB1.BoYesNoEnum
- Freight : SAPB1.BoYesNoEnum
- Tax : SAPB1.BoYesNoEnum
- DiscountLines : Collection(SAPB1.DiscountLine)

## Navigation properties

- PaymentTermsTypes : Collection(SAPB1.PaymentTermsType) [Partner=CashDiscount]

# SAPB1.CashDiscountParams (ComplexType)

## Properties

- Code : Edm.String
- Name : Edm.String

# SAPB1.CashFlowAssignment (ComplexType)

OpenType: true

## Properties

- CashFlowAssignmentsID : Edm.Int32
- CashFlowLineItemID : Edm.Int32
- Credit : Edm.Double
- PaymentMeans : SAPB1.PaymentMeansTypeEnum
- CheckNumber : Edm.String
- AmountLC : Edm.Double
- AmountFC : Edm.Double
- JDTLineId : Edm.Int32
- JDTId : Edm.Int32

# SAPB1.CashFlowLineItem (EntityType)

Key: LineItemID

## Properties

- LineItemID : Edm.Int32 [required]
- LineItemName : Edm.String
- ActiveLineItem : SAPB1.BoYesNoEnum
- ParentArticle : Edm.Int32
- Level : Edm.Int32
- Drawer : Edm.Int32

# SAPB1.CashFlowLineItemParams (ComplexType)

## Properties

- LineItemID : Edm.Int32
- LineItemName : Edm.String

# SAPB1.CategoryGroup (ComplexType)

## Properties

- AuthGroupId : Edm.Int32
- CategoryId : Edm.Int32

# SAPB1.CCDNumber (ComplexType)

OpenType: true

## Properties

- TrackingNote : Edm.Int32
- TrackingNoteLine : Edm.Int32
- CCDNumberProperty : Edm.String
- Quantity : Edm.Double
- CountryOfOrigin : Edm.String
- SubLineNumber : Edm.Int32
- DocumentEntry : Edm.Int32
- BaseLineNumber : Edm.Int32
- ChildNumber : Edm.Int32

# SAPB1.CentralBankIndicator (EntityType)

Key: Indicator

## Properties

- Indicator : Edm.String [required]
- Description : Edm.String

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- Drafts : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- CreditNotes : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- Invoices : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- Orders : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- Returns : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- DownPayments : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- ReturnRequest : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- Quotations : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- SelfInvoices : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=CentralBankIndicator2]

# SAPB1.CentralBankIndicatorParams (ComplexType)

## Properties

- Indicator : Edm.String

# SAPB1.CertificateSeries (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- Code : Edm.String
- Section : Edm.Int32
- Location : Edm.Int32
- DefaultSeries : Edm.Int32
- SeriesLines : Collection(SAPB1.SeriesLine)

## Navigation properties

- Section2 : SAPB1.Section [Partner=CertificateSeries]
- WarehouseLocation : SAPB1.WarehouseLocation [Partner=CertificateSeries]

# SAPB1.CertificateSeriesParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- Code : Edm.String
- Section : Edm.Int32
- Location : Edm.Int32

# SAPB1.CESTCodeData (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- Code : Edm.String
- Description : Edm.String

## Navigation properties

- Items : Collection(SAPB1.Item) [Partner=CESTCodeData]

# SAPB1.CESTCodeParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32

# SAPB1.ChangeLogDifferenceParams (ComplexType)

## Properties

- Date : Edm.DateTimeOffset
- ChangedField : Edm.String
- OldValue : Edm.String
- NewValue : Edm.String
- UserName : Edm.String
- ArrayOffset : Edm.Int32
- LineNumber : Edm.String

# SAPB1.ChangeLogParams (ComplexType)

## Properties

- LogInstance : Edm.Int32
- UpdatedDate : Edm.DateTimeOffset
- UserName : Edm.String
- ObjectCode : Edm.String

# SAPB1.ChartOfAccount (EntityType)

OpenType: true
Key: Code
Filtered properties: 5

## Properties

- Code : Edm.String [required]
- Name : Edm.String
- Balance : Edm.Double
- CashAccount : SAPB1.BoYesNoEnum
- BudgetAccount : SAPB1.BoYesNoEnum
- ActiveAccount : SAPB1.BoYesNoEnum
- PrimaryAccount : SAPB1.BoYesNoEnum
- AccountLevel : Edm.Int32
- DataExportCode : Edm.String
- FatherAccountKey : Edm.String
- ExternalCode : Edm.String
- RateConversion : SAPB1.BoYesNoEnum
- TaxLiableAccount : SAPB1.BoYesNoEnum
- TaxExemptAccount : SAPB1.BoYesNoEnum
- ExternalReconNo : Edm.Int32
- InternalReconNo : Edm.Int32
- AccountType : SAPB1.BoAccountTypes
- AcctCurrency : Edm.String
- Balance_syscurr : Edm.Double
- Balance_FrgnCurr : Edm.Double
- Protected : SAPB1.BoYesNoEnum
- ReconciledAccount : SAPB1.BoYesNoEnum
- LiableForAdvances : SAPB1.BoYesNoEnum
- ForeignName : Edm.String
- Details : Edm.String
- ProjectCode : Edm.String
- RevaluationCoordinated : SAPB1.BoYesNoEnum
- LockManualTransaction : SAPB1.BoYesNoEnum
- FormatCode : Edm.String
- AllowChangeVatGroup : SAPB1.BoYesNoEnum
- DefaultVatGroup : Edm.String
- Category : Edm.Int32
- TransactionCode : Edm.String
- LoadingType : SAPB1.BoYesNoEnum
- LoadingFactorCode : Edm.String
- LoadingFactorCode2 : Edm.String
- LoadingFactorCode3 : Edm.String
- LoadingFactorCode4 : Edm.String
- LoadingFactorCode5 : Edm.String
- PlanningLevel : Edm.String
- DatevAccount : Edm.String
- DatevAutoAccount : SAPB1.BoYesNoEnum
- DatevFirstDataEntry : SAPB1.BoYesNoEnum
- AllowMultipleLinking : SAPB1.BoYesNoEnum
- ProjectRelevant : SAPB1.BoYesNoEnum
- DistributionRuleRelevant : SAPB1.BoYesNoEnum
- DistributionRule2Relevant : SAPB1.BoYesNoEnum
- DistributionRule3Relevant : SAPB1.BoYesNoEnum
- DistributionRule4Relevant : SAPB1.BoYesNoEnum
- DistributionRule5Relevant : SAPB1.BoYesNoEnum
- BPLID : Edm.Int32
- BPLName : Edm.String
- VATRegNum : Edm.String
- AccountPurposeCode : SAPB1.SPEDContabilAccountPurposeCode
- ReferentialAccountCode : Edm.String
- ValidFor : SAPB1.BoYesNoEnum
- ValidFrom : Edm.DateTimeOffset
- ValidTo : Edm.DateTimeOffset
- ValidRemarks : Edm.String
- FrozenFor : SAPB1.BoYesNoEnum
- FrozenFrom : Edm.DateTimeOffset
- FrozenTo : Edm.DateTimeOffset
- FrozenRemarks : Edm.String
- BlockManualPosting : SAPB1.BoYesNoEnum
- CashFlowRelevant : SAPB1.BoYesNoEnum
- PCN874ReportRelevant : SAPB1.BoYesNoEnum
- PrimaryClosingAccount : Edm.String
- CostAccountingOnly : SAPB1.BoYesNoEnum
- CostElementRelevant : SAPB1.BoYesNoEnum
- CostElementCode : Edm.String
- StandardAccountCode : Edm.String
- TaxonomyCode : Edm.String
- IncomeClassificationCategory : Edm.Int32
- IncomeClassificationType : Edm.Int32
- ExpenseClassificationCategory : Edm.Int32
- ExpenseClassificationType : Edm.Int32
- OfficialAccountCode : Edm.String
- ExchangeRateDifference : SAPB1.BoYesNoEnum

## Navigation properties

- Currency : SAPB1.Currency [Partner=ChartOfAccounts]
- Project : SAPB1.Project [Partner=ChartOfAccounts]
- AccountCategory : SAPB1.AccountCategory [Partner=ChartOfAccounts]
- TransactionCode2 : SAPB1.TransactionCode [Partner=ChartOfAccounts]
- DistributionRule : SAPB1.DistributionRule [Partner=ChartOfAccounts]
- CostElement : SAPB1.CostElement [Partner=ChartOfAccounts]
- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- Drafts : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- VendorPayments : Collection(SAPB1.Payment) [Partner=ChartOfAccount]
- WithholdingTaxCodes : Collection(SAPB1.WithholdingTaxCode) [Partner=ChartOfAccount]
- PaymentDrafts : Collection(SAPB1.Payment) [Partner=ChartOfAccount]
- AdditionalExpenses : Collection(SAPB1.AdditionalExpense) [Partner=ChartOfAccount]
- HouseBankAccounts : Collection(SAPB1.HouseBankAccount) [Partner=ChartOfAccount]
- SalesTaxAuthorities : Collection(SAPB1.SalesTaxAuthority) [Partner=ChartOfAccount]
- CreditNotes : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- Invoices : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- WizardPaymentMethods : Collection(SAPB1.WizardPaymentMethod) [Partner=ChartOfAccount]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- FAAccountDeterminations : Collection(SAPB1.FAAccountDetermination) [Partner=ChartOfAccount]
- GLAccountAdvancedRules : Collection(SAPB1.GLAccountAdvancedRule) [Partner=ChartOfAccount]
- Orders : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- Returns : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- DunningTerms : Collection(SAPB1.DunningTerm) [Partner=ChartOfAccount]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=ChartOfAccount]
- DownPayments : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- CreditCards : Collection(SAPB1.CreditCard) [Partner=ChartOfAccount]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- ReturnRequest : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- Quotations : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- IncomingPayments : Collection(SAPB1.Payment) [Partner=ChartOfAccount]
- ExpenseTypes : Collection(SAPB1.ExpenseTypeData) [Partner=ChartOfAccount]
- CustomsGroups : Collection(SAPB1.CustomsGroup) [Partner=ChartOfAccount]
- BusinessPlaces : Collection(SAPB1.BusinessPlace) [Partner=ChartOfAccount]
- SelfInvoices : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- BankPages : Collection(SAPB1.BankPage) [Partner=ChartOfAccount]
- Items : Collection(SAPB1.Item) [Partner=ChartOfAccount]
- VatGroups : Collection(SAPB1.VatGroup) [Partner=ChartOfAccount]
- ItemGroups : Collection(SAPB1.ItemGroups) [Partner=ChartOfAccount]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- AccrualTypes : Collection(SAPB1.AccrualType) [Partner=ChartOfAccount]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=ChartOfAccount]
- Warehouses : Collection(SAPB1.Warehouse) [Partner=ChartOfAccount]

# SAPB1.ChartOfAccountParams (ComplexType)

## Properties

- Code : Edm.String

# SAPB1.CheckInParams (ComplexType)

## Properties

- LineNumber : Edm.Int32
- Date : Edm.DateTimeOffset
- Time : Edm.TimeOfDay
- Location : Edm.String
- Latitude : Edm.String
- Longitude : Edm.String
- HandledBy : Edm.Int32
- HandledByEmployee : Edm.Int32
- RecipientType : Edm.String
- RecipientName : Edm.String
- EmailAddress : Edm.String

# SAPB1.CheckLine (ComplexType)

## Properties

- CheckKey : Edm.Int32
- CheckNumber : Edm.Int32
- Bank : Edm.String
- Branch : Edm.String
- CashCheck : Edm.String
- CheckDate : Edm.DateTimeOffset
- Customer : Edm.String
- CheckAmount : Edm.Double
- Deposited : SAPB1.BoDepositCheckEnum
- Transferred : SAPB1.BoYesNoEnum
- AccountNumber : Edm.String
- CheckCurrency : Edm.String
- FiscalID : Edm.String
- OriginallyIssuedBy : Edm.String
- RejectedByBank : SAPB1.BoYesNoEnum

# SAPB1.CheckLineParams (ComplexType)

## Properties

- CheckKey : Edm.Int32

# SAPB1.ChecksforPayment (EntityType)

OpenType: true
Key: CheckKey

## Properties

- CheckKey : Edm.Int32 [required]
- CheckNumber : Edm.Int32
- BankCode : Edm.String
- Branch : Edm.String
- BankName : Edm.String
- CheckDate : Edm.DateTimeOffset
- AccountNumber : Edm.String
- Details : Edm.String
- JournalEntryReference : Edm.String
- PaymentDate : Edm.DateTimeOffset
- PaymentNo : Edm.Int32
- CheckAmount : Edm.Double
- Transferable : SAPB1.BoYesNoEnum
- VendorCode : Edm.String
- CheckCurrency : Edm.String
- Canceled : SAPB1.BoYesNoEnum
- CardOrAccount : SAPB1.BoCpCardAcct
- Printed : SAPB1.BoYesNoEnum
- VendorName : Edm.String
- Signature : Edm.String
- CustomerAccountCode : Edm.String
- TransactionNumber : Edm.Int32
- Address : Edm.String
- CreateJournalEntry : SAPB1.BoYesNoEnum
- UpdateDate : Edm.DateTimeOffset
- CreationDate : Edm.DateTimeOffset
- TaxTotal : Edm.Double
- TaxDate : Edm.DateTimeOffset
- DeductionRefundAmount : Edm.Double
- PrintedBy : Edm.Int32
- CountryCode : Edm.String
- TotalinWords : Edm.String
- AddressName : Edm.String
- ManualCheck : SAPB1.BoYesNoEnum
- AttachmentEntry : Edm.Int32
- ECheck : SAPB1.BoYesNoEnum
- PrintConfirm : SAPB1.BoYesNoEnum
- ChecksforPaymentLines : Collection(SAPB1.ChecksforPaymentLine)
- ChecksforPaymentPrintStatus : Collection(SAPB1.ChecksforPaymentPrintStatus)
- ChecksforPaymentDocumentReferences : Collection(SAPB1.ChecksforPaymentDocumentReference)

## Navigation properties

- JournalEntry : SAPB1.JournalEntry [Partner=ChecksforPayment]
- Country : SAPB1.Country [Partner=ChecksforPayment]
- Attachments2 : SAPB1.Attachments2 [Partner=ChecksforPayment]

# SAPB1.ChecksforPaymentDocumentReference (ComplexType)

OpenType: true

## Properties

- DocEntry : Edm.Int32
- LineNumber : Edm.Int32
- ReferencedDocEntry : Edm.Int32
- ReferencedDocNumber : Edm.Int32
- ExternalReferencedDocNumber : Edm.String
- ReferencedObjectType : SAPB1.ReferencedObjectTypeEnum
- IssueDate : Edm.DateTimeOffset
- Remark : Edm.String

# SAPB1.ChecksforPaymentLine (ComplexType)

OpenType: true

## Properties

- RowNumber : Edm.Int32
- RowDetails : Edm.String
- RowTotal : Edm.Double
- RowCurrency : Edm.String
- TaxDefinition : Edm.String
- TaxPercent : Edm.Double
- CreditedAccount : Edm.String
- LineTotal : Edm.Double

# SAPB1.ChecksforPaymentParams (ComplexType)

## Properties

- CheckKey : Edm.Int32

# SAPB1.ChecksforPaymentPrintStatus (ComplexType)

OpenType: true

## Properties

- DocEntry : Edm.Int32
- LineNumber : Edm.Int32
- CheckNumber : Edm.Int32
- PrintStatus : Edm.String
- PrintedBy : Edm.Int32

# SAPB1.ChooseFromList (EntityType)

OpenType: true
Key: ObjectName

## Properties

- ObjectName : Edm.String [required]
- ChooseFromList_Lines : Collection(SAPB1.ChooseFromList_Line)

# SAPB1.ChooseFromList_Line (ComplexType)

OpenType: true

## Properties

- ObjectName : Edm.String
- FieldIndex : Edm.Int32
- FieldNo : Edm.String
- DisplayedName : Edm.String
- GroupBy : SAPB1.BoYesNoEnum
- Visible : SAPB1.BoYesNoEnum
- ShowType : SAPB1.BoYesNoEnum
- SortOrder : SAPB1.SortOrderEnum
- VisualIndex : Edm.Int32

# SAPB1.ChooseFromListParams (ComplexType)

## Properties

- ObjectName : Edm.String

# SAPB1.CIGCode (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- Code : Edm.String

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=CIGCode]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=CIGCode]
- Drafts : Collection(SAPB1.Document) [Partner=CIGCode]
- VendorPayments : Collection(SAPB1.Payment) [Partner=CIGCode]
- PaymentDrafts : Collection(SAPB1.Payment) [Partner=CIGCode]
- CreditNotes : Collection(SAPB1.Document) [Partner=CIGCode]
- Invoices : Collection(SAPB1.Document) [Partner=CIGCode]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=CIGCode]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=CIGCode]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=CIGCode]
- Orders : Collection(SAPB1.Document) [Partner=CIGCode]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=CIGCode]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=CIGCode]
- Returns : Collection(SAPB1.Document) [Partner=CIGCode]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=CIGCode]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=CIGCode]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=CIGCode]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=CIGCode]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=CIGCode]
- DownPayments : Collection(SAPB1.Document) [Partner=CIGCode]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=CIGCode]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=CIGCode]
- ReturnRequest : Collection(SAPB1.Document) [Partner=CIGCode]
- Quotations : Collection(SAPB1.Document) [Partner=CIGCode]
- JournalEntries : Collection(SAPB1.JournalEntry) [Partner=CIGCode]
- IncomingPayments : Collection(SAPB1.Payment) [Partner=CIGCode]
- SelfInvoices : Collection(SAPB1.Document) [Partner=CIGCode]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=CIGCode]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=CIGCode]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=CIGCode]

# SAPB1.CIGCodeParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32

# SAPB1.ClosingDateProcedure (EntityType)

OpenType: true
Key: ClosingDateNum

## Properties

- ClosingDateNum : Edm.Int32 [required]
- ClosingDateCode : Edm.String
- BaselineDate : SAPB1.BoClosingDateProcedureBaseDateEnum
- DueMonth : SAPB1.BoClosingDateProcedureDueMonthEnum
- ExtraMonth : Edm.Int32
- ExtraDay : Edm.Int32

## Navigation properties

- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=ClosingDateProcedure]

# SAPB1.ClosingDateProcedureParams (ComplexType)

## Properties

- ClosingDateNum : Edm.Int32

# SAPB1.Cockpit (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- Code : Edm.Int32
- Name : Edm.String
- Description : Edm.String
- UserSignature : Edm.Int32
- Date : Edm.DateTimeOffset
- Time : Edm.TimeOfDay
- Manufacturer : Edm.String
- Publisher : Edm.String
- CockpitType : SAPB1.BoCockpitTypeEnum

## Navigation properties

- User : SAPB1.User [Partner=Cockpits]

# SAPB1.CockpitParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- CockpitType : SAPB1.BoCockpitTypeEnum

# SAPB1.ColumnPreferences (EntityType)

Key: User, FormID, ItemNumber, Column

## Properties

- User : Edm.Int32 [required]
- FormID : Edm.String [required]
- ItemNumber : Edm.String [required]
- Column : Edm.String [required]
- Width : Edm.Int32
- VisibleInForm : SAPB1.BoYesNoEnum
- TabsLayout : Edm.Int32
- EditableInForm : SAPB1.BoYesNoEnum
- VisibleInExpanded : SAPB1.BoYesNoEnum
- ExpandedIndex : Edm.Int32
- EditableInExpanded : SAPB1.BoYesNoEnum

## Navigation properties

- User2 : SAPB1.User [Partner=FormPreferences]

# SAPB1.ColumnsPreferencesParams (ComplexType)

## Properties

- User : Edm.Int32
- FormID : Edm.String
- ItemNumber : Edm.String
- Column : Edm.String
- Width : Edm.Int32
- VisibleInForm : SAPB1.BoYesNoEnum
- TabsLayout : Edm.Int32
- EditableInForm : SAPB1.BoYesNoEnum
- VisibleInExpanded : SAPB1.BoYesNoEnum
- ExpandedIndex : Edm.Int32
- EditableInExpanded : SAPB1.BoYesNoEnum

# SAPB1.CommissionGroup (EntityType)

OpenType: true
Key: CommissionGroupCode

## Properties

- CommissionGroupCode : Edm.Int32 [required]
- CommissionGroupName : Edm.String
- CommissionPercentage : Edm.Double

## Navigation properties

- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=CommissionGroup]
- Items : Collection(SAPB1.Item) [Partner=CommissionGroup2]
- SalesPersons : Collection(SAPB1.SalesPerson) [Partner=CommissionGroup2]

# SAPB1.CommissionGroupParams (ComplexType)

## Properties

- CommissionGroupCode : Edm.Int32

# SAPB1.CompanyInfo (ComplexType)

## Properties

- Version : Edm.Int32
- EnableExpensesManagement : SAPB1.BoYesNoEnum
- EnableAccountSegmentation : SAPB1.BoYesNoEnum
- EnableBillOfExchange : SAPB1.BoYesNoEnum
- BaseDateForExchangeRate : SAPB1.BoBaseDateRateEnum
- BISRBankActKey : Edm.Int32
- BISRBankCountry : Edm.String
- BISRBankNo : Edm.String
- BISRBankAccount : Edm.String
- BISRBranch : Edm.String
- MaxRecordsInChooseFromList : Edm.Int32
- EnableCheckQuantityInRDR : SAPB1.BoYesNoEnum
- SRIManagementSystem : SAPB1.BoManageMethod
- AutoSRICreationOnReceipt : SAPB1.BoYesNoEnum
- IEPSPayer : SAPB1.BoYesNoEnum
- DefaultDaysForOrdCanc : Edm.Int32
- PercentOfTotalAcquisition : Edm.Double
- MinimumBaseAmountPerDoc : Edm.Double
- EnableSharingSeries : SAPB1.BoYesNoEnum
- DataOwnershipIndication : SAPB1.BoYesNoEnum
- MinimumAmountForAppndixOP : Edm.Double
- DisplayTransactionsByDflt : SAPB1.BoYesNoEnum
- DefaultStampTax : Edm.String
- MinimumAmountForAnnualList : Edm.Double
- BlockStockNegativeQuantity : SAPB1.BoYesNoEnum
- AutoCreateCustomerEqCard : SAPB1.BoYesNoEnum
- MaxNumberOfDocumentsInPmt : Edm.Int32
- EnableStockRelNoCostPrice : SAPB1.BoYesNoEnum
- CompanyName : Edm.String
- GroupLinesInVATCalculation : SAPB1.BoYesNoEnum
- TaxCalculationSystem : SAPB1.TaxCalcSysEnum
- EnableTransactionNotification : SAPB1.BoYesNoEnum
- EnableConversionDifferentAcct : SAPB1.BoYesNoEnum
- B1iTimeOut : Edm.Int32
- LanguageCode : SAPB1.BoSuppLangs
- Localization : Edm.String

# SAPB1.CompanySummary (ComplexType)

## Properties

- dbName : Edm.String
- cmpName : Edm.String
- versStr : Edm.String
- dbUser : Edm.String
- LOC : Edm.String

# SAPB1.Contact (EntityType)

OpenType: true
Key: ContactCode

## Properties

- CardCode : Edm.String
- Notes : Edm.String
- ContactDate : Edm.DateTimeOffset
- ContactTime : Edm.TimeOfDay
- Recontact : Edm.DateTimeOffset
- Closed : SAPB1.BoYesNoEnum
- CloseDate : Edm.DateTimeOffset
- Phone : Edm.String
- Fax : Edm.String
- Subject : Edm.Int32
- DocType : Edm.String
- DocNum : Edm.String
- DocEntry : Edm.String
- ContactCode : Edm.Int32 [required]
- Priority : SAPB1.BoMsgPriorities
- Details : Edm.String
- Activity : SAPB1.BoActivities
- ActivityType : Edm.Int32
- Location : Edm.Int32
- StartTime : Edm.TimeOfDay
- EndTime : Edm.TimeOfDay
- Duration : Edm.Double
- DurationType : SAPB1.BoDurations
- SalesEmployee : Edm.Int32
- ContactPersonCode : Edm.Int32
- HandledBy : Edm.Int32
- Reminder : SAPB1.BoYesNoEnum
- ReminderPeriod : Edm.Double
- ReminderType : SAPB1.BoDurations
- City : Edm.String
- Personalflag : SAPB1.BoYesNoEnum
- Street : Edm.String
- ParentobjectId : Edm.Int32
- Parentobjecttype : Edm.String
- Room : Edm.String
- Inactiveflag : SAPB1.BoYesNoEnum
- State : Edm.String
- PreviousActivity : Edm.Int32
- Country : Edm.String
- Status : Edm.Int32
- Tentativeflag : SAPB1.BoYesNoEnum
- EndDuedate : Edm.DateTimeOffset
- DocTypeEx : Edm.String
- AttachmentEntry : Edm.Int32
- StartDate : Edm.DateTimeOffset
- UserSignature : Edm.Int32
- UserSignature2 : Edm.Int32
- Emailedflag : SAPB1.BoYesNoEnum

## Navigation properties

- BusinessPartner : SAPB1.BusinessPartner [Partner=Contacts]
- ActivitySubject : SAPB1.ActivitySubject [Partner=Contacts]
- ActivityType2 : SAPB1.ActivityType [Partner=Contacts]
- ActivityLocation : SAPB1.ActivityLocation [Partner=Contacts]
- SalesPerson : SAPB1.SalesPerson [Partner=Contacts]
- User : SAPB1.User [Partner=Contacts]
- Country2 : SAPB1.Country [Partner=Contacts]
- ActivityStatus : SAPB1.ActivityStatus [Partner=Contacts]

# SAPB1.ContactEmployee (ComplexType)

OpenType: true

## Properties

- CardCode : Edm.String
- Name : Edm.String
- Position : Edm.String
- Address : Edm.String
- Phone1 : Edm.String
- Phone2 : Edm.String
- MobilePhone : Edm.String
- Fax : Edm.String
- E_Mail : Edm.String
- Pager : Edm.String
- Remarks1 : Edm.String
- Remarks2 : Edm.String
- Password : Edm.String
- InternalCode : Edm.Int32
- PlaceOfBirth : Edm.String
- DateOfBirth : Edm.DateTimeOffset
- Gender : SAPB1.BoGenderTypes
- Profession : Edm.String
- Title : Edm.String
- CityOfBirth : Edm.String
- Active : SAPB1.BoYesNoEnum
- FirstName : Edm.String
- MiddleName : Edm.String
- LastName : Edm.String
- EmailGroupCode : Edm.String
- BlockSendingMarketingContent : SAPB1.BoYesNoEnum
- CreateDate : Edm.DateTimeOffset
- CreateTime : Edm.TimeOfDay
- UpdateDate : Edm.DateTimeOffset
- UpdateTime : Edm.TimeOfDay
- ConnectedAddressName : Edm.String
- ConnectedAddressType : SAPB1.BoAddressType
- ForeignCountry : Edm.String
- GenderEx : Edm.String
- NaturalPer : SAPB1.BoYesNoEnum
- ContactEmployeeBlockSendingMarketingContents : Collection(SAPB1.ContactEmployeeBlockSendingMarketingContent)

# SAPB1.ContactEmployeeBlockSendingMarketingContent (ComplexType)

## Properties

- ContactEmployeeAbsEntry : Edm.Int32
- CommunicationMediaId : Edm.Int32
- Choose : SAPB1.BoYesNoEnum
- CardCode : Edm.String
- ContactPersonName : Edm.String

# SAPB1.ContactParams (ComplexType)

## Properties

- ContactCode : Edm.Int32

# SAPB1.ContractTemplate (EntityType)

OpenType: true
Key: TemplateName

## Properties

- TemplateName : Edm.String [required]
- TemplateIsDeleted : SAPB1.BoYesNoEnum
- TemplateIsRenewal : SAPB1.BoYesNoEnum
- RemindBeforeRenewal : Edm.Int32
- RemindUnit : SAPB1.BoRemindUnits
- DurationOfCoverage : Edm.Int32
- ResponseValue : Edm.Int32
- ResolutionUnit : SAPB1.BoResolutionUnits
- Description : Edm.String
- ContractType : SAPB1.BoContractTypes
- MondayEnabled : SAPB1.BoYesNoEnum
- TuesdayEnabled : SAPB1.BoYesNoEnum
- WednesdayEnabled : SAPB1.BoYesNoEnum
- ThursdayEnabled : SAPB1.BoYesNoEnum
- FridayEnabled : SAPB1.BoYesNoEnum
- SaturdayEnabled : SAPB1.BoYesNoEnum
- SundayEnabled : SAPB1.BoYesNoEnum
- MondayStart : Edm.TimeOfDay
- MondayEnd : Edm.TimeOfDay
- TuesdayStart : Edm.TimeOfDay
- TuesdayEnd : Edm.TimeOfDay
- WednesdayStart : Edm.TimeOfDay
- WednesdayEnd : Edm.TimeOfDay
- ThursdayStart : Edm.TimeOfDay
- ThursdayEnd : Edm.TimeOfDay
- FridayStart : Edm.TimeOfDay
- FridayEnd : Edm.TimeOfDay
- SaturdayStart : Edm.TimeOfDay
- SaturdayEnd : Edm.TimeOfDay
- SundayStart : Edm.TimeOfDay
- SundayEnd : Edm.TimeOfDay
- IncludeParts : SAPB1.BoYesNoEnum
- IncludeLabor : SAPB1.BoYesNoEnum
- IncludeTravel : SAPB1.BoYesNoEnum
- Remarks : Edm.String
- IncludeHolidays : SAPB1.BoYesNoEnum
- ResponseUnit : SAPB1.BoResponseUnit
- ResolutionTime : Edm.Int32
- AttachmentEntry : Edm.Int32

## Navigation properties

- ServiceContracts : Collection(SAPB1.ServiceContract) [Partner=ContractTemplate2]
- Items : Collection(SAPB1.Item) [Partner=ContractTemplate]

# SAPB1.ContractTemplateParams (ComplexType)

## Properties

- TemplateName : Edm.String

# SAPB1.CostCenterType (EntityType)

OpenType: true
Key: CostCenterTypeCode

## Properties

- CostCenterTypeCode : Edm.String [required]
- CostCenterTypeName : Edm.String

## Navigation properties

- ProfitCenters : Collection(SAPB1.ProfitCenter) [Partner=CostCenterType2]

# SAPB1.CostCenterTypeParams (ComplexType)

## Properties

- CostCenterTypeCode : Edm.String

# SAPB1.CostElement (EntityType)

Key: Code

## Properties

- Code : Edm.String [required]
- Description : Edm.String
- IsActive : SAPB1.BoYesNoEnum

## Navigation properties

- ChartOfAccounts : Collection(SAPB1.ChartOfAccount) [Partner=CostElement]

# SAPB1.CostElementParams (ComplexType)

## Properties

- Code : Edm.String
- Description : Edm.String

# SAPB1.Country (EntityType)

OpenType: true
Key: Code

## Properties

- Code : Edm.String [required]
- Name : Edm.String
- CodeForReports : Edm.String
- AddressFormat : Edm.Int32
- EU : SAPB1.BoYesNoEnum
- NumberOfDigitsForTaxID : Edm.Int32
- BankCodeDigits : Edm.Int32
- BankBranchDigits : Edm.Int32
- BankAccountDigits : Edm.Int32
- BankControlKeyDigits : Edm.Int32
- DomesticAccountValidation : SAPB1.DomesticBankAccountValidationEnum
- IbanValidation : SAPB1.BoYesNoEnum
- Blacklisted : SAPB1.BoYesNoEnum
- UICCountryCode : Edm.String
- EAEU : SAPB1.BoYesNoEnum
- ISOAlpha2Code : Edm.String
- ISOAlpha3Code : Edm.String
- ISONumeric : Edm.String

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=Country]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=Country]
- Drafts : Collection(SAPB1.Document) [Partner=Country]
- WarehouseLocations : Collection(SAPB1.WarehouseLocation) [Partner=Country2]
- Activities : Collection(SAPB1.Activity) [Partner=Country2]
- VendorPayments : Collection(SAPB1.Payment) [Partner=Country]
- PaymentDrafts : Collection(SAPB1.Payment) [Partner=Country]
- HouseBankAccounts : Collection(SAPB1.HouseBankAccount) [Partner=Country2]
- CreditNotes : Collection(SAPB1.Document) [Partner=Country]
- Invoices : Collection(SAPB1.Document) [Partner=Country]
- ExportDeterminations : Collection(SAPB1.ExportDetermination) [Partner=Country2]
- States : Collection(SAPB1.State) [Partner=Country2]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=Country]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=Country]
- WizardPaymentMethods : Collection(SAPB1.WizardPaymentMethod) [Partner=Country]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=Country]
- GLAccountAdvancedRules : Collection(SAPB1.GLAccountAdvancedRule) [Partner=Country]
- Orders : Collection(SAPB1.Document) [Partner=Country]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=Country]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=Country]
- Returns : Collection(SAPB1.Document) [Partner=Country]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=Country]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=Country]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=Country]
- EmployeesInfo : Collection(SAPB1.EmployeeInfo) [Partner=Country]
- CustomerEquipmentCards : Collection(SAPB1.CustomerEquipmentCard) [Partner=Country]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=Country]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=Country]
- ServiceCalls : Collection(SAPB1.ServiceCall) [Partner=Country2]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=Country2]
- DownPayments : Collection(SAPB1.Document) [Partner=Country]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=Country]
- CreditCards : Collection(SAPB1.CreditCard) [Partner=Country]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=Country]
- ReturnRequest : Collection(SAPB1.Document) [Partner=Country]
- Quotations : Collection(SAPB1.Document) [Partner=Country]
- IncomingPayments : Collection(SAPB1.Payment) [Partner=Country]
- BusinessPlaces : Collection(SAPB1.BusinessPlace) [Partner=Country2]
- SelfInvoices : Collection(SAPB1.Document) [Partner=Country]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=Country]
- Contacts : Collection(SAPB1.Contact) [Partner=Country2]
- Banks : Collection(SAPB1.Bank) [Partner=Country]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=Country]
- ChecksforPayment : Collection(SAPB1.ChecksforPayment) [Partner=Country]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=Country]
- Warehouses : Collection(SAPB1.Warehouse) [Partner=Country2]
- UserDefaultGroups : Collection(SAPB1.UserDefaultGroup) [Partner=Country2]

# SAPB1.CountryParams (ComplexType)

## Properties

- Code : Edm.String
- Name : Edm.String

# SAPB1.County (EntityType)

OpenType: true
Key: AbsId

## Properties

- AbsId : Edm.Int32 [required]
- Code : Edm.String
- Country : Edm.String
- State : Edm.String
- Name : Edm.String
- IbgeCode : Edm.String
- GiaCode : Edm.String
- TaxZone : SAPB1.BoYesNoEnum

## Navigation properties

- BusinessPlaces : Collection(SAPB1.BusinessPlace) [Partner=County2]
- Warehouses : Collection(SAPB1.Warehouse) [Partner=County2]

# SAPB1.CountyParams (ComplexType)

## Properties

- AbsId : Edm.Int32
- Code : Edm.String
- Name : Edm.String

# SAPB1.CreditCard (EntityType)

OpenType: true
Key: CreditCardCode

## Properties

- CreditCardCode : Edm.Int32 [required]
- CreditCardName : Edm.String
- GLAccount : Edm.String
- Telephone : Edm.String
- CompanyID : Edm.String
- CountryCode : Edm.String

## Navigation properties

- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=CreditCard]
- ChartOfAccount : SAPB1.ChartOfAccount [Partner=CreditCards]
- Country : SAPB1.Country [Partner=CreditCards]
- CreditPaymentMethods : Collection(SAPB1.CreditPaymentMethod) [Partner=CreditCard]

# SAPB1.CreditCardParams (ComplexType)

## Properties

- CreditCardCode : Edm.Int32

# SAPB1.CreditCardPayment (EntityType)

OpenType: true
Key: DueDateCode

## Properties

- DueDateCode : Edm.String [required]
- DueDateName : Edm.String
- DueDatesType : SAPB1.DueDateTypesEnum
- PaymentAfterDays : Edm.Int32
- PaymentAfterMonths : Edm.Int32
- FromDay1 : Edm.Int32
- ToDay1 : Edm.Int32
- PaymentDay1 : Edm.Int32
- NoOfMonths1 : Edm.Int32
- FromDay2 : Edm.Int32
- ToDay2 : Edm.Int32
- PaymentDay2 : Edm.Int32
- NoOfMonths2 : Edm.Int32
- FromDay3 : Edm.Int32
- ToDay3 : Edm.Int32
- PaymentDay3 : Edm.Int32
- NoOfMonths3 : Edm.Int32
- FromDay4 : Edm.Int32
- ToDay4 : Edm.Int32
- PaymentDay4 : Edm.Int32
- NoOfMonths4 : Edm.Int32

## Navigation properties

- CreditPaymentMethods : Collection(SAPB1.CreditPaymentMethod) [Partner=CreditCardPayment]

# SAPB1.CreditCardPaymentParams (ComplexType)

## Properties

- DueDateCode : Edm.String

# SAPB1.CreditLine (ComplexType)

## Properties

- AbsId : Edm.Int32
- CreditCard : Edm.Int32
- VoucherNumber : Edm.String
- PaymentMethodCode : Edm.Int32
- PayDate : Edm.DateTimeOffset
- Deposited : SAPB1.BoYesNoEnum
- NumOfPayments : Edm.Int32
- Customer : Edm.String
- Reference : Edm.String
- Transferred : SAPB1.BoYesNoEnum
- Total : Edm.Double
- CreditCurrency : Edm.String

# SAPB1.CreditLineParams (ComplexType)

## Properties

- AbsId : Edm.Int32

# SAPB1.CreditPaymentMethod (EntityType)

OpenType: true
Key: PaymentMethodCode

## Properties

- PaymentMethodCode : Edm.Int32 [required]
- Name : Edm.String
- AssignedtoCreditCard : Edm.Int32
- PaymentCode : Edm.String
- MinimumCreditAmount : Edm.Double
- MinimumPaymentAmount : Edm.Double
- MaxQtyWithoutApproval : Edm.Double
- InstallmentPaymentsPossible : SAPB1.InstallmentPaymentsPossiblityEnum

## Navigation properties

- CreditCard : SAPB1.CreditCard [Partner=CreditPaymentMethods]
- CreditCardPayment : SAPB1.CreditCardPayment [Partner=CreditPaymentMethods]

# SAPB1.CreditPaymentMethodParams (ComplexType)

## Properties

- PaymentMethodCode : Edm.Int32

# SAPB1.CUPCode (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- Code : Edm.String

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=CUPCode]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=CUPCode]
- Drafts : Collection(SAPB1.Document) [Partner=CUPCode]
- VendorPayments : Collection(SAPB1.Payment) [Partner=CUPCode]
- PaymentDrafts : Collection(SAPB1.Payment) [Partner=CUPCode]
- CreditNotes : Collection(SAPB1.Document) [Partner=CUPCode]
- Invoices : Collection(SAPB1.Document) [Partner=CUPCode]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=CUPCode]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=CUPCode]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=CUPCode]
- Orders : Collection(SAPB1.Document) [Partner=CUPCode]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=CUPCode]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=CUPCode]
- Returns : Collection(SAPB1.Document) [Partner=CUPCode]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=CUPCode]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=CUPCode]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=CUPCode]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=CUPCode]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=CUPCode]
- DownPayments : Collection(SAPB1.Document) [Partner=CUPCode]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=CUPCode]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=CUPCode]
- ReturnRequest : Collection(SAPB1.Document) [Partner=CUPCode]
- Quotations : Collection(SAPB1.Document) [Partner=CUPCode]
- JournalEntries : Collection(SAPB1.JournalEntry) [Partner=CUPCode]
- IncomingPayments : Collection(SAPB1.Payment) [Partner=CUPCode]
- SelfInvoices : Collection(SAPB1.Document) [Partner=CUPCode]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=CUPCode]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=CUPCode]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=CUPCode]

# SAPB1.CUPCodeParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32

# SAPB1.Currency (EntityType)

OpenType: true
Key: Code

## Properties

- Code : Edm.String [required]
- Name : Edm.String
- DocumentsCode : Edm.String
- InternationalDescription : Edm.String
- HundredthName : Edm.String
- EnglishName : Edm.String
- EnglishHundredthName : Edm.String
- PluralInternationalDescription : Edm.String
- PluralHundredthName : Edm.String
- PluralEnglishName : Edm.String
- PluralEnglishHundredthName : Edm.String
- Decimals : SAPB1.CurrenciesDecimalsEnum
- Rounding : SAPB1.RoundingSysEnum
- RoundingInPayment : SAPB1.BoYesNoEnum
- MaxIncomingAmtDiff : Edm.Double
- MaxOutgoingAmtDiff : Edm.Double
- MaxIncomingAmtDiffPercent : Edm.Double
- MaxOutgoingAmtDiffPercent : Edm.Double

## Navigation properties

- ChartOfAccounts : Collection(SAPB1.ChartOfAccount) [Partner=Currency]
- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=Currency]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=Currency]
- Drafts : Collection(SAPB1.Document) [Partner=Currency]
- BankStatements : Collection(SAPB1.BankStatement) [Partner=Currency2]
- AssetManualDepreciation : Collection(SAPB1.AssetDocument) [Partner=Currency2]
- VendorPayments : Collection(SAPB1.Payment) [Partner=Currency]
- WithholdingTaxCodes : Collection(SAPB1.WithholdingTaxCode) [Partner=Currency2]
- PaymentDrafts : Collection(SAPB1.Payment) [Partner=Currency]
- BlanketAgreements : Collection(SAPB1.BlanketAgreement) [Partner=Currency]
- CreditNotes : Collection(SAPB1.Document) [Partner=Currency]
- Invoices : Collection(SAPB1.Document) [Partner=Currency]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=Currency]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=Currency]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=Currency]
- AssetCapitalization : Collection(SAPB1.AssetDocument) [Partner=Currency2]
- AssetCapitalizationCreditMemo : Collection(SAPB1.AssetDocument) [Partner=Currency2]
- Orders : Collection(SAPB1.Document) [Partner=Currency]
- AssetTransfer : Collection(SAPB1.AssetDocument) [Partner=Currency2]
- AssetRetirement : Collection(SAPB1.AssetDocument) [Partner=Currency2]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=Currency]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=Currency]
- Returns : Collection(SAPB1.Document) [Partner=Currency]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=Currency]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=Currency]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=Currency]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=Currency]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=Currency]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=Currency2]
- DownPayments : Collection(SAPB1.Document) [Partner=Currency]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=Currency]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=Currency]
- ReturnRequest : Collection(SAPB1.Document) [Partner=Currency]
- Quotations : Collection(SAPB1.Document) [Partner=Currency]
- IncomingPayments : Collection(SAPB1.Payment) [Partner=Currency]
- SelfInvoices : Collection(SAPB1.Document) [Partner=Currency]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=Currency]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=Currency]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=Currency]

# SAPB1.CurrencyParams (ComplexType)

## Properties

- Code : Edm.String

# SAPB1.CurrencyRestriction (ComplexType)

OpenType: true

## Properties

- PaymentMethodCode : Edm.String
- CurrencyCode : Edm.String
- CurrencyName : Edm.String
- Choose : SAPB1.BoYesNoEnum

# SAPB1.CurrentServerTime (ComplexType)

## Properties

- CurrentDate : Edm.DateTimeOffset
- CurrentTime : Edm.TimeOfDay

# SAPB1.CustomerEquipmentCard (EntityType)

OpenType: true
Key: EquipmentCardNum

## Properties

- EquipmentCardNum : Edm.Int32 [required]
- CustomerCode : Edm.String
- CustomerName : Edm.String
- ContactEmployeeCode : Edm.Int32
- DirectCustomerCode : Edm.String
- DirectCustomerName : Edm.String
- ManufacturerSerialNum : Edm.String
- InternalSerialNum : Edm.String
- RequiredResolutionTime : Edm.Int32
- RequiredResolutionUnit : SAPB1.BoResolutionUnits
- ItemCode : Edm.String
- ItemDescription : Edm.String
- InvoiceCode : Edm.Int32
- InvoiceNumber : Edm.Int32
- DeliveryDate : Edm.DateTimeOffset
- ContactPhone : Edm.String
- Street : Edm.String
- Block : Edm.String
- ZipCode : Edm.String
- City : Edm.String
- County : Edm.String
- CountryCode : Edm.String
- StateCode : Edm.String
- InstallLocation : Edm.String
- ContractCode : Edm.Int32
- ContractStartDate : Edm.DateTimeOffset
- ContractEndDate : Edm.DateTimeOffset
- DeliveryCode : Edm.Int32
- DeliveryNumber : Edm.Int32
- StatusOfSerialNumber : SAPB1.BoSerialNumberStatus
- ReplaceSN : Edm.Int32
- DefaultTechnician : Edm.Int32
- ReplacedBySN : Edm.Int32
- Defaultterritory : Edm.Int32
- BuildingFloorRoom : Edm.String
- AttachmentEntry : Edm.Int32
- StreetNo : Edm.String
- ServiceBPType : SAPB1.BoEquipmentBPType
- CustomerEquipmentCardBusinessPartners : Collection(SAPB1.CustomerEquipmentCardBusinessPartner)

## Navigation properties

- BusinessPartner : SAPB1.BusinessPartner [Partner=CustomerEquipmentCards]
- Item : SAPB1.Item [Partner=CustomerEquipmentCards]
- Country : SAPB1.Country [Partner=CustomerEquipmentCards]
- ServiceContract : SAPB1.ServiceContract [Partner=CustomerEquipmentCards]
- EmployeeInfo : SAPB1.EmployeeInfo [Partner=CustomerEquipmentCards]
- Territory : SAPB1.Territory [Partner=CustomerEquipmentCards]
- Attachments2 : SAPB1.Attachments2 [Partner=CustomerEquipmentCards]

# SAPB1.CustomerEquipmentCardBusinessPartner (ComplexType)

OpenType: true

## Properties

- BPCode : Edm.String

# SAPB1.CustomerEquipmentCardParams (ComplexType)

## Properties

- EquipmentCardNum : Edm.Int32

# SAPB1.CustomsDeclaration (EntityType)

OpenType: true
Key: CCDNum

## Properties

- CCDNum : Edm.String [required]
- Date : Edm.DateTimeOffset
- CustomsBroker : Edm.String
- DocNum : Edm.String
- DocDate : Edm.DateTimeOffset
- SupplyNum : Edm.String
- SupplyDate : Edm.DateTimeOffset
- CustomsTerminal : Edm.String
- PaymentKey : Edm.String

# SAPB1.CustomsDeclarationParams (ComplexType)

## Properties

- CCDNum : Edm.String

# SAPB1.CustomsGroup (EntityType)

OpenType: true
Key: Code

## Properties

- Code : Edm.Int32 [required]
- Name : Edm.String
- Number : Edm.String
- Customs : Edm.Double
- Purchase : Edm.Double
- Other : Edm.Double
- Total : Edm.Double
- Locked : SAPB1.BoYesNoEnum
- CustomsAllocationAccount : Edm.String
- CustomsExpenseAccount : Edm.String
- PortAddress : Edm.String
- PortState : Edm.String

## Navigation properties

- ChartOfAccount : SAPB1.ChartOfAccount [Partner=CustomsGroups]
- Items : Collection(SAPB1.Item) [Partner=CustomsGroup]

# SAPB1.CustomsGroupParams (ComplexType)

## Properties

- Code : Edm.Int32

# SAPB1.CycleCountDetermination (EntityType)

Key: WarehouseCode

## Properties

- WarehouseCode : Edm.String [required]
- CycleBy : SAPB1.CycleCountDeterminationCycleByEnum
- CycleCountDeterminationSetupCollection : Collection(SAPB1.CycleCountDeterminationSetup)

# SAPB1.CycleCountDeterminationParams (ComplexType)

## Properties

- WarehouseCode : Edm.String
- CycleBy : Edm.Int32

# SAPB1.CycleCountDeterminationSetup (ComplexType)

## Properties

- WarehouseCode : Edm.String
- Entry : Edm.Int32
- CycleCode : Edm.Int32
- Alert : SAPB1.BoYesNoEnum
- DestinationUser : Edm.Int32
- NextCountingDate : Edm.DateTimeOffset
- Time : Edm.TimeOfDay
- ExcludeItemsWithZeroQuantity : SAPB1.BoYesNoEnum
- ChangeExistingItems : SAPB1.BoYesNoEnum

# SAPB1.DashboardPackageImportParams (ComplexType)

## Properties

- PackageFilePath : Edm.String
- ImportQueries : SAPB1.BoYesNoEnum
- ForceOverwriteQuery : SAPB1.BoYesNoEnum
- ForceOverwritePackage : SAPB1.BoYesNoEnum

# SAPB1.DashboardPackageParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32

# SAPB1.DataSensitiveStatus (ComplexType)

## Properties

- DataSensitiveStatusProperty : SAPB1.DataSensitiveStatusEnum

# SAPB1.DatevRun (EntityType)

OpenType: true
Key: RunId

## Properties

- RunId : Edm.Int32 [required]
- Status : Edm.String
- Description : Edm.String
- ExportPath : Edm.String
- Updater : Edm.String
- GLAccounts : Edm.String
- Suppliers : Edm.String
- Customers : Edm.String
- Journals : Edm.String
- AllJETypes : Edm.String
- Manual : Edm.String
- Purchase : Edm.String
- Sales : Edm.String
- DateType : Edm.String
- StartDate : Edm.DateTimeOffset
- EndDate : Edm.DateTimeOffset
- StartFiscalYear : Edm.DateTimeOffset
- UserSign : Edm.Int32
- CreateDate : Edm.DateTimeOffset
- CreateTime : Edm.TimeOfDay
- UpdateDate : Edm.DateTimeOffset
- UserSign2 : Edm.Int32

## Navigation properties

- User : SAPB1.User [Partner=DatevRuns]

# SAPB1.DatevRunParams (ComplexType)

## Properties

- RunId : Edm.Int32

# SAPB1.DecimalData (ComplexType)

## Properties

- Value : Edm.Double
- Context : SAPB1.RoundingContextEnum
- Currency : Edm.String

# SAPB1.DeductibleTax (EntityType)

Key: Code

## Properties

- Code : Edm.String [required]
- Name : Edm.String
- Inactive : SAPB1.BoYesNoEnum
- Category : SAPB1.BoVatCategoryEnum
- DeductibleTaxRate : Edm.Double

# SAPB1.DeductibleTaxParams (ComplexType)

## Properties

- Code : Edm.String
- Name : Edm.String

# SAPB1.DeductionTaxGroup (EntityType)

OpenType: true
Key: GroupKey

## Properties

- GroupKey : Edm.Int32 [required]
- GroupCode : SAPB1.BoDeductionTaxGroupCodeEnum
- GroupName : Edm.String
- MaxRedin : Edm.Double
- GroupExtendedCode : Edm.String

## Navigation properties

- DeductionTaxSubGroup : SAPB1.DeductionTaxSubGroup [Partner=DeductionTaxGroups]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=DeductionTaxGroup]

# SAPB1.DeductionTaxGroupParams (ComplexType)

## Properties

- GroupKey : Edm.Int32

# SAPB1.DeductionTaxHierarchies_Line (ComplexType)

OpenType: true

## Properties

- RowNumber : Edm.Int32
- DeductionPercent : Edm.Double
- MaximumTotal : Edm.Double

# SAPB1.DeductionTaxHierarchy (EntityType)

OpenType: true
Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- BPCode : Edm.String
- HierarchyCode : Edm.String
- HierarchyName : Edm.String
- ValidFrom : Edm.DateTimeOffset
- ValidUntil : Edm.DateTimeOffset
- DeductionPercent : Edm.Double
- MaximumTotal : Edm.Double
- LastUpdated : Edm.DateTimeOffset
- DeductionTaxHierarchies_Lines : Collection(SAPB1.DeductionTaxHierarchies_Line)

## Navigation properties

- BusinessPartner : SAPB1.BusinessPartner [Partner=DeductionTaxHierarchies]

# SAPB1.DeductionTaxHierarchyParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32

# SAPB1.DeductionTaxSubGroup (EntityType)

Key: GroupCode

## Properties

- GroupCode : Edm.String [required]
- GroupName : Edm.String

## Navigation properties

- DeductionTaxGroups : Collection(SAPB1.DeductionTaxGroup) [Partner=DeductionTaxSubGroup]

# SAPB1.DeductionTaxSubGroupParams (ComplexType)

## Properties

- GroupCode : Edm.String
- GroupName : Edm.String

# SAPB1.DefaultCreditCard (ComplexType)

OpenType: true

## Properties

- Code : Edm.String
- CreditAccountCode : Edm.String
- CreditCardCode : Edm.Int32

# SAPB1.DefaultDocument (ComplexType)

OpenType: true

## Properties

- AddExport : SAPB1.BoYesNoEnum
- AddPrint : SAPB1.BoYesNoEnum
- Code : Edm.String
- EnglishKeyboardEnteringBPC : SAPB1.BoYesNoEnum
- NoofCopies : Edm.Int32
- NoofCopiesforManualDoc : Edm.Int32
- ObjectType : Edm.String
- PermanentRemark : Edm.String
- PrintDiscountData : SAPB1.BoYesNoEnum
- PrintToals : SAPB1.BoYesNoEnum
- PrintVendorCatalogNo : SAPB1.BoYesNoEnum
- TotalsRounding : SAPB1.BoYesNoEnum

# SAPB1.DefaultElectronicSeriesParams (ComplexType)

## Properties

- Series : Edm.Int32
- ElectronicSeries : Edm.Int32

# SAPB1.DefaultElementsforCR (EntityType)

Key: Code

## Properties

- Code : Edm.Int32 [required]
- Name : Edm.String

# SAPB1.DefaultElementsforCRParams (ComplexType)

## Properties

- Code : Edm.Int32
- Name : Edm.String

# SAPB1.DefaultReportParams (ComplexType)

## Properties

- ReportCode : Edm.String
- LayoutCode : Edm.String
- UserID : Edm.Int32
- CardCode : Edm.String

# SAPB1.Department (EntityType)

Key: Code

## Properties

- Code : Edm.Int32 [required]
- Name : Edm.String
- Description : Edm.String

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=Department]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=Department]
- Drafts : Collection(SAPB1.Document) [Partner=Department]
- Users : Collection(SAPB1.User) [Partner=Department2]
- CreditNotes : Collection(SAPB1.Document) [Partner=Department]
- Invoices : Collection(SAPB1.Document) [Partner=Department]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=Department]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=Department]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=Department]
- Orders : Collection(SAPB1.Document) [Partner=Department]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=Department]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=Department]
- Returns : Collection(SAPB1.Document) [Partner=Department]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=Department]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=Department]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=Department]
- EmployeesInfo : Collection(SAPB1.EmployeeInfo) [Partner=Department2]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=Department]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=Department]
- DownPayments : Collection(SAPB1.Document) [Partner=Department]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=Department]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=Department]
- ReturnRequest : Collection(SAPB1.Document) [Partner=Department]
- Quotations : Collection(SAPB1.Document) [Partner=Department]
- SelfInvoices : Collection(SAPB1.Document) [Partner=Department]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=Department]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=Department]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=Department]

# SAPB1.DepartmentParams (ComplexType)

## Properties

- Code : Edm.Int32
- Name : Edm.String

# SAPB1.Deposit (EntityType)

OpenType: true
Key: AbsEntry

## Properties

- DepositNumber : Edm.Int32
- AbsEntry : Edm.Int32 [required]
- DepositType : SAPB1.BoDepositTypeEnum
- DepositDate : Edm.DateTimeOffset
- DepositCurrency : Edm.String
- DepositAccount : Edm.String
- DepositorName : Edm.String
- Bank : Edm.String
- BankAccountNum : Edm.String
- BankBranch : Edm.String
- BankReference : Edm.String
- JournalRemarks : Edm.String
- TotalLC : Edm.Double
- TotalFC : Edm.Double
- TotalSC : Edm.Double
- AllocationAccount : Edm.String
- DocRate : Edm.Double
- TaxAccount : Edm.String
- TaxAmount : Edm.Double
- CommissionAccount : Edm.String
- Commission : Edm.Double
- CommissionDate : Edm.DateTimeOffset
- TaxCode : Edm.String
- DepositAccountType : SAPB1.BoDepositAccountTypeEnum
- ReconcileAfterDeposit : SAPB1.BoYesNoEnum
- VoucherAccount : Edm.String
- Series : Edm.Int32
- Project : Edm.String
- DistributionRule : Edm.String
- DistributionRule2 : Edm.String
- DistributionRule3 : Edm.String
- DistributionRule4 : Edm.String
- DistributionRule5 : Edm.String
- CommissionCurrency : Edm.String
- CommissionSC : Edm.Double
- CommissionFC : Edm.Double
- TaxAmountSC : Edm.Double
- TaxAmountFC : Edm.Double
- BPLID : Edm.Int32
- CheckDepositType : SAPB1.BoCheckDepositTypeEnum
- AttachmentEntry : Edm.Int32
- IncomeTaxAccount : Edm.String
- IncomeTaxAmount : Edm.Double
- IncomeTaxAmountSC : Edm.Double
- IncomeTaxAmountFC : Edm.Double
- CheckLines : Collection(SAPB1.CheckLine)
- CreditLines : Collection(SAPB1.CreditLine)
- BOELines : Collection(SAPB1.BOELine)

## Navigation properties

- VatGroup : SAPB1.VatGroup [Partner=Deposits]
- Project2 : SAPB1.Project [Partner=Deposits]
- DistributionRule6 : SAPB1.DistributionRule [Partner=Deposits]
- BusinessPlace : SAPB1.BusinessPlace [Partner=Deposits]
- Attachments2 : SAPB1.Attachments2 [Partner=Deposits]

# SAPB1.DepositParams (ComplexType)

## Properties

- DepositNumber : Edm.Int32
- AbsEntry : Edm.Int32
- Series : Edm.Int32

# SAPB1.DepreciationArea (EntityType)

Key: Code

## Properties

- Code : Edm.String [required]
- Description : Edm.String
- PostingOfDepreciation : SAPB1.PostingOfDepreciationEnum
- RetirementMethod : SAPB1.RetirementMethodEnum
- AreaType : SAPB1.AreaTypeEnum
- DerivedArea : Edm.String
- MainBookingArea : SAPB1.BoYesNoEnum
- DirectRevenuePosting : SAPB1.BoYesNoEnum
- TaxCreditControl : SAPB1.BoYesNoEnum
- TaxType : Edm.Int32
- BPForTaxCorrection : Edm.String
- ItemForTaxCorrection : Edm.String
- UsageForTaxCorrection : Edm.Int32

## Navigation properties

- AssetManualDepreciation : Collection(SAPB1.AssetDocument) [Partner=DepreciationArea2]
- AssetRevaluations : Collection(SAPB1.AssetRevaluation) [Partner=DepreciationArea2]
- SalesTaxAuthoritiesType : SAPB1.SalesTaxAuthoritiesType [Partner=DepreciationAreas]
- BusinessPartner : SAPB1.BusinessPartner [Partner=DepreciationAreas]
- Item : SAPB1.Item [Partner=DepreciationAreas]
- NotaFiscalUsage : SAPB1.NotaFiscalUsage [Partner=DepreciationAreas]
- AssetCapitalization : Collection(SAPB1.AssetDocument) [Partner=DepreciationArea2]
- AssetCapitalizationCreditMemo : Collection(SAPB1.AssetDocument) [Partner=DepreciationArea2]
- AssetTransfer : Collection(SAPB1.AssetDocument) [Partner=DepreciationArea2]
- AssetRetirement : Collection(SAPB1.AssetDocument) [Partner=DepreciationArea2]

# SAPB1.DepreciationAreaParams (ComplexType)

## Properties

- Code : Edm.String
- Description : Edm.String

# SAPB1.DepreciationLevel (ComplexType)

## Properties

- Level : Edm.Int32
- DepreciationCalculationBase : SAPB1.DepreciationCalculationBaseEnum
- NumberOfYears : Edm.Int32
- Percentage : Edm.Double
- Amount : Edm.Double

# SAPB1.DepreciationType (EntityType)

Key: Code

## Properties

- Code : Edm.String [required]
- Description : Edm.String
- DepreciationMethod : SAPB1.DepreciationMethodEnum
- MinimumDepreciatedValue : Edm.Double
- RoundYearEndBookValue : SAPB1.BoYesNoEnum
- IncludeSalvageInDepreciation : SAPB1.BoYesNoEnum
- SalvagePercentage : Edm.Double
- AcquisitionPeriodControl : SAPB1.AcquisitionPeriodControlEnum
- SubsequentAcquisitionPeriodControl : SAPB1.SubsequentAcquisitionPeriodControlEnum
- RetirementPeriodControl : SAPB1.RetirementPeriodControlEnum
- AcquisitionProRataType : SAPB1.AcquisitionProRataTypeEnum
- SubsequentAcquisitionProRataType : SAPB1.SubsequentAcquisitionProRataTypeEnum
- RetirementProRataType : SAPB1.RetirementProRataTypeEnum
- PercentageOfDepreciationReversedInRetirementYear : Edm.Double
- ValidFrom : Edm.DateTimeOffset
- ValidTo : Edm.DateTimeOffset
- StraightLineCalculationMethod : SAPB1.StraightLineCalculationMethodEnum
- StraightLinePercentage : Edm.Double
- StraightLinePeriodControlDepreciationPeriods : SAPB1.StraightLinePeriodControlDepreciationPeriodsEnum
- StraightLinePeriodControlFactor : Edm.Double
- DecliningPercentage : Edm.Double
- DecliningFactor : Edm.Double
- DecliningChangeTo : Edm.String
- SpecialDepreciationCalculationMethod : SAPB1.SpecialDepreciationCalculationMethodEnum
- SpecialDepreciationConcessionPeriodYears : Edm.Int32
- SpecialDepreciationMaximumPercentage : Edm.Double
- SpecialDepreciationNormalDepreciation : Edm.String
- SpecialDepreciationAlternativeDepreciation : Edm.String
- DepreciationTypePool : Edm.String
- ManualDepreciationReduceDepreciationBase : SAPB1.BoYesNoEnum
- SpecialDepreciationMaximumAmount : Edm.Double
- SpecialDepreciationMaximumFlag : SAPB1.SpecialDepreciationMaximumFlagEnum
- CalculationBase : SAPB1.CalculationBaseEnum
- DepreciationEndAtLastFullYear : SAPB1.BoYesNoEnum
- IncludePreviousDepreciationInCapitalizationPeriod : SAPB1.BoYesNoEnum
- DeltaCoefficient : Edm.Int32
- MaximumDepreciableValue : Edm.Double
- FactorOnlyRelevantToFirstFiscalYear : SAPB1.BoYesNoEnum
- TransferSourcePeriodControl : SAPB1.TransferSourcePeriodControlEnum
- TransferTargetPeriodControl : SAPB1.TransferTargetPeriodControlEnum
- TransferSourceProRataType : SAPB1.TransferSourceProRataTypeEnum
- TransferTargetProRataType : SAPB1.TransferTargetProRataTypeEnum
- RoundingMethod : SAPB1.DepreciationRoundingMethodEnum
- DepreciationLevelCollection : Collection(SAPB1.DepreciationLevel)

## Navigation properties

- AssetManualDepreciation : Collection(SAPB1.AssetDocument) [Partner=DepreciationType]
- DepreciationTypePool2 : SAPB1.DepreciationTypePool [Partner=DepreciationTypes]
- AssetCapitalization : Collection(SAPB1.AssetDocument) [Partner=DepreciationType]
- AssetCapitalizationCreditMemo : Collection(SAPB1.AssetDocument) [Partner=DepreciationType]
- AssetTransfer : Collection(SAPB1.AssetDocument) [Partner=DepreciationType]
- AssetRetirement : Collection(SAPB1.AssetDocument) [Partner=DepreciationType]

# SAPB1.DepreciationTypeParams (ComplexType)

## Properties

- Code : Edm.String
- Description : Edm.String

# SAPB1.DepreciationTypePool (EntityType)

Key: Code

## Properties

- Code : Edm.String [required]
- Description : Edm.String

## Navigation properties

- DepreciationTypes : Collection(SAPB1.DepreciationType) [Partner=DepreciationTypePool2]

# SAPB1.DepreciationTypePoolParams (ComplexType)

## Properties

- Code : Edm.String
- Description : Edm.String

# SAPB1.DeterminationCriteria (EntityType)

Key: DmcId

## Properties

- DmcId : Edm.Int32 [required]
- DeterminationCriteriaProperty : Edm.String
- IsActive : SAPB1.BoYesNoEnum
- Priority : Edm.Int32

# SAPB1.DeterminationCriteriaParams (ComplexType)

## Properties

- DmcId : Edm.Int32

# SAPB1.Dimension (EntityType)

OpenType: true
Key: DimensionCode

## Properties

- DimensionCode : Edm.Int32 [required]
- DimensionName : Edm.String
- IsActive : SAPB1.BoYesNoEnum
- DimensionDescription : Edm.String

## Navigation properties

- ProfitCenters : Collection(SAPB1.ProfitCenter) [Partner=Dimension]
- DistributionRules : Collection(SAPB1.DistributionRule) [Partner=Dimension]

# SAPB1.DimensionParams (ComplexType)

## Properties

- DimensionCode : Edm.Int32
- DimensionName : Edm.String

# SAPB1.DiscountGroup (ComplexType)

## Properties

- ObjectEntry : Edm.String
- DiscountPercentage : Edm.Double
- BPCode : Edm.String
- BaseObjectType : SAPB1.DiscountGroupBaseObjectEnum

# SAPB1.DiscountGroupLine (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- ObjectType : SAPB1.DiscountGroupBaseObjectEnum
- ObjectCode : Edm.String
- DiscountType : SAPB1.DiscountGroupDiscountTypeEnum
- Discount : Edm.Double
- PaidQuantity : Edm.Double
- FreeQuantity : Edm.Double
- MaximumFreeQuantity : Edm.Double

# SAPB1.DiscountLine (ComplexType)

## Properties

- DiscountCode : Edm.String
- LineId : Edm.Int32
- NumOfDays : Edm.Int32
- Discount : Edm.Double
- Day : Edm.Int32
- Month : Edm.Int32

# SAPB1.DistributableLine (ComplexType)

OpenType: true

## Properties

- DocumentEntry : Edm.Int32
- SourceType : SAPB1.ISDDocumentTypeEnum
- SourceLocationCode : Edm.Int32
- SourceLocationName : Edm.String
- SourceGSTTaxType : SAPB1.ISDSTATypeEnum
- SourceTaxAccount : Edm.String
- SourceITCType : SAPB1.ISDITCTypeEnum
- AvailableAmount : Edm.Double
- DistributeAmount : Edm.Double

# SAPB1.DistributedLine (ComplexType)

OpenType: true

## Properties

- DocumentEntry : Edm.Int32
- TargetLocationCode : Edm.Int32
- TargetLocationName : Edm.String
- TargetGSTTaxType : SAPB1.ISDSTATypeEnum
- TargetTaxAccount : Edm.String
- AllocatedAmount : Edm.Double

# SAPB1.DistributionList (EntityType)

OpenType: true
Key: Code

## Properties

- Code : Edm.Int32 [required]
- Name : Edm.String
- DistributionListLines : Collection(SAPB1.DistributionListLine)

# SAPB1.DistributionListLine (ComplexType)

OpenType: true

## Properties

- LineNumber : Edm.Int32
- DistributionType : Edm.String
- DistributionCode : Edm.String
- Email : Edm.String
- PortNum : Edm.String
- Fax : Edm.String

# SAPB1.DistributionListParams (ComplexType)

## Properties

- Code : Edm.Int32
- Name : Edm.String

# SAPB1.DistributionRule (EntityType)

OpenType: true
Key: FactorCode

## Properties

- FactorCode : Edm.String [required]
- FactorDescription : Edm.String
- TotalFactor : Edm.Double
- Direct : Edm.String
- InWhichDimension : Edm.Int32
- Active : SAPB1.BoYesNoEnum
- IsFixedAmount : SAPB1.BoYesNoEnum
- DistributionRuleLines : Collection(SAPB1.DistributionRuleLine)

## Navigation properties

- ChartOfAccounts : Collection(SAPB1.ChartOfAccount) [Partner=DistributionRule]
- Deposits : Collection(SAPB1.Deposit) [Partner=DistributionRule6]
- ProductionOrders : Collection(SAPB1.ProductionOrder) [Partner=DistributionRule6]
- AdditionalExpenses : Collection(SAPB1.AdditionalExpense) [Partner=DistributionRule6]
- Dimension : SAPB1.Dimension [Partner=DistributionRules]
- BudgetScenarios : Collection(SAPB1.BudgetScenario) [Partner=DistributionRule6]
- ProductTrees : Collection(SAPB1.ProductTree) [Partner=DistributionRule6]

# SAPB1.DistributionRuleLine (ComplexType)

## Properties

- CenterCode : Edm.String
- TotalInCenter : Edm.Double
- EffectiveFrom : Edm.DateTimeOffset
- EffectiveTo : Edm.DateTimeOffset

# SAPB1.DistributionRuleParams (ComplexType)

## Properties

- FactorCode : Edm.String
- FactorDescription : Edm.String

# SAPB1.DNFCodeSetup (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- NCMCode : Edm.Int32
- DNFCode : Edm.String
- UoM : Edm.String
- Factor : Edm.Double

## Navigation properties

- NCMCodeSetup : SAPB1.NCMCodeSetup [Partner=DNFCodeSetup]
- Items : Collection(SAPB1.Item) [Partner=DNFCodeSetup]

# SAPB1.DNFCodeSetupParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- NCMCode : Edm.Int32
- DNFCode : Edm.String

# SAPB1.DocExpenseTaxJurisdiction (ComplexType)

OpenType: true

## Properties

- JurisdictionCode : Edm.String
- JurisdictionType : Edm.Int32
- TaxAmount : Edm.Double
- TaxAmountSC : Edm.Double
- TaxAmountFC : Edm.Double
- TaxRate : Edm.Double
- DocEntry : Edm.Int32
- LineNumber : Edm.Int32
- RowSequence : Edm.Int32
- ExternalCalcTaxRate : Edm.Double
- ExternalCalcTaxAmount : Edm.Double
- ExternalCalcTaxAmountFC : Edm.Double
- ExternalCalcTaxAmountSC : Edm.Double

# SAPB1.DocFreightEBooksDetail (ComplexType)

OpenType: true

## Properties

- IncomeClassificationType : Edm.Int32
- IncomeClassificationCategory : Edm.Int32
- ExpensesClassificationType : Edm.Int32
- ExpensesClassificationCategory : Edm.Int32
- NetValueLC : Edm.Double
- NetValueFC : Edm.Double
- NetValueSC : Edm.Double
- VatCategory : Edm.Int32
- WithheldPercentCategory : Edm.Int32
- WithheldAmountLC : Edm.Double
- WithheldAmountFC : Edm.Double
- WithheldAmountSC : Edm.Double
- VatClassificationType : Edm.Int32
- VatClassificationCategory : Edm.Int32
- VATExemptionCause : Edm.Int32

# SAPB1.DocLinePickList (ComplexType)

## Properties

- PickListEntry : Edm.Int32
- PickListLineNum : Edm.Int32
- PickListBatchAndBinLineNum : Edm.Int32

# SAPB1.DocsInWTGroups (ComplexType)

OpenType: true

## Properties

- DocEntry : Edm.Int32
- DocObjType : Edm.String
- VATAmount : Edm.Double
- DocTotal : Edm.Double
- BaseAmount : Edm.Double
- AccumAmount : Edm.Double
- PerceptAmount : Edm.Double
- Percent : Edm.Double

# SAPB1.Document (EntityType)

OpenType: true
Key: DocEntry
Filtered properties: 45

## Properties

- DocEntry : Edm.Int32 [required]
- DocNum : Edm.Int32
- DocType : SAPB1.BoDocumentTypes
- HandWritten : SAPB1.BoYesNoEnum
- Printed : SAPB1.PrintStatusEnum
- DocDate : Edm.DateTimeOffset
- DocDueDate : Edm.DateTimeOffset
- CardCode : Edm.String
- CardName : Edm.String
- Address : Edm.String
- NumAtCard : Edm.String
- DocTotal : Edm.Double
- AttachmentEntry : Edm.Int32
- DocCurrency : Edm.String
- DocRate : Edm.Double
- Reference1 : Edm.String
- Reference2 : Edm.String
- Comments : Edm.String
- JournalMemo : Edm.String
- PaymentGroupCode : Edm.Int32
- DocTime : Edm.TimeOfDay
- SalesPersonCode : Edm.Int32
- TransportationCode : Edm.Int32
- Confirmed : SAPB1.BoYesNoEnum
- ImportFileNum : Edm.Int32
- SummeryType : SAPB1.BoDocSummaryTypes
- ContactPersonCode : Edm.Int32
- ShowSCN : SAPB1.BoYesNoEnum
- Series : Edm.Int32
- TaxDate : Edm.DateTimeOffset
- PartialSupply : SAPB1.BoYesNoEnum
- DocObjectCode : SAPB1.BoObjectTypes
- ShipToCode : Edm.String
- Indicator : Edm.String
- FederalTaxID : Edm.String
- DiscountPercent : Edm.Double
- PaymentReference : Edm.String
- CreationDate : Edm.DateTimeOffset
- UpdateDate : Edm.DateTimeOffset
- FinancialPeriod : Edm.Int32
- UserSign : Edm.Int32
- TransNum : Edm.Int32
- VatSum : Edm.Double
- VatSumSys : Edm.Double
- VatSumFc : Edm.Double
- NetProcedure : SAPB1.BoYesNoEnum
- DocTotalFc : Edm.Double
- DocTotalSys : Edm.Double
- Form1099 : Edm.Int32
- Box1099 : Edm.String
- RevisionPo : SAPB1.BoYesNoEnum
- RequriedDate : Edm.DateTimeOffset
- CancelDate : Edm.DateTimeOffset
- BlockDunning : SAPB1.BoYesNoEnum
- Submitted : SAPB1.BoYesNoEnum
- Segment : Edm.Int32
- PickStatus : SAPB1.BoYesNoEnum
- Pick : SAPB1.BoYesNoEnum
- PaymentMethod : Edm.String
- PaymentBlock : SAPB1.BoYesNoEnum
- PaymentBlockEntry : Edm.Int32
- CentralBankIndicator : Edm.String
- MaximumCashDiscount : SAPB1.BoYesNoEnum
- Reserve : SAPB1.BoYesNoEnum
- Project : Edm.String
- ExemptionValidityDateFrom : Edm.DateTimeOffset
- ExemptionValidityDateTo : Edm.DateTimeOffset
- WareHouseUpdateType : SAPB1.BoDocWhsUpdateTypes
- Rounding : SAPB1.BoYesNoEnum
- ExternalCorrectedDocNum : Edm.String
- InternalCorrectedDocNum : Edm.Int32
- NextCorrectingDocument : Edm.Int32
- DeferredTax : SAPB1.BoYesNoEnum
- TaxExemptionLetterNum : Edm.String
- WTApplied : Edm.Double
- WTAppliedFC : Edm.Double
- BillOfExchangeReserved : SAPB1.BoYesNoEnum
- AgentCode : Edm.String
- WTAppliedSC : Edm.Double
- TotalEqualizationTax : Edm.Double
- TotalEqualizationTaxFC : Edm.Double
- TotalEqualizationTaxSC : Edm.Double
- NumberOfInstallments : Edm.Int32
- ApplyTaxOnFirstInstallment : SAPB1.BoYesNoEnum
- TaxOnInstallments : SAPB1.BoTaxOnInstallmentsTypeEnum
- WTNonSubjectAmount : Edm.Double
- WTNonSubjectAmountSC : Edm.Double
- WTNonSubjectAmountFC : Edm.Double
- WTExemptedAmount : Edm.Double
- WTExemptedAmountSC : Edm.Double
- WTExemptedAmountFC : Edm.Double
- BaseAmount : Edm.Double
- BaseAmountSC : Edm.Double
- BaseAmountFC : Edm.Double
- WTAmount : Edm.Double
- WTAmountSC : Edm.Double
- WTAmountFC : Edm.Double
- VatDate : Edm.DateTimeOffset
- DocumentsOwner : Edm.Int32
- FolioPrefixString : Edm.String
- FolioNumber : Edm.Int32
- DocumentSubType : SAPB1.BoDocumentSubType
- BPChannelCode : Edm.String
- BPChannelContact : Edm.Int32
- Address2 : Edm.String
- DocumentStatus : SAPB1.BoStatus
- PeriodIndicator : Edm.String
- PayToCode : Edm.String
- ManualNumber : Edm.String
- UseShpdGoodsAct : SAPB1.BoYesNoEnum
- IsPayToBank : SAPB1.BoYesNoEnum
- PayToBankCountry : Edm.String
- PayToBankCode : Edm.String
- PayToBankAccountNo : Edm.String
- PayToBankBranch : Edm.String
- BPL_IDAssignedToInvoice : Edm.Int32
- DownPayment : Edm.Double
- ReserveInvoice : SAPB1.BoYesNoEnum
- LanguageCode : Edm.Int32
- TrackingNumber : Edm.String
- PickRemark : Edm.String
- ClosingDate : Edm.DateTimeOffset
- SequenceCode : Edm.Int32
- SequenceSerial : Edm.Int32
- SeriesString : Edm.String
- SubSeriesString : Edm.String
- SequenceModel : Edm.String
- UseCorrectionVATGroup : SAPB1.BoYesNoEnum
- TotalDiscount : Edm.Double
- DownPaymentAmount : Edm.Double
- DownPaymentPercentage : Edm.Double
- DownPaymentType : SAPB1.DownPaymentTypeEnum
- DownPaymentAmountSC : Edm.Double
- DownPaymentAmountFC : Edm.Double
- VatPercent : Edm.Double
- ServiceGrossProfitPercent : Edm.Double
- OpeningRemarks : Edm.String
- ClosingRemarks : Edm.String
- RoundingDiffAmount : Edm.Double
- RoundingDiffAmountFC : Edm.Double
- RoundingDiffAmountSC : Edm.Double
- Cancelled : SAPB1.BoYesNoEnum
- SignatureInputMessage : Edm.String
- SignatureDigest : Edm.String
- CertificationNumber : Edm.String
- PrivateKeyVersion : Edm.Int32
- ControlAccount : Edm.String
- InsuranceOperation347 : SAPB1.BoYesNoEnum
- ArchiveNonremovableSalesQuotation : SAPB1.BoYesNoEnum
- GTSChecker : Edm.Int32
- GTSPayee : Edm.Int32
- ExtraMonth : Edm.Int32
- ExtraDays : Edm.Int32
- CashDiscountDateOffset : Edm.Int32
- StartFrom : SAPB1.BoPayTermDueTypes
- NTSApproved : SAPB1.BoYesNoEnum
- ETaxWebSite : Edm.Int32
- ETaxNumber : Edm.String
- NTSApprovedNumber : Edm.String
- EDocGenerationType : SAPB1.EDocGenerationTypeEnum
- EDocSeries : Edm.Int32
- EDocNum : Edm.String
- EDocExportFormat : Edm.Int32
- EDocStatus : SAPB1.EDocStatusEnum
- EDocErrorCode : Edm.String
- EDocErrorMessage : Edm.String
- DownPaymentStatus : SAPB1.BoSoStatus
- GroupSeries : Edm.Int32
- GroupNumber : Edm.Int32
- GroupHandWritten : SAPB1.BoYesNoEnum
- ReopenOriginalDocument : SAPB1.BoYesNoEnum
- ReopenManuallyClosedOrCanceledDocument : SAPB1.BoYesNoEnum
- CreateOnlineQuotation : SAPB1.BoYesNoEnum
- POSEquipmentNumber : Edm.String
- POSManufacturerSerialNumber : Edm.String
- POSCashierNumber : Edm.Int32
- ApplyCurrentVATRatesForDownPaymentsToDraw : SAPB1.BoYesNoEnum
- ClosingOption : SAPB1.ClosingOptionEnum
- SpecifiedClosingDate : Edm.DateTimeOffset
- OpenForLandedCosts : SAPB1.BoYesNoEnum
- AuthorizationStatus : SAPB1.DocumentAuthorizationStatusEnum
- TotalDiscountFC : Edm.Double
- TotalDiscountSC : Edm.Double
- RelevantToGTS : SAPB1.BoYesNoEnum
- BPLName : Edm.String
- VATRegNum : Edm.String
- AnnualInvoiceDeclarationReference : Edm.Int32
- Supplier : Edm.String
- Releaser : Edm.Int32
- Receiver : Edm.Int32
- BlanketAgreementNumber : Edm.Int32
- IsAlteration : SAPB1.BoYesNoEnum
- CancelStatus : SAPB1.CancelStatusEnum
- DraftKey : Edm.Int32
- AssetValueDate : Edm.DateTimeOffset
- Requester : Edm.String
- RequesterName : Edm.String
- RequesterBranch : Edm.Int32
- RequesterDepartment : Edm.Int32
- RequesterEmail : Edm.String
- SendNotification : SAPB1.BoYesNoEnum
- ReqType : Edm.Int32
- ReqCode : Edm.String
- InvoicePayment : SAPB1.BoYesNoEnum
- DocumentDelivery : SAPB1.DocumentDeliveryTypeEnum
- AuthorizationCode : Edm.String
- StartDeliveryDate : Edm.DateTimeOffset
- StartDeliveryTime : Edm.TimeOfDay
- EndDeliveryDate : Edm.DateTimeOffset
- EndDeliveryTime : Edm.TimeOfDay
- VehiclePlate : Edm.String
- ATDocumentType : Edm.String
- ElecCommStatus : SAPB1.ElecCommStatusEnum
- ElecCommMessage : Edm.String
- ReuseDocumentNum : SAPB1.BoYesNoEnum
- ReuseNotaFiscalNum : SAPB1.BoYesNoEnum
- PrintSEPADirect : SAPB1.BoYesNoEnum
- FiscalDocNum : Edm.String
- POSDailySummaryNo : Edm.Int32
- POSReceiptNo : Edm.Int32
- PointOfIssueCode : Edm.String
- Letter : SAPB1.FolioLetterEnum
- FolioNumberFrom : Edm.Int32
- FolioNumberTo : Edm.Int32
- InterimType : SAPB1.BoInterimDocTypes
- RelatedType : Edm.Int32
- RelatedEntry : Edm.Int32
- SAPPassport : Edm.String
- DocumentTaxID : Edm.String
- DateOfReportingControlStatementVAT : Edm.DateTimeOffset
- ReportingSectionControlStatementVAT : Edm.String
- ExcludeFromTaxReportControlStatementVAT : SAPB1.BoYesNoEnum
- POS_CashRegister : Edm.Int32
- UpdateTime : Edm.TimeOfDay
- CreateQRCodeFrom : Edm.String
- PriceMode : SAPB1.PriceModeDocumentEnum
- PriceListNum : Edm.Int32
- DownPaymentTrasactionID : Edm.String
- OriginalRefNo : Edm.String
- OriginalRefDate : Edm.DateTimeOffset
- Revision : SAPB1.BoYesNoEnum
- GSTTransactionType : SAPB1.GSTTransactionTypeEnum
- OriginalCreditOrDebitNo : Edm.String
- OriginalCreditOrDebitDate : Edm.DateTimeOffset
- ECommerceOperator : Edm.String
- ECommerceGSTIN : Edm.String
- TaxInvoiceNo : Edm.String
- TaxInvoiceDate : Edm.DateTimeOffset
- ShipFrom : Edm.String
- CommissionTrade : SAPB1.CommissionTradeTypeEnum
- CommissionTradeReturn : SAPB1.BoYesNoEnum
- UseBillToAddrToDetermineTax : SAPB1.BoYesNoEnum
- IssuingReason : Edm.Int32
- Cig : Edm.Int32
- Cup : Edm.Int32
- EDocType : SAPB1.EDocTypeEnum
- FCEAsPaymentMeans : SAPB1.BoYesNoEnum
- PaidToDate : Edm.Double
- PaidToDateFC : Edm.Double
- PaidToDateSys : Edm.Double
- FatherCard : Edm.String
- FatherType : SAPB1.BoFatherCardTypes
- ShipState : Edm.String
- ShipPlace : Edm.String
- CustOffice : Edm.String
- FCI : Edm.String
- AddLegIn : Edm.String
- LegTextF : Edm.Int32
- DANFELgTxt : Edm.String
- DataVersion : Edm.Int32
- LastPageFolioNumber : Edm.Int32
- InventoryStatus : SAPB1.BoStatus
- PlasticPackagingTaxRelevant : SAPB1.BoYesNoEnum
- NotRelevantForMonthlyInvoice : SAPB1.BoYesNoEnum
- EndAt : SAPB1.BoPayTermDueTypes
- ShipToCodeForReturn : Edm.String
- AddressForReturn : Edm.String
- Document_ApprovalRequests : Collection(SAPB1.Document_ApprovalRequest)
- DocumentLines : Collection(SAPB1.DocumentLine)
- EWayBillDetails : SAPB1.EWayBillDetails
- EDeliveryInfo : SAPB1.EDeliveryInfo
- ElectronicProtocols : Collection(SAPB1.ElectronicProtocol)
- DocumentAdditionalExpenses : Collection(SAPB1.DocumentAdditionalExpense)
- DocumentDistributedExpenses : Collection(SAPB1.DocumentDistributedExpense)
- WithholdingTaxDataWTXCollection : Collection(SAPB1.WithholdingTaxDataWTX)
- WithholdingTaxDataCollection : Collection(SAPB1.WithholdingTaxData)
- DocumentPackages : Collection(SAPB1.DocumentPackage)
- DocumentSpecialLines : Collection(SAPB1.DocumentSpecialLine)
- DocumentInstallments : Collection(SAPB1.DocumentInstallment)
- DownPaymentsToDraw : Collection(SAPB1.DownPaymentToDraw)
- TaxExtension : SAPB1.TaxExtension
- AddressExtension : SAPB1.AddressExtension
- DocumentReferences : Collection(SAPB1.DocumentReference)
- DocumentAdditionalIntrastatExpenses : Collection(SAPB1.DocumentAdditionalIntrastatExpense)
- DutyStatus : SAPB1.BoYesNoEnum
- BaseType : Edm.Int32
- BaseEntry : Edm.Int32
- IndFinal : SAPB1.BoYesNoEnum
- AllocationNumberIL : Edm.String
- DigitalPayToAddress : Edm.String
- DigitalPayments : SAPB1.BoYesNoEnum
- SirenNumber : Edm.String
- SiretNumber : Edm.String
- RoutingCode : Edm.String
- Suffix : Edm.String
- SOIWizardId : Edm.Int32

## Navigation properties

- BusinessPartner : SAPB1.BusinessPartner [Partner=InventoryGenExits]
- Currency : SAPB1.Currency [Partner=InventoryGenExits]
- PaymentTermsType : SAPB1.PaymentTermsType [Partner=InventoryGenExits]
- SalesPerson : SAPB1.SalesPerson [Partner=InventoryGenExits]
- ShippingType : SAPB1.ShippingType [Partner=InventoryGenExits]
- LandedCost : SAPB1.LandedCost [Partner=PurchaseDeliveryNotes]
- FactoringIndicator : SAPB1.FactoringIndicator [Partner=InventoryGenExits]
- User : SAPB1.User [Partner=InventoryGenExits]
- JournalEntry : SAPB1.JournalEntry [Partner=InventoryGenExits]
- Forms1099 : SAPB1.Forms1099 [Partner=InventoryGenExits]
- WizardPaymentMethod : SAPB1.WizardPaymentMethod [Partner=InventoryGenExits]
- PaymentBlock2 : SAPB1.PaymentBlock [Partner=InventoryGenExits]
- CentralBankIndicator2 : SAPB1.CentralBankIndicator [Partner=InventoryGenExits]
- Project2 : SAPB1.Project [Partner=InventoryGenExits]
- EmployeeInfo : SAPB1.EmployeeInfo [Partner=InventoryGenExits]
- Country : SAPB1.Country [Partner=InventoryGenExits]
- BusinessPlace : SAPB1.BusinessPlace [Partner=InventoryGenExits]
- UserLanguage : SAPB1.UserLanguage [Partner=InventoryGenExits]
- NFModel : SAPB1.NFModel [Partner=InventoryGenExits]
- ChartOfAccount : SAPB1.ChartOfAccount [Partner=InventoryGenExits]
- TaxWebSite : SAPB1.TaxWebSite [Partner=InventoryGenExits]
- Branch : SAPB1.Branch [Partner=InventoryGenExits]
- Department : SAPB1.Department [Partner=InventoryGenExits]
- POSDailySummary : SAPB1.POSDailySummary [Partner=InventoryGenExits]
- PriceList : SAPB1.PriceList [Partner=InventoryGenExits]
- CIGCode : SAPB1.CIGCode [Partner=InventoryGenExits]
- CUPCode : SAPB1.CUPCode [Partner=InventoryGenExits]

# SAPB1.Document_ApprovalRequest (ComplexType)

## Properties

- ApprovalTemplatesID : Edm.Int32
- Remarks : Edm.String
- ApprovalTemplatesName : Edm.String
- ActiveForUpdate : SAPB1.BoYesNoEnum

# SAPB1.DocumentAdditionalExpense (ComplexType)

OpenType: true

## Properties

- ExpenseCode : Edm.Int32
- LineTotal : Edm.Double
- LineTotalFC : Edm.Double
- LineTotalSys : Edm.Double
- PaidToDate : Edm.Double
- PaidToDateFC : Edm.Double
- PaidToDateSys : Edm.Double
- Remarks : Edm.String
- DistributionMethod : SAPB1.BoAdEpnsDistribMethods
- TaxLiable : SAPB1.BoYesNoEnum
- VatGroup : Edm.String
- TaxPercent : Edm.Double
- TaxSum : Edm.Double
- TaxSumFC : Edm.Double
- TaxSumSys : Edm.Double
- DeductibleTaxSum : Edm.Double
- DeductibleTaxSumFC : Edm.Double
- DeductibleTaxSumSys : Edm.Double
- AquisitionTax : SAPB1.BoYesNoEnum
- TaxCode : Edm.String
- TaxType : SAPB1.BoAdEpnsTaxTypes
- TaxPaid : Edm.Double
- TaxPaidFC : Edm.Double
- TaxPaidSys : Edm.Double
- EqualizationTaxPercent : Edm.Double
- EqualizationTaxSum : Edm.Double
- EqualizationTaxFC : Edm.Double
- EqualizationTaxSys : Edm.Double
- TaxTotalSum : Edm.Double
- TaxTotalSumFC : Edm.Double
- TaxTotalSumSys : Edm.Double
- BaseDocEntry : Edm.Int32
- BaseDocLine : Edm.Int32
- BaseDocType : Edm.Int32
- BaseDocumentReference : Edm.Int32
- LineNum : Edm.Int32
- LastPurchasePrice : SAPB1.BoYesNoEnum
- Status : SAPB1.BoStatus
- Stock : SAPB1.BoYesNoEnum
- TargetAbsEntry : Edm.Int32
- TargetType : Edm.Int32
- WTLiable : SAPB1.BoYesNoEnum
- DistributionRule : Edm.String
- Project : Edm.String
- DistributionRule2 : Edm.String
- DistributionRule3 : Edm.String
- DistributionRule4 : Edm.String
- DistributionRule5 : Edm.String
- LineGross : Edm.Double
- LineGrossSys : Edm.Double
- LineGrossFC : Edm.Double
- ExternalCalcTaxRate : Edm.Double
- ExternalCalcTaxAmount : Edm.Double
- ExternalCalcTaxAmountFC : Edm.Double
- ExternalCalcTaxAmountSC : Edm.Double
- CUSplit : SAPB1.BoYesNoEnum
- DocFreight : SAPB1.BoYesNoEnum
- DocExpenseTaxJurisdictions : Collection(SAPB1.DocExpenseTaxJurisdiction)
- DocFreightEBooksDetails : Collection(SAPB1.DocFreightEBooksDetail)

# SAPB1.DocumentAdditionalIntrastatExpense (ComplexType)

OpenType: true

## Properties

- ExpenseCode : Edm.Int32
- LineTotal : Edm.Double
- LineTotalFC : Edm.Double
- LineTotalSys : Edm.Double
- PaidToDate : Edm.Double
- PaidToDateFC : Edm.Double
- PaidToDateSys : Edm.Double
- DistributionMethod : SAPB1.BoAdEpnsDistribMethods
- BaseDocEntry : Edm.Int32
- BaseDocLine : Edm.Int32
- BaseDocType : Edm.Int32
- BaseDocumentReference : Edm.Int32
- LineNum : Edm.Int32

# SAPB1.DocumentChangeMenuName (ComplexType)

## Properties

- Document : Edm.String
- DocumentSubType : Edm.String
- ChangedMenuName : Edm.String

# SAPB1.DocumentCloseParams (ComplexType)

## Properties

- DocEntry : Edm.Int32
- ClosingOption : SAPB1.ClosingOptionEnum
- SpecifiedClosingDate : Edm.DateTimeOffset

# SAPB1.DocumentDistributedExpense (ComplexType)

# SAPB1.DocumentInstallment (ComplexType)

OpenType: true

## Properties

- DueDate : Edm.DateTimeOffset
- Percentage : Edm.Double
- Total : Edm.Double
- LastDunningDate : Edm.DateTimeOffset
- DunningLevel : Edm.Int32
- TotalFC : Edm.Double
- InstallmentId : Edm.Int32
- PaymentOrdered : SAPB1.BoYesNoEnum
- PaidToDate : Edm.Double
- PaidToDateFC : Edm.Double

# SAPB1.DocumentLine (ComplexType)

OpenType: true
Filtered properties: 58

## Properties

- LineNum : Edm.Int32
- ItemCode : Edm.String
- ItemDescription : Edm.String
- Quantity : Edm.Double
- ShipDate : Edm.DateTimeOffset
- Price : Edm.Double
- PriceAfterVAT : Edm.Double
- Currency : Edm.String
- Rate : Edm.Double
- DiscountPercent : Edm.Double
- VendorNum : Edm.String
- SerialNum : Edm.String
- WarehouseCode : Edm.String
- SalesPersonCode : Edm.Int32
- CommisionPercent : Edm.Double
- TreeType : SAPB1.BoItemTreeTypes
- AccountCode : Edm.String
- UseBaseUnits : SAPB1.BoYesNoEnum
- SupplierCatNum : Edm.String
- CostingCode : Edm.String
- ProjectCode : Edm.String
- BarCode : Edm.String
- VatGroup : Edm.String
- Height1 : Edm.Double
- Hight1Unit : Edm.Int32
- Height2 : Edm.Double
- Height2Unit : Edm.Int32
- Lengh1 : Edm.Double
- Lengh1Unit : Edm.Int32
- Lengh2 : Edm.Double
- Lengh2Unit : Edm.Int32
- Weight1 : Edm.Double
- Weight1Unit : Edm.Int32
- Weight2 : Edm.Double
- Weight2Unit : Edm.Int32
- Factor1 : Edm.Double
- Factor2 : Edm.Double
- Factor3 : Edm.Double
- Factor4 : Edm.Double
- BaseType : Edm.Int32
- BaseEntry : Edm.Int32
- BaseLine : Edm.Int32
- Volume : Edm.Double
- VolumeUnit : Edm.Int32
- Width1 : Edm.Double
- Width1Unit : Edm.Int32
- Width2 : Edm.Double
- Width2Unit : Edm.Int32
- Address : Edm.String
- TaxCode : Edm.String
- TaxType : SAPB1.BoTaxTypes
- TaxLiable : SAPB1.BoYesNoEnum
- PickStatus : SAPB1.BoYesNoEnum
- PickQuantity : Edm.Double
- PickListIdNumber : Edm.Int32
- OriginalItem : Edm.String
- BackOrder : SAPB1.BoYesNoEnum
- FreeText : Edm.String
- ShippingMethod : Edm.Int32
- POTargetNum : Edm.Int32
- POTargetEntry : Edm.String
- POTargetRowNum : Edm.Int32
- CorrectionInvoiceItem : SAPB1.BoCorInvItemStatus
- CorrInvAmountToStock : Edm.Double
- CorrInvAmountToDiffAcct : Edm.Double
- AppliedTax : Edm.Double
- AppliedTaxFC : Edm.Double
- AppliedTaxSC : Edm.Double
- WTLiable : SAPB1.BoYesNoEnum
- DeferredTax : SAPB1.BoYesNoEnum
- EqualizationTaxPercent : Edm.Double
- TotalEqualizationTax : Edm.Double
- TotalEqualizationTaxFC : Edm.Double
- TotalEqualizationTaxSC : Edm.Double
- NetTaxAmount : Edm.Double
- NetTaxAmountFC : Edm.Double
- NetTaxAmountSC : Edm.Double
- MeasureUnit : Edm.String
- UnitsOfMeasurment : Edm.Double
- LineTotal : Edm.Double
- TaxPercentagePerRow : Edm.Double
- TaxTotal : Edm.Double
- ConsumerSalesForecast : SAPB1.BoYesNoEnum
- ExciseAmount : Edm.Double
- TaxPerUnit : Edm.Double
- TotalInclTax : Edm.Double
- CountryOrg : Edm.String
- SWW : Edm.String
- TransactionType : SAPB1.BoTransactionTypeEnum
- DistributeExpense : SAPB1.BoYesNoEnum
- RowTotalFC : Edm.Double
- RowTotalSC : Edm.Double
- LastBuyInmPrice : Edm.Double
- LastBuyDistributeSumFc : Edm.Double
- LastBuyDistributeSumSc : Edm.Double
- LastBuyDistributeSum : Edm.Double
- StockDistributesumForeign : Edm.Double
- StockDistributesumSystem : Edm.Double
- StockDistributesum : Edm.Double
- StockInmPrice : Edm.Double
- PickStatusEx : SAPB1.BoDocumentLinePickStatus
- TaxBeforeDPM : Edm.Double
- TaxBeforeDPMFC : Edm.Double
- TaxBeforeDPMSC : Edm.Double
- CFOPCode : Edm.String
- CSTCode : Edm.String
- Usage : Edm.Int32
- TaxOnly : SAPB1.BoYesNoEnum
- VisualOrder : Edm.Int32
- BaseOpenQuantity : Edm.Double
- UnitPrice : Edm.Double
- LineStatus : SAPB1.BoStatus
- PackageQuantity : Edm.Double
- Text : Edm.String
- LineType : SAPB1.BoDocLineType
- COGSCostingCode : Edm.String
- COGSAccountCode : Edm.String
- ChangeAssemlyBoMWarehouse : Edm.String
- GrossBuyPrice : Edm.Double
- GrossBase : Edm.Int32
- GrossProfitTotalBasePrice : Edm.Double
- CostingCode2 : Edm.String
- CostingCode3 : Edm.String
- CostingCode4 : Edm.String
- CostingCode5 : Edm.String
- ItemDetails : Edm.String
- LocationCode : Edm.Int32
- ActualDeliveryDate : Edm.DateTimeOffset
- RemainingOpenQuantity : Edm.Double
- OpenAmount : Edm.Double
- OpenAmountFC : Edm.Double
- OpenAmountSC : Edm.Double
- ExLineNo : Edm.String
- RequiredDate : Edm.DateTimeOffset
- RequiredQuantity : Edm.Double
- COGSCostingCode2 : Edm.String
- COGSCostingCode3 : Edm.String
- COGSCostingCode4 : Edm.String
- COGSCostingCode5 : Edm.String
- CSTforIPI : Edm.String
- CSTforPIS : Edm.String
- CSTforCOFINS : Edm.String
- CreditOriginCode : Edm.String
- WithoutInventoryMovement : SAPB1.BoYesNoEnum
- AgreementNo : Edm.Int32
- AgreementRowNumber : Edm.Int32
- ActualBaseEntry : Edm.Int32
- ActualBaseLine : Edm.Int32
- DocEntry : Edm.Int32
- Surpluses : Edm.Double
- DefectAndBreakup : Edm.Double
- Shortages : Edm.Double
- ConsiderQuantity : SAPB1.BoYesNoEnum
- PartialRetirement : SAPB1.BoYesNoEnum
- RetirementQuantity : Edm.Double
- RetirementAPC : Edm.Double
- ThirdParty : SAPB1.BoYesNoEnum
- PoNum : Edm.String
- PoItmNum : Edm.Int32
- ExpenseType : Edm.String
- ReceiptNumber : Edm.String
- ExpenseOperationType : SAPB1.BoExpenseOperationTypeEnum
- FederalTaxID : Edm.String
- GrossProfit : Edm.Double
- GrossProfitFC : Edm.Double
- GrossProfitSC : Edm.Double
- PriceSource : SAPB1.DocumentPriceSourceEnum
- EnableReturnCost : SAPB1.BoYesNoEnum
- ReturnCost : Edm.Double
- LineVendor : Edm.String
- ReturnAction : Edm.Int32
- ReturnReason : Edm.Int32
- StgSeqNum : Edm.Int32
- StgEntry : Edm.Int32
- StgDesc : Edm.String
- UoMEntry : Edm.Int32
- UoMCode : Edm.String
- InventoryQuantity : Edm.Double
- RemainingOpenInventoryQuantity : Edm.Double
- ParentLineNum : Edm.Int32
- Incoterms : Edm.Int32
- TransportMode : Edm.Int32
- NatureOfTransaction : Edm.Int32
- DestinationCountryForImport : Edm.String
- DestinationRegionForImport : Edm.Int32
- OriginCountryForExport : Edm.String
- OriginRegionForExport : Edm.Int32
- ItemType : SAPB1.BoDocItemType
- ChangeInventoryQuantityIndependently : SAPB1.BoYesNoEnum
- FreeOfChargeBP : SAPB1.BoYesNoEnum
- SACEntry : Edm.Int32
- HSNEntry : Edm.Int32
- GrossPrice : Edm.Double
- GrossTotal : Edm.Double
- GrossTotalFC : Edm.Double
- GrossTotalSC : Edm.Double
- NCMCode : Edm.Int32
- NVECode : Edm.String
- IndEscala : SAPB1.BoYesNoEnum
- CtrSealQty : Edm.Double
- CNJPMan : Edm.String
- CESTCode : Edm.Int32
- UFFiscalBenefitCode : Edm.String
- ReverseCharge : SAPB1.BoYesNoEnum
- ShipToCode : Edm.String
- ShipToDescription : Edm.String
- ShipFromCode : Edm.String
- ShipFromDescription : Edm.String
- OwnerCode : Edm.Int32
- ExternalCalcTaxRate : Edm.Double
- ExternalCalcTaxAmount : Edm.Double
- ExternalCalcTaxAmountFC : Edm.Double
- ExternalCalcTaxAmountSC : Edm.Double
- StandardItemIdentification : Edm.Int32
- CommodityClassification : Edm.Int32
- WeightOfRecycledPlastic : Edm.Double
- PlasticPackageExemptionReason : Edm.String
- LegalText : Edm.String
- Cig : Edm.Int32
- Cup : Edm.Int32
- OperatingProfit : Edm.Double
- OperatingProfitFC : Edm.Double
- OperatingProfitSC : Edm.Double
- NetIncome : Edm.Double
- NetIncomeFC : Edm.Double
- NetIncomeSC : Edm.Double
- CSTforIBS : Edm.String
- CSTforCBS : Edm.String
- CSTforIS : Edm.String
- UnencumberedReason : Edm.Int32
- CUSplit : SAPB1.BoYesNoEnum
- ListNum : Edm.Int32
- RecognizedTaxCode : Edm.String
- LineTaxJurisdictions : Collection(SAPB1.LineTaxJurisdiction)
- GeneratedAssets : Collection(SAPB1.GeneratedAsset)
- EBooksDetails : Collection(SAPB1.EBooksDetail)
- DocLinePickLists : Collection(SAPB1.DocLinePickList)
- DocumentLineAdditionalExpenses : Collection(SAPB1.DocumentLineAdditionalExpense)
- WithholdingTaxLines : Collection(SAPB1.WithholdingTaxLine)
- SerialNumbers : Collection(SAPB1.SerialNumber)
- BatchNumbers : Collection(SAPB1.BatchNumber)
- DocumentLinesBinAllocations : Collection(SAPB1.DocumentLinesBinAllocation)
- ExportProcesses : Collection(SAPB1.ExportProcess)
- CCDNumbers : Collection(SAPB1.CCDNumber)
- ImportProcesses : Collection(SAPB1.ImportProcess)

# SAPB1.DocumentLineAdditionalExpense (ComplexType)

OpenType: true

## Properties

- LineNumber : Edm.Int32
- GroupCode : Edm.Int32
- ExpenseCode : Edm.Int32
- LineTotal : Edm.Double
- LineTotalFC : Edm.Double
- LineTotalSys : Edm.Double
- PaidToDate : Edm.Double
- PaidToDateFC : Edm.Double
- PaidToDateSys : Edm.Double
- TaxLiable : SAPB1.BoYesNoEnum
- VatGroup : Edm.String
- TaxPercent : Edm.Double
- TaxSum : Edm.Double
- TaxSumFC : Edm.Double
- TaxSumSys : Edm.Double
- DeductibleTaxSum : Edm.Double
- DeductibleTaxSumFC : Edm.Double
- DeductibleTaxSumSys : Edm.Double
- AquisitionTax : SAPB1.BoYesNoEnum
- TaxCode : Edm.String
- TaxType : SAPB1.BoAdEpnsTaxTypes
- TaxPaid : Edm.Double
- TaxPaidFC : Edm.Double
- TaxPaidSys : Edm.Double
- EqualizationTaxPercent : Edm.Double
- EqualizationTaxSum : Edm.Double
- EqualizationTaxFC : Edm.Double
- EqualizationTaxSys : Edm.Double
- TaxTotalSum : Edm.Double
- TaxTotalSumFC : Edm.Double
- TaxTotalSumSys : Edm.Double
- WTLiable : SAPB1.BoYesNoEnum
- BaseGroup : Edm.Int32
- DistributionRule : Edm.String
- Project : Edm.String
- DistributionRule2 : Edm.String
- DistributionRule3 : Edm.String
- DistributionRule4 : Edm.String
- DistributionRule5 : Edm.String
- ExternalCalcTaxRate : Edm.Double
- ExternalCalcTaxAmount : Edm.Double
- ExternalCalcTaxAmountFC : Edm.Double
- ExternalCalcTaxAmountSC : Edm.Double
- CUSplit : SAPB1.BoYesNoEnum
- DocFreight : SAPB1.BoYesNoEnum
- LineExpenseTaxJurisdictions : Collection(SAPB1.LineExpenseTaxJurisdiction)
- LineFreightEBooksDetails : Collection(SAPB1.LineFreightEBooksDetail)

# SAPB1.DocumentLinesBinAllocation (ComplexType)

OpenType: true

## Properties

- BinAbsEntry : Edm.Int32
- Quantity : Edm.Double
- AllowNegativeQuantity : SAPB1.BoYesNoEnum
- SerialAndBatchNumbersBaseLine : Edm.Int32
- BaseLineNumber : Edm.Int32

# SAPB1.DocumentPackage (ComplexType)

OpenType: true

## Properties

- Number : Edm.Int32
- Type : Edm.String
- TotalWeight : Edm.Double
- Units : Edm.Int32
- DocumentPackageItems : Collection(SAPB1.DocumentPackageItem)

# SAPB1.DocumentPackageItem (ComplexType)

OpenType: true

## Properties

- PackageNumber : Edm.Int32
- ItemCode : Edm.String
- Quantity : Edm.Double
- UoMEntry : Edm.Int32
- MeasureUnit : Edm.String
- UnitsOfMeasurement : Edm.Double

# SAPB1.DocumentParams (ComplexType)

## Properties

- DocEntry : Edm.Int32

# SAPB1.DocumentReference (ComplexType)

## Properties

- DocEntry : Edm.Int32
- LineNumber : Edm.Int32
- RefDocEntr : Edm.Int32
- RefDocNum : Edm.Int32
- ExtDocNum : Edm.String
- RefObjType : SAPB1.ReferencedObjectTypeEnum
- AccessKey : Edm.String
- IssueDate : Edm.DateTimeOffset
- IssuerCNPJ : Edm.String
- IssuerCode : Edm.String
- Model : Edm.String
- Series : Edm.String
- Number : Edm.Int32
- RefAccKey : Edm.String
- RefAmount : Edm.Double
- SubSeries : Edm.String
- Remark : Edm.String
- LinkRefTyp : SAPB1.LinkReferenceTypeEnum

# SAPB1.DocumentSeriesParams (ComplexType)

## Properties

- Document : Edm.String
- DocumentSubType : Edm.String
- Series : Edm.Int32

# SAPB1.DocumentSeriesUserParams (ComplexType)

## Properties

- Document : Edm.String
- DocumentSubType : Edm.String
- Series : Edm.Int32
- User : Edm.Int32

# SAPB1.DocumentSpecialLine (ComplexType)

## Properties

- LineNum : Edm.Int32
- AfterLineNumber : Edm.Int32
- OrderNumber : Edm.Int32
- LineType : SAPB1.BoDocSpecialLineType
- Subtotal : Edm.Double
- LineText : Edm.String
- SubtotalFC : Edm.Double
- SubtotalSC : Edm.Double
- TaxAmount : Edm.Double
- TaxAmountFC : Edm.Double
- TaxAmountSC : Edm.Double
- Freight1 : Edm.Double
- Freight1FC : Edm.Double
- Freight1SC : Edm.Double
- Freight2 : Edm.Double
- Freight2FC : Edm.Double
- Freight2SC : Edm.Double
- Freight3 : Edm.Double
- Freight3FC : Edm.Double
- Freight3SC : Edm.Double
- GrossTotal : Edm.Double
- GrossTotalFC : Edm.Double
- GrossTotalSC : Edm.Double

# SAPB1.DocumentTypeParams (ComplexType)

## Properties

- Document : Edm.String
- DocumentSubType : Edm.String

# SAPB1.DownPaymentToDraw (ComplexType)

## Properties

- DocEntry : Edm.Int32
- PostingDate : Edm.DateTimeOffset
- DueDate : Edm.DateTimeOffset
- Name : Edm.String
- Details : Edm.String
- AmountToDraw : Edm.Double
- DownPaymentType : SAPB1.DownPaymentTypeEnum
- AmountToDrawFC : Edm.Double
- AmountToDrawSC : Edm.Double
- DocInternalID : Edm.Int32
- RowNum : Edm.Int32
- DocNumber : Edm.Int32
- Tax : Edm.Double
- TaxFC : Edm.Double
- TaxSC : Edm.Double
- GrossAmountToDraw : Edm.Double
- GrossAmountToDrawFC : Edm.Double
- GrossAmountToDrawSC : Edm.Double
- IsGrossLine : SAPB1.BoYesNoEnum
- DownPaymentsToDrawDetails : Collection(SAPB1.DownPaymentToDrawDetails)

# SAPB1.DownPaymentToDrawDetails (ComplexType)

## Properties

- DocInternalID : Edm.Int32
- RowNum : Edm.Int32
- SeqNum : Edm.Int32
- DocEntry : Edm.Int32
- VatGroupCode : Edm.String
- VatPercent : Edm.Double
- AmountToDraw : Edm.Double
- AmountToDrawFC : Edm.Double
- AmountToDrawSC : Edm.Double
- Tax : Edm.Double
- TaxFC : Edm.Double
- TaxSC : Edm.Double
- IsGrossLine : SAPB1.BoYesNoEnum
- GrossAmountToDraw : Edm.Double
- GrossAmountToDrawFC : Edm.Double
- GrossAmountToDrawSC : Edm.Double
- LineType : SAPB1.LineTypeEnum
- TaxAdjust : SAPB1.BoYesNoEnum

# SAPB1.DppChangeParams (ComplexType)

## Properties

- FromDate : Edm.DateTimeOffset
- FromTime : Edm.TimeOfDay
- HasChanged : SAPB1.BoYesNoEnum

# SAPB1.DunningLetter (EntityType)

OpenType: true
Key: RowNumber

## Properties

- FeeCurrency : Edm.String
- RowNumber : Edm.Int32 [required]
- LetterFormat : Edm.String
- Effectiveafter : Edm.String
- MinimumBalanceCurrency : Edm.String
- Feeperletter : Edm.Double
- CalcInterest : SAPB1.BoYesNoEnum
- MinimumBalance : Edm.Double

## Navigation properties

- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=DunningLetter]

# SAPB1.DunningLetterParams (ComplexType)

## Properties

- RowNumber : Edm.Int32

# SAPB1.DunningTerm (EntityType)

Key: Code

## Properties

- Code : Edm.String [required]
- Name : Edm.String
- GroupingMethod : SAPB1.GroupingMethodEnum
- DaysInYear : Edm.Int32
- DaysInMonth : Edm.Int32
- CalculateInterestMethod : SAPB1.CalculateInterestMethodEnum
- ExchangeRateSelect : SAPB1.ExchangeRateSelectEnum
- YearlyInterestRate : Edm.Double
- LetterFee : Edm.Double
- LetterFeeCurrency : Edm.String
- MinimumBalance : Edm.Double
- MinimumBalanceCurrency : Edm.String
- IncludeInterest : SAPB1.BoYesNoEnum
- ApplyHighestLetterTemplate : SAPB1.BoYesNoEnum
- AutomaticPosting : SAPB1.AutomaticPostingEnum
- InterestAccount : Edm.String
- FeeAccount : Edm.String
- BaseDateSelect : SAPB1.BaseDateSelectEnum
- DunningTermLines : Collection(SAPB1.DunningTermLine)

## Navigation properties

- ChartOfAccount : SAPB1.ChartOfAccount [Partner=DunningTerms]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=DunningTerm2]

# SAPB1.DunningTermLine (ComplexType)

## Properties

- LevelNum : Edm.Int32
- LetterFormat : SAPB1.DunningLetterTypeEnum
- Effectiveafter : Edm.String
- LetterFee : Edm.Double
- LetterFeeCurrency : Edm.String
- MininumBalance : Edm.Double
- MininumBalanceCurrency : Edm.String
- CalculateInterest : SAPB1.BoYesNoEnum

# SAPB1.DunningTermParams (ComplexType)

## Properties

- Code : Edm.String
- Name : Edm.String

# SAPB1.DynamicSystemString (EntityType)

OpenType: true
Key: FormID, ItemID, ColumnID

## Properties

- FormID : Edm.String [required]
- ItemID : Edm.String [required]
- ColumnID : Edm.String [required]
- ItemString : Edm.String
- IsBold : SAPB1.BoYesNoEnum
- IsItalics : SAPB1.BoYesNoEnum

# SAPB1.DynamicSystemStringParams (ComplexType)

## Properties

- FormID : Edm.String
- ItemID : Edm.String
- ColumnID : Edm.String

# SAPB1.EBooks (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- MARK : Edm.String
- CancelMARK : Edm.String
- UID : Edm.String
- IssuerVATID : Edm.String
- CPVATID : Edm.String
- Series : Edm.String
- AA : Edm.String
- IssueDate : Edm.DateTimeOffset
- InvoiceType : Edm.String
- Currency : Edm.String
- TotalNetValue : Edm.Double
- TotalVatAmount : Edm.Double
- TotalWithheldAmount : Edm.Double
- TotalGrossValue : Edm.Double
- LinkedDocType : Edm.Int32
- LinkedDocEntry : Edm.Int32
- IsNegativeMark : SAPB1.BoYesNoEnum
- EBooksLines : Collection(SAPB1.EBooksLine)

# SAPB1.EBooksDetail (ComplexType)

OpenType: true

## Properties

- IncomeClassificationType : Edm.Int32
- IncomeClassificationCategory : Edm.Int32
- ExpensesClassificationType : Edm.Int32
- ExpensesClassificationCategory : Edm.Int32
- NetValueLC : Edm.Double
- NetValueFC : Edm.Double
- NetValueSC : Edm.Double
- VatCategory : Edm.Int32
- WithheldPercentCategory : Edm.Int32
- WithheldAmountLC : Edm.Double
- WithheldAmountFC : Edm.Double
- WithheldAmountSC : Edm.Double
- VatClassificationType : Edm.Int32
- VatClassificationCategory : Edm.Int32
- VATExemptionCause : Edm.Int32
- RecType : Edm.Int32
- StampDutyCategory : Edm.Int32
- OtherTaxesCategory : Edm.Int32
- FeesCategory : Edm.Int32

# SAPB1.EBooksLine (ComplexType)

## Properties

- LineNumber : Edm.Int32
- NetValue : Edm.Double
- VatCategory : Edm.Int32
- VatAmount : Edm.Double
- WithheldAmount : Edm.Double
- WithheldPercentCategory : Edm.Int32
- ExpenseClassificationType : Edm.Int32
- ExpenseClassificationCategory : Edm.Int32
- VATClassificationType : Edm.Int32
- VATClassificationCategory : Edm.Int32
- VATExemptionCause : Edm.Int32
- RecordType : Edm.Int32
- StampDutyCategory : Edm.Int32
- OtherTaxesCategory : Edm.Int32
- FeesCategory : Edm.Int32

# SAPB1.EBooksParams (ComplexType)

## Properties

- MARK : Edm.String
- LinkedDocType : Edm.Int32
- LinkedDocEntry : Edm.Int32

# SAPB1.EcmAction (ComplexType)

OpenType: true
Filtered properties: 2

## Properties

- ActionID : Edm.Int32
- Protocol : Edm.String
- Type : SAPB1.EcmActionTypeEnum
- Description : Edm.String
- Status : SAPB1.EcmActionStatusEnum
- Message : Edm.String
- Environment : Edm.Int32
- BusinessPlace : Edm.Int32
- Submits : Edm.Int32
- ObjectID : Edm.String
- ReportID : Edm.String
- SourceType : Edm.String
- SourceObject : Edm.Int32
- AssignedID : Edm.String
- DocumentBatch : Edm.String
- DocumentBatchLine : Edm.Int32
- PeriodType : SAPB1.EcmActionPeriodTypeEnum
- PeriodNumber : Edm.Int32
- PeriodYear : Edm.Int32
- PeriodDateFrom : Edm.DateTimeOffset
- PeriodDateTo : Edm.DateTimeOffset
- IsRemoved : SAPB1.BoYesNoEnum
- IsCanceled : SAPB1.BoYesNoEnum
- GenerationType : SAPB1.EcmActionGenerationTypeEnum
- GUID : Edm.String

# SAPB1.EcmActionDocParams (ComplexType)

## Properties

- Protocol : Edm.String
- SourceType : Edm.String
- SourceObject : Edm.Int32

# SAPB1.EcmActionLog (ComplexType)

## Properties

- ActionID : Edm.Int32
- LogID : Edm.Int32
- Type : SAPB1.EcmActionLogTypeEnum
- Message : Edm.String
- Data : Edm.String
- LogDate : Edm.DateTimeOffset
- LogTime : Edm.Int32
- ExportFormat : Edm.Int32
- ExportFile : Edm.String
- AuthorityProcess : SAPB1.ElectronicDocumentAuthorityProcessEnum
- IsSensitive : SAPB1.BoYesNoEnum

# SAPB1.EcmActionLogParams (ComplexType)

## Properties

- ActionID : Edm.Int32
- LogID : Edm.Int32

# SAPB1.EcmActionParams (ComplexType)

## Properties

- ActionID : Edm.Int32

# SAPB1.ECMActionStatusData (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- ActStatus : SAPB1.EcmActionStatusEnum
- ReportID : Edm.String
- ReceivDate : Edm.DateTimeOffset
- ActMessage : Edm.String

# SAPB1.ECMCodeParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32

# SAPB1.EDeliveryInfo (ComplexType)

## Properties

- DocEntry : Edm.Int32
- MoveType : Edm.Int32
- VehicleNo : Edm.String

# SAPB1.EDFDocMapping (ComplexType)

## Properties

- ID : Edm.Int32
- Name : Edm.String
- Description : Edm.String

# SAPB1.EDFDocMappingInputParams (ComplexType)

## Properties

- Code : SAPB1.ElectronicDocProtocolCodeStrEnum
- DocType : Edm.String

# SAPB1.EDFEntry (ComplexType)

OpenType: true
Filtered properties: 2

## Properties

- AbsEntry : Edm.Int32
- Code : SAPB1.ElectronicDocProtocolCodeStrEnum
- ParentAbsEntry : Edm.Int32
- Type : SAPB1.ElectronicDocumentEntryTypeEnum
- Status : SAPB1.ElectronicDocumentEntryStatusEnum
- BranchID : Edm.Int32
- Environment : Edm.Int32
- Description : Edm.String
- Message : Edm.String
- Submits : Edm.Int32
- ObjectID : Edm.String
- ReportID : Edm.String
- SrcObjType : Edm.String
- SrcAbsEntry : Edm.Int32
- AssignedID : Edm.String
- DocBatchID : Edm.String
- DocBatchIndex : Edm.Int32
- GenerationType : SAPB1.ElectronicDocGenTypeEnum
- TestMode : SAPB1.BoYesNoEnum
- PeriodType : SAPB1.ElectronicDocumentEntryPeriodTypeEnum
- PeriodNumber : Edm.Int32
- PeriodYear : Edm.Int32
- PeriodDateFrom : Edm.DateTimeOffset
- PeriodDateTo : Edm.DateTimeOffset
- IsRemoved : SAPB1.BoYesNoEnum
- IsCancelation : SAPB1.BoYesNoEnum
- CreateDate : Edm.DateTimeOffset
- CreateTime : Edm.Int32
- UpdateDate : Edm.DateTimeOffset
- UpdateTime : Edm.Int32
- User : Edm.Int32
- User2 : Edm.Int32
- ScheduledJobID : Edm.Int32
- GUID : Edm.String
- Authority : Edm.String
- CancellationStatus : SAPB1.ElectronicDocumentEntryCancellationStatusEnum
- ProcessingTarget : Edm.String
- EDocType : Edm.Int32
- EDocNum : Edm.String
- Emergency : SAPB1.BoYesNoEnum
- StatusReason : Edm.String
- StatusDesc : Edm.String

# SAPB1.EDFEntryAddLogInputParams (ComplexType)

## Properties

- Code : SAPB1.ElectronicDocProtocolCodeStrEnum
- GUID : Edm.String
- LogType : SAPB1.ElectronicDocumentEntryLogTypeEnum
- LogMessage : Edm.String
- LogData : Edm.String
- ExportFormat : Edm.Int32
- LogDataContentType : SAPB1.ElectronicDocumentBlobContentTypeEnum
- ZipLogData : SAPB1.BoYesNoEnum
- ExportFile : Edm.String
- AuthorityProcess : SAPB1.ElectronicDocumentAuthorityProcessEnum
- IsSensitive : SAPB1.BoYesNoNoneEnum

# SAPB1.EDFEntryInputParams (ComplexType)

## Properties

- Code : SAPB1.ElectronicDocProtocolCodeStrEnum
- GUID : Edm.String

# SAPB1.EDFEntryListInputParams (ComplexType)

## Properties

- Code : SAPB1.ElectronicDocProtocolCodeStrEnum
- StoreEntryTypeSet : Edm.String
- StoreEntryStatusSet : Edm.String
- MaxLines : Edm.Int32
- BranchID : Edm.Int32
- FromDate : Edm.DateTimeOffset
- FromTime : Edm.Int32
- ToDate : Edm.DateTimeOffset
- ToTime : Edm.Int32
- FromEntryID : Edm.Int32
- Ascending : SAPB1.BoYesNoEnum
- CancellationStatusSet : Edm.String
- ProcessingTarget : SAPB1.ElectronicDocProcessingTargetEnum
- ProcessingTargetStr : Edm.String

# SAPB1.EDFEntryLog (ComplexType)

OpenType: true

## Properties

- AbsEntry : Edm.Int32
- LogNumber : Edm.Int32
- LogType : SAPB1.ElectronicDocumentEntryLogTypeEnum
- LogMessage : Edm.String
- LogData : Edm.String
- LogOperationDate : Edm.DateTimeOffset
- LogOperationTime : Edm.Int32
- ExportFormat : Edm.Int32
- ExportFile : Edm.String
- AuthorityProcess : SAPB1.ElectronicDocumentAuthorityProcessEnum
- IsSensitive : SAPB1.BoYesNoEnum

# SAPB1.EDFEntryLogInputParams (ComplexType)

## Properties

- Code : SAPB1.ElectronicDocProtocolCodeStrEnum
- GUID : Edm.String
- LogType : SAPB1.ElectronicDocumentEntryLogTypeEnum
- FileName : Edm.String
- LogDataContentType : SAPB1.ElectronicDocumentBlobContentTypeEnum
- UnzipLogData : SAPB1.BoYesNoEnum
- KeepLogDataPrefix : SAPB1.BoYesNoEnum

# SAPB1.EDFImportEntry (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- Code : SAPB1.ElectronicDocProtocolCodeStrEnum
- Status : SAPB1.ElectronicDocumentEntryStatusEnum
- Message : Edm.String
- TestMode : Edm.String
- GUID : Edm.String
- Authority : Edm.String
- ProcessingSource : Edm.String
- MetaData : Edm.String
- CreateDate : Edm.DateTimeOffset
- CreateTime : Edm.Int32
- UpdateDate : Edm.DateTimeOffset
- UpdateTime : Edm.Int32
- User : Edm.Int32
- User2 : Edm.Int32
- MimeType : Edm.String
- FileName : Edm.String
- AssignedID : Edm.String
- CardCode : Edm.String
- DocumentDate : Edm.DateTimeOffset
- ObjectType : Edm.String
- IsBPManual : SAPB1.BoYesNoEnum

# SAPB1.EDFMapping (ComplexType)

## Properties

- FormatID : Edm.Int32
- Hash : Edm.String
- Name : Edm.String
- Mapping : Edm.String

# SAPB1.EDFMappingInputParams (ComplexType)

## Properties

- Hash : Edm.String

# SAPB1.EDFProtocol (EntityType)

Key: Code

## Properties

- Code : SAPB1.ElectronicDocProtocolCodeStrEnum [required]
- Description : Edm.String
- IsActive : SAPB1.BoYesNoEnum

# SAPB1.EDFProtocolInputParams (ComplexType)

## Properties

- Code : SAPB1.ElectronicDocProtocolCodeStrEnum

# SAPB1.EDFProtocolParameter (ComplexType)

## Properties

- Code : SAPB1.ElectronicDocProtocolCodeStrEnum
- ParamName : Edm.String
- ParamValue : Edm.String
- ParameterID : Edm.Int32
- BranchID : Edm.Int32
- ParamParameters : Edm.String
- ParameterType : Edm.String
- Visible : SAPB1.BoYesNoEnum
- UserSignature : Edm.Int32
- CreateDate : Edm.DateTimeOffset
- UpdatingUser : Edm.Int32
- UpdateDate : Edm.DateTimeOffset
- LogInstance : Edm.Int32
- UIOrder : Edm.Int32
- Type : Edm.Int32

# SAPB1.EDFProtocolParameterInputParams (ComplexType)

## Properties

- Code : SAPB1.ElectronicDocProtocolCodeStrEnum
- LineNum : Edm.Int32
- Branch : Edm.Int32

# SAPB1.EDFProtocolWithParameters (ComplexType)

## Properties

- Code : SAPB1.ElectronicDocProtocolCodeStrEnum
- Description : Edm.String
- IsActive : SAPB1.BoYesNoEnum
- EDFProtocolParametersCollection : Collection(SAPB1.EDFProtocolParameter)
- PWPExtendedProperties : SAPB1.PWPExtendedProperties

# SAPB1.ElectronicFileFormat (EntityType)

Key: FormatID

## Properties

- FormatID : Edm.Int32 [required]
- Name : Edm.String
- Description : Edm.String
- Version : Edm.String
- SchemaVersion : Edm.String
- OutputFilePath : Edm.String
- MenuName : Edm.String
- MenuPath : Edm.String

## Navigation properties

- ExportDeterminations : Collection(SAPB1.ExportDetermination) [Partner=ElectronicFileFormat]
- ImportDeterminations : Collection(SAPB1.ImportDetermination) [Partner=ElectronicFileFormat]

# SAPB1.ElectronicFileFormatParams (ComplexType)

## Properties

- FormatID : Edm.Int32
- Name : Edm.String

# SAPB1.ElectronicProtocol (ComplexType)

OpenType: true

## Properties

- ProtocolCode : SAPB1.ElectronicDocProtocolCodeEnum
- GenerationType : SAPB1.ElectronicDocGenTypeEnum
- MappingID : Edm.Int32
- TestingMode : SAPB1.BoYesNoEnum
- Confirmation : Edm.String
- EDocType : Edm.Int32
- CFDiCancellationReason : Edm.String
- CFDiCancellationResponse : Edm.String
- RelatedDocuments : Collection(SAPB1.RelatedDocument)
- EBooksRelevant : SAPB1.BoYesNoEnum
- EBooksMARK : Edm.String
- EBooksMARKofNegative : Edm.String
- EBooksInvoiceType : Edm.String
- EBooksInvoiceTypeofNegative : Edm.String
- EBillingIRN : Edm.String
- EETPKP : Edm.String
- EETBKP : Edm.String
- SignatureInputMessage : Edm.String
- SignatureDigest : Edm.String
- FechaTimbrado : Edm.String
- SelloSAT : Edm.String
- PaymentMethod : Edm.String
- RfcProvCertif : Edm.String
- NoCertificadoSAT : Edm.String
- FPASequenceNumber : Edm.Int32
- FPASendDateSDI : Edm.DateTimeOffset
- FPAProgressivo : Edm.String
- ProtocolDescription : Edm.String
- CFDiExport : Edm.String
- EBillingAckNo : Edm.String
- EBillingAckDt : Edm.String
- EBillingSignedInvoice : Edm.String
- EBillingSignedQRCode : Edm.String
- EBillingResponseStatus : Edm.String
- CFDiCancellationReference : Edm.String
- EBooksQRCodePath : Edm.String
- EBooksQRCodePathofNegative : Edm.String
- CartaPorteID : Edm.String
- EBooksDispatchDate : Edm.DateTimeOffset
- EBooksDispatchTime : Edm.TimeOfDay

# SAPB1.ElectronicReportInfo (ComplexType)

## Properties

- ShareCapitalAmount : Edm.Double
- CompanyType : Edm.String

# SAPB1.ElectronicSeries (ComplexType)

## Properties

- ElectronicSeriesProperty : Edm.Int32
- Series : Edm.Int32
- Name : Edm.String
- InitialNumber : Edm.String
- NextNumber : Edm.String
- LastNumber : Edm.String
- Prefix : Edm.String
- ApprovalYear : Edm.Int32
- ApprovalNumber : Edm.Int32
- Remarks : Edm.String

# SAPB1.ElectronicSeriesParams (ComplexType)

## Properties

- ElectronicSeries : Edm.Int32

# SAPB1.EmailGroup (EntityType)

Key: EmailGroupCode

## Properties

- EmailGroupCode : Edm.String [required]
- EmailGroupName : Edm.String

# SAPB1.EmailGroupParams (ComplexType)

## Properties

- EmailGroupCode : Edm.String
- EmailGroupName : Edm.String

# SAPB1.EmailRecipient (ComplexType)

## Properties

- EmailAddress : Edm.String
- Name : Edm.String

# SAPB1.EmergencyNumber (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- Number : Edm.String
- Code : Edm.String
- Status : Edm.String

# SAPB1.EmployeeAbsenceInfo (ComplexType)

OpenType: true

## Properties

- EmployeeID : Edm.Int32
- LineNum : Edm.Int32
- FromDate : Edm.DateTimeOffset
- ToDate : Edm.DateTimeOffset
- Reason : Edm.String
- ApprovedBy : Edm.String
- ConfirmerNumber : Edm.Int32

# SAPB1.EmployeeBranchAssignmentItem (ComplexType)

OpenType: true

## Properties

- EmployeeID : Edm.Int32
- BPLID : Edm.Int32

# SAPB1.EmployeeEducationInfo (ComplexType)

OpenType: true

## Properties

- EmployeeNo : Edm.Int32
- LineNum : Edm.Int32
- FromDate : Edm.DateTimeOffset
- ToDate : Edm.DateTimeOffset
- EducationType : Edm.Int32
- Institute : Edm.String
- Major : Edm.String
- Diploma : Edm.String

# SAPB1.EmployeeFullNamesParams (ComplexType)

## Properties

- EmployeeID : Edm.Int32
- EmployeeFullName : Edm.String

# SAPB1.EmployeeIDType (EntityType)

Key: IDType

## Properties

- IDType : Edm.String [required]

## Navigation properties

- EmployeesInfo : Collection(SAPB1.EmployeeInfo) [Partner=EmployeeIDType]

# SAPB1.EmployeeIDTypeParams (ComplexType)

## Properties

- IDType : Edm.String

# SAPB1.EmployeeImage (EntityType)

HasStream: true
Key: EmployeeNo

## Properties

- EmployeeNo : Edm.Int32 [required]
- Picture : Edm.Int32 [required]

# SAPB1.EmployeeInfo (EntityType)

OpenType: true
Key: EmployeeID

## Properties

- EmployeeID : Edm.Int32 [required]
- LastName : Edm.String
- FirstName : Edm.String
- MiddleName : Edm.String
- Gender : SAPB1.BoGenderTypes
- JobTitle : Edm.String
- EmployeeType : Edm.Int32
- Department : Edm.Int32
- Branch : Edm.Int32
- WorkStreet : Edm.String
- WorkBlock : Edm.String
- WorkZipCode : Edm.String
- WorkCity : Edm.String
- WorkCounty : Edm.String
- WorkCountryCode : Edm.String
- WorkStateCode : Edm.String
- Manager : Edm.Int32
- ApplicationUserID : Edm.Int32
- SalesPersonCode : Edm.Int32
- OfficePhone : Edm.String
- OfficeExtension : Edm.String
- MobilePhone : Edm.String
- Pager : Edm.String
- HomePhone : Edm.String
- Fax : Edm.String
- eMail : Edm.String
- StartDate : Edm.DateTimeOffset
- StatusCode : Edm.Int32
- Salary : Edm.Double
- SalaryUnit : SAPB1.BoSalaryCostUnits
- EmployeeCosts : Edm.Double
- EmployeeCostUnit : SAPB1.BoSalaryCostUnits
- TerminationDate : Edm.DateTimeOffset
- TreminationReason : Edm.Int32
- BankCode : Edm.String
- BankBranch : Edm.String
- BankBranchNum : Edm.String
- BankAccount : Edm.String
- HomeStreet : Edm.String
- HomeBlock : Edm.String
- HomeZipCode : Edm.String
- HomeCity : Edm.String
- HomeCounty : Edm.String
- HomeCountry : Edm.String
- HomeState : Edm.String
- DateOfBirth : Edm.DateTimeOffset
- CountryOfBirth : Edm.String
- MartialStatus : SAPB1.BoMeritalStatuses
- NumOfChildren : Edm.Int32
- IdNumber : Edm.String
- CitizenshipCountryCode : Edm.String
- PassportNumber : Edm.String
- PassportExpirationDate : Edm.DateTimeOffset
- Picture : Edm.String
- Remarks : Edm.String
- SalaryCurrency : Edm.String
- EmployeeCostsCurrency : Edm.String
- WorkBuildingFloorRoom : Edm.String
- HomeBuildingFloorRoom : Edm.String
- Position : Edm.Int32
- AttachmentEntry : Edm.Int32
- CostCenterCode : Edm.String
- CompanyNumber : Edm.String
- VacationPreviousYear : Edm.Int32
- VacationCurrentYear : Edm.Int32
- MunicipalityKey : Edm.String
- TaxClass : Edm.String
- IncomeTaxLiability : Edm.String
- Religion : Edm.String
- PartnerReligion : Edm.String
- ExemptionAmount : Edm.Double
- ExemptionUnit : SAPB1.EmployeeExemptionUnitEnum
- ExemptionCurrency : Edm.String
- AdditionalAmount : Edm.Double
- AdditionalUnit : SAPB1.EmployeeExemptionUnitEnum
- AdditionalCurrency : Edm.String
- TaxOfficeName : Edm.String
- TaxOfficeNumber : Edm.String
- HealthInsuranceName : Edm.String
- HealthInsuranceCode : Edm.String
- HealthInsuranceType : Edm.String
- SocialInsuranceNumber : Edm.String
- ProfessionStatus : Edm.String
- EducationStatus : Edm.String
- PersonGroup : Edm.String
- JobTitleCode : Edm.String
- BankCodeForDATEV : Edm.String
- DeviatingBankAccountOwner : SAPB1.BoYesNoEnum
- SpouseFirstName : Edm.String
- SpouseSurname : Edm.String
- ExternalEmployeeNumber : Edm.String
- BirthPlace : Edm.String
- PaymentMethod : SAPB1.EmployeePaymentMethodEnum
- STDCode : Edm.Int32
- CPF : Edm.String
- CRCNumber : Edm.String
- AccountantResponsible : SAPB1.BoYesNoEnum
- LegalRepresentative : SAPB1.BoYesNoEnum
- DIRFResponsible : SAPB1.BoYesNoEnum
- CRCState : Edm.String
- Active : SAPB1.BoYesNoEnum
- IDType : Edm.String
- BPLID : Edm.Int32
- PassportIssueDate : Edm.DateTimeOffset
- PassportIssuer : Edm.String
- QualificationCode : SAPB1.SPEDContabilQualificationCodeEnum
- PRWebAccess : SAPB1.BoYesNoEnum
- PreviousPRWebAccess : SAPB1.BoYesNoEnum
- WorkStreetNumber : Edm.String
- HomeStreetNumber : Edm.String
- LinkedVendor : Edm.String
- CreateDate : Edm.DateTimeOffset
- CreateTime : Edm.TimeOfDay
- UpdateDate : Edm.DateTimeOffset
- UpdateTime : Edm.TimeOfDay
- EmployeeCode : Edm.String
- ARetSEFAZ : SAPB1.BoYesNoEnum
- GenderEx : Edm.String
- NaturalPer : SAPB1.BoYesNoEnum
- EmployeeAbsenceInfoLines : Collection(SAPB1.EmployeeAbsenceInfo)
- EmployeeEducationInfoLines : Collection(SAPB1.EmployeeEducationInfo)
- EmployeeReviewsInfoLines : Collection(SAPB1.EmployeeReviewsInfo)
- EmployeePreviousEmpoymentInfoLines : Collection(SAPB1.EmployeePreviousEmpoymentInfo)
- EmployeeRolesInfoLines : Collection(SAPB1.EmployeeRolesInfo)
- EmployeeSavingsPaymentInfoLines : Collection(SAPB1.EmployeeSavingsPaymentInfo)
- EmployeeBranchAssignment : Collection(SAPB1.EmployeeBranchAssignmentItem)

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- Drafts : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- Activities : Collection(SAPB1.Activity) [Partner=EmployeeInfo]
- BlanketAgreements : Collection(SAPB1.BlanketAgreement) [Partner=EmployeeInfo]
- CreditNotes : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- Invoices : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- Campaigns : Collection(SAPB1.Campaign) [Partner=EmployeeInfo]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- Orders : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- ProfitCenters : Collection(SAPB1.ProfitCenter) [Partner=EmployeeInfo]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- Returns : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- EmployeeRoleSetup : SAPB1.EmployeeRoleSetup [Partner=EmployeesInfo]
- Department2 : SAPB1.Department [Partner=EmployeesInfo]
- Branch2 : SAPB1.Branch [Partner=EmployeesInfo]
- Country : SAPB1.Country [Partner=EmployeesInfo]
- User : SAPB1.User [Partner=EmployeesInfo]
- SalesPerson : SAPB1.SalesPerson [Partner=EmployeesInfo]
- EmployeeStatus : SAPB1.EmployeeStatus [Partner=EmployeesInfo]
- TerminationReason : SAPB1.TerminationReason [Partner=EmployeesInfo]
- Bank : SAPB1.Bank [Partner=EmployeesInfo]
- EmployeePosition : SAPB1.EmployeePosition [Partner=EmployeesInfo]
- ProfitCenter : SAPB1.ProfitCenter [Partner=EmployeesInfo]
- EmployeeIDType : SAPB1.EmployeeIDType [Partner=EmployeesInfo]
- BusinessPlace : SAPB1.BusinessPlace [Partner=EmployeesInfo]
- BusinessPartner : SAPB1.BusinessPartner [Partner=EmployeesInfo]
- Gender2 : SAPB1.Gender [Partner=EmployeesInfo]
- CustomerEquipmentCards : Collection(SAPB1.CustomerEquipmentCard) [Partner=EmployeeInfo]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- ServiceCalls : Collection(SAPB1.ServiceCall) [Partner=EmployeeInfo]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=EmployeeInfo]
- DownPayments : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- ReturnRequest : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- Quotations : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- ProjectManagements : Collection(SAPB1.PM_ProjectDocumentData) [Partner=EmployeeInfo]
- ProjectManagementTimeSheet : Collection(SAPB1.PM_TimeSheetData) [Partner=EmployeeInfo]
- SalesOpportunities : Collection(SAPB1.SalesOpportunities) [Partner=EmployeeInfo]
- SelfInvoices : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- Items : Collection(SAPB1.Item) [Partner=EmployeeInfo]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=EmployeeInfo]
- Warehouses : Collection(SAPB1.Warehouse) [Partner=EmployeeInfo]

# SAPB1.EmployeeInfoParams (ComplexType)

## Properties

- EmployeeID : Edm.Int32

# SAPB1.EmployeePosition (EntityType)

Key: PositionID

## Properties

- PositionID : Edm.Int32 [required]
- Name : Edm.String
- Description : Edm.String

## Navigation properties

- EmployeesInfo : Collection(SAPB1.EmployeeInfo) [Partner=EmployeePosition]

# SAPB1.EmployeePositionParams (ComplexType)

## Properties

- PositionID : Edm.Int32
- Name : Edm.String
- Description : Edm.String

# SAPB1.EmployeePreviousEmpoymentInfo (ComplexType)

OpenType: true

## Properties

- EmployeeNo : Edm.Int32
- LineNum : Edm.Int32
- FromDtae : Edm.DateTimeOffset
- ToDate : Edm.DateTimeOffset
- Employer : Edm.String
- Position : Edm.String
- Remarks : Edm.String

# SAPB1.EmployeeReviewsInfo (ComplexType)

OpenType: true

## Properties

- EmployeeNo : Edm.Int32
- LineNum : Edm.Int32
- Date : Edm.DateTimeOffset
- ReviewDescription : Edm.String
- Manager : Edm.Int32
- Grade : Edm.String
- Remarks : Edm.String

# SAPB1.EmployeeRoleSetup (EntityType)

Key: TypeID

## Properties

- TypeID : Edm.Int32 [required]
- Name : Edm.String
- Description : Edm.String

## Navigation properties

- EmployeesInfo : Collection(SAPB1.EmployeeInfo) [Partner=EmployeeRoleSetup]

# SAPB1.EmployeeRoleSetupParams (ComplexType)

## Properties

- TypeID : Edm.Int32
- Name : Edm.String

# SAPB1.EmployeeRolesInfo (ComplexType)

OpenType: true

## Properties

- EmployeeID : Edm.Int32
- LineNum : Edm.Int32
- RoleID : Edm.Int32

# SAPB1.EmployeeSavingsPaymentInfo (ComplexType)

OpenType: true

## Properties

- EmployeeID : Edm.Int32
- LineNum : Edm.Int32
- ContractName : Edm.String
- PaymentNotes : Edm.String
- AN : Edm.Double
- ANcurrency : Edm.String
- AG : Edm.Double
- AGcurrency : Edm.String
- BankName : Edm.String
- BankCode : Edm.String
- BankAccount : Edm.String
- Sequence : SAPB1.ContractSequenceEnum

# SAPB1.EmployeeStatus (EntityType)

Key: StatusId

## Properties

- StatusId : Edm.Int32 [required]
- Name : Edm.String
- Description : Edm.String

## Navigation properties

- EmployeesInfo : Collection(SAPB1.EmployeeInfo) [Partner=EmployeeStatus]

# SAPB1.EmployeeStatusParams (ComplexType)

## Properties

- StatusId : Edm.Int32
- Name : Edm.String
- Description : Edm.String

# SAPB1.EmployeeTransfer (EntityType)

Key: TransferID

## Properties

- TransferID : Edm.Int32 [required]
- TransStartDate : Edm.DateTimeOffset
- TransStartTime : Edm.TimeOfDay
- TransEndDate : Edm.DateTimeOffset
- TransEndTime : Edm.TimeOfDay
- Status : SAPB1.EmployeeTransferStatusEnum
- Comment : Edm.String
- EmployeeTransferDetails : Collection(SAPB1.EmployeeTransferDetail)

# SAPB1.EmployeeTransferDetail (ComplexType)

## Properties

- TransferID : Edm.Int32
- EmployeeID : Edm.Int32
- TransferedDate : Edm.DateTimeOffset
- TransferedTime : Edm.TimeOfDay
- Status : SAPB1.EmployeeTransferProcessingStatusEnum
- Comment : Edm.String

# SAPB1.EmployeeTransferParams (ComplexType)

## Properties

- TransferID : Edm.Int32

# SAPB1.EmploymentCategory (EntityType)

Key: Code

## Properties

- Code : Edm.String [required]
- Description : Edm.String

# SAPB1.EmploymentCategoryParams (ComplexType)

## Properties

- Code : Edm.String

# SAPB1.EnhancedDiscountGroup (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- Type : SAPB1.DiscountGroupTypeEnum
- ObjectCode : Edm.String
- DiscountRelations : SAPB1.DiscountGroupRelationsEnum
- Active : SAPB1.BoYesNoEnum
- ValidFrom : Edm.DateTimeOffset
- ValidTo : Edm.DateTimeOffset
- DiscountGroupLineCollection : Collection(SAPB1.DiscountGroupLine)

# SAPB1.EnhancedDiscountGroupParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- Type : SAPB1.DiscountGroupTypeEnum
- ObjectCode : Edm.String

# SAPB1.Event (ComplexType)

## Properties

- WebhookID : Edm.String
- BusinessObject : Edm.String
- TransactionType : SAPB1.TransactionTypeEnum
- ObjectType : Edm.String

# SAPB1.Event (ComplexType)

## Properties

- WebhookID : Edm.String
- BusinessObject : Edm.String
- TransactionType : SAPB1.TransactionTypeEnum
- ObjectType : Edm.String

# SAPB1.EventCatagory (ComplexType)

## Properties

- Version : Edm.String
- Description : Edm.String
- Events : Collection(SAPB1.Event)

# SAPB1.EventNotification (EntityType)

Key: EventID

## Properties

- EventID : Edm.String [required]
- SourceDB : Edm.String
- Status : SAPB1.EventStatusEnum
- ObjectType : Edm.String
- BusinessObject : Edm.String
- TransactionType : Edm.String
- Operation : Edm.String
- FieldsInKey : Edm.Int32
- FieldNames : Edm.String
- FieldValues : Edm.String
- UserID : Edm.String
- ReplayState : SAPB1.EventReplayStateEnum
- CreateDate : Edm.DateTimeOffset
- CreateTime : Edm.TimeOfDay
- UpdateDate : Edm.DateTimeOffset
- UpdateTime : Edm.TimeOfDay

# SAPB1.EventNotificationParams (ComplexType)

## Properties

- EventID : Edm.String

# SAPB1.EventSubscription (EntityType)

Key: WebhookID

## Properties

- WebhookID : Edm.String [required]
- WebhookURL : Edm.String
- AuthenticationType : SAPB1.AuthenticationTypeEnum
- AuthenticationCred : Edm.String
- Handshake : SAPB1.BoYesNoEnum
- VerifyCertificate : SAPB1.BoYesNoEnum
- State : SAPB1.WebhookStateEnum
- WorkMode : SAPB1.WebhookWorkModeEnum
- CreateDate : Edm.DateTimeOffset
- UpdateDate : Edm.DateTimeOffset
- CreateTime : Edm.TimeOfDay
- UpdateTime : Edm.TimeOfDay
- LastSentDate : Edm.DateTimeOffset
- LastSentTime : Edm.TimeOfDay
- LastErrMsg : Edm.String
- EventCollection : Collection(SAPB1.Event)

# SAPB1.EventSubscriptionParams (ComplexType)

## Properties

- WebhookID : Edm.String

# SAPB1.EWayBillDetails (ComplexType)

## Properties

- DocEntry : Edm.Int32
- SupplyType : SAPB1.EWBSupplyTypeEnum
- SubType : Edm.Int32
- DocumentType : Edm.String
- TransportationMode : Edm.Int32
- Distance : Edm.Double
- TransporterDocNo : Edm.String
- TransporterDocDate : Edm.DateTimeOffset
- VehicleType : Edm.String
- VehicleNo : Edm.String
- EWayBillNo : Edm.String
- EWayBillDate : Edm.DateTimeOffset
- BillFromName : Edm.String
- BillFromGSTIN : Edm.String
- BillFromStateGSTCode : Edm.String
- DispatchFromAddress1 : Edm.String
- DispatchFromAddress2 : Edm.String
- DispatchFromZipCode : Edm.String
- DispatchFromStateGSTCode : Edm.String
- BillToName : Edm.String
- BillToGSTIN : Edm.String
- BillToStateGSTCode : Edm.String
- ShipToAddress1 : Edm.String
- ShipToAddress2 : Edm.String
- ShipToZipCode : Edm.String
- ShipToStateGSTCode : Edm.String
- MainHSNEntry : Edm.Int32
- DispatchFromPlace : Edm.String
- ShipToPlace : Edm.String
- TransporterID : Edm.String
- TransporterName : Edm.String
- EWayBillExpirationDate : Edm.DateTimeOffset
- TransporterEntry : Edm.Int32
- TransporterLineNumber : Edm.Int32
- TransactionType : SAPB1.EWBTransactionTypeEnum

# SAPB1.EWBTransporter (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- TransporterCode : Edm.String
- TransporterName : Edm.String
- TransporterID : Edm.String
- EWBTransporter_Lines : Collection(SAPB1.EWBTransporter_Line)

## Navigation properties

- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=EWBTransporter]

# SAPB1.EWBTransporter_Line (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- LineNumber : Edm.Int32
- Mode : Edm.Int32
- VehicleType : Edm.String
- VehicleNo : Edm.String

# SAPB1.EWBTransporterParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- TransporterCode : Edm.String
- TransporterName : Edm.String
- TransporterID : Edm.String

# SAPB1.ExceptionalEvent (EntityType)

Key: Code

## Properties

- Code : Edm.String [required]
- Description : Edm.String

# SAPB1.ExceptionalEventParams (ComplexType)

## Properties

- Code : Edm.String

# SAPB1.ExpenseTypeData (EntityType)

Key: ExpenseType

## Properties

- ExpenseType : Edm.String [required]
- ExpenseName : Edm.String
- ExpenseAccount : Edm.String
- PaidByCompany : SAPB1.BoYesNoEnum
- VatGroup : Edm.String

## Navigation properties

- ChartOfAccount : SAPB1.ChartOfAccount [Partner=ExpenseTypes]
- SalesTaxCode : SAPB1.SalesTaxCode [Partner=ExpenseTypes]

# SAPB1.ExpenseTypeParams (ComplexType)

## Properties

- ExpenseType : Edm.String

# SAPB1.ExportDetermination (EntityType)

OpenType: true
Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- Code : SAPB1.ElectronicDocProtocolCodeStrEnum
- Priority : Edm.Int32
- BusinessPartner : Edm.String
- Country : Edm.String
- Series : Edm.Int32
- DocumentType : Edm.String
- ExportFormat : Edm.Int32
- PathFileName : Edm.String
- DocumentSubType : Edm.String
- VersionNumber : Edm.Int32

## Navigation properties

- BusinessPartner2 : SAPB1.BusinessPartner [Partner=ExportDeterminations]
- Country2 : SAPB1.Country [Partner=ExportDeterminations]
- ElectronicFileFormat : SAPB1.ElectronicFileFormat [Partner=ExportDeterminations]

# SAPB1.ExportDeterminationParams (ComplexType)

OpenType: true

## Properties

- AbsEntry : Edm.Int32
- Code : SAPB1.ElectronicDocProtocolCodeStrEnum
- BusinessPartner : Edm.String
- Country : Edm.String
- Series : Edm.Int32
- DocumentType : Edm.String
- DocumentSubType : Edm.String

# SAPB1.ExportDeterminationsParams (ComplexType)

OpenType: true

## Properties

- Code : SAPB1.ElectronicDocProtocolCodeStrEnum

# SAPB1.ExportProcess (ComplexType)

## Properties

- LineNumber : Edm.Int32
- ExportationDocumentTypeCode : Edm.Int32
- ExportationDeclarationNumber : Edm.Int32
- ExportationDeclarationDate : Edm.DateTimeOffset
- ExportationNatureCode : Edm.Int32
- ExportationRegistryNumber : Edm.Int32
- ExportationRegistryDate : Edm.DateTimeOffset
- LadingBillNumber : Edm.String
- LadingBillDate : Edm.DateTimeOffset
- MerchandiseLeftCustomsDate : Edm.DateTimeOffset
- LadingBillTypeCode : Edm.Int32
- DrawbackSuspensionRegime : Edm.String
- NatureOfExport : Edm.String
- QuantityOfExportedItems : Edm.Double
- AdditionalItemSequentialNumber : Edm.Int32

# SAPB1.ExtendedAdminInfo (ComplexType)

## Properties

- AddressType : Edm.String
- StreetNo : Edm.String
- STDCode : Edm.Int32
- STDCodeForeign : Edm.Int32
- NatureOfCompanyCode : Edm.Int32
- EconomicActivityTypeCode : Edm.Int32
- CreditContributionOriginCode : Edm.String
- IPIPeriodCode : Edm.String
- CooperativeAssociationTypeCode : Edm.Int32
- ProfitTaxationCode : Edm.Int32
- CompanyQualificationCode : Edm.Int32
- DeclarerTypeCode : Edm.Int32
- IPITaxContributor : SAPB1.BoYesNoEnum
- CommercialRegister : Edm.String
- DateOfIncorporation : Edm.DateTimeOffset
- SPEDProfile : Edm.String
- EnvironmentType : Edm.Int32
- Opting4ICMS : SAPB1.BoYesNoEnum
- OKDPNumber : Edm.String
- GlobalLocationNumber : Edm.String
- EnableIntrastat : SAPB1.BoYesNoEnum
- AuthorityUser : Edm.String
- AuthorityPassword : Edm.String
- URLforGoodsTransportService : Edm.String
- URLforInvoiceTypeService : Edm.String
- ElectronicApprovalForGoodsTransEnabled : SAPB1.BoYesNoEnum
- ElectronicApprovalForInvoiceEnabled : SAPB1.BoYesNoEnum
- AllowInactiveItemsInInventoryOpeningBalance : SAPB1.BoYesNoEnum
- AllowInactiveItemsInInventoryCountingAndPosting : SAPB1.BoYesNoEnum
- AutoAssignNewBranchToBP : SAPB1.BoYesNoEnum
- DocumentRemarksInclude : SAPB1.DocumentRemarksIncludeTypeEnum
- CNPJOfIT : Edm.String
- CnPerson : Edm.String
- Email : Edm.String
- Telephone : Edm.String
- NoWarningForLinkTypeUDF : SAPB1.BoYesNoEnum
- EnableSameURLforPaymentTypeService : SAPB1.BoYesNoEnum
- CopyRefDocFormOrigDocToDupDoc : SAPB1.BoYesNoEnum

# SAPB1.ExtendedTranslation (EntityType)

Key: DocEntry

## Properties

- DocEntry : Edm.Int32 [required]
- Category : SAPB1.TranslationCategoryEnum
- ID : Edm.String
- SecondaryID : Edm.String
- SourceLanguage : Edm.Int32
- UpdateDate : Edm.DateTimeOffset
- CreateDate : Edm.DateTimeOffset
- ExtendedTranslation_ItemLines : Collection(SAPB1.ExtendedTranslation_ItemLine)

# SAPB1.ExtendedTranslation_ItemLine (ComplexType)

## Properties

- DocEntry : Edm.Int32
- LineNumber : Edm.Int32
- ItemCode : Edm.String
- ItemType : Edm.String
- SlimType : Edm.String
- MaxLength : Edm.Int32
- SourceText : Edm.String
- Memo : Edm.String
- ExtendedTranslation_ResultLines : Collection(SAPB1.ExtendedTranslation_ResultLine)

# SAPB1.ExtendedTranslation_ResultLine (ComplexType)

## Properties

- DocEntry : Edm.Int32
- LineNumber : Edm.Int32
- SubLineNumber : Edm.Int32
- LanguageCode : Edm.Int32
- TranslatedText : Edm.String

# SAPB1.ExtendedTranslationParams (ComplexType)

## Properties

- DocEntry : Edm.Int32
- Category : SAPB1.TranslationCategoryEnum
- ID : Edm.String
- SecondaryID : Edm.String

# SAPB1.ExternalCall (ComplexType)

## Properties

- ID : Edm.Int32
- Category : Edm.Int32
- Status : SAPB1.ExternalCallStatusEnum
- CreationDate : Edm.DateTimeOffset
- CreationTime : Edm.Int32
- LastUpdateDate : Edm.DateTimeOffset
- LastUpdateTime : Edm.Int32
- LastUpdateUserCode : Edm.String
- CallArguments : Collection(SAPB1.CallArgument)
- CallMessages : Collection(SAPB1.CallMessage)

# SAPB1.ExternalCallParams (ComplexType)

## Properties

- ID : Edm.Int32

# SAPB1.ExternalReconciliation (ComplexType)

## Properties

- ReconciliationAccountType : SAPB1.ReconciliationAccountTypeEnum
- AccountCode : Edm.String
- ReconciliationNo : Edm.Int32
- Amount : Edm.Double
- CurrencyType : Edm.String
- ReconciliationType : Edm.String
- ReconciliationDate : Edm.DateTimeOffset
- CreationDate : Edm.DateTimeOffset
- ReconciliationJournalEntryLines : Collection(SAPB1.ReconciliationJournalEntryLine)
- ReconciliationBankStatementLines : Collection(SAPB1.ReconciliationBankStatementLine)

# SAPB1.ExternalReconciliationFilterParams (ComplexType)

## Properties

- AccountCodeFrom : Edm.String
- AccountCodeTo : Edm.String
- ReconciliationDateFrom : Edm.DateTimeOffset
- ReconciliationDateTo : Edm.DateTimeOffset
- ReconciliationNoFrom : Edm.Int32
- ReconciliationNoTo : Edm.Int32
- ReconciliationAccountType : SAPB1.ReconciliationAccountTypeEnum

# SAPB1.ExternalReconciliationParams (ComplexType)

## Properties

- AccountCode : Edm.String
- ReconciliationNo : Edm.Int32

# SAPB1.FAAccountDetermination (EntityType)

Key: Code

## Properties

- Code : Edm.String [required]
- Description : Edm.String
- AssetBalanceSheetAccount : Edm.String
- ClearingAccountAcquisition : Edm.String
- RevaluationReserveAccount : Edm.String
- RevaluationReserveClearing : Edm.String
- OrdinaryDepreciation : Edm.String
- AccumulatedOrdinaryDepr : Edm.String
- UnplannedDepreciation : Edm.String
- AccumulatedUnplannedDepr : Edm.String
- SpecialDepreciation : Edm.String
- AccumulatedSpecialDepr : Edm.String
- RevenuefromAssetSalesNet : Edm.String
- RetirementwithExpenseNet : Edm.String
- RetirementwithRevenueNet : Edm.String
- LeavewithExpenseNBVGross : Edm.String
- LeavewithRevenueNBVGross : Edm.String
- RevenueAccountforRetirement : Edm.String
- RevenueClearingAccount : Edm.String
- RevaluationAccount : Edm.String
- RevaluationLossAcct : Edm.String

## Navigation properties

- ChartOfAccount : SAPB1.ChartOfAccount [Partner=FAAccountDeterminations]

# SAPB1.FAAccountDeterminationParams (ComplexType)

## Properties

- Code : Edm.String
- Description : Edm.String

# SAPB1.FactoringIndicator (EntityType)

OpenType: true
Key: IndicatorCode

## Properties

- IndicatorCode : Edm.String [required]
- IndicatorName : Edm.String

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- Drafts : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- CreditNotes : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- Invoices : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- Orders : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- Returns : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=FactoringIndicator]
- DownPayments : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- ReturnRequest : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- Quotations : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- JournalEntries : Collection(SAPB1.JournalEntry) [Partner=FactoringIndicator]
- SelfInvoices : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=FactoringIndicator]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=FactoringIndicator]

# SAPB1.FactoringIndicatorParams (ComplexType)

## Properties

- IndicatorCode : Edm.String

# SAPB1.FeatureStatus (ComplexType)

## Properties

- FeatureID : Edm.String
- Blocked : SAPB1.BoYesNoEnum

# SAPB1.FieldID (ComplexType)

OpenType: true

## Properties

- FieldIDProperty : Edm.String

# SAPB1.FIFOLayer (ComplexType)

OpenType: true

## Properties

- TransactionSequenceNum : Edm.Int32
- LayerID : Edm.Int32
- Quantity : Edm.Double
- Price : Edm.Double
- LineTotal : Edm.Double
- BaseLine : Edm.Int32

# SAPB1.FinancePeriod (ComplexType)

## Properties

- AbsoluteEntry : Edm.Int32
- PeriodCode : Edm.String
- PeriodName : Edm.String
- PostingDateFrom : Edm.DateTimeOffset
- PostingDateTo : Edm.DateTimeOffset
- ValueDateFrom : Edm.DateTimeOffset
- ValueDateTo : Edm.DateTimeOffset
- TaxDateFrom : Edm.DateTimeOffset
- TaxDateTo : Edm.DateTimeOffset
- ActiveforFeed : SAPB1.BoYesNoEnum
- Locked : SAPB1.BoYesNoEnum
- AdditionalSubPeriods : SAPB1.BoYesNoEnum
- PeriodIndicator : Edm.String
- SubNum : Edm.Int32
- PeriodStatus : SAPB1.PeriodStatusEnum

# SAPB1.FinancePeriodParams (ComplexType)

## Properties

- AbsoluteEntry : Edm.Int32
- PeriodIndicator : Edm.String

# SAPB1.FinancialYear (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- Code : Edm.String
- Description : Edm.String
- StartDate : Edm.DateTimeOffset
- EndDate : Edm.DateTimeOffset
- AssessYear : Edm.String
- TCSAccumulationBase : SAPB1.TCSAccumulationBaseEnum

# SAPB1.FinancialYearParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- Code : Edm.String
- Description : Edm.String

# SAPB1.FiscalPrinter (EntityType)

Key: EquipmentNo

## Properties

- EquipmentNo : Edm.String [required]
- Model : Edm.String
- ManufacturerSerialN : Edm.String
- RegisterNo : Edm.Int32
- FiscalDocumentModel : Edm.String
- FiscalPrintersParams : Collection(SAPB1.FiscalPrinterParams)

## Navigation properties

- POSDailySummary : Collection(SAPB1.POSDailySummary) [Partner=FiscalPrinter]
- NFModel : SAPB1.NFModel [Partner=FiscalPrinter]

# SAPB1.FiscalPrinterParams (ComplexType)

## Properties

- EquipmentNo : Edm.String

# SAPB1.FixedAssetEndBalance (ComplexType)

## Properties

- HistoricalAPC : Edm.Double
- AcquisitionCost : Edm.Double
- NetBookValue : Edm.Double
- HistoricalNBV : Edm.Double
- OrdinaryDepreciationValue : Edm.Double
- UnplanedDepreciationValue : Edm.Double
- SpecialDepreciationValue : Edm.Double
- WriteUp : Edm.Double
- SalvageValue : Edm.Double
- Quantity : Edm.Double

# SAPB1.FixedAssetValues (ComplexType)

## Properties

- TransactionType : SAPB1.AssetTransactionTypeEnum
- AcquisitionCost : Edm.Double
- Quantity : Edm.Double
- DepreciationValue : Edm.Double
- NetBookValue : Edm.Double
- OrdinaryDepreciationValue : Edm.Double
- UnplanedDepreciationValue : Edm.Double
- SpecialDepreciationValue : Edm.Double
- WriteUp : Edm.Double
- Appreciation : Edm.Double

# SAPB1.FixedAssetValuesParams (ComplexType)

## Properties

- ItemCode : Edm.String
- FiscalYear : Edm.String
- DepreciationArea : Edm.String

# SAPB1.FormattedSearch (EntityType)

OpenType: true
Key: Index

## Properties

- FormID : Edm.String
- ItemID : Edm.String
- ColumnID : Edm.String
- Action : SAPB1.BoFormattedSearchActionEnum
- QueryID : Edm.Int32
- Index : Edm.Int32 [required]
- Refresh : SAPB1.BoYesNoEnum
- FieldID : Edm.String
- ForceRefresh : SAPB1.BoYesNoEnum
- ByField : SAPB1.BoYesNoEnum
- ByFieldEx : SAPB1.FormattedSearchByFieldEnum
- UserValidValues : Collection(SAPB1.UserValidValue)
- FieldIDs : Collection(SAPB1.FieldID)

# SAPB1.FormattedSearchParams (ComplexType)

## Properties

- Index : Edm.Int32

# SAPB1.Forms1099 (EntityType)

OpenType: true
Key: FormCode

## Properties

- FormCode : Edm.Int32 [required]
- Form1099 : Edm.String
- Boxes1099 : Collection(SAPB1.Boxes1099Item)

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=Forms1099]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=Forms1099]
- Drafts : Collection(SAPB1.Document) [Partner=Forms1099]
- CreditNotes : Collection(SAPB1.Document) [Partner=Forms1099]
- Invoices : Collection(SAPB1.Document) [Partner=Forms1099]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=Forms1099]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=Forms1099]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=Forms1099]
- Orders : Collection(SAPB1.Document) [Partner=Forms1099]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=Forms1099]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=Forms1099]
- Returns : Collection(SAPB1.Document) [Partner=Forms1099]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=Forms1099]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=Forms1099]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=Forms1099]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=Forms1099]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=Forms1099]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=Forms1099]
- DownPayments : Collection(SAPB1.Document) [Partner=Forms1099]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=Forms1099]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=Forms1099]
- ReturnRequest : Collection(SAPB1.Document) [Partner=Forms1099]
- Quotations : Collection(SAPB1.Document) [Partner=Forms1099]
- SelfInvoices : Collection(SAPB1.Document) [Partner=Forms1099]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=Forms1099]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=Forms1099]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=Forms1099]

# SAPB1.Forms1099Params (ComplexType)

## Properties

- FormCode : Edm.Int32

# SAPB1.Gender (EntityType)

Key: Code

## Properties

- Code : Edm.String [required]
- Description : Edm.String

## Navigation properties

- EmployeesInfo : Collection(SAPB1.EmployeeInfo) [Partner=Gender2]

# SAPB1.GendersParams (ComplexType)

## Properties

- Code : Edm.String

# SAPB1.GeneratedAsset (ComplexType)

## Properties

- DocEntry : Edm.Int32
- LineNumber : Edm.Int32
- VisualOrder : Edm.Int32
- AssetCode : Edm.String
- Status : SAPB1.GeneratedAssetStatusEnum
- Remarks : Edm.String
- SerialNumber : Edm.String
- amount : Edm.Double
- amountSC : Edm.Double

# SAPB1.GetChangeLogParams (ComplexType)

## Properties

- PrimaryKey : Edm.String
- UDOObjectCode : Edm.String
- Object : SAPB1.BoChangeLogEnum

# SAPB1.GLAccount (ComplexType)

## Properties

- Code : Edm.String
- DueDate : Edm.DateTimeOffset
- Debit : Edm.Double
- Credit : Edm.Double
- SystemDebit : Edm.Double
- SystemCredit : Edm.Double
- ForeignDebit : Edm.Double
- ForeignCredit : Edm.Double
- ForeignCurrency : Edm.String

# SAPB1.GLAccountAdvancedRule (EntityType)

Key: AbsoluteEntry

## Properties

- AbsoluteEntry : Edm.Int32 [required]
- Period : Edm.String
- BeginningofFinancialYear : Edm.DateTimeOffset
- FinancialYear : Edm.Int32
- PeriodName : Edm.String
- SubPeriodType : SAPB1.BoSubPeriodTypeEnum
- NumberOfPeriods : Edm.Int32
- FromPostingDate : Edm.DateTimeOffset
- ToPostingDate : Edm.DateTimeOffset
- FromDueDate : Edm.DateTimeOffset
- ToDueDate : Edm.DateTimeOffset
- FromDocumentDate : Edm.DateTimeOffset
- ToDocumentDate : Edm.DateTimeOffset
- ItemCode : Edm.String
- ItemGroup : Edm.Int32
- Warehouse : Edm.String
- BPGroup : Edm.Int32
- FederalTaxID : Edm.String
- ShipToCountry : Edm.String
- ShipToState : Edm.String
- Description : Edm.String
- Code : Edm.String
- GetGLAccountBy : SAPB1.GetGLAccountByEnum
- FromDate : Edm.DateTimeOffset
- ToDate : Edm.DateTimeOffset
- ExpensesAccount : Edm.String
- RevenuesAccount : Edm.String
- ExemptIncomeAcc : Edm.String
- InventoryAccount : Edm.String
- CostAccount : Edm.String
- TransferAccount : Edm.String
- VarienceAccount : Edm.String
- PriceDifferenceAcc : Edm.String
- NegativeInventoryAdjustmentAccount : Edm.String
- DecreasingAccount : Edm.String
- IncreasingAccount : Edm.String
- ReturningAccount : Edm.String
- EURevenuesAccount : Edm.String
- EUExpensesAccount : Edm.String
- ForeignRevenueAcc : Edm.String
- ForeignExpensAcc : Edm.String
- PurchaseAcct : Edm.String
- PAReturnAcct : Edm.String
- PurchaseOffsetAcct : Edm.String
- ExchangeRateDifferencesAcct : Edm.String
- GoodsClearingAcct : Edm.String
- GLDecreaseAcct : Edm.String
- GLIncreaseAcct : Edm.String
- WipAccount : Edm.String
- WipVarianceAccount : Edm.String
- WipOffsetProfitAndLossAccount : Edm.String
- InventoryOffsetProfitAndLossAccount : Edm.String
- StockInflationAdjustAccount : Edm.String
- StockInflationOffsetAccount : Edm.String
- CostInflationAccount : Edm.String
- CostInflationOffsetAccount : Edm.String
- ExpenseClearingAct : Edm.String
- ExpenseOffsettingAccount : Edm.String
- StockInTransitAccount : Edm.String
- ShippedGoodsAccount : Edm.String
- VATInRevenueAccount : Edm.String
- SalesCreditAcc : Edm.String
- PurchaseCreditAcc : Edm.String
- ExemptedCredits : Edm.String
- SalesCreditForeignAcc : Edm.String
- ForeignPurchaseCreditAcc : Edm.String
- SalesCreditEUAcc : Edm.String
- EUPurchaseCreditAcc : Edm.String
- PurchaseBalanceAccount : Edm.String
- WHIncomingCenvatAccount : Edm.String
- WHOutgoingCenvatAccount : Edm.String
- IsActive : SAPB1.BoYesNoEnum
- BusinessPartnerType : SAPB1.BoBusinessPartnerTypes
- VATGroup : Edm.String
- BPCode : Edm.String
- Usage : Edm.Int32
- UDF1 : Edm.String
- UDF2 : Edm.String
- UDF3 : Edm.String
- UDF4 : Edm.String
- UDF5 : Edm.String

## Navigation properties

- Item : SAPB1.Item [Partner=GLAccountAdvancedRules]
- ItemGroups : SAPB1.ItemGroups [Partner=GLAccountAdvancedRules]
- Warehouse2 : SAPB1.Warehouse [Partner=GLAccountAdvancedRules]
- BusinessPartnerGroup : SAPB1.BusinessPartnerGroup [Partner=GLAccountAdvancedRules]
- Country : SAPB1.Country [Partner=GLAccountAdvancedRules]
- ChartOfAccount : SAPB1.ChartOfAccount [Partner=GLAccountAdvancedRules]
- VatGroup : SAPB1.VatGroup [Partner=GLAccountAdvancedRules]
- BusinessPartner : SAPB1.BusinessPartner [Partner=GLAccountAdvancedRules]
- NotaFiscalUsage : SAPB1.NotaFiscalUsage [Partner=GLAccountAdvancedRules]

# SAPB1.GLAccountAdvancedRuleParams (ComplexType)

## Properties

- AbsoluteEntry : Edm.Int32
- Period : Edm.String
- Code : Edm.String
- ItemCode : Edm.String
- ItemGroup : Edm.Int32
- Warehouse : Edm.String
- BPGroup : Edm.Int32
- FederalTaxID : Edm.String
- ShipToCountry : Edm.String
- ShipToState : Edm.String

# SAPB1.GovPayCode (EntityType)

Key: AbsId

## Properties

- AbsId : Edm.Int32 [required]
- Code : Edm.String
- Descr : Edm.String
- StateTax : SAPB1.BoYesNoEnum
- Prdcity : SAPB1.GovPayCodePeriodicityEnum
- GovPayCodeAuthorities : Collection(SAPB1.GovPayCodeAuthority)

## Navigation properties

- NFTaxCategories : Collection(SAPB1.NFTaxCategory) [Partner=GovPayCode]

# SAPB1.GovPayCodeAuthority (ComplexType)

## Properties

- AbsId : Edm.Int32
- BPLId : Edm.Int32
- State : Edm.String
- CardCode : Edm.String

# SAPB1.GovPayCodeParams (ComplexType)

## Properties

- AbsId : Edm.Int32
- Code : Edm.String

# SAPB1.GTIParams (ComplexType)

## Properties

- InboundFile : Edm.String
- AbsEntry : Edm.Int32

# SAPB1.Holiday (EntityType)

Key: HolidayCode

## Properties

- HolidayCode : Edm.String [required]
- WeekendFrom : SAPB1.BoWeekEnum
- WeekendTO : SAPB1.BoWeekEnum
- ValidForOneYearOnly : SAPB1.BoYesNoEnum
- SetWeekendsAsWorkDays : Edm.String
- WeekNoRule : SAPB1.BoWeekNoRuleEnum
- HolidayDates : Collection(SAPB1.HolidayDate)

# SAPB1.HolidayDate (ComplexType)

## Properties

- HolidayCode : Edm.String
- StartDate : Edm.DateTimeOffset
- EndDate : Edm.DateTimeOffset
- Remarks : Edm.String

# SAPB1.HolidayParams (ComplexType)

## Properties

- HolidayCode : Edm.String

# SAPB1.HouseBankAccount (EntityType)

OpenType: true
Key: AbsoluteEntry

## Properties

- BankCode : Edm.String
- AccNo : Edm.String
- Branch : Edm.String
- NextCheckNo : Edm.Int32
- GLAccount : Edm.String
- DSC1_STREET_ALIAS : Edm.String
- Block : Edm.String
- ZipCode : Edm.String
- City : Edm.String
- County : Edm.String
- Country : Edm.String
- State : Edm.String
- BISR : SAPB1.BoYesNoEnum
- ControlKey : Edm.String
- UserNo1 : Edm.String
- UserNo2 : Edm.String
- UserNo3 : Edm.String
- UserNo4 : Edm.String
- IBAN : Edm.String
- DebtofDiscountedBillofExc : Edm.String
- ToleranceDays : Edm.Int32
- MinAmountofBillofExchang : Edm.Double
- MaxAmountofBillofExchan : Edm.Double
- DiscountLimit : Edm.Double
- DaysInAdvance : Edm.Int32
- BankonCollection : Edm.String
- BankonDiscounted : Edm.String
- GLInterimAccount : Edm.String
- AbsoluteEntry : Edm.Int32 [required]
- BankKey : Edm.Int32
- LockChecksPrinting : SAPB1.BoYesNoEnum
- TemplateName : Edm.String
- MaximumLines : Edm.Int32
- PrintOn : SAPB1.PrintOnEnum
- CustomerIdNumber : Edm.String
- ISRBillerID : Edm.String
- ISRType : Edm.Int32
- AccountCheckDigit : Edm.String
- OurNumber : Edm.Int32
- AgreementNumber : Edm.String
- AddressType : Edm.String
- StreetNo : Edm.String
- Building : Edm.String
- IncomingPaymentSeries : Edm.Int32
- OutgoingPaymentSeries : Edm.Int32
- JournalEntrySeries : Edm.Int32
- ImportFileName : Edm.String
- AccountName : Edm.String
- BICSwiftCode : Edm.String
- FineAccount : Edm.String
- InterestAccount : Edm.String
- DiscountAccount : Edm.String
- ServiceFeeAccount : Edm.String
- IOFTaxAccount : Edm.String
- OtherExpensesAccount : Edm.String
- OtherIncomesAccount : Edm.String
- RetornoFileName : Edm.String
- BranchCheckDigit : Edm.String
- CollectionCode : Edm.String
- FileSeqNextNumber : Edm.Int32
- NoValidationForStartingEndingBal : SAPB1.BoYesNoEnum
- ECheck : SAPB1.BoYesNoEnum

## Navigation properties

- BankStatements : Collection(SAPB1.BankStatement) [Partner=HouseBankAccount]
- ChartOfAccount : SAPB1.ChartOfAccount [Partner=HouseBankAccounts]
- Country2 : SAPB1.Country [Partner=HouseBankAccounts]
- Bank : SAPB1.Bank [Partner=HouseBankAccounts]
- WizardPaymentMethods : Collection(SAPB1.WizardPaymentMethod) [Partner=HouseBankAccount]

# SAPB1.HouseBankAccountParams (ComplexType)

## Properties

- AbsoluteEntry : Edm.Int32

# SAPB1.IdentificationCode (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- Codelist : SAPB1.IdentificationCodeTypeEnum
- Code : Edm.String
- Description : Edm.String
- SchemaCode : Edm.String
- SchemaDesc : Edm.String

## Navigation properties

- Items : Collection(SAPB1.Item) [Partner=IdentificationCode]

# SAPB1.IdentificationCodeParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32

# SAPB1.ImportDetermination (EntityType)

OpenType: true
Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- Code : SAPB1.ElectronicDocProtocolCodeStrEnum
- LineNumber : Edm.Int32
- ObjectType : Edm.String
- ObjectTypeXPath : Edm.String
- FieldType : SAPB1.ImportFieldTypeEnum
- FieldTypeXPath : Edm.String
- ImportFormat : Edm.Int32
- DefaultDigitalSeries : Edm.Int32
- VersionNumber : Edm.Int32

## Navigation properties

- ElectronicFileFormat : SAPB1.ElectronicFileFormat [Partner=ImportDeterminations]

# SAPB1.ImportDeterminationParams (ComplexType)

OpenType: true

## Properties

- AbsEntry : Edm.Int32
- Code : SAPB1.ElectronicDocProtocolCodeStrEnum
- ObjectType : Edm.String

# SAPB1.ImportDeterminationsParams (ComplexType)

OpenType: true

## Properties

- Code : SAPB1.ElectronicDocProtocolCodeStrEnum

# SAPB1.ImportProcess (ComplexType)

## Properties

- LineNumber : Edm.Int32
- ImportationDocumentTypeCode : Edm.String
- ImportationDocumentNumber : Edm.String
- DateOfRegistry_DI_DSI_DA : Edm.DateTimeOffset
- CustomsClearanceDate : Edm.DateTimeOffset
- DrawbackRegimeConcessionAccountNumber : Edm.String
- AdditionalNumber : Edm.String
- AdditionalItemDiscountValue : Edm.Double
- DrawbackSuspensionRegime : Edm.String
- TypeOfImport : Edm.String
- AdditionalFreightToNavyAuthority : Edm.Double
- AdditionalItemSequentialNumber : Edm.Int32

# SAPB1.IndiaHsn (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- Chapter : Edm.String
- Heading : Edm.String
- SubHeading : Edm.String
- Description : Edm.String
- ChapterID : Edm.String

## Navigation properties

- Items : Collection(SAPB1.Item) [Partner=IndiaHsn]

# SAPB1.IndiaHsnParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- ChapterID : Edm.String

# SAPB1.IndiaSacCode (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- ServiceCode : Edm.String
- ServiceName : Edm.String

## Navigation properties

- Items : Collection(SAPB1.Item) [Partner=IndiaSacCode]

# SAPB1.IndiaSacCodeParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- ServiceCode : Edm.String

# SAPB1.IndividualCounter (ComplexType)

## Properties

- DocumentEntry : Edm.Int32
- CounterID : Edm.Int32
- CounterType : SAPB1.CounterTypeEnum
- CounterName : Edm.String
- CounterNumber : Edm.Int32
- CounterVisualOrder : Edm.Int32

# SAPB1.Industry (EntityType)

OpenType: true
Key: IndustryCode

## Properties

- IndustryDescription : Edm.String
- IndustryName : Edm.String
- IndustryCode : Edm.Int32 [required]

## Navigation properties

- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=Industry2]
- ProjectManagements : Collection(SAPB1.PM_ProjectDocumentData) [Partner=Industry2]
- SalesOpportunities : Collection(SAPB1.SalesOpportunities) [Partner=Industry2]

# SAPB1.IndustryParams (ComplexType)

## Properties

- IndustryCode : Edm.Int32

# SAPB1.IntegrationPackageConfigure (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- Code : Edm.String
- Name : Edm.String
- IsEnable : SAPB1.BoYesNoEnum

# SAPB1.IntegrationPackageParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32

# SAPB1.InternalReconciliation (EntityType)

Key: ReconNum

## Properties

- ReconNum : Edm.Int32 [required]
- ReconDate : Edm.DateTimeOffset
- CardOrAccount : SAPB1.CardOrAccountEnum
- ReconType : SAPB1.ReconTypeEnum
- Total : Edm.Double
- CancelAbs : Edm.Int32
- InternalReconciliationRows : Collection(SAPB1.InternalReconciliationRow)
- ElectronicProtocols : Collection(SAPB1.ElectronicProtocol)

# SAPB1.InternalReconciliationBP (ComplexType)

## Properties

- BPCode : Edm.String

# SAPB1.InternalReconciliationOpenTrans (ComplexType)

## Properties

- ReconDate : Edm.DateTimeOffset
- CardOrAccount : SAPB1.CardOrAccountEnum
- BPLId : Edm.Int32
- InternalReconciliationOpenTransRows : Collection(SAPB1.InternalReconciliationOpenTransRow)
- ElectronicProtocols : Collection(SAPB1.ElectronicProtocol)

# SAPB1.InternalReconciliationOpenTransParams (ComplexType)

## Properties

- ReconDate : Edm.DateTimeOffset
- CardOrAccount : SAPB1.CardOrAccountEnum
- AccountNo : Edm.String
- DateType : SAPB1.ReconSelectDateTypeEnum
- FromDate : Edm.DateTimeOffset
- ToDate : Edm.DateTimeOffset
- InternalReconciliationBPs : Collection(SAPB1.InternalReconciliationBP)

# SAPB1.InternalReconciliationOpenTransRow (ComplexType)

## Properties

- Selected : SAPB1.BoYesNoEnum
- ShortName : Edm.String
- TransId : Edm.Int32
- TransRowId : Edm.Int32
- SrcObjTyp : Edm.String
- SrcObjAbs : Edm.Int32
- CreditOrDebit : SAPB1.CreditOrDebitEnum
- ReconcileAmount : Edm.Double
- CashDiscount : Edm.Double

# SAPB1.InternalReconciliationParams (ComplexType)

## Properties

- ReconNum : Edm.Int32

# SAPB1.InternalReconciliationRow (ComplexType)

## Properties

- LineSeq : Edm.Int32
- ShortName : Edm.String
- TransId : Edm.Int32
- TransRowId : Edm.Int32
- SrcObjTyp : Edm.String
- SrcObjAbs : Edm.Int32
- CreditOrDebit : SAPB1.CreditOrDebitEnum
- ReconcileAmount : Edm.Double
- CashDiscount : Edm.Double

# SAPB1.IntrastatConfiguration (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- ConfType : SAPB1.IntrastatConfigurationEnum
- Code : Edm.String
- Descr : Edm.String
- PrcstVal : Edm.Double
- SuppUnit : Edm.Int32
- Export : SAPB1.BoYesNoEnum
- Import : SAPB1.BoYesNoEnum
- StatCode : Edm.String
- DateFrom : Edm.DateTimeOffset
- DateTo : Edm.DateTimeOffset
- Country : Edm.String
- ConfID : Edm.String
- TriangDeal : SAPB1.IntrastatConfigurationTriangDealEnum

# SAPB1.IntrastatConfigurationParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- ConfType : SAPB1.IntrastatConfigurationEnum
- Code : Edm.String
- StatCode : Edm.String
- DateFrom : Edm.DateTimeOffset
- DateTo : Edm.DateTimeOffset
- Country : Edm.String

# SAPB1.InventoryCounting (EntityType)

OpenType: true
Key: DocumentEntry

## Properties

- DocumentEntry : Edm.Int32 [required]
- DocumentNumber : Edm.Int32
- Series : Edm.Int32
- CountDate : Edm.DateTimeOffset
- CountTime : Edm.TimeOfDay
- SingleCounterType : SAPB1.CounterTypeEnum
- SingleCounterID : Edm.Int32
- DocumentStatus : SAPB1.CountingDocumentStatusEnum
- Remarks : Edm.String
- Reference2 : Edm.String
- BranchID : Edm.Int32
- DocObjectCodeEx : Edm.String
- FinancialPeriod : Edm.Int32
- PeriodIndicator : Edm.String
- CountingType : SAPB1.CountingTypeEnum
- AttachmentEntry : Edm.Int32
- YearEndDate : Edm.DateTimeOffset
- TeamCounters : Collection(SAPB1.TeamCounter)
- IndividualCounters : Collection(SAPB1.IndividualCounter)
- InventoryCountingLines : Collection(SAPB1.InventoryCountingLine)
- InventoryCountingDocumentReferencesCollection : Collection(SAPB1.InventoryCountingDocumentReferences)

## Navigation properties

- BusinessPlace : SAPB1.BusinessPlace [Partner=InventoryCountings]
- Attachments2 : SAPB1.Attachments2 [Partner=InventoryCountings]

# SAPB1.InventoryCountingBatchNumber (ComplexType)

## Properties

- BatchNumber : Edm.String
- ManufacturerSerialNumber : Edm.String
- InternalSerialNumber : Edm.String
- ExpiryDate : Edm.DateTimeOffset
- ManufactureDate : Edm.DateTimeOffset
- AddmisionDate : Edm.DateTimeOffset
- Location : Edm.String
- Notes : Edm.String
- Quantity : Edm.Double
- BaseLineNumber : Edm.Int32
- DocumentEntry : Edm.Int32
- CounterType : SAPB1.CounterTypeEnum
- CounterID : Edm.Int32
- MultipleCounterRole : SAPB1.MultipleCounterRoleEnum
- TrackingNote : Edm.Int32
- TrackingNoteLine : Edm.Int32
- ItemCode : Edm.String
- SystemSerialNumber : Edm.Int32

# SAPB1.InventoryCountingDocumentReferences (ComplexType)

## Properties

- DocEntry : Edm.Int32
- LineNumber : Edm.Int32
- ReferencedDocEntry : Edm.Int32
- ReferencedDocNumber : Edm.Int32
- ExternalReferencedDocNumber : Edm.String
- ReferencedObjectType : SAPB1.ReferencedObjectTypeEnum
- IssueDate : Edm.DateTimeOffset
- Remark : Edm.String

# SAPB1.InventoryCountingDraft (EntityType)

OpenType: true
Key: DocumentEntry

## Properties

- DocumentEntry : Edm.Int32 [required]
- DocumentNumber : Edm.Int32
- Series : Edm.Int32
- CountDate : Edm.DateTimeOffset
- CountTime : Edm.TimeOfDay
- SingleCounterType : SAPB1.CounterTypeEnum
- SingleCounterID : Edm.Int32
- DocumentStatus : SAPB1.CountingDocumentStatusEnum
- Remarks : Edm.String
- Reference2 : Edm.String
- BranchID : Edm.Int32
- DocObjectCodeEx : Edm.String
- FinancialPeriod : Edm.Int32
- PeriodIndicator : Edm.String
- CountingType : SAPB1.CountingTypeEnum
- AttachmentEntry : Edm.Int32
- YearEndDate : Edm.DateTimeOffset

## Navigation properties

- BusinessPlace : SAPB1.BusinessPlace [Partner=InventoryCountingDrafts]
- Attachments2 : SAPB1.Attachments2 [Partner=InventoryCountingDrafts]

# SAPB1.InventoryCountingDraftParams (ComplexType)

## Properties

- DocumentEntry : Edm.Int32
- DocumentNumber : Edm.Int32

# SAPB1.InventoryCountingLine (ComplexType)

OpenType: true

## Properties

- DocumentEntry : Edm.Int32
- LineNumber : Edm.Int32
- ItemCode : Edm.String
- ItemDescription : Edm.String
- Freeze : SAPB1.BoYesNoEnum
- WarehouseCode : Edm.String
- BinEntry : Edm.Int32
- InWarehouseQuantity : Edm.Double
- Counted : SAPB1.BoYesNoEnum
- UoMCode : Edm.String
- BarCode : Edm.String
- UoMCountedQuantity : Edm.Double
- ItemsPerUnit : Edm.Double
- CountedQuantity : Edm.Double
- Variance : Edm.Double
- VariancePercentage : Edm.Double
- VisualOrder : Edm.Int32
- TargetEntry : Edm.Int32
- TargetLine : Edm.Int32
- TargetType : Edm.Int32
- TargetReference : Edm.String
- ProjectCode : Edm.String
- Manufacturer : Edm.Int32
- SupplierCatalogNo : Edm.String
- PreferredVendor : Edm.String
- CostingCode : Edm.String
- CostingCode2 : Edm.String
- CostingCode3 : Edm.String
- CostingCode4 : Edm.String
- CostingCode5 : Edm.String
- Remarks : Edm.String
- LineStatus : SAPB1.CountingLineStatusEnum
- CounterType : SAPB1.CounterTypeEnum
- CounterID : Edm.Int32
- MultipleCounterRole : SAPB1.MultipleCounterRoleEnum
- WeightOfRecycledPlastic : Edm.Double
- PlasticPackageExemptionReason : Edm.String
- InventoryCountingLineUoMs : Collection(SAPB1.InventoryCountingLineUoM)
- InventoryCountingSerialNumbers : Collection(SAPB1.InventoryCountingSerialNumber)
- InventoryCountingBatchNumbers : Collection(SAPB1.InventoryCountingBatchNumber)

# SAPB1.InventoryCountingLineUoM (ComplexType)

OpenType: true

## Properties

- DocumentEntry : Edm.Int32
- LineNumber : Edm.Int32
- ChildNumber : Edm.Int32
- UoMCountedQuantity : Edm.Double
- ItemsPerUnit : Edm.Double
- CountedQuantity : Edm.Double
- UoMCode : Edm.String
- BarCode : Edm.String
- CounterType : SAPB1.CounterTypeEnum
- CounterID : Edm.Int32
- MultipleCounterRole : SAPB1.MultipleCounterRoleEnum

# SAPB1.InventoryCountingParams (ComplexType)

## Properties

- DocumentEntry : Edm.Int32
- DocumentNumber : Edm.Int32

# SAPB1.InventoryCountingSerialNumber (ComplexType)

## Properties

- ManufacturerSerialNumber : Edm.String
- InternalSerialNumber : Edm.String
- ExpiryDate : Edm.DateTimeOffset
- ManufactureDate : Edm.DateTimeOffset
- ReceptionDate : Edm.DateTimeOffset
- WarrantyStart : Edm.DateTimeOffset
- WarrantyEnd : Edm.DateTimeOffset
- Location : Edm.String
- Notes : Edm.String
- BatchID : Edm.String
- SystemSerialNumber : Edm.Int32
- BaseLineNumber : Edm.Int32
- Quantity : Edm.Double
- DocumentEntry : Edm.Int32
- CounterType : SAPB1.CounterTypeEnum
- CounterID : Edm.Int32
- MultipleCounterRole : SAPB1.MultipleCounterRoleEnum
- TrackingNote : Edm.Int32
- TrackingNoteLine : Edm.Int32
- ItemCode : Edm.String

# SAPB1.InventoryCycles (EntityType)

OpenType: true
Key: CycleCode

## Properties

- CycleCode : Edm.Int32 [required]
- CycleName : Edm.String
- Frequency : SAPB1.BoFrequency
- Day : Edm.Int32
- Hour : Edm.TimeOfDay
- NextCountingDate : Edm.DateTimeOffset
- Interval : Edm.Int32
- Sunday : SAPB1.BoYesNoEnum
- Monday : SAPB1.BoYesNoEnum
- Tuesday : SAPB1.BoYesNoEnum
- Wednesday : SAPB1.BoYesNoEnum
- Thursday : SAPB1.BoYesNoEnum
- Friday : SAPB1.BoYesNoEnum
- Saturday : SAPB1.BoYesNoEnum
- RepeatOption : SAPB1.RepeatOptionEnum
- RecurrenceSequenceSpecifier : SAPB1.RecurrenceSequenceEnum
- RecurrenceDayInMonth : Edm.Int32
- RecurrenceMonth : Edm.Int32
- RecurrenceDayOfWeek : SAPB1.RecurrenceDayOfWeekEnum
- endType : SAPB1.EndTypeEnum
- MaxOccurrence : Edm.Int32
- SeriesEndDate : Edm.DateTimeOffset

## Navigation properties

- Items : Collection(SAPB1.Item) [Partner=InventoryCycles]
- ItemGroups : Collection(SAPB1.ItemGroups) [Partner=InventoryCycles]

# SAPB1.InventoryCyclesParams (ComplexType)

## Properties

- CycleCode : Edm.Int32

# SAPB1.InventoryOpeningBalance (EntityType)

OpenType: true
Key: DocumentEntry

## Properties

- DocumentEntry : Edm.Int32 [required]
- PostingDate : Edm.DateTimeOffset
- DocumentDate : Edm.DateTimeOffset
- DocumentNumber : Edm.Int32
- Series : Edm.Int32
- Reference2 : Edm.String
- Remarks : Edm.String
- BranchID : Edm.Int32
- PriceSource : SAPB1.InventoryOpeningBalancePriceSourceEnum
- PriceList : Edm.Int32
- JournalRemark : Edm.String
- DocObjectCodeEx : Edm.String
- PeriodIndicator : Edm.String
- FinancialPeriod : Edm.Int32
- AttachmentEntry : Edm.Int32
- InventoryOpeningBalanceLines : Collection(SAPB1.InventoryOpeningBalanceLine)

## Navigation properties

- BusinessPlace : SAPB1.BusinessPlace [Partner=InventoryOpeningBalances]
- Attachments2 : SAPB1.Attachments2 [Partner=InventoryOpeningBalances]

# SAPB1.InventoryOpeningBalanceBatchNumber (ComplexType)

## Properties

- DocumentEntry : Edm.Int32
- BatchNumber : Edm.String
- ManufacturerSerialNumber : Edm.String
- InternalSerialNumber : Edm.String
- ExpiryDate : Edm.DateTimeOffset
- ManufactureDate : Edm.DateTimeOffset
- AddmisionDate : Edm.DateTimeOffset
- Location : Edm.String
- Notes : Edm.String
- Quantity : Edm.Double
- BaseLineNumber : Edm.Int32
- TrackingNote : Edm.Int32
- TrackingNoteLine : Edm.Int32
- ItemCode : Edm.String
- SystemSerialNumber : Edm.Int32

# SAPB1.InventoryOpeningBalanceCCDNumber (ComplexType)

## Properties

- TrackingNote : Edm.Int32
- TrackingNoteLine : Edm.Int32
- CCDNumber : Edm.String
- Quantity : Edm.Double
- CountryOfOrigin : Edm.String
- SubLineNumber : Edm.Int32
- DocumentEntry : Edm.Int32
- BaseLineNumber : Edm.Int32
- ChildNumber : Edm.Int32

# SAPB1.InventoryOpeningBalanceDraft (EntityType)

OpenType: true
Key: DocumentEntry

## Properties

- DocumentEntry : Edm.Int32 [required]
- DocumentNumber : Edm.Int32
- Series : Edm.Int32

# SAPB1.InventoryOpeningBalanceDraftParams (ComplexType)

## Properties

- DocumentEntry : Edm.Int32
- DocumentNumber : Edm.Int32

# SAPB1.InventoryOpeningBalanceLine (ComplexType)

OpenType: true

## Properties

- DocumentEntry : Edm.Int32
- LineNumber : Edm.Int32
- ItemCode : Edm.String
- ItemDescription : Edm.String
- WarehouseCode : Edm.String
- BinEntry : Edm.Int32
- InWarehouseQuantity : Edm.Double
- OpeningBalance : Edm.Double
- Remarks : Edm.String
- BarCode : Edm.String
- VisualOrder : Edm.Int32
- Price : Edm.Double
- Total : Edm.Double
- OpenInventoryAccount : Edm.String
- ProjectCode : Edm.String
- Manufacturer : Edm.Int32
- SupplierCatalogNo : Edm.String
- CostingCode : Edm.String
- CostingCode2 : Edm.String
- CostingCode3 : Edm.String
- CostingCode4 : Edm.String
- CostingCode5 : Edm.String
- PreferredVendor : Edm.String
- Currency : Edm.String
- AllowBinNegativeQuantity : SAPB1.BoYesNoEnum
- ActualPrice : Edm.Double
- PostedValueLC : Edm.Double
- PostedValueSC : Edm.Double
- WeightOfRecycledPlastic : Edm.Double
- PlasticPackageExemptionReason : Edm.String
- InventoryOpeningBalanceSerialNumbers : Collection(SAPB1.InventoryOpeningBalanceSerialNumber)
- InventoryOpeningBalanceBatchNumbers : Collection(SAPB1.InventoryOpeningBalanceBatchNumber)
- InventoryOpeningBalanceCCDNumbers : Collection(SAPB1.InventoryOpeningBalanceCCDNumber)

# SAPB1.InventoryOpeningBalanceParams (ComplexType)

## Properties

- DocumentEntry : Edm.Int32
- DocumentNumber : Edm.Int32

# SAPB1.InventoryOpeningBalanceSerialNumber (ComplexType)

## Properties

- DocumentEntry : Edm.Int32
- ManufacturerSerialNumber : Edm.String
- InternalSerialNumber : Edm.String
- ExpiryDate : Edm.DateTimeOffset
- ManufactureDate : Edm.DateTimeOffset
- ReceptionDate : Edm.DateTimeOffset
- WarrantyStart : Edm.DateTimeOffset
- WarrantyEnd : Edm.DateTimeOffset
- Location : Edm.String
- Notes : Edm.String
- BatchID : Edm.String
- SystemSerialNumber : Edm.Int32
- BaseLineNumber : Edm.Int32
- Quantity : Edm.Double
- TrackingNote : Edm.Int32
- TrackingNoteLine : Edm.Int32
- ItemCode : Edm.String

# SAPB1.InventoryPosting (EntityType)

OpenType: true
Key: DocumentEntry

## Properties

- DocumentEntry : Edm.Int32 [required]
- DocumentNumber : Edm.Int32
- Series : Edm.Int32
- PostingDate : Edm.DateTimeOffset
- CountDate : Edm.DateTimeOffset
- CountTime : Edm.TimeOfDay
- Remarks : Edm.String
- Reference2 : Edm.String
- BranchID : Edm.Int32
- PriceSource : SAPB1.InventoryPostingPriceSourceEnum
- PriceList : Edm.Int32
- JournalRemark : Edm.String
- DocObjectCodeEx : Edm.String
- FinancialPeriod : Edm.Int32
- PeriodIndicator : Edm.String
- AttachmentEntry : Edm.Int32
- YearEndDate : Edm.DateTimeOffset
- InventoryPostingLines : Collection(SAPB1.InventoryPostingLine)
- InventoryPostingDocumentReferencesCollection : Collection(SAPB1.InventoryPostingDocumentReferences)

## Navigation properties

- BusinessPlace : SAPB1.BusinessPlace [Partner=InventoryPostings]
- Attachments2 : SAPB1.Attachments2 [Partner=InventoryPostings]

# SAPB1.InventoryPostingBatchNumber (ComplexType)

## Properties

- DocumentEntry : Edm.Int32
- BatchNumber : Edm.String
- ManufacturerSerialNumber : Edm.String
- InternalSerialNumber : Edm.String
- ExpiryDate : Edm.DateTimeOffset
- ManufactureDate : Edm.DateTimeOffset
- AddmisionDate : Edm.DateTimeOffset
- Location : Edm.String
- Notes : Edm.String
- Quantity : Edm.Double
- BaseLineNumber : Edm.Int32
- TrackingNote : Edm.Int32
- TrackingNoteLine : Edm.Int32
- ItemCode : Edm.String
- SystemSerialNumber : Edm.Int32

# SAPB1.InventoryPostingCCDNumber (ComplexType)

## Properties

- TrackingNote : Edm.Int32
- TrackingNoteLine : Edm.Int32
- CCDNumber : Edm.String
- Quantity : Edm.Double
- CountryOfOrigin : Edm.String
- SubLineNumber : Edm.Int32
- DocumentEntry : Edm.Int32
- BaseLineNumber : Edm.Int32
- ChildNumber : Edm.Int32

# SAPB1.InventoryPostingCopyOption (ComplexType)

## Properties

- BaseEntry : Edm.Int32
- CopyOption : SAPB1.InventoryPostingCopyOptionEnum

# SAPB1.InventoryPostingDocumentReferences (ComplexType)

## Properties

- DocEntry : Edm.Int32
- LineNumber : Edm.Int32
- ReferencedDocEntry : Edm.Int32
- ReferencedDocNumber : Edm.Int32
- ExternalReferencedDocNumber : Edm.String
- ReferencedObjectType : SAPB1.ReferencedObjectTypeEnum
- IssueDate : Edm.DateTimeOffset
- Remark : Edm.String

# SAPB1.InventoryPostingDraft (EntityType)

OpenType: true
Key: DocumentEntry

## Properties

- DocumentEntry : Edm.Int32 [required]
- DocumentNumber : Edm.Int32
- Series : Edm.Int32
- PostingDate : Edm.DateTimeOffset
- CountDate : Edm.DateTimeOffset
- CountTime : Edm.TimeOfDay
- Comments : Edm.String
- Reference2 : Edm.String
- BranchID : Edm.Int32
- JournalRemark : Edm.String
- DocObjectCodeEx : Edm.String
- FinancialPeriod : Edm.Int32
- PeriodIndicator : Edm.String
- AttachmentEntry : Edm.Int32
- YearEndDate : Edm.DateTimeOffset

## Navigation properties

- BusinessPlace : SAPB1.BusinessPlace [Partner=InventoryPostingDrafts]
- Attachments2 : SAPB1.Attachments2 [Partner=InventoryPostingDrafts]

# SAPB1.InventoryPostingDraftParams (ComplexType)

## Properties

- DocumentEntry : Edm.Int32
- DocumentNumber : Edm.Int32

# SAPB1.InventoryPostingLine (ComplexType)

OpenType: true

## Properties

- DocumentEntry : Edm.Int32
- LineNumber : Edm.Int32
- ItemCode : Edm.String
- ItemDescription : Edm.String
- WarehouseCode : Edm.String
- BinEntry : Edm.Int32
- InWarehouseQuantity : Edm.Double
- BarCode : Edm.String
- Variance : Edm.Double
- VariancePercentage : Edm.Double
- CountedQuantity : Edm.Double
- Price : Edm.Double
- Currency : Edm.String
- Total : Edm.Double
- VisualOrder : Edm.Int32
- CountDate : Edm.DateTimeOffset
- CountTime : Edm.TimeOfDay
- BaseEntry : Edm.Int32
- BaseLine : Edm.Int32
- BaseType : Edm.Int32
- BaseReference : Edm.String
- Remarks : Edm.String
- InventoryOffsetIncreaseAccount : Edm.String
- InventoryOffsetDecreaseAccount : Edm.String
- ProjectCode : Edm.String
- Manufacturer : Edm.Int32
- SupplierCatalogNo : Edm.String
- PreferredVendor : Edm.String
- CostingCode : Edm.String
- CostingCode2 : Edm.String
- CostingCode3 : Edm.String
- CostingCode4 : Edm.String
- CostingCode5 : Edm.String
- UoMCode : Edm.String
- UoMCountedQuantity : Edm.Double
- ItemsPerUnit : Edm.Double
- AllowBinNegativeQuantity : SAPB1.BoYesNoEnum
- ActualPrice : Edm.Double
- PostedValueLC : Edm.Double
- PostedValueSC : Edm.Double
- InventoryPostingLineUoMs : Collection(SAPB1.InventoryPostingLineUoM)
- InventoryPostingSerialNumbers : Collection(SAPB1.InventoryPostingSerialNumber)
- InventoryPostingBatchNumbers : Collection(SAPB1.InventoryPostingBatchNumber)
- InventoryPostingCCDNumbers : Collection(SAPB1.InventoryPostingCCDNumber)

# SAPB1.InventoryPostingLineUoM (ComplexType)

OpenType: true

## Properties

- DocumentEntry : Edm.Int32
- LineNumber : Edm.Int32
- ChildNumber : Edm.Int32
- UoMCountedQuantity : Edm.Double
- ItemsPerUnit : Edm.Double
- CountedQuantity : Edm.Double
- UoMCode : Edm.String
- BarCode : Edm.String

# SAPB1.InventoryPostingParams (ComplexType)

## Properties

- DocumentEntry : Edm.Int32
- DocumentNumber : Edm.Int32

# SAPB1.InventoryPostingSerialNumber (ComplexType)

## Properties

- DocumentEntry : Edm.Int32
- ManufacturerSerialNumber : Edm.String
- InternalSerialNumber : Edm.String
- ExpiryDate : Edm.DateTimeOffset
- ManufactureDate : Edm.DateTimeOffset
- ReceptionDate : Edm.DateTimeOffset
- WarrantyStart : Edm.DateTimeOffset
- WarrantyEnd : Edm.DateTimeOffset
- Location : Edm.String
- Notes : Edm.String
- BatchID : Edm.String
- SystemSerialNumber : Edm.Int32
- BaseLineNumber : Edm.Int32
- Quantity : Edm.Double
- TrackingNote : Edm.Int32
- TrackingNoteLine : Edm.Int32
- ItemCode : Edm.String

# SAPB1.InvokeParams (ComplexType)

## Properties

- Value : Edm.String

# SAPB1.ISDCreditMemo (EntityType)

OpenType: true
Key: DocumentEntry

## Properties

- DocumentEntry : Edm.Int32 [required]
- DocumentNumber : Edm.Int32
- Series : Edm.Int32
- PostingDate : Edm.DateTimeOffset
- DocDate : Edm.DateTimeOffset
- DocumentStatus : SAPB1.ISDDocStatusEnum
- Revised : SAPB1.BoYesNoEnum
- OriginReferenceNumber : Edm.String
- OriginReferenceEntry : Edm.Int32
- OriginDocumentDate : Edm.DateTimeOffset
- TransactionNumber : Edm.Int32
- Remarks : Edm.String
- ObjectType : Edm.String
- SourceLocationCode : Edm.Int32
- SourceLocationName : Edm.String
- SourceLocationGSTIN : Edm.String
- TargetLocationCode : Edm.Int32
- TargetLocationName : Edm.String
- TargetLocationGSTIN : Edm.String
- ISDEntry : Edm.Int32
- DataSource : Edm.String
- UserSignature : Edm.Int32
- LogInstance : Edm.Int32
- UserSignature2 : Edm.Int32
- CreateDate : Edm.DateTimeOffset
- UpdateDate : Edm.DateTimeOffset
- JournalMemo : Edm.String
- HandWritten : Edm.String
- PeriodIndicator : Edm.String
- BPLId : Edm.Int32
- BPLName : Edm.String
- VATRegNum : Edm.String
- ISDCreditMemoLines : Collection(SAPB1.ISDCreditMemoLine)

## Navigation properties

- JournalEntry : SAPB1.JournalEntry [Partner=ISDCreditMemos]
- User : SAPB1.User [Partner=ISDCreditMemos]
- BusinessPlace : SAPB1.BusinessPlace [Partner=ISDCreditMemos]

# SAPB1.ISDCreditMemoLine (ComplexType)

OpenType: true

## Properties

- DocumentEntry : Edm.Int32
- LineNumber : Edm.Int32
- SourceDocumentType : SAPB1.ISDDocumentTypeEnum
- SourceDocumentNumber : Edm.Int32
- SourceDocumentEntry : Edm.Int32
- SourceGSTTaxType : SAPB1.ISDSTATypeEnum
- SourceTaxAccount : Edm.String
- TargetGSTTaxType : SAPB1.ISDSTATypeEnum
- TargetTaxAccount : Edm.String
- DistributeAmount : Edm.Double
- SourceDocumentSubtype : Edm.String
- ITCType : SAPB1.ISDITCTypeEnum

# SAPB1.ISDCreditMemoParams (ComplexType)

## Properties

- DocumentEntry : Edm.Int32
- DocumentNumber : Edm.Int32

# SAPB1.ISDDocument (EntityType)

OpenType: true
Key: DocumentEntry

## Properties

- DocumentEntry : Edm.Int32 [required]
- DocumentNumber : Edm.Int32
- SourceLocationCode : Edm.Int32
- SourceLocationName : Edm.String
- Series : Edm.Int32
- PostingDate : Edm.DateTimeOffset
- DocDate : Edm.DateTimeOffset
- DocumentStatus : SAPB1.ISDDocStatusEnum
- Revised : SAPB1.BoYesNoEnum
- OriginalReferenceNumber : Edm.String
- OriginalReferenceEntry : Edm.Int32
- OriginalDocumentDate : Edm.DateTimeOffset
- Remarks : Edm.String
- ObjectType : Edm.String
- DataSource : Edm.String
- UserSignature : Edm.Int32
- LogInstance : Edm.Int32
- UserSignature2 : Edm.Int32
- CreateDate : Edm.DateTimeOffset
- UpdateDate : Edm.DateTimeOffset
- HandWritten : Edm.String
- PeriodIndicator : Edm.String
- DistributePercent : Edm.Double
- BPLId : Edm.Int32
- BPLName : Edm.String
- VATRegNum : Edm.String
- SourceDocumentType : SAPB1.ISDDocumentTypeEnum
- DocNumFrom : Edm.Int32
- DocNumTo : Edm.Int32
- DocDateFrom : Edm.DateTimeOffset
- DocDateTo : Edm.DateTimeOffset
- DistributableLines : Collection(SAPB1.DistributableLine)
- DistributedLines : Collection(SAPB1.DistributedLine)
- AutoDistributionRuleLines : Collection(SAPB1.AutoDistributionRuleLine)

## Navigation properties

- User : SAPB1.User [Partner=ISDDocuments]
- BusinessPlace : SAPB1.BusinessPlace [Partner=ISDDocuments]

# SAPB1.ISDInvoice (EntityType)

OpenType: true
Key: DocumentEntry

## Properties

- DocumentEntry : Edm.Int32 [required]
- DocumentNumber : Edm.Int32
- Series : Edm.Int32
- PostingDate : Edm.DateTimeOffset
- DocDate : Edm.DateTimeOffset
- DocumentStatus : SAPB1.ISDDocStatusEnum
- Revised : SAPB1.BoYesNoEnum
- OriginReferenceNumber : Edm.String
- OriginReferenceEntry : Edm.Int32
- OriginDocumentDate : Edm.DateTimeOffset
- TransactionNumber : Edm.Int32
- Remarks : Edm.String
- ObjectType : Edm.String
- SourceLocationCode : Edm.Int32
- SourceLocationName : Edm.String
- SourceLocationGSTIN : Edm.String
- TargetLocationCode : Edm.Int32
- TargetLocationName : Edm.String
- TargetLocationGSTIN : Edm.String
- ISDEntry : Edm.Int32
- DataSource : Edm.String
- UserSignature : Edm.Int32
- LogInstance : Edm.Int32
- UserSignature2 : Edm.Int32
- CreateDate : Edm.DateTimeOffset
- UpdateDate : Edm.DateTimeOffset
- JournalMemo : Edm.String
- HandWritten : Edm.String
- PeriodIndicator : Edm.String
- BPLId : Edm.Int32
- BPLName : Edm.String
- VATRegNum : Edm.String
- ISDInvoiceLines : Collection(SAPB1.ISDInvoiceLine)

## Navigation properties

- JournalEntry : SAPB1.JournalEntry [Partner=ISDInvoices]
- User : SAPB1.User [Partner=ISDInvoices]
- BusinessPlace : SAPB1.BusinessPlace [Partner=ISDInvoices]

# SAPB1.ISDInvoiceLine (ComplexType)

OpenType: true

## Properties

- DocumentEntry : Edm.Int32
- LineNumber : Edm.Int32
- SourceDocumentType : SAPB1.ISDDocumentTypeEnum
- SourceDocumentNumber : Edm.Int32
- SourceDocumentEntry : Edm.Int32
- SourceGSTTaxType : SAPB1.ISDSTATypeEnum
- SourceTaxAccount : Edm.String
- TargetGSTTaxType : SAPB1.ISDSTATypeEnum
- TargetTaxAccount : Edm.String
- DistributeAmount : Edm.Double
- SourceDocumentSubtype : Edm.String
- ITCType : SAPB1.ISDITCTypeEnum

# SAPB1.ISDInvoiceParams (ComplexType)

## Properties

- DocumentEntry : Edm.Int32
- DocumentNumber : Edm.Int32

# SAPB1.ISDParams (ComplexType)

## Properties

- DocumentEntry : Edm.Int32
- DocumentNumber : Edm.Int32

# SAPB1.ISDRecipientCreditMemo (EntityType)

OpenType: true
Key: DocumentEntry

## Properties

- DocumentEntry : Edm.Int32 [required]
- DocumentNumber : Edm.Int32
- Series : Edm.Int32
- PostingDate : Edm.DateTimeOffset
- DocDate : Edm.DateTimeOffset
- DocumentStatus : SAPB1.ISDDocStatusEnum
- ReferenceNumber : Edm.String
- ReferenceEntry : Edm.Int32
- ReferenceDocumentDate : Edm.DateTimeOffset
- TransactionNumber : Edm.Int32
- Remarks : Edm.String
- ObjectType : Edm.String
- SourceLocationCode : Edm.Int32
- SourceLocationName : Edm.String
- SourceLocationGSTIN : Edm.String
- TargetLocationCode : Edm.Int32
- TargetLocationName : Edm.String
- TargetLocationGSTIN : Edm.String
- DataSource : Edm.String
- UserSignature : Edm.Int32
- LogInstance : Edm.Int32
- UserSignature2 : Edm.Int32
- CreateDate : Edm.DateTimeOffset
- UpdateDate : Edm.DateTimeOffset
- JournalMemo : Edm.String
- HandWritten : Edm.String
- PeriodIndicator : Edm.String
- BPLId : Edm.Int32
- BPLName : Edm.String
- VATRegNum : Edm.String
- ISDRecipientCreditMemoLines : Collection(SAPB1.ISDRecipientCreditMemoLine)

## Navigation properties

- JournalEntry : SAPB1.JournalEntry [Partner=ISDRecipientCreditMemos]
- User : SAPB1.User [Partner=ISDRecipientCreditMemos]
- BusinessPlace : SAPB1.BusinessPlace [Partner=ISDRecipientCreditMemos]

# SAPB1.ISDRecipientCreditMemoLine (ComplexType)

OpenType: true

## Properties

- DocumentEntry : Edm.Int32
- LineNumber : Edm.Int32
- GSTTaxType : SAPB1.ISDSTATypeEnum
- TaxAccount : Edm.String
- ReceivedAmount : Edm.Double
- EligibleAmount : Edm.Double

# SAPB1.ISDRecipientCreditMemoParams (ComplexType)

## Properties

- DocumentEntry : Edm.Int32
- DocumentNumber : Edm.Int32

# SAPB1.ISDRecipientInvoice (EntityType)

OpenType: true
Key: DocumentEntry

## Properties

- DocumentEntry : Edm.Int32 [required]
- DocumentNumber : Edm.Int32
- Series : Edm.Int32
- PostingDate : Edm.DateTimeOffset
- DocDate : Edm.DateTimeOffset
- DocumentStatus : SAPB1.ISDDocStatusEnum
- ReferenceNumber : Edm.String
- ReferenceEntry : Edm.Int32
- ReferenceDocumentDate : Edm.DateTimeOffset
- TransactionNumber : Edm.Int32
- Remarks : Edm.String
- ObjectType : Edm.String
- SourceLocationCode : Edm.Int32
- SourceLocationName : Edm.String
- SourceLocationGSTIN : Edm.String
- TargetLocationCode : Edm.Int32
- TargetLocationName : Edm.String
- TargetLocationGSTIN : Edm.String
- DataSource : Edm.String
- UserSignature : Edm.Int32
- LogInstance : Edm.Int32
- UserSignature2 : Edm.Int32
- CreateDate : Edm.DateTimeOffset
- UpdateDate : Edm.DateTimeOffset
- JournalMemo : Edm.String
- HandWritten : Edm.String
- PeriodIndicator : Edm.String
- BPLId : Edm.Int32
- BPLName : Edm.String
- VATRegNum : Edm.String
- ISDRecipientInvoiceLines : Collection(SAPB1.ISDRecipientInvoiceLine)

## Navigation properties

- JournalEntry : SAPB1.JournalEntry [Partner=ISDRecipientInvoices]
- User : SAPB1.User [Partner=ISDRecipientInvoices]
- BusinessPlace : SAPB1.BusinessPlace [Partner=ISDRecipientInvoices]

# SAPB1.ISDRecipientInvoiceLine (ComplexType)

OpenType: true

## Properties

- DocumentEntry : Edm.Int32
- LineNumber : Edm.Int32
- GSTTaxType : SAPB1.ISDSTATypeEnum
- TaxAccount : Edm.String
- ReceivedAmount : Edm.Double
- EligibleAmount : Edm.Double

# SAPB1.ISDRecipientInvoiceParams (ComplexType)

## Properties

- DocumentEntry : Edm.Int32
- DocumentNumber : Edm.Int32

# SAPB1.Item (EntityType)

OpenType: true
Key: ItemCode
Filtered properties: 24

## Properties

- ItemCode : Edm.String [required]
- ItemName : Edm.String
- ForeignName : Edm.String
- ItemsGroupCode : Edm.Int32
- CustomsGroupCode : Edm.Int32
- SalesVATGroup : Edm.String
- BarCode : Edm.String
- VatLiable : SAPB1.BoYesNoEnum
- PurchaseItem : SAPB1.BoYesNoEnum
- SalesItem : SAPB1.BoYesNoEnum
- InventoryItem : SAPB1.BoYesNoEnum
- IncomeAccount : Edm.String
- ExemptIncomeAccount : Edm.String
- ExpanseAccount : Edm.String
- Mainsupplier : Edm.String
- SupplierCatalogNo : Edm.String
- DesiredInventory : Edm.Double
- MinInventory : Edm.Double
- Picture : Edm.String
- User_Text : Edm.String
- SerialNum : Edm.String
- CommissionPercent : Edm.Double
- CommissionSum : Edm.Double
- CommissionGroup : Edm.Int32
- TreeType : SAPB1.BoItemTreeTypes
- AssetItem : SAPB1.BoYesNoEnum
- DataExportCode : Edm.String
- Manufacturer : Edm.Int32
- QuantityOnStock : Edm.Double
- QuantityOrderedFromVendors : Edm.Double
- QuantityOrderedByCustomers : Edm.Double
- ManageSerialNumbers : SAPB1.BoYesNoEnum
- ManageBatchNumbers : SAPB1.BoYesNoEnum
- Valid : SAPB1.BoYesNoEnum
- ValidFrom : Edm.DateTimeOffset
- ValidTo : Edm.DateTimeOffset
- ValidRemarks : Edm.String
- Frozen : SAPB1.BoYesNoEnum
- FrozenFrom : Edm.DateTimeOffset
- FrozenTo : Edm.DateTimeOffset
- FrozenRemarks : Edm.String
- SalesUnit : Edm.String
- SalesItemsPerUnit : Edm.Double
- SalesPackagingUnit : Edm.String
- SalesQtyPerPackUnit : Edm.Double
- SalesUnitLength : Edm.Double
- SalesLengthUnit : Edm.Int32
- SalesUnitWidth : Edm.Double
- SalesWidthUnit : Edm.Int32
- SalesUnitHeight : Edm.Double
- SalesHeightUnit : Edm.Int32
- SalesUnitVolume : Edm.Double
- SalesVolumeUnit : Edm.Int32
- SalesUnitWeight : Edm.Double
- SalesWeightUnit : Edm.Int32
- PurchaseUnit : Edm.String
- PurchaseItemsPerUnit : Edm.Double
- PurchasePackagingUnit : Edm.String
- PurchaseQtyPerPackUnit : Edm.Double
- PurchaseUnitLength : Edm.Double
- PurchaseLengthUnit : Edm.Int32
- PurchaseUnitWidth : Edm.Double
- PurchaseWidthUnit : Edm.Int32
- PurchaseUnitHeight : Edm.Double
- PurchaseHeightUnit : Edm.Int32
- PurchaseUnitVolume : Edm.Double
- PurchaseVolumeUnit : Edm.Int32
- PurchaseUnitWeight : Edm.Double
- PurchaseWeightUnit : Edm.Int32
- PurchaseVATGroup : Edm.String
- SalesFactor1 : Edm.Double
- SalesFactor2 : Edm.Double
- SalesFactor3 : Edm.Double
- SalesFactor4 : Edm.Double
- PurchaseFactor1 : Edm.Double
- PurchaseFactor2 : Edm.Double
- PurchaseFactor3 : Edm.Double
- PurchaseFactor4 : Edm.Double
- MovingAveragePrice : Edm.Double
- ForeignRevenuesAccount : Edm.String
- ECRevenuesAccount : Edm.String
- ForeignExpensesAccount : Edm.String
- ECExpensesAccount : Edm.String
- AvgStdPrice : Edm.Double
- DefaultWarehouse : Edm.String
- ShipType : Edm.Int32
- GLMethod : SAPB1.BoGLMethods
- TaxType : SAPB1.BoTaxTypes
- MaxInventory : Edm.Double
- ManageStockByWarehouse : SAPB1.BoYesNoEnum
- PurchaseHeightUnit1 : Edm.Int32
- PurchaseUnitHeight1 : Edm.Double
- PurchaseLengthUnit1 : Edm.Int32
- PurchaseUnitLength1 : Edm.Double
- PurchaseWeightUnit1 : Edm.Int32
- PurchaseUnitWeight1 : Edm.Double
- PurchaseWidthUnit1 : Edm.Int32
- PurchaseUnitWidth1 : Edm.Double
- SalesHeightUnit1 : Edm.Int32
- SalesUnitHeight1 : Edm.Double
- SalesLengthUnit1 : Edm.Int32
- SalesUnitLength1 : Edm.Double
- SalesWeightUnit1 : Edm.Int32
- SalesUnitWeight1 : Edm.Double
- SalesWidthUnit1 : Edm.Int32
- SalesUnitWidth1 : Edm.Double
- ForceSelectionOfSerialNumber : SAPB1.BoYesNoEnum
- ManageSerialNumbersOnReleaseOnly : SAPB1.BoYesNoEnum
- WTLiable : SAPB1.BoYesNoEnum
- CostAccountingMethod : SAPB1.BoInventorySystem
- SWW : Edm.String
- WarrantyTemplate : Edm.String
- IndirectTax : SAPB1.BoYesNoEnum
- ArTaxCode : Edm.String
- ApTaxCode : Edm.String
- BaseUnitName : Edm.String
- ItemCountryOrg : Edm.String
- IssueMethod : SAPB1.BoIssueMethod
- SRIAndBatchManageMethod : SAPB1.BoManageMethod
- IsPhantom : SAPB1.BoYesNoEnum
- InventoryUOM : Edm.String
- PlanningSystem : SAPB1.BoPlanningSystem
- ProcurementMethod : SAPB1.BoProcurementMethod
- ComponentWarehouse : SAPB1.BoMRPComponentWarehouse
- OrderIntervals : Edm.Int32
- OrderMultiple : Edm.Double
- LeadTime : Edm.Int32
- MinOrderQuantity : Edm.Double
- ItemType : SAPB1.ItemTypeEnum
- ItemClass : SAPB1.ItemClassEnum
- OutgoingServiceCode : Edm.Int32
- IncomingServiceCode : Edm.Int32
- ServiceGroup : Edm.Int32
- NCMCode : Edm.Int32
- MaterialType : SAPB1.BoMaterialTypes
- MaterialGroup : Edm.Int32
- ProductSource : Edm.String
- Properties1 : SAPB1.BoYesNoEnum
- Properties2 : SAPB1.BoYesNoEnum
- Properties3 : SAPB1.BoYesNoEnum
- Properties4 : SAPB1.BoYesNoEnum
- Properties5 : SAPB1.BoYesNoEnum
- Properties6 : SAPB1.BoYesNoEnum
- Properties7 : SAPB1.BoYesNoEnum
- Properties8 : SAPB1.BoYesNoEnum
- Properties9 : SAPB1.BoYesNoEnum
- Properties10 : SAPB1.BoYesNoEnum
- Properties11 : SAPB1.BoYesNoEnum
- Properties12 : SAPB1.BoYesNoEnum
- Properties13 : SAPB1.BoYesNoEnum
- Properties14 : SAPB1.BoYesNoEnum
- Properties15 : SAPB1.BoYesNoEnum
- Properties16 : SAPB1.BoYesNoEnum
- Properties17 : SAPB1.BoYesNoEnum
- Properties18 : SAPB1.BoYesNoEnum
- Properties19 : SAPB1.BoYesNoEnum
- Properties20 : SAPB1.BoYesNoEnum
- Properties21 : SAPB1.BoYesNoEnum
- Properties22 : SAPB1.BoYesNoEnum
- Properties23 : SAPB1.BoYesNoEnum
- Properties24 : SAPB1.BoYesNoEnum
- Properties25 : SAPB1.BoYesNoEnum
- Properties26 : SAPB1.BoYesNoEnum
- Properties27 : SAPB1.BoYesNoEnum
- Properties28 : SAPB1.BoYesNoEnum
- Properties29 : SAPB1.BoYesNoEnum
- Properties30 : SAPB1.BoYesNoEnum
- Properties31 : SAPB1.BoYesNoEnum
- Properties32 : SAPB1.BoYesNoEnum
- Properties33 : SAPB1.BoYesNoEnum
- Properties34 : SAPB1.BoYesNoEnum
- Properties35 : SAPB1.BoYesNoEnum
- Properties36 : SAPB1.BoYesNoEnum
- Properties37 : SAPB1.BoYesNoEnum
- Properties38 : SAPB1.BoYesNoEnum
- Properties39 : SAPB1.BoYesNoEnum
- Properties40 : SAPB1.BoYesNoEnum
- Properties41 : SAPB1.BoYesNoEnum
- Properties42 : SAPB1.BoYesNoEnum
- Properties43 : SAPB1.BoYesNoEnum
- Properties44 : SAPB1.BoYesNoEnum
- Properties45 : SAPB1.BoYesNoEnum
- Properties46 : SAPB1.BoYesNoEnum
- Properties47 : SAPB1.BoYesNoEnum
- Properties48 : SAPB1.BoYesNoEnum
- Properties49 : SAPB1.BoYesNoEnum
- Properties50 : SAPB1.BoYesNoEnum
- Properties51 : SAPB1.BoYesNoEnum
- Properties52 : SAPB1.BoYesNoEnum
- Properties53 : SAPB1.BoYesNoEnum
- Properties54 : SAPB1.BoYesNoEnum
- Properties55 : SAPB1.BoYesNoEnum
- Properties56 : SAPB1.BoYesNoEnum
- Properties57 : SAPB1.BoYesNoEnum
- Properties58 : SAPB1.BoYesNoEnum
- Properties59 : SAPB1.BoYesNoEnum
- Properties60 : SAPB1.BoYesNoEnum
- Properties61 : SAPB1.BoYesNoEnum
- Properties62 : SAPB1.BoYesNoEnum
- Properties63 : SAPB1.BoYesNoEnum
- Properties64 : SAPB1.BoYesNoEnum
- AutoCreateSerialNumbersOnRelease : SAPB1.BoYesNoEnum
- DNFEntry : Edm.Int32
- GTSItemSpec : Edm.String
- GTSItemTaxCategory : Edm.String
- FuelID : Edm.Int32
- BeverageTableCode : Edm.String
- BeverageGroupCode : Edm.String
- BeverageCommercialBrandCode : Edm.Int32
- Series : Edm.Int32
- ToleranceDays : Edm.Int32
- TypeOfAdvancedRules : SAPB1.TypeOfAdvancedRulesEnum
- IssuePrimarilyBy : SAPB1.IssuePrimarilyByEnum
- NoDiscounts : SAPB1.BoYesNoEnum
- AssetClass : Edm.String
- AssetGroup : Edm.String
- InventoryNumber : Edm.String
- Technician : Edm.Int32
- Employee : Edm.Int32
- Location : Edm.Int32
- AssetStatus : SAPB1.AssetStatusEnum
- CapitalizationDate : Edm.DateTimeOffset
- StatisticalAsset : SAPB1.BoYesNoEnum
- Cession : SAPB1.BoYesNoEnum
- DeactivateAfterUsefulLife : SAPB1.BoYesNoEnum
- ManageByQuantity : SAPB1.BoYesNoEnum
- UoMGroupEntry : Edm.Int32
- InventoryUoMEntry : Edm.Int32
- DefaultSalesUoMEntry : Edm.Int32
- DefaultPurchasingUoMEntry : Edm.Int32
- DepreciationGroup : Edm.String
- AssetSerialNumber : Edm.String
- InventoryWeight : Edm.Double
- InventoryWeightUnit : Edm.Int32
- InventoryWeight1 : Edm.Double
- InventoryWeightUnit1 : Edm.Int32
- DefaultCountingUnit : Edm.String
- CountingItemsPerUnit : Edm.Double
- DefaultCountingUoMEntry : Edm.Int32
- Excisable : SAPB1.BoYesNoEnum
- ChapterID : Edm.Int32
- ScsCode : Edm.String
- SpProdType : SAPB1.SpecialProductTypeEnum
- ProdStdCost : Edm.Double
- InCostRollup : SAPB1.BoYesNoEnum
- VirtualAssetItem : SAPB1.BoYesNoEnum
- EnforceAssetSerialNumbers : SAPB1.BoYesNoEnum
- AttachmentEntry : Edm.Int32
- LinkedResource : Edm.String
- UpdateDate : Edm.DateTimeOffset
- UpdateTime : Edm.TimeOfDay
- GSTRelevnt : SAPB1.BoYesNoEnum
- SACEntry : Edm.Int32
- GSTTaxCategory : SAPB1.GSTTaxCategoryEnum
- ServiceCategoryEntry : Edm.Int32
- CapitalGoodsOnHoldPercent : Edm.Double
- CapitalGoodsOnHoldLimit : Edm.Double
- AssessableValue : Edm.Double
- AssVal4WTR : Edm.Double
- SOIExcisable : SAPB1.SOIExcisableTypeEnum
- TNVED : Edm.String
- ImportedItem : SAPB1.BoYesNoEnum
- PricingUnit : Edm.Int32
- CreateDate : Edm.DateTimeOffset
- CreateTime : Edm.TimeOfDay
- NVECode : Edm.String
- CtrSealQty : Edm.Double
- CESTCode : Edm.Int32
- LegalText : Edm.String
- DataVersion : Edm.Int32
- CreateQRCodeFrom : Edm.String
- TraceableItem : SAPB1.BoYesNoEnum
- CommodityClassification : Edm.Int32
- WeightOfRecycledPlastic : Edm.Double
- PlasticPackageTaxCategory : Edm.String
- PlasticPackageExemptionReasonForPurchase : Edm.String
- PlasticPackageExemptionReasonForProduction : Edm.String
- SAFTProductType : SAPB1.SAFTProductTypeEnum
- SAFTProductTypeEx : Edm.String
- StandardItemIdentification : Edm.Int32
- ItemPrices : Collection(SAPB1.ItemPrice)
- ItemWarehouseInfoCollection : Collection(SAPB1.ItemWarehouseInfo)
- ItemPreferredVendors : Collection(SAPB1.ItemPreferredVendor)
- ItemLocalizationInfos : Collection(SAPB1.ItemLocalizationInfo)
- ItemProjects : Collection(SAPB1.ItemProject)
- ItemDistributionRules : Collection(SAPB1.ItemDistributionRule)
- ItemAttributeGroups : Collection(SAPB1.ItemAttributeGroups)
- ItemDepreciationParameters : Collection(SAPB1.ItemDepreciationParameter)
- ItemPeriodControls : Collection(SAPB1.ItemPeriodControl)
- ItemUnitOfMeasurementCollection : Collection(SAPB1.ItemUnitOfMeasurement)
- ItemBarCodeCollection : Collection(SAPB1.ItemBarCode)
- ItemIntrastatExtension : SAPB1.ItemIntrastatExtension

## Navigation properties

- BatchNumberDetails : Collection(SAPB1.BatchNumberDetail) [Partner=Item]
- SerialNumberDetails : Collection(SAPB1.SerialNumberDetail) [Partner=Item]
- BinLocations : Collection(SAPB1.BinLocation) [Partner=Item]
- DepreciationAreas : Collection(SAPB1.DepreciationArea) [Partner=Item]
- GLAccountAdvancedRules : Collection(SAPB1.GLAccountAdvancedRule) [Partner=Item]
- BarCodes : Collection(SAPB1.BarCode) [Partner=Item]
- CustomerEquipmentCards : Collection(SAPB1.CustomerEquipmentCard) [Partner=Item]
- KnowledgeBaseSolutions : Collection(SAPB1.KnowledgeBaseSolution) [Partner=Item]
- ServiceCalls : Collection(SAPB1.ServiceCall) [Partner=Item]
- Resources : Collection(SAPB1.Resource) [Partner=Item]
- StockTakings : Collection(SAPB1.StockTaking) [Partner=Item]
- ItemGroups : SAPB1.ItemGroups [Partner=Items]
- CustomsGroup : SAPB1.CustomsGroup [Partner=Items]
- VatGroup : SAPB1.VatGroup [Partner=Items]
- ChartOfAccount : SAPB1.ChartOfAccount [Partner=Items]
- BusinessPartner : SAPB1.BusinessPartner [Partner=Items]
- CommissionGroup2 : SAPB1.CommissionGroup [Partner=Items]
- Manufacturer2 : SAPB1.Manufacturer [Partner=Items]
- ShippingType : SAPB1.ShippingType [Partner=Items]
- ContractTemplate : SAPB1.ContractTemplate [Partner=Items]
- SalesTaxCode : SAPB1.SalesTaxCode [Partner=Items]
- InventoryCycles : SAPB1.InventoryCycles [Partner=Items]
- ServiceGroup2 : SAPB1.ServiceGroup [Partner=Items]
- NCMCodeSetup : SAPB1.NCMCodeSetup [Partner=Items]
- MaterialGroup2 : SAPB1.MaterialGroup [Partner=Items]
- DNFCodeSetup : SAPB1.DNFCodeSetup [Partner=Items]
- BrazilFuelIndexer : SAPB1.BrazilFuelIndexer [Partner=Items]
- BrazilStringIndexer : SAPB1.BrazilStringIndexer [Partner=Items]
- BrazilNumericIndexer : SAPB1.BrazilNumericIndexer [Partner=Items]
- AssetClass2 : SAPB1.AssetClass [Partner=Items]
- AssetGroup2 : SAPB1.AssetGroup [Partner=Items]
- EmployeeInfo : SAPB1.EmployeeInfo [Partner=Items]
- WarehouseLocation : SAPB1.WarehouseLocation [Partner=Items]
- UnitOfMeasurementGroup : SAPB1.UnitOfMeasurementGroup [Partner=Items]
- UnitOfMeasurement : SAPB1.UnitOfMeasurement [Partner=Items]
- AssetDepreciationGroup : SAPB1.AssetDepreciationGroup [Partner=Items]
- IndiaHsn : SAPB1.IndiaHsn [Partner=Items]
- Resource : SAPB1.Resource [Partner=Items]
- IndiaSacCode : SAPB1.IndiaSacCode [Partner=Items]
- CESTCodeData : SAPB1.CESTCodeData [Partner=Items]
- IdentificationCode : SAPB1.IdentificationCode [Partner=Items]
- ProductTrees : Collection(SAPB1.ProductTree) [Partner=Item]
- SpecialPrices : Collection(SAPB1.SpecialPrice) [Partner=Item]
- AlternateCatNum : Collection(SAPB1.AlternateCatNum) [Partner=Item]

# SAPB1.ItemAttributeGroups (ComplexType)

## Properties

- Attribute1 : Edm.String
- Attribute2 : Edm.String
- Attribute3 : Edm.String
- Attribute4 : Edm.String
- Attribute5 : Edm.String
- Attribute6 : Edm.String
- Attribute7 : Edm.String
- Attribute8 : Edm.String
- Attribute9 : Edm.String
- Attribute10 : Edm.String
- Attribute11 : Edm.String
- Attribute12 : Edm.String
- Attribute13 : Edm.String
- Attribute14 : Edm.String
- Attribute15 : Edm.String
- Attribute16 : Edm.String
- Attribute17 : Edm.String
- Attribute18 : Edm.String
- Attribute19 : Edm.String
- Attribute20 : Edm.String
- Attribute21 : Edm.String
- Attribute22 : Edm.String
- Attribute23 : Edm.String
- Attribute24 : Edm.String
- Attribute25 : Edm.String
- Attribute26 : Edm.String
- Attribute27 : Edm.String
- Attribute28 : Edm.String
- Attribute29 : Edm.String
- Attribute30 : Edm.String
- Attribute31 : Edm.String
- Attribute32 : Edm.String
- Attribute33 : Edm.Int32
- Attribute34 : Edm.Int32
- Attribute35 : Edm.Int32
- Attribute36 : Edm.Int32
- Attribute37 : Edm.Int32
- Attribute38 : Edm.Int32
- Attribute39 : Edm.Int32
- Attribute40 : Edm.Int32
- Attribute41 : Edm.Int32
- Attribute42 : Edm.Int32
- Attribute43 : Edm.DateTimeOffset
- Attribute44 : Edm.DateTimeOffset
- Attribute45 : Edm.DateTimeOffset
- Attribute46 : Edm.DateTimeOffset
- Attribute47 : Edm.DateTimeOffset
- Attribute48 : Edm.Double
- Attribute49 : Edm.Double
- Attribute50 : Edm.Double
- Attribute51 : Edm.Double
- Attribute52 : Edm.Double
- Attribute53 : Edm.Double
- Attribute54 : Edm.Double
- Attribute55 : Edm.Double
- Attribute56 : Edm.Double
- Attribute57 : Edm.Double
- Attribute58 : Edm.Double
- Attribute59 : Edm.Double
- Attribute60 : Edm.Double
- Attribute61 : Edm.Double
- Attribute62 : Edm.Double
- Attribute63 : Edm.Double
- Attribute64 : Edm.Double

# SAPB1.ItemBarCode (ComplexType)

OpenType: true

## Properties

- AbsEntry : Edm.Int32
- UoMEntry : Edm.Int32
- Barcode : Edm.String
- FreeText : Edm.String

# SAPB1.ItemCycleCount (ComplexType)

OpenType: true

## Properties

- CycleCode : Edm.Int32
- Alert : SAPB1.BoYesNoEnum
- NextCountingDate : Edm.DateTimeOffset
- AlertTime : Edm.TimeOfDay
- DestinationUser : Edm.Int32
- WarehouseCode : Edm.String

# SAPB1.ItemDepreciationParameter (ComplexType)

## Properties

- FiscalYear : Edm.String
- DepreciationArea : Edm.String
- DepreciationStartDate : Edm.DateTimeOffset
- DepreciationEndDate : Edm.DateTimeOffset
- UsefulLife : Edm.Int32
- RemainingLife : Edm.Double
- DepreciationType : Edm.String
- TotalUnitsInUsefulLife : Edm.Int32
- RemainingUnits : Edm.Int32
- StandardUnits : Edm.Int32

# SAPB1.ItemDistributionRule (ComplexType)

## Properties

- LineNumber : Edm.Int32
- ValidFrom : Edm.DateTimeOffset
- ValidTo : Edm.DateTimeOffset
- DistributionRule : Edm.String
- DistributionRule2 : Edm.String
- DistributionRule3 : Edm.String
- DistributionRule4 : Edm.String
- DistributionRule5 : Edm.String

# SAPB1.ItemGroupParams (ComplexType)

## Properties

- Number : Edm.Int32

# SAPB1.ItemGroups (EntityType)

OpenType: true
Key: Number

## Properties

- PriceDifferencesAccount : Edm.String
- StockInflationAdjustAccount : Edm.String
- MinimumOrderQuantity : Edm.Double
- OrderInterval : Edm.Int32
- ExchangeRateDifferencesAccount : Edm.String
- IncreasingAccount : Edm.String
- StockInflationOffsetAccount : Edm.String
- ProcurementMethod : SAPB1.BoProcurementMethod
- ComponentWarehouse : SAPB1.BoMRPComponentWarehouse
- PurchaseOffsetAccount : Edm.String
- InventorySystem : SAPB1.BoInventorySystem
- WIPMaterialVarianceAccount : Edm.String
- PlanningSystem : SAPB1.BoPlanningSystem
- PurchaseAccount : Edm.String
- ReturningAccount : Edm.String
- CostInflationAccount : Edm.String
- ExpensesAccount : Edm.String
- RevenuesAccount : Edm.String
- TransfersAccount : Edm.String
- LeadTime : Edm.Int32
- OrderMultiple : Edm.Double
- CostInflationOffsetAccount : Edm.String
- InventoryAccount : Edm.String
- DecreaseGLAccount : Edm.String
- Number : Edm.Int32 [required]
- GoodsClearingAccount : Edm.String
- IncreaseGLAccount : Edm.String
- ForeignRevenuesAccount : Edm.String
- Alert : SAPB1.BoYesNoEnum
- WIPMaterialAccount : Edm.String
- ShippedGoodsAccount : Edm.String
- ExemptRevenuesAccount : Edm.String
- DecreasingAccount : Edm.String
- VATInRevenueAccount : Edm.String
- VarianceAccount : Edm.String
- EUExpensesAccount : Edm.String
- ForeignExpensesAccount : Edm.String
- CycleCode : Edm.Int32
- CostAccount : Edm.String
- EURevenuesAccount : Edm.String
- PAReturnAccount : Edm.String
- GroupName : Edm.String
- ExpenseClearingAct : Edm.String
- PurchaseCreditAcc : Edm.String
- EUPurchaseCreditAcc : Edm.String
- ForeignPurchaseCreditAcc : Edm.String
- SalesCreditAcc : Edm.String
- SalesCreditEUAcc : Edm.String
- ExemptedCredits : Edm.String
- SalesCreditForeignAcc : Edm.String
- ExpenseOffsetAccount : Edm.String
- NegativeInventoryAdjustmentAccount : Edm.String
- WHIncomingCenvatAccount : Edm.String
- WHOutgoingCenvatAccount : Edm.String
- StockInTransitAccount : Edm.String
- WipOffsetProfitAndLossAccount : Edm.String
- InventoryOffsetProfitAndLossAccount : Edm.String
- ToleranceDays : Edm.Int32
- DefaultUoMGroup : Edm.Int32
- DefaultInventoryUoM : Edm.Int32
- PurchaseBalanceAccount : Edm.String
- ItemClass : SAPB1.ItemClassEnum
- RawMaterial : SAPB1.BoYesNoEnum
- ItemGroupsWarehouseInfos : Collection(SAPB1.ItemGroupsWarehouseInfo)

## Navigation properties

- BinLocations : Collection(SAPB1.BinLocation) [Partner=ItemGroups]
- GLAccountAdvancedRules : Collection(SAPB1.GLAccountAdvancedRule) [Partner=ItemGroups]
- ServiceCalls : Collection(SAPB1.ServiceCall) [Partner=ItemGroups]
- Items : Collection(SAPB1.Item) [Partner=ItemGroups]
- ChartOfAccount : SAPB1.ChartOfAccount [Partner=ItemGroups]
- InventoryCycles : SAPB1.InventoryCycles [Partner=ItemGroups]
- UnitOfMeasurementGroup : SAPB1.UnitOfMeasurementGroup [Partner=ItemGroups]
- UnitOfMeasurement : SAPB1.UnitOfMeasurement [Partner=ItemGroups]

# SAPB1.ItemGroupsWarehouseInfo (ComplexType)

## Properties

- ItmsGrpCod : Edm.Int32
- WarehouseCode : Edm.String
- DefaultBin : Edm.Int32
- DefaultBinEnforced : SAPB1.BoYesNoEnum

# SAPB1.ItemImage (EntityType)

HasStream: true
Key: ItemCode

## Properties

- ItemCode : Edm.String [required]
- Picture : Edm.String [required]

# SAPB1.ItemIntrastatExtension (ComplexType)

## Properties

- ItemCode : Edm.String
- CommodityCode : Edm.Int32
- SupplementaryUnit : Edm.Int32
- FactorOfSupplementaryUnit : Edm.Double
- ImportRegionState : Edm.Int32
- ExportRegionState : Edm.Int32
- ImportNatureOfTransaction : Edm.Int32
- ExportNatureOfTransaction : Edm.Int32
- ImportStatisticalProcedure : Edm.Int32
- ExportStatisticalProcedure : Edm.Int32
- CountryOfOrigin : Edm.String
- ServiceCode : Edm.Int32
- Type : SAPB1.BoDocumentTypes
- ServiceSupplyMethod : SAPB1.BoServiceSupplyMethods
- ServicePaymentMethod : SAPB1.BoServicePaymentMethods
- ImportRegionCountry : Edm.String
- ExportRegionCountry : Edm.String
- UseWeightInCalculation : SAPB1.BoYesNoEnum
- IntrastatRelevant : SAPB1.BoYesNoEnum
- StatisticalCode : Edm.String

# SAPB1.ItemLocalizationInfo (ComplexType)

OpenType: true

## Properties

- ItemCode : Edm.String
- IncomeNature : Edm.String

# SAPB1.ItemParams (ComplexType)

## Properties

- ItemCode : Edm.String

# SAPB1.ItemPeriodControl (ComplexType)

## Properties

- FiscalYear : Edm.String
- DepreciationArea : Edm.String
- SubPeriod : Edm.Int32
- DepreciationStatus : SAPB1.BoYesNoEnum
- Factor : Edm.Double
- ActualUnits : Edm.Int32

# SAPB1.ItemPreferredVendor (ComplexType)

OpenType: true

## Properties

- BPCode : Edm.String

# SAPB1.ItemPrice (ComplexType)

OpenType: true

## Properties

- PriceList : Edm.Int32
- Price : Edm.Double
- Currency : Edm.String
- AdditionalPrice1 : Edm.Double
- AdditionalCurrency1 : Edm.String
- AdditionalPrice2 : Edm.Double
- AdditionalCurrency2 : Edm.String
- BasePriceList : Edm.Int32
- Factor : Edm.Double
- UoMPrices : Collection(SAPB1.UoMPrice)

# SAPB1.ItemPriceParams (ComplexType)

## Properties

- Date : Edm.DateTimeOffset
- UoMEntry : Edm.Int32
- BlanketAgreementNumber : Edm.Int32
- BlanketAgreementLine : Edm.Int32
- UoMQuantity : Edm.Double
- InventoryQuantity : Edm.Double
- Currency : Edm.String
- ItemCode : Edm.String
- CardCode : Edm.String
- PriceList : Edm.Int32

# SAPB1.ItemPriceReturnParams (ComplexType)

## Properties

- Price : Edm.Double
- Currency : Edm.String
- Discount : Edm.Double

# SAPB1.ItemProject (ComplexType)

## Properties

- LineNumber : Edm.Int32
- ValidFrom : Edm.DateTimeOffset
- ValidTo : Edm.DateTimeOffset
- Project : Edm.String

# SAPB1.ItemProperty (EntityType)

OpenType: true
Key: Number

## Properties

- Number : Edm.Int32 [required]
- PropertyName : Edm.String

# SAPB1.ItemPropertyParams (ComplexType)

## Properties

- Number : Edm.Int32

# SAPB1.ItemUnitOfMeasurement (ComplexType)

OpenType: true

## Properties

- UoMType : SAPB1.ItemUoMTypeEnum
- UoMEntry : Edm.Int32
- DefaultBarcode : Edm.Int32
- DefaultPackage : Edm.Int32
- Length1 : Edm.Double
- Length1Unit : Edm.Int32
- Length2 : Edm.Double
- Length2Unit : Edm.Int32
- Width1 : Edm.Double
- Width1Unit : Edm.Int32
- Width2 : Edm.Double
- Width2Unit : Edm.Int32
- Height1 : Edm.Double
- Height1Unit : Edm.Int32
- Height2 : Edm.Double
- Height2Unit : Edm.Int32
- Volume : Edm.Double
- VolumeUnit : Edm.Int32
- Weight1 : Edm.Double
- Weight1Unit : Edm.Int32
- Weight2 : Edm.Double
- Weight2Unit : Edm.Int32
- ItemUoMPackageCollection : Collection(SAPB1.ItemUoMPackage)

# SAPB1.ItemUoMPackage (ComplexType)

OpenType: true

## Properties

- UoMType : SAPB1.ItemUoMTypeEnum
- UoMEntry : Edm.Int32
- PackageTypeEntry : Edm.Int32
- Length1 : Edm.Double
- Length1Unit : Edm.Int32
- Length2 : Edm.Double
- Length2Unit : Edm.Int32
- Width1 : Edm.Double
- Width1Unit : Edm.Int32
- Width2 : Edm.Double
- Width2Unit : Edm.Int32
- Height1 : Edm.Double
- Height1Unit : Edm.Int32
- Height2 : Edm.Double
- Height2Unit : Edm.Int32
- Volume : Edm.Double
- VolumeUnit : Edm.Int32
- Weight1 : Edm.Double
- Weight1Unit : Edm.Int32
- Weight2 : Edm.Double
- Weight2Unit : Edm.Int32
- QuantityPerPackage : Edm.Double

# SAPB1.ItemWarehouseInfo (ComplexType)

OpenType: true

## Properties

- MinimalStock : Edm.Double
- MaximalStock : Edm.Double
- MinimalOrder : Edm.Double
- StandardAveragePrice : Edm.Double
- Locked : SAPB1.BoYesNoEnum
- InventoryAccount : Edm.String
- CostAccount : Edm.String
- TransferAccount : Edm.String
- RevenuesAccount : Edm.String
- VarienceAccount : Edm.String
- DecreasingAccount : Edm.String
- IncreasingAccount : Edm.String
- ReturningAccount : Edm.String
- ExpensesAccount : Edm.String
- EURevenuesAccount : Edm.String
- EUExpensesAccount : Edm.String
- ForeignRevenueAcc : Edm.String
- ForeignExpensAcc : Edm.String
- ExemptIncomeAcc : Edm.String
- PriceDifferenceAcc : Edm.String
- WarehouseCode : Edm.String
- InStock : Edm.Double
- Committed : Edm.Double
- Ordered : Edm.Double
- CountedQuantity : Edm.Double
- WasCounted : SAPB1.BoYesNoEnum
- UserSignature : Edm.Int32
- Counted : Edm.Double
- ExpenseClearingAct : Edm.String
- PurchaseCreditAcc : Edm.String
- EUPurchaseCreditAcc : Edm.String
- ForeignPurchaseCreditAcc : Edm.String
- SalesCreditAcc : Edm.String
- SalesCreditEUAcc : Edm.String
- ExemptedCredits : Edm.String
- SalesCreditForeignAcc : Edm.String
- ExpenseOffsettingAccount : Edm.String
- WipAccount : Edm.String
- ExchangeRateDifferencesAcct : Edm.String
- GoodsClearingAcct : Edm.String
- NegativeInventoryAdjustmentAccount : Edm.String
- CostInflationOffsetAccount : Edm.String
- GLDecreaseAcct : Edm.String
- GLIncreaseAcct : Edm.String
- PAReturnAcct : Edm.String
- PurchaseAcct : Edm.String
- PurchaseOffsetAcct : Edm.String
- ShippedGoodsAccount : Edm.String
- StockInflationOffsetAccount : Edm.String
- StockInflationAdjustAccount : Edm.String
- VATInRevenueAccount : Edm.String
- WipVarianceAccount : Edm.String
- CostInflationAccount : Edm.String
- WHIncomingCenvatAccount : Edm.String
- WHOutgoingCenvatAccount : Edm.String
- StockInTransitAccount : Edm.String
- WipOffsetProfitAndLossAccount : Edm.String
- InventoryOffsetProfitAndLossAccount : Edm.String
- DefaultBin : Edm.Int32
- DefaultBinEnforced : SAPB1.BoYesNoEnum
- PurchaseBalanceAccount : Edm.String
- ItemCode : Edm.String
- IndEscala : SAPB1.BoYesNoEnum
- CNJPMan : Edm.String
- ItemCycleCounts : Collection(SAPB1.ItemCycleCount)

# SAPB1.JournalEntry (EntityType)

OpenType: true
Key: JdtNum

## Properties

- ReferenceDate : Edm.DateTimeOffset
- Memo : Edm.String
- Reference : Edm.String
- Reference2 : Edm.String
- TransactionCode : Edm.String
- ProjectCode : Edm.String
- TaxDate : Edm.DateTimeOffset
- JdtNum : Edm.Int32 [required]
- Indicator : Edm.String
- UseAutoStorno : SAPB1.BoYesNoEnum
- StornoDate : Edm.DateTimeOffset
- VatDate : Edm.DateTimeOffset
- Series : Edm.Int32
- StampTax : SAPB1.BoYesNoEnum
- DueDate : Edm.DateTimeOffset
- AutoVAT : SAPB1.BoYesNoEnum
- Number : Edm.Int32
- FolioNumber : Edm.Int32
- FolioPrefixString : Edm.String
- ReportEU : SAPB1.BoYesNoEnum
- Report347 : SAPB1.BoYesNoEnum
- Printed : SAPB1.PrintStatusEnum
- LocationCode : Edm.Int32
- OriginalJournal : SAPB1.TransTypesEnum
- Original : Edm.Int32
- BaseReference : Edm.String
- BlockDunningLetter : SAPB1.BoYesNoEnum
- AutomaticWT : SAPB1.BoYesNoEnum
- WTSum : Edm.Double
- WTSumSC : Edm.Double
- WTSumFC : Edm.Double
- SignatureInputMessage : Edm.String
- SignatureDigest : Edm.String
- CertificationNumber : Edm.String
- PrivateKeyVersion : Edm.Int32
- Corisptivi : SAPB1.BoYesNoEnum
- Reference3 : Edm.String
- DocumentType : Edm.String
- DeferredTax : SAPB1.BoYesNoEnum
- BlanketAgreementNumber : Edm.Int32
- OperationCode : SAPB1.OperationCodeTypeEnum
- ResidenceNumberType : SAPB1.ResidenceNumberTypeEnum
- ECDPostingType : SAPB1.ECDPostingTypeEnum
- ExposedTransNumber : Edm.Int32
- PointOfIssueCode : Edm.String
- Letter : SAPB1.FolioLetterEnum
- FolioNumberFrom : Edm.Int32
- FolioNumberTo : Edm.Int32
- IsCostCenterTransfer : SAPB1.BoYesNoEnum
- ReportingSectionControlStatementVAT : Edm.String
- ExcludeFromTaxReportControlStatementVAT : SAPB1.BoYesNoEnum
- SAPPassport : Edm.String
- Cig : Edm.Int32
- Cup : Edm.Int32
- AdjustTransaction : SAPB1.BoYesNoEnum
- AttachmentEntry : Edm.Int32
- SAFTTransactionType : SAPB1.SAFTTransactionTypeEnum
- AllocationNumberIL : Edm.String
- SAFTTransactionTypeEx : Edm.String
- JournalEntryLines : Collection(SAPB1.JournalEntryLine)
- WithholdingTaxDataCollection : Collection(SAPB1.WithholdingTaxData)
- ElectronicProtocols : Collection(SAPB1.ElectronicProtocol)

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=JournalEntry]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=JournalEntry]
- Drafts : Collection(SAPB1.Document) [Partner=JournalEntry]
- StockTransferDrafts : Collection(SAPB1.StockTransfer) [Partner=JournalEntry]
- MaterialRevaluation : Collection(SAPB1.MaterialRevaluation) [Partner=JournalEntry]
- ProductionOrders : Collection(SAPB1.ProductionOrder) [Partner=JournalEntry]
- AssetRevaluations : Collection(SAPB1.AssetRevaluation) [Partner=JournalEntry]
- ISDRecipientInvoices : Collection(SAPB1.ISDRecipientInvoice) [Partner=JournalEntry]
- CreditNotes : Collection(SAPB1.Document) [Partner=JournalEntry]
- Invoices : Collection(SAPB1.Document) [Partner=JournalEntry]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=JournalEntry]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=JournalEntry]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=JournalEntry]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=JournalEntry]
- Returns : Collection(SAPB1.Document) [Partner=JournalEntry]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=JournalEntry]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=JournalEntry]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=JournalEntry]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=JournalEntry]
- BillOfExchangeTransactions : Collection(SAPB1.BillOfExchangeTransaction) [Partner=JournalEntry]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=JournalEntry]
- DownPayments : Collection(SAPB1.Document) [Partner=JournalEntry]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=JournalEntry]
- ReturnRequest : Collection(SAPB1.Document) [Partner=JournalEntry]
- TransactionCode2 : SAPB1.TransactionCode [Partner=JournalEntries]
- Project : SAPB1.Project [Partner=JournalEntries]
- FactoringIndicator : SAPB1.FactoringIndicator [Partner=JournalEntries]
- WarehouseLocation : SAPB1.WarehouseLocation [Partner=JournalEntries]
- JournalEntryDocumentType : SAPB1.JournalEntryDocumentType [Partner=JournalEntries]
- BlanketAgreement : SAPB1.BlanketAgreement [Partner=JournalEntries]
- CIGCode : SAPB1.CIGCode [Partner=JournalEntries]
- CUPCode : SAPB1.CUPCode [Partner=JournalEntries]
- Attachments2 : SAPB1.Attachments2 [Partner=JournalEntries]
- ISDInvoices : Collection(SAPB1.ISDInvoice) [Partner=JournalEntry]
- ISDCreditMemos : Collection(SAPB1.ISDCreditMemo) [Partner=JournalEntry]
- ISDRecipientCreditMemos : Collection(SAPB1.ISDRecipientCreditMemo) [Partner=JournalEntry]
- SelfInvoices : Collection(SAPB1.Document) [Partner=JournalEntry]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=JournalEntry]
- LandedCosts : Collection(SAPB1.LandedCost) [Partner=JournalEntry]
- ChecksforPayment : Collection(SAPB1.ChecksforPayment) [Partner=JournalEntry]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=JournalEntry]
- StockTransfers : Collection(SAPB1.StockTransfer) [Partner=JournalEntry]

# SAPB1.JournalEntryDocumentType (EntityType)

Key: JournalEntryType

## Properties

- JournalEntryType : Edm.String [required]
- DocTypeDescription : Edm.String
- ShortName : Edm.String

## Navigation properties

- JournalEntries : Collection(SAPB1.JournalEntry) [Partner=JournalEntryDocumentType]

# SAPB1.JournalEntryDocumentTypeParams (ComplexType)

## Properties

- JournalEntryType : Edm.String
- DocTypeDescription : Edm.String
- ShortName : Edm.String

# SAPB1.JournalEntryLine (ComplexType)

OpenType: true

## Properties

- Line_ID : Edm.Int32
- AccountCode : Edm.String
- Debit : Edm.Double
- Credit : Edm.Double
- FCDebit : Edm.Double
- FCCredit : Edm.Double
- FCCurrency : Edm.String
- DueDate : Edm.DateTimeOffset
- ShortName : Edm.String
- ContraAccount : Edm.String
- LineMemo : Edm.String
- ReferenceDate1 : Edm.DateTimeOffset
- ReferenceDate2 : Edm.DateTimeOffset
- Reference1 : Edm.String
- Reference2 : Edm.String
- ProjectCode : Edm.String
- CostingCode : Edm.String
- TaxDate : Edm.DateTimeOffset
- BaseSum : Edm.Double
- TaxGroup : Edm.String
- DebitSys : Edm.Double
- CreditSys : Edm.Double
- VatDate : Edm.DateTimeOffset
- VatLine : SAPB1.BoYesNoEnum
- SystemBaseAmount : Edm.Double
- VatAmount : Edm.Double
- SystemVatAmount : Edm.Double
- GrossValue : Edm.Double
- AdditionalReference : Edm.String
- CheckAbs : Edm.Int32
- CostingCode2 : Edm.String
- CostingCode3 : Edm.String
- CostingCode4 : Edm.String
- TaxCode : Edm.String
- TaxPostAccount : SAPB1.BoTaxPostAccEnum
- CostingCode5 : Edm.String
- LocationCode : Edm.Int32
- ControlAccount : Edm.String
- EqualizationTaxAmount : Edm.Double
- SystemEqualizationTaxAmount : Edm.Double
- TotalTax : Edm.Double
- SystemTotalTax : Edm.Double
- WTLiable : SAPB1.BoYesNoEnum
- WTRow : SAPB1.BoYesNoEnum
- PaymentBlock : SAPB1.BoYesNoEnum
- BlockReason : Edm.Int32
- FederalTaxID : Edm.String
- BPLID : Edm.Int32
- BPLName : Edm.String
- VATRegNum : Edm.String
- PaymentOrdered : SAPB1.BoYesNoEnum
- ExposedTransNumber : Edm.Int32
- DocumentArray : Edm.Int32
- DocumentLine : Edm.Int32
- CostElementCode : Edm.String
- Cig : Edm.Int32
- Cup : Edm.Int32
- IncomeClassificationCategory : Edm.Int32
- IncomeClassificationType : Edm.Int32
- ExpensesClassificationCategory : Edm.Int32
- ExpensesClassificationType : Edm.Int32
- VATClassificationCategory : Edm.Int32
- VATClassificationType : Edm.Int32
- VATExemptionCause : Edm.Int32
- LineAllocationNumber : Edm.String
- CashFlowAssignments : Collection(SAPB1.CashFlowAssignment)

# SAPB1.JournalEntryParams (ComplexType)

## Properties

- JdtNum : Edm.Int32

# SAPB1.KnowledgeBaseSolution (EntityType)

OpenType: true
Key: SolutionCode

## Properties

- ItemCode : Edm.String
- Status : Edm.Int32
- Owner : Edm.Int32
- CreatedBy : Edm.Int32
- CreationDate : Edm.DateTimeOffset
- LastUpdatedBy : Edm.Int32
- LastUpdateDate : Edm.DateTimeOffset
- Solution : Edm.String
- Symptom : Edm.String
- Cause : Edm.String
- Description : Edm.String
- SolutionCode : Edm.Int32 [required]
- AttachmentEntry : Edm.Int32

## Navigation properties

- Item : SAPB1.Item [Partner=KnowledgeBaseSolutions]
- ServiceCallSolutionStatus : SAPB1.ServiceCallSolutionStatus [Partner=KnowledgeBaseSolutions]
- User : SAPB1.User [Partner=KnowledgeBaseSolutions]

# SAPB1.KnowledgeBaseSolutionParams (ComplexType)

## Properties

- SolutionCode : Edm.Int32

# SAPB1.KPI (EntityType)

Key: KPICode

## Properties

- KPICode : Edm.String [required]
- KPIName : Edm.String
- KPIType : SAPB1.KPITypeEnum
- NumberOfColumns : Edm.Int32
- KPI_ItemLines : Collection(SAPB1.KPI_ItemLine)

# SAPB1.KPI_ItemLine (ComplexType)

## Properties

- KPICode : Edm.String
- KPILineNumber : Edm.Int32
- KPIName : Edm.String
- KPIValue1 : Edm.Double
- KPIValue2 : Edm.Double
- KPIValue3 : Edm.Double
- KPIValue4 : Edm.Double
- KPIValue5 : Edm.Double
- KPIValue6 : Edm.Double
- KPIValue7 : Edm.Double
- KPIValue8 : Edm.Double
- KPIValue9 : Edm.Double
- KPIValue10 : Edm.Double
- KPIValue11 : Edm.Double
- KPIValue12 : Edm.Double
- KPIValue13 : Edm.Double
- KPIValue14 : Edm.Double
- KPIValue15 : Edm.Double
- KPIValue16 : Edm.Double
- KPIValue17 : Edm.Double
- KPIValue18 : Edm.Double
- KPIValue19 : Edm.Double
- KPIValue20 : Edm.Double
- KPIValue21 : Edm.Double
- KPIValue22 : Edm.Double
- KPIValue23 : Edm.Double
- KPIValue24 : Edm.Double
- KPIValue25 : Edm.Double
- KPIValue26 : Edm.Double
- KPIValue27 : Edm.Double
- KPIValue28 : Edm.Double
- KPIValue29 : Edm.Double
- KPIValue30 : Edm.Double

# SAPB1.KPIParams (ComplexType)

## Properties

- KPICode : Edm.String
- KPIName : Edm.String

# SAPB1.LandedCost (EntityType)

OpenType: true
Key: DocEntry

## Properties

- DocEntry : Edm.Int32 [required]
- LandedCostNumber : Edm.Int32
- PostingDate : Edm.DateTimeOffset
- DueDate : Edm.DateTimeOffset
- VendorCode : Edm.String
- VendorName : Edm.String
- Broker : Edm.String
- BrokerName : Edm.String
- ClosedDocument : SAPB1.LandedCostDocStatusEnum
- FileNumber : Edm.String
- Remarks : Edm.String
- Reference : Edm.String
- DocumentCurrency : Edm.String
- DocumentRate : Edm.Double
- ProjectedCustoms : Edm.Double
- ActualCustoms : Edm.Double
- ActualCustomsFC : Edm.Double
- Tax1 : Edm.Double
- Tax2 : Edm.Double
- BeforeTax : Edm.Double
- Total : Edm.Double
- TotalFreightCharges : Edm.Double
- ProjectedCustomsFC : Edm.Double
- Tax1FC : Edm.Double
- Tax2FC : Edm.Double
- BeforeTaxFC : Edm.Double
- TotalFC : Edm.Double
- TotalFreightChargesFC : Edm.Double
- Series : Edm.Int32
- CustomsAffectsInventory : SAPB1.BoYesNoEnum
- AmountToBalance : Edm.Double
- AmountToBalanceFC : Edm.Double
- BillofLadingNumber : Edm.String
- TransportType : Edm.Int32
- TransactionNumber : Edm.Int32
- JournalRemarks : Edm.String
- AttachmentEntry : Edm.Int32
- LandedCost_ItemLines : Collection(SAPB1.LandedCost_ItemLine)
- LandedCost_CostLines : Collection(SAPB1.LandedCost_CostLine)

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=LandedCost]
- BusinessPartner : SAPB1.BusinessPartner [Partner=LandedCosts]
- ShippingType : SAPB1.ShippingType [Partner=LandedCosts]
- JournalEntry : SAPB1.JournalEntry [Partner=LandedCosts]

# SAPB1.LandedCost_CostLine (ComplexType)

OpenType: true

## Properties

- DocEntry : Edm.Int32
- LandedCostCode : Edm.String
- AllocationBy : SAPB1.LandedCostAllocationByEnum
- Amount : Edm.Double
- AmountFC : Edm.Double
- Factor : Edm.Double
- CostType : SAPB1.LCCostTypeEnum
- IncludeForCustoms : SAPB1.BoYesNoEnum
- OpenAmount : Edm.Double
- OpenAmountFC : Edm.Double
- Broker : Edm.String
- BrokerName : Edm.String
- CostCategory : SAPB1.LandedCostCostCategoryEnum

# SAPB1.LandedCost_ItemLine (ComplexType)

OpenType: true

## Properties

- DocEntry : Edm.Int32
- LineNumber : Edm.Int32
- BaseDocumentType : SAPB1.LandedCostBaseDocumentTypeEnum
- BaseEntry : Edm.Int32
- Number : Edm.String
- ItemDescription : Edm.String
- Quantity : Edm.Double
- BaseDocumentPrice : Edm.Double
- Rate : Edm.Double
- ProjectedCustoms : Edm.Double
- ProjectedCustomsFC : Edm.Double
- Expenditure : Edm.Double
- ExpenditureFC : Edm.Double
- WarehousePrice : Edm.Double
- WarehousePriceFC : Edm.Double
- LineTotal : Edm.Double
- LineTotalFC : Edm.Double
- Volume : Edm.Double
- VolumeUoM : Edm.Int32
- Weight1 : Edm.Double
- Weight1UnitCode : Edm.Int32
- Weight2 : Edm.Double
- Weight2UnitCode : Edm.Int32
- VendorCode : Edm.String
- Reference : Edm.String
- FactorWithoutCustoms : Edm.Double
- FactorWithCustoms : Edm.Double
- InventoryUoM : Edm.String
- BlockNumber : Edm.String
- ImportLog : Edm.String
- OriginalWarehouse : Edm.String
- Warehouse : Edm.String
- ReleaseNumber : Edm.Int32
- VariantCosts : Edm.Double
- FixCosts : Edm.Double
- VariantCostsFC : Edm.Double
- FixCostsFC : Edm.Double
- Customs : Edm.Double
- CustomsFC : Edm.Double
- BaseDocumentValueLineTotal : Edm.Double
- BaseDocumentValueLineTotalFC : Edm.Double
- AllocatedUnitCostsLineTotal : Edm.Double
- AllocatedUnitCostsLineTotalFC : Edm.Double
- CustomsValue : Edm.Double
- CustomsValueFC : Edm.Double
- TotalCosts : Edm.Double
- TotalCostsFC : Edm.Double
- TotalVolume : Edm.Double
- BaseLine : Edm.Int32
- TotalLineProjectedCustoms : Edm.Double
- AllocatedCostsLineTotal : Edm.Double
- FOBandIncludedCosts : Edm.Double
- FOBandIncludedCostsFC : Edm.Double
- Project : Edm.String
- DistributionRule : Edm.String
- DistributionRule2 : Edm.String
- DistributionRule3 : Edm.String
- DistributionRule4 : Edm.String
- DistributionRule5 : Edm.String
- PriceList : Edm.Int32
- AutomaticExpenditure : SAPB1.BoYesNoEnum
- InventoryValuation : SAPB1.BoYesNoEnum
- OriginLine : Edm.Int32
- Currency : Edm.String
- CustomsGroupRate : Edm.Double
- VatGroup : Edm.String
- VatPercent : Edm.Double
- ExciseSum : Edm.Double
- ExciseSumFC : Edm.Double
- ExciseAffectStock : SAPB1.BoYesNoEnum
- CustomsCost : Edm.Double
- CustomsCostFC : Edm.Double
- CustomsAffectStock : SAPB1.BoYesNoEnum
- CustomsVat : Edm.Double
- CustomsVatFC : Edm.Double
- CustomsVatAffectStock : SAPB1.BoYesNoEnum
- CCDNumber : Edm.String
- CorrectedBaseDocumentValue : Edm.Double
- CorrectedBaseDocumentValueFC : Edm.Double

# SAPB1.LandedCostParams (ComplexType)

## Properties

- DocEntry : Edm.Int32

# SAPB1.LandedCostsCode (EntityType)

OpenType: true
Key: Code

## Properties

- Code : Edm.String [required]
- Name : Edm.String
- AllocationBy : SAPB1.BoAllocationByEnum
- LandedCostsAllocationAccount : Edm.String

# SAPB1.LandedCostsCodeParams (ComplexType)

## Properties

- Code : Edm.String

# SAPB1.Layer (ComplexType)

## Properties

- TransactionSequenceNum : Edm.Int32
- LayerID : Edm.Int32
- DocNumber : Edm.String
- DocType : SAPB1.TransTypesEnum
- EntryDate : Edm.DateTimeOffset
- CurrentCost : Edm.Double
- OpenQty : Edm.Double

# SAPB1.LegalData (EntityType)

Key: DocEntry

## Properties

- DocEntry : Edm.Int32 [required]
- SourceObjectType : SAPB1.BoAPARDocumentTypes
- SourceObjectEntry : Edm.Int32
- DateOfPrinting : Edm.DateTimeOffset
- TimeOfPrinting : Edm.TimeOfDay
- PrinterBrand : Edm.String
- PrinterType : Edm.String
- PrinterModel : Edm.String
- PrinterFirmwareVersion : Edm.String
- PrinterDllVersion : Edm.String
- FiscalSeries : Edm.String
- FiscalNumber : Edm.String
- DocumentNumber : Edm.String
- FiscalUserID : Edm.Int32
- LegalDataDetailCollection : Collection(SAPB1.LegalDataDetail)

## Navigation properties

- User : SAPB1.User [Partner=LegalData]

# SAPB1.LegalDataDetail (ComplexType)

## Properties

- DocEntry : Edm.Int32
- LineSequence : Edm.Int32
- LineType : SAPB1.LegalDataLineTypeEnum
- TaxCode : Edm.String
- TaxRate : Edm.Double
- Amount : Edm.Double

# SAPB1.LegalDataParams (ComplexType)

## Properties

- DocEntry : Edm.Int32
- SourceObjectType : Edm.String
- SourceObjectEntry : Edm.Int32

# SAPB1.LengthMeasure (EntityType)

OpenType: true
Key: UnitCode

## Properties

- UnitCode : Edm.Int32 [required]
- UnitDisplay : Edm.String
- UnitName : Edm.String
- UnitCodeforQuantityDisplay : Edm.String
- UnitLengthinmm : Edm.Double

# SAPB1.LengthMeasureParams (ComplexType)

## Properties

- UnitCode : Edm.Int32

# SAPB1.LineExpenseTaxJurisdiction (ComplexType)

OpenType: true

## Properties

- JurisdictionCode : Edm.String
- JurisdictionType : Edm.Int32
- TaxAmount : Edm.Double
- TaxAmountSC : Edm.Double
- TaxAmountFC : Edm.Double
- TaxRate : Edm.Double
- DocEntry : Edm.Int32
- LineNumber : Edm.Int32
- RowSequence : Edm.Int32
- ExternalCalcTaxRate : Edm.Double
- ExternalCalcTaxAmount : Edm.Double
- ExternalCalcTaxAmountFC : Edm.Double
- ExternalCalcTaxAmountSC : Edm.Double

# SAPB1.LineFreightEBooksDetail (ComplexType)

OpenType: true

## Properties

- IncomeClassificationType : Edm.Int32
- IncomeClassificationCategory : Edm.Int32
- ExpensesClassificationType : Edm.Int32
- ExpensesClassificationCategory : Edm.Int32
- NetValueLC : Edm.Double
- NetValueFC : Edm.Double
- NetValueSC : Edm.Double
- VatCategory : Edm.Int32
- WithheldPercentCategory : Edm.Int32
- WithheldAmountLC : Edm.Double
- WithheldAmountFC : Edm.Double
- WithheldAmountSC : Edm.Double
- VatClassificationType : Edm.Int32
- VatClassificationCategory : Edm.Int32
- VATExemptionCause : Edm.Int32

# SAPB1.LineTaxJurisdiction (ComplexType)

OpenType: true

## Properties

- JurisdictionCode : Edm.String
- JurisdictionType : Edm.Int32
- TaxAmount : Edm.Double
- TaxAmountSC : Edm.Double
- TaxAmountFC : Edm.Double
- TaxRate : Edm.Double
- DocEntry : Edm.Int32
- LineNumber : Edm.Int32
- RowSequence : Edm.Int32
- ExternalCalcTaxRate : Edm.Double
- ExternalCalcTaxAmount : Edm.Double
- ExternalCalcTaxAmountFC : Edm.Double
- ExternalCalcTaxAmountSC : Edm.Double
- BaseSum : Edm.Double
- TaxInPrice : SAPB1.BoYesNoEnum
- NonDeductiblePercent : Edm.Double
- TaxOnReserveInvoice : SAPB1.BoYesNoEnum
- Exempt : SAPB1.BoYesNoEnum
- Unencumbered : SAPB1.BoYesNoEnum

# SAPB1.LocalEra (EntityType)

OpenType: true
Key: Code

## Properties

- EraName : Edm.String
- StartDate : Edm.DateTimeOffset
- Code : Edm.String [required]

# SAPB1.LocalEraParams (ComplexType)

## Properties

- Code : Edm.String

# SAPB1.MailElectronicDocumentParam (ComplexType)

## Properties

- ProtocolCode : SAPB1.ElectronicDocProtocolCodeStrEnum
- GUID : Edm.String
- SenderUserId : Edm.Int32

# SAPB1.MailParam (ComplexType)

## Properties

- Subject : Edm.String
- Body : Edm.String
- SenderUserId : Edm.Int32
- AttachmentId : Edm.Int32
- EmailRecipients : Collection(SAPB1.EmailRecipient)

# SAPB1.Manufacturer (EntityType)

OpenType: true
Key: Code

## Properties

- Code : Edm.Int32 [required]
- ManufacturerName : Edm.String

## Navigation properties

- Items : Collection(SAPB1.Item) [Partner=Manufacturer2]

# SAPB1.ManufacturerParams (ComplexType)

## Properties

- Code : Edm.Int32

# SAPB1.MaterialGroup (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- MaterialGroupCode : Edm.String
- Description : Edm.String

## Navigation properties

- Items : Collection(SAPB1.Item) [Partner=MaterialGroup2]

# SAPB1.MaterialGroupParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- MaterialGroupCode : Edm.String

# SAPB1.MaterialRevaluation (EntityType)

OpenType: true
Key: DocEntry

## Properties

- DocNum : Edm.Int32
- DocDate : Edm.DateTimeOffset
- Reference1 : Edm.String
- Reference2 : Edm.String
- Comments : Edm.String
- JournalMemo : Edm.String
- DocTime : Edm.TimeOfDay
- Series : Edm.Int32
- TaxDate : Edm.DateTimeOffset
- DocEntry : Edm.Int32 [required]
- CreationDate : Edm.DateTimeOffset
- UpdateDate : Edm.DateTimeOffset
- TransNum : Edm.Int32
- RevalType : Edm.String
- RevaluationIncomeAccount : Edm.String
- RevaluationExpenseAccount : Edm.String
- DataSource : Edm.String
- UserSignature : Edm.Int32
- InflationRevaluation : SAPB1.BoYesNoEnum
- CardCode : Edm.String
- CardName : Edm.String
- MaterialRevaluationLines : Collection(SAPB1.MaterialRevaluationLine)
- MaterialRevaluationDocumentReferencesCollection : Collection(SAPB1.MaterialRevaluationDocumentReferences)

## Navigation properties

- JournalEntry : SAPB1.JournalEntry [Partner=MaterialRevaluation]
- User : SAPB1.User [Partner=MaterialRevaluation]
- BusinessPartner : SAPB1.BusinessPartner [Partner=MaterialRevaluation]

# SAPB1.MaterialRevaluationDocumentReferences (ComplexType)

## Properties

- DocEntry : Edm.Int32
- LineNumber : Edm.Int32
- ReferencedDocEntry : Edm.Int32
- ReferencedDocNumber : Edm.Int32
- ExternalReferencedDocNumber : Edm.String
- ReferencedObjectType : SAPB1.ReferencedObjectTypeEnum
- IssueDate : Edm.DateTimeOffset
- Remark : Edm.String

# SAPB1.MaterialRevaluationFIFO (ComplexType)

## Properties

- Layers : Collection(SAPB1.Layer)

# SAPB1.MaterialRevaluationFIFOParams (ComplexType)

## Properties

- ItemCode : Edm.String
- LocationType : Edm.String
- LocationCode : Edm.String
- ShowIssuedLayers : SAPB1.BoYesNoEnum

# SAPB1.MaterialRevaluationLine (ComplexType)

OpenType: true

## Properties

- LineNum : Edm.Int32
- ItemCode : Edm.String
- ItemDescription : Edm.String
- Quantity : Edm.Double
- Price : Edm.Double
- WarehouseCode : Edm.String
- ActualPrice : Edm.Double
- OnHand : Edm.Double
- DebitCredit : Edm.Double
- DocEntry : Edm.Int32
- RevaluationDecrementAccount : Edm.String
- RevaluationIncrementAccount : Edm.String
- RevalAmountToStock : Edm.Double
- Project : Edm.String
- DistributionRule : Edm.String
- DistributionRule2 : Edm.String
- DistributionRule3 : Edm.String
- DistributionRule4 : Edm.String
- DistributionRule5 : Edm.String
- FIFOLayers : Collection(SAPB1.FIFOLayer)
- SNBLinesCollection : Collection(SAPB1.SNBLines)

# SAPB1.MaterialRevaluationParams (ComplexType)

## Properties

- DocEntry : Edm.Int32

# SAPB1.MaterialRevaluationSNBParam (ComplexType)

## Properties

- ItemCode : Edm.String

# SAPB1.MaterialRevaluationSNBParams (ComplexType)

## Properties

- SnbAbsEntry : Edm.Int32
- NewCost : Edm.Double
- DebitCredit : Edm.Double
- SystemNumber : Edm.Int32
- LotNumber : Edm.String
- ManufactureNumber : Edm.String
- AdmissionDate : Edm.DateTimeOffset
- ExpirationDate : Edm.DateTimeOffset

# SAPB1.Message (EntityType)

Key: Code

## Properties

- Code : Edm.Int32 [required]
- User : Edm.Int32
- Priority : SAPB1.BoMsgPriorities
- Subject : Edm.String
- Text : Edm.String
- Attachment : Edm.Int32
- MessageDataColumns : Collection(SAPB1.MessageDataColumn)
- RecipientCollection : Collection(SAPB1.Recipient)

# SAPB1.MessageDataColumn (ComplexType)

## Properties

- ColumnName : Edm.String
- Link : SAPB1.BoYesNoEnum
- MessageDataLines : Collection(SAPB1.MessageDataLine)

# SAPB1.MessageDataLine (ComplexType)

## Properties

- Value : Edm.String
- Object : Edm.String
- ObjectKey : Edm.String

# SAPB1.MessageHeader (ComplexType)

## Properties

- Code : Edm.Int32
- Received : SAPB1.BoYesNoEnum
- Read : SAPB1.BoYesNoEnum
- ReceivedDate : Edm.DateTimeOffset
- ReceivedTime : Edm.TimeOfDay
- SentDate : Edm.DateTimeOffset
- SentTime : Edm.TimeOfDay

# SAPB1.MobileAddOnSetting (EntityType)

Key: Code

## Properties

- Code : Edm.String [required]
- Description : Edm.String
- Url : Edm.String
- Type : SAPB1.MobileAddonSettingTypeEnum
- Provider : Edm.String
- ViewStyle : SAPB1.ViewStyleTypeEnum
- LogonMethod : SAPB1.LogonMethodEnum
- Enable : SAPB1.BoYesNoEnum
- B1MobileApp : SAPB1.BoYesNoEnum
- B1SalesApp : SAPB1.BoYesNoEnum
- B1ServiceApp : SAPB1.BoYesNoEnum

# SAPB1.MobileAddOnSettingParams (ComplexType)

## Properties

- Code : Edm.String
- Description : Edm.String

# SAPB1.MobileServerDateTime (ComplexType)

## Properties

- Date : Edm.DateTimeOffset
- Time : Edm.TimeOfDay

# SAPB1.MultiLanguageTranslation (EntityType)

OpenType: true
Key: Numerator

## Properties

- Numerator : Edm.Int32 [required]
- TableName : Edm.String
- FieldAlias : Edm.String
- PrimaryKeyofobject : Edm.String
- TranslationsInUserLanguages : Collection(SAPB1.TranslationsInUserLanguage)

# SAPB1.MultiLanguageTranslationParams (ComplexType)

## Properties

- Numerator : Edm.Int32

# SAPB1.MultiplePayment (ComplexType)

## Properties

- BankStatmentLineID : Edm.Int32
- ListLineID : Edm.Int32
- DocumentIdentifier : Edm.String
- AmountLC : Edm.Double
- AmountFC : Edm.Double
- IsDebit : SAPB1.BoYesNoEnum

# SAPB1.NatureOfAssessee (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- Code : Edm.String
- Description : Edm.String
- AssesseeType : SAPB1.AssesseeTypeEnum

## Navigation properties

- WithholdingTaxCodes : Collection(SAPB1.WithholdingTaxCode) [Partner=NatureOfAssessee]

# SAPB1.NatureOfAssesseeParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- Code : Edm.String
- Description : Edm.String

# SAPB1.NCMCodeSetup (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- NCMCode : Edm.String
- Description : Edm.String
- GroupCode : Edm.String

## Navigation properties

- DNFCodeSetup : Collection(SAPB1.DNFCodeSetup) [Partner=NCMCodeSetup]
- Items : Collection(SAPB1.Item) [Partner=NCMCodeSetup]

# SAPB1.NCMCodeSetupParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- NCMCode : Edm.String
- Description : Edm.String

# SAPB1.NFModel (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.String [required]
- NFMName : Edm.String
- NFMDescription : Edm.String
- NFMCode : Edm.String

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=NFModel]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=NFModel]
- Drafts : Collection(SAPB1.Document) [Partner=NFModel]
- CreditNotes : Collection(SAPB1.Document) [Partner=NFModel]
- Invoices : Collection(SAPB1.Document) [Partner=NFModel]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=NFModel]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=NFModel]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=NFModel]
- Orders : Collection(SAPB1.Document) [Partner=NFModel]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=NFModel]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=NFModel]
- Returns : Collection(SAPB1.Document) [Partner=NFModel]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=NFModel]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=NFModel]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=NFModel]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=NFModel]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=NFModel]
- DownPayments : Collection(SAPB1.Document) [Partner=NFModel]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=NFModel]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=NFModel]
- ReturnRequest : Collection(SAPB1.Document) [Partner=NFModel]
- Quotations : Collection(SAPB1.Document) [Partner=NFModel]
- SelfInvoices : Collection(SAPB1.Document) [Partner=NFModel]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=NFModel]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=NFModel]
- FiscalPrinter : Collection(SAPB1.FiscalPrinter) [Partner=NFModel]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=NFModel]

# SAPB1.NFModelParams (ComplexType)

## Properties

- AbsEntry : Edm.String
- NFMName : Edm.String
- NFMDescription : Edm.String
- NFMCode : Edm.String

# SAPB1.NFTaxCategory (EntityType)

Key: AbsId

## Properties

- AbsId : Edm.Int32 [required]
- Code : Edm.String
- Locked : SAPB1.BoYesNoEnum
- GPCId : Edm.Int32
- CESTrel : SAPB1.BoYesNoEnum

## Navigation properties

- SalesTaxAuthoritiesTypes : Collection(SAPB1.SalesTaxAuthoritiesType) [Partner=NFTaxCategory]
- NotaFiscalCST : Collection(SAPB1.NotaFiscalCST) [Partner=NFTaxCategory]
- GovPayCode : SAPB1.GovPayCode [Partner=NFTaxCategories]

# SAPB1.NFTaxCategoryParams (ComplexType)

## Properties

- AbsId : Edm.Int32
- Code : Edm.String

# SAPB1.NotaFiscalCFOP (EntityType)

OpenType: true
Key: ID

## Properties

- ID : Edm.Int32 [required]
- Description : Edm.String
- Code : Edm.String
- Application : Edm.String

## Navigation properties

- SalesTaxCodes : Collection(SAPB1.SalesTaxCode) [Partner=NotaFiscalCFOP]
- NotaFiscalUsage : Collection(SAPB1.NotaFiscalUsage) [Partner=NotaFiscalCFOP]

# SAPB1.NotaFiscalCFOPParams (ComplexType)

## Properties

- ID : Edm.Int32

# SAPB1.NotaFiscalCST (EntityType)

OpenType: true
Key: ID

## Properties

- ID : Edm.Int32 [required]
- Code : Edm.String
- Situation : Edm.String
- TaxCategory : Edm.Int32
- CSTCodeOutgoing : Edm.String
- DescriptionOutgoing : Edm.String

## Navigation properties

- WithholdingTaxCodes : Collection(SAPB1.WithholdingTaxCode) [Partner=NotaFiscalCST]
- NFTaxCategory : SAPB1.NFTaxCategory [Partner=NotaFiscalCST]

# SAPB1.NotaFiscalCSTParams (ComplexType)

## Properties

- ID : Edm.Int32

# SAPB1.NotaFiscalUsage (EntityType)

OpenType: true
Key: ID

## Properties

- ID : Edm.Int32 [required]
- Usage : Edm.String
- IncomingInStateCFOPCode : Edm.String
- IncomingOutStateCFOPCode : Edm.String
- IncomingImportCFOPCode : Edm.String
- OutgoingInStateCFOPCode : Edm.String
- OutgoingOutStateCFOPCode : Edm.String
- OutgoingExportCFOPCode : Edm.String
- Description : Edm.String

## Navigation properties

- DepreciationAreas : Collection(SAPB1.DepreciationArea) [Partner=NotaFiscalUsage]
- GLAccountAdvancedRules : Collection(SAPB1.GLAccountAdvancedRule) [Partner=NotaFiscalUsage]
- NotaFiscalCFOP : SAPB1.NotaFiscalCFOP [Partner=NotaFiscalUsage]

# SAPB1.NotaFiscalUsageParams (ComplexType)

## Properties

- ID : Edm.Int32

# SAPB1.OccurenceCode (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- Code : Edm.String
- Description : Edm.String
- Note : Edm.String
- RequestedBoeStatus : SAPB1.BoBoeStatus
- IsMovement : SAPB1.BoYesNoEnum

# SAPB1.OccurenceCodeParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- Code : Edm.String
- Description : Edm.String
- Note : Edm.String
- RequestedBoeStatus : SAPB1.BoBoeStatus
- IsMovement : SAPB1.BoYesNoEnum

# SAPB1.OpenningBalanceAccount (ComplexType)

## Properties

- OpenBalanceAccount : Edm.String
- Date : Edm.DateTimeOffset
- Ref1 : Edm.String
- Ref2 : Edm.String
- Details : Edm.String
- BPLID : Edm.Int32

# SAPB1.OriginalItem (ComplexType)

## Properties

- ItemCode : Edm.String
- ItemName : Edm.String
- AlternativeItems : Collection(SAPB1.AlternativeItem)

# SAPB1.OriginalItemParams (ComplexType)

## Properties

- ItemCode : Edm.String
- ItemName : Edm.String

# SAPB1.PackagesType (EntityType)

OpenType: true
Key: Code

## Properties

- Type : Edm.String
- Code : Edm.Int32 [required]
- Length1 : Edm.Double
- Length1Unit : Edm.Int32
- Length2 : Edm.Double
- Length2Unit : Edm.Int32
- Width1 : Edm.Double
- Width1Unit : Edm.Int32
- Width2 : Edm.Double
- Width2Unit : Edm.Int32
- Height1 : Edm.Double
- Height1Unit : Edm.Int32
- Height2 : Edm.Double
- Height2Unit : Edm.Int32
- Volume : Edm.Double
- VolumeUnit : Edm.Int32
- Weight1 : Edm.Double
- Weight1Unit : Edm.Int32
- Weight2 : Edm.Double
- Weight2Unit : Edm.Int32

# SAPB1.PackagesTypeParams (ComplexType)

## Properties

- Code : Edm.Int32

# SAPB1.PartnersSetup (EntityType)

Key: PartnerID

## Properties

- PartnerID : Edm.Int32 [required]
- Name : Edm.String
- DefaultRelationship : Edm.Int32
- RelatedBP : Edm.String
- Details : Edm.String

## Navigation properties

- Relationship : SAPB1.Relationship [Partner=PartnersSetups]
- BusinessPartner : SAPB1.BusinessPartner [Partner=PartnersSetups]

# SAPB1.PartnersSetupParams (ComplexType)

## Properties

- PartnerID : Edm.Int32
- Name : Edm.String
- DefaultRelationship : Edm.Int32
- RelatedBP : Edm.String
- Details : Edm.String

# SAPB1.PathAdmin (ComplexType)

## Properties

- WordTemplateFolderPath : Edm.String
- PicturesFolderPath : Edm.String
- AttachmentsFolderPath : Edm.String
- ExtensionsFolderPath : Edm.String
- PrintId : Edm.String

# SAPB1.Payment (EntityType)

OpenType: true
Key: DocEntry
Filtered properties: 4

## Properties

- DocNum : Edm.Int32
- DocType : SAPB1.BoRcptTypes
- HandWritten : SAPB1.BoYesNoEnum
- Printed : SAPB1.BoYesNoEnum
- DocDate : Edm.DateTimeOffset
- CardCode : Edm.String
- CardName : Edm.String
- Address : Edm.String
- CashAccount : Edm.String
- DocCurrency : Edm.String
- CashSum : Edm.Double
- CheckAccount : Edm.String
- TransferAccount : Edm.String
- TransferSum : Edm.Double
- TransferDate : Edm.DateTimeOffset
- TransferReference : Edm.String
- LocalCurrency : SAPB1.BoYesNoEnum
- DocRate : Edm.Double
- Reference1 : Edm.String
- Reference2 : Edm.String
- CounterReference : Edm.String
- PaymentReferenceNo : Edm.String
- Remarks : Edm.String
- JournalRemarks : Edm.String
- SplitTransaction : SAPB1.BoYesNoEnum
- ContactPersonCode : Edm.Int32
- ApplyVAT : SAPB1.BoYesNoEnum
- TaxDate : Edm.DateTimeOffset
- Series : Edm.Int32
- BankCode : Edm.String
- BankAccount : Edm.String
- DiscountPercent : Edm.Double
- ProjectCode : Edm.String
- CurrencyIsLocal : SAPB1.BoYesNoEnum
- DeductionPercent : Edm.Double
- DeductionSum : Edm.Double
- CashSumFC : Edm.Double
- CashSumSys : Edm.Double
- BoeAccount : Edm.String
- BillOfExchangeAmount : Edm.Double
- BillofExchangeStatus : SAPB1.BoBoeStatus
- BillOfExchangeAmountFC : Edm.Double
- BillOfExchangeAmountSC : Edm.Double
- BillOfExchangeAgent : Edm.String
- WTCode : Edm.String
- WTAmount : Edm.Double
- WTAmountFC : Edm.Double
- WTAmountSC : Edm.Double
- WTAccount : Edm.String
- WTTaxableAmount : Edm.Double
- Proforma : SAPB1.BoYesNoEnum
- PayToBankCode : Edm.String
- PayToBankBranch : Edm.String
- PayToBankAccountNo : Edm.String
- PayToCode : Edm.String
- PayToBankCountry : Edm.String
- IsPayToBank : SAPB1.BoYesNoEnum
- DocEntry : Edm.Int32 [required]
- PaymentPriority : SAPB1.BoPaymentPriorities
- TaxGroup : Edm.String
- BankChargeAmount : Edm.Double
- BankChargeAmountInFC : Edm.Double
- BankChargeAmountInSC : Edm.Double
- UnderOverpaymentdifference : Edm.Double
- UnderOverpaymentdiffSC : Edm.Double
- WtBaseSum : Edm.Double
- WtBaseSumFC : Edm.Double
- WtBaseSumSC : Edm.Double
- VatDate : Edm.DateTimeOffset
- TransactionCode : Edm.String
- PaymentType : SAPB1.BoORCTPaymentTypeEnum
- TransferRealAmount : Edm.Double
- DocObjectCode : SAPB1.BoPaymentsObjectType
- DocTypte : SAPB1.BoRcptTypes
- DueDate : Edm.DateTimeOffset
- LocationCode : Edm.Int32
- Cancelled : SAPB1.BoYesNoEnum
- CancelStatus : SAPB1.CancelStatusEnum
- ControlAccount : Edm.String
- UnderOverpaymentdiffFC : Edm.Double
- AuthorizationStatus : SAPB1.PaymentsAuthorizationStatusEnum
- BPLID : Edm.Int32
- BPLName : Edm.String
- VATRegNum : Edm.String
- BlanketAgreement : Edm.Int32
- PaymentByWTCertif : SAPB1.BoYesNoEnum
- Cig : Edm.Int32
- Cup : Edm.Int32
- AttachmentEntry : Edm.Int32
- SignatureInputMessage : Edm.String
- SignatureDigest : Edm.String
- CertificationNumber : Edm.String
- PrivateKeyVersion : Edm.Int32
- EDocExportFormat : Edm.Int32
- ElecCommStatus : SAPB1.ElecCommStatusEnum
- ElecCommMessage : Edm.String
- SplitVendorCreditRow : SAPB1.BoYesNoEnum
- DigitalPayments : SAPB1.BoYesNoEnum
- AllocationNumberIL : Edm.String
- PaymentChecks : Collection(SAPB1.PaymentCheck)
- PaymentInvoices : Collection(SAPB1.PaymentInvoice)
- PaymentCreditCards : Collection(SAPB1.PaymentCreditCard)
- PaymentAccounts : Collection(SAPB1.PaymentAccount)
- PaymentDocumentReferencesCollection : Collection(SAPB1.PaymentDocumentReferences)
- BillOfExchange : SAPB1.BillOfExchange
- WithholdingTaxCertificatesCollection : Collection(SAPB1.WithholdingTaxCertificatesData)
- ElectronicProtocols : Collection(SAPB1.ElectronicProtocol)
- CashFlowAssignments : Collection(SAPB1.CashFlowAssignment)
- Payments_ApprovalRequests : Collection(SAPB1.Payments_ApprovalRequest)
- WithholdingTaxDataWTXCollection : Collection(SAPB1.WithholdingTaxDataWTX)

## Navigation properties

- BusinessPartner : SAPB1.BusinessPartner [Partner=IncomingPayments]
- ChartOfAccount : SAPB1.ChartOfAccount [Partner=IncomingPayments]
- Currency : SAPB1.Currency [Partner=IncomingPayments]
- Project : SAPB1.Project [Partner=IncomingPayments]
- WithholdingTaxCode : SAPB1.WithholdingTaxCode [Partner=IncomingPayments]
- Country : SAPB1.Country [Partner=IncomingPayments]
- VatGroup : SAPB1.VatGroup [Partner=IncomingPayments]
- TransactionCode2 : SAPB1.TransactionCode [Partner=IncomingPayments]
- WarehouseLocation : SAPB1.WarehouseLocation [Partner=IncomingPayments]
- BusinessPlace : SAPB1.BusinessPlace [Partner=IncomingPayments]
- BlanketAgreement2 : SAPB1.BlanketAgreement [Partner=IncomingPayments]
- CIGCode : SAPB1.CIGCode [Partner=IncomingPayments]
- CUPCode : SAPB1.CUPCode [Partner=IncomingPayments]
- Attachments2 : SAPB1.Attachments2 [Partner=IncomingPayments]

# SAPB1.PaymentAccount (ComplexType)

OpenType: true

## Properties

- LineNum : Edm.Int32
- AccountCode : Edm.String
- SumPaid : Edm.Double
- SumPaidFC : Edm.Double
- Decription : Edm.String
- VatGroup : Edm.String
- AccountName : Edm.String
- GrossAmount : Edm.Double
- ProfitCenter : Edm.String
- ProjectCode : Edm.String
- VatAmount : Edm.Double
- ProfitCenter2 : Edm.String
- ProfitCenter3 : Edm.String
- ProfitCenter4 : Edm.String
- ProfitCenter5 : Edm.String
- LocationCode : Edm.Int32
- EqualizationVatAmount : Edm.Double

# SAPB1.PaymentAmountParams (ComplexType)

## Properties

- DocType : SAPB1.PaymentInvoiceTypeEnum
- DocEntry : Edm.Int32
- InstallmentId : Edm.Int32
- CashDiscountPercentage : Edm.Double
- CashDiscountAmount : Edm.Double
- CashDiscountAmountFC : Edm.Double
- CashDiscountAmountSC : Edm.Double
- TotalPaymentAmount : Edm.Double
- TotalPaymentAmountFC : Edm.Double
- TotalPaymentAmountSC : Edm.Double

# SAPB1.PaymentBlock (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- PaymentBlockCode : Edm.String

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- Drafts : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- CreditNotes : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- Invoices : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- Orders : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- Returns : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=PaymentBlock2]
- DownPayments : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- ReturnRequest : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- Quotations : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- SelfInvoices : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=PaymentBlock2]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=PaymentBlock2]

# SAPB1.PaymentBlockParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- PaymentBlockCode : Edm.String

# SAPB1.PaymentBPCode (ComplexType)

## Properties

- BPCode : Edm.String
- Date : Edm.DateTimeOffset

# SAPB1.PaymentCheck (ComplexType)

OpenType: true

## Properties

- LineNum : Edm.Int32
- DueDate : Edm.DateTimeOffset
- CheckNumber : Edm.Int32
- BankCode : Edm.String
- Branch : Edm.String
- AccounttNum : Edm.String
- Details : Edm.String
- Trnsfrable : SAPB1.BoYesNoEnum
- CheckSum : Edm.Double
- Currency : Edm.String
- CountryCode : Edm.String
- CheckAbsEntry : Edm.Int32
- CheckAccount : Edm.String
- ManualCheck : SAPB1.BoYesNoEnum
- FiscalID : Edm.String
- OriginallyIssuedBy : Edm.String
- Endorse : SAPB1.BoYesNoEnum
- EndorsableCheckNo : Edm.Int32
- ECheck : SAPB1.BoYesNoEnum

# SAPB1.PaymentCreditCard (ComplexType)

OpenType: true

## Properties

- LineNum : Edm.Int32
- CreditCard : Edm.Int32
- CreditAcct : Edm.String
- CreditCardNumber : Edm.String
- CardValidUntil : Edm.DateTimeOffset
- VoucherNum : Edm.String
- OwnerIdNum : Edm.String
- OwnerPhone : Edm.String
- PaymentMethodCode : Edm.Int32
- NumOfPayments : Edm.Int32
- FirstPaymentDue : Edm.DateTimeOffset
- FirstPaymentSum : Edm.Double
- AdditionalPaymentSum : Edm.Double
- CreditSum : Edm.Double
- CreditCur : Edm.String
- CreditRate : Edm.Double
- ConfirmationNum : Edm.String
- NumOfCreditPayments : Edm.Int32
- CreditType : SAPB1.BoRcptCredTypes
- SplitPayments : SAPB1.BoYesNoEnum

# SAPB1.PaymentDocumentReferences (ComplexType)

## Properties

- DocEntry : Edm.Int32
- LineNumber : Edm.Int32
- ReferencedDocEntry : Edm.Int32
- ReferencedDocNumber : Edm.Int32
- ExternalReferencedDocNumber : Edm.String
- ReferencedObjectType : SAPB1.ReferencedObjectTypeEnum
- IssueDate : Edm.DateTimeOffset
- Remark : Edm.String

# SAPB1.PaymentInvoice (ComplexType)

OpenType: true

## Properties

- LineNum : Edm.Int32
- DocEntry : Edm.Int32
- DocNum : Edm.Int32
- SumApplied : Edm.Double
- AppliedFC : Edm.Double
- AppliedSys : Edm.Double
- DocRate : Edm.Double
- DocLine : Edm.Int32
- InvoiceType : SAPB1.BoRcptInvTypes
- DiscountPercent : Edm.Double
- PaidSum : Edm.Double
- InstallmentId : Edm.Int32
- WitholdingTaxApplied : Edm.Double
- WitholdingTaxAppliedFC : Edm.Double
- WitholdingTaxAppliedSC : Edm.Double
- LinkDate : Edm.DateTimeOffset
- DistributionRule : Edm.String
- DistributionRule2 : Edm.String
- DistributionRule3 : Edm.String
- DistributionRule4 : Edm.String
- DistributionRule5 : Edm.String
- TotalDiscount : Edm.Double
- TotalDiscountFC : Edm.Double
- TotalDiscountSC : Edm.Double

# SAPB1.PaymentInvoiceEntry (ComplexType)

## Properties

- DocType : SAPB1.PaymentInvoiceTypeEnum
- DocEntry : Edm.Int32
- InstallmentId : Edm.Int32

# SAPB1.PaymentParams (ComplexType)

## Properties

- DocEntry : Edm.Int32

# SAPB1.PaymentReasonCode (EntityType)

Key: Code

## Properties

- Code : Edm.String [required]

## Navigation properties

- SpecificWTHAmountsService : Collection(SAPB1.SpecificWTHAmounts) [Partner=PaymentReasonCode2]

# SAPB1.PaymentReasonCodeParams (ComplexType)

## Properties

- Code : Edm.String

# SAPB1.PaymentRunExport (EntityType)

OpenType: true
Key: AbsoluteEntry

## Properties

- AbsoluteEntry : Edm.Int32 [required]
- RunDate : Edm.DateTimeOffset
- VendorNum : Edm.String
- CustomerNum : Edm.String
- PaymentMethod : Edm.String
- DocNum : Edm.Int32
- FiscalYear : Edm.DateTimeOffset
- Countery : Edm.String
- CompanyTaxNum : Edm.String
- PayeeName : Edm.String
- PayeePostalCode : Edm.String
- PayeeCity : Edm.String
- PayeeStreet : Edm.String
- PayeeCountry : Edm.String
- PayeeState : Edm.String
- PayeeBankName : Edm.String
- PayeeBankZip : Edm.String
- PayeeBankCity : Edm.String
- PayeeBankStreet : Edm.String
- PayeeBankCountry : Edm.String
- PayeeBankAccount : Edm.String
- PayeeBankCode : Edm.String
- PayeeBankCtrlKey : Edm.String
- PayeeBankSwiftNum : Edm.String
- PayeeBankIBAN : Edm.String
- PostingDate : Edm.DateTimeOffset
- BankAccount : Edm.String
- BankCountry : Edm.String
- BankCode : Edm.String
- BankIBAN : Edm.String
- GLAccount : Edm.String
- Currency : Edm.String
- DocAmountLocal : Edm.Double
- DocCurrnecy : Edm.String
- DocAmountForign : Edm.Double
- DocCashDiscount : Edm.Double
- DocCashDiscountForign : Edm.Double
- DocNumOffieldPaid : Edm.Int32
- DocRate : Edm.Double
- WizCode : Edm.Int32
- CollectionAuthorization : SAPB1.BoYesNoEnum
- PayeeBankPostOffice : SAPB1.BoYesNoEnum
- PayeeBankNextCheckNumber : Edm.Int32
- PayeeBankHouseBank : SAPB1.BoYesNoEnum
- PayeeBankBlock : Edm.String
- PayeeBankCounty : Edm.String
- PayeeBankState : Edm.String
- PayeeBankBISR : SAPB1.BoYesNoEnum
- PayeeBankUserNum1 : Edm.String
- PayeeBankUserNum2 : Edm.String
- PayeeBankUserNum3 : Edm.String
- PayeeBankUserNum4 : Edm.String
- InstructionKey : Edm.String
- PaymentFormat : Edm.String
- CompanyName : Edm.String
- CompanyAddress : Edm.String
- Status : SAPB1.BoOpexStatus
- CompIsrBillerID : Edm.String
- VendorIsrBillerID : Edm.String
- AdditionalIdNumber : Edm.String
- OrganizationNumber : Edm.String
- PayeeBankBranch : Edm.String
- PaymentBankBranch : Edm.String
- UserName : Edm.String
- UserEMail : Edm.String
- UserMobilePhoneNumber : Edm.String
- UserFaxNumber : Edm.String
- UserDepartment : Edm.Int32
- DebitMemo : SAPB1.BoYesNoEnum
- EUInternalTransfer : SAPB1.BoYesNoEnum
- FilePath : Edm.String
- OrderingParty : Edm.String
- PaymentBankControlKey : Edm.String
- PayeeTaxNumber : Edm.String
- PaymentKeyCode : Edm.String
- PayeeReferenceDetails : Edm.String
- FormatName : Edm.String
- PaymentDonewithCheck : SAPB1.BoYesNoEnum
- CompanyBlock : Edm.String
- CompanyCity : Edm.String
- CompanyCounty : Edm.String
- CompanyState : Edm.String
- CompanyStreet : Edm.String
- CompanyZipCode : Edm.String
- PaymentBankCharges : Edm.String
- PaymentBankUserNo1 : Edm.String
- PaymentBankUserNo2 : Edm.String
- PaymentBankUserNo3 : Edm.String
- PaymentBankUserNo4 : Edm.String
- PaymentBankChargesAllocationCode : Edm.String
- PaymentOrderNum : Edm.Int32
- FreeText1 : Edm.String
- FreeText2 : Edm.String
- FreeText3 : Edm.String
- RowType : SAPB1.PaymentRunExportRowTypeEnum
- PaymentRunExport_Lines : Collection(SAPB1.PaymentRunExport_Line)

## Navigation properties

- PaymentWizard : SAPB1.PaymentWizard [Partner=PaymentRunExport]
- BankChargesAllocationCode : SAPB1.BankChargesAllocationCode [Partner=PaymentRunExport]

# SAPB1.PaymentRunExport_Line (ComplexType)

OpenType: true

## Properties

- RowNumber : Edm.Int32
- DateOfPaymentRun : Edm.DateTimeOffset
- PaymentWizardCode : Edm.Int32
- VendorNumber : Edm.String
- CustomerNumber : Edm.String
- PaymentMeans : Edm.String
- PaymentDocNum : Edm.Int32
- FiscalYear : Edm.DateTimeOffset
- VendorRefNum : Edm.String
- DocumentObjectType : Edm.String
- DocumentPostingDate : Edm.DateTimeOffset
- DocumentTaxDate : Edm.DateTimeOffset
- BPDebitPayableAccount : Edm.String
- DocumentCurrency : Edm.String
- DocumentRate : Edm.Double
- DocumentTotal : Edm.Double
- DocumentTotalFC : Edm.Double
- DocumentTaxAmount : Edm.Double
- DocumentTaxAmountFC : Edm.Double
- DocumentRemarks : Edm.String
- DocumentPaymentTerms : Edm.Int32
- PaymentDocReference : Edm.String
- DocumentLocalCurrency : Edm.String
- PaymentTermsPeriod : Edm.Int32
- DocumentObjectTypeEx : Edm.String
- DocumentNumber : Edm.Int32
- PaymentNumber : Edm.Int32
- PaymentOrderNum : Edm.Int32
- FreeText1 : Edm.String
- FreeText2 : Edm.String
- FreeText3 : Edm.String

# SAPB1.PaymentRunExportParams (ComplexType)

## Properties

- AbsoluteEntry : Edm.Int32

# SAPB1.Payments_ApprovalRequest (ComplexType)

## Properties

- ApprovalTemplatesID : Edm.Int32
- Remarks : Edm.String
- ApprovalTemplatesName : Edm.String
- ActiveForUpdate : SAPB1.BoYesNoEnum

# SAPB1.PaymentTermsType (EntityType)

OpenType: true
Key: GroupNumber
Filtered properties: 1

## Properties

- GroupNumber : Edm.Int32 [required]
- PaymentTermsGroupName : Edm.String
- StartFrom : SAPB1.BoPayTermDueTypes
- NumberOfAdditionalMonths : Edm.Int32
- NumberOfAdditionalDays : Edm.Int32
- CreditLimit : Edm.Double
- GeneralDiscount : Edm.Double
- InterestOnArrears : Edm.Double
- PriceListNo : Edm.Int32
- LoadLimit : Edm.Double
- OpenReceipt : SAPB1.BoOpenIncPayment
- DiscountCode : Edm.String
- DunningCode : Edm.String
- BaselineDate : SAPB1.BoBaselineDate
- NumberOfInstallments : Edm.Int32
- NumberOfToleranceDays : Edm.Int32
- EndAt : SAPB1.BoPayTermDueTypes

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- Drafts : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- StockTransferDrafts : Collection(SAPB1.StockTransfer) [Partner=PaymentTermsType]
- InventoryTransferRequests : Collection(SAPB1.StockTransfer) [Partner=PaymentTermsType]
- BlanketAgreements : Collection(SAPB1.BlanketAgreement) [Partner=PaymentTermsType]
- CreditNotes : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- PriceList : SAPB1.PriceList [Partner=PaymentTermsTypes]
- CashDiscount : SAPB1.CashDiscount [Partner=PaymentTermsTypes]
- Invoices : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- WizardPaymentMethods : Collection(SAPB1.WizardPaymentMethod) [Partner=PaymentTermsType]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- Orders : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- Returns : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=PaymentTermsType]
- DownPayments : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- ReturnRequest : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- Quotations : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- SelfInvoices : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=PaymentTermsType]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=PaymentTermsType]

# SAPB1.PaymentTermsTypeParams (ComplexType)

## Properties

- GroupNumber : Edm.Int32

# SAPB1.PaymentWizard (EntityType)

Key: IdNumber

## Properties

- IdNumber : Edm.Int32 [required]
- WizardName : Edm.String
- PmntDate : Edm.DateTimeOffset
- OutgoingType : SAPB1.PaymentWizardTypeEnum
- IncomingType : SAPB1.PaymentWizardTypeEnum
- CheckPaymentMethod : SAPB1.PaymentMethodEnum
- BankTransferPaymentMethod : SAPB1.PaymentMethodEnum
- BillOfExchangePaymentMethod : SAPB1.PaymentMethodEnum

## Navigation properties

- PaymentRunExport : Collection(SAPB1.PaymentRunExport) [Partner=PaymentWizard]

# SAPB1.PaymentWizardParams (ComplexType)

## Properties

- IdNumber : Edm.Int32
- WizardName : Edm.String

# SAPB1.PeriodCategory (ComplexType)

## Properties

- AbsoluteEntry : Edm.Int32
- BeginningofFinancialYear : Edm.DateTimeOffset
- PeriodCategoryProperty : Edm.String
- SubPeriodType : SAPB1.BoSubPeriodTypeEnum
- NumberOfPeriods : Edm.Int32
- PeriodName : Edm.String
- DebitorsFollowUpAccount : Edm.String
- AccountforOutgoingChecks : Edm.String
- AccountforCashReceipt : Edm.String
- CustomersDeductionatSource : Edm.String
- CommissionAccountDefault : Edm.String
- PurchaseTax : Edm.String
- ForeignAccountsReceivables : Edm.String
- CreditorsFollowUpAccount : Edm.String
- OutgoingChecksAccount : Edm.String
- OutgoingCashAccount : Edm.String
- AccountforCreditMemoPayme : Edm.String
- InputTaxAccount : Edm.String
- TaxDefinition : Edm.String
- WithholodingTax : Edm.String
- OpeningBalancesAccount : Edm.String
- DefaultSaleAccount : Edm.String
- TaxExemptRevenuesDefault : Edm.String
- ExpenseAccountDefault : Edm.String
- RevenuesAccountForeign : Edm.String
- SalesRevenueEU : Edm.String
- ExpensesAccountForeign : Edm.String
- RateDifferencesDefaultAcc : Edm.String
- DecreaseGLAcc : Edm.String
- ReconciliationDifference : Edm.String
- AcountforOpeningWHBalance : Edm.String
- APCashDiscountAccount : Edm.String
- APLossCashDiscountAccount : Edm.String
- APLossRealizedExchangeDif : Edm.String
- ARCashDiscountAccount : Edm.String
- ARLossRealizedExchangeDi : Edm.String
- RoundingAccount : Edm.String
- APGainRealizedExchngeDif : Edm.String
- ARGainRealizedExchngeDif : Edm.String
- IncreaseGLAccount : Edm.String
- SalesReturns : Edm.String
- CostOfGoodsSold : Edm.String
- AllocationAcc : Edm.String
- VarianceAcc : Edm.String
- PriceDifferenceAccount : Edm.String
- CustomerDownPaymentsAccount : Edm.String
- VendorDownPaymentsAccount : Edm.String
- BillofExchangeAccountsRece : Edm.String
- CustBillofExchangeonC : Edm.String
- CustomerBillofExchangePres : Edm.String
- CustomerBillofExchngeDisc : Edm.String
- CustomerUnpaidBoE : Edm.String
- BoEAccountsPayable : Edm.String
- BoEAccountsPayable2 : Edm.String
- CustomerDoubtfulDebtsAcct : Edm.String
- VendorDoubtfulDebtsAcct : Edm.String
- PurchaseAccount : Edm.String
- PurchaseReturnAccount : Edm.String
- PurchaseOffsetAccount : Edm.String
- EOYControlAccount : Edm.String
- ExchangeRateDifferencesAcct : Edm.String
- GoodsClearingAcc : Edm.String
- ExpenseClearingAccount : Edm.String
- ExpenseOffsetAccount : Edm.String
- CostofSaleRevaluationAcct : Edm.String
- RepomoAccount : Edm.String
- WIPMaterialVarianceAccount : Edm.String
- DownPaymentVATAcctSale : Edm.String
- DownPaymentVATAcctPurch : Edm.String
- DownPaymentSClearingAcct : Edm.String
- DownPaymentPClearingAcct : Edm.String
- ExpenseVarianceAccount : Edm.String
- CostofSaleRevOffsetAcct : Edm.String
- EUExpenseAccount : Edm.String
- StockAccount : Edm.String
- InventoryOffsetIncrease : Edm.String
- InventoryOffsetDecrease : Edm.String
- VendorAssetsAccount : Edm.String
- StockRevaluationAccount : Edm.String
- StockRevaluationOffsetAcct : Edm.String
- WIPMaterialAccount : Edm.String
- InvoicePaymentBP : Edm.String
- GLRevaluationOffsetAccount : Edm.String
- OverpaymentsAPAccount : Edm.String
- UnderpaymentsAPAccount : Edm.String
- OverpaymentsARAccount : Edm.String
- UnderpaymentsARAccount : Edm.String
- PurchaseCreditAcc : Edm.String
- EUPurchaseCreditAcc : Edm.String
- ForeignPurchaseCreditAcc : Edm.String
- SalesCreditAcc : Edm.String
- SalesCreditEUAcc : Edm.String
- ExemptedCredits : Edm.String
- SalesCreditForeignAcc : Edm.String
- FromPostingDate : Edm.DateTimeOffset
- ToPostingDate : Edm.DateTimeOffset
- FromDueDate : Edm.DateTimeOffset
- ToDueDate : Edm.DateTimeOffset
- FromDocumentDate : Edm.DateTimeOffset
- ToDocumentDate : Edm.DateTimeOffset
- OutgoingTaxAccount : Edm.String
- NegativeInventoryAdjustmentAccount : Edm.String
- FinancialYear : Edm.Int32
- SelfInvoiceRevenueAccount : Edm.String
- SelfInvoiceExpenseAccount : Edm.String
- StockInTransitAccount : Edm.String
- SalesDownPaymentInterimAccount : Edm.String
- PurchaseDownPaymentInterimAccount : Edm.String
- EUAccountsReceivable : Edm.String
- EUAccountsPayable : Edm.String
- WipOffsetProfitAndLossAccount : Edm.String
- InventoryOffsetProfitAndLossAccount : Edm.String
- DunningInterestAccount : Edm.String
- DunningFeeAccount : Edm.String
- ARGainRealizedConversionDiff : Edm.String
- ARLossRealizedConversionDiff : Edm.String
- APGainRealizedConversionDiff : Edm.String
- APLossRealizedConversionDiff : Edm.String
- GLGainRealizedConversionDiff : Edm.String
- GLLossRealizedConversionDiff : Edm.String
- ARExRateInterim : Edm.String
- APExRateInterim : Edm.String
- ARCashDiscountInterim : Edm.String
- APCashDiscountInterim : Edm.String
- SalesInterimAcctLnWTax : Edm.String
- PurchaseInterimAcctLnWTax : Edm.String
- ExhRatesDiffAcctLnWTax : Edm.String
- WIPMappingCollection : Collection(SAPB1.WIPMapping)

# SAPB1.PeriodCategoryParams (ComplexType)

## Properties

- AbsoluteEntry : Edm.Int32

# SAPB1.PickList (EntityType)

OpenType: true
Key: Absoluteentry

## Properties

- Absoluteentry : Edm.Int32 [required]
- Name : Edm.String
- OwnerCode : Edm.Int32
- OwnerName : Edm.String
- PickDate : Edm.DateTimeOffset
- Remarks : Edm.String
- Status : SAPB1.BoPickStatus
- ObjectType : Edm.String
- UseBaseUnits : SAPB1.BoYesNoEnum
- CreateQRCodeFrom : Edm.String
- PickListsLines : Collection(SAPB1.PickListsLine)

## Navigation properties

- User : SAPB1.User [Partner=PickLists]

# SAPB1.PickListParams (ComplexType)

## Properties

- Absoluteentry : Edm.Int32

# SAPB1.PickListsLine (ComplexType)

OpenType: true

## Properties

- AbsoluteEntry : Edm.Int32
- LineNumber : Edm.Int32
- OrderEntry : Edm.Int32
- OrderRowID : Edm.Int32
- PickedQuantity : Edm.Double
- PickStatus : SAPB1.BoPickStatus
- ReleasedQuantity : Edm.Double
- PreviouslyReleasedQuantity : Edm.Double
- BaseObjectType : Edm.Int32
- SerialNumbers : Collection(SAPB1.SerialNumber)
- BatchNumbers : Collection(SAPB1.BatchNumber)
- DocumentLinesBinAllocations : Collection(SAPB1.DocumentLinesBinAllocation)

# SAPB1.Picture (EntityType)

HasStream: true
Key: PictureName

## Properties

- PictureName : Edm.String [required]
- PicturePath : Edm.String [required]
- PictureSize : Edm.Int32 [required]
- PictureCreateDate : Edm.String [required]
- PictureModifyDate : Edm.String [required]

# SAPB1.PM_ActivityData (ComplexType)

OpenType: true

## Properties

- LineID : Edm.Int32
- StageID : Edm.Int32
- ActivityID : Edm.Int32

# SAPB1.PM_DocAttachement (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- LineID : Edm.Int32
- SourcePath : Edm.String
- FileName : Edm.String
- FileExtension : Edm.String
- AttachementDate : Edm.DateTimeOffset

# SAPB1.PM_DocumentData (ComplexType)

OpenType: true

## Properties

- LineID : Edm.Int32
- StageID : Edm.Int32
- DocType : SAPB1.PMDocumentTypeEnum
- DocEntry : Edm.Int32
- DocDate : Edm.DateTimeOffset
- Total : Edm.Double
- LineNumber : Edm.Int32
- Status : SAPB1.LineStatusTypeEnum
- AmountCategory : SAPB1.AmountCatTypeEnum
- Categorize : SAPB1.PMCategorizeTypeEnum
- Operation : SAPB1.PMOperationTypeEnum

# SAPB1.PM_OpenIssueData (ComplexType)

OpenType: true

## Properties

- LineID : Edm.Int32
- StageID : Edm.Int32
- Area : Edm.Int32
- Priority : Edm.Int32
- Remarks : Edm.String
- Closed : SAPB1.BoYesNoEnum
- SolutionID : Edm.Int32
- Responsible : Edm.Int32
- EnteredBy : Edm.Int32
- EnteredDate : Edm.DateTimeOffset
- Effort : Edm.Double

# SAPB1.PM_ProjectDocumentData (EntityType)

OpenType: true
Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- Owner : Edm.Int32
- ProjectName : Edm.String
- StartDate : Edm.DateTimeOffset
- FinishedPercent : Edm.Double
- DocNum : Edm.Int32
- Series : Edm.Int32
- ProjectType : SAPB1.ProjectTypeEnum
- BusinessPartner : Edm.String
- BusinessPartnerName : Edm.String
- ContactPerson : Edm.Int32
- Territory : Edm.Int32
- SalesEmployee : Edm.Int32
- AllowSubprojects : SAPB1.BoYesNoEnum
- ProjectStatus : SAPB1.ProjectStatusTypeEnum
- DueDate : Edm.DateTimeOffset
- ClosingDate : Edm.DateTimeOffset
- FinancialProject : Edm.String
- RiskLevel : SAPB1.RiskLevelTypeEnum
- Industry : Edm.Int32
- Reason : Edm.String
- AttachmentEntry : Edm.Int32
- PM_StagesCollection : Collection(SAPB1.PM_StageData)
- PM_OpenIssuesCollection : Collection(SAPB1.PM_OpenIssueData)
- PM_DocumentsCollection : Collection(SAPB1.PM_DocumentData)
- PM_ActivitiesCollection : Collection(SAPB1.PM_ActivityData)
- PM_WorkOrdersCollection : Collection(SAPB1.PM_WorkOrderData)
- PM_SummaryData : SAPB1.PM_SummaryData
- PM_DocAttachements : Collection(SAPB1.PM_DocAttachement)
- PM_StageAttachements : Collection(SAPB1.PM_StageAttachement)

## Navigation properties

- EmployeeInfo : SAPB1.EmployeeInfo [Partner=ProjectManagements]
- BusinessPartner2 : SAPB1.BusinessPartner [Partner=ProjectManagements]
- Territory2 : SAPB1.Territory [Partner=ProjectManagements]
- SalesPerson : SAPB1.SalesPerson [Partner=ProjectManagements]
- Project : SAPB1.Project [Partner=ProjectManagements]
- Industry2 : SAPB1.Industry [Partner=ProjectManagements]
- Attachments2 : SAPB1.Attachments2 [Partner=ProjectManagements]

# SAPB1.PM_ProjectDocumentParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32

# SAPB1.PM_StageAttachement (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- LineID : Edm.Int32
- SourcePath : Edm.String
- FileName : Edm.String
- FileExtension : Edm.String
- AttachementDate : Edm.DateTimeOffset

# SAPB1.PM_StageData (ComplexType)

OpenType: true

## Properties

- LineID : Edm.Int32
- StageID : Edm.Int32
- StageType : Edm.Int32
- StartDate : Edm.DateTimeOffset
- CloseDate : Edm.DateTimeOffset
- Task : Edm.Int32
- Description : Edm.String
- ExpectedCosts : Edm.Double
- InvoicedAmountSales : Edm.Double
- OpenAmountSales : Edm.Double
- InvoicedAmountPurchase : Edm.Double
- OpenAmountPurchase : Edm.Double
- PercentualCompletness : Edm.Double
- IsFinished : SAPB1.BoYesNoEnum
- StageOwner : Edm.Int32
- DependsOnStage1 : Edm.Int32
- DependsOnStage2 : Edm.Int32
- DependsOnStage3 : Edm.Int32
- DependsOnStage4 : Edm.Int32
- StageDependency1Type : SAPB1.StageDepTypeEnum
- StageDependency2Type : SAPB1.StageDepTypeEnum
- StageDependency3Type : SAPB1.StageDepTypeEnum
- StageDependency4Type : SAPB1.StageDepTypeEnum
- DependsOnStageID1 : Edm.Int32
- DependsOnStageID2 : Edm.Int32
- DependsOnStageID3 : Edm.Int32
- DependsOnStageID4 : Edm.Int32
- AttachmentEntry : Edm.Int32
- UniqueID : Edm.String
- FinishedDate : Edm.DateTimeOffset

# SAPB1.PM_SubprojectDocumentData (ComplexType)

OpenType: true

## Properties

- AbsEntry : Edm.Int32
- Owner : Edm.Int32
- SubprojectName : Edm.String
- StartDate : Edm.DateTimeOffset
- FinishedPercent : Edm.Double
- ParentID : Edm.Int32
- ProjectID : Edm.Int32
- Order : Edm.Int32
- SubprojectType : Edm.Int32
- SubprojectContribution : Edm.Double
- SubprojectStatus : SAPB1.SubprojectStatusTypeEnum
- SubprojectEndDate : Edm.DateTimeOffset
- ActualCost : Edm.Double
- PlannedCost : Edm.Double
- SubprojectDepth : Edm.Int32
- DueDate : Edm.DateTimeOffset
- PMS_StagesCollection : Collection(SAPB1.PMS_StageData)
- PMS_OpenIssuesCollection : Collection(SAPB1.PMS_OpenIssueData)
- PMS_DocumentsCollection : Collection(SAPB1.PMS_DocumentData)
- PMS_ActivitiesCollection : Collection(SAPB1.PMS_ActivityData)
- PMS_WorkOrdersCollection : Collection(SAPB1.PMS_WorkOrderData)
- PMS_SummaryData : SAPB1.PMS_SummaryData
- PMS_DocAttachements : Collection(SAPB1.PMS_DocAttachement)
- PMS_StageAttachements : Collection(SAPB1.PMS_StageAttachement)

# SAPB1.PM_SubprojectDocumentParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32

# SAPB1.PM_SubprojectParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- IsSubproject : SAPB1.BoYesNoEnum

# SAPB1.PM_SummaryData (ComplexType)

## Properties

- LineID : Edm.Int32
- SubprojectBudget : Edm.Double
- SumOpenAmountPurchase : Edm.Double
- SumInvoicedAmountPurchase : Edm.Double
- TotalAmountPurchase : Edm.Double
- TotalVariancePurchase : Edm.Double
- VariancePerceptionPurchase : Edm.Double
- AccumSubprojectBudget : Edm.Double
- AccumOpenAmountPurchase : Edm.Double
- AccumInvoicedAmountPurchase : Edm.Double
- AccumTotalPurchase : Edm.Double
- AccumTotalVariancePurchase : Edm.Double
- AccumVariancePerceptionPurchase : Edm.Double
- PotentialSubprojectAmount : Edm.Double
- SumOpenAmountSales : Edm.Double
- SumInvoicedAmountSales : Edm.Double
- TotalAmountSales : Edm.Double
- TotalVarianceSales : Edm.Double
- VariancePerceptionSales : Edm.Double
- AccumPotentialSubprojectAmount : Edm.Double
- AccumOpenAmountSales : Edm.Double
- AccumInvoicedAmountSales : Edm.Double
- AccumTotalSales : Edm.Double
- AccumTotalVarianceSales : Edm.Double
- AccumVariancePerceptionSales : Edm.Double
- ActualItemComponentCost : Edm.Double
- ActualResourceComponentCost : Edm.Double
- ActualAdditionalCost : Edm.Double
- ActualProductCost : Edm.Double
- ActualByProductCost : Edm.Double
- TotalVariance : Edm.Double
- DueDate : Edm.DateTimeOffset
- ActualClosingDate : Edm.DateTimeOffset
- Overdue : Edm.Int32

# SAPB1.PM_TimeSheetData (EntityType)

OpenType: true
Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- DocNumber : Edm.Int32
- TimeSheetType : SAPB1.TimeSheetTypeEnum
- UserID : Edm.Int32
- LastName : Edm.String
- FirstName : Edm.String
- Department : Edm.Int32
- OwnerCode : Edm.Int32
- DateFrom : Edm.DateTimeOffset
- DateTo : Edm.DateTimeOffset
- SAPPassport : Edm.String
- AttachmentEntry : Edm.Int32
- UserCode : Edm.String
- PM_TimeSheetLineDataCollection : Collection(SAPB1.PM_TimeSheetLineData)

## Navigation properties

- EmployeeInfo : SAPB1.EmployeeInfo [Partner=ProjectManagementTimeSheet]
- Attachments2 : SAPB1.Attachments2 [Partner=ProjectManagementTimeSheet]

# SAPB1.PM_TimeSheetLineData (ComplexType)

OpenType: true

## Properties

- LineID : Edm.Int32
- Date : Edm.DateTimeOffset
- ActivityType : Edm.Int32
- LaborItem : Edm.String
- StartTime : Edm.TimeOfDay
- EndTime : Edm.TimeOfDay
- Workorder : Edm.Int32
- ServiceCall : Edm.Int32
- CostCenter : Edm.String
- FinancialProject : Edm.String
- Location : Edm.Int32
- GPSData : Edm.String
- Branch : Edm.Int32
- Break : Edm.TimeOfDay
- NonBillableTime : Edm.TimeOfDay
- EffectiveTime : Edm.TimeOfDay
- BillableTime : Edm.TimeOfDay
- FullDay : SAPB1.BoYesNoEnum
- ProjectID : Edm.Int32
- SubprojectID : Edm.Int32
- StageID : Edm.Int32

# SAPB1.PM_TimeSheetParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32

# SAPB1.PM_WorkOrderData (ComplexType)

OpenType: true

## Properties

- LineID : Edm.Int32
- StageID : Edm.Int32
- DocNumber : Edm.Int32
- DocEntry : Edm.Int32

# SAPB1.PMC_ActivityData (ComplexType)

## Properties

- ActivityID : Edm.Int32
- ActivityType : Edm.String
- LaborItem : Edm.String
- IsChargeable : SAPB1.BoYesNoEnum
- IsAbsence : SAPB1.BoYesNoEnum

# SAPB1.PMC_AreaData (ComplexType)

## Properties

- AreaID : Edm.Int32
- AreaName : Edm.String

# SAPB1.PMC_PriorityData (ComplexType)

## Properties

- PriorityID : Edm.Int32
- PriorityName : Edm.String

# SAPB1.PMC_StageTypeData (ComplexType)

## Properties

- StageID : Edm.Int32
- StageName : Edm.String
- StageDescription : Edm.String

# SAPB1.PMC_SubprojectTypeData (ComplexType)

## Properties

- SubprojectTypeID : Edm.Int32
- SubprojectTypeName : Edm.String

# SAPB1.PMC_TaskData (ComplexType)

## Properties

- TaskID : Edm.Int32
- TaskName : Edm.String

# SAPB1.PMS_ActivityData (ComplexType)

OpenType: true

## Properties

- LineID : Edm.Int32
- StageID : Edm.Int32
- ActivityID : Edm.Int32

# SAPB1.PMS_DocAttachement (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- LineID : Edm.Int32
- SourcePath : Edm.String
- FileName : Edm.String
- FileExtension : Edm.String
- AttachementDate : Edm.DateTimeOffset

# SAPB1.PMS_DocumentData (ComplexType)

OpenType: true

## Properties

- LineID : Edm.Int32
- StageID : Edm.Int32
- DocType : SAPB1.PMDocumentTypeEnum
- DocEntry : Edm.Int32
- DocDate : Edm.DateTimeOffset
- Total : Edm.Double
- LineNumber : Edm.Int32
- Status : SAPB1.LineStatusTypeEnum
- AmountCategory : SAPB1.AmountCatTypeEnum
- Categorize : SAPB1.PMCategorizeTypeEnum
- Operation : SAPB1.PMOperationTypeEnum

# SAPB1.PMS_OpenIssueData (ComplexType)

OpenType: true

## Properties

- LineID : Edm.Int32
- StageID : Edm.Int32
- Area : Edm.Int32
- Priority : Edm.Int32
- Remarks : Edm.String
- Closed : SAPB1.BoYesNoEnum
- SolutionID : Edm.Int32
- Responsible : Edm.Int32
- EnteredBy : Edm.Int32
- EnteredDate : Edm.DateTimeOffset
- Effort : Edm.Double

# SAPB1.PMS_StageAttachement (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- LineID : Edm.Int32
- SourcePath : Edm.String
- FileName : Edm.String
- FileExtension : Edm.String
- AttachementDate : Edm.DateTimeOffset

# SAPB1.PMS_StageData (ComplexType)

OpenType: true

## Properties

- LineID : Edm.Int32
- StageID : Edm.Int32
- StageType : Edm.Int32
- StartDate : Edm.DateTimeOffset
- CloseDate : Edm.DateTimeOffset
- Task : Edm.Int32
- Description : Edm.String
- ExpectedCosts : Edm.Double
- InvoicedAmountSales : Edm.Double
- OpenAmountSales : Edm.Double
- InvoicedAmountPurchase : Edm.Double
- OpenAmountPurchase : Edm.Double
- PercentualCompletness : Edm.Double
- IsFinished : SAPB1.BoYesNoEnum
- StageOwner : Edm.Int32
- DependsOnStage1 : Edm.Int32
- DependsOnStage2 : Edm.Int32
- DependsOnStage3 : Edm.Int32
- DependsOnStage4 : Edm.Int32
- StageDependency1Type : SAPB1.StageDepTypeEnum
- StageDependency2Type : SAPB1.StageDepTypeEnum
- StageDependency3Type : SAPB1.StageDepTypeEnum
- StageDependency4Type : SAPB1.StageDepTypeEnum
- DependsOnStageID1 : Edm.Int32
- DependsOnStageID2 : Edm.Int32
- DependsOnStageID3 : Edm.Int32
- DependsOnStageID4 : Edm.Int32
- AttachmentEntry : Edm.Int32
- UniqueID : Edm.String
- FinishedDate : Edm.DateTimeOffset

# SAPB1.PMS_SummaryData (ComplexType)

## Properties

- LineID : Edm.Int32
- SubprojectBudget : Edm.Double
- SumOpenAmountPurchase : Edm.Double
- SumInvoicedAmountPurchase : Edm.Double
- TotalAmountPurchase : Edm.Double
- TotalVariancePurchase : Edm.Double
- VariancePerceptionPurchase : Edm.Double
- AccumSubprojectBudget : Edm.Double
- AccumOpenAmountPurchase : Edm.Double
- AccumInvoicedAmountPurchase : Edm.Double
- AccumTotalPurchase : Edm.Double
- AccumTotalVariancePurchase : Edm.Double
- AccumVariancePerceptionPurchase : Edm.Double
- PotentialSubprojectAmount : Edm.Double
- SumOpenAmountSales : Edm.Double
- SumInvoicedAmountSales : Edm.Double
- TotalAmountSales : Edm.Double
- TotalVarianceSales : Edm.Double
- VariancePerceptionSales : Edm.Double
- AccumPotentialSubprojectAmount : Edm.Double
- AccumOpenAmountSales : Edm.Double
- AccumInvoicedAmountSales : Edm.Double
- AccumTotalSales : Edm.Double
- AccumTotalVarianceSales : Edm.Double
- AccumVariancePerceptionSales : Edm.Double
- ActualItemComponentCost : Edm.Double
- ActualResourceComponentCost : Edm.Double
- ActualAdditionalCost : Edm.Double
- ActualProductCost : Edm.Double
- ActualByProductCost : Edm.Double
- TotalVariance : Edm.Double
- DueDate : Edm.DateTimeOffset
- ActualClosingDate : Edm.DateTimeOffset
- Overdue : Edm.Int32

# SAPB1.PMS_WorkOrderData (ComplexType)

OpenType: true

## Properties

- LineID : Edm.Int32
- StageID : Edm.Int32
- DocNumber : Edm.Int32
- DocEntry : Edm.Int32

# SAPB1.POSDailySummary (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- Date : Edm.DateTimeOffset
- EquipmentNo : Edm.String
- CounterPosition : Edm.Int32
- ResetCounterPosition : Edm.Int32
- OperationCounter : Edm.Int32
- Total : Edm.Double
- GrossSales : Edm.Double
- PISTotal : Edm.Double
- COFINSTotal : Edm.Double
- POSTotalizerCollection : Collection(SAPB1.POSTotalizer)

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=POSDailySummary]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=POSDailySummary]
- Drafts : Collection(SAPB1.Document) [Partner=POSDailySummary]
- CreditNotes : Collection(SAPB1.Document) [Partner=POSDailySummary]
- Invoices : Collection(SAPB1.Document) [Partner=POSDailySummary]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=POSDailySummary]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=POSDailySummary]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=POSDailySummary]
- Orders : Collection(SAPB1.Document) [Partner=POSDailySummary]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=POSDailySummary]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=POSDailySummary]
- Returns : Collection(SAPB1.Document) [Partner=POSDailySummary]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=POSDailySummary]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=POSDailySummary]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=POSDailySummary]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=POSDailySummary]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=POSDailySummary]
- DownPayments : Collection(SAPB1.Document) [Partner=POSDailySummary]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=POSDailySummary]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=POSDailySummary]
- ReturnRequest : Collection(SAPB1.Document) [Partner=POSDailySummary]
- Quotations : Collection(SAPB1.Document) [Partner=POSDailySummary]
- FiscalPrinter : SAPB1.FiscalPrinter [Partner=POSDailySummary]
- SelfInvoices : Collection(SAPB1.Document) [Partner=POSDailySummary]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=POSDailySummary]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=POSDailySummary]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=POSDailySummary]

# SAPB1.POSDailySummaryParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32

# SAPB1.PostingTemplates (EntityType)

Key: Code

## Properties

- Code : Edm.String [required]
- Description : Edm.String
- StampTax : SAPB1.BoYesNoEnum
- AutomaticVAT : SAPB1.BoYesNoEnum
- ManageWTax : SAPB1.BoYesNoEnum
- DeferredTax : SAPB1.BoYesNoEnum
- PostingTemplatesLineCollection : Collection(SAPB1.PostingTemplatesLine)

# SAPB1.PostingTemplatesLine (ComplexType)

## Properties

- TrtCode : Edm.String
- LineNumber : Edm.Int32
- ControlAccount : Edm.String
- AccountCode : Edm.String
- AccountName : Edm.String
- Debit : Edm.Double
- Credit : Edm.Double
- TaxGroup : Edm.String
- VatLine : SAPB1.BoYesNoEnum
- TaxPostingAccount : SAPB1.BoTaxPostingAccountTypeEnum
- TaxCode : Edm.String
- DistributionRule : Edm.String
- CostingCode1 : Edm.String
- CostingCode2 : Edm.String
- CostingCode3 : Edm.String
- CostingCode4 : Edm.String
- CostingCode5 : Edm.String
- WTaxLiable : SAPB1.BoYesNoEnum
- WTaxLine : SAPB1.BoYesNoEnum
- ProjectCode : Edm.String
- CostElementCode : Edm.String

# SAPB1.PostingTemplatesParams (ComplexType)

## Properties

- Code : Edm.String
- Description : Edm.String

# SAPB1.POSTotalizer (ComplexType)

## Properties

- LineNum : Edm.Int32
- Code : Edm.String
- Number : Edm.Int32
- Total : Edm.Double
- Description : Edm.String

# SAPB1.PredefinedText (EntityType)

Key: Numerator

## Properties

- Numerator : Edm.Int32 [required]
- TextCode : Edm.String
- Text : Edm.String

# SAPB1.PredefinedTextParams (ComplexType)

## Properties

- Numerator : Edm.Int32
- TextCode : Edm.String

# SAPB1.PriceList (EntityType)

OpenType: true
Key: PriceListNo

## Properties

- RoundingMethod : SAPB1.BoRoundingMethod
- GroupNum : SAPB1.BoPriceListGroupNum
- BasePriceList : Edm.Int32
- Factor : Edm.Double
- PriceListNo : Edm.Int32 [required]
- PriceListName : Edm.String
- IsGrossPrice : SAPB1.BoYesNoEnum
- Active : SAPB1.BoYesNoEnum
- ValidFrom : Edm.DateTimeOffset
- ValidTo : Edm.DateTimeOffset
- DefaultPrimeCurrency : Edm.String
- DefaultAdditionalCurrency1 : Edm.String
- DefaultAdditionalCurrency2 : Edm.String
- RoundingRule : SAPB1.BoRoundingRule
- FixedAmount : Edm.Double

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=PriceList]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=PriceList]
- Drafts : Collection(SAPB1.Document) [Partner=PriceList]
- BlanketAgreements : Collection(SAPB1.BlanketAgreement) [Partner=PriceList2]
- CreditNotes : Collection(SAPB1.Document) [Partner=PriceList]
- PaymentTermsTypes : Collection(SAPB1.PaymentTermsType) [Partner=PriceList]
- Invoices : Collection(SAPB1.Document) [Partner=PriceList]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=PriceList]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=PriceList]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=PriceList]
- Orders : Collection(SAPB1.Document) [Partner=PriceList]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=PriceList]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=PriceList]
- Returns : Collection(SAPB1.Document) [Partner=PriceList]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=PriceList]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=PriceList]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=PriceList]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=PriceList]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=PriceList]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=PriceList]
- DownPayments : Collection(SAPB1.Document) [Partner=PriceList]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=PriceList]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=PriceList]
- ReturnRequest : Collection(SAPB1.Document) [Partner=PriceList]
- Quotations : Collection(SAPB1.Document) [Partner=PriceList]
- SelfInvoices : Collection(SAPB1.Document) [Partner=PriceList]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=PriceList]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=PriceList]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=PriceList]
- ProductTrees : Collection(SAPB1.ProductTree) [Partner=PriceList2]
- StockTransfers : Collection(SAPB1.StockTransfer) [Partner=PriceList2]
- SpecialPrices : Collection(SAPB1.SpecialPrice) [Partner=PriceList]

# SAPB1.PriceListParams (ComplexType)

## Properties

- PriceListNo : Edm.Int32

# SAPB1.ProductionOrder (EntityType)

OpenType: true
Key: AbsoluteEntry
Filtered properties: 1

## Properties

- AbsoluteEntry : Edm.Int32 [required]
- DocumentNumber : Edm.Int32
- Series : Edm.Int32
- ItemNo : Edm.String
- ProductionOrderStatus : SAPB1.BoProductionOrderStatusEnum
- ProductionOrderType : SAPB1.BoProductionOrderTypeEnum
- PlannedQuantity : Edm.Double
- CompletedQuantity : Edm.Double
- RejectedQuantity : Edm.Double
- PostingDate : Edm.DateTimeOffset
- DueDate : Edm.DateTimeOffset
- ProductionOrderOriginEntry : Edm.Int32
- ProductionOrderOriginNumber : Edm.Int32
- ProductionOrderOrigin : SAPB1.BoProductionOrderOriginEnum
- UserSignature : Edm.Int32
- Remarks : Edm.String
- ClosingDate : Edm.DateTimeOffset
- ReleaseDate : Edm.DateTimeOffset
- CustomerCode : Edm.String
- Warehouse : Edm.String
- InventoryUOM : Edm.String
- JournalRemarks : Edm.String
- TransactionNumber : Edm.Int32
- CreationDate : Edm.DateTimeOffset
- Printed : SAPB1.BoYesNoEnum
- DistributionRule : Edm.String
- Project : Edm.String
- DistributionRule2 : Edm.String
- DistributionRule3 : Edm.String
- DistributionRule4 : Edm.String
- DistributionRule5 : Edm.String
- UoMEntry : Edm.Int32
- StartDate : Edm.DateTimeOffset
- ProductDescription : Edm.String
- Priority : Edm.Int32
- RoutingDateCalculation : SAPB1.ResourceAllocationEnum
- UpdateAllocation : SAPB1.BoUpdateAllocationEnum
- SAPPassport : Edm.String
- AttachmentEntry : Edm.Int32
- PickRemarks : Edm.String
- ProductionOrderLines : Collection(SAPB1.ProductionOrderLine)
- ProductionOrdersSalesOrderLines : Collection(SAPB1.ProductionOrdersSalesOrderLine)
- ProductionOrdersStages : Collection(SAPB1.ProductionOrdersStage)
- ProductionOrdersDocumentReferences : Collection(SAPB1.ProductionOrdersDocumentReference)

## Navigation properties

- ProductTree : SAPB1.ProductTree [Partner=ProductionOrders]
- User : SAPB1.User [Partner=ProductionOrders]
- BusinessPartner : SAPB1.BusinessPartner [Partner=ProductionOrders]
- Warehouse2 : SAPB1.Warehouse [Partner=ProductionOrders]
- JournalEntry : SAPB1.JournalEntry [Partner=ProductionOrders]
- DistributionRule6 : SAPB1.DistributionRule [Partner=ProductionOrders]
- Project2 : SAPB1.Project [Partner=ProductionOrders]
- UnitOfMeasurement : SAPB1.UnitOfMeasurement [Partner=ProductionOrders]
- Attachments2 : SAPB1.Attachments2 [Partner=ProductionOrders]

# SAPB1.ProductionOrderLine (ComplexType)

OpenType: true

## Properties

- DocumentAbsoluteEntry : Edm.Int32
- LineNumber : Edm.Int32
- ItemNo : Edm.String
- BaseQuantity : Edm.Double
- PlannedQuantity : Edm.Double
- IssuedQuantity : Edm.Double
- ProductionOrderIssueType : SAPB1.BoIssueMethod
- Warehouse : Edm.String
- VisualOrder : Edm.Int32
- DistributionRule : Edm.String
- LocationCode : Edm.Int32
- Project : Edm.String
- DistributionRule2 : Edm.String
- DistributionRule3 : Edm.String
- DistributionRule4 : Edm.String
- DistributionRule5 : Edm.String
- UoMEntry : Edm.Int32
- UoMCode : Edm.Int32
- WipAccount : Edm.String
- ItemType : SAPB1.ProductionItemType
- LineText : Edm.String
- AdditionalQuantity : Edm.Double
- ResourceAllocation : SAPB1.ResourceAllocationEnum
- StartDate : Edm.DateTimeOffset
- EndDate : Edm.DateTimeOffset
- StageID : Edm.Int32
- RequiredDays : Edm.Double
- ItemName : Edm.String
- WeightOfRecycledPlastic : Edm.Double
- PlasticPackageExemptionReason : Edm.String
- SerialNumbers : Collection(SAPB1.SerialNumber)
- BatchNumbers : Collection(SAPB1.BatchNumber)

# SAPB1.ProductionOrderParams (ComplexType)

## Properties

- AbsoluteEntry : Edm.Int32

# SAPB1.ProductionOrdersDocumentReference (ComplexType)

OpenType: true

## Properties

- DocEntry : Edm.Int32
- LineNumber : Edm.Int32
- RefDocEntr : Edm.Int32
- RefDocNum : Edm.Int32
- ExtDocNum : Edm.String
- RefObjType : SAPB1.ReferencedObjectTypeEnum
- IssueDate : Edm.DateTimeOffset
- Remark : Edm.String

# SAPB1.ProductionOrdersSalesOrderLine (ComplexType)

OpenType: true

## Properties

- DocEntry : Edm.Int32
- BaseNumber : Edm.Int32
- BaseAbsEntry : Edm.Int32
- BaseLine : Edm.Int32

# SAPB1.ProductionOrdersStage (ComplexType)

OpenType: true

## Properties

- DocEntry : Edm.Int32
- StageID : Edm.Int32
- SequenceNumber : Edm.Int32
- StageEntry : Edm.Int32
- Name : Edm.String
- StartDate : Edm.DateTimeOffset
- EndDate : Edm.DateTimeOffset
- RequiredDays : Edm.Double
- WaitingDays : Edm.Double
- CalculationProportion : Edm.Double

# SAPB1.ProductTree (EntityType)

OpenType: true
Key: TreeCode

## Properties

- TreeCode : Edm.String [required]
- TreeType : SAPB1.BoItemTreeTypes
- Quantity : Edm.Double
- DistributionRule : Edm.String
- Project : Edm.String
- DistributionRule2 : Edm.String
- DistributionRule3 : Edm.String
- DistributionRule4 : Edm.String
- DistributionRule5 : Edm.String
- PriceList : Edm.Int32
- Warehouse : Edm.String
- PlanAvgProdSize : Edm.Double
- HideBOMComponentsInPrintout : SAPB1.BoYesNoEnum
- ProductDescription : Edm.String
- AttachmentEntry : Edm.Int32
- ProductTreeLines : Collection(SAPB1.ProductTreeLine)
- ProductTreeStages : Collection(SAPB1.ProductTreeStage)

## Navigation properties

- ProductionOrders : Collection(SAPB1.ProductionOrder) [Partner=ProductTree]
- Item : SAPB1.Item [Partner=ProductTrees]
- DistributionRule6 : SAPB1.DistributionRule [Partner=ProductTrees]
- Project2 : SAPB1.Project [Partner=ProductTrees]
- PriceList2 : SAPB1.PriceList [Partner=ProductTrees]
- Attachments2 : SAPB1.Attachments2 [Partner=ProductTrees]

# SAPB1.ProductTreeLine (ComplexType)

OpenType: true

## Properties

- ItemCode : Edm.String
- Quantity : Edm.Double
- Warehouse : Edm.String
- Price : Edm.Double
- Currency : Edm.String
- IssueMethod : SAPB1.BoIssueMethod
- InventoryUOM : Edm.String
- Comment : Edm.String
- ParentItem : Edm.String
- PriceList : Edm.Int32
- DistributionRule : Edm.String
- Project : Edm.String
- DistributionRule2 : Edm.String
- DistributionRule3 : Edm.String
- DistributionRule4 : Edm.String
- DistributionRule5 : Edm.String
- WipAccount : Edm.String
- ItemType : SAPB1.ProductionItemType
- LineText : Edm.String
- AdditionalQuantity : Edm.Double
- StageID : Edm.Int32
- ChildNum : Edm.Int32
- VisualOrder : Edm.Int32
- ItemName : Edm.String

# SAPB1.ProductTreeParams (ComplexType)

## Properties

- TreeCode : Edm.String

# SAPB1.ProductTreeStage (ComplexType)

OpenType: true

## Properties

- Father : Edm.String
- StageID : Edm.Int32
- SequenceNumber : Edm.Int32
- StageEntry : Edm.Int32
- Name : Edm.String
- WaitingDays : Edm.Double

# SAPB1.ProfitCenter (EntityType)

OpenType: true
Key: CenterCode

## Properties

- CenterCode : Edm.String [required]
- CenterName : Edm.String
- GroupCode : Edm.String
- InWhichDimension : Edm.Int32
- CostCenterType : Edm.String
- EffectiveFrom : Edm.DateTimeOffset
- EffectiveTo : Edm.DateTimeOffset
- Active : SAPB1.BoYesNoEnum
- CenterOwner : Edm.Int32

## Navigation properties

- Dimension : SAPB1.Dimension [Partner=ProfitCenters]
- CostCenterType2 : SAPB1.CostCenterType [Partner=ProfitCenters]
- EmployeeInfo : SAPB1.EmployeeInfo [Partner=ProfitCenters]
- EmployeesInfo : Collection(SAPB1.EmployeeInfo) [Partner=ProfitCenter]

# SAPB1.ProfitCenterParams (ComplexType)

## Properties

- CenterCode : Edm.String
- CenterName : Edm.String

# SAPB1.ProgressiveTax_Line (ComplexType)

OpenType: true

## Properties

- TaxRate : Edm.Double
- MinAmount : Edm.Double
- MaxAmount : Edm.Double

# SAPB1.Project (EntityType)

OpenType: true
Key: Code

## Properties

- Code : Edm.String [required]
- Name : Edm.String
- ValidFrom : Edm.DateTimeOffset
- ValidTo : Edm.DateTimeOffset
- Active : SAPB1.BoYesNoEnum

## Navigation properties

- ChartOfAccounts : Collection(SAPB1.ChartOfAccount) [Partner=Project]
- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=Project2]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=Project2]
- Drafts : Collection(SAPB1.Document) [Partner=Project2]
- Deposits : Collection(SAPB1.Deposit) [Partner=Project2]
- VendorPayments : Collection(SAPB1.Payment) [Partner=Project]
- ProductionOrders : Collection(SAPB1.ProductionOrder) [Partner=Project2]
- PaymentDrafts : Collection(SAPB1.Payment) [Partner=Project]
- AdditionalExpenses : Collection(SAPB1.AdditionalExpense) [Partner=Project2]
- BlanketAgreements : Collection(SAPB1.BlanketAgreement) [Partner=Project2]
- CreditNotes : Collection(SAPB1.Document) [Partner=Project2]
- Invoices : Collection(SAPB1.Document) [Partner=Project2]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=Project2]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=Project2]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=Project2]
- Orders : Collection(SAPB1.Document) [Partner=Project2]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=Project2]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=Project2]
- Returns : Collection(SAPB1.Document) [Partner=Project2]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=Project2]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=Project2]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=Project2]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=Project2]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=Project2]
- ServiceCalls : Collection(SAPB1.ServiceCall) [Partner=Project]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=Project]
- DownPayments : Collection(SAPB1.Document) [Partner=Project2]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=Project2]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=Project2]
- ReturnRequest : Collection(SAPB1.Document) [Partner=Project2]
- Quotations : Collection(SAPB1.Document) [Partner=Project2]
- ProjectManagements : Collection(SAPB1.PM_ProjectDocumentData) [Partner=Project]
- JournalEntries : Collection(SAPB1.JournalEntry) [Partner=Project]
- BudgetScenarios : Collection(SAPB1.BudgetScenario) [Partner=Project2]
- IncomingPayments : Collection(SAPB1.Payment) [Partner=Project]
- SalesOpportunities : Collection(SAPB1.SalesOpportunities) [Partner=Project]
- SelfInvoices : Collection(SAPB1.Document) [Partner=Project2]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=Project2]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=Project2]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=Project2]
- ProductTrees : Collection(SAPB1.ProductTree) [Partner=Project2]

# SAPB1.ProjectParams (ComplexType)

## Properties

- Code : Edm.String
- Name : Edm.String

# SAPB1.PurchaseTaxInvoice (EntityType)

OpenType: true
Key: DocEntry

## Properties

- DocEntry : Edm.Int32 [required]
- DocNum : Edm.Int32
- DocType : SAPB1.BoTaxInvoiceTypes
- Printed : SAPB1.BoYesNoEnum
- DocDate : Edm.DateTimeOffset
- CardCode : Edm.String
- CreationDate : Edm.DateTimeOffset
- UpdateDate : Edm.DateTimeOffset
- DocDueDate : Edm.DateTimeOffset
- Series : Edm.Int32
- Segment : Edm.Int32
- ContactPersonCode : Edm.Int32
- TaxDate : Edm.DateTimeOffset
- Comments : Edm.String
- ShipToCode : Edm.String
- Address : Edm.String
- Address2 : Edm.String
- CurrencySource : SAPB1.BoCurrencySources
- DocCurrency : Edm.String
- CustomerOrVendorRefNo : Edm.String
- CustomerOrVendorName : Edm.String
- CancelDate : Edm.DateTimeOffset
- DocumentTotal : Edm.Double
- TaxTotal : Edm.Double
- PaymentRefNo : Edm.String
- PaymentRefDate : Edm.DateTimeOffset
- AlterationRevision : Edm.Int32
- PurchaseTaxInvoiceLines : Collection(SAPB1.PurchaseTaxInvoiceLine)
- PurchaseTaxInvoiceOperationCodes : Collection(SAPB1.PurchaseTaxInvoiceOperationCode)
- PurchaseTaxInvoiceDocumentReferences : Collection(SAPB1.PurchaseTaxInvoiceDocumentReference)
- PurchaseTaxInvoiceLinkedDownPayments : Collection(SAPB1.PurchaseTaxInvoiceLinkedDownPayment)

## Navigation properties

- BusinessPartner : SAPB1.BusinessPartner [Partner=PurchaseTaxInvoices]

# SAPB1.PurchaseTaxInvoiceDocumentReference (ComplexType)

OpenType: true

## Properties

- DocEntry : Edm.Int32
- LineNumber : Edm.Int32
- ReferencedDocEntry : Edm.Int32
- ReferencedDocNumber : Edm.Int32
- ExternalReferencedDocNumber : Edm.String
- ReferencedObjectType : SAPB1.ReferencedObjectTypeEnum
- IssueDate : Edm.DateTimeOffset
- Remark : Edm.String
- CardCode : Edm.String

# SAPB1.PurchaseTaxInvoiceLine (ComplexType)

OpenType: true

## Properties

- RefEntry1 : Edm.Int32
- RefEntry2 : Edm.Int32

# SAPB1.PurchaseTaxInvoiceLinkedDownPayment (ComplexType)

OpenType: true

## Properties

- DocEntry : Edm.Int32
- LineNum : Edm.Int32
- DownPaymentType : Edm.Int32
- DownPaymentEntry : Edm.Int32
- DownPaymentNum : Edm.Int32
- PaymentType : Edm.Int32
- PaymentEntry : Edm.Int32
- PaymentNum : Edm.Int32
- PaymentTaxDate : Edm.DateTimeOffset
- TransferDate : Edm.DateTimeOffset
- TransferReference : Edm.String
- AmountToDraw : Edm.Double
- AmountToDrawFC : Edm.Double
- AmountToDrawSC : Edm.Double
- DocCurrency : Edm.String

# SAPB1.PurchaseTaxInvoiceOperationCode (ComplexType)

OpenType: true

## Properties

- OpCode : Edm.Int32

# SAPB1.PurchaseTaxInvoiceParams (ComplexType)

## Properties

- DocEntry : Edm.Int32

# SAPB1.PWPExtendedProperties (ComplexType)

## Properties

- IsEncrypted : SAPB1.BoYesNoEnum

# SAPB1.QRCodeData (ComplexType)

## Properties

- ObjectType : Edm.Int32
- ObjectAbsEntry : Edm.String
- FieldName : Edm.String
- QRCodeText : Edm.String

# SAPB1.QueryAuthGroup (EntityType)

Key: AuthGroupId

## Properties

- AuthGroupCode : Edm.String
- AuthGroupDes : Edm.String
- AuthGroupId : Edm.Int32 [required]
- CategoryGroupCollection : Collection(SAPB1.CategoryGroup)

# SAPB1.QueryAuthGroupParams (ComplexType)

## Properties

- AuthGroupId : Edm.Int32
- AuthGroupCode : Edm.String

# SAPB1.QueryCategory (EntityType)

OpenType: true
Key: Code

## Properties

- Code : Edm.Int32 [required]
- Name : Edm.String
- Permissions : Edm.String

## Navigation properties

- UserQueries : Collection(SAPB1.UserQuery) [Partner=QueryCategory2]

# SAPB1.QueryCategoryParams (ComplexType)

## Properties

- Code : Edm.Int32

# SAPB1.Queue (EntityType)

OpenType: true
Key: QueueID

## Properties

- QueueID : Edm.String [required]
- Description : Edm.String
- Inactive : SAPB1.BoYesNoEnum
- QueueManager : Edm.Int32
- QueueEmail : Edm.String
- QueueMembers : Collection(SAPB1.QueueMember)

## Navigation properties

- ServiceCalls : Collection(SAPB1.ServiceCall) [Partner=Queue2]
- User : SAPB1.User [Partner=Queue]

# SAPB1.QueueMember (ComplexType)

OpenType: true

## Properties

- QueueID : Edm.String
- MemberUserID : Edm.Int32

# SAPB1.QueueParams (ComplexType)

## Properties

- QueueID : Edm.String

# SAPB1.RclRecurringExecutionParams (ComplexType)

## Properties

- OnError : SAPB1.RclRecurringExecutionHandlingEnum

# SAPB1.RclRecurringTransaction (ComplexType)

## Properties

- TransactionID : Edm.Int32
- TemplateID : Edm.Int32
- Instance : Edm.Int32
- PlannedDate : Edm.DateTimeOffset
- Status : SAPB1.RclRecurringTransactionStatusEnum
- DocType : Edm.String
- DocEntry : Edm.Int32

# SAPB1.RclRecurringTransactionParams (ComplexType)

## Properties

- TransactionID : Edm.Int32
- PlannedDate : Edm.DateTimeOffset

# SAPB1.Recipient (ComplexType)

## Properties

- UserCode : Edm.String
- UserType : SAPB1.BoMsgRcpTypes
- NameTo : Edm.String
- SendEmail : SAPB1.BoYesNoEnum
- EmailAddress : Edm.String
- SendSMS : SAPB1.BoYesNoEnum
- CellularNumber : Edm.String
- SendFax : SAPB1.BoYesNoEnum
- FaxNumber : Edm.String
- SendInternal : SAPB1.BoYesNoEnum

# SAPB1.ReconciliationBankStatementLine (ComplexType)

## Properties

- BankStatementAccountCode : Edm.String
- Sequence : Edm.Int32
- Date : Edm.DateTimeOffset
- Ref1 : Edm.String
- Amount : Edm.Double
- Details : Edm.String

# SAPB1.ReconciliationJournalEntryLine (ComplexType)

## Properties

- TransactionNumber : Edm.Int32
- LineNumber : Edm.Int32
- PostingDate : Edm.DateTimeOffset
- DueDate : Edm.DateTimeOffset
- Ref1 : Edm.String
- Ref2 : Edm.String
- Ref3 : Edm.String
- DebitAmount : Edm.Double
- CreditAmount : Edm.Double
- Details : Edm.String

# SAPB1.RecordsetParams (ComplexType)

## Properties

- Query : Edm.String

# SAPB1.RecurringPostings (EntityType)

Key: Code, Instance

## Properties

- Code : Edm.String [required]
- Description : Edm.String
- Instance : Edm.Int32 [required]
- Reference1 : Edm.String
- Reference2 : Edm.String
- Reference3 : Edm.String
- TransactionCode : Edm.String
- Remarks : Edm.String
- Frequency : SAPB1.BoFrequencyTypeEnum
- SubFrequency : SAPB1.BoSubFrequencyTypeEnum
- NextExecution : Edm.DateTimeOffset
- StampTax : SAPB1.BoYesNoEnum
- AutomaticVAT : SAPB1.BoYesNoEnum
- ManageWTax : SAPB1.BoYesNoEnum
- DeferredTax : SAPB1.BoYesNoEnum
- ValidUntil : SAPB1.BoYesNoEnum
- ValidUntilDate : Edm.DateTimeOffset
- RecurringPostingsLineCollection : Collection(SAPB1.RecurringPostingsLine)
- RecurringPostingsDocumentReferenceCollection : Collection(SAPB1.RecurringPostingsDocumentReference)

# SAPB1.RecurringPostingsDocumentReference (ComplexType)

## Properties

- RcrCode : Edm.String
- LineNumber : Edm.Int32
- ReferencedDocEntry : Edm.Int32
- ReferencedDocNumber : Edm.Int32
- ExternalReferencedDocNumber : Edm.String
- ReferencedObjectType : SAPB1.ReferencedObjectTypeEnum
- IssueDate : Edm.DateTimeOffset
- Remark : Edm.String

# SAPB1.RecurringPostingsLine (ComplexType)

## Properties

- RcrCode : Edm.String
- LineNumber : Edm.Int32
- ControlAccount : Edm.String
- AccountCode : Edm.String
- AccountName : Edm.String
- Debit : Edm.Double
- Credit : Edm.Double
- Currency : Edm.String
- TaxGroup : Edm.String
- VatLine : SAPB1.BoYesNoEnum
- DistributionRule : Edm.String
- TaxPostingAccount : SAPB1.BoTaxPostingAccountTypeEnum
- TaxCode : Edm.String
- CostingCode1 : Edm.String
- CostingCode2 : Edm.String
- CostingCode3 : Edm.String
- CostingCode4 : Edm.String
- CostingCode5 : Edm.String
- WTaxLiable : SAPB1.BoYesNoEnum
- WTaxLine : SAPB1.BoYesNoEnum
- ProjectCode : Edm.String
- CostElementCode : Edm.String

# SAPB1.RecurringPostingsParams (ComplexType)

## Properties

- Code : Edm.String
- Instance : Edm.Int32
- Description : Edm.String

# SAPB1.RecurringTransactionTemplate (EntityType)

Key: AbsoluteEntry

## Properties

- AbsoluteEntry : Edm.Int32 [required]
- TemplateCode : Edm.String
- TemplateDescription : Edm.String
- DocumentObjectType : SAPB1.DocumentObjectTypeEnum
- DraftEntry : Edm.Int32
- Frequency : SAPB1.RecurringTransactionTemplateFrequencyEnum
- Remind : SAPB1.RecurringTransactionTemplateRemindEnum
- StartDate : Edm.DateTimeOffset
- EndDate : Edm.DateTimeOffset
- PriceUpdate : SAPB1.BoYesNoEnum
- CardCode : Edm.String

## Navigation properties

- BusinessPartner : SAPB1.BusinessPartner [Partner=RecurringTransactionTemplates]

# SAPB1.RecurringTransactionTemplateParams (ComplexType)

## Properties

- AbsoluteEntry : Edm.Int32

# SAPB1.RefreshPathsDocuments (ComplexType)

## Properties

- AttachmentsFolderPath : Edm.String

# SAPB1.RelatedDocument (ComplexType)

## Properties

- DocType : SAPB1.RelatedDocumentTypeEnum
- AbsEntry : Edm.Int32
- UUID : Edm.String
- DocTye : SAPB1.RelatedDocumentTypeEnum
- AbsEnry : Edm.Int32

# SAPB1.Relationship (EntityType)

OpenType: true
Key: RelationshipCode

## Properties

- RelationshipDescription : Edm.String
- RelationshipCode : Edm.Int32 [required]

## Navigation properties

- PartnersSetups : Collection(SAPB1.PartnersSetup) [Partner=Relationship]

# SAPB1.RelationshipParams (ComplexType)

## Properties

- RelationshipCode : Edm.Int32

# SAPB1.ReportInputParams (ComplexType)

## Properties

- ReportLayoutMenuID : Edm.String

# SAPB1.ReportLayout (ComplexType)

## Properties

- Name : Edm.String
- Author : Edm.String
- Remarks : Edm.String
- Width : Edm.Int32
- Height : Edm.Int32
- LeftMargin : Edm.Int32
- RightMargin : Edm.Int32
- TopMargin : Edm.Int32
- BottomMargin : Edm.Int32
- Editable : SAPB1.BoYesNoEnum
- PaperSize : Edm.String
- Orientation : SAPB1.BoOrientationEnum
- GridSize : Edm.Int32
- GridType : SAPB1.BoGridTypeEnum
- ShowGrid : SAPB1.BoYesNoEnum
- SnapToGrid : SAPB1.BoYesNoEnum
- Picture : Edm.String
- TypeCode : Edm.String
- ForeignLanguageReport : SAPB1.BoYesNoEnum
- Sortable : SAPB1.BoYesNoEnum
- LeaderReport : Edm.String
- FollowUpReport : Edm.String
- ConvertFontInPrintPreview : SAPB1.BoYesNoEnum
- PreviewPrintingFont : Edm.String
- ChangeFontSizeInPreview : Edm.Int32
- ConvertFontForEMail : SAPB1.BoYesNoEnum
- EMailFont : Edm.String
- ChangeFontSizeForEMail : Edm.Int32
- Query : Edm.String
- QueryType : SAPB1.BoQueryTypeEnum
- language : Edm.Int32
- ImpExpObjCode : Edm.Int32
- ExtensionName : Edm.String
- ExtensionErrorAction : SAPB1.BoExtensionErrorActionEnum
- RepetitiveAreasNumber : Edm.Int32
- AllignFooterToBottom : SAPB1.BoYesNoEnum
- LayoutCode : Edm.String
- Category : SAPB1.ReportLayoutCategoryEnum
- Printer : Edm.String
- PrinterFirstPage : Edm.String
- NumberOfCopies : Edm.Int32
- Localization : Edm.String
- UseFirstPrinter : SAPB1.BoYesNoEnum
- B1Version : Edm.String
- CRVersion : Edm.String
- TypeDetail : Edm.String
- ReportLayoutItems : Collection(SAPB1.ReportLayoutItem)
- ReportLayout_TranslationLines : Collection(SAPB1.ReportLayout_TranslationLine)

# SAPB1.ReportLayout_TranslationLine (ComplexType)

## Properties

- DocEntry : Edm.String
- LineNumber : Edm.Int32
- DocName : Edm.String
- LanguageCode : Edm.Int32
- CreateDate : Edm.DateTimeOffset
- UpdateDate : Edm.DateTimeOffset
- CreateTime : Edm.Int32
- UpdateTime : Edm.Int32

# SAPB1.ReportLayoutItem (ComplexType)

## Properties

- FieldIdentifier : Edm.String
- ParentType : Edm.Int32
- Type : SAPB1.BoReportLayoutItemTypeEnum
- Visible : SAPB1.BoYesNoEnum
- SuppressZeros : SAPB1.BoYesNoEnum
- Left : Edm.Int32
- Top : Edm.Int32
- Width : Edm.Int32
- Height : Edm.Int32
- LeftMargin : Edm.Int32
- RightMargin : Edm.Int32
- TopMargin : Edm.Int32
- BottomMargin : Edm.Int32
- LeftBorderLineThickness : Edm.Int32
- RightBorderLineThickness : Edm.Int32
- TopBorderLineThickness : Edm.Int32
- BottomBorderLineThickness : Edm.Int32
- ShadowThickness : Edm.Int32
- BackgroundRed : Edm.Int32
- BackgroundGreen : Edm.Int32
- BackgroundBlue : Edm.Int32
- TextRed : Edm.Int32
- TextGreen : Edm.Int32
- TextBlue : Edm.Int32
- HighlightRed : Edm.Int32
- HighlightGreen : Edm.Int32
- HighlightBlue : Edm.Int32
- BorderRed : Edm.Int32
- BorderGreen : Edm.Int32
- BorderBlue : Edm.Int32
- GroupNumber : Edm.Int32
- FontName : Edm.String
- FontSize : Edm.Int32
- TextStyle : Edm.Int32
- HorizontalAlignment : SAPB1.BoHorizontalAlignmentEnum
- LineBreak : SAPB1.BoLineBreakEnum
- PictureSize : SAPB1.BoPictureSizeEnum
- DataSource : SAPB1.BoDataSourceEnum
- String : Edm.String
- VariableNumber : Edm.Int32
- TableName : Edm.String
- FieldName : Edm.String
- DisplayDescription : SAPB1.BoYesNoEnum
- Editable : Edm.Int32
- ItemNumber : Edm.Int32
- VerticalAlignment : SAPB1.BoVerticalAlignmentEnum
- SortLevel : Edm.Int32
- ReverseSort : SAPB1.BoYesNoEnum
- SortType : SAPB1.BoSortTypeEnum
- Unique : SAPB1.BoYesNoEnum
- SetAsGroup : SAPB1.BoYesNoEnum
- NewPage : SAPB1.BoYesNoEnum
- PrintAsBarCode : SAPB1.BoYesNoEnum
- LinkToField : Edm.String
- BarCodeStandard : SAPB1.BoBarCodeStandardEnum
- DisplayTotalAsAWord : SAPB1.BoYesNoEnum
- BlockFontChange : SAPB1.BoYesNoEnum
- ParentIndex : Edm.Int32
- ItemIndex : Edm.Int32
- StringLength : Edm.Int32
- StringFiller : Edm.String
- RelateToField : Edm.String
- NextSegmentItemNumber : Edm.String
- HeightAdjustments : SAPB1.BoYesNoEnum
- DuplicateRepetitiveArea : SAPB1.BoYesNoEnum
- NumberOfLinesInRepetitiveArea : Edm.Int32
- DistanceToRepetitiveDuplicate : Edm.Int32
- HideRepetitiveAreaIfEmpty : SAPB1.BoYesNoEnum
- DisplayRepetitiveAreaFooterOnAllPages : SAPB1.BoYesNoEnum

# SAPB1.ReportLayoutParams (ComplexType)

## Properties

- LayoutCode : Edm.String
- LayoutName : Edm.String
- Category : SAPB1.ReportLayoutCategoryEnum

# SAPB1.ReportLayoutPrintParams (ComplexType)

## Properties

- LayoutCode : Edm.String
- DocEntry : Edm.Int32

# SAPB1.ReportParams (ComplexType)

## Properties

- ReportCode : Edm.String
- UserID : Edm.Int32
- CardCode : Edm.String

# SAPB1.ReportType (EntityType)

Key: TypeCode

## Properties

- TypeCode : Edm.String [required]
- TypeName : Edm.String
- DefaultReportLayout : Edm.String
- AddonName : Edm.String
- AddonFormType : Edm.String
- MenuID : Edm.String

# SAPB1.ReportTypeParams (ComplexType)

## Properties

- TypeCode : Edm.String
- TypeName : Edm.String
- AddonName : Edm.String
- AddonFormType : Edm.String
- MenuID : Edm.String

# SAPB1.Resource (EntityType)

OpenType: true
Key: Code

## Properties

- Code : Edm.String [required]
- VisCode : Edm.String
- Series : Edm.Int32
- Number : Edm.Int32
- CodeBar : Edm.String
- Name : Edm.String
- ForeignName : Edm.String
- Type : SAPB1.ResourceTypeEnum
- Group : Edm.Int32
- UnitOfMeasure : Edm.String
- IssueMethod : SAPB1.ResourceIssueMethodEnum
- Cost1 : Edm.Double
- Cost2 : Edm.Double
- Cost3 : Edm.Double
- Cost4 : Edm.Double
- Cost5 : Edm.Double
- Cost6 : Edm.Double
- Cost7 : Edm.Double
- Cost8 : Edm.Double
- Cost9 : Edm.Double
- Cost10 : Edm.Double
- Active : SAPB1.BoYesNoEnum
- ActiveFrom : Edm.DateTimeOffset
- ActiveTo : Edm.DateTimeOffset
- Inactive : SAPB1.BoYesNoEnum
- InactiveFrom : Edm.DateTimeOffset
- InactiveTo : Edm.DateTimeOffset
- DefaultWarehouse : Edm.String
- Picture : Edm.String
- Remarks : Edm.String
- Property1 : SAPB1.BoYesNoEnum
- Property2 : SAPB1.BoYesNoEnum
- Property3 : SAPB1.BoYesNoEnum
- Property4 : SAPB1.BoYesNoEnum
- Property5 : SAPB1.BoYesNoEnum
- Property6 : SAPB1.BoYesNoEnum
- Property7 : SAPB1.BoYesNoEnum
- Property8 : SAPB1.BoYesNoEnum
- Property9 : SAPB1.BoYesNoEnum
- Property10 : SAPB1.BoYesNoEnum
- Property11 : SAPB1.BoYesNoEnum
- Property12 : SAPB1.BoYesNoEnum
- Property13 : SAPB1.BoYesNoEnum
- Property14 : SAPB1.BoYesNoEnum
- Property15 : SAPB1.BoYesNoEnum
- Property16 : SAPB1.BoYesNoEnum
- Property17 : SAPB1.BoYesNoEnum
- Property18 : SAPB1.BoYesNoEnum
- Property19 : SAPB1.BoYesNoEnum
- Property20 : SAPB1.BoYesNoEnum
- Property21 : SAPB1.BoYesNoEnum
- Property22 : SAPB1.BoYesNoEnum
- Property23 : SAPB1.BoYesNoEnum
- Property24 : SAPB1.BoYesNoEnum
- Property25 : SAPB1.BoYesNoEnum
- Property26 : SAPB1.BoYesNoEnum
- Property27 : SAPB1.BoYesNoEnum
- Property28 : SAPB1.BoYesNoEnum
- Property29 : SAPB1.BoYesNoEnum
- Property30 : SAPB1.BoYesNoEnum
- Property31 : SAPB1.BoYesNoEnum
- Property32 : SAPB1.BoYesNoEnum
- Property33 : SAPB1.BoYesNoEnum
- Property34 : SAPB1.BoYesNoEnum
- Property35 : SAPB1.BoYesNoEnum
- Property36 : SAPB1.BoYesNoEnum
- Property37 : SAPB1.BoYesNoEnum
- Property38 : SAPB1.BoYesNoEnum
- Property39 : SAPB1.BoYesNoEnum
- Property40 : SAPB1.BoYesNoEnum
- Property41 : SAPB1.BoYesNoEnum
- Property42 : SAPB1.BoYesNoEnum
- Property43 : SAPB1.BoYesNoEnum
- Property44 : SAPB1.BoYesNoEnum
- Property45 : SAPB1.BoYesNoEnum
- Property46 : SAPB1.BoYesNoEnum
- Property47 : SAPB1.BoYesNoEnum
- Property48 : SAPB1.BoYesNoEnum
- Property49 : SAPB1.BoYesNoEnum
- Property50 : SAPB1.BoYesNoEnum
- Property51 : SAPB1.BoYesNoEnum
- Property52 : SAPB1.BoYesNoEnum
- Property53 : SAPB1.BoYesNoEnum
- Property54 : SAPB1.BoYesNoEnum
- Property55 : SAPB1.BoYesNoEnum
- Property56 : SAPB1.BoYesNoEnum
- Property57 : SAPB1.BoYesNoEnum
- Property58 : SAPB1.BoYesNoEnum
- Property59 : SAPB1.BoYesNoEnum
- Property60 : SAPB1.BoYesNoEnum
- Property61 : SAPB1.BoYesNoEnum
- Property62 : SAPB1.BoYesNoEnum
- Property63 : SAPB1.BoYesNoEnum
- Property64 : SAPB1.BoYesNoEnum
- ActiveRemarks : Edm.String
- InactiveRemarks : Edm.String
- AttachmentEntry : Edm.Int32
- UnitsPerTime : Edm.Int32
- TimePerUnits : Edm.Int32
- Allocation : SAPB1.ResourceAllocationEnum
- LinkedItem : Edm.String
- RelevantForSingleRun1 : SAPB1.BoYesNoEnum
- RelevantForSingleRun2 : SAPB1.BoYesNoEnum
- RelevantForSingleRun3 : SAPB1.BoYesNoEnum
- RelevantForSingleRun4 : SAPB1.BoYesNoEnum
- ResourceWarehouses : Collection(SAPB1.ResourceWarehouse)
- ResourceFixedAssets : Collection(SAPB1.ResourceFixedAsset)
- ResourceEmployees : Collection(SAPB1.ResourceEmployee)
- ResourceDailyCapacities : Collection(SAPB1.ResourceDailyCapacity)

## Navigation properties

- ResourceCapacities : Collection(SAPB1.ResourceCapacity) [Partner=Resource]
- ResourceGroup : SAPB1.ResourceGroup [Partner=Resources]
- Item : SAPB1.Item [Partner=Resources]
- Items : Collection(SAPB1.Item) [Partner=Resource]

# SAPB1.ResourceCapacity (EntityType)

Key: Id

## Properties

- Id : Edm.Int32 [required]
- Code : Edm.String
- Warehouse : Edm.String
- Date : Edm.DateTimeOffset
- Type : SAPB1.ResourceCapacityTypeEnum
- Capacity : Edm.Double
- SourceType : SAPB1.ResourceCapacitySourceTypeEnum
- SourceEntry : Edm.Int32
- SourceLineNum : Edm.Int32
- BaseType : SAPB1.ResourceCapacityBaseTypeEnum
- BaseEntry : Edm.Int32
- BaseLineNum : Edm.Int32
- Action : SAPB1.ResourceCapacityActionEnum
- OwningType : SAPB1.ResourceCapacityOwningTypeEnum
- OwningEntry : Edm.Int32
- OwningLineNum : Edm.Int32
- RevertedType : SAPB1.ResourceCapacityRevertedTypeEnum
- RevertedEntry : Edm.Int32
- RevertedLineNum : Edm.Int32
- MemoSource : SAPB1.ResourceCapacityMemoSourceEnum
- Memo : Edm.String
- SingleRunCapacity : Edm.Double
- SingleRunMemoSource : SAPB1.ResourceCapacityMemoSourceEnum
- SingleRunMemo : Edm.String

## Navigation properties

- Resource : SAPB1.Resource [Partner=ResourceCapacities]
- Warehouse2 : SAPB1.Warehouse [Partner=ResourceCapacities]

# SAPB1.ResourceCapacityParams (ComplexType)

## Properties

- Id : Edm.Int32
- Code : Edm.String
- Warehouse : Edm.String
- Date : Edm.DateTimeOffset
- Type : SAPB1.ResourceCapacityTypeEnum
- Capacity : Edm.Double
- SourceType : SAPB1.ResourceCapacitySourceTypeEnum
- SourceEntry : Edm.Int32
- SourceLineNum : Edm.Int32
- BaseType : SAPB1.ResourceCapacityBaseTypeEnum
- BaseEntry : Edm.Int32
- BaseLineNum : Edm.Int32
- Action : SAPB1.ResourceCapacityActionEnum
- OwningType : SAPB1.ResourceCapacityOwningTypeEnum
- OwningEntry : Edm.Int32
- OwningLineNum : Edm.Int32
- RevertedType : SAPB1.ResourceCapacityRevertedTypeEnum
- RevertedEntry : Edm.Int32
- RevertedLineNum : Edm.Int32
- MemoSource : SAPB1.ResourceCapacityMemoSourceEnum
- Memo : Edm.String
- SingleRunCapacity : Edm.Double
- SingleRunMemoSource : SAPB1.ResourceCapacityMemoSourceEnum
- SingleRunMemo : Edm.String

# SAPB1.ResourceCapacityWithFilterParams (ComplexType)

## Properties

- Code : Edm.String
- Warehouse : Edm.String
- Date : Edm.DateTimeOffset
- Type : SAPB1.ResourceCapacityTypeEnum

# SAPB1.ResourceDailyCapacity (ComplexType)

## Properties

- Code : Edm.String
- Weekday : SAPB1.ResourceDailyCapacityWeekdayEnum
- Factor1 : Edm.Double
- Factor2 : Edm.Double
- Factor3 : Edm.Double
- Factor4 : Edm.Double
- Total : Edm.Double
- Remarks : Edm.String
- SingleRun : Edm.Double

# SAPB1.ResourceEmployee (ComplexType)

## Properties

- Code : Edm.String
- Employee : Edm.String

# SAPB1.ResourceFixedAsset (ComplexType)

## Properties

- Code : Edm.String
- ItemCode : Edm.String

# SAPB1.ResourceGroup (EntityType)

Key: Code

## Properties

- Code : Edm.Int32 [required]
- Name : Edm.String
- Type : SAPB1.ResourceTypeEnum
- CostName1 : Edm.String
- Cost1 : Edm.Double
- CostName2 : Edm.String
- Cost2 : Edm.Double
- CostName3 : Edm.String
- Cost3 : Edm.Double
- CostName4 : Edm.String
- Cost4 : Edm.Double
- CostName5 : Edm.String
- Cost5 : Edm.Double
- CostName6 : Edm.String
- Cost6 : Edm.Double
- CostName7 : Edm.String
- Cost7 : Edm.Double
- CostName8 : Edm.String
- Cost8 : Edm.Double
- CostName9 : Edm.String
- Cost9 : Edm.Double
- CostName10 : Edm.String
- Cost10 : Edm.Double
- NumOfUnitsText : Edm.String

## Navigation properties

- Resources : Collection(SAPB1.Resource) [Partner=ResourceGroup]

# SAPB1.ResourceGroupParams (ComplexType)

## Properties

- Code : Edm.Int32
- Name : Edm.String

# SAPB1.ResourceParams (ComplexType)

## Properties

- Code : Edm.String

# SAPB1.ResourceProperty (EntityType)

Key: Code

## Properties

- Code : Edm.Int32 [required]
- Name : Edm.String

# SAPB1.ResourcePropertyParams (ComplexType)

## Properties

- Code : Edm.Int32
- Name : Edm.String

# SAPB1.ResourceWarehouse (ComplexType)

OpenType: true

## Properties

- Code : Edm.String
- Warehouse : Edm.String
- Locked : SAPB1.BoYesNoEnum

# SAPB1.RetornoCode (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- OccurenceCode : Edm.Int32
- MovementCode : Edm.Int32
- BoeStatus : SAPB1.BoBoeStatus
- Description : Edm.String
- Color : Edm.Int32
- FileFormat : Edm.String
- BankCode : Edm.String

# SAPB1.RetornoCodeParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- OccurenceCode : Edm.Int32
- MovementCode : Edm.Int32
- BoeStatus : SAPB1.BoBoeStatus
- Description : Edm.String
- Color : Edm.Int32
- FileFormat : Edm.String
- BankCode : Edm.String

# SAPB1.RoundedData (ComplexType)

## Properties

- Value : Edm.Double

# SAPB1.RouteStage (EntityType)

Key: InternalNumber

## Properties

- InternalNumber : Edm.Int32 [required]
- Code : Edm.String
- Description : Edm.String
- CreationDate : Edm.DateTimeOffset
- GenerationTime : Edm.TimeOfDay
- DateOfUpdate : Edm.DateTimeOffset

# SAPB1.RouteStageParams (ComplexType)

## Properties

- InternalNumber : Edm.Int32
- Code : Edm.String
- Description : Edm.String
- CreationDate : Edm.DateTimeOffset
- GenerationTime : Edm.TimeOfDay
- DateOfUpdate : Edm.DateTimeOffset

# SAPB1.RoutingDateCalculationInput (ComplexType)

## Properties

- ResourceCode : Edm.String
- WarehouseCode : Edm.String
- CalculateFromDate : Edm.DateTimeOffset
- CalculateUntilDate : Edm.DateTimeOffset
- CapacitySum : Edm.Double
- FirstDateProportion : Edm.Double
- ResourceAlloc : SAPB1.ResourceAllocationEnum
- WORObjAbs : Edm.Int32
- WORLine : Edm.Int32

# SAPB1.RoutingDateCalculationOutput (ComplexType)

## Properties

- ResultDate : Edm.DateTimeOffset
- Proportion : Edm.Double

# SAPB1.SalesAppSetting (ComplexType)

## Properties

- Code : Edm.Int32
- Name : Edm.String
- AdvancedDashBoard : Edm.Int32
- CustomerAdvancedDashBoard : Edm.Int32

# SAPB1.SalesAppSettingParams (ComplexType)

## Properties

- Code : Edm.Int32
- Name : Edm.String

# SAPB1.SalesForecast (EntityType)

OpenType: true
Key: Numerator

## Properties

- ForecastStartDate : Edm.DateTimeOffset
- ForecastEndDate : Edm.DateTimeOffset
- ForecastCode : Edm.String
- ForecastName : Edm.String
- Numerator : Edm.Int32 [required]
- View : SAPB1.BoForecastViewType
- SalesForecastLines : Collection(SAPB1.SalesForecastLine)

# SAPB1.SalesForecastLine (ComplexType)

OpenType: true

## Properties

- Quantity : Edm.Double
- ForecastedDay : Edm.DateTimeOffset
- ItemNo : Edm.String
- Warehouse : Edm.String

# SAPB1.SalesForecastParams (ComplexType)

## Properties

- Numerator : Edm.Int32

# SAPB1.SalesOpportunities (EntityType)

OpenType: true
Key: SequentialNo
Filtered properties: 1

## Properties

- SequentialNo : Edm.Int32 [required]
- CardCode : Edm.String
- SalesPerson : Edm.Int32
- ContactPerson : Edm.Int32
- Source : Edm.Int32
- InterestField1 : Edm.Int32
- InterestField2 : Edm.Int32
- InterestField3 : Edm.Int32
- InterestLevel : Edm.Int32
- StartDate : Edm.DateTimeOffset
- PredictedClosingDate : Edm.DateTimeOffset
- MaxLocalTotal : Edm.Double
- MaxSystemTotal : Edm.Double
- WeightedSumLC : Edm.Double
- WeightedSumSC : Edm.Double
- GrossProfit : Edm.Double
- GrossProfitTotalLocal : Edm.Double
- GrossProfitTotalSystem : Edm.Double
- Remarks : Edm.String
- Status : SAPB1.BoSoOsStatus
- ReasonForClosing : Edm.Int32
- TotalAmountLocal : Edm.Double
- TotalAmounSystem : Edm.Double
- ClosingGrossProfitLocal : Edm.Double
- ClosingGrossProfitSystem : Edm.Double
- ClosingPercentage : Edm.Double
- CurrentStageNo : Edm.Int32
- CurrentStageNumber : Edm.Int32
- OpportunityName : Edm.String
- Industry : Edm.Int32
- LinkedDocumentType : Edm.String
- DataOwnershipfield : Edm.Int32
- StatusRemarks : Edm.String
- ProjectCode : Edm.String
- BPChanelName : Edm.String
- UserSignature : Edm.Int32
- CustomerName : Edm.String
- DocumentCheckbox : Edm.String
- LinkedDocumentNumber : Edm.Int32
- Territory : Edm.Int32
- ClosingDate : Edm.DateTimeOffset
- BPChannelContact : Edm.Int32
- BPChanelCode : Edm.String
- ClosingType : SAPB1.BoSoClosedInTypes
- AttachmentEntry : Edm.Int32
- OpportunityType : SAPB1.OpportunityTypeEnum
- UpdateDate : Edm.DateTimeOffset
- UpdateTime : Edm.TimeOfDay
- SalesOpportunitiesLines : Collection(SAPB1.SalesOpportunitiesLine)
- SalesOpportunitiesCompetition : Collection(SAPB1.SalesOpportunitiesCompetitionItem)
- SalesOpportunitiesPartners : Collection(SAPB1.SalesOpportunitiesPartner)
- SalesOpportunitiesInterests : Collection(SAPB1.SalesOpportunitiesInterest)
- SalesOpportunitiesReasons : Collection(SAPB1.SalesOpportunitiesReason)

## Navigation properties

- BusinessPartner : SAPB1.BusinessPartner [Partner=SalesOpportunities]
- SalesPerson2 : SAPB1.SalesPerson [Partner=SalesOpportunities]
- SalesOpportunitySourceSetup : SAPB1.SalesOpportunitySourceSetup [Partner=SalesOpportunities]
- SalesOpportunityInterestSetup : SAPB1.SalesOpportunityInterestSetup [Partner=SalesOpportunities]
- SalesOpportunityReasonSetup : SAPB1.SalesOpportunityReasonSetup [Partner=SalesOpportunities]
- SalesStage : SAPB1.SalesStage [Partner=SalesOpportunities]
- Industry2 : SAPB1.Industry [Partner=SalesOpportunities]
- EmployeeInfo : SAPB1.EmployeeInfo [Partner=SalesOpportunities]
- Project : SAPB1.Project [Partner=SalesOpportunities]
- User : SAPB1.User [Partner=SalesOpportunities]
- Territory2 : SAPB1.Territory [Partner=SalesOpportunities]

# SAPB1.SalesOpportunitiesCompetitionItem (ComplexType)

OpenType: true

## Properties

- RowNo : Edm.Int32
- Competition : Edm.Int32
- Details : Edm.String
- SequenceNo : Edm.Int32
- WonOrLost : Edm.String
- ThreatLevel : SAPB1.ThreatLevelEnum

# SAPB1.SalesOpportunitiesInterest (ComplexType)

OpenType: true

## Properties

- RowNo : Edm.Int32
- SequenceNo : Edm.Int32
- PrimaryInterest : SAPB1.BoYesNoEnum
- InterestId : Edm.Int32

# SAPB1.SalesOpportunitiesLine (ComplexType)

OpenType: true

## Properties

- LineNum : Edm.Int32
- SalesPerson : Edm.Int32
- StartDate : Edm.DateTimeOffset
- ClosingDate : Edm.DateTimeOffset
- StageKey : Edm.Int32
- PercentageRate : Edm.Double
- MaxLocalTotal : Edm.Double
- MaxSystemTotal : Edm.Double
- Remarks : Edm.String
- Contact : SAPB1.BoYesNoEnum
- Status : SAPB1.BoSoStatus
- WeightedAmountLocal : Edm.Double
- WeightedAmountSystem : Edm.Double
- DocumentNumber : Edm.Int32
- DocumentType : SAPB1.BoAPARDocumentTypes
- DocumentCheckbox : SAPB1.BoYesNoEnum
- ContactPerson : Edm.Int32
- BPChanelName : Edm.String
- BPChanelCode : Edm.String
- SequenceNo : Edm.Int32
- DataOwnershipfield : Edm.Int32
- BPChannelContact : Edm.Int32

# SAPB1.SalesOpportunitiesParams (ComplexType)

## Properties

- SequentialNo : Edm.Int32

# SAPB1.SalesOpportunitiesPartner (ComplexType)

OpenType: true

## Properties

- RowNo : Edm.Int32
- Partners : Edm.Int32
- Details : Edm.String
- RelationshipCode : Edm.Int32
- SequenceNo : Edm.Int32

# SAPB1.SalesOpportunitiesReason (ComplexType)

OpenType: true

## Properties

- RowNo : Edm.Int32
- SequenceNo : Edm.Int32
- Reason : Edm.Int32

# SAPB1.SalesOpportunityCompetitorSetup (EntityType)

Key: SequenceNo

## Properties

- SequenceNo : Edm.Int32 [required]
- Name : Edm.String
- ThreatLevel : SAPB1.ThreatLevelEnum
- Details : Edm.String

# SAPB1.SalesOpportunityCompetitorSetupParams (ComplexType)

## Properties

- SequenceNo : Edm.Int32
- Name : Edm.String
- ThreatLevel : SAPB1.ThreatLevelEnum

# SAPB1.SalesOpportunityInterestSetup (EntityType)

Key: SequenceNo

## Properties

- SequenceNo : Edm.Int32 [required]
- Description : Edm.String
- Sort : Edm.Int32

## Navigation properties

- SalesOpportunities : Collection(SAPB1.SalesOpportunities) [Partner=SalesOpportunityInterestSetup]

# SAPB1.SalesOpportunityInterestSetupParams (ComplexType)

## Properties

- SequenceNo : Edm.Int32
- Description : Edm.String

# SAPB1.SalesOpportunityReasonSetup (EntityType)

Key: SequenceNo

## Properties

- SequenceNo : Edm.Int32 [required]
- Description : Edm.String
- Sort : Edm.Int32

## Navigation properties

- SalesOpportunities : Collection(SAPB1.SalesOpportunities) [Partner=SalesOpportunityReasonSetup]

# SAPB1.SalesOpportunityReasonSetupParams (ComplexType)

## Properties

- SequenceNo : Edm.Int32
- Description : Edm.String

# SAPB1.SalesOpportunitySourceSetup (EntityType)

Key: SequenceNo

## Properties

- SequenceNo : Edm.Int32 [required]
- Description : Edm.String
- Sort : Edm.Int32

## Navigation properties

- SalesOpportunities : Collection(SAPB1.SalesOpportunities) [Partner=SalesOpportunitySourceSetup]

# SAPB1.SalesOpportunitySourceSetupParams (ComplexType)

## Properties

- SequenceNo : Edm.Int32
- Description : Edm.String

# SAPB1.SalesPerson (EntityType)

OpenType: true
Key: SalesEmployeeCode

## Properties

- SalesEmployeeCode : Edm.Int32 [required]
- SalesEmployeeName : Edm.String
- Remarks : Edm.String
- CommissionForSalesEmployee : Edm.Double
- CommissionGroup : Edm.Int32
- Locked : SAPB1.BoYesNoEnum
- EmployeeID : Edm.Int32
- Active : SAPB1.BoYesNoEnum
- Telephone : Edm.String
- Mobile : Edm.String
- Fax : Edm.String
- Email : Edm.String

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=SalesPerson]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=SalesPerson]
- Drafts : Collection(SAPB1.Document) [Partner=SalesPerson]
- StockTransferDrafts : Collection(SAPB1.StockTransfer) [Partner=SalesPerson]
- Activities : Collection(SAPB1.Activity) [Partner=SalesPerson]
- InventoryTransferRequests : Collection(SAPB1.StockTransfer) [Partner=SalesPerson]
- CreditNotes : Collection(SAPB1.Document) [Partner=SalesPerson]
- Invoices : Collection(SAPB1.Document) [Partner=SalesPerson]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=SalesPerson]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=SalesPerson]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=SalesPerson]
- Orders : Collection(SAPB1.Document) [Partner=SalesPerson]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=SalesPerson]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=SalesPerson]
- Returns : Collection(SAPB1.Document) [Partner=SalesPerson]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=SalesPerson]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=SalesPerson]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=SalesPerson]
- EmployeesInfo : Collection(SAPB1.EmployeeInfo) [Partner=SalesPerson]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=SalesPerson]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=SalesPerson]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=SalesPerson]
- DownPayments : Collection(SAPB1.Document) [Partner=SalesPerson]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=SalesPerson]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=SalesPerson]
- ReturnRequest : Collection(SAPB1.Document) [Partner=SalesPerson]
- Quotations : Collection(SAPB1.Document) [Partner=SalesPerson]
- ProjectManagements : Collection(SAPB1.PM_ProjectDocumentData) [Partner=SalesPerson]
- SalesOpportunities : Collection(SAPB1.SalesOpportunities) [Partner=SalesPerson2]
- SelfInvoices : Collection(SAPB1.Document) [Partner=SalesPerson]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=SalesPerson]
- Contacts : Collection(SAPB1.Contact) [Partner=SalesPerson]
- CommissionGroup2 : SAPB1.CommissionGroup [Partner=SalesPersons]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=SalesPerson]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=SalesPerson]
- StockTransfers : Collection(SAPB1.StockTransfer) [Partner=SalesPerson]
- UserDefaultGroups : Collection(SAPB1.UserDefaultGroup) [Partner=SalesPerson]

# SAPB1.SalesPersonParams (ComplexType)

## Properties

- SalesEmployeeCode : Edm.Int32

# SAPB1.SalesStage (EntityType)

OpenType: true
Key: SequenceNo

## Properties

- SequenceNo : Edm.Int32 [required]
- Name : Edm.String
- Stageno : Edm.Int32
- ClosingPercentage : Edm.Double
- Cancelled : SAPB1.BoYesNoEnum
- IsSales : SAPB1.BoYesNoEnum
- IsPurchasing : SAPB1.BoYesNoEnum

## Navigation properties

- SalesOpportunities : Collection(SAPB1.SalesOpportunities) [Partner=SalesStage]

# SAPB1.SalesStageParams (ComplexType)

## Properties

- SequenceNo : Edm.Int32

# SAPB1.SalesTaxAuthoritiesType (EntityType)

OpenType: true
Key: Numerator

## Properties

- UserSignature : Edm.Int32
- Name : Edm.String
- VAT : SAPB1.BoYesNoEnum
- Numerator : Edm.Int32 [required]
- TaxCreditControl : SAPB1.BoYesNoEnum
- NfTaxId : Edm.Int32
- TaxParamSetId : Edm.Int32

## Navigation properties

- SalesTaxAuthorities : Collection(SAPB1.SalesTaxAuthority) [Partner=SalesTaxAuthoritiesType]
- User : SAPB1.User [Partner=SalesTaxAuthoritiesTypes]
- NFTaxCategory : SAPB1.NFTaxCategory [Partner=SalesTaxAuthoritiesTypes]
- DepreciationAreas : Collection(SAPB1.DepreciationArea) [Partner=SalesTaxAuthoritiesType]

# SAPB1.SalesTaxAuthoritiesTypeParams (ComplexType)

## Properties

- Numerator : Edm.Int32

# SAPB1.SalesTaxAuthority (EntityType)

OpenType: true
Key: Type, Code

## Properties

- UseTaxAccount : Edm.String
- UserSignature : Edm.Int32
- Type : Edm.Int32 [required]
- AOrRTaxAccount : Edm.String
- Rate : Edm.Double
- AOrPTaxAccount : Edm.String
- NonDeductiblePrecent : Edm.Double
- NonDeductibleAccount : Edm.String
- Name : Edm.String
- DeferredTaxAccount : Edm.String
- Code : Edm.String [required]
- MinTaxableAmount : Edm.Double
- MaxTaxableAmount : Edm.Double
- FlatTaxAmount : Edm.Double
- InclInPrice : SAPB1.BoYesNoEnum
- Exempt : SAPB1.BoYesNoEnum
- APExpAccount : Edm.String
- ARExpAccount : Edm.String
- InclInGrossRevenue : SAPB1.BoYesNoEnum
- TextCode : Edm.Int32
- InclInFirstInstallment : SAPB1.BoYesNoEnum
- ReverseChargePercent : Edm.Double
- SalesTaxRCMAccount : Edm.String
- SalesTaxRCMClrAccount : Edm.String
- VATExemption : SAPB1.BoYesNoEnum
- VATExemptionBasePercent : Edm.Double
- VATExemptionPercent : Edm.Double
- TaxDefinitions : Collection(SAPB1.TaxDefinition)

## Navigation properties

- ChartOfAccount : SAPB1.ChartOfAccount [Partner=SalesTaxAuthorities]
- User : SAPB1.User [Partner=SalesTaxAuthorities]
- SalesTaxAuthoritiesType : SAPB1.SalesTaxAuthoritiesType [Partner=SalesTaxAuthorities]

# SAPB1.SalesTaxAuthorityParams (ComplexType)

## Properties

- Code : Edm.String
- Type : Edm.Int32

# SAPB1.SalesTaxCode (EntityType)

OpenType: true
Key: Code

## Properties

- ValidForAR : SAPB1.BoYesNoEnum
- ValidForAP : SAPB1.BoYesNoEnum
- UserSignature : Edm.Int32
- Rate : Edm.Double
- Name : Edm.String
- Freight : SAPB1.BoYesNoEnum
- Code : Edm.String [required]
- IsItemLevel : SAPB1.BoYesNoEnum
- Inactive : SAPB1.BoYesNoEnum
- FADebit : SAPB1.BoYesNoEnum
- TypeFormulaCombId : Edm.Int32
- CFOPIn : Edm.String
- CFOPOut : Edm.String
- SalesTaxCodes_Lines : Collection(SAPB1.SalesTaxCodes_Line)

## Navigation properties

- User : SAPB1.User [Partner=SalesTaxCodes]
- NotaFiscalCFOP : SAPB1.NotaFiscalCFOP [Partner=SalesTaxCodes]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=SalesTaxCode]
- ExpenseTypes : Collection(SAPB1.ExpenseTypeData) [Partner=SalesTaxCode]
- Items : Collection(SAPB1.Item) [Partner=SalesTaxCode]
- Warehouses : Collection(SAPB1.Warehouse) [Partner=SalesTaxCode]
- UserDefaultGroups : Collection(SAPB1.UserDefaultGroup) [Partner=SalesTaxCode]

# SAPB1.SalesTaxCodeParams (ComplexType)

## Properties

- Code : Edm.String

# SAPB1.SalesTaxCodes_Line (ComplexType)

OpenType: true

## Properties

- STATaxOnTaxType : Edm.Int32
- STATaxonTaxCode : Edm.String
- STCCode : Edm.String
- STAType : Edm.Int32
- STACode : Edm.String
- RowNumber : Edm.Int32
- EffectiveRate : Edm.Double
- FormulaId : Edm.Int32
- CSTCodeIn : Edm.String
- CSTSuffix : Edm.String

# SAPB1.SalesTaxInvoice (EntityType)

OpenType: true
Key: DocEntry

## Properties

- DocEntry : Edm.Int32 [required]
- DocNum : Edm.Int32
- DocType : SAPB1.BoTaxInvoiceTypes
- Printed : SAPB1.BoYesNoEnum
- DocDate : Edm.DateTimeOffset
- CardCode : Edm.String
- CreationDate : Edm.DateTimeOffset
- UpdateDate : Edm.DateTimeOffset
- DocDueDate : Edm.DateTimeOffset
- Series : Edm.Int32
- Segment : Edm.Int32
- ContactPersonCode : Edm.Int32
- TaxDate : Edm.DateTimeOffset
- Comments : Edm.String
- ShipToCode : Edm.String
- Address : Edm.String
- Address2 : Edm.String
- CurrencySource : SAPB1.BoCurrencySources
- DocCurrency : Edm.String
- CustomerOrVendorRefNo : Edm.String
- CustomerOrVendorName : Edm.String
- CancelDate : Edm.DateTimeOffset
- DocumentTotal : Edm.Double
- TaxTotal : Edm.Double
- PaymentRefNo : Edm.String
- PaymentRefDate : Edm.DateTimeOffset
- AlterationRevision : Edm.Int32
- SalesTaxInvoiceLines : Collection(SAPB1.SalesTaxInvoiceLine)
- SalesTaxInvoiceOperationCodes : Collection(SAPB1.SalesTaxInvoiceOperationCode)
- SalesTaxInvoiceDocumentReferences : Collection(SAPB1.SalesTaxInvoiceDocumentReference)
- SalesTaxInvoiceLinkedDownPayments : Collection(SAPB1.SalesTaxInvoiceLinkedDownPayment)

## Navigation properties

- BusinessPartner : SAPB1.BusinessPartner [Partner=SalesTaxInvoices]

# SAPB1.SalesTaxInvoiceDocumentReference (ComplexType)

OpenType: true

## Properties

- DocEntry : Edm.Int32
- LineNumber : Edm.Int32
- ReferencedDocEntry : Edm.Int32
- ReferencedDocNumber : Edm.Int32
- ExternalReferencedDocNumber : Edm.String
- ReferencedObjectType : SAPB1.ReferencedObjectTypeEnum
- IssueDate : Edm.DateTimeOffset
- Remark : Edm.String
- CardCode : Edm.String

# SAPB1.SalesTaxInvoiceLine (ComplexType)

OpenType: true

## Properties

- RefEntry1 : Edm.Int32
- RefEntry2 : Edm.Int32

# SAPB1.SalesTaxInvoiceLinkedDownPayment (ComplexType)

OpenType: true

## Properties

- DocEntry : Edm.Int32
- LineNum : Edm.Int32
- DownPaymentType : Edm.Int32
- DownPaymentEntry : Edm.Int32
- DownPaymentNum : Edm.Int32
- PaymentType : Edm.Int32
- PaymentEntry : Edm.Int32
- PaymentNum : Edm.Int32
- PaymentTaxDate : Edm.DateTimeOffset
- TransferDate : Edm.DateTimeOffset
- TransferReference : Edm.String
- AmountToDraw : Edm.Double
- AmountToDrawFC : Edm.Double
- AmountToDrawSC : Edm.Double
- Tax : Edm.Double
- TaxFC : Edm.Double
- TaxSC : Edm.Double
- GrossAmountToDraw : Edm.Double
- GrossAmountToDrawFC : Edm.Double
- GrossAmountToDrawSC : Edm.Double
- DocCurrency : Edm.String

# SAPB1.SalesTaxInvoiceOperationCode (ComplexType)

OpenType: true

## Properties

- OpCode : Edm.Int32

# SAPB1.SalesTaxInvoiceParams (ComplexType)

## Properties

- DocEntry : Edm.Int32

# SAPB1.Section (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- Code : Edm.String
- Description : Edm.String
- ECode : Edm.String

## Navigation properties

- CertificateSeries : Collection(SAPB1.CertificateSeries) [Partner=Section2]
- WithholdingTaxCodes : Collection(SAPB1.WithholdingTaxCode) [Partner=Section2]

# SAPB1.SectionParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- Code : Edm.String
- Description : Edm.String

# SAPB1.SensitiveDataAccess (ComplexType)

## Properties

- Table : Edm.String
- Key1 : Edm.String
- Key2 : Edm.String
- Key3 : Edm.String
- Key4 : Edm.String
- PropertyName : Edm.String
- PropertyID : Edm.Int32
- PropertyValue : Edm.String

# SAPB1.SerialNumber (ComplexType)

OpenType: true
Filtered properties: 29

## Properties

- ManufacturerSerialNumber : Edm.String
- InternalSerialNumber : Edm.String
- ExpiryDate : Edm.DateTimeOffset
- ManufactureDate : Edm.DateTimeOffset
- ReceptionDate : Edm.DateTimeOffset
- WarrantyStart : Edm.DateTimeOffset
- WarrantyEnd : Edm.DateTimeOffset
- Location : Edm.String
- Notes : Edm.String
- BatchID : Edm.String
- SystemSerialNumber : Edm.Int32
- BaseLineNumber : Edm.Int32
- Quantity : Edm.Double
- TrackingNote : Edm.Int32
- TrackingNoteLine : Edm.Int32
- ItemCode : Edm.String

# SAPB1.SerialNumberDetail (EntityType)

OpenType: true
Key: DocEntry
Filtered properties: 29

## Properties

- DocEntry : Edm.Int32 [required]
- ItemCode : Edm.String
- ItemDescription : Edm.String
- MfrSerialNo : Edm.String
- SerialNumber : Edm.String
- LotNumber : Edm.String
- SystemNumber : Edm.Int32
- AdmissionDate : Edm.DateTimeOffset
- ManufacturingDate : Edm.DateTimeOffset
- ExpirationDate : Edm.DateTimeOffset
- MfrWarrantyStart : Edm.DateTimeOffset
- MFrWarrantyEnd : Edm.DateTimeOffset
- Location : Edm.String
- Details : Edm.String

## Navigation properties

- Item : SAPB1.Item [Partner=SerialNumberDetails]

# SAPB1.SerialNumberDetailParams (ComplexType)

## Properties

- DocEntry : Edm.Int32

# SAPB1.Series (ComplexType)

OpenType: true

## Properties

- Document : Edm.String
- DocumentSubType : Edm.String
- InitialNumber : Edm.Int32
- LastNumber : Edm.Int32
- NextNumber : Edm.Int32
- Prefix : Edm.String
- Suffix : Edm.String
- Remarks : Edm.String
- GroupCode : SAPB1.BoSeriesGroupEnum
- Locked : SAPB1.BoYesNoEnum
- PeriodIndicator : Edm.String
- Name : Edm.String
- SeriesProperty : Edm.Int32
- IsDigitalSeries : SAPB1.BoYesNoEnum
- DigitNumber : Edm.Int32
- SeriesType : SAPB1.BoSeriesTypeEnum
- IsManual : SAPB1.BoYesNoEnum
- BPLID : Edm.Int32
- ATDocumentType : Edm.String
- IsElectronicCommEnabled : SAPB1.BoYesNoEnum
- CostAccountOnly : SAPB1.BoYesNoEnum
- InvoiceType : Edm.Int32
- InvoiceTypeOfNegativeInvoice : Edm.Int32
- PortugalSeriesAction : Edm.String
- PortugalSeriesStatus : Edm.String
- PortugalSeriesPhase : Edm.String

# SAPB1.SeriesLine (ComplexType)

## Properties

- Series : Edm.Int32
- Prefix : Edm.String
- FirstNum : Edm.Int32
- NextNum : Edm.Int32
- LastNum : Edm.Int32

# SAPB1.SeriesParams (ComplexType)

## Properties

- Series : Edm.Int32

# SAPB1.ServiceAppReport (ComplexType)

## Properties

- Code : Edm.Int32
- SystemReportName : Edm.String
- CustomizedReportName : Edm.String
- ReportChoice : SAPB1.MobileAppReportChoiceEnum

# SAPB1.ServiceAppReportContent (ComplexType)

## Properties

- ReportContent : Edm.String

# SAPB1.ServiceAppReportParams (ComplexType)

## Properties

- Code : Edm.Int32
- ReportChoice : SAPB1.MobileAppReportChoiceEnum

# SAPB1.ServiceCall (EntityType)

OpenType: true
Key: ServiceCallID
Filtered properties: 1

## Properties

- ServiceCallID : Edm.Int32 [required]
- Subject : Edm.String
- CustomerCode : Edm.String
- CustomerName : Edm.String
- ContactCode : Edm.Int32
- ManufacturerSerialNum : Edm.String
- InternalSerialNum : Edm.String
- ContractID : Edm.Int32
- ContractEndDate : Edm.DateTimeOffset
- ResolutionDate : Edm.DateTimeOffset
- ResolutionTime : Edm.TimeOfDay
- Origin : Edm.Int32
- ItemCode : Edm.String
- ItemDescription : Edm.String
- ItemGroupCode : Edm.Int32
- Status : Edm.Int32
- Priority : SAPB1.BoSvcCallPriorities
- CallType : Edm.Int32
- ProblemType : Edm.Int32
- AssigneeCode : Edm.Int32
- Description : Edm.String
- TechnicianCode : Edm.Int32
- Resolution : Edm.String
- CreationDate : Edm.DateTimeOffset
- CreationTime : Edm.TimeOfDay
- Responder : Edm.Int32
- UpdatedTime : Edm.TimeOfDay
- BelongsToAQueue : SAPB1.BoYesNoEnum
- ResponseByTime : Edm.TimeOfDay
- ResponseByDate : Edm.DateTimeOffset
- ResolutionOnDate : Edm.DateTimeOffset
- ResponseOnTime : Edm.TimeOfDay
- ResponseOnDate : Edm.DateTimeOffset
- ClosingTime : Edm.TimeOfDay
- AssignedDate : Edm.DateTimeOffset
- Queue : Edm.String
- ResponseAssignee : Edm.Int32
- EntitledforService : SAPB1.BoYesNoEnum
- ResolutionOnTime : Edm.TimeOfDay
- AssignedTime : Edm.TimeOfDay
- ClosingDate : Edm.DateTimeOffset
- Series : Edm.Int32
- DocNum : Edm.Int32
- HandWritten : SAPB1.BoYesNoEnum
- PeriodIndicator : Edm.String
- StartDate : Edm.DateTimeOffset
- StartTime : Edm.TimeOfDay
- EndDueDate : Edm.DateTimeOffset
- EndTime : Edm.TimeOfDay
- Duration : Edm.Double
- DurationType : SAPB1.BoDurations
- Reminder : SAPB1.BoYesNoEnum
- ReminderPeriod : Edm.Double
- ReminderType : SAPB1.BoDurations
- Location : Edm.Int32
- AddressName : Edm.String
- AddressType : SAPB1.BoAddressType
- Street : Edm.String
- City : Edm.String
- Room : Edm.String
- State : Edm.String
- Country : Edm.String
- DisplayInCalendar : SAPB1.BoYesNoEnum
- CustomerRefNo : Edm.String
- ProblemSubType : Edm.Int32
- AttachmentEntry : Edm.Int32
- ServiceBPType : SAPB1.ServiceTypeEnum
- BPContactPerson : Edm.String
- BPPhone1 : Edm.String
- BPPhone2 : Edm.String
- BPCellular : Edm.String
- BPFax : Edm.String
- BPeMail : Edm.String
- BPProjectCode : Edm.String
- BPTerritory : Edm.Int32
- BPShipToCode : Edm.String
- BPShipToAddress : Edm.String
- BPBillToCode : Edm.String
- BPBillToAddress : Edm.String
- Telephone : Edm.String
- UpdateDate : Edm.DateTimeOffset
- SupplementaryCode : Edm.String
- ServiceCallActivities : Collection(SAPB1.ServiceCallActivity)
- ServiceCallInventoryExpenses : Collection(SAPB1.ServiceCallInventoryExpense)
- ServiceCallSolutions : Collection(SAPB1.ServiceCallSolution)
- ServiceCallSchedulings : Collection(SAPB1.ServiceCallScheduling)
- ServiceCallBPAddressComponents : Collection(SAPB1.ServiceCallBPAddressComponent)

## Navigation properties

- BusinessPartner : SAPB1.BusinessPartner [Partner=ServiceCalls]
- ServiceContract : SAPB1.ServiceContract [Partner=ServiceCalls]
- ServiceCallOrigin : SAPB1.ServiceCallOrigin [Partner=ServiceCalls]
- Item : SAPB1.Item [Partner=ServiceCalls]
- ItemGroups : SAPB1.ItemGroups [Partner=ServiceCalls]
- ServiceCallStatus : SAPB1.ServiceCallStatus [Partner=ServiceCalls]
- ServiceCallType : SAPB1.ServiceCallType [Partner=ServiceCalls]
- ServiceCallProblemType : SAPB1.ServiceCallProblemType [Partner=ServiceCalls]
- User : SAPB1.User [Partner=ServiceCalls]
- EmployeeInfo : SAPB1.EmployeeInfo [Partner=ServiceCalls]
- Queue2 : SAPB1.Queue [Partner=ServiceCalls]
- ActivityLocation : SAPB1.ActivityLocation [Partner=ServiceCalls]
- Country2 : SAPB1.Country [Partner=ServiceCalls]
- ServiceCallProblemSubType : SAPB1.ServiceCallProblemSubType [Partner=ServiceCalls]
- Project : SAPB1.Project [Partner=ServiceCalls]

# SAPB1.ServiceCallActivity (ComplexType)

OpenType: true

## Properties

- LineNum : Edm.Int32
- ActivityCode : Edm.Int32

# SAPB1.ServiceCallBPAddressComponent (ComplexType)

OpenType: true
Filtered properties: 4

## Properties

- ShipToStreet : Edm.String
- ShipToStreetNo : Edm.String
- ShipToBlock : Edm.String
- ShipToBuilding : Edm.String
- ShipToCity : Edm.String
- ShipToZipCode : Edm.String
- ShipToState : Edm.String
- ShipToCounty : Edm.String
- ShipToCountry : Edm.String
- ShipToAddressType : Edm.String
- ShipToAddress2 : Edm.String
- ShipToAddress3 : Edm.String
- ShipToGlobalLocationNumber : Edm.String
- BillToStreet : Edm.String
- BillToStreetNo : Edm.String
- BillToBlock : Edm.String
- BillToBuilding : Edm.String
- BillToCity : Edm.String
- BillToZipCode : Edm.String
- BillToState : Edm.String
- BillToCounty : Edm.String
- BillToCountry : Edm.String
- BillToAddressType : Edm.String
- BillToAddress2 : Edm.String
- BillToAddress3 : Edm.String
- BillToGlobalLocationNumber : Edm.String

# SAPB1.ServiceCallInventoryExpense (ComplexType)

OpenType: true

## Properties

- LineNum : Edm.Int32
- PartType : SAPB1.BoSvcExpPartTypes
- DocumentType : SAPB1.BoSvcEpxDocTypes
- DocumentPostingDate : Edm.DateTimeOffset
- DocumentNumber : Edm.Int32
- StockTransferDirection : SAPB1.BoStckTrnDir
- DocEntry : Edm.Int32

# SAPB1.ServiceCallOrigin (EntityType)

Key: OriginID

## Properties

- OriginID : Edm.Int32 [required]
- Name : Edm.String
- Description : Edm.String
- Active : SAPB1.BoYesNoEnum

## Navigation properties

- ServiceCalls : Collection(SAPB1.ServiceCall) [Partner=ServiceCallOrigin]

# SAPB1.ServiceCallOriginParams (ComplexType)

## Properties

- OriginID : Edm.Int32
- Name : Edm.String

# SAPB1.ServiceCallParams (ComplexType)

## Properties

- ServiceCallID : Edm.Int32

# SAPB1.ServiceCallProblemSubType (EntityType)

Key: ProblemSubTypeID

## Properties

- ProblemSubTypeID : Edm.Int32 [required]
- Name : Edm.String
- Description : Edm.String
- Active : SAPB1.BoYesNoEnum

## Navigation properties

- ServiceCalls : Collection(SAPB1.ServiceCall) [Partner=ServiceCallProblemSubType]

# SAPB1.ServiceCallProblemSubTypeParams (ComplexType)

## Properties

- ProblemSubTypeID : Edm.Int32
- Name : Edm.String

# SAPB1.ServiceCallProblemType (EntityType)

Key: ProblemTypeID

## Properties

- ProblemTypeID : Edm.Int32 [required]
- Name : Edm.String
- Description : Edm.String
- Active : SAPB1.BoYesNoEnum

## Navigation properties

- ServiceCalls : Collection(SAPB1.ServiceCall) [Partner=ServiceCallProblemType]

# SAPB1.ServiceCallProblemTypeParams (ComplexType)

## Properties

- ProblemTypeID : Edm.Int32
- Name : Edm.String

# SAPB1.ServiceCallScheduling (ComplexType)

OpenType: true

## Properties

- LineNum : Edm.Int32
- Technician : Edm.Int32
- HandledBy : Edm.Int32
- StartDate : Edm.DateTimeOffset
- StartTime : Edm.TimeOfDay
- EndDate : Edm.DateTimeOffset
- EndTime : Edm.TimeOfDay
- Duration : Edm.Double
- ActualDuration : Edm.Double
- DurationType : SAPB1.BoDurations
- ActualDurationType : SAPB1.BoDurations
- Reminder : SAPB1.BoYesNoEnum
- ReminderPeriod : Edm.Double
- ReminderType : SAPB1.BoDurations
- ReminderSent : SAPB1.BoYesNoEnum
- ReminderDate : Edm.DateTimeOffset
- ReminderTime : Edm.TimeOfDay
- DisplayInCalendar : SAPB1.BoYesNoEnum
- IsUnscheduled : SAPB1.BoYesNoEnum
- Location : Edm.Int32
- AddressName : Edm.String
- AddressText : Edm.String
- Street : Edm.String
- City : Edm.String
- Room : Edm.String
- State : Edm.String
- Country : Edm.String
- Address2 : Edm.String
- Address3 : Edm.String
- AddressType : Edm.String
- StreetNo : Edm.String
- ZipCode : Edm.String
- Block : Edm.String
- County : Edm.String
- TaxOffice : Edm.String
- GlobalLocNum : Edm.String
- IsClosed : SAPB1.BoYesNoEnum
- Remark : Edm.String
- AddressTypeBS : SAPB1.BoAddressType
- SignatureName : Edm.String
- SalesOrders : Edm.String
- CheckInDate : Edm.DateTimeOffset
- CheckInTime : Edm.TimeOfDay
- CheckInLocation : Edm.String
- CheckInLatitude : Edm.String
- CheckInLongitude : Edm.String
- CheckOutDate : Edm.DateTimeOffset
- CheckOutTime : Edm.TimeOfDay

# SAPB1.ServiceCallSolution (ComplexType)

OpenType: true

## Properties

- LineNum : Edm.Int32
- SolutionID : Edm.Int32

# SAPB1.ServiceCallSolutionStatus (EntityType)

Key: StatusId

## Properties

- StatusId : Edm.Int32 [required]
- Name : Edm.String
- Description : Edm.String
- Active : SAPB1.BoYesNoEnum

## Navigation properties

- KnowledgeBaseSolutions : Collection(SAPB1.KnowledgeBaseSolution) [Partner=ServiceCallSolutionStatus]

# SAPB1.ServiceCallSolutionStatusParams (ComplexType)

## Properties

- StatusId : Edm.Int32
- Name : Edm.String

# SAPB1.ServiceCallStatus (EntityType)

Key: StatusId

## Properties

- StatusId : Edm.Int32 [required]
- Name : Edm.String
- Description : Edm.String
- Active : SAPB1.BoYesNoEnum

## Navigation properties

- ServiceCalls : Collection(SAPB1.ServiceCall) [Partner=ServiceCallStatus]

# SAPB1.ServiceCallStatusParams (ComplexType)

## Properties

- StatusId : Edm.Int32
- Name : Edm.String

# SAPB1.ServiceCallType (EntityType)

Key: CallTypeID

## Properties

- CallTypeID : Edm.Int32 [required]
- Name : Edm.String
- Description : Edm.String
- Active : SAPB1.BoYesNoEnum

## Navigation properties

- ServiceCalls : Collection(SAPB1.ServiceCall) [Partner=ServiceCallType]

# SAPB1.ServiceCallTypeParams (ComplexType)

## Properties

- CallTypeID : Edm.Int32
- Name : Edm.String

# SAPB1.ServiceContract (EntityType)

OpenType: true
Key: ContractID

## Properties

- ContractID : Edm.Int32 [required]
- CustomerCode : Edm.String
- CustomerName : Edm.String
- ContactCode : Edm.Int32
- Owner : Edm.Int32
- Status : SAPB1.BoSvcContractStatus
- ContractTemplate : Edm.String
- ContractType : SAPB1.BoContractTypes
- Renewal : SAPB1.BoYesNoEnum
- ReminderTime : Edm.Int32
- RemindUnit : SAPB1.BoRemindUnits
- DurationOfCoverage : Edm.Int32
- StartDate : Edm.DateTimeOffset
- EndDate : Edm.DateTimeOffset
- ResolutionTime : Edm.Int32
- ResolutionUnit : SAPB1.BoResolutionUnits
- Description : Edm.String
- MondayEnabled : SAPB1.BoYesNoEnum
- TuesdayEnabled : SAPB1.BoYesNoEnum
- WednesdayEnabled : SAPB1.BoYesNoEnum
- ThursdayEnabled : SAPB1.BoYesNoEnum
- FridayEnabled : SAPB1.BoYesNoEnum
- SaturdayEnabled : SAPB1.BoYesNoEnum
- SundayEnabled : SAPB1.BoYesNoEnum
- MondayStart : Edm.TimeOfDay
- MondayEnd : Edm.TimeOfDay
- TuesdayStart : Edm.TimeOfDay
- TuesdayEnd : Edm.TimeOfDay
- WednesdayStart : Edm.TimeOfDay
- WednesdayEnd : Edm.TimeOfDay
- ThursdayStart : Edm.TimeOfDay
- ThursdayEnd : Edm.TimeOfDay
- FridayStart : Edm.TimeOfDay
- FridayEnd : Edm.TimeOfDay
- SaturdayStart : Edm.TimeOfDay
- SaturdayEnd : Edm.TimeOfDay
- SundayStart : Edm.TimeOfDay
- SundayEnd : Edm.TimeOfDay
- IncludeParts : SAPB1.BoYesNoEnum
- IncludeLabor : SAPB1.BoYesNoEnum
- IncludeTravel : SAPB1.BoYesNoEnum
- TemplateRemarks : Edm.String
- Remarks : Edm.String
- IncludeHolidays : SAPB1.BoYesNoEnum
- ServiceType : SAPB1.BoServiceTypes
- ResponseUnit : SAPB1.BoResponseUnit
- ResponseTime : Edm.Int32
- TerminationDate : Edm.DateTimeOffset
- AttachmentEntry : Edm.Int32
- ServiceBPType : SAPB1.ServiceTypeEnum
- ServiceContract_Lines : Collection(SAPB1.ServiceContract_Line)

## Navigation properties

- CustomerEquipmentCards : Collection(SAPB1.CustomerEquipmentCard) [Partner=ServiceContract]
- BusinessPartner : SAPB1.BusinessPartner [Partner=ServiceContracts]
- User : SAPB1.User [Partner=ServiceContracts]
- ContractTemplate2 : SAPB1.ContractTemplate [Partner=ServiceContracts]
- Attachments2 : SAPB1.Attachments2 [Partner=ServiceContracts]
- ServiceCalls : Collection(SAPB1.ServiceCall) [Partner=ServiceContract]

# SAPB1.ServiceContract_Line (ComplexType)

OpenType: true

## Properties

- LineNum : Edm.Int32
- ManufacturerSerialNum : Edm.String
- InternalSerialNum : Edm.String
- ItemCode : Edm.String
- ItemName : Edm.String
- ItemGroup : Edm.Int32
- StartDate : Edm.DateTimeOffset
- EndDate : Edm.DateTimeOffset
- ItemGroupName : Edm.String
- TerminationDate : Edm.DateTimeOffset

# SAPB1.ServiceContractParams (ComplexType)

## Properties

- ContractID : Edm.Int32

# SAPB1.ServiceGroup (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- ServiceGroupCode : Edm.String
- Description : Edm.String

## Navigation properties

- Items : Collection(SAPB1.Item) [Partner=ServiceGroup2]

# SAPB1.ServiceGroupParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- ServiceGroupCode : Edm.String

# SAPB1.ServiceTaxPostingParams (ComplexType)

## Properties

- DocEntry : Edm.Int32

# SAPB1.ShippingType (EntityType)

OpenType: true
Key: Code

## Properties

- Code : Edm.Int32 [required]
- Name : Edm.String
- Website : Edm.String

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=ShippingType]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=ShippingType]
- Drafts : Collection(SAPB1.Document) [Partner=ShippingType]
- BlanketAgreements : Collection(SAPB1.BlanketAgreement) [Partner=ShippingType2]
- CreditNotes : Collection(SAPB1.Document) [Partner=ShippingType]
- Invoices : Collection(SAPB1.Document) [Partner=ShippingType]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=ShippingType]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=ShippingType]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=ShippingType]
- Orders : Collection(SAPB1.Document) [Partner=ShippingType]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=ShippingType]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=ShippingType]
- Returns : Collection(SAPB1.Document) [Partner=ShippingType]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=ShippingType]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=ShippingType]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=ShippingType]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=ShippingType]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=ShippingType]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=ShippingType2]
- DownPayments : Collection(SAPB1.Document) [Partner=ShippingType]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=ShippingType]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=ShippingType]
- ReturnRequest : Collection(SAPB1.Document) [Partner=ShippingType]
- Quotations : Collection(SAPB1.Document) [Partner=ShippingType]
- SelfInvoices : Collection(SAPB1.Document) [Partner=ShippingType]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=ShippingType]
- LandedCosts : Collection(SAPB1.LandedCost) [Partner=ShippingType]
- Items : Collection(SAPB1.Item) [Partner=ShippingType]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=ShippingType]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=ShippingType]

# SAPB1.ShippingTypeParams (ComplexType)

## Properties

- Code : Edm.Int32

# SAPB1.ShortLinkMapping (EntityType)

Key: Guid

## Properties

- Guid : Edm.String [required]
- Origin : Edm.String
- SrcLink : Edm.String
- OwnerCode : Edm.String
- CreateDate : Edm.DateTimeOffset
- CreateTime : Edm.TimeOfDay

# SAPB1.ShortLinkMappingParams (ComplexType)

## Properties

- Guid : Edm.String

# SAPB1.ShowDifferenceParams (ComplexType)

## Properties

- PrimaryKey : Edm.String
- UDOObjectCode : Edm.String
- Object : SAPB1.BoChangeLogEnum
- LogInstance2 : Edm.Int32
- LogInstance : Edm.Int32

# SAPB1.SingleUserConnection (EntityType)

Key: Code

## Properties

- Code : Edm.Int32 [required]
- Action : SAPB1.SingleUserConnectionActionEnum

# SAPB1.SingleUserConnectionParams (ComplexType)

## Properties

- Code : Edm.Int32

# SAPB1.SNBLines (ComplexType)

## Properties

- SnbAbsEntry : Edm.Int32
- NewCost : Edm.Double
- DebitCredit : Edm.Double
- SystemNumber : Edm.Int32
- LotNumber : Edm.String
- ManufactureNumber : Edm.String
- AdmissionDate : Edm.DateTimeOffset
- ExpirationDate : Edm.DateTimeOffset
- BaseLine : Edm.Int32

# SAPB1.SpecialPrice (EntityType)

OpenType: true
Key: ItemCode, CardCode

## Properties

- ItemCode : Edm.String [required]
- CardCode : Edm.String [required]
- Price : Edm.Double
- Currency : Edm.String
- DiscountPercent : Edm.Double
- PriceListNum : Edm.Int32
- AutoUpdate : SAPB1.BoYesNoEnum
- SourcePrice : SAPB1.SourceCurrencyEnum
- Valid : SAPB1.BoYesNoEnum
- ValidFrom : Edm.DateTimeOffset
- ValidTo : Edm.DateTimeOffset
- SpecialPriceDataAreas : Collection(SAPB1.SpecialPriceDataArea)

## Navigation properties

- Item : SAPB1.Item [Partner=SpecialPrices]
- BusinessPartner : SAPB1.BusinessPartner [Partner=SpecialPrices]
- PriceList : SAPB1.PriceList [Partner=SpecialPrices]

# SAPB1.SpecialPriceDataArea (ComplexType)

OpenType: true

## Properties

- PriceCurrency : Edm.String
- AutoUpdate : SAPB1.BoYesNoEnum
- Dateto : Edm.DateTimeOffset
- Discount : Edm.Double
- SpecialPrice : Edm.Double
- DateFrom : Edm.DateTimeOffset
- BPCode : Edm.String
- PriceListNo : Edm.Int32
- ItemNo : Edm.String
- RowNumber : Edm.Int32
- SpecialPriceQuantityAreas : Collection(SAPB1.SpecialPriceQuantityArea)

# SAPB1.SpecialPriceParams (ComplexType)

## Properties

- ItemCode : Edm.String
- CardCode : Edm.String
- PriceListNum : Edm.Int32

# SAPB1.SpecialPriceQuantityArea (ComplexType)

OpenType: true

## Properties

- Quantity : Edm.Double
- SPDARowNumber : Edm.Int32
- SpecialPrice : Edm.Double
- ItemNo : Edm.String
- BPCode : Edm.String
- RowNumber : Edm.Int32
- PriceCurrency : Edm.String
- Discountin : Edm.Double
- UoMEntry : Edm.Int32

# SAPB1.SpecificWTHAmounts (EntityType)

OpenType: true
Key: PaymentReasonCode, CardCode, CUSplit

## Properties

- PaymentReasonCode : Edm.String [required]
- CardCode : Edm.String [required]
- CUSplit : SAPB1.BoYesNoEnum [required]
- FullWtaxTaxationInAdvance : Edm.Double
- WTaxAmountOnHold : Edm.Double
- RegionalIRPEFHeldAsWTax : Edm.Double
- RegionalIRPEFInAdvance : Edm.Double
- RegionalSuspendedTaxIRPEF : Edm.Double
- MunicipalTaxAsWTaxIRPEF : Edm.Double
- MunicipalTaxHeldAsAdvance : Edm.Double
- SuspendedMunicipalTax : Edm.Double
- TaxableAmtPreviousYear : Edm.Double
- WTaxAmountPreviousYear : Edm.Double
- ExpensesReimbursed : Edm.Double
- WTaxReimbursed : Edm.Double
- ReturnedAmountAfterDeductionOfWTax : Edm.Double
- DeliveryIdentificationNo : Edm.String
- SingleCertificationNo : Edm.String
- EarningYear : Edm.Int32
- Advanced : SAPB1.BoYesNoEnum
- WTaxTypeCode : Edm.String
- SocialSecurityFiscalC : Edm.String
- SocialSecurityInstitut : Edm.String
- CompanyCode : Edm.String
- Category : SAPB1.BoOSWACategoryEnum
- EmployeeSocialSecurity : Edm.Double
- EmployerSocialSecurity : Edm.Double
- OtherContributions : SAPB1.BoYesNoEnum
- ValueOfOtherContribut : Edm.Double
- OtherAmountsDue : Edm.Double
- OtherAmountsPaid : Edm.Double
- AmountPaidBeforeBankr : Edm.Double
- AmountPaidByTrustee : Edm.Double
- FiscalCode : Edm.String
- TaxableAmount : Edm.Double
- TaxAmount : Edm.Double
- TaxAmountInAdvance : Edm.Double
- SuspendedWTHTax : Edm.Double
- AdditionalRegionalTax57 : Edm.Double
- AdditionalRegionalTax58 : Edm.Double
- SuspendedRegionalTax : Edm.Double
- AdditionalCitytaxToI60 : Edm.Double
- AdditionalCityTaxToI : Edm.Double
- SuspendedCityTax : Edm.Double
- FiscalCodeThirdParty71 : Edm.String
- FiscalCodeThirdParty72 : Edm.String
- FiscalCodeExpropriation : Edm.String
- FiscalCodeOfMainDeb101 : Edm.String
- AmountPaid102 : Edm.Double
- AmountsProvidedAndNo104 : Edm.Double
- WHTApplied103 : Edm.Double
- FiscalCodeOfMainDeb105 : Edm.String
- AmountPaid106 : Edm.Double
- AmountsProvidedAndNo108 : Edm.Double
- WHTApplied107 : Edm.Double
- AmountPaid131 : Edm.Double
- TaxApplied132 : Edm.Double
- AmountPaid133 : Edm.Double
- TaxApplied134 : Edm.Double
- AmountPaid135 : Edm.Double
- TaxApplied136 : Edm.Double
- AmountPaid137 : Edm.Double
- TaxApplied138 : Edm.Double

## Navigation properties

- PaymentReasonCode2 : SAPB1.PaymentReasonCode [Partner=SpecificWTHAmountsService]
- BusinessPartner : SAPB1.BusinessPartner [Partner=SpecificWTHAmountsService]
- WTaxTypeCode2 : SAPB1.WTaxTypeCode [Partner=SpecificWTHAmountsService]

# SAPB1.SpecificWTHAmountsParams (ComplexType)

OpenType: true

## Properties

- PaymentReasonCode : Edm.String
- CardCode : Edm.String
- CUSplit : SAPB1.BoYesNoEnum
- FullWtaxTaxationInAdvance : Edm.Double
- WTaxAmountOnHold : Edm.Double
- RegionalIRPEFHeldAsWTax : Edm.Double
- RegionalIRPEFInAdvance : Edm.Double
- RegionalSuspendedTaxIRPEF : Edm.Double
- MunicipalTaxAsWTaxIRPEF : Edm.Double
- MunicipalTaxHeldAsAdvance : Edm.Double
- SuspendedMunicipalTax : Edm.Double
- TaxableAmtPreviousYear : Edm.Double
- WTaxAmountPreviousYear : Edm.Double
- ExpensesReimbursed : Edm.Double
- WTaxReimbursed : Edm.Double
- ReturnedAmountAfterDeductionOfWTax : Edm.Double
- DeliveryIdentificationNo : Edm.String
- SingleCertificationNo : Edm.String
- EarningYear : Edm.Int32
- Advanced : SAPB1.BoYesNoEnum
- WTaxTypeCode : Edm.String
- SocialSecurityFiscalC : Edm.String
- SocialSecurityInstitut : Edm.String
- CompanyCode : Edm.String
- Category : SAPB1.BoOSWACategoryEnum
- EmployeeSocialSecurity : Edm.Double
- EmployerSocialSecurity : Edm.Double
- OtherContributions : SAPB1.BoYesNoEnum
- ValueOfOtherContribut : Edm.Double
- OtherAmountsDue : Edm.Double
- OtherAmountsPaid : Edm.Double
- AmountPaidBeforeBankr : Edm.Double
- AmountPaidByTrustee : Edm.Double
- FiscalCode : Edm.String
- TaxableAmount : Edm.Double
- TaxAmount : Edm.Double
- TaxAmountInAdvance : Edm.Double
- SuspendedWTHTax : Edm.Double
- AdditionalRegionalTax57 : Edm.Double
- AdditionalRegionalTax58 : Edm.Double
- SuspendedRegionalTax : Edm.Double
- AdditionalCitytaxToI60 : Edm.Double
- AdditionalCityTaxToI : Edm.Double
- SuspendedCityTax : Edm.Double
- FiscalCodeThirdParty71 : Edm.String
- FiscalCodeThirdParty72 : Edm.String
- FiscalCodeExpropriation : Edm.String
- FiscalCodeOfMainDeb101 : Edm.String
- AmountPaid102 : Edm.Double
- AmountsProvidedAndNo104 : Edm.Double
- WHTApplied103 : Edm.Double
- FiscalCodeOfMainDeb105 : Edm.String
- AmountPaid106 : Edm.Double
- AmountsProvidedAndNo108 : Edm.Double
- WHTApplied107 : Edm.Double
- AmountPaid131 : Edm.Double
- TaxApplied132 : Edm.Double
- AmountPaid133 : Edm.Double
- TaxApplied134 : Edm.Double
- AmountPaid135 : Edm.Double
- TaxApplied136 : Edm.Double
- AmountPaid137 : Edm.Double
- TaxApplied138 : Edm.Double

# SAPB1.SQLQuery (EntityType)

Key: SqlCode

## Properties

- SqlCode : Edm.String [required]
- SqlName : Edm.String
- SqlText : Edm.String
- ParamList : Edm.String
- CreateDate : Edm.DateTimeOffset
- UpdateDate : Edm.DateTimeOffset

# SAPB1.SQLQueryParams (ComplexType)

## Properties

- SqlCode : Edm.String

# SAPB1.SQLQueryResult (ComplexType)

OpenType: true

## Properties

- SqlText : Edm.String

# SAPB1.SQLView (EntityType)

Key: Name

## Properties

- Name : Edm.String [required]
- DBType : Edm.String
- SchemaName : Edm.String
- CreateDate : Edm.DateTimeOffset

# SAPB1.SQLViewParams (ComplexType)

## Properties

- Name : Edm.String

# SAPB1.State (EntityType)

Key: Code, Country

## Properties

- Code : Edm.String [required]
- Country : Edm.String [required]
- Name : Edm.String
- GSTCode : Edm.String
- IsUnionTerritory : SAPB1.BoYesNoEnum

## Navigation properties

- Country2 : SAPB1.Country [Partner=States]

# SAPB1.StateParams (ComplexType)

## Properties

- Code : Edm.String
- Country : Edm.String
- Name : Edm.String

# SAPB1.StockTaking (EntityType)

OpenType: true
Key: ItemCode, WarehouseCode

## Properties

- ItemCode : Edm.String [required]
- WarehouseCode : Edm.String [required]
- Counted : Edm.Double

## Navigation properties

- Item : SAPB1.Item [Partner=StockTakings]
- Warehouse : SAPB1.Warehouse [Partner=StockTakings]

# SAPB1.StockTakingParams (ComplexType)

## Properties

- ItemCode : Edm.String
- WarehouseCode : Edm.String

# SAPB1.StockTransfer (EntityType)

OpenType: true
Key: DocEntry
Filtered properties: 45

## Properties

- DocEntry : Edm.Int32 [required]
- Series : Edm.Int32
- Printed : SAPB1.BoYesNoEnum
- DocDate : Edm.DateTimeOffset
- DueDate : Edm.DateTimeOffset
- CardCode : Edm.String
- CardName : Edm.String
- Address : Edm.String
- Reference1 : Edm.String
- Reference2 : Edm.String
- Comments : Edm.String
- JournalMemo : Edm.String
- PriceList : Edm.Int32
- SalesPersonCode : Edm.Int32
- FromWarehouse : Edm.String
- ToWarehouse : Edm.String
- CreationDate : Edm.DateTimeOffset
- UpdateDate : Edm.DateTimeOffset
- FinancialPeriod : Edm.Int32
- TransNum : Edm.Int32
- DocNum : Edm.Int32
- TaxDate : Edm.DateTimeOffset
- ContactPerson : Edm.Int32
- FolioPrefixString : Edm.String
- FolioNumber : Edm.Int32
- DocObjectCode : Edm.String
- AuthorizationStatus : SAPB1.StockTransferAuthorizationStatusEnum
- BPLID : Edm.Int32
- BPLName : Edm.String
- VATRegNum : Edm.String
- AuthorizationCode : Edm.String
- StartDeliveryDate : Edm.DateTimeOffset
- StartDeliveryTime : Edm.TimeOfDay
- EndDeliveryDate : Edm.DateTimeOffset
- EndDeliveryTime : Edm.TimeOfDay
- VehiclePlate : Edm.String
- ATDocumentType : Edm.String
- EDocExportFormat : Edm.Int32
- ElecCommStatus : SAPB1.ElecCommStatusEnum
- ElecCommMessage : Edm.String
- PointOfIssueCode : Edm.String
- Letter : SAPB1.FolioLetterEnum
- FolioNumberFrom : Edm.Int32
- FolioNumberTo : Edm.Int32
- AttachmentEntry : Edm.Int32
- DocumentStatus : SAPB1.BoStatus
- ShipToCode : Edm.String
- SAPPassport : Edm.String
- LastPageFolioNumber : Edm.Int32
- DutyStatus : SAPB1.BoYesNoEnum
- CreateQRCodeFrom : Edm.String
- CopyDutyStatus : SAPB1.BoYesNoEnum
- StockTransfer_ApprovalRequests : Collection(SAPB1.StockTransfer_ApprovalRequest)
- ElectronicProtocols : Collection(SAPB1.ElectronicProtocol)
- StockTransferLines : Collection(SAPB1.StockTransferLine)
- StockTransferTaxExtension : SAPB1.StockTransferTaxExtension
- DocumentReferences : Collection(SAPB1.DocumentReference)
- EDeliveryInfo : SAPB1.EDeliveryInfo

## Navigation properties

- BusinessPartner : SAPB1.BusinessPartner [Partner=StockTransfers]
- PaymentTermsType : SAPB1.PaymentTermsType [Partner=InventoryTransferRequests]
- SalesPerson : SAPB1.SalesPerson [Partner=StockTransfers]
- Warehouse : SAPB1.Warehouse [Partner=StockTransfers]
- JournalEntry : SAPB1.JournalEntry [Partner=StockTransfers]
- BusinessPlace : SAPB1.BusinessPlace [Partner=StockTransfers]
- PriceList2 : SAPB1.PriceList [Partner=StockTransfers]

# SAPB1.StockTransfer_ApprovalRequest (ComplexType)

## Properties

- ApprovalTemplatesID : Edm.Int32
- Remarks : Edm.String
- ApprovalTemplatesName : Edm.String
- ActiveForUpdate : SAPB1.BoYesNoEnum

# SAPB1.StockTransferLine (ComplexType)

OpenType: true
Filtered properties: 58

## Properties

- LineNum : Edm.Int32
- DocEntry : Edm.Int32
- ItemCode : Edm.String
- ItemDescription : Edm.String
- Quantity : Edm.Double
- Price : Edm.Double
- Currency : Edm.String
- Rate : Edm.Double
- DiscountPercent : Edm.Double
- VendorNum : Edm.String
- SerialNumber : Edm.String
- WarehouseCode : Edm.String
- FromWarehouseCode : Edm.String
- ProjectCode : Edm.String
- Factor : Edm.Double
- Factor2 : Edm.Double
- Factor3 : Edm.Double
- Factor4 : Edm.Double
- DistributionRule : Edm.String
- DistributionRule2 : Edm.String
- DistributionRule3 : Edm.String
- DistributionRule4 : Edm.String
- DistributionRule5 : Edm.String
- UseBaseUnits : SAPB1.BoYesNoEnum
- MeasureUnit : Edm.String
- UnitsOfMeasurment : Edm.Double
- BaseType : SAPB1.InvBaseDocTypeEnum
- BaseLine : Edm.Int32
- BaseEntry : Edm.Int32
- UnitPrice : Edm.Double
- UoMEntry : Edm.Int32
- UoMCode : Edm.String
- InventoryQuantity : Edm.Double
- RemainingOpenQuantity : Edm.Double
- RemainingOpenInventoryQuantity : Edm.Double
- LineStatus : SAPB1.BoStatus
- VatGroup : Edm.String
- AdditionalIdentifier : Edm.String
- WeightOfRecycledPlastic : Edm.Double
- PlasticPackageExemptionReason : Edm.String
- SerialNumbers : Collection(SAPB1.SerialNumber)
- BatchNumbers : Collection(SAPB1.BatchNumber)
- CCDNumbers : Collection(SAPB1.CCDNumber)
- StockTransferLinesBinAllocations : Collection(SAPB1.StockTransferLinesBinAllocation)
- DocLinePickLists : Collection(SAPB1.DocLinePickList)

# SAPB1.StockTransferLinesBinAllocation (ComplexType)

OpenType: true

## Properties

- BinAbsEntry : Edm.Int32
- Quantity : Edm.Double
- AllowNegativeQuantity : SAPB1.BoYesNoEnum
- SerialAndBatchNumbersBaseLine : Edm.Int32
- BinActionType : SAPB1.BinActionTypeEnum
- BaseLineNumber : Edm.Int32

# SAPB1.StockTransferParams (ComplexType)

## Properties

- DocEntry : Edm.Int32

# SAPB1.StockTransferTaxExtension (ComplexType)

OpenType: true
Filtered properties: 4

## Properties

- SupportVAT : SAPB1.BoYesNoEnum
- FormNumber : Edm.String
- TransactionCategory : Edm.String

# SAPB1.SupportUserLoginRecord (ComplexType)

## Properties

- ID : Edm.Int32
- RealName : Edm.String
- LogReason : SAPB1.SupportUserLoginRecordLogReasonTypeEnum
- LogDetail : Edm.String

# SAPB1.TableInfo (ComplexType)

## Properties

- Name : Edm.String

# SAPB1.TargetGroup (EntityType)

Key: TargetGroupCode

## Properties

- TargetGroupCode : Edm.String [required]
- TargetGroupName : Edm.String
- TargetGroupType : SAPB1.TargetGroupTypeEnum
- TargetGroupsDetails : Collection(SAPB1.TargetGroupsDetail)

## Navigation properties

- Campaigns : Collection(SAPB1.Campaign) [Partner=TargetGroup2]

# SAPB1.TargetGroupParams (ComplexType)

## Properties

- TargetGroupCode : Edm.String
- TargetGroupName : Edm.String

# SAPB1.TargetGroupsDetail (ComplexType)

## Properties

- TargetGroupCode : Edm.String
- BusinessPartnerCode : Edm.String
- BusinessPartnerName : Edm.String
- GroupCode : Edm.String
- Industry : Edm.String
- ActiveStatus : SAPB1.TargetGroupsDetailStatusEnum
- ContactPerson : Edm.String
- Title : Edm.String
- Position : Edm.String
- E_Mail : Edm.String
- Telephone : Edm.String
- MobilePhone : Edm.String
- Fax : Edm.String
- Address : Edm.String
- Street : Edm.String
- Block : Edm.String
- City : Edm.String
- ZipCode : Edm.String
- County : Edm.String
- State : Edm.String
- Country : Edm.String
- Building : Edm.String

# SAPB1.TaxCodeDetermination (EntityType)

Key: DocEntry

## Properties

- DocEntry : Edm.Int32 [required]
- LineNumber : Edm.Int32
- DocumentType : SAPB1.BoTCDDocumentTypeEnum
- BusinessArea : SAPB1.BoBusinessAreaEnum
- Condition1 : SAPB1.BoTCDConditionEnum
- UDFTable1 : Edm.String
- NumberValue1 : Edm.Int32
- StringValue1 : Edm.String
- MoneyValue1 : Edm.Double
- Condition2 : SAPB1.BoTCDConditionEnum
- UDFTable2 : Edm.String
- NumberValue2 : Edm.Int32
- StringValue2 : Edm.String
- MoneyValue2 : Edm.Double
- Condition3 : SAPB1.BoTCDConditionEnum
- UDFTable3 : Edm.String
- NumberValue3 : Edm.Int32
- StringValue3 : Edm.String
- MoneyValue3 : Edm.Double
- Condition4 : SAPB1.BoTCDConditionEnum
- UDFTable4 : Edm.String
- NumberValue4 : Edm.Int32
- StringValue4 : Edm.String
- MoneyValue4 : Edm.Double
- Condition5 : SAPB1.BoTCDConditionEnum
- UDFTable5 : Edm.String
- NumberValue5 : Edm.Int32
- StringValue5 : Edm.String
- MoneyValue5 : Edm.Double
- Description : Edm.String
- TaxCode : Edm.String
- FreightRowTax : Edm.String
- FreightHeaderTax : Edm.String
- UDFAlias1 : Edm.String
- UDFAlias2 : Edm.String
- UDFAlias3 : Edm.String
- UDFAlias4 : Edm.String
- UDFAlias5 : Edm.String

# SAPB1.TaxCodeDeterminationParams (ComplexType)

## Properties

- DocEntry : Edm.Int32

# SAPB1.TaxCodeDeterminationTCD (EntityType)

Key: AbsId

## Properties

- AbsId : Edm.Int32 [required]
- TcdType : SAPB1.TaxCodeDeterminationTCDTypeEnum
- DftArCode : Edm.String
- DftApCode : Edm.String
- TaxCodeDeterminationTCDDefaultWTs : Collection(SAPB1.TaxCodeDeterminationTCDDefaultWT)
- TaxCodeDeterminationTCDByUsages : Collection(SAPB1.TaxCodeDeterminationTCDByUsage)
- TaxCodeDeterminationTCDKeyFields : Collection(SAPB1.TaxCodeDeterminationTCDKeyField)

# SAPB1.TaxCodeDeterminationTCDByUsage (ComplexType)

## Properties

- AbsId : Edm.Int32
- UsageCode : Edm.Int32
- TaxCode : Edm.String
- ExpTaxCode : Edm.String
- Type : SAPB1.TaxCodeDeterminationTCDByUsageTypeEnum
- PurTaxCode : Edm.String

# SAPB1.TaxCodeDeterminationTCDDefaultWT (ComplexType)

## Properties

- AbsId : Edm.Int32
- WTCode : Edm.String
- Type : SAPB1.TaxCodeDeterminationTCDDefaultWTTypeEnum

# SAPB1.TaxCodeDeterminationTCDKeyField (ComplexType)

## Properties

- AbsId : Edm.Int32
- Descr : Edm.String
- Priority : Edm.Int32
- KeyFld_1 : Edm.Int32
- UDFTable_1 : Edm.String
- UDFAlias_1 : Edm.String
- KeyFld_2 : Edm.Int32
- UDFTable_2 : Edm.String
- UDFAlias_2 : Edm.String
- KeyFld_3 : Edm.Int32
- UDFTable_3 : Edm.String
- UDFAlias_3 : Edm.String
- KeyFld_4 : Edm.Int32
- UDFTable_4 : Edm.String
- UDFAlias_4 : Edm.String
- LegalText : Edm.String
- KeyFld_5 : Edm.Int32
- UDFTable_5 : Edm.String
- UDFAlias_5 : Edm.String
- TaxCodeDeterminationTCDKeyFieldValues : Collection(SAPB1.TaxCodeDeterminationTCDKeyFieldValue)

# SAPB1.TaxCodeDeterminationTCDKeyFieldValue (ComplexType)

## Properties

- AbsId : Edm.Int32
- DispOrder : Edm.Int32
- KeyFld_1_V : Edm.String
- KeyFld_2_V : Edm.String
- KeyFld_3_V : Edm.String
- KeyFld_4_V : Edm.String
- KeyFld_5_V : Edm.String
- TaxCodeDeterminationTCDKeyFieldValuePeriods : Collection(SAPB1.TaxCodeDeterminationTCDKeyFieldValuePeriod)
- TaxCodeDeterminationTCDKeyFieldValueDefaultWTs : Collection(SAPB1.TaxCodeDeterminationTCDKeyFieldValueDefaultWT)

# SAPB1.TaxCodeDeterminationTCDKeyFieldValueDefaultWT (ComplexType)

## Properties

- AbsId : Edm.Int32
- WTCode : Edm.String

# SAPB1.TaxCodeDeterminationTCDKeyFieldValuePeriod (ComplexType)

## Properties

- AbsId : Edm.Int32
- EfctFrom : Edm.DateTimeOffset
- EfctTo : Edm.DateTimeOffset
- TaxCode : Edm.String
- TaxCodeDeterminationTCDKeyFieldValuePeriodByUsages : Collection(SAPB1.TaxCodeDeterminationTCDKeyFieldValuePeriodByUsage)

# SAPB1.TaxCodeDeterminationTCDKeyFieldValuePeriodByUsage (ComplexType)

## Properties

- AbsId : Edm.Int32
- UsageCode : Edm.Int32
- TaxCode : Edm.String
- ExpTaxCode : Edm.String
- PurTaxCode : Edm.String

# SAPB1.TaxCodeDeterminationTCDParams (ComplexType)

## Properties

- AbsId : Edm.Int32

# SAPB1.TaxDefinition (ComplexType)

OpenType: true

## Properties

- Effectivefrom : Edm.DateTimeOffset
- Rate : Edm.Double

# SAPB1.TaxExemptReason (EntityType)

Key: Code

## Properties

- Code : Edm.String [required]
- Description : Edm.String

## Navigation properties

- VatGroups : Collection(SAPB1.VatGroup) [Partner=TaxExemptReason]

# SAPB1.TaxExemptReasonParams (ComplexType)

## Properties

- Code : Edm.String

# SAPB1.TaxExtension (ComplexType)

## Properties

- TaxId0 : Edm.String
- TaxId1 : Edm.String
- TaxId2 : Edm.String
- TaxId3 : Edm.String
- TaxId4 : Edm.String
- TaxId5 : Edm.String
- TaxId6 : Edm.String
- TaxId7 : Edm.String
- TaxId8 : Edm.String
- TaxId9 : Edm.String
- State : Edm.String
- County : Edm.String
- Incoterms : Edm.String
- Vehicle : Edm.String
- VehicleState : Edm.String
- NFRef : Edm.String
- Carrier : Edm.String
- PackQuantity : Edm.Int32
- PackDescription : Edm.String
- Brand : Edm.String
- ShipUnitNo : Edm.Int32
- NetWeight : Edm.Double
- GrossWeight : Edm.Double
- StreetS : Edm.String
- BlockS : Edm.String
- BuildingS : Edm.String
- CityS : Edm.String
- ZipCodeS : Edm.String
- CountyS : Edm.String
- StateS : Edm.String
- CountryS : Edm.String
- StreetB : Edm.String
- BlockB : Edm.String
- BuildingB : Edm.String
- CityB : Edm.String
- ZipCodeB : Edm.String
- CountyB : Edm.String
- StateB : Edm.String
- CountryB : Edm.String
- ImportOrExport : SAPB1.BoYesNoEnum
- MainUsage : Edm.Int32
- GlobalLocationNumberS : Edm.String
- GlobalLocationNumberB : Edm.String
- TaxId12 : Edm.String
- TaxId13 : Edm.String
- BillOfEntryNo : Edm.String
- BillOfEntryDate : Edm.DateTimeOffset
- OriginalBillOfEntryNo : Edm.String
- OriginalBillOfEntryDate : Edm.DateTimeOffset
- ImportOrExportType : SAPB1.ImportOrExportTypeEnum
- PortCode : Edm.String
- DocEntry : Edm.Int32
- BoEValue : Edm.Double
- ClaimRefund : SAPB1.BoYesNoEnum
- DifferentialOfTaxRate : Edm.Int32
- IsIGSTAccount : SAPB1.BoYesNoEnum
- TaxId14 : Edm.String

# SAPB1.TaxInvoiceReport (EntityType)

Key: TaxInvoiceReportNumber

## Properties

- NTSApproval : SAPB1.TaxInvoiceReportNTSApprovedEnum
- ETaxWebSite : Edm.Int32
- ETaxNo : Edm.String
- NTSApprovalNo : Edm.String
- OriginalNTSApprovalNo : Edm.String
- Remarks : Edm.String
- TaxInvoiceReportNumber : Edm.String [required]
- Date : Edm.DateTimeOffset
- BusinessPlace : Edm.Int32
- BPCode : Edm.String
- BPName : Edm.String
- BaseAmount : Edm.Double
- TaxAmount : Edm.Double
- Canceled : Edm.String
- ReportType : Edm.Int32
- TaxInvoiceReportLineCollection : Collection(SAPB1.TaxInvoiceReportLine)

## Navigation properties

- TaxWebSite : SAPB1.TaxWebSite [Partner=TaxInvoiceReport]

# SAPB1.TaxInvoiceReportLine (ComplexType)

## Properties

- DocumentType : Edm.Int32
- DocumentEntry : Edm.Int32
- LineType : SAPB1.TaxInvoiceReportLineTypeEnum
- BaseAmount : Edm.Double
- TaxAmount : Edm.Double
- ItemQuantity : Edm.Double
- ItemNo : Edm.String
- ItemDescription : Edm.String
- TaxCode : Edm.String
- DocumentDate : Edm.DateTimeOffset
- ItemPrice : Edm.Double
- LineNumber : Edm.Int32
- Currency : Edm.String
- BusinessPlace : Edm.Int32
- TaxInvoiceReportNumber : Edm.String
- BPCode : Edm.String
- BPName : Edm.String
- Legacy : Edm.String

# SAPB1.TaxInvoiceReportParams (ComplexType)

## Properties

- TaxInvoiceReportNumber : Edm.String

# SAPB1.TaxReplStateSubData (EntityType)

Key: State

## Properties

- State : Edm.String [required]
- IEST : Edm.String

# SAPB1.TaxReplStateSubParams (ComplexType)

## Properties

- State : Edm.String

# SAPB1.TaxReportAccount (ComplexType)

## Properties

- Code : Edm.String

# SAPB1.TaxReportBusinessPartner (ComplexType)

## Properties

- Code : Edm.String

# SAPB1.TaxReportDocument (ComplexType)

## Properties

- DocumentType : SAPB1.TaxReportFilterDocumentType
- FromNumber : Edm.Int32
- ToNumber : Edm.Int32

# SAPB1.TaxReportFilter (EntityType)

Key: Code

## Properties

- Code : Edm.Int32 [required]
- Name : Edm.String
- ReportLayout : SAPB1.TaxReportFilterReportLayoutType
- FirstPrintedNumber : Edm.Int32
- FromDate : Edm.DateTimeOffset
- ToDate : Edm.DateTimeOffset
- TaxDate : SAPB1.BoYesNoEnum
- RoundAmount : SAPB1.BoYesNoEnum
- DeclarationType : SAPB1.TaxReportFilterDeclarationType
- FilterType : SAPB1.TaxReportFilterType
- ExcludeWT : SAPB1.BoYesNoEnum
- IncludeCustomers : SAPB1.BoYesNoEnum
- IncludeVendors : SAPB1.BoYesNoEnum
- Period : SAPB1.TaxReportFilterPeriod
- Quarter : Edm.Int32
- Year : Edm.Int32
- DocumentType : SAPB1.TaxReportFilterApArDocumentType
- FirstRegisterNumber : Edm.Int32
- IncludeGLAccounts : SAPB1.BoYesNoEnum
- AppendixOorPSelection : SAPB1.BoYesNoEnum
- OpeningAndClosingBalance : SAPB1.BoYesNoEnum
- FromSeries : Edm.Int32
- ToSeries : Edm.Int32
- Cancellation : SAPB1.BoYesNoEnum
- HideTaxWithoutTransaction : SAPB1.BoYesNoEnum
- IncludeSeriesFilter : SAPB1.BoYesNoEnum
- IncludeDocumentType : SAPB1.BoYesNoEnum
- DiplayCreditMemosInSeparateColumn : SAPB1.BoYesNoEnum
- ShowPaymentsWithDeferredTax : SAPB1.BoYesNoEnum
- QuarterOrDates : SAPB1.TaxReportFilterQuarterOrDates
- TaxReportGroups : Collection(SAPB1.TaxReportGroup)
- TaxReportBusinessPartners : Collection(SAPB1.TaxReportBusinessPartner)
- TaxReportDocuments : Collection(SAPB1.TaxReportDocument)
- TaxReportSeriesCollection : Collection(SAPB1.TaxReportSeries)
- TaxReportAccounts : Collection(SAPB1.TaxReportAccount)

# SAPB1.TaxReportFilterParams (ComplexType)

## Properties

- Code : Edm.Int32
- Name : Edm.String
- FilterType : SAPB1.TaxReportFilterType

# SAPB1.TaxReportGroup (ComplexType)

## Properties

- Code : Edm.String
- Sum : SAPB1.BoYesNoEnum

# SAPB1.TaxReportSeries (ComplexType)

## Properties

- DocumentType : SAPB1.TaxReportFilterDocumentType
- SeriesCode : Edm.Int32

# SAPB1.TaxWebSite (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- WebSiteName : Edm.String
- WebSiteURL : Edm.String
- Description : Edm.String

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=TaxWebSite]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=TaxWebSite]
- Drafts : Collection(SAPB1.Document) [Partner=TaxWebSite]
- CreditNotes : Collection(SAPB1.Document) [Partner=TaxWebSite]
- Invoices : Collection(SAPB1.Document) [Partner=TaxWebSite]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=TaxWebSite]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=TaxWebSite]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=TaxWebSite]
- Orders : Collection(SAPB1.Document) [Partner=TaxWebSite]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=TaxWebSite]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=TaxWebSite]
- Returns : Collection(SAPB1.Document) [Partner=TaxWebSite]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=TaxWebSite]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=TaxWebSite]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=TaxWebSite]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=TaxWebSite]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=TaxWebSite]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=TaxWebSite]
- DownPayments : Collection(SAPB1.Document) [Partner=TaxWebSite]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=TaxWebSite]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=TaxWebSite]
- ReturnRequest : Collection(SAPB1.Document) [Partner=TaxWebSite]
- Quotations : Collection(SAPB1.Document) [Partner=TaxWebSite]
- TaxInvoiceReport : Collection(SAPB1.TaxInvoiceReport) [Partner=TaxWebSite]
- SelfInvoices : Collection(SAPB1.Document) [Partner=TaxWebSite]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=TaxWebSite]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=TaxWebSite]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=TaxWebSite]

# SAPB1.TaxWebSiteParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- WebSiteName : Edm.String

# SAPB1.Team (EntityType)

OpenType: true
Key: TeamID

## Properties

- TeamID : Edm.Int32 [required]
- TeamName : Edm.String
- Description : Edm.String
- TeamMembers : Collection(SAPB1.TeamMember)

# SAPB1.TeamCounter (ComplexType)

## Properties

- DocumentEntry : Edm.Int32
- CounterID : Edm.Int32
- CounterType : SAPB1.CounterTypeEnum
- CounterName : Edm.String
- CounterNumber : Edm.Int32
- CounterVisualOrder : Edm.Int32

# SAPB1.TeamMember (ComplexType)

OpenType: true

## Properties

- TeamID : Edm.Int32
- EmployeeID : Edm.Int32
- RoleInTeam : SAPB1.BoRoleInTeam

# SAPB1.TeamParams (ComplexType)

## Properties

- TeamID : Edm.Int32

# SAPB1.TechnicianSchedulings (ComplexType)

## Properties

- ServiceCallID : Edm.Int32
- SchedulingLineNum : Edm.Int32
- StartDate : Edm.DateTimeOffset
- EndDate : Edm.DateTimeOffset
- IsClosed : SAPB1.BoYesNoEnum

# SAPB1.TechnicianSchedulingsParams (ComplexType)

## Properties

- Technician : Edm.Int32
- StartDate : Edm.DateTimeOffset
- EndDate : Edm.DateTimeOffset

# SAPB1.TechnicianSettings (ComplexType)

## Properties

- Technician : Edm.Int32
- GroupCode : Edm.Int32

# SAPB1.TechnicianSettingsGroup (ComplexType)

## Properties

- Code : Edm.Int32
- Name : Edm.String
- CustomizedGroup : SAPB1.BoYesNoEnum
- EnableEditTime : SAPB1.BoYesNoEnum
- EnableReject : SAPB1.BoYesNoEnum
- EnableResign : SAPB1.BoYesNoEnum
- EnableFollowup : SAPB1.BoYesNoEnum
- EnableSignature : SAPB1.BoYesNoEnum
- EnableStarRating : SAPB1.BoYesNoEnum
- EnableActualDuration : SAPB1.BoYesNoEnum
- AdvancedDashBoard : Edm.Int32

# SAPB1.TechnicianSettingsGroupParams (ComplexType)

## Properties

- Code : Edm.Int32
- Name : Edm.String

# SAPB1.TechnicianSettingsParams (ComplexType)

## Properties

- Technician : Edm.Int32

# SAPB1.TerminationReason (EntityType)

Key: ReasonID

## Properties

- ReasonID : Edm.Int32 [required]
- Name : Edm.String
- Description : Edm.String

## Navigation properties

- EmployeesInfo : Collection(SAPB1.EmployeeInfo) [Partner=TerminationReason]

# SAPB1.TerminationReasonParams (ComplexType)

## Properties

- ReasonID : Edm.Int32
- Name : Edm.String
- Description : Edm.String

# SAPB1.Territory (EntityType)

OpenType: true
Key: TerritoryID

## Properties

- TerritoryID : Edm.Int32 [required]
- Description : Edm.String
- LocationIndex : Edm.Int32
- Inactive : SAPB1.BoYesNoEnum
- Parent : Edm.Int32

## Navigation properties

- CustomerEquipmentCards : Collection(SAPB1.CustomerEquipmentCard) [Partner=Territory]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=Territory2]
- ProjectManagements : Collection(SAPB1.PM_ProjectDocumentData) [Partner=Territory2]
- SalesOpportunities : Collection(SAPB1.SalesOpportunities) [Partner=Territory2]

# SAPB1.TerritoryParams (ComplexType)

## Properties

- TerritoryID : Edm.Int32

# SAPB1.TrackingNote (EntityType)

Key: TrackingNoteNumber

## Properties

- TrackingNoteNumber : Edm.Int32 [required]
- CCDNumber : Edm.String
- Date : Edm.DateTimeOffset
- CustomsTerminal : Edm.String
- CountryOfOrigin : Edm.String
- IsDirectImport : SAPB1.BoYesNoEnum
- TrackingNoteItemCollection : Collection(SAPB1.TrackingNoteItem)
- TrackingNoteBrokerCollection : Collection(SAPB1.TrackingNoteBroker)

# SAPB1.TrackingNoteBroker (ComplexType)

## Properties

- TrackingNoteNumber : Edm.Int32
- TrackingNoteLineNumber : Edm.Int32
- BPCode : Edm.String
- AgreementNumber : Edm.Int32

# SAPB1.TrackingNoteItem (ComplexType)

## Properties

- TrackingNoteNumber : Edm.Int32
- TrackingNoteLineNumber : Edm.Int32
- ItemCCDNumber : Edm.String
- ItemCode : Edm.String
- Quantity : Edm.Double
- CountryOfOrigin : Edm.String
- CustomsGroupCode : Edm.Int32
- AccumulatedAPQuantity : Edm.Double
- AccumulatedARQuantity : Edm.Double
- AccumulatedRelocatedQuantity : Edm.Double

# SAPB1.TrackingNoteParams (ComplexType)

## Properties

- TrackingNoteNumber : Edm.Int32
- CCDNumber : Edm.String

# SAPB1.TransactionCode (EntityType)

Key: Code

## Properties

- Code : Edm.String [required]
- Description : Edm.String

## Navigation properties

- ChartOfAccounts : Collection(SAPB1.ChartOfAccount) [Partner=TransactionCode2]
- VendorPayments : Collection(SAPB1.Payment) [Partner=TransactionCode2]
- PaymentDrafts : Collection(SAPB1.Payment) [Partner=TransactionCode2]
- JournalEntries : Collection(SAPB1.JournalEntry) [Partner=TransactionCode2]
- IncomingPayments : Collection(SAPB1.Payment) [Partner=TransactionCode2]

# SAPB1.TransactionCodeParams (ComplexType)

## Properties

- Code : Edm.String
- Description : Edm.String

# SAPB1.TranslationsInUserLanguage (ComplexType)

OpenType: true

## Properties

- KeyFromHeaderTable : Edm.Int32
- LanguageCodeOfUserLanguage : Edm.Int32
- Translationscontent : Edm.String

# SAPB1.TransportationDocumentData (EntityType)

Key: TranspDocNumber

## Properties

- TranspDocNumber : Edm.Int32 [required]
- NextNumber : Edm.Int32
- PostDate : Edm.DateTimeOffset
- ElDocGenType : SAPB1.ElectronicDocGenTypeEnum
- ElDocExportFormat : Edm.Int32
- TransportationNumber : Edm.String
- ExpirationDate : Edm.DateTimeOffset
- VehicleID : Edm.String
- TrailerID : Edm.String
- CarrierCode : Edm.String
- IssueGate : Edm.Int32
- AttachmentEntry : Edm.Int32
- Canceled : SAPB1.BoYesNoEnum
- Weight : Edm.Double
- WeightUnit : Edm.Int32
- TransportedTotalLC : Edm.Double
- WarehouseCode : Edm.String
- COTCode : Edm.String
- TransportationDocumentLineDataCollection : Collection(SAPB1.TransportationDocumentLineData)
- ElectronicProtocols : Collection(SAPB1.ElectronicProtocol)

# SAPB1.TransportationDocumentLineData (ComplexType)

## Properties

- TranspDocNumber : Edm.Int32
- LineID : Edm.Int32
- DocType : SAPB1.DocumentObjectTypeEnum
- DocNumber : Edm.Int32
- DocLineNumber : Edm.Int32
- ItemCode : Edm.String
- TransportedQuantity : Edm.Double
- DocOrderNum : Edm.Int32

# SAPB1.TransportationDocumentParams (ComplexType)

## Properties

- TranspDocNumber : Edm.Int32

# SAPB1.TSRExceptionalEvent (EntityType)

Key: Code

## Properties

- Code : Edm.String [required]
- Description : Edm.String

# SAPB1.TSRExceptionalEventParams (ComplexType)

## Properties

- Code : Edm.String

# SAPB1.UnitOfMeasurement (EntityType)

OpenType: true
Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- Code : Edm.String
- Name : Edm.String
- Length1 : Edm.Double
- Length1Unit : Edm.Int32
- Length2 : Edm.Double
- Length2Unit : Edm.Int32
- Width1 : Edm.Double
- Width1Unit : Edm.Int32
- Width2 : Edm.Double
- Width2Unit : Edm.Int32
- Height1 : Edm.Double
- Height1Unit : Edm.Int32
- Height2 : Edm.Double
- Height2Unit : Edm.Int32
- Volume : Edm.Double
- VolumeUnit : Edm.Int32
- Weight1 : Edm.Double
- Weight1Unit : Edm.Int32
- Weight2 : Edm.Double
- Weight2Unit : Edm.Int32
- InternationalSymbol : Edm.String
- EWBUnitEntry : Edm.Int32
- PPWeight1 : Edm.Double
- PPWe1Unit : Edm.Int32
- PPWeight2 : Edm.Double
- PPWe2Unit : Edm.Int32

## Navigation properties

- UnitOfMeasurementGroups : Collection(SAPB1.UnitOfMeasurementGroup) [Partner=UnitOfMeasurement]
- BinLocations : Collection(SAPB1.BinLocation) [Partner=UnitOfMeasurement]
- ProductionOrders : Collection(SAPB1.ProductionOrder) [Partner=UnitOfMeasurement]
- BarCodes : Collection(SAPB1.BarCode) [Partner=UnitOfMeasurement]
- Items : Collection(SAPB1.Item) [Partner=UnitOfMeasurement]
- ItemGroups : Collection(SAPB1.ItemGroups) [Partner=UnitOfMeasurement]

# SAPB1.UnitOfMeasurementGroup (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- Code : Edm.String
- Name : Edm.String
- BaseUoM : Edm.Int32
- UoMGroupDefinitionCollection : Collection(SAPB1.UoMGroupDefinition)

## Navigation properties

- UnitOfMeasurement : SAPB1.UnitOfMeasurement [Partner=UnitOfMeasurementGroups]
- BinLocations : Collection(SAPB1.BinLocation) [Partner=UnitOfMeasurementGroup]
- Items : Collection(SAPB1.Item) [Partner=UnitOfMeasurementGroup]
- ItemGroups : Collection(SAPB1.ItemGroups) [Partner=UnitOfMeasurementGroup]

# SAPB1.UnitOfMeasurementGroupParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- Code : Edm.String

# SAPB1.UnitOfMeasurementParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- Code : Edm.String

# SAPB1.UoMGroupDefinition (ComplexType)

## Properties

- AlternateUoM : Edm.Int32
- AlternateQuantity : Edm.Double
- BaseQuantity : Edm.Double
- WeightFactor : Edm.Int32
- UdfFactor : Edm.Int32
- Active : SAPB1.BoYesNoEnum
- BaseUdfFtr : Edm.Int32
- BaseWgtFtr : Edm.Int32

# SAPB1.UoMPrice (ComplexType)

OpenType: true

## Properties

- PriceList : Edm.Int32
- UoMEntry : Edm.Int32
- ReduceBy : Edm.Double
- Price : Edm.Double
- Currency : Edm.String
- AdditionalReduceBy1 : Edm.Double
- AdditionalPrice1 : Edm.Double
- AdditionalCurrency1 : Edm.String
- AdditionalReduceBy2 : Edm.Double
- AdditionalPrice2 : Edm.Double
- AdditionalCurrency2 : Edm.String
- Auto : SAPB1.BoYesNoEnum

# SAPB1.UpdateUserLicenseParams (ComplexType)

## Properties

- UserName : Edm.String
- LicenseType : SAPB1.LicenseTypeEnum
- LicenseUpdateType : SAPB1.LicenseUpdateTypeEnum

# SAPB1.User (EntityType)

OpenType: true
Key: InternalKey
Filtered properties: 4

## Properties

- InternalKey : Edm.Int32 [required]
- UserPassword : Edm.String
- UserCode : Edm.String
- UserName : Edm.String
- Superuser : SAPB1.BoYesNoEnum
- eMail : Edm.String
- MobilePhoneNumber : Edm.String
- Defaults : Edm.String
- FaxNumber : Edm.String
- Branch : Edm.Int32
- Department : Edm.Int32
- LanguageCode : SAPB1.BoSuppLangs
- Locked : SAPB1.BoYesNoEnum
- Group : SAPB1.BoUserGroup
- MaxDiscountGeneral : Edm.Double
- MaxDiscountSales : Edm.Double
- MaxDiscountPurchase : Edm.Double
- CashLimit : SAPB1.BoYesNoEnum
- MaxCashAmtForIncmngPayts : Edm.Double
- LastLogoutDate : Edm.DateTimeOffset
- LastLoginTime : Edm.TimeOfDay
- LastLogoutTime : Edm.TimeOfDay
- LastPasswordChangeTime : Edm.TimeOfDay
- LastPasswordChangedBy : Edm.String
- NaturalPer : SAPB1.BoYesNoEnum
- UserPermission : Collection(SAPB1.UserPermissionItem)
- UserActionRecord : Collection(SAPB1.UserActionRecordItem)
- UserGroupByUser : Collection(SAPB1.UserGroupByUserItem)
- UserBranchAssignment : Collection(SAPB1.UserBranchAssignmentItem)

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=User]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=User]
- Drafts : Collection(SAPB1.Document) [Partner=User]
- ApprovalRequests : Collection(SAPB1.ApprovalRequest) [Partner=User]
- Activities : Collection(SAPB1.Activity) [Partner=User]
- UserPermissionTree : Collection(SAPB1.UserPermissionTree) [Partner=User]
- MaterialRevaluation : Collection(SAPB1.MaterialRevaluation) [Partner=User]
- Cockpits : Collection(SAPB1.Cockpit) [Partner=User]
- ProductionOrders : Collection(SAPB1.ProductionOrder) [Partner=User]
- Branch2 : SAPB1.Branch [Partner=Users]
- Department2 : SAPB1.Department [Partner=Users]
- SalesTaxAuthorities : Collection(SAPB1.SalesTaxAuthority) [Partner=User]
- SalesTaxAuthoritiesTypes : Collection(SAPB1.SalesTaxAuthoritiesType) [Partner=User]
- ISDRecipientInvoices : Collection(SAPB1.ISDRecipientInvoice) [Partner=User]
- SalesTaxCodes : Collection(SAPB1.SalesTaxCode) [Partner=User]
- CreditNotes : Collection(SAPB1.Document) [Partner=User]
- Invoices : Collection(SAPB1.Document) [Partner=User]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=User]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=User]
- WizardPaymentMethods : Collection(SAPB1.WizardPaymentMethod) [Partner=User]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=User]
- Orders : Collection(SAPB1.Document) [Partner=User]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=User]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=User]
- PickLists : Collection(SAPB1.PickList) [Partner=User]
- Returns : Collection(SAPB1.Document) [Partner=User]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=User]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=User]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=User]
- EmployeesInfo : Collection(SAPB1.EmployeeInfo) [Partner=User]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=User]
- KnowledgeBaseSolutions : Collection(SAPB1.KnowledgeBaseSolution) [Partner=User]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=User]
- ServiceContracts : Collection(SAPB1.ServiceContract) [Partner=User]
- ServiceCalls : Collection(SAPB1.ServiceCall) [Partner=User]
- Queue : Collection(SAPB1.Queue) [Partner=User]
- DownPayments : Collection(SAPB1.Document) [Partner=User]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=User]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=User]
- ReturnRequest : Collection(SAPB1.Document) [Partner=User]
- Quotations : Collection(SAPB1.Document) [Partner=User]
- DatevRuns : Collection(SAPB1.DatevRun) [Partner=User]
- ISDDocuments : Collection(SAPB1.ISDDocument) [Partner=User]
- SalesOpportunities : Collection(SAPB1.SalesOpportunities) [Partner=User]
- ISDInvoices : Collection(SAPB1.ISDInvoice) [Partner=User]
- ISDCreditMemos : Collection(SAPB1.ISDCreditMemo) [Partner=User]
- ISDRecipientCreditMemos : Collection(SAPB1.ISDRecipientCreditMemo) [Partner=User]
- SelfInvoices : Collection(SAPB1.Document) [Partner=User]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=User]
- Contacts : Collection(SAPB1.Contact) [Partner=User]
- BankPages : Collection(SAPB1.BankPage) [Partner=User]
- FormPreferences : Collection(SAPB1.ColumnPreferences) [Partner=User2]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=User]
- LegalData : Collection(SAPB1.LegalData) [Partner=User]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=User]
- UserDefaultGroups : Collection(SAPB1.UserDefaultGroup) [Partner=User]

# SAPB1.UserAccessLog (ComplexType)

## Properties

- UserCode : Edm.String
- Action : SAPB1.UserActionTypeEnum
- ActionBy : Edm.String
- ClientIP : Edm.String
- ClientName : Edm.String
- ActionDate : Edm.DateTimeOffset
- ActionTime : Edm.TimeOfDay
- WinUsrName : Edm.String
- WinSessnID : Edm.Int32
- ProcName : Edm.String
- ProcessID : Edm.Int32
- SessionID : Edm.Int32
- ReasonID : SAPB1.UserAccessLogReasonIDTypeEnum
- ReasonDesc : Edm.String
- Source : Edm.String
- UserID : Edm.Int32

# SAPB1.UserActionRecordItem (ComplexType)

OpenType: true

## Properties

- UserCode : Edm.String
- Action : SAPB1.UserActionTypeEnum
- ActionBy : Edm.String
- ClientIP : Edm.String
- ClientName : Edm.String
- ActionDate : Edm.DateTimeOffset
- ActionTime : Edm.TimeOfDay
- WindowsSession : Edm.Int32
- WindowsUser : Edm.String
- ProcessName : Edm.String
- ProcessID : Edm.Int32
- AliveDuration : Edm.Int32

# SAPB1.UserBranchAssignmentItem (ComplexType)

OpenType: true

## Properties

- UserCode : Edm.String
- BPLID : Edm.Int32

# SAPB1.UserDefaultGroup (EntityType)

OpenType: true
Key: Code

## Properties

- Code : Edm.String [required]
- Name : Edm.String
- Warehouse : Edm.String
- SalesEmployee : Edm.Int32
- BPforInvoicePayment : Edm.String
- CashAccount : Edm.String
- CheckingAcct : Edm.String
- PrintReceipt : SAPB1.BoPrintReceiptEnum
- PrintInvoiceandPaymentinS : SAPB1.BoYesNoEnum
- WindowsColor : Edm.Int32
- Address : Edm.String
- Country : Edm.String
- PrintingHeader : Edm.String
- PhoneNumber1 : Edm.String
- PhoneNumber2 : Edm.String
- FaxNumber : Edm.String
- eMail : Edm.String
- AddressinForeignLanguage : Edm.String
- PrintingHeaderInForeignLangu : Edm.String
- PhoneNumber1ForeignLang : Edm.String
- PhoneNumber2ForeignLang : Edm.String
- FaxNumberForeignLang : Edm.String
- DefaultTaxCode : Edm.String
- AdditionalIdNumber : Edm.String
- UserSignature : Edm.Int32
- UseTax : SAPB1.BoYesNoEnum
- UseWarehouseAddressinAPD : SAPB1.BoYesNoEnum
- BPLID : Edm.Int32
- AssetInDoc : SAPB1.BoYesNoEnum
- LanguageCode : SAPB1.BoSuppLangs
- DefaultDocuments : Collection(SAPB1.DefaultDocument)
- DefaultCreditCards : Collection(SAPB1.DefaultCreditCard)

## Navigation properties

- Warehouse2 : SAPB1.Warehouse [Partner=UserDefaultGroups]
- SalesPerson : SAPB1.SalesPerson [Partner=UserDefaultGroups]
- BusinessPartner : SAPB1.BusinessPartner [Partner=UserDefaultGroups]
- Country2 : SAPB1.Country [Partner=UserDefaultGroups]
- SalesTaxCode : SAPB1.SalesTaxCode [Partner=UserDefaultGroups]
- User : SAPB1.User [Partner=UserDefaultGroups]
- BusinessPlace : SAPB1.BusinessPlace [Partner=UserDefaultGroups]
- UserLanguage : SAPB1.UserLanguage [Partner=UserDefaultGroups]

# SAPB1.UserDefaultGroupParams (ComplexType)

## Properties

- Code : Edm.String

# SAPB1.UserFieldMD (EntityType)

Key: TableName, FieldID

## Properties

- Name : Edm.String
- Type : SAPB1.BoFieldTypes
- Size : Edm.Int32
- Description : Edm.String
- SubType : SAPB1.BoFldSubTypes
- LinkedTable : Edm.String
- DefaultValue : Edm.String
- TableName : Edm.String [required]
- FieldID : Edm.Int32 [required]
- EditSize : Edm.Int32
- Mandatory : SAPB1.BoYesNoEnum
- LinkedUDO : Edm.String
- LinkedSystemObject : SAPB1.UDFLinkedSystemObjectTypesEnum
- ValidValuesMD : Collection(SAPB1.ValidValueMD)

## Navigation properties

- UserTablesMD : SAPB1.UserTablesMD [Partner=UserFieldsMD]

# SAPB1.UserFieldMDParams (ComplexType)

## Properties

- TableName : Edm.String
- FieldID : Edm.Int32

# SAPB1.UserGroup (EntityType)

Key: UserGroupId

## Properties

- UserGroupId : Edm.Int32 [required]
- UserGroupName : Edm.String
- UserGroupDec : Edm.String
- TPLId : Edm.Int32
- StartDate : Edm.DateTimeOffset
- DueDate : Edm.DateTimeOffset
- UserGroupType : SAPB1.UserGroupCategoryEnum

# SAPB1.UserGroupByUserItem (ComplexType)

OpenType: true

## Properties

- USERId : Edm.Int32
- GroupId : Edm.Int32
- StartDate : Edm.DateTimeOffset
- DueDate : Edm.DateTimeOffset

# SAPB1.UserGroupParams (ComplexType)

## Properties

- UserGroupId : Edm.Int32
- UserGroupName : Edm.String

# SAPB1.UserKeysMD (EntityType)

OpenType: true
Key: TableName, KeyIndex

## Properties

- TableName : Edm.String [required]
- KeyIndex : Edm.Int32 [required]
- KeyName : Edm.String
- Unique : SAPB1.BoYesNoEnum
- UserKeysMD_Elements : Collection(SAPB1.UserKeysMD_Element)

# SAPB1.UserKeysMD_Element (ComplexType)

OpenType: true

## Properties

- SubKeyIndex : Edm.Int32
- ColumnAlias : Edm.String

# SAPB1.UserKeysMDParams (ComplexType)

## Properties

- TableName : Edm.String
- KeyIndex : Edm.Int32

# SAPB1.UserLanguage (EntityType)

OpenType: true
Key: Code

## Properties

- Code : Edm.Int32 [required]
- LanguageShortName : Edm.String
- LanguageFullName : Edm.String
- RelatedSystemLanguage : Edm.Int32

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=UserLanguage]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=UserLanguage]
- Drafts : Collection(SAPB1.Document) [Partner=UserLanguage]
- CreditNotes : Collection(SAPB1.Document) [Partner=UserLanguage]
- Invoices : Collection(SAPB1.Document) [Partner=UserLanguage]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=UserLanguage]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=UserLanguage]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=UserLanguage]
- Orders : Collection(SAPB1.Document) [Partner=UserLanguage]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=UserLanguage]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=UserLanguage]
- Returns : Collection(SAPB1.Document) [Partner=UserLanguage]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=UserLanguage]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=UserLanguage]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=UserLanguage]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=UserLanguage]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=UserLanguage]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=UserLanguage]
- DownPayments : Collection(SAPB1.Document) [Partner=UserLanguage]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=UserLanguage]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=UserLanguage]
- ReturnRequest : Collection(SAPB1.Document) [Partner=UserLanguage]
- Quotations : Collection(SAPB1.Document) [Partner=UserLanguage]
- SelfInvoices : Collection(SAPB1.Document) [Partner=UserLanguage]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=UserLanguage]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=UserLanguage]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=UserLanguage]
- UserDefaultGroups : Collection(SAPB1.UserDefaultGroup) [Partner=UserLanguage]

# SAPB1.UserLanguageParams (ComplexType)

## Properties

- Code : Edm.Int32

# SAPB1.UserMenuItem (ComplexType)

## Properties

- Name : Edm.String
- Position : Edm.Int32
- Type : SAPB1.UserMenuItemTypeEnum
- LinkedObjType : Edm.String
- LinkedObjKey : Edm.String
- LinkedFormMenuID : Edm.Int32
- LinkedFormNum : Edm.Int32
- ReportPath : Edm.String

# SAPB1.UserMenuParams (ComplexType)

## Properties

- UserID : Edm.Int32

# SAPB1.UserObjectMD_ChildTable (ComplexType)

OpenType: true

## Properties

- SonNumber : Edm.Int32
- TableName : Edm.String
- LogTableName : Edm.String
- Code : Edm.String
- ObjectName : Edm.String

# SAPB1.UserObjectMD_EnhancedFormColumn (ComplexType)

OpenType: true

## Properties

- Code : Edm.String
- ColumnNumber : Edm.Int32
- ChildNumber : Edm.Int32
- ColumnAlias : Edm.String
- ColumnDescription : Edm.String
- ColumnIsUsed : SAPB1.BoYesNoEnum
- Editable : SAPB1.BoYesNoEnum

# SAPB1.UserObjectMD_FindColumn (ComplexType)

OpenType: true

## Properties

- ColumnNumber : Edm.Int32
- ColumnAlias : Edm.String
- ColumnDescription : Edm.String
- Code : Edm.String

# SAPB1.UserObjectMD_FormColumn (ComplexType)

OpenType: true

## Properties

- FormColumnAlias : Edm.String
- FormColumnDescription : Edm.String
- FormColumnNumber : Edm.Int32
- SonNumber : Edm.Int32
- Code : Edm.String
- Editable : SAPB1.BoYesNoEnum

# SAPB1.UserObjectsMD (EntityType)

OpenType: true
Key: Code

## Properties

- TableName : Edm.String
- Code : Edm.String [required]
- LogTableName : Edm.String
- CanCreateDefaultForm : SAPB1.BoYesNoEnum
- ObjectType : SAPB1.BoUDOObjType
- ExtensionName : Edm.String
- CanCancel : SAPB1.BoYesNoEnum
- CanDelete : SAPB1.BoYesNoEnum
- CanLog : SAPB1.BoYesNoEnum
- ManageSeries : SAPB1.BoYesNoEnum
- CanFind : SAPB1.BoYesNoEnum
- CanYearTransfer : SAPB1.BoYesNoEnum
- Name : Edm.String
- CanClose : SAPB1.BoYesNoEnum
- OverwriteDllfile : SAPB1.BoYesNoEnum
- UseUniqueFormType : SAPB1.BoYesNoEnum
- CanArchive : SAPB1.BoYesNoEnum
- MenuItem : SAPB1.BoYesNoEnum
- MenuCaption : Edm.String
- FatherMenuID : Edm.Int32
- Position : Edm.Int32
- MenuUID : Edm.String
- EnableEnhancedForm : SAPB1.BoYesNoEnum
- RebuildEnhancedForm : SAPB1.BoYesNoEnum
- FormSRF : Edm.String
- ApplyAuthorization : SAPB1.BoYesNoEnum
- PersonalDataProtection : SAPB1.BoYesNoEnum
- UserObjectMD_ChildTables : Collection(SAPB1.UserObjectMD_ChildTable)
- UserObjectMD_FindColumns : Collection(SAPB1.UserObjectMD_FindColumn)
- UserObjectMD_FormColumns : Collection(SAPB1.UserObjectMD_FormColumn)
- UserObjectMD_EnhancedFormColumns : Collection(SAPB1.UserObjectMD_EnhancedFormColumn)

## Navigation properties

- UserTablesMD : SAPB1.UserTablesMD [Partner=UserObjectsMD]

# SAPB1.UserObjectsMDParams (ComplexType)

## Properties

- Code : Edm.String

# SAPB1.UserParams (ComplexType)

## Properties

- InternalKey : Edm.Int32

# SAPB1.UserPermissionForm (ComplexType)

OpenType: true

## Properties

- FormType : Edm.String
- DisplayOrder : Edm.Int32
- PermissionID : Edm.String

# SAPB1.UserPermissionItem (ComplexType)

OpenType: true

## Properties

- UserCode : Edm.Int32
- PermissionID : Edm.String
- Permission : SAPB1.BoPermission
- EffectivePermission : SAPB1.BoPermission

# SAPB1.UserPermissionTree (EntityType)

OpenType: true
Key: PermissionID

## Properties

- UserSignature : Edm.Int32
- DisplayOrder : Edm.Int32
- PermissionID : Edm.String [required]
- Options : SAPB1.BoUPTOptions
- Name : Edm.String
- Levels : Edm.Int32
- IsItem : SAPB1.BoYesNoEnum
- ParentID : Edm.String
- UserPermissionForms : Collection(SAPB1.UserPermissionForm)

## Navigation properties

- User : SAPB1.User [Partner=UserPermissionTree]

# SAPB1.UserPermissionTreeParams (ComplexType)

## Properties

- PermissionID : Edm.String

# SAPB1.UserQuery (EntityType)

OpenType: true
Key: InternalKey, QueryCategory

## Properties

- InternalKey : Edm.Int32 [required]
- QueryCategory : Edm.Int32 [required]
- QueryDescription : Edm.String
- Query : Edm.String
- ProcedureAlias : Edm.String
- ProcedureName : Edm.String
- QueryType : SAPB1.UserQueryTypeEnum
- MenuCaption : Edm.String
- ParentMenuID : Edm.Int32
- MenuPosition : Edm.Int32
- MenuUniqueID : Edm.String
- EnableMenuEntry : SAPB1.BoYesNoEnum

## Navigation properties

- QueryCategory2 : SAPB1.QueryCategory [Partner=UserQueries]

# SAPB1.UserQueryParams (ComplexType)

## Properties

- InternalKey : Edm.Int32
- QueryCategory : Edm.Int32

# SAPB1.UserTablesMD (EntityType)

OpenType: true
Key: TableName

## Properties

- TableName : Edm.String [required]
- TableDescription : Edm.String
- TableType : SAPB1.BoUTBTableType
- Archivable : SAPB1.BoYesNoEnum
- ArchiveDateField : Edm.String
- DisplayMenu : SAPB1.BoYesNoEnum
- ApplyAuthorization : SAPB1.BoYesNoEnum

## Navigation properties

- UserFieldsMD : Collection(SAPB1.UserFieldMD) [Partner=UserTablesMD]
- UserObjectsMD : Collection(SAPB1.UserObjectsMD) [Partner=UserTablesMD]

# SAPB1.UserTablesMDParams (ComplexType)

## Properties

- TableName : Edm.String

# SAPB1.UserValidValue (ComplexType)

OpenType: true

## Properties

- FieldValue : Edm.String

# SAPB1.ValidValueMD (ComplexType)

## Properties

- Value : Edm.String
- Description : Edm.String

# SAPB1.ValueMappingCommunicationData (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- ThirdPartySystemId : Edm.Int32
- ObjectId : Edm.Int32
- CommunicationType : SAPB1.VMCommunicationTypeEnum
- StartDate : Edm.DateTimeOffset
- StartTime : Edm.Int32
- EndDate : Edm.DateTimeOffset
- EndTime : Edm.Int32
- Message : Edm.String
- Status : SAPB1.VMCommunicationStatusEnum

# SAPB1.ValueMappingCommunicationParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32

# SAPB1.ValueMappingParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32

# SAPB1.VatGroup (EntityType)

OpenType: true
Key: Code

## Properties

- Code : Edm.String [required]
- Name : Edm.String
- Category : SAPB1.BoVatCategoryEnum
- TaxAccount : Edm.String
- EU : SAPB1.BoYesNoEnum
- TriangularDeal : Edm.String
- AcquisitionReverse : SAPB1.BoYesNoEnum
- NonDeduct : Edm.Double
- AcquisitionTax : Edm.String
- GoodsShipment : Edm.String
- NonDeductAcc : Edm.String
- DeferredTaxAcc : Edm.String
- Correction : SAPB1.BoYesNoEnum
- VatCorrection : Edm.String
- EqualizationTaxAccount : Edm.String
- ServiceSupply : Edm.String
- Inactive : SAPB1.BoYesNoEnum
- TaxTypeBlackList : SAPB1.TaxTypeBlackListEnum
- Report349Code : SAPB1.Report349CodeListEnum
- VATInRevenueAccount : Edm.String
- DownPaymentTaxOffsetAccount : Edm.String
- CashDiscountAccount : Edm.String
- VATDeductibleAccount : Edm.String
- TaxRegion : SAPB1.VatGroupsTaxRegionEnum
- AcquisitionReverseCorrespondingTaxCode : Edm.String
- EBooksVatCategory : Edm.Int32
- TaxExemptionReason : Edm.String
- SAFTTaxCode : SAPB1.SAFTTaxCodeEnum
- EBooksVatExemptionCause : Edm.Int32
- EBooksVatExpClassType : Edm.Int32
- EBooksVatExpClassCategory : Edm.Int32
- SAFTTaxCodeEx : Edm.String
- GroupDescription : Edm.String
- VATType : Edm.Int32
- VatGroups_Lines : Collection(SAPB1.VatGroups_Line)

## Navigation properties

- Deposits : Collection(SAPB1.Deposit) [Partner=VatGroup]
- VendorPayments : Collection(SAPB1.Payment) [Partner=VatGroup]
- PaymentDrafts : Collection(SAPB1.Payment) [Partner=VatGroup]
- AdditionalExpenses : Collection(SAPB1.AdditionalExpense) [Partner=VatGroup]
- GLAccountAdvancedRules : Collection(SAPB1.GLAccountAdvancedRule) [Partner=VatGroup]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=VatGroup2]
- IncomingPayments : Collection(SAPB1.Payment) [Partner=VatGroup]
- Items : Collection(SAPB1.Item) [Partner=VatGroup]
- ChartOfAccount : SAPB1.ChartOfAccount [Partner=VatGroups]
- TaxExemptReason : SAPB1.TaxExemptReason [Partner=VatGroups]
- BrazilNumericIndexer : SAPB1.BrazilNumericIndexer [Partner=VatGroups]

# SAPB1.VatGroupParams (ComplexType)

## Properties

- Code : Edm.String

# SAPB1.VatGroups_Line (ComplexType)

OpenType: true

## Properties

- Effectivefrom : Edm.DateTimeOffset
- Rate : Edm.Double
- EqualizationTax : Edm.Double
- DatevCode : Edm.Int32

# SAPB1.VM_B1ValuesData (EntityType)

Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- ObjectId : Edm.Int32
- ObjectAbsEntry : Edm.String
- VM_ThirdPartyValuesCollection : Collection(SAPB1.VM_ThirdPartyValuesData)

# SAPB1.VM_ThirdPartyValuesData (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- LineId : Edm.Int32
- ThirdPartySystemId : Edm.Int32
- ThirdPartyValue : Edm.String

# SAPB1.Warehouse (EntityType)

OpenType: true
Key: WarehouseCode

## Properties

- Street : Edm.String
- StockInflationOffsetAccount : Edm.String
- ZipCode : Edm.String
- DecreasingAccount : Edm.String
- PurchaseAccount : Edm.String
- EURevenuesAccount : Edm.String
- ReturningAccount : Edm.String
- ShippedGoodsAccount : Edm.String
- StockInflationAdjustAccount : Edm.String
- AllowUseTax : SAPB1.BoYesNoEnum
- CostInflationAccount : Edm.String
- ForeignExpensesAccount : Edm.String
- EUExpensesAccount : Edm.String
- CostInflationOffsetAccount : Edm.String
- ExpensesClearingAccount : Edm.String
- PurchaseReturningAccount : Edm.String
- VATInRevenueAccount : Edm.String
- FederalTaxID : Edm.String
- Location : Edm.Int32
- Block : Edm.String
- ExpenseAccount : Edm.String
- DecreaseGLAccount : Edm.String
- RevenuesAccount : Edm.String
- TaxGroup : Edm.String
- ExemptRevenuesAccount : Edm.String
- PurchaseOffsetAccount : Edm.String
- CostOfGoodsSold : Edm.String
- WarehouseCode : Edm.String [required]
- State : Edm.String
- City : Edm.String
- PriceDifferencesAccount : Edm.String
- VarianceAccount : Edm.String
- Country : Edm.String
- IncreaseGLAccount : Edm.String
- ExchangeRateDifferencesAccount : Edm.String
- WIPMaterialAccount : Edm.String
- WarehouseName : Edm.String
- DropShip : SAPB1.BoYesNoEnum
- WIPMaterialVarianceAccount : Edm.String
- TransfersAcc : Edm.String
- InternalKey : Edm.Int32
- ForeignRevenuesAcc : Edm.String
- BuildingFloorRoom : Edm.String
- County : Edm.String
- Nettable : SAPB1.BoYesNoEnum
- IncreasingAcc : Edm.String
- ExpenseOffsetingAct : Edm.String
- GoodsClearingAcc : Edm.String
- StockAccount : Edm.String
- BusinessPlaceID : Edm.Int32
- PurchaseCreditAcc : Edm.String
- EUPurchaseCreditAcc : Edm.String
- ForeignPurchaseCreditAcc : Edm.String
- SalesCreditAcc : Edm.String
- SalesCreditEUAcc : Edm.String
- ExemptedCredits : Edm.String
- SalesCreditForeignAcc : Edm.String
- NegativeInventoryAdjustmentAccount : Edm.String
- WHShipToName : Edm.String
- Excisable : SAPB1.BoYesNoEnum
- WHIncomingCenvatAccount : Edm.String
- WHOutgoingCenvatAccount : Edm.String
- StockInTransitAccount : Edm.String
- WipOffsetProfitAndLossAccount : Edm.String
- InventoryOffsetProfitAndLossAccount : Edm.String
- AddressType : Edm.String
- StreetNo : Edm.String
- Storekeeper : Edm.Int32
- Shipper : Edm.String
- ManageSerialAndBatchNumbers : SAPB1.BoYesNoEnum
- GlobalLocationNumber : Edm.String
- EnableBinLocations : SAPB1.BoYesNoEnum
- BinLocCodeSeparator : Edm.String
- DefaultBin : Edm.Int32
- DefaultBinEnforced : SAPB1.BoYesNoEnum
- AutoAllocOnIssue : SAPB1.BoDocWhsAutoIssueMethod
- EnableReceivingBinLocations : SAPB1.BoYesNoEnum
- ReceivingBinLocationsBy : SAPB1.ReceivingBinLocationsMethodEnum
- PurchaseBalanceAccount : Edm.String
- Inactive : SAPB1.BoYesNoEnum
- RestrictReceiptToEmptyBinLocation : SAPB1.BoYesNoEnum
- ReceiveUpToMaxQuantity : SAPB1.BoYesNoEnum
- AutoAllocOnReceipt : SAPB1.AutoAllocOnReceiptMethodEnum
- ReceiveUpToMaxWeight : SAPB1.BoYesNoEnum
- ReceiveUpToMethod : SAPB1.ReceivingUpToMethodEnum
- LegalText : Edm.String
- AddressName2 : Edm.String
- AddressName3 : Edm.String

## Navigation properties

- StockTransferDrafts : Collection(SAPB1.StockTransfer) [Partner=Warehouse]
- BinLocations : Collection(SAPB1.BinLocation) [Partner=Warehouse2]
- ResourceCapacities : Collection(SAPB1.ResourceCapacity) [Partner=Warehouse2]
- ProductionOrders : Collection(SAPB1.ProductionOrder) [Partner=Warehouse2]
- InventoryTransferRequests : Collection(SAPB1.StockTransfer) [Partner=Warehouse]
- GLAccountAdvancedRules : Collection(SAPB1.GLAccountAdvancedRule) [Partner=Warehouse2]
- BusinessPlaces : Collection(SAPB1.BusinessPlace) [Partner=Warehouse]
- StockTakings : Collection(SAPB1.StockTaking) [Partner=Warehouse]
- ChartOfAccount : SAPB1.ChartOfAccount [Partner=Warehouses]
- WarehouseLocation : SAPB1.WarehouseLocation [Partner=Warehouses]
- SalesTaxCode : SAPB1.SalesTaxCode [Partner=Warehouses]
- Country2 : SAPB1.Country [Partner=Warehouses]
- County2 : SAPB1.County [Partner=Warehouses]
- EmployeeInfo : SAPB1.EmployeeInfo [Partner=Warehouses]
- BusinessPartner : SAPB1.BusinessPartner [Partner=Warehouses]
- BinLocation : SAPB1.BinLocation [Partner=Warehouses]
- StockTransfers : Collection(SAPB1.StockTransfer) [Partner=Warehouse]
- UserDefaultGroups : Collection(SAPB1.UserDefaultGroup) [Partner=Warehouse2]

# SAPB1.WarehouseLocation (EntityType)

OpenType: true
Key: Code

## Properties

- Code : Edm.Int32 [required]
- Name : Edm.String
- LSTVATNumber : Edm.String
- CSTNumber : Edm.String
- ExemptionNumber : Edm.String
- TANNumber : Edm.String
- ServiceTaxNumber : Edm.String
- AssesseeType : Edm.String
- CompanyType : Edm.String
- NatureOfBusiness : Edm.String
- TINNumber : Edm.String
- RegistrationType : Edm.String
- EccNumber : Edm.String
- CERange : Edm.String
- CEDivision : Edm.String
- CECommissionerate : Edm.String
- ManufacturerCode : Edm.String
- Jurisdiction : Edm.String
- Street : Edm.String
- Block : Edm.String
- ZipCode : Edm.String
- City : Edm.String
- County : Edm.String
- Country : Edm.String
- State : Edm.String
- PANNumber : Edm.String
- CERegisterNumber : Edm.String
- BuildingFloorRoom : Edm.String
- GSTIN : Edm.String
- GstType : SAPB1.BoGSTRegnTypeEnum
- GSTTDS : Edm.String
- GSTISD : Edm.String

## Navigation properties

- CertificateSeries : Collection(SAPB1.CertificateSeries) [Partner=WarehouseLocation]
- Country2 : SAPB1.Country [Partner=WarehouseLocations]
- VendorPayments : Collection(SAPB1.Payment) [Partner=WarehouseLocation]
- WithholdingTaxCodes : Collection(SAPB1.WithholdingTaxCode) [Partner=WarehouseLocation]
- PaymentDrafts : Collection(SAPB1.Payment) [Partner=WarehouseLocation]
- JournalEntries : Collection(SAPB1.JournalEntry) [Partner=WarehouseLocation]
- IncomingPayments : Collection(SAPB1.Payment) [Partner=WarehouseLocation]
- Items : Collection(SAPB1.Item) [Partner=WarehouseLocation]
- Warehouses : Collection(SAPB1.Warehouse) [Partner=WarehouseLocation]

# SAPB1.WarehouseLocationParams (ComplexType)

## Properties

- Code : Edm.Int32

# SAPB1.WarehouseParams (ComplexType)

## Properties

- WarehouseCode : Edm.String

# SAPB1.WarehouseSublevelCode (EntityType)

Key: AbsEntry

## Properties

- WarehouseSublevel : Edm.Int32
- Code : Edm.String
- Description : Edm.String
- AbsEntry : Edm.Int32 [required]

## Navigation properties

- BinLocationField : SAPB1.BinLocationField [Partner=WarehouseSublevelCodes]

# SAPB1.WarehouseSublevelCodeParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- WarehouseSublevel : Edm.Int32
- Code : Edm.String

# SAPB1.WebClientBookmarkTile (EntityType)

Key: Guid

## Properties

- Guid : Edm.String [required]
- Title : Edm.String
- SubTitle : Edm.String
- Info : Edm.String
- BindType : Edm.String
- UrlTarget : Edm.String
- Endpoint : Edm.String

# SAPB1.WebClientBookmarkTileParams (ComplexType)

## Properties

- Guid : Edm.String

# SAPB1.WebClientDashboard (EntityType)

Key: Guid

## Properties

- Guid : Edm.String [required]
- UserId : Edm.Int32
- Content : Edm.String
- Sys : SAPB1.BoYesNoEnum
- WebClientDashboardCards : Collection(SAPB1.WebClientDashboardCard)

# SAPB1.WebClientDashboardCard (ComplexType)

## Properties

- Guid : Edm.String
- UserId : Edm.Int32
- Content : Edm.String
- Sys : SAPB1.BoYesNoEnum
- Version : Edm.String

# SAPB1.WebClientDashboardParams (ComplexType)

## Properties

- Guid : Edm.String

# SAPB1.WebClientFormSetting (EntityType)

Key: Guid

## Properties

- Guid : Edm.String [required]
- FormId : Edm.String
- UserId : Edm.Int32
- DocObjectCode : Edm.String
- WebClientFormSettingItems : Collection(SAPB1.WebClientFormSettingItem)

# SAPB1.WebClientFormSettingItem (ComplexType)

## Properties

- Guid : Edm.String
- ItemId : Edm.String
- Order : Edm.Int32
- Visible : Edm.String
- Editable : Edm.String
- VisibleInGrid : Edm.String
- EditableInGrid : Edm.String

# SAPB1.WebClientFormSettingParams (ComplexType)

## Properties

- Guid : Edm.String

# SAPB1.WebClientLaunchpad (EntityType)

Key: Guid

## Properties

- Guid : Edm.String [required]
- UserId : Edm.Int32
- ThemeId : Edm.String
- DisplayQuickView : SAPB1.BoYesNoEnum
- NotificationShowDays : Edm.Int32
- WebClientLaunchpadGroups : Collection(SAPB1.WebClientLaunchpadGroup)

# SAPB1.WebClientLaunchpadGroup (ComplexType)

## Properties

- Guid : Edm.String
- Order : Edm.Int32
- GroupId : Edm.String
- GroupName : Edm.String
- Visible : SAPB1.BoYesNoEnum
- WebClientLaunchpadTiles : Collection(SAPB1.WebClientLaunchpadTile)

# SAPB1.WebClientLaunchpadParams (ComplexType)

## Properties

- Guid : Edm.String

# SAPB1.WebClientLaunchpadTile (ComplexType)

## Properties

- Guid : Edm.String
- Order : Edm.Int32
- TileId : Edm.String

# SAPB1.WebClientListviewFilter (EntityType)

Key: Guid

## Properties

- Guid : Edm.String [required]
- UserId : Edm.Int32
- TableName : Edm.String
- FilterName : Edm.String
- WebClientListviewFilterConditions : Collection(SAPB1.WebClientListviewFilterCondition)

# SAPB1.WebClientListviewFilterCondition (ComplexType)

## Properties

- Guid : Edm.String
- Order : Edm.Int32
- ColumnName : Edm.String
- CompareExpression : Edm.String
- Value : Edm.String

# SAPB1.WebClientListviewFilterParams (ComplexType)

## Properties

- Guid : Edm.String

# SAPB1.WebClientNotification (EntityType)

Key: Guid

## Properties

- Guid : Edm.String [required]
- UserId : Edm.Int32
- ActivityDate : Edm.DateTimeOffset
- ReadStatus : Edm.String
- IsDismissed : Edm.String
- NotiType : Edm.Int32

# SAPB1.WebClientNotificationParams (ComplexType)

## Properties

- Guid : Edm.String

# SAPB1.WebClientPreference (EntityType)

Key: Guid

## Properties

- Guid : Edm.String [required]
- UserId : Edm.Int32
- TableName : Edm.String
- ColumnName : Edm.String
- DefaultValue : Edm.String

# SAPB1.WebClientPreferenceParams (ComplexType)

## Properties

- Guid : Edm.String

# SAPB1.WebClientRecentActivity (EntityType)

Key: Guid

## Properties

- Guid : Edm.String [required]
- AppId : Edm.String
- AppType : Edm.String
- Count : Edm.Int32
- Timestamp : Edm.String
- Title : Edm.String
- Url : Edm.String
- UsageArray : Edm.String
- UserId : Edm.Int32
- RecentDay : Edm.String

# SAPB1.WebClientRecentActivityParams (ComplexType)

## Properties

- Guid : Edm.String

# SAPB1.WebClientVariant (EntityType)

Key: Guid

## Properties

- Guid : Edm.String [required]
- Order : Edm.Int32
- UserId : Edm.Int32
- ViewType : Edm.String
- SubViewType : Edm.String
- ViewId : Edm.String
- ObjectName : Edm.String
- FilterBarLayout : Edm.String
- SystemFilter : Edm.String
- UserFilter : Edm.String
- ConditionFilter : Edm.String
- IsPublic : SAPB1.BoYesNoEnum
- IsSystem : SAPB1.BoYesNoEnum
- Name : Edm.String
- Version : Edm.Int32
- OverviewCustomization : Edm.String
- ChartCustomization : Edm.String
- ReportCustomization : Edm.String
- WebClientVariantSelectedColumnCollection : Collection(SAPB1.WebClientVariantSelectedColumn)
- WebClientVariantGroupByCollection : Collection(SAPB1.WebClientVariantGroupBy)
- WebClientVariantSortByCollection : Collection(SAPB1.WebClientVariantSortBy)
- WebClientVariantEmbeddedChartCollection : Collection(SAPB1.WebClientVariantEmbeddedChart)
- WebClientVariantMChartCollection : Collection(SAPB1.WebClientVariantMChart)

# SAPB1.WebClientVariantEmbeddedChart (ComplexType)

## Properties

- Guid : Edm.String
- ChartType : Edm.String
- IsShowLegend : SAPB1.BoYesNoEnum
- CategoryAxis1 : Edm.String
- CategoryAxis2 : Edm.String
- TimeAxis : Edm.String
- Color : Edm.String
- Shape : Edm.String
- BubbleWidth : Edm.String
- WebClientVariantEmbeddedChartValue1Collection : Collection(SAPB1.WebClientVariantEmbeddedChartValue1)
- WebClientVariantEmbeddedChartValue2Collection : Collection(SAPB1.WebClientVariantEmbeddedChartValue2)
- WebClientVariantEmbeddedChartSizeCollection : Collection(SAPB1.WebClientVariantEmbeddedChartSize)

# SAPB1.WebClientVariantEmbeddedChartSize (ComplexType)

## Properties

- Guid : Edm.String
- Order : Edm.Int32
- ColumnName : Edm.String

# SAPB1.WebClientVariantEmbeddedChartValue1 (ComplexType)

## Properties

- Guid : Edm.String
- Order : Edm.Int32
- ColumnName : Edm.String

# SAPB1.WebClientVariantEmbeddedChartValue2 (ComplexType)

## Properties

- Guid : Edm.String
- Order : Edm.Int32
- ColumnName : Edm.String

# SAPB1.WebClientVariantGroup (EntityType)

Key: Guid

## Properties

- Guid : Edm.String [required]
- UserId : Edm.Int32
- ViewType : Edm.String
- ViewId : Edm.String
- ObjectName : Edm.String
- DefaultVariant : Edm.String

# SAPB1.WebClientVariantGroupBy (ComplexType)

## Properties

- Guid : Edm.String
- Order : Edm.Int32
- ColumnName : Edm.String

# SAPB1.WebClientVariantGroupParams (ComplexType)

## Properties

- Guid : Edm.String

# SAPB1.WebClientVariantMChart (ComplexType)

## Properties

- Guid : Edm.String
- ChartType : Edm.String
- IsShowLegend : SAPB1.BoYesNoEnum
- CategoryAxis1 : Edm.String
- CategoryAxis2 : Edm.String
- TimeAxis : Edm.String
- Color : Edm.String
- Shape : Edm.String
- BubbleWidth : Edm.String
- WebClientVariantMChartValue1Collection : Collection(SAPB1.WebClientVariantMChartValue1)
- WebClientVariantMChartValue2Collection : Collection(SAPB1.WebClientVariantMChartValue2)
- WebClientVariantMChartSizeCollection : Collection(SAPB1.WebClientVariantMChartSize)

# SAPB1.WebClientVariantMChartSize (ComplexType)

## Properties

- Guid : Edm.String
- Order : Edm.Int32
- ColumnName : Edm.String

# SAPB1.WebClientVariantMChartValue1 (ComplexType)

## Properties

- Guid : Edm.String
- Order : Edm.Int32
- ColumnName : Edm.String

# SAPB1.WebClientVariantMChartValue2 (ComplexType)

## Properties

- Guid : Edm.String
- Order : Edm.Int32
- ColumnName : Edm.String

# SAPB1.WebClientVariantParams (ComplexType)

## Properties

- Guid : Edm.String

# SAPB1.WebClientVariantSelectedColumn (ComplexType)

## Properties

- Guid : Edm.String
- Order : Edm.Int32
- ColumnName : Edm.String

# SAPB1.WebClientVariantSortBy (ComplexType)

## Properties

- Guid : Edm.String
- Order : Edm.Int32
- ColumnName : Edm.String
- Direction : Edm.String

# SAPB1.WeightMeasure (EntityType)

OpenType: true
Key: UnitCode

## Properties

- UnitCode : Edm.Int32 [required]
- UnitDisplay : Edm.String
- UnitName : Edm.String
- UnitWeightinmg : Edm.Double

## Navigation properties

- BinLocations : Collection(SAPB1.BinLocation) [Partner=WeightMeasure]

# SAPB1.WeightMeasureParams (ComplexType)

## Properties

- UnitCode : Edm.Int32

# SAPB1.WIPMapping (ComplexType)

## Properties

- AbsoluteEntry : Edm.Int32
- LineNumber : Edm.Int32
- AccountFrom : Edm.String
- AccountTo : Edm.String

# SAPB1.WithholdingTaxCertificatesData (ComplexType)

OpenType: true

## Properties

- POICodeRef : Edm.String
- POICode : Edm.String
- Certificate : Edm.String
- WTaxType : Edm.String
- PeriodIndicator : Edm.String
- WhtAbsId : Edm.Int32
- Series : Edm.Int32
- Number : Edm.Int32
- IssueDate : Edm.DateTimeOffset
- SumVATAmount : Edm.Double
- SumDocTotal : Edm.Double
- SumBaseAmount : Edm.Double
- SumAccumAmount : Edm.Double
- SumPercAmount : Edm.Double
- WTGroupsCollection : Collection(SAPB1.WTGroups)

# SAPB1.WithholdingTaxCode (EntityType)

OpenType: true
Key: WTCode

## Properties

- WTCode : Edm.String [required]
- WTName : Edm.String
- Category : SAPB1.WithholdingTaxCodeCategoryEnum
- BaseType : SAPB1.WithholdingTaxCodeBaseTypeEnum
- BaseAmount : Edm.Double
- OfficialCode : Edm.String
- Account : Edm.String
- WithholdingType : SAPB1.WithholdingTypeEnum
- RoundingType : SAPB1.RoundingTypeEnum
- Section : Edm.Int32
- Threshold : Edm.Double
- Surcharge : Edm.Double
- Concessional : SAPB1.BoYesNoEnum
- Assessee : Edm.Int32
- APTDSAccount : Edm.String
- APSurchargeAccount : Edm.String
- APCessAccount : Edm.String
- APHSCAccount : Edm.String
- APIGSTAccount : Edm.String
- APCGSTAccount : Edm.String
- APSGSTAccount : Edm.String
- APUTGSTAccount : Edm.String
- APCessGSTAccount : Edm.String
- ARTDSAccount : Edm.String
- ARSurchargeAccount : Edm.String
- ARCessAccount : Edm.String
- ARHSCAccount : Edm.String
- ARIGSTAccount : Edm.String
- ARCGSTAccount : Edm.String
- ARSGSTAccount : Edm.String
- ARUTGSTAccount : Edm.String
- ARCessGSTAccount : Edm.String
- ARTCSInterimAccount : Edm.String
- ARSurchargeInterimAccount : Edm.String
- ARCessInterimAccount : Edm.String
- ARHSCInterimAccount : Edm.String
- APTCSInterimAccount : Edm.String
- APSurchargeInterimAccount : Edm.String
- APCessInterimAccount : Edm.String
- APHSCInterimAccount : Edm.String
- Location : Edm.Int32
- ReturnType : SAPB1.ReturnTypeEnum
- Inactive : SAPB1.BoYesNoEnum
- CSTCodeIncomingID : Edm.Int32
- CSTCodeOutgoingID : Edm.Int32
- NatureOfCalculationBaseCode : Edm.String
- TypeID : Edm.Int32
- Rate : Edm.Double
- EffectiveFrom : Edm.DateTimeOffset
- MinimumTaxableAmount : Edm.Double
- IsProgressiveTax : SAPB1.BoYesNoEnum
- Currency : Edm.String
- TdsType : SAPB1.TdsTypeEnum
- TransactonThreshold : Edm.Double
- EBooksWTaxCategory : Edm.Int32
- NonDeductThreshold : SAPB1.BoYesNoEnum
- UseInAPDPR : SAPB1.BoYesNoEnum
- WithholdingTaxCodes_Lines : Collection(SAPB1.WithholdingTaxCodes_Line)

## Navigation properties

- VendorPayments : Collection(SAPB1.Payment) [Partner=WithholdingTaxCode]
- ChartOfAccount : SAPB1.ChartOfAccount [Partner=WithholdingTaxCodes]
- Section2 : SAPB1.Section [Partner=WithholdingTaxCodes]
- NatureOfAssessee : SAPB1.NatureOfAssessee [Partner=WithholdingTaxCodes]
- WarehouseLocation : SAPB1.WarehouseLocation [Partner=WithholdingTaxCodes]
- NotaFiscalCST : SAPB1.NotaFiscalCST [Partner=WithholdingTaxCodes]
- BrazilStringIndexer : SAPB1.BrazilStringIndexer [Partner=WithholdingTaxCodes]
- Currency2 : SAPB1.Currency [Partner=WithholdingTaxCodes]
- PaymentDrafts : Collection(SAPB1.Payment) [Partner=WithholdingTaxCode]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=WithholdingTaxCode]
- IncomingPayments : Collection(SAPB1.Payment) [Partner=WithholdingTaxCode]

# SAPB1.WithholdingTaxCodeParams (ComplexType)

## Properties

- WTCode : Edm.String

# SAPB1.WithholdingTaxCodes_Line (ComplexType)

OpenType: true

## Properties

- Effectivefrom : Edm.DateTimeOffset
- Rate : Edm.Double
- TDSRate : Edm.Double
- SurchargeRate : Edm.Double
- CessRate : Edm.Double
- HSCRate : Edm.Double
- IGSTRate : Edm.Double
- CGSTRate : Edm.Double
- SGSTRate : Edm.Double
- UTGSTRate : Edm.Double
- CessGSTRate : Edm.Double
- LineNum : Edm.Int32
- UoMEntry : Edm.Int32
- UoMCode : Edm.String
- FixedAmount : Edm.Double
- Currency : Edm.String
- ITRNonCompliantRate : Edm.Double
- PANNonCompliantRate : Edm.Double
- ProgressiveTax_Lines : Collection(SAPB1.ProgressiveTax_Line)
- WithholdingTaxCodes_ValueRange_Lines : Collection(SAPB1.WithholdingTaxCodes_ValueRange_Line)

# SAPB1.WithholdingTaxCodes_ValueRange_Line (ComplexType)

OpenType: true

## Properties

- ValueFrom : Edm.Double
- WTaxToBeDeductible : Edm.Double
- Rate : Edm.Double

# SAPB1.WithholdingTaxData (ComplexType)

OpenType: true

## Properties

- WTCode : Edm.String
- WTAmountSys : Edm.Double
- WTAmountFC : Edm.Double
- WTAmount : Edm.Double
- WithholdingType : Edm.String
- TaxableAmountinSys : Edm.Double
- TaxableAmountFC : Edm.Double
- TaxableAmount : Edm.Double
- RoundingType : Edm.String
- Rate : Edm.Double
- Criteria : Edm.String
- Category : Edm.String
- BaseType : Edm.String
- AppliedWTAmountSys : Edm.Double
- AppliedWTAmountFC : Edm.Double
- AppliedWTAmount : Edm.Double
- GLAccount : Edm.String
- LineNum : Edm.Int32
- BaseDocEntry : Edm.Int32
- BaseDocLine : Edm.Int32
- BaseDocType : Edm.Int32
- BaseDocumentReference : Edm.Int32
- Status : SAPB1.BoStatus
- TargetAbsEntry : Edm.Int32
- TargetDocumentType : Edm.Int32

# SAPB1.WithholdingTaxDataWTX (ComplexType)

OpenType: true

## Properties

- WTAmountSys : Edm.Double
- WTAmountFC : Edm.Double
- WTAmount : Edm.Double
- WithholdingType : Edm.String
- TaxableAmountinSys : Edm.Double
- TaxableAmountFC : Edm.Double
- TaxableAmount : Edm.Double
- Rate : Edm.Double
- Category : Edm.String
- BaseType : Edm.String
- AppliedWTAmountSys : Edm.Double
- AppliedWTAmountFC : Edm.Double
- AppliedWTAmount : Edm.Double
- GLAccount : Edm.String
- LineNum : Edm.Int32
- BaseDocEntry : Edm.Int32
- BaseDocLine : Edm.Int32
- BaseDocType : Edm.String
- WTAbsId : Edm.String
- ExemptRate : Edm.Double
- BaseNetAmountSys : Edm.Double
- BaseNetAmountFC : Edm.Double
- BaseNetAmount : Edm.Double
- BaseVatmountSys : Edm.Double
- BaseVatmountFC : Edm.Double
- BaseVatmount : Edm.Double
- AccumBaseAmountSys : Edm.Double
- AccumBaseAmountFC : Edm.Double
- AccumBaseAmount : Edm.Double
- AccumWTaxAmountSys : Edm.Double
- AccumWTaxAmountFC : Edm.Double
- AccumWTaxAmount : Edm.Double

# SAPB1.WithholdingTaxLine (ComplexType)

OpenType: true

## Properties

- WTCode : Edm.String
- WTAmountSys : Edm.Double
- WTAmountFC : Edm.Double
- WTAmount : Edm.Double
- WithholdingType : Edm.String
- TaxableAmountinSys : Edm.Double
- TaxableAmountFC : Edm.Double
- TaxableAmount : Edm.Double
- RoundingType : Edm.String
- Rate : Edm.Double
- Criteria : Edm.String
- Category : Edm.String
- BaseType : Edm.String
- AppliedWTAmountSys : Edm.Double
- AppliedWTAmountFC : Edm.Double
- AppliedWTAmount : Edm.Double
- GLAccount : Edm.String
- LineNum : Edm.Int32
- BaseDocEntry : Edm.Int32
- BaseDocLine : Edm.Int32
- BaseDocType : Edm.Int32
- BaseDocumentReference : Edm.Int32
- Status : SAPB1.BoStatus
- TargetAbsEntry : Edm.Int32
- TargetDocumentType : Edm.Int32
- CSTCodeIncoming : Edm.String
- CSTCodeOutgoing : Edm.String
- Doc1LineNum : Edm.Int32

# SAPB1.WizardPaymentMethod (EntityType)

OpenType: true
Key: PaymentMethodCode
Filtered properties: 1

## Properties

- PaymentMethodCode : Edm.String [required]
- Description : Edm.String
- Type : SAPB1.BoPaymentTypeEnum
- PaymentMeans : SAPB1.BoPaymentMeansEnum
- CheckAddress : SAPB1.BoYesNoEnum
- CheckBankDetails : SAPB1.BoYesNoEnum
- CollectionAuthorizationCheck : SAPB1.BoYesNoEnum
- BlockForeignPayment : SAPB1.BoYesNoEnum
- BlockForeignBank : SAPB1.BoYesNoEnum
- CurrencyRestriction : SAPB1.BoYesNoEnum
- PostOfficeBank : SAPB1.BoYesNoEnum
- MinimumAmount : Edm.Double
- MaximumAmount : Edm.Double
- DefaultBank : Edm.String
- UserSignature : Edm.Int32
- CreationDate : Edm.DateTimeOffset
- BankCountry : Edm.String
- DefaultAccount : Edm.String
- GLAccount : Edm.String
- Branch : Edm.String
- KeyCode : Edm.String
- TransactionType : Edm.String
- Format : Edm.String
- AgentCollection : SAPB1.BoYesNoEnum
- SendforAcceptance : SAPB1.BoYesNoEnum
- GroupByDate : SAPB1.BoYesNoEnum
- DepositNorm : Edm.String
- DebitMemo : SAPB1.BoYesNoEnum
- GroupByPaymentReference : SAPB1.BoYesNoEnum
- GroupInvoicesbyPay : SAPB1.BoYesNoEnum
- DueDateSelection : SAPB1.BoDueDateEnum
- PaymentTermsCode : Edm.Int32
- PosttoGLInterimAccount : SAPB1.BoYesNoEnum
- BankAccountKey : Edm.Int32
- DocType : Edm.String
- Accepted : Edm.String
- PortfolioID : Edm.String
- CurCode : Edm.String
- Instruction1 : Edm.String
- Instruction2 : Edm.String
- PaymentPlace : Edm.String
- BarcodeDll : Edm.String
- Active : SAPB1.BoYesNoEnum
- GroupInvoicesByPayToBank : SAPB1.BoYesNoEnum
- GroupInvoicesByCurrency : SAPB1.BoYesNoEnum
- BankChargeRate : Edm.Double
- ReportCode : Edm.String
- CancelInstruction : Edm.String
- OccurenceCode : Edm.String
- MovementCode : Edm.String
- DirectDebit : Edm.String
- CurrencyRestrictions : Collection(SAPB1.CurrencyRestriction)

## Navigation properties

- PurchaseDeliveryNotes : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- CorrectionPurchaseInvoiceReversal : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- Drafts : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- BlanketAgreements : Collection(SAPB1.BlanketAgreement) [Partner=WizardPaymentMethod]
- CreditNotes : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- Invoices : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- GoodsReturnRequest : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- PurchaseRequests : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- User : SAPB1.User [Partner=WizardPaymentMethods]
- Country : SAPB1.Country [Partner=WizardPaymentMethods]
- ChartOfAccount : SAPB1.ChartOfAccount [Partner=WizardPaymentMethods]
- PaymentTermsType : SAPB1.PaymentTermsType [Partner=WizardPaymentMethods]
- HouseBankAccount : SAPB1.HouseBankAccount [Partner=WizardPaymentMethods]
- InventoryGenEntries : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- Orders : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- DeliveryNotes : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- PurchaseDownPayments : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- Returns : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- CorrectionPurchaseInvoice : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- CorrectionInvoice : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- CorrectionInvoiceReversal : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- PurchaseInvoices : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- PurchaseCreditNotes : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- BusinessPartners : Collection(SAPB1.BusinessPartner) [Partner=WizardPaymentMethod]
- DownPayments : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- PurchaseReturns : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- PurchaseOrders : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- ReturnRequest : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- Quotations : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- SelfInvoices : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- SelfCreditMemos : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- PurchaseQuotations : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]
- InventoryGenExits : Collection(SAPB1.Document) [Partner=WizardPaymentMethod]

# SAPB1.WizardPaymentMethodParams (ComplexType)

## Properties

- PaymentMethodCode : Edm.String

# SAPB1.WorkflowApprovalTaskListParams (ComplexType)

## Properties

- Status : Edm.String

# SAPB1.WorkflowTask (ComplexType)

## Properties

- InstanceID : Edm.Int32
- TaskID : Edm.Int32
- TemplateID : Edm.String
- TemplateName : Edm.String
- Description : Edm.String
- Operation : Edm.String
- Type : Edm.String
- Owner : Edm.String
- Priority : Edm.Int32
- Status : Edm.String
- Name : Edm.String
- WorkflowTaskInputObjectCollection : Collection(SAPB1.WorkflowTaskInputObject)
- WorkflowTaskNoteCollection : Collection(SAPB1.WorkflowTaskNote)
- WorkflowTaskOutputObjectCollection : Collection(SAPB1.WorkflowTaskOutputObject)

# SAPB1.WorkflowTaskCompleteParams (ComplexType)

## Properties

- TaskID : Edm.Int32
- Note : Edm.String
- TriggerParams : Edm.String

# SAPB1.WorkflowTaskInputObject (ComplexType)

## Properties

- TaskID : Edm.Int32
- LineId : Edm.Int32
- Type : Edm.String
- Key : Edm.String
- SubType : Edm.String
- Detail : Edm.String

# SAPB1.WorkflowTaskNote (ComplexType)

## Properties

- TaskID : Edm.Int32
- LineId : Edm.Int32
- Note : Edm.String
- Creator : Edm.String
- NoteDate : Edm.DateTimeOffset

# SAPB1.WorkflowTaskOutputObject (ComplexType)

## Properties

- TaskID : Edm.Int32
- LineId : Edm.String
- Type : Edm.String
- Key : Edm.String
- SubType : Edm.String

# SAPB1.WTaxTypeCode (EntityType)

Key: Code

## Properties

- Code : Edm.Int32 [required]
- Description : Edm.String

## Navigation properties

- SpecificWTHAmountsService : Collection(SAPB1.SpecificWTHAmounts) [Partner=WTaxTypeCode2]

# SAPB1.WTaxTypeCodeParams (ComplexType)

## Properties

- Code : Edm.Int32

# SAPB1.WTDBP (ComplexType)

OpenType: true

## Properties

- BPKeyPart1 : Edm.String
- BPKeyPart2 : Edm.String
- WTaxCode : Edm.String
- EffectiveDateFrom : Edm.DateTimeOffset
- EffectiveDateTo : Edm.DateTimeOffset
- Rate : Edm.Double
- DetailType : SAPB1.WTDDetailType

# SAPB1.WTDCode (EntityType)

OpenType: true
Key: AbsEntry

## Properties

- AbsEntry : Edm.Int32 [required]
- WTaxCode : Edm.String
- WTaxName : Edm.String
- FormulaID : Edm.Int32
- Inactive : SAPB1.BoYesNoEnum
- OfficialCode : Edm.String
- Category : SAPB1.WithholdingTaxCodeCategoryEnum
- BaseType : SAPB1.WithholdingTaxCodeBaseTypeEnum
- Type : Edm.Int32
- MinAmount : Edm.Double
- BaseAmountPrct : Edm.Double
- SlidingScaleProgressiveTax : SAPB1.BoYesNoEnum
- CalculateInAutomaticCM : SAPB1.BoYesNoEnum
- WTDEffectiveDateCollection : Collection(SAPB1.WTDEffectiveDate)
- WTDBPCollection : Collection(SAPB1.WTDBP)
- WTDItemCollection : Collection(SAPB1.WTDItem)
- WTDFreightCollection : Collection(SAPB1.WTDFreight)

# SAPB1.WTDCodeParams (ComplexType)

## Properties

- AbsEntry : Edm.Int32
- WTaxCode : Edm.String
- WTaxName : Edm.String

# SAPB1.WTDEffectiveDate (ComplexType)

OpenType: true

## Properties

- LineNumber : Edm.Int32
- EffectiveFrom : Edm.DateTimeOffset
- Rate : Edm.Double
- WTDValueRangeCollection : Collection(SAPB1.WTDValueRange)

# SAPB1.WTDFreight (ComplexType)

OpenType: true

## Properties

- FreightCode : Edm.Int32
- WTaxCode : Edm.String
- EffectiveDateFrom : Edm.DateTimeOffset
- EffectiveDateTo : Edm.DateTimeOffset

# SAPB1.WTDItem (ComplexType)

OpenType: true

## Properties

- ItemCode : Edm.String
- WTaxCode : Edm.String
- EffectiveDateFrom : Edm.DateTimeOffset
- EffectiveDateTo : Edm.DateTimeOffset

# SAPB1.WTDValueRange (ComplexType)

OpenType: true

## Properties

- LineNumber : Edm.Int32
- SeqNum : Edm.Int32
- EffectiveFrom : Edm.DateTimeOffset
- ValueFrom : Edm.Double
- Rate : Edm.Double

# SAPB1.WTGroups (ComplexType)

OpenType: true

## Properties

- WTAbsEntry : Edm.Int32
- Percent : Edm.Double
- SumVATAmount : Edm.Double
- SumDocTotal : Edm.Double
- SumBaseAmount : Edm.Double
- SumAccumAmount : Edm.Double
- SumPerceptAmount : Edm.Double
- DocsInWTGroupsCollection : Collection(SAPB1.DocsInWTGroups)

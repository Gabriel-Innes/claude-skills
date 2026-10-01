<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# ExportDeterminationService (Object)

ExportDeterminationService Class

## Methods (8)
- `Public Sub AddDetermination(ByVal pIExportDetermination As ExportDetermination)` AddDetermination
  - param `pIExportDetermination`: 
- `Public Sub DeleteDetermination(ByVal pIExportDeterminationParams As ExportDeterminationParams)` DeleteDetermination
  - param `pIExportDeterminationParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ExportDeterminationServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ExportDeterminationServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetDetermination(ByVal pIExportDeterminationParams As ExportDeterminationParams) As ExportDetermination` GetDetermination
  - param `pIExportDeterminationParams`: 
- `Public Function GetDeterminations(ByVal pIExportDeterminationsParams As ExportDeterminationsParams) As ExportDeterminationsCollection` GetDeterminations
  - param `pIExportDeterminationsParams`: 
- `Public Sub UpdateDetermination(ByVal pIExportDetermination As ExportDetermination)` UpdateDetermination
  - param `pIExportDetermination`: 

# ExportDeterminationsParams (Object)

ExportDeterminationsParams Class

## Properties (1)
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R/W] property Code

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ExportProcesses (Object)

Source table: DOC18.

## Properties (14)
- `Public Property AdditionalItemSequentialNumber() As Long` [R/W] Enter the Additional Item Sequential Number for the Export Process. Field name: nSeqAdic.
- `Public Property DrawbackSuspensionRegime() As String` [R/W] Specify the Drawback - Suspension Regime number that reflects the reduction of the production costs of exportable items, assuring direct gains on imports, cash gains and non-accrual of tax credits on purchases.. Field name: DrawSReg. Length: 11 characters.
- `Public Property ExportationDeclarationDate() As Date` [R/W] Exportation Declaration Date. Field name: ExpDeclDat.
- `Public Property ExportationDeclarationNumber() As Long` [R/W] Exportation Declaration Number. Field name: ExpDeclNum.
- `Public Property ExportationDocumentTypeCode() As Long` [R/W] Type of Exportation Document. Field name: ExpDocType.
- `Public Property ExportationNatureCode() As Long` [R/W] Nature of Exportation. Field name: ExpNature.
- `Public Property ExportationRegistryDate() As Date` [R/W] Date of Exportation Registry. Field name: ExpRegDate.
- `Public Property ExportationRegistryNumber() As Long` [R/W] Number of Exportation Registry. Field name: ExpRegNum.
- `Public Property LadingBillDate() As Date` [R/W] Date of Bill of Lading. Field name: LadBillDat.
- `Public Property LadingBillNumber() As String` [R/W] Bill of Lading Number. Field name: LadBillNum. Length: 19 characters.
- `Public Property LadingBillTypeCode() As Long` [R/W] Type of Bill of Lading. Field name: LadBillTyp.
- `Public Property MerchandiseLeftCustomsDate() As Date` [R/W] Date Merchandise Left Customs. Field name: MerchLeftD.
- `Public Property NatureOfExport() As String` [R/W] Specify the Nature of Export for the Export Process. Field name: NatureExp. Length: 44 characters.
- `Public Property QuantityOfExportedItems() As Double` [R/W] Specify the Quantity of Exported Items for the Export Process.. Field name: QultExpItm.

# ExtendedAdminInfo (Object)

Enables you to set and get additional administration properties, in addition to the properties accessed via the AdminInfo object. Source table: ADM1

**Example:**
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
  Dim oExtenedAdminInfo As SAPbobsCOM.IExtendedAdminInfo

  Dim oAdminInfo As SAPbobsCOM.IAdminInfo

  'Get AdminInfo object

  oCmpSrv = oCompany.GetCompanyService()

  oAdminInfo = oCmpSrv.GetAdminInfo()

  oAdminInfo.CompanyName = "07B_SP0_Brazil_up"

  'Set extended properties

  oAdminInfo.ExtendedAdminInfo.AddressType = "DI_Addresstype"

  oAdminInfo.ExtendedAdminInfo.StreetNo = "DI_streetNo"

  oCmpSrv.UpdateAdminInfo(oAdminInfo)
  ```

## Properties (35)
- `Public Property AddressType() As String` [R/W] The address type for the company. Field name: AddrType. Length: 100 characters.
  - remarks: For Brazil only.
- `Public Property AllowInactiveItemsInInventoryCountingAndPosting() As BoYesNoEnum` [R/W] property AllowInactiveItemsInInventoryCountingAndPosting
- `Public Property AllowInactiveItemsInInventoryOpeningBalance() As BoYesNoEnum` [R/W] property AllowInactiveItemsInInventoryOpeningBalance
- `Public Property AuthorityPassword() As String` [R/W] property AuthorityPassword
- `Public Property AuthorityUser() As String` [R/W] property AuthorityUser
- `Public Property AutoAssignNewBranchToBP() As BoYesNoEnum` [R/W] property AutoAssignNewBranchToBP
- `Public Property CNPJofITCompany() As String` [R/W] CNPJ of IT company responsible for NFe. Field name: CNPJOfIT. Length: 14 characters.
- `Public Property CommercialRegister() As String` [R/W] property CommercialRegister
- `Public Property CompanyQualificationCode() As Long` [R/W] property CompanyQualificationCode
- `Public Property ContactPerson() As String` [R/W] Contact person name. Field name: CnPerson. Length: 60 characters.
- `Public Property ContactPersonEMail() As String` [R/W] Contact person Email. Field name: Email. Length: 60 characters.
- `Public Property ContactPersonPhone() As String` [R/W] Contact person phone number. Field name: Telephone. Length: 50 characters.
- `Public Property CooperativeAssociationTypeCode() As Long` [R/W] property CooperativeAssociationTypeCode
- `Public Property CreditContributionOriginCode() As String` [R/W] property CreditContributionOriginCode
- `Public Property DateOfIncorporation() As Date` [R/W] property DateOfIncorporation
- `Public Property DeclarerTypeCode() As Long` [R/W] property DeclarerTypeCode
- `Public Property DocumentRemarksInclude() As DocumentRemarksIncludeTypeEnum` [R/W] Determines the Remarks field when you copy a base marketing document to a target document. Field name: RmrksIncld.
  - remarks: Field name in the application: Document Remarks Include. To display the form in the application, select Administration --> System Initialization --> Document Settings --> General tab.
- `Public Property EconomicActivityTypeCode() As Long` [R/W] property EconomicActivityTypeCode
- `Public Property ElectronicApprovalForGoodsTransEnabled() As BoYesNoEnum` [R/W] property ElectronicApprovalForGoodsTransEnabled
- `Public Property ElectronicApprovalForInvoiceEnabled() As BoYesNoEnum` [R/W] property ElectronicApprovalForInvoiceEnabled
- `Public Property EnableIntrastat() As BoYesNoEnum` [R/W] property EnableIntrastat
- `Public Property EnvironmentType() As Long` [R/W] property EnvironmentType
- `Public Property GlobalLocationNumber() As String` [R/W] property GlobalLocationNumber
- `Public Property IPIPeriodCode() As String` [R/W] property IPIPeriodCode
- `Public Property IPITaxContributor() As BoYesNoEnum` [R/W] property IPITaxContributor
- `Public Property NatureOfCompanyCode() As Long` [R/W] property NatureOfCompanyCode
- `Public Property OKDPNumber() As String` [R/W] property OKDPNumber
- `Public Property Opting4ICMS() As BoYesNoEnum` [R/W] property Opting4ICMS
- `Public Property ProfitTaxationCode() As Long` [R/W] property ProfitTaxationCode
- `Public Property SPEDProfile() As String` [R/W] property SPEDProfile
- `Public Property STDCode() As Long` [R/W] property STDCode
- `Public Property STDCodeForeign() As Long` [R/W] property STDCodeForeign
- `Public Property StreetNo() As String` [R/W] The street number for the company. Field name: StreetNo. Length: 100 characters.
  - remarks: For Brazil only.
- `Public Property URLforGoodsTransportService() As String` [R/W] property URLforGoodsTransportService
- `Public Property URLforInvoiceTypeService() As String` [R/W] property URLforInvoiceTypeService

# ExtendedTranslation (Object)

ExtendedTranslation Class

## Properties (8)
- `Public Property Category() As TranslationCategoryEnum` [R/W] property Category
- `Public Property CreateDate() As Date` [R] property CreateDate
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property ExtendedTranslation_ItemLines() As ExtendedTranslation_ItemLines` [R] property ExtendedTranslation_ItemLines
- `Public Property ID() As String` [R/W] property ID
- `Public Property SecondaryID() As String` [R/W] property SecondaryID
- `Public Property SourceLanguage() As Long` [R/W] property SourceLanguage
- `Public Property UpdateDate() As Date` [R] property UpdateDate

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ExtendedTranslation_ItemLine (Object)

ExtendedTranslation_ItemLine Class

## Properties (9)
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property ExtendedTranslation_ResultLines() As ExtendedTranslation_ResultLines` [R] property ExtendedTranslation_ResultLines
- `Public Property ItemCode() As String` [R/W] property ItemCode
- `Public Property ItemType() As String` [R/W] property ItemType
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property MaxLength() As Long` [R/W] property MaxLength
- `Public Property Memo() As String` [R/W] property Memo
- `Public Property SlimType() As String` [R/W] property SlimType
- `Public Property SourceText() As String` [R/W] property SourceText

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ExtendedTranslation_ItemLines (Collection)

ExtendedTranslation_ItemLines Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As ExtendedTranslation_ItemLine` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As ExtendedTranslation_ItemLine` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` method Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ExtendedTranslation_ResultLine (Object)

ExtendedTranslation_ResultLine Class

## Properties (5)
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property LanguageCode() As Long` [R/W] property LanguageCode
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property SubLineNumber() As Long` [R] property SubLineNumber
- `Public Property TranslatedText() As String` [R/W] property TranslatedText

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ExtendedTranslation_ResultLines (Collection)

ExtendedTranslation_ResultLines Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As ExtendedTranslation_ResultLine` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As ExtendedTranslation_ResultLine` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` method Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ExtendedTranslationParams (Object)

ExtendedTranslationParams Class

## Properties (4)
- `Public Property Category() As TranslationCategoryEnum` [R/W] property Category
- `Public Property DocEntry() As Long` [R/W] property DocEntry
- `Public Property ID() As String` [R/W] property ID
- `Public Property SecondaryID() As String` [R/W] property SecondaryID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ExtendedTranslationsParams (Collection)

ExtendedTranslationsParams Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As ExtendedTranslationParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As ExtendedTranslationParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ExtendedTranslationsService (Object)

ExtendedTranslationsService Class

## Methods (8)
- `Public Function AddExtendedTranslation(ByVal pIExtendedTranslation As ExtendedTranslation) As ExtendedTranslationParams` AddExtendedTranslation
  - param `pIExtendedTranslation`: 
- `Public Sub DeleteExtendedTranslation(ByVal pIExtendedTranslationParams As ExtendedTranslationParams)` DeleteExtendedTranslation
  - param `pIExtendedTranslationParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ExtendedTranslationsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ExtendedTranslationsServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetExtendedTranslation(ByVal pIExtendedTranslationParams As ExtendedTranslationParams) As ExtendedTranslation` GetExtendedTranslation
  - param `pIExtendedTranslationParams`: 
- `Public Function GetExtendedTranslationList() As ExtendedTranslationsParams` GetExtendedTranslationList
- `Public Sub UpdateExtendedTranslation(ByVal pIExtendedTranslation As ExtendedTranslation)` UpdateExtendedTranslation
  - param `pIExtendedTranslation`: 

# ExternalCall (Object)

ExternalCall object is a request initiated by SAP Business One application that requires to be processed by external applications (e.g. SAP Business One Intergration). Source table: OREQ.

## Properties (10)
- `Public Property CallArguments() As CallArguments` [R] Returns the arguments affiliated to the original request call.
- `Public Property CallMessages() As CallMessages` [R] Returns the response messages written back by the external application that processes the request call.
- `Public Property Category() As Long` [R/W] Sets or returns the category number defined between the request sender and receiver. The purpose for this field is to identify the type of the request call that a certain receiver may be interested in. Field name: Category.
- `Public Property CreationDate() As Date` [R] Returns the date when the request call is created. Field name: CreateDate.
- `Public Property CreationTime() As Long` [R] Returns the time when the request call is created. Field name: CreateTime.
- `Public Property ID() As Long` [R] Returns the unique identity number of the request call (auto-increment). Field name: AbsEntry.
- `Public Property LastUpdateDate() As Date` [R/W] Returns the latest update date of the request call. Field name: LstUpdDate.
- `Public Property LastUpdateTime() As Long` [R/W] Returns the latest update time of the request call. Field name: LstUpdTime.
- `Public Property LastUpdateUserCode() As String` [R/W] Sets or returns the code of the last user that updated the request call. Field name: UserSign.
- `Public Property Status() As ExternalCallStatusEnum` [R/W] Sets or returns the current status of the request call. The status is updated by the external application that processes the request call. Field name: Status.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object's data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object's data.

# ExternalCallParams (Object)

This object holds identification properties to get an ExternalCall instance.

## Properties (1)
- `Public Property ID() As Long` [R/W] Returns the ID of an External Call object.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object's data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object's data.

# ExternalCallsService (Object)

External Call Service is used as an communication mechanism between Business One and any 3rd party or external applications. When Business One application is initiating an operation that requires real time external application (e.g. Business One integration), an external call request record is added to OREQ table. External applications could access this request via External Call Service, update the status of the request and attach response messages to the request. Mandatory properties: ID, Category, Status. Source table: OREQ.

## Methods (6)
- `Public Function GetCall(ByVal pIExternalCallParams As ExternalCallParams) As ExternalCall` Returns an instance of an external call by ID.
  - param `pIExternalCallParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ExternalCallsServiceDataInterfaces) As Object` Creates an empty data interface. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ExternalCallsServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Retrieves the Data Interface from XML file.
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Retrieves the Data Interface from XML string.
  - param `bstrXMLString`: 
- `Public Function SendCall(ByVal pIExternalCall As ExternalCall) As ExternalCallParams` Creates a new Call.
  - param `pIExternalCall`: 
- `Public Sub UpdateCall(ByVal pIExternalCall As ExternalCall)` Updates a call.
  - param `pIExternalCall`: 

# ExternalReconciliation (Object)

Represents external reconciliation, which is the comparison of open transactions within SAP Business One with an external account statement. Source table: OMTH.

## Properties (10)
- `Public Property AccountCode() As String` [R] The G/L account or business partner code for which the reconciliation is performed. Field name: MthAcctCod.
- `Public Property amount() As Double` [R] The reconciliation amount. Field name: Totals.
- `Public Property CreationDate() As Date` [R] Date on which the reconciliation was performed. Field name: CreateDate.
- `Public Property CurrencyType() As String` [R] The currency of the reconciliation. Field name: CurrType.
- `Public Property ReconciliationAccountType() As ReconciliationAccountTypeEnum` [R/W] The account type for which the reconciliation is performed. Field name: IsCard.
- `Public Property ReconciliationBankStatementLines() As ReconciliationBankStatementLines` [R] The reconciliation bank statement line.
- `Public Property ReconciliationDate() As Date` [R] The reconciliation date. Field name: MatchDate.
- `Public Property ReconciliationJournalEntryLines() As ReconciliationJournalEntryLines` [R] The reconciliation journal entry line.
- `Public Property ReconciliationNo() As Long` [R] The reconciliation number. Field name: MatchNum.
- `Public Property ReconciliationType() As String` [R] The reconciliation type. Field name: MatchType.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ExternalReconciliationFilterParams (Object)

Specifies the selection criteria for viewing, canceling, or re-creating previous external reconciliations created for business partners or G/L accounts.

**Remarks:** To open the Manage Previous External Reconciliations - Selection Criteria window, choose Banking --> Bank Statements and External Reconciliations --> Manage Previous External Reconciliations.

## Properties (7)
- `Public Property AccountCodeFrom() As String` [R/W] The business partner or one G/L account code from which you want to reconcile. Field name: AcctCodeFrom.
- `Public Property AccountCodeTo() As String` [R/W] The business partner or one G/L account code to which you want to reconcile. Field name: AcctCodeTo.
- `Public Property ReconciliationAccountType() As ReconciliationAccountTypeEnum` [R/W] The account type for which the reconciliation is performed. Field name: IsCard.
- `Public Property ReconciliationDateFrom() As Date` [R/W] The date from which the application performs reconciliations. Field name: MthDateFrom.
- `Public Property ReconciliationDateTo() As Date` [R/W] The date to which the application performs reconciliations. Field name: MthDateTo.
- `Public Property ReconciliationNoFrom() As Long` [R/W] A range of numbers representing the reconciliations the application should display. Field name: MatchNumFrom.
- `Public Property ReconciliationNoTo() As Long` [R/W] A range of numbers representing the reconciliations the application should display. Field name: MatchNumTo.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ExternalReconciliationParams (Object)

Holds the key to an existing parameter set. This object is used to pass keys to and retrieve keys from ExternalReconciliationsService methods.

## Properties (2)
- `Public Property AccountCode() As String` [R/W] The G/L account or business partner code for which the reconciliation is performed. Field name: MthAcctCod.
- `Public Property ReconciliationNo() As Long` [R/W] The reconciliation number. Field name: MatchNum.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ExternalReconciliationsParamsCollection (Collection)

A collection of ExternalReconciliationParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ExternalReconciliationParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ExternalReconciliationParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ExternalReconciliationsService (Object)

The ExternalReconciliationsService service enables you to add, look up, and cancel external reconciliations. Source table: OMTH.

**Remarks:** To perform external reconciliations, choose Banking --> Bank Statements and External Reconciliations --> Reconciliation. In the External Reconciliation – Selection Criteria window, select either the Manual or Automatic radio button, specify the selection criteria, and choose the Reconcile button.

**Example:**
- C# example (from SAP's help):
  ```csharp
  //Get business service.

  SAPbobsCOM.CompanyService oCompanyService = Cmpy.GetCompanyService();

  SAPbobsCOM.ExternalReconciliationsService ExtReconSvc =
                          (SAPbobsCOM.ExternalReconciliationsService)oCompanyService.GetBusinessService
  (SAPbobsCOM.ServiceTypes.ExternalReconciliationsService);

  SAPbobsCOM.ExternalReconciliation ExtReconciliation =
                          (SAPbobsCOM.ExternalReconciliation)ExtReconSvc.GetDataInterface(SAPbobsCOM.ExternalReconciliationsServiceDataInterfaces.ersExternalReconciliations);

  ExtReconciliation.ReconciliationAccountType = SAPbobsCOM.ReconciliationAccountTypeEnum.rat_BusinessPartner; // default is GL Account

  //Reconcile object.
  SAPbobsCOM. ReconciliationJournalEntryLine jeLine1 = (SAPbobsCOM. ReconciliationJournalEntryLine)ExtReconciliation.ReconciliationJournalEntryLines.Add();
  jeLine1.TransactionNumber = "1";
  jeLine1.LineNumber = 1;

  SAPbobsCOM.ReconciliationJournalEntryLine jeLine2 = (SAPbobsCOM. ReconciliationJournalEntryLine)ExtReconciliation.ReconciliationJournalEntryLines.Add();
   jeLine2.TransactionNumber = "2";
  jeLine2.LineNumber = 2;

  SAPbobsCOM.ReconciliationBankStatementLine bstLine1 = (SAPbobsCOM. ReconciliationBankStatementLine)ExtReconciliation. ReconciliationBankStatementLines.Add();
  bstLine1.BankStatementAccountCode = "C1";
  bstLine1.Sequence = 1;

  SAPbobsCOM. ReconciliationBankStatementLine bstLine2 = (SAPbobsCOM. ReconciliationBankStatementLine)ExtReconciliation. ReconciliationBankStatementLines.Add();
  bstLine2.BankStatementAccountCode = " C1";
  bstLine2.Sequence = 2;

  ExtReconSvc.Reconcile(ExtReconciliation);

  //Get object.
  SAPbobsCOM.ExternalReconciliationParams ExtReconParam =
                          (SAPbobsCOM.ExternalReconciliationParams)ExtReconSvc.GetDataInterface(SAPbobsCOM.ExternalReconciliationsServiceDataInterfaces.ersExternalReconciliationParams);
  ExtReconParam.AccountCode = "100012";
  ExtReconParam.ReconciliationNo = "2";
  ExtReconciliation = ExtReconSvc.GetReconciliation(ExtReconParam);

  //Get Reconcile List.
  SAPbobsCOM.ExternalReconciliationsParamsCollection ExtReconsParamsCollection = (SAPbobsCOM. ExternalReconciliationsParamsCollection)ExtReconSvc.GetDataInterface(SAPbobsCOM.ExternalReconciliationsServiceDataInterfaces.ersExternalReconciliationsParamsCollection);

  SAPbobsCOM.ExternalReconciliationFilterParams ExtReconFilteredParams =
                          (SAPbobsCOM.ExternalReconciliationFilterParams)ExtReconSvc.GetDataInterface(SAPbobsCOM.ExternalReconciliationsServiceDataInterfaces.ersExternalReconciliationFilterParams);
  ExtReconFilteredParams.ReconciliationAccountType = SAPbobsCOM.ReconciliationAccountTypeEnum.rat_GLAccount;//"G/L Account"
  ExtReconFilteredParams.AccountCodeFrom = "11200000-01-001-01";
  ExtReconFilteredParams.AccountCodeTo = "12400000-01-001-01";
  ExtReconFilteredParams.ReconciliationDateFrom = "05/03/11";
  ExtReconFilteredParams.ReconciliationDateTo = "06/03/11";
  ExtReconFilteredParams.ReconciliationNoFrom = 1;
  ExtReconFilteredParams.ReconciliationNoTo = 2;
  ExtReconsParamsCollection = ExtReconSvc.GetReconciliationList(ExtReconFilteredParams);

  //Cancel reconciliations.
  foreach (SAPbobsCOM.ExternalReconciliationParams ExtReconParam in ExtReconsParamsCollection)
  {
              ExtReconSvc.CancelReconciliation(ExtReconParam);
    }
  ```

## Methods (7)
- `Public Sub CancelReconciliation(ByVal pIExternalReconciliationParams As ExternalReconciliationParams)` Cancels an external reconciliation.
  - param `pIExternalReconciliationParams`: The key of the external reconciliation to be canceled.
- `Public Function GetDataInterface(ByVal enumMSDI As ExternalReconciliationsServiceDataInterfaces) As Object` Creates an empty data structure for use with the ExternalReconciliationsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ExternalReconciliationsServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLFile(Hashtable Properties, String Path)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair In Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        oGeneralData.ToXMLFile(Path);

        //Retrieve XML and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLFile(Path);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLString(Hashtable Properties)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;
        string XMLString;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair in Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        XMLString = oGeneralData.ToXMLString();

        //Retrieve XML string and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLString(XMLString);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetReconciliation(ByVal pIExternalReconciliationParams As ExternalReconciliationParams) As ExternalReconciliation` Retrieves an external reconciliation.
  - param `pIExternalReconciliationParams`: The key of the external reconciliation to be retrieved.
- `Public Function GetReconciliationList(ByVal pIExternalReconciliationFilterParams As ExternalReconciliationFilterParams) As ExternalReconciliationsParamsCollection` Returns the ExternalReconciliationsParamsCollection data collection that identifies all external reconciliations.
  - param `pIExternalReconciliationFilterParams`: The key of the external reconciliation to be retrieved.
- `Public Sub Reconcile(ByVal pIExternalReconciliation As ExternalReconciliation)` Performs an external reconciliation.
  - param `pIExternalReconciliation`: The data for the external reconciliations.

# FAAccountDetermination (Object)

Account determination enables the system to automatically determine the relevant general ledger accounts for a fixed asset when an asset transaction takes place. SAP Business One lets you define multiple account determination sets. For each asset, you can apply more than one set of G/L accounts, so that the asset value and transactions can be posted to more than one accounting area at the same time. Source table: OADT.

## Properties (21)
- `Public Property AccumulatedOrdinaryDepr() As String` [R/W] The account on the liability side for the accumulated value of ordinary, planned depreciation. This account is the offsetting account for ordinary, planned depreciation. Field name: OrdDprAcc. Length: 15 characters.
- `Public Property AccumulatedSpecialDepr() As String` [R/W] The account for the accumulated special depreciation of fixed assets. Field name: SpDprAcc. Length: 15 characters.
- `Public Property AccumulatedUnplannedDepr() As String` [R/W] The account for the accumulated unplanned depreciation of fixed assets. Field name: UnpDprAcc. Length: 15 characters.
- `Public Property AssetBalanceSheetAccount() As String` [R/W] The account for the acquisition and production costs of fixed assets. Field name: BalanceAct. Length: 15 characters.
- `Public Property ClearingAccountAcquisition() As String` [R/W] The clearing account for the acquisition and production costs of the fixed assets. Field name: ClrAcqAct. Length: 15 characters.
- `Public Property Code() As String` [R/W] The unique code for the set of G/L accounts you are defining. Field name: Code. Length: 15 characters.
- `Public Property Description() As String` [R/W] The description for the set of G/L accounts you are defining. Field name: Descr. Length: 100 characters.
- `Public Property LeavewithExpenseNBVGross() As String` [R/W] The expense account for recording the net book value of an asset during retirement. When an asset with the gross posting method retires with losses, the account records the net book value of the asset during retirement. Field name: ReNBVeAct. Length: 15 characters.
- `Public Property LeavewithRevenueNBVGross() As String` [R/W] The revenue account for recording the net book value of an asset during retirement. When an asset with the gross posting method retires with profits, the account records the net book value of the asset during retirement. Field name: ReNBVrAct. Length: 15 characters.
- `Public Property OrdinaryDepreciation() As String` [R/W] The expense account for the ordinary, planned, annual depreciation of fixed assets. Field name: OrdDprAct. Length: 15 characters.
- `Public Property RetirementwithExpenseNet() As String` [R/W] The account to which the net losses resulting from asset sales are posted. Field name: ReExpNAct. Length: 15 characters.
- `Public Property RetirementwithRevenueNet() As String` [R/W] The account to which the net profits gained from asset sales are posted. Field name: ReRevNAct. Length: 15 characters.
- `Public Property RevaluationAccount() As String` [R/W] Revaluation account for fixed assets. Field name: RevAct. Length: 15 characters.
- `Public Property RevaluationLossAcct() As String` [R/W] Revaluation loss account for fixed assets. Field name: RevLossAct. Length: 15 characters.
- `Public Property RevaluationReserveAccount() As String` [R/W] The account to which the increase in the asset's value, as a result of revaluation, is posted. Field name: RevResvAct. Length: 15 characters.
- `Public Property RevaluationReserveClearing() As String` [R/W] The clearing account to which the increase in the asset's value as a result of revaluation is posted temporarily when an asset is sold. Field name: RevResvClr. Length: 15 characters.
- `Public Property RevenueAccountforRetirement() As String` [R/W] The account for the revenue resulting from asset retirement. Field name: RevReAct. Length: 15 characters.
- `Public Property RevenueClearingAccount() As String` [R/W] The clearing account for the revenue resulting from asset sales. Field name: ClearAccRe. Length: 15 characters.
- `Public Property RevenuefromAssetSalesNet() As String` [R/W] The account for the net revenues from asset sales before tax. This account is the offsetting account for the revenue account from asset sales that is specified for sales from the customer account. The net book value and the profits or losses are posted to this account when a sale is made. Field name: SaRevNAct. Length: 15 characters.
- `Public Property SpecialDepreciation() As String` [R/W] The expense account for the special depreciation of fixed assets. Field name: SpDprAct. Length: 15 characters.
- `Public Property UnplannedDepreciation() As String` [R/W] The expense account for the unplanned annual depreciation of fixed assets. Field name: UnpDprAct. Length: 15 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# FAAccountDeterminationParams (Object)

Holds the key to an existing account determination rule for your fixed assets. This object is used to pass keys to and retrieve keys from FAAccountDeterminationsService methods.

## Properties (2)
- `Public Property Code() As String` [R/W] The unique code for the set of G/L accounts you are defining. Field name: Code. Length: 15 characters.
- `Public Property Description() As String` [R] The description for the set of G/L accounts you are defining. Field name: Descr. Length: 100 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# FAAccountDeterminationParamsCollection (Collection)

A collection of FAAccountDeterminationParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As FAAccountDeterminationParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As FAAccountDeterminationParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# FAAccountDeterminationsService (Object)

The FAAccountDeterminationsService service enables you to define and view different sets of G/L accounts for your fixed assets. Source table: OADT.

**Remarks:** To open the Account Determination - Setup window, from the SAP Business One Main Menu, choose Administration --> Setup --> Financials --> Fixed Assets --> Account Determination.

## Methods (8)
- `Public Function Add(ByVal pIFAAccountDetermination As FAAccountDetermination) As FAAccountDeterminationParams` Adds a fixed asset account determination rule.
  - param `pIFAAccountDetermination`: The data for the new fixed asset account determination rule.
- `Public Sub Delete(ByVal pIFAAccountDeterminationParams As FAAccountDeterminationParams)` Deletes an existing fixed asset account determination rule.
  - param `pIFAAccountDeterminationParams`: The key of the fixed asset account determination rule to be deleted.
- `Public Function Get(ByVal pIFAAccountDeterminationParams As FAAccountDeterminationParams) As FAAccountDetermination` Retrieves a fixed asset account determination rule. The fixed asset account determination rule is specified by its key, which is contained in the FAAccountDeterminationParams object passed to the method.
  - param `pIFAAccountDeterminationParams`: The key of the fixed asset account determination rule to retrieve
- `Public Function GetDataInterface(ByVal enumMSDI As FAAccountDeterminationsServiceDataInterfaces) As Object` Creates an empty data structure for use with the FAAccountDeterminationsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `FAAccountDeterminationsServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLFile(Hashtable Properties, String Path)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair In Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        oGeneralData.ToXMLFile(Path);

        //Retrieve XML and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLFile(Path);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLString(Hashtable Properties)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;
        string XMLString;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair in Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        XMLString = oGeneralData.ToXMLString();

        //Retrieve XML string and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLString(XMLString);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetList() As FAAccountDeterminationParamsCollection` Returns the FAAccountDeterminationParamsCollection data collection that identifies all fixed asset account determination rules.
- `Public Sub Update(ByVal pIFAAccountDetermination As FAAccountDetermination)` Updates an existing fixed asset account determination rule. The data for the fixed asset account determination rule, including the key of the fixed asset account determination rule to be updated, is contained in the FAAccountDetermination object passed to the method. To update a fixed asset account determination rule, you must first retrieve it using the Get method.
  - param `pIFAAccountDetermination`: The data for the fixed asset account determination rule to be updated. The FAAccountDetermination object must contain the key of the object to be updated.

# FactoringIndicators (Object)

The FactoringIndicators object enables to define a key that can be recorded in certain journal entries and used as a selection criterion in various reports. Source table: OIDC.

**Remarks:** To display the form in the application: - Select Business Partners --> Business Partner Master Data --> General tab. - Click the Choose From List button of the Factoring Indicator field. - In the List of Indicators dialog box, click the New button.

## Properties (4)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property IndicatorCode() As String` [R/W] Sets or returns the factoring indicator code. Field name: Code. Lentgh: 2 characters.
- `Public Property IndicatorName() As String` [R/W] Sets or returns the factoring indicator name. Field name: Name. Lentgh: 50 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (6)
- `Public Function Add() As Long` Adds a factoring indicator.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal bstrCode As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `bstrCode`: IndicatorCode.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Sub SaveToFile(ByVal bstrFileName As String)` Save the object to a file as XML data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef pbstrFileName As String)` Saves the object data to XML formatted data.
  - param `pbstrFileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# FeatureStatus (Object)

This object represents the status of a specified feature in the application, whether it is blocked or not according to the installation type: new 2007 release installation or upgrade installation prior to 2007 release.

**Remarks:** The following table provides a description for each feature, for which type of installation it is available, and where applicable. Feature Name ID Description Available for: AuthorizationEncryption 0 Removal of Use Encryption checkbox. Menu entry: Administration > Authorizations > General Authorizations. New installations only. Applicable for all localizations except Panama. LimitQueryTool 2 Adding authorization for SQL edit to prevent changes by unauthorized users. Menu entry: Tools > Queries > Query Generator & Query Wizard. All installations. Applicable for all localizations. QueryToolAuthorization 3 The new feature name is Modify SQL Statement. Menu enrty: Reports > Query Generator. The feature includes two options: Full Authorization or No Authorization (which controls the option to use the Pencil Icon on the query form). All installations. Applicable for all localizations. LimitLIFOInValuationReport 4 Removal of the LIFO valuation method from the Calc. method list box in the Inventory Valuation Report. Menu entry: Reports > Inventory >Inventory Valuation Report. New installations only. Applicable for all localizations. LimitComprehensiveImport 5 Limitation of the Comprehensive Import functionality to Israel localization. Menu entry: Administration > Data Import/Export > Data Import > Comprehensive Import. New installations only. Applicable for all localizations except Israel. LimitDunningInAgingReport 7 Removal of Dunning functionality in Aging report (Customers). Menu entry: Reports > Accounting > Aging > Customer Receivable > Customer Receivable - Details. New installations only. Applicable for all localizations. RemoveTaxChkForPay 8 Removal of Tax Code in the Checks for Payment form. Menu entry: Banking > Outgoing Payments > Checks for Payment. New installations only. Applicable for all localizations where this field exists (EU tax code based localizations). RemoveASSEMBLYFromBomList 10 Removal of the ability to create Assembly BOM (ability to view and update existing Assembly BOM remains). Menu entry: Production > Bill of Material. In the application, applicable for new installations only. In the DI, applicable for for all installtions. Applicable for all localizations. LimitLineTotalCalcChkbx 11 Removal of the Calculate the Row Total using the Unit Price checkbox for new installations. Menu entry: Administration > System Initialization > Document Settings. New installations only. Applicable for all localizations. EnableTaxForPmnOnAccount 12 Removal the Tax Code field in Payment on Account from both outgoing and incoming payments. Menu entry: Banking > Outgoing Payments > Outgoing Payment; Banking > Incoming Payments > Incoming Payment. New installations only. Applicable for all localizations where this field exists (EU tax code based localizations). LimitRestoreWizard 14 Removal of the Restore Wizard utility from the main menu and add it to the menu bar under Help > Support desk. Menu entry: Administration > Utilities > Restore. All installations. Applicable for all localizations. LimitRestoreChartOfAccount 15 Removal of the Restore Chart Of Account utility from the main menu and add it to the menu bar under Help > Support desk. Menu entry: Administration > Utilities > Restore. All installations. Applicable for all localizations. LimitRestoreOpenChecksBalance 16 Removal of the Restore Open Checks Balance utility from the main menu and add it to the menu bar under Help > Support desk. Menu entry: Administration > Utilities > Restore. All installations. Applicable for all localizations. LimitRestoreBudgetBalances 17 Removal of the Restore Budget Balances utility from the main menu and add it to the menu bar under Help > Support desk. Menu entry: Administration > Utilities > Restore. All installations. Applicable for all localizations. LimitResotreBudgetScenarios 18 Removal of the Restore Budget Scenarios utility from the main menu and add it to the menu bar under Help > Support desk. Menu entry: Administration > Utilities > Restore. All installations. Applicable for all localizations. LimitRestoreBatchAccumulators 19 Removal of the Restore Batch Accumulators utility from the main menu and add it to the menu bar under Help > Support desk. Menu entry: Administration > Utilities > Restore. All installations. Applicable for all localizations. EnableCopyOpeningClosingRemark 25 Removal of the Copy Opening and Closing Remarks to target document checkbox from Documents Settings. This checkbox is set to Enable for new installations (but not visible to the user). This checkbox is not open for changes through the DI API. Menu entry: Administration > System Initialization > Document Settings > General tab. New installations only. Applicable for all localizations.

## Properties (2)
- `Public Property Blocked() As BoYesNoEnum` [R] Specifies whether the feature is blocked or not.
- `Public Property FeatureID() As String` [R] Returns the feature ID.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the string of the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# FeatureStatusCollection (Collection)

FeatureStatusCollection is a Data Collection of FeatureStatus data structures.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the total objects in the collection.

## Methods (5)
- `Public Function Add() As FeatureStatus` Adds a new object to the collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As FeatureStatus` Returns a reference to a specified object in the collection.
  - param `vtIndex`: Specifies the index of the object.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# Field (Object)

The Field object contains both standard and custom data access properties. This object enables you to manipulate the field data.

**Remarks:** All of the properties, except ValidValue and Value, are read only.

## Properties (13)
- `Public Property DefaultValue() As String` [R] Returns the field default value.
- `Public Property Description() As String` [R] Returns the field description (when available).
  - remarks: Use this property only when you link it to a UserFields object.
- `Public Property FieldID() As Long` [R] Returns the field ID.
- `Public Property LinkedTable() As String` [R] Returns the table name linked to the field.
- `Public Property Mandatory() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not this field is mandatory in SAP Business One.
- `Public Property Name() As String` [R] Returns the field name.
- `Public Property Size() As Long` [R] Returns the actual field size.
- `Public Property SubType() As BoFldSubTypes` [R] Returns a valid value of BoFldSubTypes type that specifies the sub-type of the field as defined in the SubType property of the UserFieldsMD object.
- `Public Property Table() As String` [R] property Table
- `Public Property Type() As BoFieldTypes` [R] Returns the field data type as defined in the Type property of the UserFieldsMD object.
- `Public Property ValidValue() As String` [R/W] Sets or returns the actual value of the field (instead of the SQL query value).
- `Public Property ValidValues() As ValidValues` [R] Returns the ValidValues object.
- `Public Property Value() As Variant` [R/W] Sets or returns the field SQL query value.

## Methods (2)
- `Public Function IsNull() As BoYesNoEnum` Returns true (Y) if the field is null and false (N) if the field contains a non-null value.
  - remarks: To get the correct value of "IsNull", it is necessary to call the property Value of SAPbobsCOM.Fields object in order to update the current row of the RecordSet.
  - C# example (from SAP's help):
    ```csharp
    string Query = "SELECT NULL UNION SELECT 'THIS IS NOT NULL'";

    SAPbobsCOM.Recordset recordSet = (SAPbobsCOM.Recordset)SBO_Company.GetBusinessObject(SAPbobsCOM.BoObjectTypes.BoRecordset);
    recordSet.DoQuery(Query);
    recordSet.MoveFirst();
    recordSet.MoveNext(); // Skip the first row, goes directly to the row that is NOT NULL

    var item = recordSet.Fields.Item("0");
    var value = item.Value; // This operation updates the current row properties and it is required before using the IsNULL property.
    SAPbobsCOM.BoYesNoEnum isNull = item.IsNull(); // It returns NO. There's a Temporal Coupling behavior for the object SAPbobsCOM.Fields when moving through a RecordSet
    ```
- `Public Function SetNullValue() As Long` Sets the field value to Null.

# Fields (Collection)

The Fields object is a collection of Field objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of fields in the collection.

## Methods (1)
- `Public Function Item(ByVal Index As Variant) As Field` Retrieves a Field object by its position or by its alias.
  - param `Index`: Sets the field retrieval method by position or by alias (starts from 0).
  - returns: If the index value is wrong (for example, the value does not exist), the method fails and throws an exception.

# FIFOLayers (Object)

Specifies the FIFO layers to be updated, and the new values for the quantity and price. Source table: MRV2

**Remarks:** A FIFO layer is identified by its LayerID and TransactionSequenceNum properties. For more information, see the Layer object.

## Properties (7)
- `Public Property BaseLine() As Long` [R/W] property BaseLine
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property LayerID() As Long` [R/W] A layer ID. Obtain the ID for a specific layer from the Layer object.
- `Public Property LineTotal() As Double` [R/W] The new total value for this FIFO layer. Only relevant when the revaluation method is inventory debit/credit (see RevalType property of the MaterialRevaluation object).
- `Public Property Price() As Double` [R/W] The new price for this FIFO layer. Only relevant when the revaluation method is price change (see RevalType property of the MaterialRevaluation object).
- `Public Property Quantity() As Double` [R/W] The quantity of this FIFO layer to be revalued. Only relevant when the revaluation method is inventory debit/credit (see RevalType property of the MaterialRevaluation object).
- `Public Property TransactionSequenceNum() As Long` [R/W] A layer transaction sequence number. Obtain the ID for a specific layer from the Layer object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# FinancePeriod (Object)

The FinancePeriod object is a data structure related to the CompanyService. The object is used to identify and define a new Finance Period. Source table: OFPR.

## Properties (15)
- `Public Property AbsoluteEntry() As Long` [R] Sets or return the key of the period category as assigned by the system when creating a new period category. Field name: AbsEntry.
- `Public Property ActiveforFeed() As BoYesNoEnum` [R/W] Determines whether or not to enable adding documents to the finance period. However, a journal entries can be added. Field name: Free2. Use the property PeriodStatus instead of ActiveforFeed.
- `Public Property AdditionalSubPeriods() As BoYesNoEnum` [R] Determines whether or not additional sub periods exists. Field name: Addition.
- `Public Property Locked() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not to lock the Finance Period for additional journal entries. Field name: Free3. Use the property PeriodStatus instead of Locked.
- `Public Property PeriodCode() As String` [R/W] Sets or returns the Period Code. Field name: Code. Length: 20 characters.
- `Public Property PeriodIndicator() As String` [R/W] Sets or returns the PeriodIndicator, a foreign key to OPID. Field name: Indicator). Length: 10 characters.
- `Public Property PeriodName() As String` [R/W] Sets or returns the Period Name. Field name: Name. Length: 20 characters.
- `Public Property PeriodStatus() As PeriodStatusEnum` [R/W] Sets or returns a valid value that specifies the finance period status. Each status indicates what transactions and documents can be posted within the date range of each posting period. Field name: PeriodStat)
- `Public Property PostingDateFrom() As Date` [R/W] Sets or returns the Posting Period initiation date. Field name: F_RefDate.
- `Public Property PostingDateTo() As Date` [R/W] Sets or returns the Posting Period termination date. Field name: T_RefDate.
- `Public Property SubNum() As Long` [R] Returns the No. of Additional Sub-Period contained within the period. Field name: SubNum.
- `Public Property TaxDateFrom() As Date` [R/W] Sets or returns the starting date for Tax calculation. Field name: F_TaxDate.
- `Public Property TaxDateTo() As Date` [R/W] Sets or returns the ending date for Tax calculation. Field name: T_TaxDate.
- `Public Property ValueDateFrom() As Date` [R/W] Sets or returns the starting date for value calculation. Field name: F_DueDate.
- `Public Property ValueDateTo() As Date` [R/W] Sets or returns the ending date for value calculation. Field name: T_DueDate.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# FinancePeriodParams (Object)

The FinancePeriodParams specifies the identification key(system number, period indicator ) for which the CompanyService is related.

## Properties (2)
- `Public Property AbsoluteEntry() As Long` [R/W] Sets or returns the System Number, a key to the CompanyService. Field name: AbsEntry.
- `Public Property PeriodIndicator() As String` [R/W] Sets or returns the period indicator. Field name: Indicator. Length: 10 characters. This is a foreign key to the Period Indicators table OPID, which is not exposed through the DI API.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML file.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# FinancePeriods (Collection)

FinancePeriods is a collection of FinancePeriod objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the total number of FinancePeriod in the FinancePeriods Collection .

## Methods (5)
- `Public Function Add() As FinancePeriod` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As FinancePeriod` Retrieves an existing FinancePeriod item from the FinancePeriods collection by its index.
  - param `vtIndex`: Specifies the index of the FinancePeriod item to be retrieved.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# FinancialYear (Object)

Represents a financial year for TDS (withholding tax) reports. Source table: OFYM

**Remarks:** For India only. Mandatory properties: Code, Description, StartDate, AssessYear

## Properties (7)
- `Public Property AbsEntry() As Long` [R] The key for the financial year. Field name: AbsId
- `Public Property AssessYear() As String` [R/W] The assessment year code for the financial year. Field name: AssessYear Length: 6 characters
  - remarks: Must be a number.
- `Public Property Code() As String` [R/W] The display name for the financial year. Field name: Code Length: 6 characters
  - remarks: Must be a number.
- `Public Property Description() As String` [R/W] A description for the financial year. Field name: Descr
- `Public Property EndDate() As Date` [R] The end date for the financial year. Field name: EndDate
- `Public Property StartDate() As Date` [R/W] The start date for the financial year. Field name: StartDate
- `Public Property TCSAccumulationBase() As TCSAccumulationBaseEnum` [R/W] TCS Accumulation Base in the Financial Year Master - Setup window.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# FinancialYearParams (Object)

Holds the key and name to an existing financial period for TDS (withholding tax) reports. This object is used to pass keys to and retrieve keys from FinancialYearsService methods.

**Remarks:** For India only.

## Properties (3)
- `Public Property AbsEntry() As Long` [R/W] The key of a specific employee role. Field name: AbsId
- `Public Property Code() As String` [R] The display name for a specific financial year. Field name: Code
- `Public Property Description() As String` [R] The description for a specific financial year. Field name: Descr

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# FinancialYearsParams (Collection)

A collection of FinancialYearParams objects.

**Remarks:** For India only.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As FinancialYearParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As FinancialYearParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# FinancialYearsService (Object)

The FinancialYearsService service enables you to add, look up and remove financial roles for TDS (withholding tax) reports. To see the list of employee roles and create a new one, select Administration --> Setup --> Financials --> TDS --> Financial Year Master. Source table: OFYM.

**Remarks:** For India only.

## Methods (8)
- `Public Function AddFinancialYear(ByVal pIFinancialYear As FinancialYear) As FinancialYearParams` Adds a financial year.
  - param `pIFinancialYear`: The data for the new financial year
  - returns: Contains the key (AbsId) of the new financial year.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SAPbobsCOM.FinancialYear oFY;
        oFY = (SAPbobsCOM.FinancialYear)oFYSrv.GetDataInterface(FinancialYearsServiceDataInterfaces.fysFinancialYear);
        oFY.Code = "200703";
        oFY.Description = "FY 07-08";
        DateTime otime = DateTime.Parse("01/03/2007");
        oFY.StartDate = otime;
        oFY.AssessYear = "200703";
        oFYSrv.AddFinancialYear(oFY);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Sub DeleteFinancialYear(ByVal pIFinancialYearParams As FinancialYearParams)` Deletes an existing financial year. The financial year is specified by its key (AbsId), which is contained in the FinancialYearParams object passed to the method.
  - param `pIFinancialYearParams`: The key of the financial year to be deleted
  - remarks: You cannot delete a financial year if it is associated with a record in the OACM (accumulation) or OACK (acknowledge number) tables.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SAPbobsCOM.FinancialYearParams oDeleteLine;
        oDeleteLine = (SAPbobsCOM.FinancialYearParams)oFYSrv.GetDataInterface(FinancialYearsServiceDataInterfaces.fysFinancialYearParams);
        oDeleteLine.AbsEntry = 4;
        oFYSrv.DeleteFinancialYear(oDeleteLine);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As FinancialYearsServiceDataInterfaces) As Object` Creates an empty data structure for use with the FinancialYearsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `FinancialYearsServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLFile(Hashtable Properties, String Path)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair In Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        oGeneralData.ToXMLFile(Path);

        //Retrieve XML and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLFile(Path);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLString(Hashtable Properties)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;
        string XMLString;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair in Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        XMLString = oGeneralData.ToXMLString();

        //Retrieve XML string and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLString(XMLString);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetFinancialYear(ByVal pIFinancialYearParams As FinancialYearParams) As FinancialYear` Retrieves a specific financial year. The financial year is specified by its key (AbsId), which is contained in the FinancialYearParams object passed to the method.
  - param `pIFinancialYearParams`: The key of the financial year to retrieve
  - returns: The financial year with the specified key
- `Public Function GetFinancialYearList() As FinancialYearsParams` Retrieves the keys and names of all the financial years.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SAPbobsCOM.FinancialYearsParams oGetList = oFYSrv.GetFinancialYearList();
        String result;
        foreach(SAPbobsCOM.FinancialYearParams oGetItem in oGetList)
        {
            result = oGetItem.AbsEntry + " " + oGetItem.Code + " " + oGetItem.Description;
            Interaction.MsgBox(result, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
        }
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Sub UpdateFinancialYear(ByVal pIFinancialYear As FinancialYear)` Updates an existing financial year. The data for the financial year, including the key of the financial year to be updated, is contained in the FinancialYear passed to the method. To update a financial year, you must first retrieve it using the GetFinancialYear method.
  - param `pIFinancialYear`: The data for the financial year to be updated. The FinancialYear object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SAPbobsCOM.FinancialYear oUpdateLine;
        SAPbobsCOM.FinancialYearParams oGetLine;

        oGetLine = (SAPbobsCOM.FinancialYearParams)oFYSrv.GetDataInterface(FinancialYearsServiceDataInterfaces.fysFinancialYearParams);
        oGetLine.AbsEntry = 4;
        oUpdateLine = oFYSrv.GetFinancialYear(oGetLine);
         DateTime otime = DateTime.Parse("01/05/2008");
         oUpdateLine.StartDate = otime;
        oUpdateLine.Description = "updated";
        oFYSrv.UpdateFinancialYear(oUpdateLine);

    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```

# FiscalPrinter (Object)

FiscalPrinter Class

## Properties (6)
- `Public Property EquipmentNo() As String` [R/W] property EquipmentNo
- `Public Property FiscalDocumentModel() As String` [R/W] property FiscalDocumentModel
- `Public Property FiscalPrintersParams() As FiscalPrintersParams` [R] property FiscalPrintersParams
- `Public Property ManufacturerSerialN() As String` [R/W] property ManufacturerSerialN
- `Public Property Model() As String` [R/W] property Model
- `Public Property RegisterNo() As Long` [R/W] property RegisterNo

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# FiscalPrinterParams (Object)

FiscalPrinterParams Class

## Properties (1)
- `Public Property EquipmentNo() As String` [R/W] property EquipmentNo

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# FiscalPrinterService (Object)

FiscalPrinterService Class

## Methods (8)
- `Public Function AddFiscalPrinter(ByVal pIFiscalPrinter As FiscalPrinter) As FiscalPrinterParams` AddFiscalPrinter
  - param `pIFiscalPrinter`: 
- `Public Sub DeleteFiscalPrinter(ByVal pIFiscalPrinterParams As FiscalPrinterParams)` DeleteFiscalPrinter
  - param `pIFiscalPrinterParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As FiscalPrinterServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `FiscalPrinterServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetFiscalPrinter(ByVal pIFiscalPrinterParams As FiscalPrinterParams) As FiscalPrinter` GetFiscalPrinter
  - param `pIFiscalPrinterParams`: 
- `Public Function GetFiscalPrinterList() As FiscalPrintersParams` GetFiscalPrinterList
- `Public Sub UpdateFiscalPrinter(ByVal pIFiscalPrinter As FiscalPrinter)` UpdateFiscalPrinter
  - param `pIFiscalPrinter`: 

# FiscalPrintersParams (Collection)

FiscalPrintersParams Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As FiscalPrinterParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As FiscalPrinterParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# FixedAssetEndBalance (Object)

Source table: OFEV.

## Properties (10)
- `Public Property AcquisitionCost() As Double` [R] The asset's acquisition and production costs. Field name: APC.
- `Public Property HistoricalAPC() As Double` [R/W] property HistoricalAPC
- `Public Property HistoricalNBV() As Double` [R] property HistoricalNBV
- `Public Property NetBookValue() As Double` [R] The asset's net book value. Field name: NetNBV.
- `Public Property OrdinaryDepreciationValue() As Double` [R] The asset's accumulated ordinary depreciation amount. Field name: OrDpAcc.
- `Public Property Quantity() As Double` [R] If the asset is planned for quantity maintenance, the field displays the quantity. Field name: Quantity.
- `Public Property SalvageValue() As Double` [R/W] property SalvageValue
- `Public Property SpecialDepreciationValue() As Double` [R] The asset's accumulated special depreciation amount. Field name: SpDpAcc.
- `Public Property UnplanedDepreciationValue() As Double` [R] The asset's accumulated unplanned depreciation amount. Field name: UnDpAcc.
- `Public Property WriteUp() As Double` [R] The asset's accumulated write-up amount. In SAP Business One, write-up is the increase in an asset's value as a result of manual appreciation or revaluation. Field name: WriteUpAcc.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# FixedAssetItemsService (Object)

The FixedAssetItemsService service enables you to look up and update the end balance of an asset. Source table: OFDV, OFEV.

## Methods (6)
- `Public Function GetAssetEndBalance(ByVal pIFixedAssetValuesParams As FixedAssetValuesParams) As FixedAssetEndBalance` GetAssetEndBalance
  - param `pIFixedAssetValuesParams`: 
- `Public Function GetAssetValuesList(ByVal pIFixedAssetValuesParams As FixedAssetValuesParams) As FixedAssetValuesParamsCollection` GetAssetValuesList
  - param `pIFixedAssetValuesParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As FixedAssetItemsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `FixedAssetItemsServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Sub UpdateAssetEndBalance(ByVal pIFixedAssetValuesParams As FixedAssetValuesParams, ByVal pIFixedAssetEndBalance As FixedAssetEndBalance)` UpdateAssetEndBalance
  - param `pIFixedAssetValuesParams`: 
  - param `pIFixedAssetEndBalance`: 

# FixedAssetValues (Object)

You can monitor the changes in the value of an asset over the course of one year. Source table: OFDV.

## Properties (10)
- `Public Property AcquisitionCost() As Double` [R] The asset's acquisition and production costs at the beginning and end of the year. Field name: AcqCost.
- `Public Property Appreciation() As Double` [R] The asset's appreciation amount. Field name: Appreciate.
- `Public Property DepreciationValue() As Double` [R] The asset's depreciation amount. Field name: DprVal.
- `Public Property NetBookValue() As Double` [R] The asset's net book value. Field name: NBV.
- `Public Property OrdinaryDepreciationValue() As Double` [R] The asset's ordinary depreciation amount. Field name: OrdDprVal.
- `Public Property Quantity() As Double` [R] If the asset is planned for quantity maintenance, the field displays the quantity at the beginning and end of the year. Field name: Quantity.
- `Public Property SpecialDepreciationValue() As Double` [R] The asset's special depreciation amount. Field name: SpDprVal.
- `Public Property TransactionType() As AssetTransactionTypeEnum` [R] The transaction type of the fixed asset. Field name: TransType.
- `Public Property UnplanedDepreciationValue() As Double` [R] The asset's unplanned depreciation amount. Field name: UnpDprVal.
- `Public Property WriteUp() As Double` [R] The asset's write-up amount. In SAP Business One, write-up is the increase in an asset's value as a result of manual appreciation or revaluation. Field name: Write-Up.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# FixedAssetValuesParams (Object)

FixedAssetValuesParams Class

## Properties (3)
- `Public Property DepreciationArea() As String` [R/W] property DepreciationArea
- `Public Property FiscalYear() As String` [R/W] property FiscalYear
- `Public Property ItemCode() As String` [R/W] property ItemCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# FixedAssetValuesParamsCollection (Collection)

FixedAssetValuesCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As FixedAssetValues` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As FixedAssetValues` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# FormattedSearches (Object)

The FormattedSearches object enables to assign a formatted search function to a specified field, so that SAP Business One users can enter values, originated by a pre-defined search process, to the field. The formatted search is applicable for any field in the system including user defined fields. Source table: CSHS.

**Remarks:** The mandatory properties include the FormID, ItemID, and ColumnID. The combination of these properties determines the key of the field for which the formatted search is applicable. Additional mandatory properties are according to the value of the Action property. The following are examples of using the formatted search function: - Automatic entery of values into fields using various objects in the system. - Entering values into fields using a pre-defined list of valid values. - Automatic entery of values into fields by user-defined queries. - Creating dependency between fields in the system. That is, the value of field X influence the value of field Y. - Displaying fields that can only be displayed using queries such as, User Signature, Creation Date, Open Checks Balance (for business partner). To display the form in the application: - Open a document and click any field. - From the menu bar, select Tools --> Search Function --> Define. The Define Formatted Search form opens. - To view more fields, select the Search by Saved Query. General Guidelines Make sure to follow these guidelines, otherwise the system responds with the error -1003. - The formatted search query must refer to an existing field. For user-defined fields add the "U_" prefix. - The SQL syntax must be correct. - Add a Space character between the Equal sign (=) and the field/string before the Equal sign. - To compare a field of Alpha type to a variable such as [0], use a single quotation mark ' '[0]'. - Values must exist for the specified field before activating the formatted search function. For more details, refer to SMB Portal (upper menu: Service and Support. left menu: Knowledge & Services --> Knowledge Base). Look for the Formatted Search document.

## Properties (15)
- `Public Property Action() As BoFormattedSearchActionEnum` [R/W] Determines the type of action to be taken by the system when activating the formatted search function. The options include: Without Search, Search in Existing Values, and Search By Saved Query. Field name: ActionT.
  - remarks: The mandatory properties, in addition to FormID, ItemID, and ColumnID, depend on the value of the Action property as follows: bofsaNone | no additional mandatory properties. bofsaValidValues | UserValidValues object. bofsaQuery | QueryID, FieldID.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property ByField() As BoYesNoEnum` [R/W] Determines whether the automatic refresh is activated when the field changes or when exiting an altered column. Applicable for Table fields only and when the Refresh property is set tYES. Field name: ByField.
- `Public Property ByFieldEx() As FormattedSearchByFieldEnum` [R/W] property ByFieldEx
- `Public Property ColumnID() As String` [R/W] Sets or returns the column identification key. Mandatory for Table fields. The default value: -1 (Title field). Length: 11 characters.
  - remarks: The entered value must be a valid column ID (the system does not validate the entered value). To display the column ID in the application status bar: - From the main menu, select View --> System Information.
- `Public Property FieldID() As String` [R/W] Sets or returns the field ID. Field name: FieldID. Length: 11 characters. Mandatory in case Action is set to bofsaQuery.
  - remarks: Each form includes different set of Field IDs.
- `Public Property FieldIDs() As FormattedSearchFields` [R] property FieldIDs
- `Public Property ForceRefresh() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to refresh the data regularly or only to display the saved value. Field name: FrceRfrsh.
- `Public Property FormID() As String` [R/W] Sets or returns the form identification key. Field name: FormID. Mandatory property. Length: 100 characters.
  - remarks: The entered value must be a valid form ID (the system does not validate the entered value). To display the form ID in the application status bar: - From the main menu, select View System Information.
- `Public Property Index() As Long` [R] Returns the primary key of the formatted search function as assigned by the system when adding the object. Field name: IndexID.
- `Public Property ItemID() As String` [R/W] Sets or returns the ID of the field or the table in a form (primary key with FormID). Field name: ItemID. Mandatory property. Length: 20 characters.
  - remarks: The entered value must be a valid item ID (the system does not validate the entered value). In case the ItemID specifies a table, set also the ColumnID, otherwise the system sets the value -1. To display the item ID in the application status bar: - From the main menu, select View --> System Information. For a list of item IDs and coulmn IDs, refer to SMB Portal (from the main menu, select Service and Support. Then from the left menu, select Knowledge & Services --> Knowledge Base). Look for the document FormattedSearch.Doc.
- `Public Property QueryID() As Long` [R/W] Sets or returns the key of the query for the formatted search function. Field name: QueryId. Mandatory in case Action is set to bofsaQuery.
- `Public Property Refresh() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to automatically refresh the data when the field value is modified. Field name: Refresh.
  - remarks: In case this property is set to tYES and the field is a Table field, then the ByField property is applicable.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserValidValues() As UserValidValues` [R] Returns the UserValidValues object.

## Methods (7)
- `Public Function Add() As Long` Assigns a formatted search function to a specified field.
- `Public Function GetAsXML() As String` GetAsXML
- `Public Function GetByKey(ByVal lIndex As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lIndex`: Index.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes the current record.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal bstrFileName As String)` Save the object to a file as XML data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef pbstrFileName As String)` Saves the object data to XML formatted data.
  - param `pbstrFileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# FormattedSearchFields (Object)

FormattedSearchFields Class

## Properties (2)
- `Public Property Count() As Long` [R] property Count
- `Public Property FieldID() As String` [R/W] property FieldID

## Methods (3)
- `Public Sub Add()` method Add
- `Public Sub Remove()` method Remove
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 

# FormPreferencesService (Object)

The FormPreferencesService manages the display preferences of a specified form for a specified user. Form preferences include settings such as, column width, visual order of columns, and more.

**Remarks:** To use the service: - Connect to a valid company. - Call the CompanyService, which is the main DI service that you must call before using any other service. - Call the method GetBusinessService for the required service. - Create an empty data structure related to the required service. - or- You can create a data structure from an XML file or XML string. - Set the required properties of the specified data structure. - Call the required service method. To display the form in the application: - Select a form. - From the main menu, select Tools --> Form Settings. Mandatory properties: - FormID and User (ColumnsPreferencesParams) - Column, ItemNumber and Width (ColumnPreferences).

## Methods (5)
- `Public Function GetColumnsPreferences(ByVal pIColumnsPreferencesParams As ColumnsPreferencesParams) As ColumnsPreferences` Retrieves the column preferences of a specified form for a specified user.
  - param `pIColumnsPreferencesParams`: Returns the data structure that specifies the identification key combination (user and form) of the Form Preferences.
- `Public Function GetDataInterface(ByVal enumMSDI As FormPreferencesServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `FormPreferencesServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates a data structure from a specified XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates a data structure from a specified XML string.
  - param `bstrXMLString`: XML string.
  - example note: Shows how to get a Columns Preferences from an XML string
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oFormPreferencesService As FormPreferencesService

    Dim oColsPreferences As ColumnsPreferences

    Dim oColPreferencesParams As ColumnsPreferencesParams

    Dim oColsPreferencesXmlStr As ColumnsPreferences

    Dim sColsPreferencesStr As String

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get Form Preferences Service

    oFormPreferencesService = oCmpSrv.GetBusinessService(ServiceTypes.FormPreferencesService)

    'get Columns Preferences Params

    oColPreferencesParams = oFormPreferencesService.GetDataInterface(FormPreferencesServiceDataInterfaces.fpsdiColumnsPreferencesParams)

    'set the form id (e.g. A/R invoice=133)

    oColPreferencesParams.FormID = "133"

    'set the user id (e.g manager= 1)

    oColPreferencesParams.User = 1

    'get the Columns Preferences according to the formId & user id

    oColsPreferences = oFormPreferencesService.GetColumnsPreferences(oColPreferencesParams)

    'save Columns Preferences to string

    sColsPreferencesStr = oColsPreferences.ToXMLString()

    'create Columns Preferences object from string

    oColsPreferencesXmlStr = oFormPreferencesService.GetDataInterfaceFromXMLString(sColsPreferencesStr)
    ```
- `Public Sub UpdateColumnsPreferences(ByVal pIColumnsPreferencesParams As ColumnsPreferencesParams, ByVal pIColumnsPreferences As ColumnsPreferences)` Updates the column preferences of a specified form for a specified user with the data specified in ColumnsPreferences data structure.
  - param `pIColumnsPreferencesParams`: Returns the data structure that specifies the identification key combination (user and form) of the Form Preferences.
  - param `pIColumnsPreferences`: Returns the data structure that specifies the data for update the Form Preferences.
  - example note: The following is a VB.NET sample that updates the width of all the visible items in the invoice form settings.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oFormPreferencesService As FormPreferencesService

    Dim oColsPreferences As ColumnsPreferences

    Dim oColPreferencesParams As ColumnsPreferencesParams

    Dim i As Integer

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get Form Preferences Service

    oFormPreferencesService = oCmpSrv.GetBusinessService(ServiceTypes.FormPreferencesService)

    'get Columns Preferences Params

    oColPreferencesParams = oFormPreferencesService.GetDataInterface(FormPreferencesServiceDataInterfaces.fpsdiColumnsPreferencesParams)

    'set the form id (e.g. A/R invoice=133)

    oColPreferencesParams.FormID = "133"

    'set the user id (e.g manager= 1)

    oColPreferencesParams.User = 1

    'get the Columns Preferences according to the formId & user id

    oColsPreferences =  oFormPreferencesService.GetColumnsPreferences(oColPreferencesParams)

    'change the width of all the visible items

    For i = 0 To oColsPreferences.Count - 1

        'check if the item is visible

        If oColsPreferences.Item(i).VisibleInForm = BoYesNoEnum.tYES Then

            'set the width of the item

            oColsPreferences.Item(i).Width = 100

        End If

    Next

    'update all changes

    oFormPreferencesService.UpdateColumnsPreferences(oColPreferencesParams, oColsPreferences)
    ```

# Forms1099 (Object)

Forms1099 object enables to define new Form 1099 types in addition to the existing types: 1099 Miscellaneous, 1099 Interest, and 1099 Dividends. Source table: OTNN.

**Remarks:** Country-specific for USA only. To display the form in the application: - Select Administration -->Setup -->Financials -->1099 Table.

## Properties (5)
- `Public Property Boxes1099() As Boxes1099` [R] Returns the Box1099 child object.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Form1099() As String` [R/W] Sets or returns the description of the Form 1099 type. Field name: Form1099. Length: 100 characters.
- `Public Property FormCode() As Long` [R] Returns the identification key of the 1099 Form type as assigned by the system when adding a new 1099 Form type. Field name: FormCode.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a new Form 1099 type to the 1099 Table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lFormCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lFormCode`: 
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
- `Public Sub SaveToFile(ByVal bstrFileName As String)` Save the object to a file as XML data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef pbstrFileName As String)` Saves the object data to XML formatted data.
  - param `pbstrFileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# GeneralCollectionParams (Collection)

A collection of GeneralDataParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As GeneralDataParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As GeneralDataParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# GeneralData (Object)

Represents a single record of a UDO or a child UDO.

## Methods (8)
- `Public Function Child(ByVal bstrDataName As String) As GeneralDataCollection` Returns a GeneralDataCollection object that represents all the lines in the specified child table/UDO for the current record.
  - param `bstrDataName`: Specifies the child table/UDO from which to retrieve the lines. When registering a UDO, you can specify one or more child tables to link to the UDO and from which to create a child UDO. By default, the name of the child UDO is the same as the child table, but can be changed during the UDO registration.
  - returns: A collection of child lines.
  - remarks: This method is not relevant when the GeneralData object represents a record in a child table of the UDO.
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetProperty(ByVal bstrPropertyName As String) As Variant` Gets a property, or field, from the current record.
  - param `bstrPropertyName`: The name of the property to retrieve.
  - returns: The value of the property.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub SetProperty(ByVal bstrPropertyName As String, ByVal vtValue As Variant)` Sets a property, or field, for the current record.
  - param `bstrPropertyName`: The name of the property to retrieve.
  - param `vtValue`: The new value for the property.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# GeneralDataCollection (Collection)

A collection of GeneralData objects, each of which represents a record in a child UDO for a specific record of the main UDO.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As GeneralData` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As GeneralData` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub Remove(ByVal vtIndex As Variant)` Removes the object at the specified index.
  - param `vtIndex`: The index of the object to be removed.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# GeneralDataParams (Object)

Holds the keys to rows in database tables linked to a UDO data. This object is used to pass keys to and from GeneralService methods. Because it cannot be known the names of the properties that contain the key, properties of the GeneralDataParams object are set and retrieved with the generic SetProperty and GetProperty methods

## Methods (2)
- `Public Function GetProperty(ByVal bstrPropertyName As String) As Variant` Gets a property of the GeneralDataParams object.
  - param `bstrPropertyName`: The name of the property to be retrieved.
  - returns: The value of the property.
- `Public Sub SetProperty(ByVal bstrPropertyName As String, ByVal vtValue As Variant)` Sets a property of the GeneralDataParams object.
  - param `bstrPropertyName`: The name of the property to be set.
  - param `vtValue`: The new value for the property.

# GeneralService (Object)

The GeneralService provides access to UDOs. With the service, you can add, look up and remove rows from user-defined tables. You can also invoke custom methods on the UDO's custom business implementation DLL.

## Methods (12)
- `Public Function Add(ByVal pIGeneralData As GeneralData) As GeneralDataParams` Adds a row to the database table of the current UDO. The data for the row is contained in the GeneralData object passed to the method.
  - param `pIGeneralData`: The data for the new row.
  - returns: The key of the new row.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oGeneralService As SAPbobsCOM.GeneralService

    Dim oGeneralData As SAPbobsCOM.GeneralData

    Dim oSons As SAPbobsCOM.GeneralDataCollection

    Dim oSon As SAPbobsCOM.GeneralData

    Dim sCmp As SAPbobsCOM.CompanyService

    sCmp = oCompany.GetCompanyService

    'Get a handle to the SM_MOR UDO

    oGeneralService = sCmp.GetGeneralService("SM_MOR")

    'Specify data for main UDO

    oGeneralData = oGeneralService.GetDataInterface(SAPbobsCOM.GeneralServiceDataInterfaces.gsGeneralData)

    oGeneralData.SetProperty("U_Room", "1")

    oGeneralData.SetProperty("U_Price", "20")

    oGeneralData.SetProperty("U_Name", "David")

    'Specify data for child UDO

    oSons = oGeneralData.Child("SM_MOR1")

    oSon = oSons.Add

    oSon.SetProperty("U_MainDish", "Chicken")

    oSon.SetProperty("U_SideDish", "Fries")

    oSon.SetProperty("U_Drink", "Cola")

    'Add records

    oGeneralService.Add(oGeneralData)
    ```
- `Public Sub Cancel(ByVal pIGeneralDataParams As GeneralDataParams)` Cancels a row in the database table of the current UDO.
  - param `pIGeneralDataParams`: Contains a property whose value is the key of the row to cancel. For example, for a UDO for a master data table, the object contains a property called Code whose value is the key of the row to cancel.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oGeneralService As SAPbobsCOM.GeneralService

    Dim oGeneralParams As SAPbobsCOM.GeneralDataParams

    'Get a handle to the SM_MOR UDO

    oGeneralService = sCmp.GetGeneralService("SM_MOR")

    'Cancel UDO record

    oGeneralParams = oGeneralService.GetDataInterface(SAPbobsCOM.GeneralServiceDataInterfaces.gsGeneralDataParams)

    oGeneralParams.SetProperty("DocEntry", "2")

    oGeneralService.Cancel(oGeneralParams)
    ```
- `Public Sub Close(ByVal pIGeneralDataParams As GeneralDataParams)` Closes a row in the database table of the current UDO.
  - param `pIGeneralDataParams`: Contains a property whose value is the key of the row to close. For example, for a UDO for a document table, the object contains a property called DocEntry whose value is the key of the row to close.
  - remarks: For document-type UDOs only.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oGeneralService As SAPbobsCOM.GeneralService

    Dim oGeneralParams As SAPbobsCOM.GeneralDataParams

    'Get a handle to the SM_MOR UDO

    oGeneralService = sCmp.GetGeneralService("SM_MOR")

    'Close UDO record

    oGeneralParams = oGeneralService.GetDataInterface(SAPbobsCOM.GeneralServiceDataInterfaces.gsGeneralDataParams)

    oGeneralParams.SetProperty("DocEntry", "2")

    oGeneralService.Close(oGeneralParams)
    ```
- `Public Sub Delete(ByVal pIGeneralDataParams As GeneralDataParams)` Deletes a row in the database table of the current UDO.
  - param `pIGeneralDataParams`: Contains a property whose value is the key of the row to delete. For example, for a UDO for a master data table, the object contains a property called Code whose value is the key of the row to delete.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oGeneralService As SAPbobsCOM.GeneralService

    Dim oGeneralParams As SAPbobsCOM.GeneralDataParams

    Dim sCmp As SAPbobsCOM.CompanyService

    sCmp = oCompany.GetCompanyService

    'Get a handle to the SM_MOR UDO

    oGeneralService = sCmp.GetGeneralService("SM_MOR")

    'Delete UDO record

    oGeneralParams = oGeneralService.GetDataInterface(SAPbobsCOM.GeneralServiceDataInterfaces.gsGeneralDataParams)

    oGeneralParams.SetProperty("DocEntry", "2")

    oGeneralService.Delete(oGeneralParams)
    ```
- `Public Function DoCommand(ByVal pGeneralData As GeneralData, ByVal Command_Name As String) As GeneralData` DoCommand
  - param `pGeneralData`: 
  - param `Command_Name`: 
- `Public Function GetByParams(ByVal pIGeneralDataParams As GeneralDataParams) As GeneralData` Gets a row from the database table of the current UDO. The row is specified by passing its key to the method.
  - param `pIGeneralDataParams`: Contains a property whose value is the key of the row to return. For example, for a UDO for a master data table, the object contains a property called Code whose value is the key of the row to return.
  - returns: The data for the returned row.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oGeneralService As SAPbobsCOM.GeneralService

    Dim oGeneralData As SAPbobsCOM.GeneralData

    Dim oGeneralParams As SAPbobsCOM.GeneralDataParams

    Dim sCmp As SAPbobsCOM.CompanyService

    sCmp = oCompany.GetCompanyService

    'Get a handle to the SM_MOR UDO

    oGeneralService = sCmp.GetGeneralService("SM_MOR")

    'Get UDO record

    oGeneralParams = oGeneralService.GetDataInterface(SAPbobsCOM.GeneralServiceDataInterfaces.gsGeneralDataParams)

    oGeneralParams.SetProperty("DocEntry", "2")

    oGeneralData = oGeneralService.GetByParams(oGeneralParams)
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As GeneralServiceDataInterfaces) As Object` Creates an empty data structure for use with the GeneralService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `GeneralServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLFile(Hashtable Properties, String Path)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair In Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        oGeneralData.ToXMLFile(Path);

        //Retrieve XML and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLFile(Path);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLString(Hashtable Properties)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;
        string XMLString;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair in Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        XMLString = oGeneralData.ToXMLString();

        //Retrieve XML string and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLString(XMLString);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetList() As GeneralCollectionParams` Returns the keys for all the rows in the main table for a specific UDO. For example, if the UDO MealOrders was linked to the user-defined table @SM_OMOR table, and the service was instantiated for the MealOrders UDO, then this method would return the keys for all the rows in @SM_OMOR.
  - returns: A collection of GeneralDataParams objects is returned. Each object contains the key for one row in the table. For example, for a UDO for a master data table, each object contains a property called Code whose value is the key of a row in the table.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oGeneralService As SAPbobsCOM.GeneralService

    Dim oGeneralData As SAPbobsCOM.GeneralData

    Dim oGeneralParams As SAPbobsCOM.GeneralDataParams

    Dim oGeneralList As SAPbobsCOM.GeneralCollectionParams

    Dim lRet As Long

    'Create handle to "MUSIC" UDO

    oGeneralService = sCmp.GetGeneralService("MUSIC")

    'Add first record

    oGeneralData = oGeneralService.GetDataInterface(gsGeneralData)

    oGeneralData.SetProperty("Code", "First")

    oGeneralData.SetProperty("U_Data", "my data")

    oGeneralService.Add(oGeneralData)

    'Add second record

    oGeneralData = oGeneralService.GetDataInterface(gsGeneralData)

    oGeneralData.SetProperty("Code", "Second")

    oGeneralData.SetProperty("U_Data", "my data")

    oGeneralService.Add(oGeneralData)

    'Get list of all records

    oGeneralList = oGeneralService.GetList
    ```
- `Public Function InvokeMethod(ByVal pIInvokeParams As InvokeParams, ByVal pIGeneralData As GeneralData) As InvokeParams` Executes the InvokeMethod method of your UDO's custom business implementation DLL. The InvokeMethod has the following signature: TCHAR* InvokeMethod(CSboBusinessObject * refObj, const TCHAR* sInput) The CSboBusinessObject object receives data from the GeneralData parameter of this method, which represents a record of this UDO. The TCHAR object receives the string from the InvokeParams parameter of this method. You can use the InvokeMethod method as a dispatcher to other methods in your DLL, and use this string to determine how to dispatch to other functions in the DLL.
  - param `pIInvokeParams`: A string to be used by InvokeMethod method as needed and defined by the InvokeMethod method, which you create.
  - param `pIGeneralData`: A row in the database table that is linked to this GeneralService instance. You can obtain a GeneralData object for a specific row, for example, by calling the GetByParams method. Any changes to the CSboBusinessObject in the DLL's InvokeMethod does not affect the data in the GeneralData object that is passed. When control returns to your add-on from the DLL, the data in the GeneralData object is unchanged. This can cause a situation where the data in the GeneralData object is not up to date.
  - returns: A string returned from the DLL's InvokeMethod.
  - example note: You can invoke a custom method written in an implementation DLL for your UDO.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.GeneralService oGeneralService;
    SAPbobsCOM.GeneralData oGeneralData;
    SAPbobsCOM.InvokeParams oInvokeInput;
    SAPbobsCOM.InvokeParams oInvokeOutput;

    // Get GeneralService
    oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);

    // Get data interface
    oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);
    oInvokeInput = (InvokeParams)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsInvokeParams);

    oInvokeInput.Value = InvokeInputString;

    // Use invoke method
    oInvokeOutput = oGeneralService.InvokeMethod(oInvokeInput, oGeneralData);
    ```
- `Public Sub Update(ByVal pIGeneralData As GeneralData)` Updates an existing row in the database table of the current UDO. The data for the row, including the key of the row to be updated, is contained in the GeneralData passed to the method.
  - param `pIGeneralData`: The data for the row to be updated. The GeneralData object must contain the key of the object to be updated.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oGeneralService As SAPbobsCOM.GeneralService

    Dim oGeneralData As SAPbobsCOM.GeneralData

    Dim oGeneralParams As SAPbobsCOM.GeneralDataParams

    Dim sCmp As SAPbobsCOM.CompanyService

    sCmp = oCompany.GetCompanyService

    'Get a handle to the SM_MOR UDO

    oGeneralService = sCmp.GetGeneralService("SM_MOR")

    'Get UDO record

    oGeneralParams = oGeneralService.GetDataInterface(SAPbobsCOM.GeneralServiceDataInterfaces.gsGeneralDataParams)

    oGeneralParams.SetProperty("DocEntry", "2")

    oGeneralData = oGeneralService.GetByParams(oGeneralParams)

    'Update UDO record

    oGeneralData.SetProperty("U_Room", "2")

    oGeneralData.SetProperty("U_Price", "40")

    oGeneralData.SetProperty("U_Name", "Guy")

    oGeneralService.Update(oGeneralData)
    ```

# GeneratedAssets (Object)

GeneratedAssets Class

## Properties (10)
- `Public Property amount() As Double` [R] property amount
- `Public Property amountSC() As Double` [R] property amountSC
- `Public Property AssetCode() As String` [R/W] property AssetCode
- `Public Property Count() As Long` [R] property Count
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property LineNumber() As Long` [R/W] property LineNumber
- `Public Property Remarks() As String` [R/W] property Remarks
- `Public Property SerialNumber() As String` [R/W] property SerialNumber
- `Public Property Status() As GeneratedAssetStatusEnum` [R] property Status
- `Public Property VisOrder() As Long` [R] property VisOrder

## Methods (3)
- `Public Sub Add()` method Add
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 

# GetChangeLogParams (Object)

Holds the key to an existing change log. This object is used to pass keys to and retrieve keys from the ChangeLogsService methods.

## Properties (3)
- `Public Property Object() As BoChangeLogEnum` [R/W] The object that is changed. Field name: ObjectCode. Length: 50 characters.
- `Public Property PrimaryKey() As String` [R/W] The primary number of the document. Note: This field is for non user-defined objects. Field name: PK1. Length: 64 characters.
- `Public Property UDOObjectCode() As String` [R/W] The unique code of the user-defined object that is changed. Field name: UDOObjectCode. Length: 11 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# GLAccount (Object)

GLAccount is a data structure related to the AccountsService. The data is stored temporarily in a virtual table.

**Remarks:** To display the form related to the data structure: - Select Administration --> System Initialization --> Openning Balances --> G/L Accounts Openning Balance.

## Properties (9)
- `Public Property Code() As String` [R/W] Sets or returns the G/L account code for which to create an opening balance. Length: 15 characters.
- `Public Property Credit() As Double` [R/W] Sets or returns the amount to credit the G/L account.
- `Public Property Debit() As Double` [R/W] Sets or returns the amount to debit the G/L account.
- `Public Property DueDate() As Date` [R/W] Sets or returns the due date of the transaction.
- `Public Property ForeignCredit() As Double` [R/W] Sets or returns the amount, in foreign currency, to credit the G/L account.
- `Public Property ForeignCurrency() As String` [R/W] Sets or returns the foreign currency code used in the transaction. Length: 3 characters.
- `Public Property ForeignDebit() As Double` [R/W] Sets or returns the amount, in foreign currency, to debit the G/L account.
- `Public Property SystemCredit() As Double` [R/W] Sets or returns the amount, in system currency, to credit the G/L account.
- `Public Property SystemDebit() As Double` [R/W] Sets or returns the amount, in system currency, to debit the G/L account.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

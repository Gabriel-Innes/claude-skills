<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
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

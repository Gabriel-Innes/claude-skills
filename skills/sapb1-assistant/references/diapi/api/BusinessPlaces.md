<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BusinessPlaces (Object)

BusinessPlaces is a business object that represents a company's business locations. Each Korean company that issues tax invoices and VAT reports must indicate its business place. Each business place is bound with a VAT registry number. This object enables you to: - Retrieve a business place of a company by its key (BPLID). - Retrieve a business place of a company from XML data. - Save the object to a file as XML data. - Save the object as XML formatted data. Source table: OBPL.

**Remarks:** Country-specific for Korea. Business Place is a mandatory field in all marketing documents. You can get all defined Business Place objects through this object and assign the Business Place on marketing documents. To display the form in the application: - Select Administration --> Setup --> Financials --> Define Business Places.

## Properties (53)
- `Public Property AdditionalIdNumber() As String` [R/W] property AdditionalIdNumber
- `Public Property Address() As String` [R/W] Returns the business place address. Field name: Address. Length: 30 characters.
- `Public Property Addressforeign() As String` [R/W] Returns the foreign name of the business place address. Field name: AddressFr. Length: 100 characters.
- `Public Property AddressType() As String` [R/W] property AddressType
- `Public Property AliasName() As String` [R/W] proprety AliasName
- `Public Property Block() As String` [R/W] property Block
- `Public Property BPLID() As Long` [R] Returns the business place ID (primary key). Field name: BPLId.
- `Public Property BPLName() As String` [R/W] Returns the business place identification name. Field name: BPLName. Length: 20 characters.
- `Public Property BPLNameForeign() As String` [R/W] Returns the foreign identification name of the business place. Field name: BPLFrName. Length: 100 characters.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Building() As String` [R/W] property Building
- `Public Property Business() As String` [R/W] Returns the type of business that each business place manages. Field name: Business. Length: 20 characters.
- `Public Property City() As String` [R/W] property City
- `Public Property CommercialRegister() As String` [R/W] property CommercialRegister
- `Public Property CompanyQualificationCode() As Long` [R/W] property CompanyQualificationCode
- `Public Property CooperativeAssociationTypeCode() As Long` [R/W] property CooperativeAssociationTypeCode
- `Public Property Country() As String` [R/W] property Country
- `Public Property County() As String` [R/W] property County
- `Public Property CreditContributionOriginCode() As String` [R/W] property CreditContributionOriginCode
- `Public Property DateOfIncorporation() As Date` [R/W] property DateOfIncorporation
- `Public Property DeclarerTypeCode() As Long` [R/W] property DeclarerTypeCode
- `Public Property DefaultCustomerID() As String` [R/W] property DefaultCustomerID
- `Public Property DefaultResourceWarehouseID() As String` [R/W] property DefaultResourceWarehouseID
- `Public Property DefaultTaxCode() As String` [R/W] property DefaultTaxCode
- `Public Property DefaultVendorID() As String` [R/W] property DefaultVendorID
- `Public Property DefaultWarehouseID() As String` [R/W] property DefaultWarehouseID
- `Public Property Disabled() As BoYesNoEnum` [R/W] Returns a valid value of BoYesNoEnum type that specifies whether to disable (Y) or enable (N) the business place. Field name: Disabled.
  - remarks: Default: N (enable).
- `Public Property EconomicActivityTypeCode() As Long` [R/W] property EconomicActivityTypeCode
- `Public Property EnvironmentType() As Long` [R/W] property EnvironmentType
- `Public Property FederalTaxID() As String` [R/W] property FederalTaxID
- `Public Property FederalTaxID2() As String` [R/W] property FederalTaxID2
- `Public Property FederalTaxID3() As String` [R/W] property FederalTaxID3
- `Public Property GlobalLocationNumber() As String` [R/W] property GlobalLocationNumber
- `Public Property IENumbers() As BusinessPlaceIENumbers` [R] Get IENumbers
- `Public Property Industry() As String` [R/W] Returns the type of the industry that each business place manages. Field name: Industry. Length: 20 characters.
- `Public Property IPIPeriodCode() As String` [R/W] property IPIPeriodCode
- `Public Property MainBPL() As BoYesNoEnum` [R/W] Returns a valid value of BoYesNoEnum type that specifies whether the business place is the main business place (Y) or not (N). Field name: MainBPL.
  - remarks: Default: N (not the main business place).
- `Public Property NatureOfCompanyCode() As Long` [R/W] property NatureOfCompanyCode
- `Public Property Opting4ICMS() As BoYesNoEnum` [R/W] property Opting4ICMS
- `Public Property PaymentClearingAccount() As String` [R/W] property PaymentClearingAccount
- `Public Property PreferredStateCode() As String` [R/W] property PreferredStateCode
- `Public Property ProfitTaxationCode() As Long` [R/W] property ProfitTaxationCode
- `Public Property RepName() As String` [R/W] Returns the owner name of the business place. Field name: RepName. Length: 15 characters.
- `Public Property SPEDProfile() As String` [R/W] property SPEDProfile
- `Public Property State() As String` [R/W] property State
- `Public Property Street() As String` [R/W] property Street
- `Public Property StreetNo() As String` [R/W] property StreetNo
- `Public Property TaxOffice() As String` [R/W] property TaxOffice
- `Public Property TaxOfficeNo() As String` [R/W] Returns the tax office number of the business place. This number is used in the VAT report of the company. Field name: TxOffcNo. Length: 3 characters.
- `Public Property TributaryInfos() As BusinessPlaceTributaryInfos` [R] property TributaryInfos
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VATRegNum() As String` [R/W] Returns the VAT registration number of the business place. Field name: VATRegNum. Length: 12 characters.
  - remarks: Format: xxx-xx-xxxxx (10 digits, for example: 100-23-77654).
- `Public Property ZipCode() As String` [R/W] property ZipCode

## Methods (7)
- `Public Function Add() As Long` method Add
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lBplId As Long) As Boolean` GetByKey
  - param `lBplId`: BPLID
- `Public Function Remove() As Long` method Remove
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
- `Public Function Update() As Long` Method Update

<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CampaignBusinessPartner (Object)

The relevant business partners for the campaign. Source table: CPN1.

**Remarks:** To maintain the business partner master data, choose Business Partners --> Business Partner Master Data.

## Properties (43)
- `Public Property AddressID() As String` [R/W] property AddressID
- `Public Property AddressName2() As String` [R/W] property AddressName2
- `Public Property AddressName3() As String` [R/W] property AddressName3
- `Public Property AddressType() As String` [R/W] property AddressType
- `Public Property AssignName() As Long` [R/W] property AssignName
- `Public Property AssignTo() As CampaignAssignToEnum` [R/W] property AssignTo
- `Public Property Block() As String` [R/W] The block of the contact person. Field name: Block. Length: 100 characters.
- `Public Property BPCode() As String` [R/W] The code of the business partner. Field name: BpCode. Length: 15 characters.
- `Public Property BPGroupName() As String` [R] The group name of the business partner. Field name: GroupName. Length: 20 characters.
- `Public Property BPIndustryName() As String` [R] The industry of the business partner. Field name: Industry. Length: 15 characters.
- `Public Property BPName() As String` [R/W] The name of the business partner. Field name: BpName. Length: 100 characters.
- `Public Property BPStatus() As String` [R] The status of this campaign. Field name: Status.
- `Public Property Building() As String` [R/W] The building/floor/room of the contact person. Field name: Building. Length: 16 characters.
- `Public Property CampaignLineNumber() As Long` [R] The current row number. Field name: CpnLineNum.
- `Public Property CampaignNumber() As Long` [R] Automatically generated number the application assigns to this campaign. Field name: CpnNo.
- `Public Property City() As String` [R/W] The city of the contact person. Field name: City. Length: 100 characters.
- `Public Property ContactAddress() As String` [R/W] The address of the contact person. Field name: CntAddress. Length: 100 characters.
- `Public Property ContactCode() As String` [R/W] The default contact person of the business partner. Field name: CntCode. Length: 50 characters.
- `Public Property ContactEmail() As String` [R/W] The E-mail of the contact person. Field name: CntEmail. Length: 100 characters.
- `Public Property ContactFax() As String` [R/W] The fax number of the contact person. Field name: CntFax. Length: 20 characters.
- `Public Property ContactMobile() As String` [R/W] The mobile phone of the contact person. Field name: CntMobile. Length: 50 characters.
- `Public Property ContactPosition() As String` [R/W] The position of the contact person. Field name: CntPstn. Length: 90 characters.
- `Public Property ContactTelephone() As String` [R/W] The telephone number of the contact person. Field name: CntTel. Length: 50 characters.
- `Public Property ContactTitle() As String` [R/W] The title of the contact person. Field name: CntTitle. Length: 10 characters.
- `Public Property Country() As String` [R/W] The country of the contact person. Field name: Country. Length: 3 characters.
- `Public Property County() As String` [R/W] The county of the contact person. Field name: County. Length: 100 characters.
- `Public Property CreateActivity() As BoYesNoEnum` [R/W] property CreateActivity
- `Public Property DocEntry() As Long` [R/W] property DocEntry
- `Public Property DocNumber() As Long` [R] property DocNumber
- `Public Property DocType() As LinkedDocTypeEnum` [R/W] property DocType
- `Public Property FederalTaxID() As String` [R/W] property FederalTaxID
- `Public Property FirstName() As String` [R/W] property FirstName
- `Public Property IsShowLinkedDoc() As BoYesNoEnum` [R/W] property IsShowLinkedDoc
- `Public Property LastName() As String` [R/W] property LastName
- `Public Property MiddleName() As String` [R/W] property MiddleName
- `Public Property RelatedSalesOpportunity() As Long` [R/W] The related sales opportunity. Field name: OpprId.
- `Public Property Response() As BoYesNoEnum` [R/W] Indicates whether the company has responsed or not. Field name: Response.
- `Public Property ResponseType() As String` [R/W] property ResponseType
- `Public Property State() As String` [R/W] The state of the contact person. Field name: State. Length: 3 characters.
- `Public Property Street() As String` [R/W] The street of the contact person. Field name: Street. Length: 100 characters.
- `Public Property StreetNo() As String` [R/W] property StreetNo
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.
- `Public Property ZipCode() As String` [R/W] The zipcode of the contact person. Field name: ZipCode. Length: 100 characters.

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

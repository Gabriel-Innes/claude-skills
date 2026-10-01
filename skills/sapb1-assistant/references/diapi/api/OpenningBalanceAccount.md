<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# OpenningBalanceAccount (Object)

OpenningBalanceAccount is a data structure related to the AccountsService and BusinessPartnersService. The data is stored temporarily in a virtual table.

**Remarks:** Mandatory property: OpenBalanceAccount. To display the form related to the data structure: - Select Administration --> System Initialization --> Openning Balances --> G/L Accounts Openning Balance. or - Select Administration --> System Initialization --> Openning Balances --> Business Partners Openning Balance.

## Properties (6)
- `Public Property BPLID() As Long` [R/W] property BPLID
- `Public Property Date() As Date` [R/W] Sets or returns the posting date of the journal entry.
- `Public Property Details() As String` [R/W] Sets or returns details about the journal entry. Length: 50 characters.
- `Public Property OpenBalanceAccount() As String` [R/W] Sets or returns the openning balance account code from which to credit or debit G/L accounts or business partner accounts. Mandatory property.
- `Public Property Ref1() As String` [R/W] Sets or returns the first reference code of the journal entry. Length: 11 characters.
- `Public Property Ref2() As String` [R/W] Sets or returns the second reference code of the journal entry. Length: 11 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

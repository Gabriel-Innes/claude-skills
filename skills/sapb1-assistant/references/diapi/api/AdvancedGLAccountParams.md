<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AdvancedGLAccountParams (Object)

AdvancedGLAccountParams Class

## Properties (15)
- `Public Property AccountType() As InventoryAccountTypeEnum` [R/W] property AccountType
- `Public Property BPCode() As String` [R/W] property BPCode
- `Public Property FederalTaxID() As String` [R/W] property FederalTaxID
- `Public Property ItemCode() As String` [R/W] property ItemCode
- `Public Property PostingDate() As Date` [R/W] property PostingDate
- `Public Property ShipToCountry() As String` [R/W] property ShipToCountry
- `Public Property ShipToState() As String` [R/W] property ShipToState
- `Public Property UDF1() As String` [R/W] property UDF1
- `Public Property UDF2() As String` [R/W] property UDF2
- `Public Property UDF3() As String` [R/W] property UDF3
- `Public Property UDF4() As String` [R/W] property UDF4
- `Public Property UDF5() As String` [R/W] property UDF5
- `Public Property Usage() As Long` [R/W] property Usage
- `Public Property VatGroup() As String` [R/W] property VatGroup
- `Public Property Warehouse() As String` [R/W] property Warehouse

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

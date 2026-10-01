<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CustomsDeclaration (Object)

A data structure related with the CustomsDeclarationService holding the information about a Cargo Customs Declaration (CCD). Source table: OCCD.

## Properties (10)
- `Public Property CCDNum() As String` [R/W] Sets or returns the unique CCD number. Field name: CCDNum.
- `Public Property CustomsBroker() As String` [R/W] Sets or returns the customs broker (a valid business partner code from the OCRD table). Field name: CustBroker.
- `Public Property CustomsTerminal() As String` [R/W] Sets or returns the customs terminal (a valid business partner code from the OCRD table). Field name: CustTerm.
- `Public Property Date() As Date` [R/W] Sets or returns the date of declaration. Field name: Date.
- `Public Property DocDate() As Date` [R/W] Sets or returns the import or export document date. Field name: DocDate.
- `Public Property DocNum() As String` [R/W] Sets or returns the import or export document number. Field name: DocNum.
- `Public Property PaymentKey() As String` [R/W] Sets or returns the payment key. Field name: PayKey.
- `Public Property SupplyDate() As Date` [R/W] Sets or returns the supply agreement date. Field name: SupDate.
- `Public Property SupplyNum() As String` [R/W] Sets or returns the supply agreement number. Field name: SupNum.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the string of the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

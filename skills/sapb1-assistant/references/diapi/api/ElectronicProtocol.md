<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ElectronicProtocol (Object)

ElectronicProtocol Class

## Properties (12)
- `Public Property Confirmation() As String` [R/W] property Confirmation
- `Public Property EBooksInvoiceType() As String` [R/W] property EBooksInvoiceType
- `Public Property EBooksInvoiceTypeofNegative() As String` [R/W] property EBooksInvoiceTypeofNegative
- `Public Property EBooksMARK() As String` [R] property EBooksMARK
- `Public Property EBooksMARKofNegative() As String` [R] property EBooksMARKofNegative
- `Public Property EBooksRelevant() As BoYesNoEnum` [R/W] property EBooksRelevant
- `Public Property EDocType() As Long` [R/W] property EDocType
- `Public Property GenerationType() As ElectronicDocGenTypeEnum` [R/W] property GenerationType
- `Public Property MappingID() As Long` [R/W] property MappingID
- `Public Property ProtocolCode() As ElectronicDocProtocolCodeEnum` [R/W] property ProtocolCode
- `Public Property RelatedDocuments() As RelatedDocumentCollection` [R] property RelatedDocuments
- `Public Property TestingMode() As BoYesNoEnum` [R] property TestingMode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

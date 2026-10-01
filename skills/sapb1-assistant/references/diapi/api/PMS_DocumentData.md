<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PMS_DocumentData (Object)

Source table: PHA4.

## Properties (12)
- `Public Property AmountCategory() As AmountCatTypeEnum` [R] property AmountCategory
- `Public Property Categorize() As PMCategorizeTypeEnum` [R/W] property Categorize
- `Public Property DocDate() As Date` [R] property DocDate
- `Public Property DocEntry() As Long` [R/W] property DocEntry
- `Public Property DocType() As PMDocumentTypeEnum` [R/W] property DocType
- `Public Property LineId() As Long` [R] property LineID
- `Public Property LineNumber() As Long` [R/W] property LineNumber
- `Public Property Operation() As PMOperationTypeEnum` [R/W] property Operation
- `Public Property StageID() As Long` [R/W] property StageID
- `Public Property Status() As LineStatusTypeEnum` [R] property Status
- `Public Property Total() As Double` [R] property Total
- `Public Property UserFields() As Fields` [R] property User Fields

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

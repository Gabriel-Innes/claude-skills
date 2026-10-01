<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# RecurringPostings (Object)

RecurringPostings Class

## Properties (19)
- `Public Property AutomaticVAT() As BoYesNoEnum` [R/W] property AutomaticVAT
- `Public Property Code() As String` [R/W] property Code
- `Public Property DeferredTax() As BoYesNoEnum` [R/W] property DeferredTax
- `Public Property Description() As String` [R/W] property Description
- `Public Property Frequency() As BoFrequencyTypeEnum` [R/W] property Frequency
- `Public Property Instance() As Long` [R] property Instance
- `Public Property ManageWTax() As BoYesNoEnum` [R/W] property ManageWTax
- `Public Property NextExecution() As Date` [R/W] property NextExecution
- `Public Property RecurringPostingsDocumentReferenceCollection() As RecurringPostingsDocumentReferenceCollection` [R] property RecurringPostingsDocumentReferenceCollection
- `Public Property RecurringPostingsLineCollection() As RecurringPostingsLineCollection` [R] property RecurringPostingsLineCollection
- `Public Property Reference1() As String` [R/W] property Reference1
- `Public Property Reference2() As String` [R/W] property Reference2
- `Public Property Reference3() As String` [R/W] property Reference3
- `Public Property Remarks() As String` [R/W] property Remarks
- `Public Property StampTax() As BoYesNoEnum` [R/W] property StampTax
- `Public Property SubFrequency() As BoSubFrequencyTypeEnum` [R/W] property SubFrequency
- `Public Property TransactionCode() As String` [R/W] property TransactionCode
- `Public Property ValidUntil() As BoYesNoEnum` [R/W] property ValidUntil
- `Public Property ValidUntilDate() As Date` [R/W] property ValidUntilDate

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

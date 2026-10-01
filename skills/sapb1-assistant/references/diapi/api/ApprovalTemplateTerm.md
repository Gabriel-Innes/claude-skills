<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ApprovalTemplateTerm (Object)

ApprovalTemplateTerm is a data structure related to the ApprovalTemplatesService. Source table: WTM4.

## Properties (3)
- `Public Property ConditionType() As ApprovalTemplateConditionTypeEnum` [R/W] Sets or returns a valid value that defines the Deviation type that needs approval. Field name: CondId.
- `Public Property OperationType() As ApprovalTemplateOperationTypeEnum` [R/W] Sets or returns the logical operation required to define the deviation that initiate this Approval Template. Field name: opCode.
- `Public Property Value() As String` [R/W] Sets or returns the value associated with this Approval Template. Field name: opValue.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the an XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ApprovalTemplateStage (Object)

ApprovalTemplateStage is a data structure related to the ApprovalTemplatesService. Source table: WTM2.

## Properties (3)
- `Public Property ApprovalStageCode() As Long` [R/W] Sets or returns the confirmation level of this approval. Field name: WstCode. This is a foreign key to the ApprovalStagesService object.
- `Public Property Remarks() As String` [R/W] Sets or returns the description of this Approval Template . Field name: Remarks. Length: 100 characters.
- `Public Property SortID() As Long` [R/W] Sets or returns the Sort code. Field name: SortId.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

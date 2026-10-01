<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ApprovalStage (Object)

ApprovalStage is a Data structure related to the ApprovalStagesService. Source table: OWST.

## Properties (5)
- `Public Property ApprovalStageApprovers() As ApprovalStageApprovers` [R] Returns the ApprovalStageApprovers object, a DataCollection of ApprovalStageApprover data structures.
- `Public Property Code() As Long` [R] Returns this approval stage code. Field name: WstCode. This is a key to the ApprovalStage Object.
- `Public Property Name() As String` [R/W] Sets or returns the stage approver's name. Field name: Name. Length: 20 characters.
- `Public Property NoOfApproversRequired() As Long` [R/W] Returns the No. of authorizes required for this Approval Stage. Field name: MaxReqr.
- `Public Property Remarks() As String` [R/W] Sets or returns the Description of this approval stage. Field name: Remarks. Length: 100 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

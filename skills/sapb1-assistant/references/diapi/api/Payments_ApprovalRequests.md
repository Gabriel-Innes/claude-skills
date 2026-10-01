<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Payments_ApprovalRequests (Object)

Payments_ApprovalRequests is a child object of the Payments object. You can set the remarks field of the approval request. Source table: OWDDV.

## Properties (5)
- `Public Property ActiveForUpdate() As BoYesNoEnum` [R] property ActiveForUpdate
- `Public Property ApprovalTemplatesID() As Long` [R] The ID of the approval template. Field: WtmCode.
- `Public Property ApprovalTemplatesName() As String` [R] property ApprovalTemplatesName
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.
- `Public Property Remarks() As String` [R/W] Remarks made by the originator that are included with the approval request. Field: Remarks. Length: 100 characters.

## Methods (1)
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

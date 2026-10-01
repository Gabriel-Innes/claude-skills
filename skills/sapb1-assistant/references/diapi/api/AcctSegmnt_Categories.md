<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AcctSegmnt_Categories (Object)

The category of the account segmentation. Source table: OASC.

## Properties (4)
- `Public Property Code() As String` [R/W] The code of the segment. Field name: Code. Length: 20 characters.
  - remarks: You can use the digit 0 in a segment code. For example, if the segment size is 3, you can enter values such as 000 or 001.
- `Public Property Name() As String` [R/W] The name of the segment. Field name: Name. Length: 100 characters.
- `Public Property SegmentID() As Long` [R/W] The ID of the segment. Field name: SegmentId.
- `Public Property ShortName() As String` [R/W] The short name of the segment. SAP Business One uses this short name when creating automatic names for your G/L accounts. Field name: ShortName. Length: 10 characters.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

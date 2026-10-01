<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# QueueMembers (Object)

QueueMembers is a child object of Queue object and represents SAP Business One users that are members of the queue. Source tables: QUE1.

**Remarks:** To display the form in the application: - Select Administration --> Setup --> Service --> Queues. - Select a queue and then click Queue Members.

## Properties (4)
- `Public Property Count() As Long` [R] Returns the number of queue members for the current queue.
- `Public Property MemberUserID() As Long` [R/W] Sets or returns the Queue's member user ID. Field name: member. This is a foreign key to the Users object.
- `Public Property QueueID() As String` [R/W] Sets or returns a unique code for identifying the queue. Mandatory property. Field name: queueID. Length: 20 characters This is a foreign key to the Queue object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

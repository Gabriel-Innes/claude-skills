<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ExternalCall (Object)

ExternalCall object is a request initiated by SAP Business One application that requires to be processed by external applications (e.g. SAP Business One Intergration). Source table: OREQ.

## Properties (10)
- `Public Property CallArguments() As CallArguments` [R] Returns the arguments affiliated to the original request call.
- `Public Property CallMessages() As CallMessages` [R] Returns the response messages written back by the external application that processes the request call.
- `Public Property Category() As Long` [R/W] Sets or returns the category number defined between the request sender and receiver. The purpose for this field is to identify the type of the request call that a certain receiver may be interested in. Field name: Category.
- `Public Property CreationDate() As Date` [R] Returns the date when the request call is created. Field name: CreateDate.
- `Public Property CreationTime() As Long` [R] Returns the time when the request call is created. Field name: CreateTime.
- `Public Property ID() As Long` [R] Returns the unique identity number of the request call (auto-increment). Field name: AbsEntry.
- `Public Property LastUpdateDate() As Date` [R/W] Returns the latest update date of the request call. Field name: LstUpdDate.
- `Public Property LastUpdateTime() As Long` [R/W] Returns the latest update time of the request call. Field name: LstUpdTime.
- `Public Property LastUpdateUserCode() As String` [R/W] Sets or returns the code of the last user that updated the request call. Field name: UserSign.
- `Public Property Status() As ExternalCallStatusEnum` [R/W] Sets or returns the current status of the request call. The status is updated by the external application that processes the request call. Field name: Status.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object's data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object's data.

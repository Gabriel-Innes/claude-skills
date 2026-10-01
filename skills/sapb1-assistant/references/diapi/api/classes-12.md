<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# EcmActionDocParams (Object)

EcmActionDocParams Class

## Properties (3)
- `Public Property Protocol() As String` [R/W] property Protocol
- `Public Property SourceObject() As Long` [R/W] property SourceObject
- `Public Property SourceType() As String` [R/W] property SourceType

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EcmActionLog (Object)

EcmActionLog Class

## Properties (9)
- `Public Property ActionID() As Long` [R/W] property ActionID
- `Public Property Data() As String` [R/W] property Data
- `Public Property ExportFile() As String` [R/W] property ExportFile
- `Public Property ExportFormat() As Long` [R/W] property ExportFormat
- `Public Property LogDate() As Date` [R/W] property LogDate
- `Public Property LogID() As Long` [R] property LogID
- `Public Property LogTime() As Long` [R/W] property LogTime
- `Public Property Message() As String` [R/W] property Message
- `Public Property Type() As EcmActionLogTypeEnum` [R/W] property Type

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EcmActionLogCollection (Collection)

EcmActionLogCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As EcmActionLog` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As EcmActionLog` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EcmActionLogParams (Object)

EcmActionLogParams Class

## Properties (2)
- `Public Property ActionID() As Long` [R/W] property ActionID
- `Public Property LogID() As Long` [R/W] property LogID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EcmActionParams (Object)

EcmActionParams Class

## Properties (1)
- `Public Property ActionID() As Long` [R/W] property ActionID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ECMActionStatusData (Object)

ECMActionStatusData Class

## Properties (5)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property ActMessage() As String` [R/W] property ActMessage
- `Public Property ActStatus() As EcmActionStatusEnum` [R/W] property ActStatus
- `Public Property ReceivDate() As Date` [R/W] property ReceivDate
- `Public Property ReportID() As String` [R/W] property ReportID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ECMCodeParams (Object)

ECMCodeParams Class

## Properties (1)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ECMCodeParamsCollection (Collection)

ECMCodeParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As ECMCodeParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As ECMCodeParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EDFDocMapping (Object)

EDFDocMapping Class

## Properties (3)
- `Public Property Description() As String` [R] property Description
- `Public Property ID() As Long` [R] property ID
- `Public Property Name() As String` [R] property Name

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EDFDocMappingInputParams (Object)

EDFDocMappingInputParams Class

## Properties (2)
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R/W] property Code
- `Public Property DocType() As String` [R/W] property DocType

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EDFDocMappingsCollection (Collection)

EDFDocMappingsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As EDFDocMapping` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As EDFDocMapping` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EDFEntriesCollection (Collection)

EDFEntriesCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As EDFEntry` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As EDFEntry` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EDFEntry (Object)

EDFEntry Class

## Properties (40)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property AssignedID() As String` [R/W] property AssignedID
- `Public Property Authority() As String` [R/W] property Authority
- `Public Property BranchID() As Long` [R/W] property BranchID
- `Public Property CancellationStatus() As ElectronicDocumentEntryCancellationStatusEnum` [R/W] property CancellationStatus
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R/W] property Code
- `Public Property CreateDate() As Date` [R] property CreateDate
- `Public Property CreateTime() As Long` [R] property CreateTime
- `Public Property Description() As String` [R/W] property Description
- `Public Property DocBatchID() As String` [R/W] property DocBatchID
- `Public Property DocBatchIndex() As Long` [R/W] property DocBatchIndex
- `Public Property EDocNum() As String` [R/W] property EDocNum
- `Public Property EDocType() As Long` [R/W] property EDocType
- `Public Property Environment() As Long` [R/W] property Environment
- `Public Property GenerationType() As ElectronicDocGenTypeEnum` [R/W] property GenerationType
- `Public Property Guid() As String` [R/W] property GUID
- `Public Property IsCancelation() As BoYesNoEnum` [R] property IsCancelation
- `Public Property IsRemoved() As BoYesNoEnum` [R] property IsRemoved
- `Public Property Message() As String` [R/W] property Message
- `Public Property ObjectID() As String` [R/W] property ObjectID
- `Public Property ParentAbsEntry() As Long` [R/W] property ParentAbsEntry
- `Public Property PeriodDateFrom() As Date` [R/W] property PeriodDateFrom
- `Public Property PeriodDateTo() As Date` [R/W] property PeriodDateTo
- `Public Property PeriodNumber() As Long` [R/W] property PeriodNumber
- `Public Property PeriodType() As ElectronicDocumentEntryPeriodTypeEnum` [R/W] property PeriodType
- `Public Property PeriodYear() As Long` [R/W] property PeriodYear
- `Public Property ProcessingTarget() As String` [R/W] property ProcessingTarget
- `Public Property ReportID() As String` [R/W] property ReportID
- `Public Property ScheduledJobID() As Long` [R/W] property ScheduledJobID
- `Public Property SrcAbsEntry() As Long` [R/W] property SrcAbsEntry
- `Public Property SrcObjType() As String` [R/W] property SrcObjType
- `Public Property Status() As ElectronicDocumentEntryStatusEnum` [R/W] property Status
- `Public Property Submits() As Long` [R/W] property Submits
- `Public Property TestMode() As BoYesNoEnum` [R/W] property TestMode
- `Public Property Type() As ElectronicDocumentEntryTypeEnum` [R/W] property Type
- `Public Property UpdateDate() As Date` [R] property UpdateDate
- `Public Property UpdateTime() As Long` [R] property UpdateTime
- `Public Property User() As Long` [R] property User
- `Public Property User2() As Long` [R] property User2
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

# EDFEntryAddLogInputParams (Object)

EDFEntryAddLogInputParams Class

## Properties (9)
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R/W] property Code
- `Public Property ExportFile() As String` [R/W] property ExportFile
- `Public Property ExportFormat() As Long` [R/W] property ExportFormat
- `Public Property Guid() As String` [R/W] property GUID
- `Public Property LogData() As String` [R/W] property LogData
- `Public Property LogDataContentType() As ElectronicDocumentBlobContentTypeEnum` [R/W] property LogDataContentType
- `Public Property LogMessage() As String` [R/W] property LogMessage
- `Public Property LogType() As ElectronicDocumentEntryLogTypeEnum` [R/W] property LogType
- `Public Property ZipLogData() As BoYesNoEnum` [R/W] property ZipLogData

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EDFEntryInputParams (Object)

EDFEntryInputParams Class

## Properties (2)
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R/W] property Code
- `Public Property Guid() As String` [R/W] property GUID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EDFEntryListInputParams (Object)

EDFEntryListInputParams Class

## Properties (14)
- `Public Property Ascending() As BoYesNoEnum` [R/W] property Ascending
- `Public Property BranchID() As Long` [R/W] property BranchID
- `Public Property CancellationStatusSet() As String` [R/W] property CancellationStatusSet
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R/W] property Code
- `Public Property FromDate() As Date` [R/W] property FromDate
- `Public Property FromEntryID() As Long` [R/W] property FromEntryID
- `Public Property FromTime() As Long` [R/W] property FromTime
- `Public Property MaxLines() As Long` [R/W] property MaxLines
- `Public Property ProcessingTarget() As ElectronicDocProcessingTargetEnum` [R/W] property ProcessingTarget
- `Public Property ProcessingTargetStr() As String` [R/W] property ProcessingTargetStr
- `Public Property StoreEntryStatusSet() As String` [R/W] property StoreEntryStatusSet
- `Public Property StoreEntryTypeSet() As String` [R/W] property StoreEntryTypeSet
- `Public Property ToDate() As Date` [R/W] property ToDate
- `Public Property ToTime() As Long` [R/W] property ToTime

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EDFEntryLog (Object)

EDFEntryLog Class

## Properties (9)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property ExportFile() As String` [R/W] property ExportFile
- `Public Property ExportFormat() As Long` [R/W] property ExportFormat
- `Public Property LogData() As String` [R/W] property LogData
- `Public Property LogMessage() As String` [R/W] property LogMessage
- `Public Property LogNumber() As Long` [R] property LogNumber
- `Public Property LogOperationDate() As Date` [R/W] property LogOperationDate
- `Public Property LogOperationTime() As Long` [R/W] property LogOperationTime
- `Public Property LogType() As ElectronicDocumentEntryLogTypeEnum` [R/W] property LogType

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EDFEntryLogInputParams (Object)

EDFEntryLogInputParams Class

## Properties (7)
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R/W] property Code
- `Public Property FileName() As String` [R/W] property FileName
- `Public Property Guid() As String` [R/W] property GUID
- `Public Property KeepLogDataPrefix() As BoYesNoEnum` [R/W] property KeepLogDataPrefix
- `Public Property LogDataContentType() As ElectronicDocumentBlobContentTypeEnum` [R/W] property LogDataContentType
- `Public Property LogType() As ElectronicDocumentEntryLogTypeEnum` [R/W] property LogType
- `Public Property UnzipLogData() As BoYesNoEnum` [R/W] property UnzipLogData

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EDFEntryLogsCollection (Collection)

EDFEntryLogsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As EDFEntryLog` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As EDFEntryLog` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EDFImportEntry (Object)

Electronic document import files. Source table: ECM8.

**Remarks:** Purchasing - A/P --> Electronic Document Import Wizard.

## Properties (17)
- `Public Property AbsEntry() As Long` [R] Internal ID. Field name: AbsEntry.
- `Public Property Authority() As String` [R/W] Authority code. Field name: Authority. Length: 16 characters.
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R/W] Protocol code. Field name: Code.
- `Public Property CreateDate() As Date` [R] Creation date. Field name: CreateDate.
- `Public Property CreateTime() As Long` [R] Creation time. Field name: CreateTS.
- `Public Property FileName() As String` [R/W] Name of file imported by EDF. Field name: FileName.
- `Public Property Guid() As String` [R/W] GUID. Field name: GUID. Length: 100 characters.
- `Public Property Message() As String` [R/W] Import message. Field name: ActMessage. Length: 254 characters.
- `Public Property MetaData() As String` [R/W] Import metadata. Field name: MetaData.
- `Public Property MimeType() As String` [R/W] Type of file imported by EDF. Field name: MIMEType. Length: 128 characters.
- `Public Property ProcessingSource() As String` [R/W] Import source. Field name: ProcSource. Length: 20 characters.
- `Public Property Status() As ElectronicDocumentEntryStatusEnum` [R/W] Imported document status. Field name: ActStatus.
- `Public Property TestMode() As String` [R/W] Test mode. Field name: TestMode. Length: 1 characters.
- `Public Property UpdateDate() As Date` [R] Update date. Field name: UpdateDate.
- `Public Property UpdateTime() As Long` [R] Update time. Field name: UpdateTS.
- `Public Property User() As Long` [R] Created by user. Field name: UserSign.
- `Public Property User2() As Long` [R] Updated by user. Field name: UserSign2.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# EDFMapping (Object)

EDFMapping Class

## Properties (4)
- `Public Property FormatID() As Long` [R] property FormatID
- `Public Property Hash() As String` [R] property Hash
- `Public Property Mapping() As String` [R] property Mapping
- `Public Property Name() As String` [R] property Name

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EDFMappingInputParams (Object)

EDFMappingInputParams Class

## Properties (1)
- `Public Property Hash() As String` [R/W] property Hash

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EDFProtocol (Object)

EDFProtocol Class

## Properties (3)
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R/W] property Code
- `Public Property Description() As String` [R] property Description
- `Public Property IsActive() As BoYesNoEnum` [R] property IsActive

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EDFProtocolInputParams (Object)

EDFProtocolInputParams Class

## Properties (3)
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R/W] property Code
- `Public Property Description() As String` [R] property Description
- `Public Property IsActive() As BoYesNoEnum` [R] property IsActive

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EDFProtocolParameter (Object)

EDFProtocolParameter Class

## Properties (6)
- `Public Property BranchID() As Long` [R] property BranchID
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R] property Code
- `Public Property ParameterID() As Long` [R] property ParameterID
- `Public Property ParamName() As String` [R] property ParamName
- `Public Property ParamParameters() As String` [R] property ParamParameters
- `Public Property ParamValue() As String` [R] property ParamValue

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EDFProtocolParametersCollection (Collection)

EDFProtocolParametersCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As EDFProtocolParameter` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As EDFProtocolParameter` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EDFProtocolsCollection (Collection)

EDFProtocolsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As EDFProtocol` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As EDFProtocol` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EDFProtocolWithParameters (Object)

EDFProtocolWithParameters Class

## Properties (4)
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R] property Code
- `Public Property Description() As String` [R/W] property Description
- `Public Property EDFProtocolParametersCollection() As EDFProtocolParametersCollection` [R] property EDFProtocolParametersCollection
- `Public Property IsActive() As BoYesNoEnum` [R/W] property IsActive

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ElectronicCommunicationActionService (Object)

ElectronicCommunicationActionService Class

## Methods (8)
- `Public Sub ConfirmSuccessOfCommunication(ByVal pIECMCodeParams As ECMCodeParams)` ConfirmSuccessOfCommunication
  - param `pIECMCodeParams`: 
- `Public Function GetAction(ByVal pIECMCodeParams As ECMCodeParams) As ECMActionStatusData` GetAction
  - param `pIECMCodeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ElectronicCommunicationActionServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ElectronicCommunicationActionServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Sub ReportErrorAndContinue(ByVal pIECMCodeParams As ECMCodeParams)` ReportErrorAndContinue
  - param `pIECMCodeParams`: 
- `Public Sub ReportErrorAndStop(ByVal pIECMCodeParams As ECMCodeParams)` ReportErrorAndStop
  - param `pIECMCodeParams`: 
- `Public Sub UpdateAction(ByVal pActionStatusData As ECMActionStatusData)` UpdateAction
  - param `pActionStatusData`: 

# ElectronicCommunicationActionsService (Object)

ElectronicCommunicationActionsService Class

## Methods (11)
- `Public Function AddEcmAction(ByVal pIEcmAction As EcmAction) As EcmAction` AddEcmAction
  - param `pIEcmAction`: 
- `Public Function AddEcmActionLog(ByVal pIEcmActionLog As EcmActionLog) As EcmActionLog` AddEcmActionLog
  - param `pIEcmActionLog`: 
- `Public Sub DeleteEcmAction(ByVal pIEcmAction As EcmAction)` DeleteEcmAction
  - param `pIEcmAction`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ElectronicCommunicationActionsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ElectronicCommunicationActionsServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetEcmAction(ByVal pIEcmActionParams As EcmActionParams) As EcmAction` GetEcmAction
  - param `pIEcmActionParams`: 
- `Public Function GetEcmActionByDoc(ByVal pIEcmActionDocParams As EcmActionDocParams) As EcmAction` GetEcmActionByDoc
  - param `pIEcmActionDocParams`: 
- `Public Function GetEcmActionLog(ByVal pIEcmActionLogParams As EcmActionLogParams) As EcmActionLog` GetEcmActionLog
  - param `pIEcmActionLogParams`: 
- `Public Function GetEcmActionLogList(ByVal pIEcmAction As EcmAction) As EcmActionLogCollection` GetEcmActionLogList
  - param `pIEcmAction`: 
- `Public Sub UpdateEcmAction(ByVal pIEcmAction As EcmAction)` UpdateEcmAction
  - param `pIEcmAction`: 

# ElectronicDocumentService (Object)

ElectronicDocumentService Class

## Methods (16)
- `Public Sub AddImportEntry(ByVal pIEDFImportEntry As EDFImportEntry)` Import electronic document.
  - param `pIEDFImportEntry`: Electronic document import file.
- `Public Sub AddLog(ByVal pIEDFEntryLogInputParams As EDFEntryAddLogInputParams)` AddLog
  - param `pIEDFEntryLogInputParams`: 
- `Public Sub ExportEntryLog(ByVal pIEDFEntryLogInputParams As EDFEntryLogInputParams)` ExportEntryLog
  - param `pIEDFEntryLogInputParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ElectronicDocumentServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ElectronicDocumentServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetDocMappingList(ByVal pIEDFDocMappingInputParams As EDFDocMappingInputParams) As EDFDocMappingsCollection` GetDocMappingList
  - param `pIEDFDocMappingInputParams`: 
- `Public Function GetEntry(ByVal pIEDFEntryInputParams As EDFEntryInputParams) As EDFEntry` GetEntry
  - param `pIEDFEntryInputParams`: 
- `Public Function GetEntryList(ByVal pIEDFEntryListInputParams As EDFEntryListInputParams) As EDFEntriesCollection` GetEntryList
  - param `pIEDFEntryListInputParams`: 
- `Public Function GetLastLog(ByVal pIEDFEntryLogInputParams As EDFEntryLogInputParams) As EDFEntryLog` GetLastLog
  - param `pIEDFEntryLogInputParams`: 
- `Public Function GetLogs(ByVal pIEDFEntryLogInputParams As EDFEntryLogInputParams) As EDFEntryLogsCollection` GetLogs
  - param `pIEDFEntryLogInputParams`: 
- `Public Function GetMappingByHash(ByVal pIEDFMappingInputParams As EDFMappingInputParams) As EDFMapping` GetMappingByHash
  - param `pIEDFMappingInputParams`: 
- `Public Function GetProtocol(ByVal pIEDFProtocolInputParams As EDFProtocolInputParams) As EDFProtocol` GetProtocol
  - param `pIEDFProtocolInputParams`: 
- `Public Function GetProtocolParameters(ByVal pIEDFProtocolInputParams As EDFProtocolInputParams) As EDFProtocolWithParameters` GetProtocolParameters
  - param `pIEDFProtocolInputParams`: 
- `Public Function GetProtocols() As EDFProtocolsCollection` GetProtocols
- `Public Sub UpdateEntry(ByVal pIEDFEntry As EDFEntry)` UpdateEntry
  - param `pIEDFEntry`: 

# ElectronicFileFormat (Object)

Represents the generic electronic file formats in SAP Business One. Source table: OLLF.

## Properties (8)
- `Public Property Description() As String` [R] The description for the electronic file format. Field name: Descr.
- `Public Property FormatID() As Long` [R] The format ID. This is a foreign key to the File Format table (OFRM). Field name: FrmId.
- `Public Property MenuName() As String` [R] The menu entry name for the electronic file format that to be displayed in the SAP Business One. Field name: MenuName.
- `Public Property MenuPath() As String` [R] The menu path in SAP Business One for accessing the electronic file format. Field name: MenuPath.
- `Public Property Name() As String` [R] The name of the electronic file format. Field name: Name.
- `Public Property OutputFilePath() As String` [R] The destination file path for the generated electronic file. Field name: OutPath.
- `Public Property SchemaVersion() As String` [R] The version of the electronic file schema. Field name: SchVersion.
- `Public Property Version() As String` [R] The version of the electronic file format. Field name: Version.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ElectronicFileFormatParams (Object)

Holds the key and name to an existing electronic file format. This object is used to pass keys to and retrieve keys from ElectronicFileFormatsService methods.

## Properties (2)
- `Public Property FormatID() As Long` [R/W] Returns the format ID of the electronic file format. Field name: FrmId.
- `Public Property Name() As String` [R/W] Returns the name of the electronic file format. Field name: Name.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ElectronicFileFormatsParams (Collection)

A collection of ElectronicFileFormatParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ElectronicFileFormatParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ElectronicFileFormatParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ElectronicFileFormatsService (Object)

The ElectronicFileFormatsService service enables you to import, look up, and delete the generic electronic file formats in SAP Business One. Source table: OLLF.

**Remarks:** To display the Electronic File Manager - Setup window, from SAP Business One, choose Administration --> Setup --> General --> Electronic File Manager - Setup.

## Methods (7)
- `Public Function AddElectronicFileFormat(ByVal pIImportFileParam As ImportFileParam) As ElectronicFileFormatParams` Adds a new electronic file format.
  - param `pIImportFileParam`: The data for the new electronic file format.
- `Public Sub DeleteElectronicFileFormat(ByVal pIElectronicFileFormatParams As ElectronicFileFormatParams)` Deletes an existing electronic file format.
  - param `pIElectronicFileFormatParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ElectronicFileFormatsServiceDataInterfaces) As Object` Creates an empty data structure for use with the ElectronicFileFormatsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ElectronicFileFormatsServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLFile(Hashtable Properties, String Path)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair In Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        oGeneralData.ToXMLFile(Path);

        //Retrieve XML and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLFile(Path);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLString(Hashtable Properties)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;
        string XMLString;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair in Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        XMLString = oGeneralData.ToXMLString();

        //Retrieve XML string and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLString(XMLString);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetElectronicFileFormat(ByVal pIElectronicFileFormatParams As ElectronicFileFormatParams) As ElectronicFileFormat` Retrieves an electronic file format. The electronic file format is specified by its key, which is contained in the ElectronicFileFormatParams object passed to the method.
  - param `pIElectronicFileFormatParams`: The key of the electronic file format to retrieve.
- `Public Function GetElectronicFileFormatList() As ElectronicFileFormatsParams` Returns the ElectronicFileFormatsParams data collection that identify all electronic file formats.

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

# ElectronicProtocolCollection (Collection)

ElectronicProtocolCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As ElectronicProtocol` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As ElectronicProtocol` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ElectronicProtocols (Object)

ElectronicProtocols Class

## Properties (27)
- `Public Property Confirmation() As String` [R/W] property Confirmation
- `Public Property Count() As Long` [R] property Count
- `Public Property EBillingIRN() As String` [R/W] The IRN of e-billing.
- `Public Property EBooksInvoiceType() As String` [R/W] property EBooksInvoiceType
- `Public Property EBooksInvoiceTypeofNegative() As String` [R/W] property EBooksInvoiceTypeofNegative
- `Public Property EBooksMARK() As String` [R] property EBooksMARK
- `Public Property EBooksMARKofNegative() As String` [R] property EBooksMARKofNegative
- `Public Property EBooksRelevant() As BoYesNoEnum` [R/W] property EBooksRelevant
- `Public Property EDocType() As Long` [R/W] property EDocType
- `Public Property EETBKP() As String` [R/W] property EETBKP
- `Public Property EETPKP() As String` [R/W] property EETPKP
- `Public Property FechaTimbrado() As String` [R] property FechaTimbrado
- `Public Property FPAProgressivo() As String` [R] property FPAProgressivo
- `Public Property FPASendDateSDI() As Date` [R] property FPASendDateSDI
- `Public Property FPASequenceNumber() As Long` [R] property FPASequenceNumber
- `Public Property GenerationType() As ElectronicDocGenTypeEnum` [R/W] property GenerationType
- `Public Property MappingID() As Long` [R/W] property MappingID
- `Public Property NoCertificadoSAT() As String` [R] property NoCertificadoSAT
- `Public Property PaymentMethod() As String` [R] property PaymentMethod
- `Public Property ProtocolCode() As ElectronicDocProtocolCodeEnum` [R/W] property ProtocolCode
- `Public Property ProtocolDescription() As String` [R] property ProtocolDescription
- `Public Property RelatedDocuments() As RelatedDocuments` [R] property RelatedDocuments
- `Public Property RfcProvCertif() As String` [R] property RfcProvCertif
- `Public Property SelloSAT() As String` [R] property SelloSAT
- `Public Property SignatureDigest() As String` [R] property SignatureDigest
- `Public Property SignatureInputMessage() As String` [R] property SignatureInputMessage
- `Public Property TestingMode() As BoYesNoEnum` [R] property TestingMode

## Methods (3)
- `Public Sub Add()` method Add
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 

# ElectronicReportInfo (Object)

Setup values for electronic reports.

**Remarks:** Specific to localization for France.

**Example:**
- C# example (from SAP's help):
  ```csharp
  "SAPbobsCOM.CompanyService oCmpSrv = oCompany.GetCompanyService();
  SAPbobsCOM.AdminInfo oAdminInfo = oCmpSrv.GetAdminInfo();
  oAdminInfo.ElectronicReportInfo.ShareCapitalAmount = 12.3;
  oAdminInfo.ElectronicReportInfo.CompanyType = ""BB"";
  oCmpSrv.UpdateAdminInfo(oAdminInfo);
  ```

## Properties (2)
- `Public Property CompanyType() As String` [R/W] Company type.
- `Public Property ShareCapitalAmount() As Double` [R/W] Share capital amount.

# ElectronicSeries (Object)

ElectronicSeries Class

## Properties (10)
- `Public Property ApprovalNumber() As Long` [R/W] property ApprovalNumber
- `Public Property ApprovalYear() As Long` [R/W] property ApprovalYear
- `Public Property ElectronicSeries() As Long` [R] property ElectronicSeries
- `Public Property InitialNumber() As String` [R/W] property InitialNumber
- `Public Property LastNumber() As String` [R/W] property LastNumber
- `Public Property Name() As String` [R/W] property Name
- `Public Property NextNumber() As String` [R] property NextNumber
- `Public Property Prefix() As String` [R/W] property Prefix
- `Public Property Remarks() As String` [R/W] property Remarks
- `Public Property Series() As Long` [R/W] property Series

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ElectronicSeriesCollection (Collection)

ElectronicSeriesCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As ElectronicSeries` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As ElectronicSeries` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ElectronicSeriesParams (Object)

ElectronicSeriesParams Class

## Properties (1)
- `Public Property ElectronicSeries() As Long` [R/W] property ElectronicSeries

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EmailGroup (Object)

EmailGroup Class

## Properties (2)
- `Public Property EmailGroupCode() As String` [R/W] property EmailGroupCode
- `Public Property EmailGroupName() As String` [R/W] property EmailGroupName

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EmailGroupParams (Object)

EmailGroupParams Class

## Properties (2)
- `Public Property EmailGroupCode() As String` [R/W] property EmailGroupCode
- `Public Property EmailGroupName() As String` [R] property EmailGroupName

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EmailGroupParamsCollection (Collection)

EmailGroupParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As EmailGroupParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As EmailGroupParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EmailGroupsService (Object)

EmailGroupsService Class

## Methods (8)
- `Public Function Add(ByVal pIEmailGroup As EmailGroup) As EmailGroupParams` Add
  - param `pIEmailGroup`: 
- `Public Sub Delete(ByVal pIEmailGroupParams As EmailGroupParams)` Delete
  - param `pIEmailGroupParams`: 
- `Public Function Get(ByVal pIEmailGroupParams As EmailGroupParams) As EmailGroup` Get
  - param `pIEmailGroupParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As EmailGroupsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `EmailGroupsServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As EmailGroupParamsCollection` GetList
- `Public Sub Update(ByVal pIEmailGroup As EmailGroup)` Update
  - param `pIEmailGroup`: 

# EmployeeAbsenceInfo (Object)

EmployeeAbsenceInfo is a child object of the EmployeesInfo object and represents the employee absence information. Source table: HEM1.

**Remarks:** To display the form in the application: - Select Human Resources --> Employee Master Data - Select the Administration tab. - Click Absence.

## Properties (9)
- `Public Property ApprovedBy() As String` [R/W] Sets or returns the person name that approves the absence. Field name: approvedBy. Length: 20 characters.
- `Public Property ConfirmerNumber() As Long` [R/W] Sets or returns the employee's Confirmer Number. Field name: cnfrmrNum). This is a foreign key to the EmployeesInfo object.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property EmployeeID() As Long` [R/W] Sets or returns the employee ID, which SAP Business One generates automatically when adding a new employee. Field name: empID. This is a foreign key to the EmployeesInfo object. Sets or returns the employee ID, which SAP Business One generates automatically when adding a new employee. Field name: empID. This is a foreign key to the EmployeesInfo object.
- `Public Property FromDate() As Date` [R/W] Sets or returns the start date of the employee absence period. Field name: fromDate.
- `Public Property LineNum() As Long` [R] Returns the current row number in the employee absence information list. Field name: line.
- `Public Property Reason() As String` [R/W] Sets or returns the reason for employee absence. Field name: reason. Length: 20 characters.
- `Public Property ToDate() As Date` [R/W] Sets or returns the end date of the employee absence period. Field name: toDate.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the line number. The count starts from 0. Specifies the row number. The count starts from 0.

# EmployeeBranchAssignment (Object)

EmployeeBranchAssignment Class

## Properties (3)
- `Public Property BPLID() As Long` [R/W] property BPLID
- `Public Property Count() As Long` [R] property Count
- `Public Property EmployeeID() As Long` [R] property EmployeeID

## Methods (3)
- `Public Sub Add()` method Add
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 

# EmployeeEducationInfo (Object)

EmployeeEducationInfo is a child object of the EmployeesInfo object and represents the employee education information. Source table: HEM2.

**Remarks:** To display the form in the application: - Select Human Resources --> Employee Master Data. - Select the Administration tab. - Click Education.

## Properties (10)
- `Public Property Count() As Long` [R] Returns the total data rows in the employee education information list.
- `Public Property Diploma() As String` [R/W] Sets or returns the diploma of the employee (such as, BA, MBA, and so on). Field name: diploma. Length: 50 characters.
- `Public Property EducationType() As Long` [R/W] Sets or returns the education type of the employee (such as, high-school, university, and so on). Field name: type. Length: 50 characters. This is a foreign key to the Education Types table (OHED - not exposed through the DI API).
- `Public Property EmployeeNo() As Long` [R/W] Sets or returns the employee ID, which SAP Business One generates automatically when adding a new employee. Field name: empID. This is a foreign key to the EmployeesInfo object.
- `Public Property FromDate() As Date` [R/W] Sets or returns the start date of the education period. Field name: fromDate.
- `Public Property Institute() As String` [R/W] Sets or returns the institute name. Field name: institute. Length: 100 characters.
- `Public Property LineNum() As Long` [R] Returns the current row number in the employee education list. Field name: line.
- `Public Property Major() As String` [R/W] Sets or returns the major study subject. Field name: major. Length: 50 characters.
- `Public Property ToDate() As Date` [R/W] Sets or returns the end date of the education period. Field name: toDate.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# EmployeeFullNamesParams (Object)

EmployeeFullNamesParams Class

## Properties (2)
- `Public Property EmployeeFullName() As String` [R/W] property EmployeeFullName
- `Public Property EmployeeID() As Long` [R/W] property EmployeeID

# EmployeeFullNamesParamsCollection (Collection)

EmployeeFullNamesParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As EmployeeFullNamesParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As EmployeeFullNamesParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EmployeeIDType (Object)

EmployeeIDType Class

## Properties (1)
- `Public Property IDType() As String` [R/W] property IDType

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EmployeeIDTypeParams (Object)

EmployeeIDTypeParams Class

## Properties (1)
- `Public Property IDType() As String` [R/W] property IDType

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EmployeeIDTypeParamsCollection (Collection)

EmployeeIDTypeParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As EmployeeIDTypeParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As EmployeeIDTypeParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EmployeeIDTypeService (Object)

EmployeeIDTypeService Class

## Methods (8)
- `Public Function Add(ByVal pIEmployeeIDType As EmployeeIDType) As EmployeeIDTypeParams` Add
  - param `pIEmployeeIDType`: 
- `Public Sub Delete(ByVal pIEmployeeIDTypeParams As EmployeeIDTypeParams)` Delete
  - param `pIEmployeeIDTypeParams`: 
- `Public Function Get(ByVal pIEmployeeIDTypeParams As EmployeeIDTypeParams) As EmployeeIDType` Get
  - param `pIEmployeeIDTypeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As EmployeeIDTypeServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `EmployeeIDTypeServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As EmployeeIDTypeParamsCollection` GetList
- `Public Sub Update(ByVal pIEmployeeIDType As EmployeeIDType)` Update
  - param `pIEmployeeIDType`: 

# EmployeePosition (Object)

EmployeePosition Class

## Properties (3)
- `Public Property Description() As String` [R/W] property Description
- `Public Property Name() As String` [R/W] property Name
- `Public Property PositionID() As Long` [R] property PositionID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EmployeePositionParams (Object)

EmployeePositionParams Class

## Properties (3)
- `Public Property Description() As String` [R] property Description
- `Public Property Name() As String` [R] property Name
- `Public Property PositionID() As Long` [R/W] property PositionID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EmployeePositionParamsCollection (Collection)

EmployeePositionParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As EmployeePositionParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As EmployeePositionParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EmployeePositionService (Object)

EmployeePositionService Class

## Methods (8)
- `Public Function Add(ByVal pIEmployeePosition As EmployeePosition) As EmployeePositionParams` Add
  - param `pIEmployeePosition`: 
- `Public Sub Delete(ByVal pIEmployeePositionParams As EmployeePositionParams)` Delete
  - param `pIEmployeePositionParams`: 
- `Public Function Get(ByVal pIEmployeePositionParams As EmployeePositionParams) As EmployeePosition` Get
  - param `pIEmployeePositionParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As EmployeePositionServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `EmployeePositionServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As EmployeePositionParamsCollection` GetList
- `Public Sub Update(ByVal pIEmployeePosition As EmployeePosition)` Update
  - param `pIEmployeePosition`: 

# EmployeePrevEmpoymentInfo (Object)

EmployeePrevEmploymentInfo is a child object of the EmployeesInfo object and represents the employee previous employment information. Source table: HEM4.

**Remarks:** To display the form in the application: - Select Human Resources --> Employee Master Data. - Select the Administration tab. - Click Previous Employment.

## Properties (9)
- `Public Property Count() As Long` [R] Returns the number of lines in the employee previous employment list.
- `Public Property EmployeeNo() As Long` [R/W] P>Sets or returns the employee ID, which SAP Business One generates automatically when adding a new employee. Field name: empID. This is a foreign key to the EmployeesInfo object.
- `Public Property Employer() As String` [R/W] Sets or returns the name of the previous employer. Field name: employer. Length: 50 characters.
- `Public Property FromDtae() As Date` [R/W] Sets or returns the start date of the previous employment period. Field name: fromDate.
- `Public Property LineNum() As Long` [R] Returns the current row number in the employee reviews list. Field name: line.
- `Public Property Position() As String` [R/W] Sets or returns the employee position in the previous employment. Field name: position. Length: 50 characters.
- `Public Property Remarks() As String` [R/W] Sets or returns a memo type string that specifies remarks of the previous employment. Field name: remarks. Length: 64,000 characters.
- `Public Property ToDate() As Date` [R/W] Sets or returns the end date of the previous employment period. Field name: toDate.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# EmployeeReviewsInfo (Object)

EmployeeReviewsInfo is a child object of the EmployeesInfo object and represents the employee reviews information. Source table: HEM3.

**Remarks:** To display the form in the application: - Select Human Resources --> Employee Master Data. - Select the Administration tab. - Click Reviews.

## Properties (9)
- `Public Property Count() As Long` [R] Returns the total data rows in the employee reviews list.
- `Public Property Date() As Date` [R/W] Sets or returns the date of the review. Field name: date.
- `Public Property EmployeeNo() As Long` [R/W] Sets or returns the employee ID, which SAP Business One generates automatically when adding a new employee. Field name: empID. This is a foreign key to the EmployeesInfo object.
- `Public Property Grade() As String` [R/W] Sets or returns the grade of the employee. Field name: grade. Length: 50 characters.
- `Public Property LineNum() As Long` [R] Returns the current row number in the employee reviews list. Field name: line.
- `Public Property Manager() As Long` [R/W] Sets or returns the manager's employee-ID of the employee. Field name: manager. This is a foreign key to the EmployeesInfo object.
- `Public Property Remarks() As String` [R/W] Sets or returns a memo type string that specifies remarks of the employee review. Field name: remarks. Length: 64,000 characters.
- `Public Property ReviewDescription() As String` [R/W] Sets or returns a description of the employee review. Field name: reviewDesc. Length: 100 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# EmployeeRoleSetup (Object)

Represents an employee role. Source table: OHTY Mandatory properties: Name and Description cannot both be blank.

## Properties (3)
- `Public Property Description() As String` [R/W] A description for the employee role. Field name: descriptio
- `Public Property Name() As String` [R/W] The display name of the employee role. Field name: name
- `Public Property TypeID() As Long` [R] The key for the employee role. Field name: typeID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# EmployeeRoleSetupParams (Object)

Holds the key and name to an existing employee role. This object is used to pass keys to and retrieve keys from EmployeeRolesSetupService methods.

## Properties (2)
- `Public Property Name() As String` [R] The display name of a specific employee role. Field name: name
- `Public Property TypeID() As Long` [R/W] The key for a specific role. Field name: typeID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# EmployeeRoleSetupParamsCollection (Collection)

A collection of EmployeeRoleSetupParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As EmployeeRoleSetupParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As EmployeeRoleSetupParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# EmployeeRolesInfo (Object)

A child object of the EmployeesInfo object that represents the employee roles, for example, technician, sales employee and purchasing. Source table: HEM6.

**Remarks:** To display the form in the application: - Select Human Resources --> Employee Master Data. - Select the Membership tab. To modify the master data list of employees roles, use the EmployeeRolesSetupService service.

## Properties (5)
- `Public Property Count() As Long` [R] Returns the number of roles of the employee.
- `Public Property EmployeeID() As Long` [R/W] Sets or returns the employee ID, which SAP Business One generates automatically when adding a new employee. Field name: empID. This is a foreign key to the EmployeesInfo object.
- `Public Property LineNum() As Long` [R] Returns the current row number in the employee roles list. Field name: line.
- `Public Property RoleID() As Long` [R/W] Sets or returns the role ID of the employee. Field name: roleID. This is a foreign key to OHTY table, which is not exposed through the DI API.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# EmployeeRolesSetupService (Object)

The EmployeeRolesSetupService service enables you to add, look up and remove roles in the employee roles master data table. To see the list of employee roles and create a new one, select Human Resources --> Employee Master Data, and select the Membership tab. Source table: OHTY

**Remarks:** This service affects the employee roles master data. The role for a specific employee can be retrieved from the EmployeeRolesInfo object of an employee's EmployeesInfo object. System roles have their Locked field set to Y. System roles cannot be updated or deleted.

## Methods (8)
- `Public Function AddEmployeeRoleSetup(ByVal pIEmployeeRoleSetup As EmployeeRoleSetup) As EmployeeRoleSetupParams` Adds an employee role.
  - param `pIEmployeeRoleSetup`: The data for the new employee role
  - returns: Contains the key (TypeID) of the new role.
  - C# example (from SAP's help):
    ```csharp
    public void AddEmployeeRole()
    {
        try
        {
            EmployeeRolesSetupService oRoleSrv;
            oRoleSrv = (SAPbobsCOM.EmployeeRolesSetupService)(MainModule.oCmpSrv.GetBusinessService(ServiceTypes.EmployeeRolesSetupService));

            EmployeeRoleSetup addLine;
            addLine = (EmployeeRoleSetup)oRoleSrv.GetDataInterface(EmployeeRolesSetupServiceDataInterfaces.erssEmployeeRoleSetup);

            addLine.Name = "Role1";
            addLine.Description = "Desc1";
            oRoleSrv.AddEmployeeRoleSetup(addLine);

        }
        catch (Exception ex)
        {
            Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
        }
    }
    ```
- `Public Sub DeleteEmployeeRoleSetup(ByVal pIEmployeeRoleSetupParams As EmployeeRoleSetupParams)` Deletes an existing employee role. The role is specified by its key (TypeID), which is contained in the EmployeeRoleSetupParams object passed to the method.
  - param `pIEmployeeRoleSetupParams`: The key of the role to be deleted
  - remarks: System roles -- those with their Locked field set to Y -- cannot be deleted. Roles that have been assigned to an employee, via the EmployeeRolesInfo object, cannot be deleted.
  - C# example (from SAP's help):
    ```csharp
    public void delete()
    {
      try
      {
          EmployeeRoleSetupParams delLine;
          delLine = (EmployeeRoleSetupParams)oRoleSrv.GetDataInterface(SAPbobsCOM.EmployeeRolesSetupServiceDataInterfaces.erssEmployeeRoleSetupParams);

          //delete a record
          //please note that the typeID should be the typeID of an existing record.
          delLine.TypeID = 19;
          //delete
          oRoleSrv.DeleteEmployeeRoleSetup(delLine);
      }
      catch (Exception ex)
      {
          Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
      }
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As EmployeeRolesSetupServiceDataInterfaces) As Object` Creates an empty data structure for use with the EmployeeRolesSetupService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `EmployeeRolesSetupServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLFile(Hashtable Properties, String Path)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair In Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        oGeneralData.ToXMLFile(Path);

        //Retrieve XML and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLFile(Path);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLString(Hashtable Properties)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;
        string XMLString;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair in Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        XMLString = oGeneralData.ToXMLString();

        //Retrieve XML string and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLString(XMLString);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetEmployeeRoleSetup(ByVal pIEmployeeRoleSetupParams As EmployeeRoleSetupParams) As EmployeeRoleSetup` Retrieves a specific employee role. The role is specified by its key (TypeID), which is contained in the EmployeeRoleSetupParams object passed to the method.
  - param `pIEmployeeRoleSetupParams`: The key of the role to retrieve.
  - returns: The role with the specified key.
- `Public Function GetEmployeeRoleSetupList() As EmployeeRoleSetupParamsCollection` Retrieves the keys and names of all the employee roles.
  - C# example (from SAP's help):
    ```csharp
    public void getlist()
    {
      try
      {
          EmployeeRoleSetupParamsCollection getlistParams;
          getlistParams = oRoleSrv.GetEmployeeRoleSetupList();

          String resultSet = "";

          foreach (EmployeeRoleSetupParams record in getlistParams)
          {
              resultSet = resultSet + record.TypeID + "\t" + record.Name + "\n";
          }

          Interaction.MsgBox(resultSet, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
      }
      catch (Exception ex)
      {
          Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
      }
    }
    ```
- `Public Sub UpdateEmployeeRoleSetup(ByVal pIEmployeeRoleSetup As EmployeeRoleSetup)` Updates an existing employee role. The data for the role, including the key of the role to be updated, is contained in the EmployeeRoleSetup passed to the method. To update a role, you must first retrieve it using the GetEmployeeRoleSetup method.
  - param `pIEmployeeRoleSetup`: The data for the role to be updated. The EmployeeRoleSetup object must contain the key of the object to be updated.
  - remarks: System roles -- those with their Locked field set to Y -- cannot be updated.

# EmployeeSavingsPaymentInfo (Object)

A child object of the EmployeesInfo object that represents the employee's capital formation savings payments. Source table: HEM7.

**Remarks:** To display the form in the SAP Business One application: Choose Human Resources --> Employee Master Data, and select the Finance tab.

## Properties (14)
- `Public Property AG() As String` [R/W] The company part of the capital formation savings payments contract. Field name: AG. Length: 20 characters.
- `Public Property AGcurrency() As String` [R/W] The currency for the company part of the capital formation savings payments contract. Field name: AGCurrency.
- `Public Property AN() As String` [R/W] The employee part of the capital formation savings payments contract. Field name: AN. Length: 20 characters.
- `Public Property ANcurrency() As String` [R/W] The currency for the employee part of the capital formation savings payments contract. Field name: ANCurrency.
- `Public Property BankAccount() As String` [R/W] The bank account recipient of the capital formation savings payments contract. Field name: BankAcct. Length: 20 characters.
- `Public Property BankCode() As String` [R/W] The bank code recipient of the capital formation savings payments contract. Field name: BankCode. Length: 20 characters.
- `Public Property BankName() As String` [R/W] The bank name recipient of the capital formation savings payments contract. Field name: BankName. Length: 50 characters.
- `Public Property ContractName() As String` [R/W] The name of the capital formation savings payments contract. Field name: ConName. Length: 50 characters.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
- `Public Property EmployeeID() As Long` [R/W] The foreign key to the EmployeesInfo object. Field name: empID.
- `Public Property LineNum() As Long` [R] Returns the current row number.
- `Public Property PaymentNotes() As String` [R/W] The payment notes of the capital formation savings payments contract. Field name: PmntNotes. Length: 50 characters.
- `Public Property Sequence() As ContractSequenceEnum` [R/W] The contract sequence. Field name: Sequence.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# EmployeesInfo (Object)

EmployeesInfo is a business object that represents the employee master data in the Human Resources module. This object enables you to: - Add employee's details. - Retrieve employee's details by its key. - Update employee's details. - Save the object in XML format. Source table: OHEM.

**Remarks:** Mandatory fields in SAP Business One: FirstName and LastName. To display the form in the application: - Select Human Resources --> Employee Master Data.

## Properties (127)
- `Public Property AbsenceInfo() As EmployeeAbsenceInfo` [R] Returns the EmployeeAbsenceInfo object.
- `Public Property AccountantResponsible() As BoYesNoEnum` [R/W] property AccountantResponsible
- `Public Property Active() As BoYesNoEnum` [R/W] property Active
- `Public Property AdditionalAmount() As Double` [R/W] The additional benefit amount of the employee. Field: AddiAmnt.
- `Public Property AdditionalCurrency() As String` [R/W] The currency of the additional benefit amount. Field: AddiCurr.
- `Public Property AdditionalUnit() As EmployeeExemptionUnitEnum` [R/W] The time period unit of the additional benefit. Field: AddiUnit.
- `Public Property ApplicationUserID() As Long` [R/W] Sets or returns the employee user code of SAP Business One application. Field name: userId. This is a foreign key to the Users object.
- `Public Property AttachmentEntry() As Long` [R/W] Sets or returns the Attachment Entry. Field name: AtcEntry.
- `Public Property Attachments() As Attachments` [R] Returns the Attachments object.
- `Public Property AuthorizationForRetrieveFromSEFAZ() As BoYesNoEnum` [R/W] Authorization to Retrieve NFe from SEFAZ. Field name: ARetSEFAZ.
- `Public Property BankAccount() As String` [R/W] Sets or returns the bank account number of the employee . Field name: bankAcount. Length: 100 characters.
- `Public Property BankBranch() As String` [R/W] Sets or returns the bank branch name of the employee . Field name: branch Length: 100 characters
- `Public Property BankBranchNum() As String` [R/W] Sets or returns the bank branch number of the employee . Field name: bankBranNo. Length: 30 characters.
- `Public Property BankCode() As String` [R/W] Sets or returns the employee bank name. Field name: bankCode. Length: 30 characters.
- `Public Property BankCodeForDATEV() As String` [R/W] The bank code for DATEV. Field name: BCodeDateV. Length: 20 characters.
- `Public Property BirthPlace() As String` [R/W] The birth place of the employee. Field: BirthPlace.
- `Public Property BPLID() As Long` [R/W] property BPLID
- `Public Property Branch() As Long` [R/W] Sets or returns the branch office of the employee. Field name: branch.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CitizenshipCountryCode() As String` [R/W] Sets or returns the citizenship country code. Field name: citizenshp. This is a foreign key to the Countries table (OCRY - not exposed through the DI API). Length: 3 characters.
- `Public Property CompanyNumber() As String` [R/W] Indicate the company number to which the employee belongs, in case there are various numbers available within the company. Field name: CompanyNum. Length: 20 characters.
- `Public Property CostCenterCode() As String` [R/W] Sets or returns the cost center to which the employee belongs. Field name: CostCenter.
- `Public Property CountryOfBirth() As String` [R/W] Sets or returns the country of birth of the employee. Field name: brthCountr. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
- `Public Property CPF() As String` [R/W] property CPF
- `Public Property CRCNumber() As String` [R/W] property CRCNumber
- `Public Property CRCState() As String` [R/W] property CRCState
- `Public Property CreateDate() As Date` [R] property CreateDate
- `Public Property CreateTime() As Date` [R] property CreateTime
- `Public Property DateOfBirth() As Date` [R/W] Sets or returns the birth date of the employee. Field name: birthDate.
- `Public Property Department() As Long` [R/W] Sets or returns the employee department. Field name: dept This is a foreign key to the Departments table (OUDP), which is exposed via the DepartmentsService object.
- `Public Property DeviatingBankAccountOwner() As BoYesNoEnum` [R/W] Indicate whether the bank account owner is a person other than the employee, for example, the spouse of the employee. Field: DevBAOwner.
- `Public Property DIRFResponsible() As BoYesNoEnum` [R/W] property DIRFResponsible
- `Public Property EducationInfo() As EmployeeEducationInfo` [R] Returns the EmployeeEducationInfo object.
- `Public Property EducationStatus() As String` [R/W] The education level of the employee. 1 - Without Profession 2 - With Profession 3 - High school without profession 4 - High school with profession 5 - Professional skilled exam 6 - University 7 - Indication not possible Field: StatusOfE.
- `Public Property eMail() As String` [R/W] Sets or returns the e-mail address. Field name: email. Length: 100 characters.
- `Public Property EmployeeBranchAssignment() As EmployeeBranchAssignment` [R] property EmployeeBranchAssignment
- `Public Property EmployeeCode() As String` [R/W] property EmployeeCode
- `Public Property EmployeeCosts() As Double` [R/W] Sets or returns the employee costs. Field name: empCostCur.
- `Public Property EmployeeCostsCurrency() As String` [R/W] Sets or returns the currency of the employee cost. Field name: empCostCur. Length: 3 characters.
- `Public Property EmployeeCostUnit() As BoSalaryCostUnits` [R/W] Sets or returns a valid value of BoSalaryCostUnits type that specifies the employee cost unit (for example: per hour, per day, per month, and so on). Field name: empCostUnt.
- `Public Property EmployeeID() As Long` [R] Returns the employee ID. Field name: empID.
  - remarks: SAP Business One generates a consequent ID number automatically when adding a new employee.
- `Public Property EmployeeRolesInfo() As EmployeeRolesInfo` [R] Returns the EmployeeRolesInfo child object.
- `Public Property EmployeeType() As Long` [R/W] Sets or returns the default role ID of the employee. Field name: type. This is a foreign key to the Employee Type table (OHTY - not exposed through the DI API).
  - remarks: To set a default role ID, first set the RoleID in the EmployeeRolesInfo child object.
- `Public Property ExemptionAmount() As Double` [R/W] The amount of the exemption benefit of the employee. Field: ExemptAmnt.
- `Public Property ExemptionCurrency() As String` [R/W] The currency of the exemption benefit amount. Field: ExemptCurr.
- `Public Property ExemptionUnit() As EmployeeExemptionUnitEnum` [R/W] The time period unit of the exemption benefit. Field: ExemptUnit.
- `Public Property ExternalEmployeeNumber() As String` [R/W] The external employee number. Field: ExtEmpNo.
- `Public Property Fax() As String` [R/W] Sets or returns the fax number. Field name: fax. Length: 50 characters.
- `Public Property FirstName() As String` [R/W] Sets or returns the employee first name. Field name: firstName. Mandatory property. Length: 50 characters.
- `Public Property Gender() As BoGenderTypes` [R/W] Sets or returns a valid value of BoGenderTypes type that specifies the employee gender type. Field name: sex.
- `Public Property HealthInsuranceCode() As String` [R/W] The health insurance code of the employee. Field name: HeaInsCode. Length: 50 characters.
- `Public Property HealthInsuranceName() As String` [R/W] The health insurance name of the employee. Field name: HeaInsName. Length: 50 characters.
- `Public Property HealthInsuranceType() As String` [R/W] Indicate the type of the employee's health insurance. - AOK - Allgemeine Ortskrankenkasse (AOK) - IKK - Innungskrankenkasse (IKK) - EKK - Ersatzkasse (EKK) - BKK - Betriebskrankenkasse (BKK) - BKS - Bundesknappschaft (BKS) - LKK - Landeskrankenkasse (LKK) Field name: HeaInsType. Length: 20 characters.
- `Public Property HomeBlock() As String` [R/W] Sets or returns the block of the home address. Field name: homeBlock. Length: 100 characters.
- `Public Property HomeBuildingFloorRoom() As String` [R/W] Sets or returns additional details of the home address, such as building number, floor number, and room number. Field name: HomeBuild. Length: 64,000 characters.
- `Public Property HomeCity() As String` [R/W] Sets or returns the city of the home address. Field name: homeCity. Length: 100 characters.
- `Public Property HomeCountry() As String` [R/W] Sets or returns the country of the home address. Field name: homeCountr. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
- `Public Property HomeCounty() As String` [R/W] Sets or returns the county part of the home address. Field name: homeCounty. Length: 100 characters.
- `Public Property HomePhone() As String` [R/W] Sets or returns the home phone number. Field name: homeTel. Length: 50 characters.
- `Public Property HomeState() As String` [R/W] Sets or returns the state of the home address. Field name: homeState. Length: 3 characters. This is a foreign key to the Countries table (OCST - not exposed through the DI API).
- `Public Property HomeStreet() As String` [R/W] Sets or returns the street of the home address. Field name: homeStreet. Length: 100 characters.
- `Public Property HomeStreetNumber() As String` [R/W] property HomeStreetNumber
- `Public Property HomeZipCode() As String` [R/W] Sets or returns the zip code of the home address. Field name: homeZip. Length: 20 characters.
- `Public Property IdNumber() As String` [R/W] Sets or returns the personal ID number of the employee (such as, government ID number or social security number). Field name: govID. Length: 20 characters.
- `Public Property IDType() As String` [R/W] property IDType
- `Public Property IncomeTaxLiability() As String` [R/W] Indicate the income tax liability code: 1 - Unlimited 2 - Restricted 3 - Flat-rate tax 4 - Not liable Field: InTaxLiabi.
- `Public Property JobTitle() As String` [R/W] Sets or returns the employee job title. Field name: jobTitle. Length: 20 characters.
- `Public Property JobTitleCode() As String` [R/W] The job title of the employee. Field name: JTCode. Length: 5 characters.
- `Public Property LastName() As String` [R/W] Sets or returns the employee last name. Field name: lastName. Mandatory property. Length: 50 characters.
- `Public Property LegalRepresentative() As BoYesNoEnum` [R/W] property LegalRepresentative
- `Public Property LinkedVendor() As String` [R/W] property LinkedVendor
- `Public Property Manager() As Long` [R/W] Sets or returns the manager's employee-ID of the employee. Field name: manager. This is a key to the OHEM object.
- `Public Property MartialStatus() As BoMeritalStatuses` [R/W] Sets or returns a valid value of BoMeritalStatuses type that specifies the merital status. Field name: martStatus.
- `Public Property MiddleName() As String` [R/W] Sets or returns the employee middle name. Field name: middleName. Length: 50 characters.
- `Public Property MobilePhone() As String` [R/W] Sets or returns the mobile phone number. Field name: mobile. Length: 50 characters.
- `Public Property MunicipalityKey() As String` [R/W] The key of the municipality to which the employee belongs. Field name: MunKey. Length: 20 characters.
- `Public Property NumOfChildren() As Long` [R/W] Sets or returns the number of children. Field name: nChildren.
- `Public Property OfficeExtension() As String` [R/W] Sets or returns the extension of the office phone number. Field name: officeExt. Length: 50 characters.
- `Public Property OfficePhone() As String` [R/W] Sets or returns the office phone number. Field name: officeTel. Length: 50 characters.
- `Public Property Pager() As String` [R/W] Sets or returns the pager number. Field name: pager. Length: 50 characters.
- `Public Property PartnerReligion() As String` [R/W] Indicates the religion of the employee's spouse. -- - No church tax liability AK - Old catholic EV - Protestant FA - Non-denomination Alzey FB - Non-denominational regional congregation Baden FG - Non-denominational regional congregation Palatinate FM - Non-denominational congregation Mainz FR - French-reformed FS - Non-denominational congregation Offenbach/Mainz IB - Israelite Religious Community Baden IL - Israelite Rural IS - Israelite IW - Israelite religious community Wuerttemberg JD - Jewish religion tax JH - Jewish religion tax JS - Jewish religion tax LT - Lutheran RF - Reformed RK - Roman catholic Field: RelPartner.
- `Public Property PassportExpirationDate() As Date` [R/W] Sets or returns the expiration date of the passport. Field name: passportEx.
- `Public Property PassportIssueDate() As Date` [R/W] property PassportIssueDate
- `Public Property PassportIssuer() As String` [R/W] property PassportIssuer
- `Public Property PassportNumber() As String` [R/W] Sets or returns the employee passport number. Field name: passportNo. Length: 20 characters.
- `Public Property PaymentMethod() As EmployeePaymentMethodEnum` [R/W] The payment method of the employee. Field name: PymMeth.
- `Public Property PersonGroup() As String` [R/W] The person group of the employee. 101 - Social insurance obliged without characteristic 102 - Apprentice 104 - Home worker 105 - Trainee 106 - Student 108 - Early retirement 109 - Part time occupied employee 110 - Short time occupied 112 - Family related person agriculture 113 - Additio. income agriculture 114 - Additio. income agriculture seasonal 116 - Receiver of clearing cash 118 - Unregular occupied 119 - Pensioner 997 - Not specified Field: PersGroup.
- `Public Property Picture() As String` [R/W] Sets or returns the picture file name (without the path). Field name: picture. Length: 200 characters.
  - remarks: All picture files must be stored in the /Bitmaps sub-directory of SAP Business One. The following are supported formats: JPG, BMP, PNG, PCX.
- `Public Property Position() As Long` [R/W] Sets or returns a value that specifies the employee position. This property This is a foreign key to OHPS table, which is not exposed through the DI API. Field name: Position.
- `Public Property PreviousEmpoymentInfo() As EmployeePrevEmpoymentInfo` [R] Returns the EmployeePrevEmpoymentInfo object.
- `Public Property PreviousPRWebAccess() As BoYesNoEnum` [R] property PreviousPRWebAccess
- `Public Property ProfessionStatus() As String` [R/W] The profession of the employee. 0 - Trainee 1 - Worker 2 - Skilled Worker 3 - Supervisor/Foreman 4 - Clerk 5 - Youthhelp/Sheltered Workshop 6 - Participation for profession focused measures 7 - Homeworker 8 - Part time < 18 hrs 9 - Part time > 18 hrs Field: StatusOfP.
- `Public Property PRWebAccess() As BoYesNoEnum` [R/W] property PRWebAccess
- `Public Property QualificationCode() As SPEDContabilQualificationCodeEnum` [R/W] property QualificationCode
- `Public Property Religion() As String` [R/W] Indicates the religion of the employee. -- - No church tax liability AK - Old catholic EV - Protestant FA - Non-denomination Alzey FB - Non-denominational regional congregation Baden FG - Non-denominational regional congregation Palatinate FM - Non-denominational congregation Mainz FR - French-reformed FS - Non-denominational congregation Offenbach/Mainz IB - Israelite Religious Community Baden IL - Israelite Rural IS - Israelite IW - Israelite religious community Wuerttemberg JD - Jewish religion tax JH - Jewish religion tax JS - Jewish religion tax LT - Lutheran RF - Reformed RK - Roman catholic Field: EmTaxCCode.
- `Public Property Remarks() As String` [R/W] Sets or returns a memo type string that specifies remarks on the employee. Field name: remark. Length: 64,000 characters.
- `Public Property ReviewsInfo() As EmployeeReviewsInfo` [R] Returns the EmployeeReviewsInfo object.
- `Public Property Salary() As Double` [R/W] Sets or returns the employee salary. Field name: salary.
- `Public Property SalaryCurrency() As String` [R/W] Sets or returns the currency of the salary. Field name: salaryCurr. Length: 3 characters.
- `Public Property SalaryUnit() As BoSalaryCostUnits` [R/W] Sets or returns a valid value of BoSalaryCostUnits type that specifies the salary unit (for example: per hour, per day, per month, and so on). Field name: salaryUnit.
- `Public Property SalesPersonCode() As Long` [R/W] Sets or returns the sales person code. Field name: salesPrson. This is a foreign key to the SalesPersons Object.
  - remarks: The sales employees can be defined through the SalesPersons object (see SalesEmployeeCode).
- `Public Property SavingsPaymentInfo() As EmployeeSavingsPaymentInfo` [R] Returns the EmployeeSavingsPaymentInfo child object.
- `Public Property SocialInsuranceNumber() As String` [R/W] The social insurance number of the employee. Field name: SInsurNum. Length: 20 characters.
- `Public Property SpouseFirstName() As String` [R/W] The first name of the employee's spouse. Field name: FNameSP. Length: 50 characters.
- `Public Property SpouseSurname() As String` [R/W] The surname of the employee's spouse. Field name: SurnameSP. Length: 50 characters.
- `Public Property StartDate() As Date` [R/W] Sets or returns the date when the employee started the work in the company. Field name: startDate.
- `Public Property StatusCode() As Long` [R/W] Sets or returns the employee status code. Field name: status.
- `Public Property STDCode() As Long` [R/W] property STDCode
- `Public Property TaxClass() As String` [R/W] Indicates the tax class of the employee: 1 - Tax Class I 2 - Tax Class II 3 - Tax Class III 4 - Tax Class IV 5 - Tax Class V 6 - Tax Class VI Field name: TaxClass.
- `Public Property TaxOfficeName() As String` [R/W] The tax office name of the employee. Field name: TaxOName. Length: 50 characters.
- `Public Property TaxOfficeNumber() As String` [R/W] The tax office number of the employee. Field name: TaxONum. Length: 20 characters.
- `Public Property TerminationDate() As Date` [R/W] Sets or returns the date when the employee terminated the work in the company. Field name: termDate.
- `Public Property TreminationReason() As Long` [R/W] Sets or returns the termination reason. Field name: termReason. This is a foreign key to the Termination Reason table (OHTR - not exposed through the DI API).
- `Public Property UpdateDate() As Date` [R] property UpdateDate
- `Public Property UpdateTime() As Date` [R] property UpdateTime
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VacationCurrentYear() As Long` [R/W] The employee's vacation information of the current year. Field name: VacCurYear. Length: 3 characters.
- `Public Property VacationPreviousYear() As Long` [R/W] The employee's vacation information of the previous year. Field name: VacPreYear. Length: 3 characters.
- `Public Property WorkBlock() As String` [R/W] Sets or returns the block of the workplace address. Field name: workBlock. Length: 100 characters.
- `Public Property WorkBuildingFloorRoom() As String` [R/W] Sets or returns additional details of the workplace address, such as building number, floor number, and room number. Field name: WorkBuild. Length: 64,000 characters.
- `Public Property WorkCity() As String` [R/W] Sets or returns the city of the workplace address. Field name: workCity. Length: 100 characters.
- `Public Property WorkCountryCode() As String` [R/W] Sets or returns the country of the workplace address. Field name: workCountr. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
- `Public Property WorkCounty() As String` [R/W] Sets or returns the county of the workplace address. Field name: workCounty. Length: 100 characters.
- `Public Property WorkStateCode() As String` [R/W] Sets or returns the state of the workplace address. Field name: workState. Length: 3 characters. This is a foreign key to the States table (OCST - not exposed through the DI API).
- `Public Property WorkStreet() As String` [R/W] Sets or returns the street of the workplace address. Field name: workStreet. Length: 100 characters.
- `Public Property WorkStreetNumber() As String` [R/W] property WorkStreetNumber
- `Public Property WorkZipCode() As String` [R/W] Sets or returns the zip code of the workplace address. Field name: workZip. Length: 20 characters.

## Methods (8)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal EmployeeID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `EmployeeID`: Specifies the employee ID in the database.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# EmployeeStatus (Object)

EmployeeStatus Class

## Properties (3)
- `Public Property Description() As String` [R/W] property Description
- `Public Property Name() As String` [R/W] property Name
- `Public Property StatusId() As Long` [R] property StatusId

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EmployeeStatusParams (Object)

EmployeeStatusParams Class

## Properties (3)
- `Public Property Description() As String` [R] property Description
- `Public Property Name() As String` [R] property Name
- `Public Property StatusId() As Long` [R/W] property StatusId

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EmployeeStatusParamsCollection (Collection)

EmployeeStatusParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As EmployeeStatusParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As EmployeeStatusParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EmployeeStatusService (Object)

EmployeeStatusService Class

## Methods (8)
- `Public Function Add(ByVal pIEmployeeStatus As EmployeeStatus) As EmployeeStatusParams` Add
  - param `pIEmployeeStatus`: 
- `Public Sub Delete(ByVal pIEmployeeStatusParams As EmployeeStatusParams)` Delete
  - param `pIEmployeeStatusParams`: 
- `Public Function Get(ByVal pIEmployeeStatusParams As EmployeeStatusParams) As EmployeeStatus` Get
  - param `pIEmployeeStatusParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As EmployeeStatusServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `EmployeeStatusServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As EmployeeStatusParamsCollection` GetList
- `Public Sub Update(ByVal pIEmployeeStatus As EmployeeStatus)` Update
  - param `pIEmployeeStatus`: 

# EmployeeTransfer (Object)

Represents the employee transfer record to the payroll provider. Source table: OHET.

## Properties (8)
- `Public Property Comment() As String` [R/W] Any comment. For example, B1iSN would report error details here. Field name: Comment.
- `Public Property EmployeeTransferDetails() As EmployeeTransferDetails` [R] Returns the EmployeeTransferDetails object.
- `Public Property Status() As EmployeeTransferStatusEnum` [R/W] The status of the employee transfer. When you add a new transfer, SAP Business One sets the status to New. B1iSN updates the status during the processing. Field name: Status.
- `Public Property TransEndDate() As Date` [R/W] Represents the date on which the data was sent or exported successfully. Field name: TransEnd.
- `Public Property TransEndTime() As Date` [R/W] Represents the time at which the data was sent or exported successfully. Field name: EndTime.
- `Public Property TransferID() As Long` [R/W] The unique ID of the transfer process; unique per company DB. Field name: TransferID. Length: 11 characters.
- `Public Property TransStartDate() As Date` [R/W] Represents the transfer start date. Field name: TransStart.
- `Public Property TransStartTime() As Date` [R/W] Represents the transfer start time. Field name: StartTime.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# EmployeeTransferDetail (Object)

EmployeeTransferDetail is a child object of the EmployeeTransfer object. Represents the sub-record of an employee transfer to the payroll provider. Source table: HET1.

## Properties (6)
- `Public Property Comment() As String` [R/W] Any comment. For example, B1iSN would report error details here. Field name: Comment.
- `Public Property EmployeeID() As Long` [R/W] This is a foreign key to the EmployeesInfo object. Field name: empID.
- `Public Property Status() As EmployeeTransferProcessingStatusEnum` [R/W] The status of the employee transfer processing. When you add a new transfer, SAP Business One sets the status to New. B1iSN updates the status during the processing. Field name: Status.
- `Public Property TransferedDate() As Date` [R/W] Represents the date that the data have been sent or exported successfully. Field name: Transfered.
- `Public Property TransferedTime() As Date` [R/W] Represents the time that the data have been sent or exported successfully. Field name: TransTime.
- `Public Property TransferID() As Long` [R] This is a foreign key to the EmployeeTransfer object. Field name: TransferID.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# EmployeeTransferDetails (Collection)

A collection of EmployeeTransferDetail objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As EmployeeTransferDetail` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As EmployeeTransferDetail` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# EmployeeTransferParams (Object)

Holds the key of an employee transfer. This object is used to pass keys to and retrieve keys from EmployeeTransfersService methods. Source table: OHET.

## Properties (1)
- `Public Property TransferID() As Long` [R/W] The key for a specific employee transfer. Field name: TransferID.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# EmployeeTransfersParams (Collection)

A collection of EmployeeTransferParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As EmployeeTransferParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As EmployeeTransferParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# EmployeeTransfersService (Object)

EmployeeTransfersService is a business object that manages employee master data transfers from SAP Business One to the DATEV HR client application. Source table: OHET.

**Remarks:** To transfer employee information from SAP Business One: - Choose Human Resources --> Human Resources Reports --> Employee List. - Select the desired employee from the list. - Choose the Transfer button.

## Methods (8)
- `Public Function AddEmployeeTransfer(ByVal pIEmployeeTransfer As EmployeeTransfer) As EmployeeTransferParams` Adds an employee transfer.
  - param `pIEmployeeTransfer`: The data for the new employee transfer.
  - returns: Contains the key of the new employee transfer.
  - C# example (from SAP's help):
    ```csharp
    EmployeeTransfersService oTrans = (EmployeeTransfersService)oCompany.GetCompanyService().GetBusinessService(ServiceTypes.EmployeeTransfersService);
    EmployeeTransfer oTransfer = (EmployeeTransfer) oTrans.GetDataInterface(EmployeeTransfersServiceDataInterfaces.etsEmployeeTransfer);

    oTransfer.TransStartDate = DateTime.Today;
    oTransfer.TransStartTime = DateTime.Now;
    oTransfer.TransEndDate = DateTime.Today;
    oTransfer.TransEndTime = DateTime.Now;

    oTransfer.Status = EmployeeTransferStatusEnum.ets_New;

    oTransfer.EmployeeTransferDetails.Add();
    oTransfer.EmployeeTransferDetails.Item(0).EmployeeID = 1;
    oTransfer.EmployeeTransferDetails.Item(0).TransferedDate = DateTime.Today;
    oTransfer.EmployeeTransferDetails.Item(0).TransferedTime = DateTime.Now;
    oTransfer.EmployeeTransferDetails.Item(0).Status = EmployeeTransferProcessingStatusEnum.etps_New;

    oTransfer.EmployeeTransferDetails.Add();
    oTransfer.EmployeeTransferDetails.Item(1).EmployeeID = 2;
    oTransfer.EmployeeTransferDetails.Item(1).TransferedDate = DateTime.Today;
    oTransfer.EmployeeTransferDetails.Item(1).TransferedTime = DateTime.Now;
    oTransfer.EmployeeTransferDetails.Item(1).Status = EmployeeTransferProcessingStatusEnum.etps_New;

    oTrans.AddEmployeeTransfer(oTransfer);
    ```
- `Public Sub DeleteEmployeeTransfer(ByVal pIEmployeeTransferParams As EmployeeTransferParams)` Deletes an existing employee transfer.
  - param `pIEmployeeTransferParams`: The key of the employee transfer to be deleted.
- `Public Function GetDataInterface(ByVal enumMSDI As EmployeeTransfersServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default settings/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `EmployeeTransfersServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates a data structure from a specified XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates a data structure from a specified XML string.
  - param `bstrXMLString`: Specifies the XML String.
- `Public Function GetEmployeeTransfer(ByVal pIEmployeeTransferParams As EmployeeTransferParams) As EmployeeTransfer` Retrieves an employee transfer.
  - param `pIEmployeeTransferParams`: The key of the employee transfer to retrieve.
  - returns: The employee transfer with the specified key.
- `Public Function GetEmployeeTransferList() As EmployeeTransfersParams` Retrieves the list of employee transfers.
- `Public Sub UpdateEmployeeTransfer(ByVal pIEmployeeTransfer As EmployeeTransfer)` Updates an existing employee transfer.
  - param `pIEmployeeTransfer`: The data for the employee transfer to be updated.
  - C# example (from SAP's help):
    ```csharp
    EmployeeTransfersService oTrans = (EmployeeTransfersService)oCompany.GetCompanyService().GetBusinessService(ServiceTypes.EmployeeTransfersService);
    EmployeeTransferParams oTransParams = (EmployeeTransferParams)oTrans.GetDataInterface(EmployeeTransfersServiceDataInterfaces.etsEmployeeTransferParams);

    oTransParams.TransferID = 1;

    EmployeeTransfer oTransfer = oTrans.GetEmployeeTransfer(oTransParams);

    oTransfer.TransEndDate = DateTime.Today;
    oTransfer.TransEndTime = DateTime.Now;
    oTransfer.Status = EmployeeTransferStatusEnum.ets_Sent;

    oTransfer.EmployeeTransferDetails.Item(0).TransferedDate = DateTime.Today;
    oTransfer.EmployeeTransferDetails.Item(0).TransferedTime = DateTime.Now;
    oTransfer.EmployeeTransferDetails.Item(0).Status = EmployeeTransferProcessingStatusEnum.etps_Sent;

    oTransfer.EmployeeTransferDetails.Item(1).TransferedDate = DateTime.Today;
    oTransfer.EmployeeTransferDetails.Item(1).TransferedTime = DateTime.Now;
    oTransfer.EmployeeTransferDetails.Item(1).Status = EmployeeTransferProcessingStatusEnum.etps_Sent;

    oTrans.UpdateEmployeeTransfer(oTransfer);
    ```

# EmploymentCategory (Object)

Source table: OETC.

## Properties (2)
- `Public Property Code() As String` [R/W] Employment category code. Field name: EmptCtCod. Length: 3 characters.
- `Public Property Description() As String` [R/W] Employment category description. Field name: EmptCtDes. Length: 100 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# EmploymentCategoryParams (Object)

EmploymentCategoryParams Class

## Properties (1)
- `Public Property Code() As String` [R/W] Employment category code. Field name: EmptCtCod. Length: 3 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# EmploymentCategoryService (Object)

Source table: OETC.

**Remarks:** For the Italy localization only. Navigation path: Business Partner Master Data → Accounting → Tax, select the checkbox Subject to Withholding Tax and go to the field Employment Category.

## Methods (7)
- `Public Function AddEmploymentCategory(ByVal pIEmploymentCategory As EmploymentCategory) As EmploymentCategoryParams` AddEmploymentCategory
  - param `pIEmploymentCategory`: 
- `Public Function GetDataInterface(ByVal enumMSDI As EmploymentCategoryServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `EmploymentCategoryServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetEmploymentCategory(ByVal pIEmploymentCategoryParams As EmploymentCategoryParams) As EmploymentCategory` GetEmploymentCategory
  - param `pIEmploymentCategoryParams`: 
- `Public Function GetEmploymentCategoryList() As EmploymentCategorysParams` GetEmploymentCategoryList
- `Public Sub UpdateEmploymentCategory(ByVal pIEmploymentCategory As EmploymentCategory)` UpdateEmploymentCategory
  - param `pIEmploymentCategory`: 

# EmploymentCategorysParams (Collection)

EmploymentCategorysParams Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As EmploymentCategoryParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As EmploymentCategoryParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# EnhancedDiscountGroup (Object)

EnhancedDiscountGroup Class

## Properties (8)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property Active() As BoYesNoEnum` [R/W] property Active
- `Public Property DiscountGroupLineCollection() As DiscountGroupLineCollection` [R] property DiscountGroupLineCollection
- `Public Property DiscountRelations() As DiscountGroupRelationsEnum` [R/W] property DiscountRelations
- `Public Property ObjectCode() As String` [R/W] property ObjectCode
- `Public Property Type() As DiscountGroupTypeEnum` [R/W] property Type
- `Public Property ValidFrom() As Date` [R/W] property ValidFrom
- `Public Property ValidTo() As Date` [R/W] property ValidTo

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EnhancedDiscountGroupCollectionParams (Collection)

EnhancedDiscountGroupCollectionParams Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As EnhancedDiscountGroupParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As EnhancedDiscountGroupParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EnhancedDiscountGroupParams (Object)

EnhancedDiscountGroupParams Class

## Properties (3)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property ObjectCode() As String` [R] property ObjectCode
- `Public Property Type() As DiscountGroupTypeEnum` [R] property Type

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EnhancedDiscountGroupsService (Object)

EnhancedDiscountGroupsService Class

## Methods (8)
- `Public Function Add(ByVal pIEnhancedDiscountGroup As EnhancedDiscountGroup) As EnhancedDiscountGroupParams` Add
  - param `pIEnhancedDiscountGroup`: 
- `Public Sub Delete(ByVal pIEnhancedDiscountGroupParams As EnhancedDiscountGroupParams)` Delete
  - param `pIEnhancedDiscountGroupParams`: 
- `Public Function Get(ByVal pIEnhancedDiscountGroupParams As EnhancedDiscountGroupParams) As EnhancedDiscountGroup` Get
  - param `pIEnhancedDiscountGroupParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As EnhancedDiscountGroupsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `EnhancedDiscountGroupsServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As EnhancedDiscountGroupCollectionParams` GetList
- `Public Sub Update(ByVal pIEnhancedDiscountGroup As EnhancedDiscountGroup)` Update
  - param `pIEnhancedDiscountGroup`: 

# EWBTransporter (Object)

EWBTransporter Class

## Properties (5)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property EWBTransporter_Lines() As EWBTransporter_Lines` [R] property EWBTransporter_Lines
- `Public Property TransporterCode() As String` [R/W] property TransporterCode
- `Public Property TransporterID() As String` [R/W] property TransporterID
- `Public Property TransporterName() As String` [R/W] property TransporterName

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EWBTransporter_Line (Object)

EWBTransporter_Line Class

## Properties (5)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property Mode() As Long` [R/W] property Mode
- `Public Property VehicleNo() As String` [R/W] property VehicleNo
- `Public Property VehicleType() As String` [R/W] property VehicleType

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EWBTransporter_Lines (Collection)

EWBTransporter_Lines Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As EWBTransporter_Line` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As EWBTransporter_Line` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` method Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EWBTransporterParams (Object)

EWBTransporterParams Class

## Properties (4)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property TransporterCode() As String` [R] property TransporterCode
- `Public Property TransporterID() As String` [R] property TransporterID
- `Public Property TransporterName() As String` [R] property TransporterName

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EWBTransporterParamsCollection (Collection)

EWBTransporterParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As EWBTransporterParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As EWBTransporterParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# EWBTransporterService (Object)

EWBTransporterService Class

## Methods (8)
- `Public Function AddTransporter(ByVal pIEWBTransporter As EWBTransporter) As EWBTransporterParams` AddTransporter
  - param `pIEWBTransporter`: 
- `Public Sub DeleteTransporter(ByVal pIEWBTransporterParams As EWBTransporterParams)` DeleteTransporter
  - param `pIEWBTransporterParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As EWBTransporterServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `EWBTransporterServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetEWBTransporterList() As EWBTransporterParamsCollection` GetEWBTransporterList
- `Public Function GetTransporter(ByVal pIEWBTransporterParams As EWBTransporterParams) As EWBTransporter` GetTransporter
  - param `pIEWBTransporterParams`: 
- `Public Sub UpdateTransporter(ByVal pIEWBTransporter As EWBTransporter)` UpdateTransporter
  - param `pIEWBTransporter`: 

# ExceptionalEvent (Object)

Source table: OEPE.

## Properties (2)
- `Public Property Code() As String` [R/W] Exceptional event code. Field name: Code. Length: 2 characters.
- `Public Property Description() As String` [R/W] Exceptional event description. Field name: Name. Length: 100 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ExceptionalEventParams (Object)

ExceptionalEventParams Class

## Properties (1)
- `Public Property Code() As String` [R/W] Exceptional event code. Field name: Code. Length: 2 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ExceptionalEventService (Object)

Source table: OEPE.

**Remarks:** For the Italy localization only. Navigation path: Business Partner Master Data → Accounting → Tax, select the checkbox Subject to Withholding Tax and go to the field Exceptional Event.

## Methods (8)
- `Public Function AddExceptionalEvent(ByVal pIExceptionalEvent As ExceptionalEvent) As ExceptionalEventParams` AddExceptionalEvent
  - param `pIExceptionalEvent`: 
- `Public Sub DeleteExceptionalEvent(ByVal pIExceptionalEventParams As ExceptionalEventParams)` DeleteExceptionalEvent
  - param `pIExceptionalEventParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ExceptionalEventServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ExceptionalEventServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetExceptionalEvent(ByVal pIExceptionalEventParams As ExceptionalEventParams) As ExceptionalEvent` GetExceptionalEvent
  - param `pIExceptionalEventParams`: 
- `Public Function GetExceptionalEventList() As ExceptionalEventsParams` GetExceptionalEventList
- `Public Sub UpdateExceptionalEvent(ByVal pIExceptionalEvent As ExceptionalEvent)` UpdateExceptionalEvent
  - param `pIExceptionalEvent`: 

# ExceptionalEventsParams (Collection)

ExceptionalEventsParams Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ExceptionalEventParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ExceptionalEventParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ExpenseTypeData (Object)

ExpenseTypeData Class

## Properties (5)
- `Public Property ExpenseAccount() As String` [R/W] property ExpenseAccount
- `Public Property ExpenseName() As String` [R/W] property ExpenseName
- `Public Property ExpenseType() As String` [R/W] property ExpenseType
- `Public Property PaidByCompany() As BoYesNoEnum` [R/W] property PaidByCompany
- `Public Property VatGroup() As String` [R/W] property VatGroup

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ExpenseTypeParams (Object)

ExpenseTypeParams Class

## Properties (1)
- `Public Property ExpenseType() As String` [R/W] property ExpenseType

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ExpenseTypeService (Object)

ExpenseTypeService Class

## Methods (6)
- `Public Function Add(ByVal pIExpenseTypeData As ExpenseTypeData) As ExpenseTypeParams` Add
  - param `pIExpenseTypeData`: 
- `Public Function Get(ByVal pIExpenseTypeParams As ExpenseTypeParams) As ExpenseTypeData` Get
  - param `pIExpenseTypeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ExpenseTypeServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ExpenseTypeServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Sub Update(ByVal pIExpenseTypeData As ExpenseTypeData)` Update
  - param `pIExpenseTypeData`: 

# ExportDetermination (Object)

ExportDetermination Class

## Properties (10)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property BusinessPartner() As String` [R/W] property BusinessPartner
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R/W] property Code
- `Public Property Country() As String` [R/W] property Country
- `Public Property DocumentSubType() As String` [R/W] property DocumentSubType
- `Public Property DocumentType() As String` [R/W] property DocumentType
- `Public Property ExportFormat() As Long` [R/W] property ExportFormat
- `Public Property PathFileName() As String` [R/W] property PathFileName
- `Public Property Priority() As Long` [R/W] property Priority
- `Public Property Series() As Long` [R/W] property Series

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ExportDeterminationParams (Object)

ExportDeterminationParams Class

## Properties (7)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property BusinessPartner() As String` [R/W] property BusinessPartner
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R/W] property Code
- `Public Property Country() As String` [R/W] property Country
- `Public Property DocumentSubType() As String` [R/W] property DocumentSubType
- `Public Property DocumentType() As String` [R/W] property DocumentType
- `Public Property Series() As Long` [R/W] property Series

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ExportDeterminationsCollection (Collection)

ExportDeterminationsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As ExportDetermination` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As ExportDetermination` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

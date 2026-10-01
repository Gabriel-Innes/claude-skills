<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AlertManagement (Object)

AlertManagement is Data structure related to the AlertManagementService. Source table: OALT.

## Properties (19)
- `Public Property Active() As BoYesNoEnum` [R/W] Sets or returns valid value that determines whether or not this is Active Alert. Field name: Active.
- `Public Property AlertManagementDocuments() As AlertManagementDocuments` [R] Returns the AlertManagementDocuments object, a DataCollection that defines the Collection of documents attached to this alert.
- `Public Property AlertManagementRecipients() As AlertManagementRecipients` [R] Returns the AlertManagementRecipients object, a DataCollection that defines the Collection of recipients attached to this alert.
- `Public Property Code() As Long` [R] Returns the internal number of this alert. Field name: Code.
- `Public Property DayOfExecution() As Long` [R/W] Sets or Returns the number of days remains until the day of execution of this alert. Field name: ExecDaY.
- `Public Property ExecutionTime() As Date` [R/W] Returns the time remaining until the execution hour of this alert. Field name: ExecTime.
- `Public Property FrequencyInterval() As Long` [R/W] Returns the time unit used to define the cycle Frequency of this alert. Field name: FrqncyIntr.
- `Public Property FrequencyType() As AlertManagementFrequencyType` [R/W] Sets or returns a valid value that determines this allert frequency type. Field name: FrqncyType.
- `Public Property LastExecutionDate() As Date` [R] Returns the last Execution Date of this alert. Field name: LastDate.
- `Public Property LastExecutionTime() As Long` [R] Returns the last Execution Time of this alert. Field name: LastTIME.
- `Public Property Name() As String` [R/W] Sets or returns the Name of this Alert. Field name: Name.
- `Public Property NextExecutionDate() As Date` [R] Returns the Next Date this alert will be activated. Field name: NextDate.
- `Public Property NextExecutionTime() As Date` [R] Returns the next time this alert will be activated. Field name: NextTime.
- `Public Property Param() As String` [R/W] Sets or returns the Parameters that define this Alert. Field name: Params.
- `Public Property Priority() As AlertManagementPriorityEnum` [R/W] Sets or returns valid value for this alert Priority. Field name: Priority.
- `Public Property QueryID() As Long` [R/W] Sets or returns this query Id. Field name: QueryId.
- `Public Property SaveHistory() As BoYesNoEnum` [R/W] Determines whether or not to save history for this Alert. Field name: History.
- `Public Property Type() As AlertManagementTypeEnum` [R] Sets or returns valid value that determines whether this alert is System Alert or User Alert. Field name: Type.
- `Public Property UserFields() As Fields` [R] Get User Fields

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Exports data from the object to an XML string.

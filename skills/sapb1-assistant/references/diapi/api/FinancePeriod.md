<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# FinancePeriod (Object)

The FinancePeriod object is a data structure related to the CompanyService. The object is used to identify and define a new Finance Period. Source table: OFPR.

## Properties (15)
- `Public Property AbsoluteEntry() As Long` [R] Sets or return the key of the period category as assigned by the system when creating a new period category. Field name: AbsEntry.
- `Public Property ActiveforFeed() As BoYesNoEnum` [R/W] Determines whether or not to enable adding documents to the finance period. However, a journal entries can be added. Field name: Free2. Use the property PeriodStatus instead of ActiveforFeed.
- `Public Property AdditionalSubPeriods() As BoYesNoEnum` [R] Determines whether or not additional sub periods exists. Field name: Addition.
- `Public Property Locked() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not to lock the Finance Period for additional journal entries. Field name: Free3. Use the property PeriodStatus instead of Locked.
- `Public Property PeriodCode() As String` [R/W] Sets or returns the Period Code. Field name: Code. Length: 20 characters.
- `Public Property PeriodIndicator() As String` [R/W] Sets or returns the PeriodIndicator, a foreign key to OPID. Field name: Indicator). Length: 10 characters.
- `Public Property PeriodName() As String` [R/W] Sets or returns the Period Name. Field name: Name. Length: 20 characters.
- `Public Property PeriodStatus() As PeriodStatusEnum` [R/W] Sets or returns a valid value that specifies the finance period status. Each status indicates what transactions and documents can be posted within the date range of each posting period. Field name: PeriodStat)
- `Public Property PostingDateFrom() As Date` [R/W] Sets or returns the Posting Period initiation date. Field name: F_RefDate.
- `Public Property PostingDateTo() As Date` [R/W] Sets or returns the Posting Period termination date. Field name: T_RefDate.
- `Public Property SubNum() As Long` [R] Returns the No. of Additional Sub-Period contained within the period. Field name: SubNum.
- `Public Property TaxDateFrom() As Date` [R/W] Sets or returns the starting date for Tax calculation. Field name: F_TaxDate.
- `Public Property TaxDateTo() As Date` [R/W] Sets or returns the ending date for Tax calculation. Field name: T_TaxDate.
- `Public Property ValueDateFrom() As Date` [R/W] Sets or returns the starting date for value calculation. Field name: F_DueDate.
- `Public Property ValueDateTo() As Date` [R/W] Sets or returns the ending date for value calculation. Field name: T_DueDate.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

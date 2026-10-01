<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Series (Object)

Series is a data structure related to the SeriesService. It represents the series object, a part of a document name. Source table: NNM1 (Documents Numbering - Series).

## Properties (27)
- `Public Property ATDocumentType() As String` [R/W] property ATDocumentType
- `Public Property BPLID() As Long` [R/W] property BPLID
- `Public Property CostAccountOnly() As BoYesNoEnum` [R/W] property CostAccountOnly
- `Public Property DigitNumber() As Long` [R/W] property DigitNumber
- `Public Property Document() As String` [R/W] Sets or returns Document name. Field name: ObjectCode. Length: 20 characters.
- `Public Property DocumentSubType() As String` [R/W] Sets or returns the document sub-type, part of the document name. Field name: DocSubType.
- `Public Property GroupCode() As BoSeriesGroupEnum` [R/W] Sets or returns a Group Code for current series. Field name: GroupCode.
- `Public Property InitialNumber() As Long` [R/W] Sets or returns Initial Number of current Series. Field name: InitialNum.
- `Public Property InvoiceType() As Long` [R/W] property InvoiceType
- `Public Property InvoiceTypeOfNegativeInvoice() As Long` [R/W] property InvoiceTypeOfNegativeInvoice
- `Public Property IsDigitalSeries() As BoYesNoEnum` [R/W] property IsDigitalSeries
- `Public Property IsElectronicCommEnabled() As BoYesNoEnum` [R/W] property IsElectronicCommEnabled
- `Public Property IsManual() As BoYesNoEnum` [R] property IsManual
- `Public Property LastNumber() As Long` [R/W] Sets or returns the last number allowed for current Series. Field name: LastNum.
- `Public Property Locked() As BoYesNoEnum` [R/W] Determines whether or not the current series is locked. Field name: Locked.
- `Public Property Name() As String` [R/W] Sets or returns current Series name. Field name: SeriesName. Length:8 characters.
- `Public Property NextNumber() As Long` [R/W] Sets or returns the next number to be used from current series. Field name: NextNumber.
- `Public Property PeriodIndicator() As String` [R/W] Sets or returns the period indicator. Field name: Indicator. This is a foreign key to the Period Indicators table OPID, which is not exposed through the DI API. Length: 10 characters.
- `Public Property PortugalSeriesAction() As String` [R/W] Field name: Action. Length: 1 Characters. R - Report C - Cancel F - Finalize
- `Public Property PortugalSeriesPhase() As String` [R] Field name: Phase. Length: 1 Characters. T - To Be Processed I - In Process O - OK E - Error
- `Public Property PortugalSeriesStatus() As String` [R] Field name: Status. Length: 1 Characters. R - Reported C - Canceled F - Finalized
- `Public Property Prefix() As String` [R/W] Sets or returns the folio prefix string of this series. Field name: BeginStr. Length: 2 Characters.
- `Public Property Remarks() As String` [R/W] Sets or returns remarks regarding current series. Field name: Remark. Length: 50 Characters.
- `Public Property Series() As Long` [R] Returns current Series value. Field name: Series.
- `Public Property SeriesType() As BoSeriesTypeEnum` [R/W] property SeriesType
- `Public Property Suffix() As String` [R/W] Sets or returns the suffix string of this series. Field name: EndStr. Length: 8 Characters.
- `Public Property UserFields() As Fields` [R] Get User Fields

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DefaultReportParams (Object)

Specifies the default report layout for a document type. The default report layout can be designated for a specific user and business partner, or for all users and business partners. Use this object with the GetDefaultReport/SetDefaultReport methods of the ReportLayoutsService. Source table: RDFL

**Remarks:** To specify a default report layout in SAP Business One: - Open a marketing document form (for example, Sales A/R -- Sales Quotation). - Select Tools --> Print Layout Designer (or select the pencil icon on the toolbar). - Select a report layout. - Click Set as Default.

## Properties (4)
- `Public Property CardCode() As String` [R/W] A business partner for which the report layout is the default. If blank, the report layout is default for all business partners. Field name: CardCode Length: 15 characters This is a foreign key to the BusinessPartners object.
- `Public Property LayoutCode() As String` [R/W] The default report layout for the document type specified in the ReportCode property. Field name: DfltReport Length: 8 characters
  - remarks: This is the key of the report layout (LayoutCode property of the ReportLayout object).
- `Public Property ReportCode() As String` [R/W] The document type for which the report layout specified by the LayoutCode property is the default. Field name: DoumntDode. Length: 4 characters.
  - remarks: The Code field of the table RTYP contains valid values.
- `Public Property UserID() As Long` [R/W] A user for which the report layout is the default. If blank, the report layout is default for all users. Field name: UserId Length: 11 characters Returns the identification key of the active user who operates the system.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure. Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data. Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data. Creates an XML string that represents the object data.

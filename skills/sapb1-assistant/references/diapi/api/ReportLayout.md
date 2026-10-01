<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ReportLayout (Object)

Represents a layout for PLD or a layout/report for Crystal Reports. Source table: RDOC

**Remarks:** The ReportLayoutsService enables you to transfer PLD report layouts from one company to another. When transferring a system layout, change the following properties before adding the layout to the destination company: - Author: Change from System to a different name. If left unchanged, an exception is thrown. - Editable: Change from NO to Yes to make the new layout editable. - Name: Give the report layout a new name. When this object is used to import a layout/report for Crystal Reports, the fields Name, TypeCode, Author and Category must be set. Set Category to Crystal Reports and set TypeCode to either RCRI (for standalone reports) or a document type (for layouts).

## Properties (48)
- `Public Property AllignFooterToBottom() As BoYesNoEnum` [R/W] Determines whether or not to align layout report footer to page bottom. Field name: AlgnFooter.
- `Public Property Author() As String` [R/W] Sets or returns the name of layout report Author. Field name: Author. Length: 32 characters.
- `Public Property B1Version() As String` [R/W] The SAP Business One release number. Field name: B1Version
- `Public Property BottomMargin() As Long` [R/W] Sets or returns the size of the Bottom Margin of the layout Report. Field name: BMargin.
- `Public Property Category() As ReportLayoutCategoryEnum` [R/W] Indicates whether the report layout is a PLD or Crystal Reports layout. Field name: Category
- `Public Property ChangeFontSizeForEMail() As Long` [R/W] Sets or returns Font Size for email. Field name: EmFOffset.
- `Public Property ChangeFontSizeInPreview() As Long` [R/W] Sets or returns Font Size for layout Preview printing. Field name: ScrFOffset.
- `Public Property ConvertFontForEMail() As BoYesNoEnum` [R/W] Determines whether or not to convert font type for email. Field name: SwpInEmail.
- `Public Property ConvertFontInPrintPreview() As BoYesNoEnum` [R/W] Determines whether or not to convert font type for Print Preview. Field name: SwapOnScrn.
- `Public Property CRVersion() As String` [R/W] The Crystal Reports release number. Field name: CRVersion
- `Public Property Editable() As BoYesNoEnum` [R] Determines whether or not current report is editable. Field name: CanChange.
- `Public Property EMailFont() As String` [R/W] Sets or returns the font type currently used for email. Field name: EmailFont. Length: 50 characters.
- `Public Property ExtensionErrorAction() As BoExtensionErrorActionEnum` [R/W] Sets or returns current definition of the action to be taken upon printer extension error. Field name: ExtOnErr.
- `Public Property ExtensionName() As String` [R/W] Sets or returns current printer extension name. Field name: ExtName. Length: 16 characters.
- `Public Property FollowUpReport() As String` [R/W] Sets or returns Follow-Up Report. Field name: FollowCode.
- `Public Property ForeignLanguageReport() As BoYesNoEnum` [R/W] Determines whether or not to use Foreign Language Report. Field name: FrgnReport. FrgnReport
- `Public Property GridSize() As Long` [R/W] Sets or returns the vertical distance between two Grid points. Field name: GridSize.
- `Public Property GridType() As BoGridTypeEnum` [R/W] Sets or returns a valid value that determines the grid lines type in the reports layout: dots, or lines, or combination of dots and lines. Field name: GridType.
- `Public Property Height() As Long` [R/W] Sets or returns document hight. Field name: Height.
- `Public Property ImpExpObjCode() As Long` [R/W] Sets or returns the ImpExpObjCode value for the printer. Field name: RobjCode.
- `Public Property language() As Long` [R/W] Sets or returns the current printer language value. Field name: Language.
- `Public Property LayoutCode() As String` [R] The key of the report layout. Field name: DocCode
- `Public Property LeaderReport() As String` [R/W] Sets or returns the Leader Report value for the printer. Field name: LeaderCode. Length: 8 characters.
- `Public Property LeftMargin() As Long` [R/W] Sets or returns the LMargin value of the report layout. Field name: LMargin.
- `Public Property Localization() As String` [R/W] The localization assigned to the layout. Field name: Local
- `Public Property Name() As String` [R/W] Sets or returns the Document's Name value. Field name: DocName
- `Public Property NumberOfCopies() As Long` [R/W] The number of printed copies. Field name: NumCopy
- `Public Property Orientation() As BoOrientationEnum` [R/W] Determines the printer's orintation (Vertical or Horizontal). Field name: Oreint.
- `Public Property PaperSize() As String` [R/W] Sets or returns printer's Paper Size. Field name: PaperSize. Length: 100 characters.
- `Public Property Picture() As String` [R/W] Sets or returns a string that defines the path and name of the picture. Field name: Picture. Length: 16 characters.
- `Public Property PreviewPrintingFont() As String` [R/W] Sets or returns the name of the selected font to be Previewed upon screen. Length: 50 characters. Field name: ScreenFont.
- `Public Property Printer() As String` [R/W] The printer assigned to the layout. Field name: Printer.
- `Public Property PrinterFirstPage() As String` [R/W] The printer for the first page of a layout. Field name: Prtr1st
- `Public Property Query() As String` [R/W] Sets or returns query text. Field name: QString. Length: 16 characters.
- `Public Property QueryType() As BoQueryTypeEnum` [R/W] Sets or returns a valid value that determines wether Query type is Wizard or Regular. Length: 1 character. Field name: QType.
- `Public Property Remarks() As String` [R/W] Set or returns the the content of the remark used by the remark property of the printer. Field name: Notes. Length 254 characters.
- `Public Property RepetitiveAreasNumber() As Long` [R] Set or returns the number of Repetitive Areas property. Field name: NumRepArs.
- `Public Property ReportLayoutItems() As ReportLayoutItems` [R/W] Set or returns the ReportLayoutItems Object.
- `Public Property RightMargin() As Long` [R/W] Sets or returns the RMargin value of the report layout. Field name: RMargin.
- `Public Property ShowGrid() As BoYesNoEnum` [R/W] Determines whether to display or hide a grid in the report layout. Field name: ShowGrid.
- `Public Property SnapToGrid() As BoYesNoEnum` [R/W] Determines whether or not to use the printer grid alignment property for current report. Field name: SnapGrid.
- `Public Property Sortable() As BoYesNoEnum` [R] Determines whether or not to use the printer Sortable property for current report. Field name: CanSort.
- `Public Property TopMargin() As Long` [R/W] Sets or returns the TMargin value of the report layout. Field name: TMargin.
- `Public Property TranslationLines() As ReportLayout_TranslationLines` [R] property TranslationLines
- `Public Property TypeCode() As String` [R/W] Sets or returns the TypeCode property of the printer. Field name: TypeCode. Length 4 characters. This is a foreign key to the RTYP table.
- `Public Property TypeDetail() As String` [R/W] property TypeDetail
- `Public Property UseFirstPrinter() As BoYesNoEnum` [R/W] Indicates whether to use the first printer. Field name: Use1stPrtr
- `Public Property Width() As Long` [R/W] Sets or returns document width. Field name: TypeCode.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: Specifies the the XML file. The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: Specifies the the XML string. The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure. Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data. Creates an XML file that represents the object.
  - param `bstrFileName`: Specifies the XML file name including path. The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data. Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

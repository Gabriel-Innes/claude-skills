<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# JournalEntries (Object)

JournalEntries is a business object that represents the journal transactions in the Finance module. This object enables you to: - Add a journal transaction. - Retrieve a journal transaction by its key. - Update a journal transaction. - Remove a journal transaction. - Save the object in XML format. Source table: OJDT.

**Remarks:** To display the form in the applicationl, select Financials --> Journal Entry.

## Properties (62)
- `Public Property AdjustTransaction() As BoYesNoEnum` [R/W] property AdjustTransaction
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property AutomaticWT() As BoYesNoEnum` [R/W] Indicates whether withholding tax is calculated for this journal entry. Field name: AutoWT
- `Public Property AutoVAT() As BoYesNoEnum` [R/W] Determines whether or not to use automatic VAT calculation. Field name: AutoVAT.
- `Public Property BaseReference() As String` [R] The document number of the document that triggered the current journal entry (DocNum property of the Documents object). Field name: BaseRef
- `Public Property BlanketAgreementNumber() As Long` [R] property BlanketAgreementNumber
- `Public Property BlockDunningLetter() As BoYesNoEnum` [R/W] Indicates whether to prevent dunning letter for this journal entry. Yes means no dunning letters are generated. Field name: BlockDunn
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CertificationNumber() As String` [R] property CertificationNumber
- `Public Property Cig() As Long` [R/W] property Cig
- `Public Property Corisptivi() As BoYesNoEnum` [R/W] Indicates the journal entry is for a cash register transaction. Field name: Corisptivi
  - remarks: For Italy only.
- `Public Property Count() As Long` [R] Returns the total journal entries.
- `Public Property Cup() As Long` [R/W] property Cup
- `Public Property DeferredTax() As BoYesNoEnum` [R/W] Indicates whether to apply the deferred tax function associated with the selected tax group or tax code. Field name: DeferredTax.
- `Public Property DocumentType() As String` [R/W] property DocumentType
- `Public Property DueDate() As Date` [R/W] Sets or returns the value date of the journal entry. Field name: DueDate.
- `Public Property ECDPostingType() As ECDPostingTypeEnum` [R/W] property ECDPostingType
- `Public Property ElectronicProtocols() As ElectronicProtocols` [R] property ElectronicProtocols
- `Public Property ExcludeFromTaxReportControlStatementVAT() As BoYesNoEnum` [R/W] property ExcludeFromTaxReportControlStatementVAT
- `Public Property ExposedTransNumber() As Long` [R/W] property ExposedTransNumber
- `Public Property FolioNumber() As Long` [R] Returns the Folio number assigned to the document that initiated the journal entry. It is updated automatically after printing the document. Remains empty for journal entries that result from cancellation of documents with Folio numbers, and for manual journal entries. Country-specific for Chile and Mexico. Field name: FolioNum.
- `Public Property FolioNumberFrom() As Long` [R] property FolioNumberFrom
- `Public Property FolioNumberTo() As Long` [R] property FolioNumberTo
- `Public Property FolioPrefixString() As String` [R] Returns the prefix of the FolioNumber. Country-specific for Chile and Mexico. Field name: FolioPref. Length: 2 characters.
- `Public Property Indicator() As String` [R/W] Sets or returns the Factoring Indicator for the journal entries master record. Field name: Indicator. Length: 2 characters. This is a foreign key to the FactoringIndicators object.
  - remarks: This indicator is automatically inserted as default value in outgoing invoices and may be displayed in the account statements. Can be used later for sorting invoices related to this business partner. You can set only an indicator that is already defined in SAP Business One.
- `Public Property IsCostCenterTransfer() As BoYesNoEnum` [R/W] property IsCostCenterTransfer
- `Public Property JdtNum() As Long` [R] Returns the number of the journal transaction in the system. Field name: JDT_NUM.
- `Public Property Letter() As FolioLetterEnum` [R] property Letter
- `Public Property Lines() As JournalEntries_Lines` [R] Returns the JournalEntries_Lines object.
  - remarks: Each line represents one journal entry.
- `Public Property LocationCode() As Long` [R/W] Sets or returns the location code in journal entries. Applicable for cluster B. Field name: LocCode.
- `Public Property Memo() As String` [R/W] Sets or returns details about the journal entry. Field name: Memo. Length: 50 characters.
- `Public Property Number() As Long` [R] Returns Number of entries in Journal. Field name: Number.
- `Public Property OperationCode() As OperationCodeTypeEnum` [R/W] property OperationCode
- `Public Property Original() As Long` [R] The document entry of the document that triggered the current journal entry (DocEntry property of the Documents object). Field name: CreatedBy
- `Public Property OriginalJournal() As TransTypesEnum` [R] The type of document that triggered the current journal entry. Field name: TransType
- `Public Property PointOfIssueCode() As String` [R] property PointOfIssueCode
- `Public Property Printed() As PrintStatusEnum` [R] Returns a valid value that specifies the print status of the journal entry document.
- `Public Property PrivateKeyVersion() As Long` [R] property PrivateKeyVersion
- `Public Property ProjectCode() As String` [R/W] Sets or returns the project code related to the journal entry. Field name: Project, length: 8 characters. This is a foriegn key to Project Codes table, exposed via ProjectsService. In SAP Business One, you can relate business transactions to projects. This can help you to create cost/income analyzes reports based on projects.
  - remarks: Editing project code in the Journal Entry header does not affect the project code assigned to Journal Entry lines. To enforce the change on the lines, you must set JournalEntries_Lines.ProjectCode.
- `Public Property Reference() As String` [R/W] Sets or returns the first reference code of the journal entry. Field name: Ref1. Length: 100 characters.
- `Public Property Reference2() As String` [R/W] Sets or returns the second reference code of the journal entry. Field name: Ref2. Length: 100 characters.
- `Public Property Reference3() As String` [R/W] Sets or returns the third reference code of the journal entry. Field name: Ref3. Length: 100 characters.
- `Public Property ReferenceDate() As Date` [R/W] Sets or returns the posting date of the journal entry. Field name: RefDate.
- `Public Property Report347() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not to include the journal entry in the 347 report. Country-specific for Spain. Field name: Report347.
  - remarks: Once the journal entry is reported, and the report is approved, the status of this property cannot be changed. A journal entry that includes more than one or no business partner, cannot be specified as relevant to the 347 report.
- `Public Property ReportEU() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not to include the journal entry in the 349 report and/or the EU Sales report. Country-specific for Spain. Field name: ReportEU.
  - remarks: Once the journal entry is reported, and the report is approved, the status of this property cannot be changed. A journal entry that includes more than one or no business partner, cannot be specified as relevant to the 349 report and/or the EU Sales report.
- `Public Property ReportingSectionControlStatementVAT() As String` [R/W] property ReportingSectionControlStatementVAT
- `Public Property ResidenceNumberType() As ResidenceNumberTypeEnum` [R/W] property ResidenceNumberType
- `Public Property SAPPassport() As String` [R] property SAPPassport
- `Public Property Series() As Long` [R/W] Sets or returns the auto-number series that generated the Journal entry number. Field name: Series.
- `Public Property SignatureDigest() As String` [R] property SignatureDigest
- `Public Property SignatureInputMessage() As String` [R] property SignatureInputMessage
- `Public Property StampTax() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to apply stamp tax instead of TaxGroup in the JournalEntries_Lines child object. Field name: StampTax.
- `Public Property StornoDate() As Date` [R/W] Sets or returns the date for cancelling the transaction (creating a reverse transaction). Field name: StornoDate.
  - remarks: Default: the first day of the consecutive month.
- `Public Property TaxDate() As Date` [R/W] Sets or returns the date for the tax calculation or payment. Field name: TaxDate. Sets or returns the date for the tax calculation or payment. Field name: TaxDate.
  - remarks: Default: current date retrieved from the system server. This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types. Default: current date retrieved from the system server. This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property TransactionCode() As String` [R/W] Sets or returns the transaction code as defined in SAP Business One. Field name: TransCode. Length: 4 characters. This is a foreign key to the Journal Entry Codes table (OTRC), not exposed through the DI API).
  - remarks: In SAP Business One, users can assign codes to manual posting in accounting as another mean of identifying transactions. In this way, users can search manual posting more efficiently using the transaction code in the search.
- `Public Property UseAutoStorno() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to cancel the transaction (create a reverse transaction) in the date specified in the StornoDate property. Field name: AutoStorno.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VatDate() As Date` [R/W] Sets or returns the date from which the tax rate for this VAT Group code applies. Field name: vatdate.
  - remarks: If the DocDate value (posting date) is later than the VatDate value,SAP Business One applies the latest tax rate, else it applies the tax rate defined for the period before the VatDate value. Relevant to sales and purchase documents only.
- `Public Property WithholdingTaxData() As WithholdingTaxData` [R] Withholding tax information for this journal entry.
- `Public Property WTSum() As Double` [R] The withholding tax amount. Field name: WTSum
- `Public Property WTSumFC() As Double` [R] The withholding tax amount in foreign currency. Field name: WTSumFC
- `Public Property WTSumSC() As Double` [R] The withholding tax amount in foreign currency. Field name: WTSumSC

## Methods (10)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Cancel() As Long` Not supported.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal JdtNum As Long) As Boolean` Retrieves one SAP Business One object by its absolute key in the database.
  - param `JdtNum`: Specifies the number of the journal transaction (see JdtNum property).
  - returns: The method returns True, if it finds an object by the key you specified. The method returns False, if it cannot find a record with the key you specified.
  - remarks: In SAP Business One, every Business Object is assigned with a unique key. This method is useful when you know the key of an object, or when you want to know whether or not there is an object assigned to the key you specified.
- `Public Function Remove() As Long` Not supported.
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
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

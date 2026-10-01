<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Attachments2_Lines (Object)

The Attachments2_Lines is a child object of the Attachments2 object. Each line stores details about one attachment file. Source table: ATC1.

**Remarks:** Mandatory properties: Attachments2_Lines, FileName, and FileExtension. To display the form in the application: - Select the Attachments tab of one of the following forms: Employee Master Data, Contracts, Contract Template, Service Contract, and Customer Equipment Card.

## Properties (13)
- `Public Property AbsoluteEntry() As Long` [R] Returns the identification key of the attachment file as assigned by SAP Business One when adding an attachment file. Field name: AbsEntry.
- `Public Property AttachmentDate() As Date` [R] Returns the date when the file was copied to the system attachments folder. Field name: Date.
- `Public Property CopyToProductionOrder() As BoYesNoEnum` [R/W] Copy attachments automatically from BOM to production order. Field name: CopyToProd.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.Attachments2 att = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oAttachments2); success = att.GetByKey(productionOrder.AttachmentEntry);
    att.Lines.SetCurrentLine(0);
    att.Lines.CopyToProductionOrder = BoYesNoEnum.tYES;
    ```
- `Public Property CopyToTargetDoc() As BoYesNoEnum` [R/W] Copy to target document. Field name: CopyToTrgt.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property FileExtension() As String` [R/W] Sets or returns the file extension. Field name: FileExt. Length: 8 characters.
  - remarks: Mandatory fields in SAP Business One: FileExtension.
- `Public Property FileName() As String` [R/W] Sets or returns the file name. Field name: FileName. Length: 254 characters.
  - remarks: Mandatory fields in SAP Business One: FileName.
- `Public Property FreeText() As String` [R/W] Free text. Field name: FreeText. Length: 100 characters.
- `Public Property LineNum() As Long` [R/W] Row number. Field name: Line.
- `Public Property Override() As BoYesNoEnum` [R/W] Determines whether or not to override a file, with the same name, that is already stored in the system attachments folder. Field name: Override.
- `Public Property SourcePath() As String` [R/W] Sets or returns the folder name and path where the source files are stored. Field name: srcPath. Length: 64,000 characters.
  - remarks: Mandatory fields in SAP Business One: SourcePath.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserID() As Long` [R] Returns the identification key of the user who operates the system. Field name: UsrID. Returns the identification key of the active user who operates the system.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

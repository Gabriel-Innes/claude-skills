<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DefaultDocuments (Object)

The DefaultDocuments is a child object of the UserDefaultGroups object. It enables to set default settings for printing documents per user or users group. Source table: UDG1.

**Remarks:** If you set this object, the system uses these defaults instead of the Print Preferences (OADP and ADP1 tables, which are not exposed through the DI API). The relatedness of the properties depends on the document type (ObjectType). For example, PrintTotal is related to document types such as, Goods Receipt and Sales Quatation. To display the form in the application: - Select Administration -->Setup -->General -->Users. - From the Defaults field, click the Choose From List button. - In the List of User Defaults, click the New button. - In the User Defaults form, select the Print tab.

## Properties (15)
- `Public Property AddExport() As BoYesNoEnum` [R/W] Determines the default for whether or not to also export the document to Microsoft Word format when the user clicks the Add button (adds the document to the system). Field name: ExprtOnAdd.
  - remarks: If you set this property, the system uses its setting as default instead of ExprtOnAdd field of the ADP1 table.
- `Public Property AddPrint() As BoYesNoEnum` [R/W] Determines the default for whether or not to also print the document when the user clicks the Add button (adds the document to the system). Field name: PrintOnAdd.
  - remarks: If you set this property, the system uses its setting as default instead of PrintOnAdd field of the ADP1 table.
- `Public Property Code() As String` [R] Returns the code (primary key) of the user defaults group. Field name: Code. Length: 8 characters.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property EnglishKeyboardEnteringBPC() As BoYesNoEnum` [R/W] Determines the default for whether or not to switch the keyboard to English when entering a business partner code for the specified document type. Field name: EngKBCard.
  - remarks: If you set this property, the system uses its setting as default instead of EngKBCard field of the ADP1 table.
- `Public Property EnglishKeyboardEnteringItem() As BoYesNoEnum` [R/W] Determines the default for whether or not to switch the keyboard to English when entering an item code for the specified document type. Field name: EngKBCard.
  - remarks: If you set this property, the system uses its setting as default instead of EngKBItem field of the ADP1 table.
- `Public Property NoofCopies() As Long` [R/W] Sets or returns the number of copies (including original) to print when creating a new document of the specified document type. Field name: Copies.
  - remarks: If you set this property, the system uses its setting as default instead of Copies field of the ADP1 table.
- `Public Property NoofCopiesforManualDoc() As Long` [R/W] Sets or returns the number of copies to print when creating a document with manual number assignment. The system treats a document with manual number assignment as a copy, not as an original document. Field name: HandCopies.
  - remarks: If you set this property, the system uses its setting as default instead of HandCopies field of the ADP1 table.
- `Public Property ObjectType() As String` [R/W] Returns the document type number for which these defaults apply. For example, set the value 23 for sales quatation (see the ObjList field of the OADP table). Field name: ObjType. Length: 20 characters.
- `Public Property PermanentRemark() As String` [R/W] Sets or returns the default permanent remark for printing in the specified document type. Field name: Remark. Length: 16 characters.
  - remarks: If you set this property, the system uses its setting as default instead of Remark field of the ADP1 table.
- `Public Property PrintDiscountData() As BoYesNoEnum` [R/W] Determines the default for whether or not to print discount data in the specified document type. Field name: PrnDscnt.
  - remarks: If you set this property, the system uses its setting as default instead of PrnDscnt field of the ADP1 table.
- `Public Property PrintTotals() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to print the total amount in the document. Field name: PrintSums.
  - remarks: If you set this property, the system uses its setting as default instead of PrintSums field of the ADP1 table.
- `Public Property PrintVendorCatalogNo() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to print the manufacturer number instead of the item number in the specified document type. Field name: VndrNum.
  - remarks: If you set this property, the system uses its setting as default instead of VndrNum field of the ADP1 table.
- `Public Property TotalsRounding() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to round total amounts in the specified document type. Field name: RoundSums.
  - remarks: If you set this property, the system uses its setting as default instead of RoundSums field of the ADP1 table.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AdditionalExpenses (Object)

AdditionalExpenses is a business object that represents the additional expenses defined in the Administration module. These definitions are used by the Marketing Documents and Receipts. This object enables to calculate additional costs connected with a document, such as delivery changes and deposit tax. This object enables you to: - Add an additional expense. - Retrieve an additional expense by its key. - Update an additional expense. - Save the object in XML format. Source table: OEXD.

**Remarks:** To display the form in the application: - Select Administration --> System Initialization --> Document Settings. - In the General tab, select Manage Expenses In Documents. - Click Define Expenses.

## Properties (30)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property DistributionMethod() As BoAeDistMthd` [R/W] Sets or returns a valid value of BoAeDistMthd type that specifies the distribution method of the additional expenses. Field name: DistrbMthd
- `Public Property DistributionRule() As String` [R/W] The distribution rule for allocating costs and revenues (both direct and indirect) to one or more cost centers. This is a foreign key to the DistributionRule object. Field name: OcrCode
- `Public Property DistributionRule2() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode2
- `Public Property DistributionRule3() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode3
- `Public Property DistributionRule4() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode4
- `Public Property DistributionRule5() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode5
- `Public Property DrawingMethod() As DrawingMethodEnum` [R/W] The calculation method for freight per row. The calculation method is relevant when you copy rows from a base document to a target document. Field name: BaseMethod
- `Public Property ExpensCode() As Long` [R] Returns the unique ID (primary key) of the additional expense. SAP Business One assigns a sequential number when adding an additional expense. Field name: ExpnsCode
- `Public Property ExpenseAccount() As String` [R/W] Sets or returns the expense account number. You can set only accounts that are defined as Expenses type in Chart of Accounts. Field name: ExpnsAcct Length: 15 characters This is a foreign key to the ChartOfAccounts object.
- `Public Property ExpenseExemptedAccount() As String` [R/W] Sets or returns the expense exempted account. Field name: ExpnsExAct Length: 15 characters This is a foreign key to the ChartOfAccounts object.
- `Public Property FixedAmountExpenses() As Double` [R/W] Sets or returns the fixed amount of the expense. Field name: ExpFixSum
- `Public Property FixedAmountRevenues() As Double` [R/W] Sets or returns the fixed revenue amount of the expense. Field name: RevFixSum
- `Public Property FreightOffsetAccount() As String` [R/W] Sets or returns the freight offset account. Field name: ExpOfstAc Length: 15 characters This is a foreign key to the ChartOfAccounts object.
- `Public Property FreightType() As FreightTypeEnum` [R/W] Indicates the type of freight expense. Field name: ExpnsType
- `Public Property FreightTypeForBollo() As FreightTypeForBolloEnum` [R/W] property FreightTypeForBollo
- `Public Property GrossFreight() As BoYesNoEnum` [R/W] property GrossFreight
- `Public Property Includein1099() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to include the expense in the 1099 form. Field name: In1099
- `Public Property InputVATGroup() As String` [R/W] Sets or returns the input VAT group. Field name: VatGroupi Length: 8 characters This is a foreign key to the VatGroups object.
- `Public Property LastPurchasePrice() As BoYesNoEnum` [R/W] Indicates whether to update the last purchase price list after adding an A/P invoice that includes a freight amount per row. Field name: LstPchPrce
- `Public Property Name() As String` [R/W] Sets or returns the expense name. Field name: ExpnsName Length: 20 characters
- `Public Property OutputVATGroup() As String` [R/W] Sets or returns the output VAT group. Field name: VatGroupo Length: 8 characters This is a foreign key to the VatGroups object.
- `Public Property Project() As String` [R/W] The project that relates to the freight. Field: Project. Length: 20 characters.
- `Public Property RevenuesAccount() As String` [R/W] Sets or returns the revenues account. You can set only accounts that are defined as Revenues type in Chart of Accounts. Field name: RevAcct Length: 15 characters This is a foreign key to the ChartOfAccounts object.
- `Public Property RevenuesExemptedAccount() As String` [R/W] Sets or returns the revenues exempted account. Field name: RevExmAcct Length: 15 characters This is a foreign key to the ChartOfAccounts object.
- `Public Property SACCode() As String` [R/W] property SACCode
- `Public Property Stock() As BoYesNoEnum` [R/W] Indicates whether to add the freight amount, either in the row level or the total level, to the item's cost when working with perpetual inventory. Field name: Stock
- `Public Property TaxLiable() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the additional expense is VAT liable. Field name: TaxLiable
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WTLiable() As String` [R] Returns the whether or not the additional expense is subject to withholding tax. Field name: TaxLiable Length: 1 character

## Methods (8)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal ExpnsCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ExpnsCode`: Specifies the code of the additional expense.
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

<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BudgetDistribution (Object)

BudgetDistribution is a business object that represents the budget distribution methods used by the budget management in the Finance module. This object enables you to: - Add a budget distribution method. - Retrieve a budget distribution method by its key. - Update a budget distribution method. - Save the object in XML format. Source table: OBGD.

**Remarks:** To initialize the budget management: - Select Administration --> System Initialization --> General Settings. - In the Budget tab, select Budget Initialization. - Set the budget initialization parameters and click OK. To display the form in the application: - Select Financials --> Budget --> Define Budget Distribution Method.

## Properties (17)
- `Public Property April() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property August() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property BudgetAmount() As Double` [R/W] Returns the total of the 12 monthly factors. Field name: BgdTotal.
- `Public Property December() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property Description() As String` [R/W] Sets or returns the name of the budget distribution method. Field name: BgdName. Length: 30 characters.
- `Public Property DivisionCode() As Long` [R] Returns the budget distribution code. Field name: BgdCode.
- `Public Property February() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property January() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property July() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property June() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property March() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property May() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property November() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property October() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property September() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (8)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Cancel() As Long` Cancels a record from the object table.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lBgdCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lBgdCode`: Budget distribution code (DivisionCode).
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

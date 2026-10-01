<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# FormattedSearches (Object)

The FormattedSearches object enables to assign a formatted search function to a specified field, so that SAP Business One users can enter values, originated by a pre-defined search process, to the field. The formatted search is applicable for any field in the system including user defined fields. Source table: CSHS.

**Remarks:** The mandatory properties include the FormID, ItemID, and ColumnID. The combination of these properties determines the key of the field for which the formatted search is applicable. Additional mandatory properties are according to the value of the Action property. The following are examples of using the formatted search function: - Automatic entery of values into fields using various objects in the system. - Entering values into fields using a pre-defined list of valid values. - Automatic entery of values into fields by user-defined queries. - Creating dependency between fields in the system. That is, the value of field X influence the value of field Y. - Displaying fields that can only be displayed using queries such as, User Signature, Creation Date, Open Checks Balance (for business partner). To display the form in the application: - Open a document and click any field. - From the menu bar, select Tools --> Search Function --> Define. The Define Formatted Search form opens. - To view more fields, select the Search by Saved Query. General Guidelines Make sure to follow these guidelines, otherwise the system responds with the error -1003. - The formatted search query must refer to an existing field. For user-defined fields add the "U_" prefix. - The SQL syntax must be correct. - Add a Space character between the Equal sign (=) and the field/string before the Equal sign. - To compare a field of Alpha type to a variable such as [0], use a single quotation mark ' '[0]'. - Values must exist for the specified field before activating the formatted search function. For more details, refer to SMB Portal (upper menu: Service and Support. left menu: Knowledge & Services --> Knowledge Base). Look for the Formatted Search document.

## Properties (15)
- `Public Property Action() As BoFormattedSearchActionEnum` [R/W] Determines the type of action to be taken by the system when activating the formatted search function. The options include: Without Search, Search in Existing Values, and Search By Saved Query. Field name: ActionT.
  - remarks: The mandatory properties, in addition to FormID, ItemID, and ColumnID, depend on the value of the Action property as follows: bofsaNone | no additional mandatory properties. bofsaValidValues | UserValidValues object. bofsaQuery | QueryID, FieldID.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property ByField() As BoYesNoEnum` [R/W] Determines whether the automatic refresh is activated when the field changes or when exiting an altered column. Applicable for Table fields only and when the Refresh property is set tYES. Field name: ByField.
- `Public Property ByFieldEx() As FormattedSearchByFieldEnum` [R/W] property ByFieldEx
- `Public Property ColumnID() As String` [R/W] Sets or returns the column identification key. Mandatory for Table fields. The default value: -1 (Title field). Length: 11 characters.
  - remarks: The entered value must be a valid column ID (the system does not validate the entered value). To display the column ID in the application status bar: - From the main menu, select View --> System Information.
- `Public Property FieldID() As String` [R/W] Sets or returns the field ID. Field name: FieldID. Length: 11 characters. Mandatory in case Action is set to bofsaQuery.
  - remarks: Each form includes different set of Field IDs.
- `Public Property FieldIDs() As FormattedSearchFields` [R] property FieldIDs
- `Public Property ForceRefresh() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to refresh the data regularly or only to display the saved value. Field name: FrceRfrsh.
- `Public Property FormID() As String` [R/W] Sets or returns the form identification key. Field name: FormID. Mandatory property. Length: 100 characters.
  - remarks: The entered value must be a valid form ID (the system does not validate the entered value). To display the form ID in the application status bar: - From the main menu, select View System Information.
- `Public Property Index() As Long` [R] Returns the primary key of the formatted search function as assigned by the system when adding the object. Field name: IndexID.
- `Public Property ItemID() As String` [R/W] Sets or returns the ID of the field or the table in a form (primary key with FormID). Field name: ItemID. Mandatory property. Length: 20 characters.
  - remarks: The entered value must be a valid item ID (the system does not validate the entered value). In case the ItemID specifies a table, set also the ColumnID, otherwise the system sets the value -1. To display the item ID in the application status bar: - From the main menu, select View --> System Information. For a list of item IDs and coulmn IDs, refer to SMB Portal (from the main menu, select Service and Support. Then from the left menu, select Knowledge & Services --> Knowledge Base). Look for the document FormattedSearch.Doc.
- `Public Property QueryID() As Long` [R/W] Sets or returns the key of the query for the formatted search function. Field name: QueryId. Mandatory in case Action is set to bofsaQuery.
- `Public Property Refresh() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to automatically refresh the data when the field value is modified. Field name: Refresh.
  - remarks: In case this property is set to tYES and the field is a Table field, then the ByField property is applicable.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserValidValues() As UserValidValues` [R] Returns the UserValidValues object.

## Methods (7)
- `Public Function Add() As Long` Assigns a formatted search function to a specified field.
- `Public Function GetAsXML() As String` GetAsXML
- `Public Function GetByKey(ByVal lIndex As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lIndex`: Index.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes the current record.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal bstrFileName As String)` Save the object to a file as XML data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef pbstrFileName As String)` Saves the object data to XML formatted data.
  - param `pbstrFileName`: Specifies the path and file name of the XML data.
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

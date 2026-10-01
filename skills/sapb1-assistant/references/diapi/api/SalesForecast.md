<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SalesForecast (Object)

SalesForecast is a business object that represents the sales forecast for a specified period. The sales forecast is required for planning the purchase and production of items in the MRP module. This object enables you to: - Add a sales forecast. - Retrieve a sales forecast by its key. - Update a sales forecast. - Remove a sales forecast. - Save the object in XML format. Source table: OFCT.

**Remarks:** Mandatory fields in SAP Business One: ForecastCode and ForecastName. To display the form in the application: - Select MRP --> Define Forecasts.

## Properties (9)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property ForecastCode() As String` [R/W] Sets or returns the sales forecast code. Field name: Code Mandatory property. Length: 16 characters.
- `Public Property ForecastEndDate() As Date` [R/W] Sets or returns the end date for the sales forecast. The default is the last day of the current year. Field name: EndDate
  - remarks: Default: end date of current year.
- `Public Property ForecastName() As String` [R/W] Sets or returns the sales forecast name. Mandatory property. Field name: Name Length: 100 characters.
- `Public Property ForecastStartDate() As Date` [R/W] Sets or returns the start date for the sales forecast. The default is the current date. Field name: StartDate
  - remarks: Default: current date.
- `Public Property Lines() As SalesForecast_Lines` [R] Returns the SalesForecast_Lines child object.
- `Public Property Numerator() As Long` [R] Returns the sales forecast absolute ID. Field name: AbsID
  - remarks: This is a sequential number assigned by SAP Business One when adding a sales forecast.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property View() As ForecastViewTypeEnum` [R/W] Indicates whether the lines represent daily, weekly, or monthly forecasts. The default is daily. Field name: FormView
  - remarks: The field cannot be changed after adding the forecast. If you select weeks, the ForecastStartDate and ForecastEndDate must be the start and end of a week. The week is defined at Administration --> System Initialization --> Company Detail --> Accouting Data tab --> Holiday field. If you select months, the ForecastStartDate and ForecastEndDate must be the start and end of a month.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lID`: Sales forecast absolute ID (Numerator).
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

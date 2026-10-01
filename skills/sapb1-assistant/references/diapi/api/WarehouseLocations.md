<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# WarehouseLocations (Object)

The WarehouseLocations object enables to define geographical locations for warehouses. Source table: OLCT.

**Remarks:** To display the form in the application: - Select Administration --> Setup --> Inventory --> Warehouses. - From the Location field select Define New. Defining few locations for a warehouse is required when the warehouse includes few areas, where each area can be concidered as a separate warehouse, with the same address as the main warehouse.

## Properties (34)
- `Public Property AssesseeType() As String` [R/W] Sets or returns the assessee type in the location definition. Applicable for cluster B only. Field name: AsseType.
- `Public Property Block() As String` [R/W] Sets or returns the block name in the location definition. Applicable for cluster B only. Field name: Block.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property BuildingFloorRoom() As String` [R/W] Sets or returns the building in the location definition. Applicable for cluster B only. Field name: Building.
- `Public Property CECommissionerate() As String` [R/W] Sets or returns the C.E. commissionerate in the location definition. Applicable for cluster B only. Field name: CeComRate.
- `Public Property CEDivision() As String` [R/W] Sets or returns the C.E division in the location definition. Applicable for cluster B only. Field name: CeDivision.
- `Public Property CERange() As String` [R/W] Sets or returns the C.E range in the location definition. Applicable for cluster B only. Field name: CeRange.
- `Public Property CERegisterNumber() As String` [R/W] Sets or returns the C.E Register number in the location definition. Applicable for cluster B only. Field name: CeRegNo.
- `Public Property City() As String` [R/W] Sets or returns the city in the location definition. Applicable for cluster B only. Field name: City.
- `Public Property Code() As Long` [R] Returns the warehouse location code (primary key) in the Location definition. Field name: Code.
- `Public Property CompanyType() As String` [R/W] Sets or returns the company type in the location definition. Applicable for cluster B only. Field name: CompType.
- `Public Property Country() As String` [R/W] Sets or returns the country in the location definition. Applicable for cluster B only. Field name: Country.
- `Public Property County() As String` [R/W] Sets or returns the county in the location definition. Applicable for cluster B only. Field name: County.
- `Public Property CSTNumber() As String` [R/W] Sets or returns the CST number in the location definition. Applicable for cluster B only. Field name: CstNo.
- `Public Property EccNumber() As String` [R/W] Sets or returns the E.C.C number in the location definition. Applicable for cluster B only. Field name: EccNo.
- `Public Property ExemptionNumber() As String` [R/W] Sets or returns the exempt number in the location definition. Applicable for cluster B only. Field name: EccNo.
- `Public Property GSTIN() As String` [R/W] property GSTIN
- `Public Property GSTISD() As String` [R/W] property GSTISD
- `Public Property GSTTDS() As String` [R/W] property GSTTDS
- `Public Property GstType() As BoGSTRegnTypeEnum` [R/W] property GstType
- `Public Property Jurisdiction() As String` [R/W] Sets or returns the jurisdiction in the location definition. Applicable for cluster B only. Field name: Jurisd.
- `Public Property LSTVATNumber() As String` [R/W] Sets or returns the LST/VAT number in the location definition. Applicable for cluster B only. Field name: LstVatNo.
- `Public Property ManufacturerCode() As String` [R/W] Sets or returns the manufacture code in the location definition. Applicable for cluster B only. Field name: ManuCode.
- `Public Property Name() As String` [R/W] Sets or returns the name of the geographical location for warehouses. Field name: Location. Length: 100 characters.
- `Public Property NatureOfBusiness() As String` [R/W] Sets or returns the nature of business in the location definition. Applicable for cluster B only. Field name: NatOfBiz.
- `Public Property PANNumber() As String` [R/W] Sets or returns the PAN number in the location definition. Applicable for cluster B only. Field name: PanNo.
- `Public Property RegistrationType() As String` [R] Returns the registration type in the location definition. Applicable for cluster B only. Field name: RegType.
- `Public Property ServiceTaxNumber() As String` [R/W] Sets or returns the Service Tax Number in the location definition. Applicable for cluster B only. Field name: ServTaxNo.
- `Public Property State() As String` [R/W] Sets or returns the state in the location definition. Applicable for cluster B only. Field name: State.
- `Public Property Street() As String` [R/W] Sets or returns the street in the location definition. Applicable for cluster B only. Field name: Street.
- `Public Property TANNumber() As String` [R/W] Sets or returns the TAN number in the location definition. Applicable for cluster B only. Field name: TanNo.
- `Public Property TINNumber() As String` [R/W] Sets or returns the T.I.N number in the location definition. Applicable for cluster B only. Field name: TinNo.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property ZipCode() As String` [R/W] Sets or returns the zip code in the location definition. Applicable for cluster B only. Field name: ZipCode.

## Methods (6)
- `Public Function Add() As Long` Adds a warehouse location definition.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lCode`: Code.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
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

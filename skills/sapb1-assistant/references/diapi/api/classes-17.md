<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# LengthMeasures (Object)

The LengthMeasures object enables to define the length and width measure units that are used for item records. Source table: OLGT.

**Remarks:** To display the form in the application: - Select Administration --> Setup --> Inventory --> Length and Width UoM.

## Properties (7)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property UnitCode() As Long` [R] Returns the length unit code (primary key). Field name: UnitCode.
- `Public Property UnitCodeforQuantityDisplay() As String` [R/W] Sets or returns the volume code (for example, cc). Field name: VolDisply. Length: 3 characters.
- `Public Property UnitDisplay() As String` [R/W] Sets or returns the displayed name for the length or width unit (for example, cm). Field name: UnitDisply. Length: 2 characters.
- `Public Property UnitLengthinmm() As Double` [R/W] Sets or returns the length in milimeters. For example: 10 mm for cm measure unit or 25.4 mm for Inch measure unit. Field name: SizeInMM.
- `Public Property UnitName() As String` [R/W] Sets or returns the unit name (for example, centimeter). Field name: UnitName. Length: 20 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a length unit of measure definition.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lUnitCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lUnitCode`: UnitCode.
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

# LocalEra (Object)

LocalEra is a business object that represents the Local Era. Local Era is a type of calendar system that co-existent in some countries (such as, Japan) with the Gregorian calendar. This object enables you to: - Browse the Local Era table for mapping to or from the Gregorian calendar (Browser). - Retrieve details about the Local Era by its key (Code). - Retrieve the Local Era details from XML data. - Save the object to a file as XML data. - Save the object as XML formatted data. Source table: OJPE.

**Remarks:** Country-specific for Japan. To display the form in the application: - Select Administration --> Setup --> Define Local Era.

## Properties (5)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Code() As String` [R] Returns the Local Era code. Field name: Code. Length: 1 character.
- `Public Property EraName() As String` [R] Returns the Local Era name. Field name: EraName. Length: 20 characters.
- `Public Property StartDate() As Date` [R] Returns the start date of the Local Era calendar. Field name: StartDate.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (4)
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal bstrCode As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `bstrCode`: Code.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Sub SaveToFile(ByVal bstrFileName As String)` Save the object to a file as XML data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef pbstrFileName As String)` method SaveXML
  - param `pbstrFileName`: Specifies the path and file name of the XML data.

# Manufacturers (Object)

The Manufacturers object enables to define manufacturers used in the Item master data. Source table: OMRC.

**Remarks:** To display the form in the application: - Select Administration --> Setup --> Inventory --> Manufacturers.

## Properties (4)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Code() As Long` [R] Returns the manufacturer code (primary key). Field name: FirmCode.
- `Public Property ManufacturerName() As String` [R/W] Sets or returns the manufacturer name. Field name: FirmName. Length: 30 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a manufacturer definition.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lCode`: Code.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You cannot delete a manufacturer if it is used in item master data. You must use the GetByKey method to retrieve a valid object.
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

# MaterialGroup (Object)

Represents a material group, which is used for the automatic tax code determination for materials. Source table: OMGP.

**Remarks:** Country-specific for Brazil only.

## Properties (3)
- `Public Property AbsEntry() As Long` [R] The internal key of a specific material group. Field name: AbsEntry.
- `Public Property Description() As String` [R/W] The description of the material group. Field name: Descrip. Length: 70 characters.
- `Public Property MaterialGroupCode() As String` [R/W] The code of the material group. Field name: MatGrp. Length: 3 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# MaterialGroupParams (Object)

Holds the key and name to an existing material group. This object is used to pass keys to and retrieve keys from MaterialGroupsService methods.

## Properties (2)
- `Public Property AbsEntry() As Long` [R/W] The internal key that identifies the material group. Field name: AbsEntry.
- `Public Property MaterialGroupCode() As String` [R] The code of the material group. Field name: MatGrp.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# MaterialGroupsParams (Collection)

A collection of MaterialGroupParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As MaterialGroupParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As MaterialGroupParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# MaterialGroupsService (Object)

The MaterialGroupsService service enables you to add, look up, update, and remove material groups. Source table: OMGP.

**Remarks:** Country-specific for Brazil only. To see the material groups, from the SAP Business One Main Menu, choose Administration --> Setup --> Financials --> Tax --> Item Classification --> Material Group.

## Methods (8)
- `Public Function AddMaterialGroup(ByVal pIMaterialGroup As MaterialGroup) As MaterialGroupParams` Adds a material group.
  - param `pIMaterialGroup`: The data for the new material group.
- `Public Sub DeleteMaterialGroup(ByVal pIMaterialGroupParams As MaterialGroupParams)` Deletes an existing material group.
  - param `pIMaterialGroupParams`: The key of the material group to be deleted.
- `Public Function GetDataInterface(ByVal enumMSDI As MaterialGroupsServiceDataInterfaces) As Object` Creates an empty data structure for use with the MaterialGroupsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `MaterialGroupsServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLFile(Hashtable Properties, String Path)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair In Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        oGeneralData.ToXMLFile(Path);

        //Retrieve XML and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLFile(Path);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLString(Hashtable Properties)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;
        string XMLString;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair in Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        XMLString = oGeneralData.ToXMLString();

        //Retrieve XML string and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLString(XMLString);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetMaterialGroup(ByVal pIMaterialGroupParams As MaterialGroupParams) As MaterialGroup` Retrieves a material group. The material group is specified by its key, which is contained in the MaterialGroupParams object passed to the method.
  - param `pIMaterialGroupParams`: The key of the material group to retrieve.
- `Public Function GetMaterialGroupList() As MaterialGroupsParams` Returns the MaterialGroupsParams data collection that identify all material groups.
- `Public Sub UpdateMaterialGroup(ByVal pIMaterialGroup As MaterialGroup)` Updates an existing material group. The data for the material group, including the key of the material group to be updated, is contained in the MaterialGroup object passed to the method. To update a material group, you must first retrieve it using the GetMaterialGroup method.
  - param `pIMaterialGroup`: The data for the material group to be updated. The MaterialGroup object must contain the key of the object to be updated.

# MaterialRevaluation (Object)

MaterialRevaluation is a business object that enables you to update the items' price (average price or standard price only), revaluate the stock, and create journal entries accordingly. This object applies only to companies that manage their stock using Continuous Stock system. This object enables you to: - Add a material revaluation. - Retrieve a material revaluation by its key. - Update a material revaluation. - Save the object in XML format. Source table: OMRV.

## Properties (25)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CardCode() As String` [R/W] property CardCode
- `Public Property CardName() As String` [R/W] property CardName
- `Public Property Comments() As String` [R/W] Sets or returns comments for the document. Field name: Comments. Length: 254 characters.
  - remarks: This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property CreationDate() As Date` [R] Returns the creation date of the document. Field name: CreateDate.
  - remarks: This property is internal in SAP Business One.
- `Public Property DataSource() As String` [R] Not used. Field name: DataSource.
- `Public Property DocDate() As Date` [R/W] Sets or returns the document posting date. Field name: DocDate.
  - remarks: The default is the current date retrieved from the system server. This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property DocEntry() As Long` [R] Returns the document entry key that uniquely identifies the document. Field name: DocEntry.
- `Public Property DocNum() As Long` [R] Sets or returns the number of the document. Field name: DocNum.
  - remarks: and also verify Relevant to sales documents only. In case the value of the HandWritten property is tNO and you add a sales document, SAP Business One automatically assigns the next available number to the document, in accordance with the document numbering system defined during system configuration. When saving the document as a draft, this number is stored for the document draft only. So that the number of the draft is still available in the system for other new documents. The system may assign this number to a new document of the same type. When saving the draft as a document, SAP Business One assigns a new available number. In case the value of the HandWritten property is tYES, set a value (greater than 0) to the DocNum property and also set the Series property to -1.
- `Public Property DocTime() As Date` [R] Sets or returns the document creation time. Field name: DocTime.
  - remarks: This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property DocumentReferences() As MaterialRevaluationDocumentReferences` [R] property DocumentReferences
- `Public Property InflationRevaluation() As BoYesNoEnum` [R/W] Specify whether to record inflation as the reason for this revaluation. You can then filter out inflation-based revaluations in the inventory valuation simulation report. Field: InflaReval.
  - remarks: It is a requirement of IFRS not to include inflation-based revaluations in inventory valuation.
- `Public Property JournalMemo() As String` [R/W] Sets or returns the journal entry remarks that is copied later to the accounting document. Field name: JrnlMemo. Length: 50 characters.
  - remarks: SAP Business One, by default, automatically enters the document type and the business partner number. When using the system's default template for printing, the remark is not printed on the associated document. This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property Lines() As MaterialRevaluation_lines` [R] Returns the MaterialRevaluation_lines child object.
- `Public Property Reference1() As String` [R] P>Sets or returns the first reference code of the document. Field name: Ref1. Length: 11 characters.
  - remarks: This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property Reference2() As String` [R/W] Sets or returns the second reference code of the document. Field name: Ref2. Length: 11 characters.
  - remarks: This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property RevalType() As String` [R/W] Sets or returns the revaluation type: price change or material debit/credit. Field name: RevalType. Length: 1 character.
- `Public Property RevaluationExpenseAccount() As String` [R/W] Sets or returns the revaluation expense account code. Field name: RExpnAcct. Length: 15 characters.
- `Public Property RevaluationIncomeAccount() As String` [R/W] Sets or returns the revaluation income account code. Field name: RIncmAcct. Length: 15 characters.
- `Public Property Series() As Long` [R/W] Sets or returns the auto-number series that generated the document number. Field name: Series. This is a foreign key to the Series object.
  - remarks: This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property TaxDate() As Date` [R/W] Sets or returns the date for the tax calculation or payment. Field name: TaxDate.
  - remarks: Default: current date retrieved from the system server. This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property TransNum() As Long` [R] Returns the transaction number that SAP Business One creates for the document. Field name: TransId. This is a foreign key to the JournalEntries object.
- `Public Property UpdateDate() As Date` [R] Returns the date when the material revaluation was last updated. Field name: UpdateDate.
  - remarks: Internal property in SAP Business One.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserSignature() As Long` [R] Returns the ID of the user who created the document. Field name: UserSign.

## Methods (9)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
- `Public Function Cancel() As Long` Not supported.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal AbsEntry As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `AbsEntry`: Specifies the document entry key (see DocEntry property).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Not supported.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Save object as XML document
  - param `FileName`: Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# MaterialRevaluation_lines (Object)

MaterialRevaluation_Lines is a child object of the MaterialRevaluation object representing the line entries of each transaction. Source table: MRV1.

## Properties (23)
- `Public Property ActualPrice() As Double` [R] Returns the current item price (item price before revaluation). Field name: RActPrice.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property DebitCredit() As Double` [R/W] Sets or returns the amount of money to be recalculated on items.
- `Public Property DistributionRule() As String` [R/W] The distribution rule for allocating costs and revenues (both direct and indirect) to one or more cost centers. This is a foreign key to the DistributionRule object. Field name: OcrCode
- `Public Property DistributionRule2() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode2
- `Public Property DistributionRule3() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode3
- `Public Property DistributionRule4() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode4
- `Public Property DistributionRule5() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode5
- `Public Property DocEntry() As Long` [R] Returns the document entry key that uniquely identifies the document. Field name: DocEntry.
- `Public Property FIFOLayers() As FIFOLayers` [R] The FIFO layers to be revalued. Relevant when the item's valuation method is FIFO.
- `Public Property ItemCode() As String` [R/W] Sets or returns the item code in the inventory. The item code must be unique. This is a foreign key to the Items object. Field name: ItemCode. Mandatory property. Length: 20 characters.
  - remarks: ItemCode is the primary key of item records in SAP Business One and used to distinguish between items in the system.
- `Public Property ItemDescription() As String` [R] Sets or returns the item name/description. Field name: Dscription. Length: 100 characters.
- `Public Property LineNum() As Long` [R] Returns the current row number in the list. Field name: LineNum.
- `Public Property OnHand() As Double` [R] Returns the number of available items in warehouse during the revaluation. Field name: ROnHand.
- `Public Property Price() As Double` [R/W] Sets or returns the item price before taxation. Field name: Price.
- `Public Property Project() As String` [R/W] The project to which the changed inventory value of the item is allocated. Field: Project. Length: 20 characters.
- `Public Property Quantity() As Double` [R/W] Sets or returns the number of items for recalculating their DebitCredit amount.
- `Public Property RevalAmountToStock() As Double` [R] Sets or returns the revaluation amount posted to the Stock Account. Field name: RToStock.
- `Public Property RevaluationDecrementAccount() As String` [R/W] Sets or returns the revaluation decrement account code. Field name: RDcrmAcct. Length: 15 characters.
- `Public Property RevaluationIncrementAccount() As String` [R/W] Sets or returns the revaluation increment account code. Field name: RIncmAcct. Length: 15 characters.
- `Public Property SNBLines() As SNBLines` [R] property SNBLines
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WarehouseCode() As String` [R/W] Sets or returns the warehouse code where the item is stored. Field name: WhsCode. Length: 8 characters. This is a foreign key to the Warehoses object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# MaterialRevaluationDocumentReferences (Object)

MaterialRevaluationDocumentReferences Class

## Properties (9)
- `Public Property Count() As Long` [R] property Count
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property ExternalReferencedDocNumber() As String` [R/W] property ExternalReferencedDocNumber
- `Public Property IssueDate() As Date` [R/W] property IssueDate
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property ReferencedDocEntry() As Long` [R/W] property ReferencedDocEntry
- `Public Property ReferencedDocNumber() As Long` [R] property ReferencedDocNumber
- `Public Property ReferencedObjectType() As ReferencedObjectTypeEnum` [R/W] property ReferencedObjectType
- `Public Property Remark() As String` [R/W] property Remark

## Methods (3)
- `Public Sub Add()` method Add
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 

# MaterialRevaluationFIFO (Object)

A specific item's FIFO layers. You can use the MaterialRevaluationFIFOService service to retrieve an item's FIFO layers, which are returned in this object. You can then revaluate these layers by passing the IDs of these FIFO layers to the items in the FIFOLayers property of the MaterialRevaluation_lines object.

## Properties (1)
- `Public Property Layers() As Layers` [R] The FIFO layers for a specific item and location.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# MaterialRevaluationFIFOParams (Object)

Contains parameters for retrieving FIFO layers using the MaterialRevaluationFIFOService service.

## Properties (4)
- `Public Property ItemCode() As String` [R/W] The key of an item whose costs are to be revaluated. This is a foreign key to the Items object.
- `Public Property LocationCode() As String` [R/W] A key to a location. Only layers for this location are returned by the GetMaterialRevaluationFIFO method. You must specify the location type in the LocationType property. Currently, the only location type is warehouse and, therefore, this property is a foreign key to the Warehouses object.
- `Public Property LocationType() As String` [R/W] A type of location for storing items. A specific location of this type is specified in the LocationCode property. Currently, the only valid value is 64, indicating a warehouse.
- `Public Property ShowIssuedLayers() As BoYesNoEnum` [R/W] Indicates which layers to retrieve, as follows: - If set to yes, all layer are retrieved. - If set to no, only layers with an open quantity not equal to zero are retrieved. Only relevant when the revaluation method is inventory debit/credit (see RevalType property of the MaterialRevaluation object).

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# MaterialRevaluationFIFOService (Object)

The MaterialRevaluationFIFOService service enables you to retrieve the FIFO layers for a specific item and location. You can then use information about the FIFO layers to specify specific layers to revalue (FIFOLayers) and provide these to the MaterialRevaluation object. To perform material revaluation, select Inventory --> Inventory Transactions --> Inventory Revaluation.

**Example:**
- C# example (from SAP's help):
  ```csharp
  SAPbobsCOM.MaterialRevaluation m_MaterialRev;
  SAPbobsCOM.MaterialRevaluation_lines m_MaterialRevLines;
  SAPbobsCOM.FIFOLayers m_FIFOLayers;

  SAPbobsCOM.MaterialRevaluationFIFOService m_MRVFIFOService;
  SAPbobsCOM.MaterialRevaluationFIFO m_MRVFIFO;
  SAPbobsCOM.MaterialRevaluationFIFOParams m_MRVFIFOParam;

  SAPbobsCOM.Items m_FIFOItems;
  SAPbobsCOM.Documents m_APInvoice;
  SAPbobsCOM.Document_Lines m_APInvoice_Line;

  SAPbobsCOM.BusinessPartners m_Vendor;

  m_MaterialRev = (MaterialRevaluation)m_Company.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oMaterialRevaluation);
  m_MaterialRev.DocDate = DateTime.Now;
  m_MaterialRev.RevalType = "P";

  // Line sub object:
  m_MaterialRevLines = m_MaterialRev.Lines;
  m_MaterialRevLines.SetCurrentLine(0);
  m_MaterialRevLines.ItemCode = m_FIFOItems.ItemCode;

  // Layer sub object
  m_FIFOLayers = m_MaterialRevLines.FIFOLayers;

  // Get Company Service
  m_companyService = (CompanyService)m_Company.GetCompanyService();

  // Get Material Revaluation FIFO Service
  m_MRVFIFOService = (MaterialRevaluationFIFOService)m_companyService.GetBusinessService(SAPbobsCOM.ServiceTypes.MaterialRevaluationFIFOService);

  // Create Material Revaluation FIFO Service parameters
  m_MRVFIFOParam = (MaterialRevaluationFIFOParams)m_MRVFIFOService.GetDataInterface(SAPbobsCOM.MaterialRevaluationFIFOServiceDataInterfaces.mrfifosMaterialRevaluationFIFOParams);
  m_MRVFIFOParam.ItemCode = m_FIFOItems.ItemCode;
  m_MRVFIFOParam.LocationCode = "01";
  m_MRVFIFOParam.LocationType = "64";
  m_MRVFIFOParam.ShowIssuedLayers = BoYesNoEnum.tNO;

  // Process FIFO layers
  m_MRVFIFO = m_MRVFIFOService.GetMaterialRevaluationFIFO(m_MRVFIFOParam);
  // Process first layer
  m_FIFOLayers.LayerID = m_MRVFIFO.Layers.Item(0).LayerID;
  m_FIFOLayers.TransactionSequenceNum = m_MRVFIFO.Layers.Item(0).TransactionSequenceNum;
  String strNewPrice = NewPriceTxt.Text;
  m_FIFOLayers.Price = 500;
  // Process other layers
  int LayerNum = m_MRVFIFO.Layers.Count;
  for (int i = 1; i < LayerNum ; ++i)
  {
       m_FIFOLayers.Add();
       m_FIFOLayers.SetCurrentLine(i);
       m_FIFOLayers.LayerID = m_MRVFIFO.Layers.Item(i).LayerID;
       m_FIFOLayers.TransactionSequenceNum = m_MRVFIFO.Layers.Item(i).TransactionSequenceNum;
       m_FIFOLayers.Price = 500;
  }
  m_MaterialRev.Add();
  ```

## Methods (4)
- `Public Function GetDataInterface(ByVal enumMSDI As MaterialRevaluationFIFOServiceDataInterfaces) As Object` Creates an empty data structure for use with the MaterialRevaluationFIFOService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `MaterialRevaluationFIFOServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLFile(Hashtable Properties, String Path)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair In Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        oGeneralData.ToXMLFile(Path);

        //Retrieve XML and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLFile(Path);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLString(Hashtable Properties)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;
        string XMLString;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair in Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        XMLString = oGeneralData.ToXMLString();

        //Retrieve XML string and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLString(XMLString);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetMaterialRevaluationFIFO(ByVal pIMaterialRevaluationFIFOParams As MaterialRevaluationFIFOParams) As MaterialRevaluationFIFO` Retrieves the FIFO layers for a specific item and location.
  - param `pIMaterialRevaluationFIFOParams`: The parameters for specifying the FIFO layers to retrieve
  - returns: The retrieved FIFO layers
  - remarks: If you specify a non-FIFO item, an exception is thrown.

# MaterialRevaluationSNBParam (Object)

MaterialRevaluationSNBParam Class

## Properties (1)
- `Public Property ItemCode() As String` [R/W] property ItemCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# MaterialRevaluationSNBParams (Object)

MaterialRevaluationSNBParams Class

## Properties (8)
- `Public Property AdmissionDate() As Date` [R] property AdmissionDate
- `Public Property DebitCredit() As Double` [R/W] property DebitCredit
- `Public Property ExpirationDate() As Date` [R] property ExpirationDate
- `Public Property LotNumber() As String` [R] property LotNumber
- `Public Property ManufactureNumber() As String` [R] property ManufactureNumber
- `Public Property NewCost() As Double` [R/W] property NewCost
- `Public Property SnbAbsEntry() As Long` [R/W] property SnbAbsEntry
- `Public Property SystemNumber() As Long` [R] property SystemNumber

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# MaterialRevaluationSNBParamsCollection (Collection)

MaterialRevaluationSNBParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As MaterialRevaluationSNBParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As MaterialRevaluationSNBParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# MaterialRevaluationSNBService (Object)

MaterialRevaluationSNBService Class

## Methods (5)
- `Public Function Add(ByVal pIMaterialRevaluationSNBParam As MaterialRevaluationSNBParam) As MaterialRevaluationSNBParams` Add
  - param `pIMaterialRevaluationSNBParam`: 
- `Public Function GetDataInterface(ByVal enumMSDI As MaterialRevaluationSNBServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `MaterialRevaluationSNBServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList(ByVal pIMaterialRevaluationSNBParam As MaterialRevaluationSNBParam) As MaterialRevaluationSNBParamsCollection` GetList
  - param `pIMaterialRevaluationSNBParam`: 

# Message (Object)

Message is a data structure related to the MessagesService. It includes properties related to the message content, such as subject, text, attached file, and attached data. Source table: OALR.

**Remarks:** The Message object replaces the Messages object. However, add-on that use the Messages object are valid. The major modification is in the way of attaching data to a message. That is, using the MessageDataColumn and MessageDataLine instead of AddDataColumn (Messages. To display the form in the application: - From the main menu bar, click the Message/Alert Overview icon.

## Properties (7)
- `Public Property Attachment() As Long` [R/W] Sets or returns the key of the attachment as assigned by SAP Business One when adding an attached file. Field name: Attachment.
- `Public Property MessageDataColumns() As MessageDataColumns` [R/W] Sets or returns the MessageDataColumns collection, which represents the data attached to a message.
- `Public Property Priority() As BoMsgPriorities` [R/W] Determines the priority flag of the message: Low, Normal, or High. Field name: Priority.
- `Public Property RecipientCollection() As RecipientCollection` [R/W] Sets or returns the RecipientCollection.
- `Public Property Subject() As String` [R/W] Sets or returns the message subject. Field name: Subject. Length: 50 characters.
- `Public Property Text() As String` [R/W] Sets or returns the message text. Field name: UserText. Length: 64,000 characters.
- `Public Property User() As Long` [R/W] Sets or returns the ID of the user that creates the message. Field name: UserSign. This is a foreign key to the Users object (InternalKey).

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# MessageDataColumn (Object)

MessageDataColumn is a data structure related to the MessagesService. It enables to add one data column to the data columns collection. The MessageDataColumn object contains the title of the column and whether or not it includes a link to a document. Source table: ALR2.

**Remarks:** To display the form in the application: - From the main menu bar, click the Message/Alert Overview icon. - Select the Data tab.

## Properties (3)
- `Public Property ColumnName() As String` [R/W] Sets or returns the column name in the message. Field name: ColName. Length: 30 characters.
- `Public Property Link() As BoYesNoEnum` [R/W] Determines whether or not to display a Link button in the data column. For example, link to a specified invoice. If the Link property is set to tYES, the object type (Object) and document key (ObjectKey) must be specified in the MessageDataLine object. Field name: Link.
- `Public Property MessageDataLines() As MessageDataLines` [R/W] Sets or returns the MessageDataLines collection.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# MessageDataColumns (Collection)

MessageDataColumns is a collection of MessageDataColumn data stractures. This enables to attache data to a message, such as invoice or quatation, that exits in the company database. The MessageDataColumns collection represents the columns of the Data tab table of a message.

## Properties (1)
- `Public Property Count() As Long` [R] Specifies the number of columns in the data table.

## Methods (5)
- `Public Function Add() As MessageDataColumn` Adds a column to the data table.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As MessageDataColumn` Returns a reference to an existing item in the collection by its index.
  - param `vtIndex`: Specifies the location of the column in the data table (starts from 0).
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# MessageDataLine (Object)

The MessageDataLine is a child data structure related to the MessageDataColumn. It contains the value of a specified cell in the Data table, which is defined by its column number (vtIndex of Item of MessageDataColumns) and row number (vtIndex of Item of MessageDataLines. Source table: ALR3.

## Properties (3)
- `Public Property Object() As String` [R/W] Sets or returns the object type that is linked to the message. For example, 13 for A/R invoice. Mandatory in case Link (MessageDataColumn) is set to tYES. Field name: ObjType. Length: 20 characters.
- `Public Property ObjectKey() As String` [R/W] Sets or returns the object key that is linked to the message. For example, a document identification key. Mandatory in case Link (MessageDataColumn) is set to tYES. Field name: KeyStr. Length: 254 characters.
- `Public Property Value() As String` [R/W] Sets or returns the value of the cell in the Data table (represented by the column index and line index). Field name: Value. Length: 254 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# MessageDataLines (Collection)

MessageDataLines is a collection of the MessageDataLine data structures.

## Properties (1)
- `Public Property Count() As Long` [R] Retrurns the number of MessageDataLine data structures in the data column.

## Methods (5)
- `Public Function Add() As MessageDataLine` Adds a data structure (Item in the collection) and returns a reference to it (Index starting from 0).
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As MessageDataLine` Returns a reference to an existing item in the collection by its index.
  - param `vtIndex`: Specifies the location of the row in the data column (starts from 0).
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# MessageHeader (Object)

MessageHeader is a data structure related to the MessagesService. The data is stored temporarily in the memory in a virtual table (at a later stage, the data is stored in the OAOB and OAIB tables). Source tables: - OAOB (Message Sent). - OAIB (Received Alerts).

## Properties (7)
- `Public Property Code() As Long` [R/W] Sets or returns the message key. Field name: AlertCode.
- `Public Property Read() As BoYesNoEnum` [R] Determines whether or not the message was read by the recipient (see OAIB table). Field name: WasRead.
- `Public Property Received() As BoYesNoEnum` [R] Determines whether or not the message was opened by the recipient (see OAIB table). Field name: Opened.
- `Public Property ReceivedDate() As Date` [R] Returns the received date (see OAIB table). Field name: RecDate.
- `Public Property ReceivedTime() As Date` [R] Returns the received time (see OAIB table). Field name: RecTime.
- `Public Property SentDate() As Date` [R] Returns the sent date (see OAOB table). Field name: SendDate.
- `Public Property SentTime() As Date` [R] Returns the sent time (see OAOB table). Field name: SendTime.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# MessageHeaders (Collection)

MessageHeaders is a collection of MessageHeader.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of MessageHeader in the collection. Returns the number of GLAccount data structures in the collection.

## Methods (5)
- `Public Function Add() As MessageHeader` Adds a data structure (Item in the collection) and returns a reference to it (Index starting from 0).
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As MessageHeader` Returns a reference to an existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the new item, which was added to the collection.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# Messages (Object)

Messages is a business object that represents the messages in the Administration module. This object enables you to send messages through SAP Business One messaging service. You can use the MessagesService, which enables more functions than the Messages object. Source table: OALR.

**Remarks:** To display the form in the application: - From the main menu bar, select File --> Send --> Send Message.

## Properties (6)
- `Public Property AttachmentEntry() As Long` [R/W] Sets or returns the identification key of the attachment file, as assigned by SAP Business One when adding an Attachment Entry to alert message. Field name: AtcEntry.
- `Public Property Attachments() As Attachments` [R] Returns the Attachments object.
- `Public Property MessageText() As String` [R/W] Sets or returns a memo type string that specifies the message text. Field name: MsgData. Length: 64,000 characters.
- `Public Property Priority() As BoMsgPriorities` [R/W] Sets or returns a valid value that determines the message priority. Field name: ).
- `Public Property Recipients() As Recipients` [R] Returns a Recipients object, which specifies the recipients of this message.
- `Public Property Subject() As String` [R/W] Sets or returns the message subject. Field name: Subject. Length: 50 characters.

## Methods (2)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Sub AddDataColumn(ByVal Title As String, ByVal Text As String, ByVal Object As BoObjectTypes, ByVal ObjectKey As String)` Links a business object to your message.
  - param `Title`: Specifies the column title.
  - param `Text`: Specifies column description.
  - param `Object`: one of the enumeration's values (see the enum file)
  - param `ObjectKey`: Specifies the object key.
  - enum: `BoObjectTypes` in `../enums/enums-01.md`

# MessagesService (Object)

This service enables to manage the Inbox and Outbox messages, and to send messages.

**Remarks:** To use the service: - Connect to a valid company. - Call the CompanyService, which is the main DI service that you must call before using any other service. - Call the method GetBusinessService for the required service. - Create an empty data structure related to the required service. - or- You can create a data structure from an XML file or XML string. - Set the required properties of the specified data structure. - Call the required service method.

## Methods (8)
- `Public Function GetDataInterface(ByVal enumMSDI As MessagesServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `MessagesServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - example note: This is a VB.NET sample that shows how to get a Message Inbox from an existing XML file.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oMessageService As MessagesService

    Dim oMessageInbox As MessageHeaders

    Dim oInboxFromFile As MessageHeaders

    Dim oInboxFromString As MessageHeaders

    Dim oMessageHeader As MessageHeader

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get msg service

    oMessageService = oCmpSrv.GetBusinessService(ServiceTypes.MessagesService)

    'get message inbox

    oMessageInbox = oMessageService.GetInbox

    'save inbox to file

    oMessageInbox.ToXMLFile("c:\MyInbox.xml")

    'create a new inbox data structure and fill it with the data from

    'the xml file

    oInboxFromFile = oMessageService.GetDataInterfaceFromXMLFile("c:\MyInbox.xml")

    'get first message header

    oMessageHeader = oInboxFromFile.Item(0)
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates a data structure from a specified XML string.
  - param `bstrXMLString`: XML string.
  - example note: This is a VB.NET sample that shows how to get a Message Inbox from an existing XMLstring.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oMessageService As MessagesService

    Dim oMessageInbox As MessageHeaders

    Dim sInboxXmlString As String

    Dim oInboxFromString As MessageHeaders

    Dim oMessageHeader As MessageHeader

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get msg service

    oMessageService = oCmpSrv.GetBusinessService(ServiceTypes.MessagesService)

    'get inbox

    oMessageInbox = oMessageService.GetInbox

    'retrieve the inbox as xml string

    sInboxXmlString = oMessageInbox.ToXMLString

    'create a new inbox data structure and fill it with the data from

    'the xml string

    oInboxFromString = oMessageService.GetDataInterfaceFromXMLString(sInboxXmlString)

    'get first message header

    oMessageHeader = oInboxFromString.Item(0)
    ```
- `Public Function GetInbox() As MessageHeaders` Retrieves the Inbox messages.
  - example note: The following is a VB.NET sample that retrieves the Inbox messages (similar to the Messages Overview in the application).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oMessageService As MessagesService

    Dim oUserInbox As MessageHeaders

    Dim oMessageHeader As MessageHeader

    Dim oMessage As Message

    Dim sUserCode As String

    Dim iAttachment As integer

    Dim sSubject As string

    Dim sReceivedDate As String

    Dim eReadMail As BoYesNoEnum

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get msg service

    oMessageService = oCmpSrv.GetBusinessService(ServiceTypes.MessagesService)

    'get inbox

    oUserInbox = oMessageService.GetInbox

    'get first message header

    oMessageHeader = oUserInbox.Item(0)

    'get the first message

    oMessage = oMessageService.GetMessage(oMessageHeader)

    'get subject

    sSubject=oMessage.Subject

    'get Date

    sReceivedDate=oMessageHeader.ReceivedDate

    'get the user's code

    sUserCode =oMessage.User

    'get read confirmation

    eReadMail=oMessageHeader.Read

    'get attachement code key

    iAttachment = oMessage.Attachment
    ```
- `Public Function GetMessage(ByVal pMessageHeader As MessageHeader) As Message` Retrieves a message by its header.
  - param `pMessageHeader`: Message Header input.
- `Public Function GetOutbox() As MessageHeaders` Retrieves the Outbox messages.
  - example note: The following is a VB.NET sample that retrievs the Outbox messages (similar to the Messages Overview in the application).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oMessageService As MessagesService

    Dim oUserOutbox As MessageHeaders

    Dim oMessageHeader As MessageHeader

    Dim oMessage As Message

    Dim iAttachment As Integer

    Dim sSubject As string

    Dim sDate As String

    Dim sTime As String

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get msg service

    oMessageService =         oCmpSrv.GetBusinessService(ServiceTypes.MessagesService)

    'get inbox

    oUserOutbox = oMessageService.GetOutbox

    'get first message header

    oMessageHeader = oUserOutbox.Item(0)

    'get the first message

    oMessage = oMessageService.GetMessage(oMessageHeader)

    'get subject

    sSubject=oMessage.Subject

    'get Date

    sDate= oMessageHeader.SentDate.ToShortDateString

    'get Time

    sTime= oMessageHeader.SentTime.ToShortTimeString

    'get attachement code key

    iAttachment = oMessage.Attachment
    ```
- `Public Function GetSentMessages() As MessageHeaders` Retrieves the Sent messages.
  - example note: The following is a VB.NET sample that retrievs the Sent messages (similar to the Message Overview in the application).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oMessageService As MessagesService

    Dim oUserSendMsgs As MessageHeaders

    Dim oMessageHeader As MessageHeader

    Dim oMessage As Message

    Dim iAttachment As Integer

    Dim sSubject As string

    Dim sDate As String

    Dim sTime As String

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get msg service

    oMessageService =         oCmpSrv.GetBusinessService(ServiceTypes.MessagesService)

    'get Sent Messages

    oUserSendMsgs = oMessageService.GetSentMessages

    'get first message header

    oMessageHeader = oUserSendMsgs.Item(0)

    'get the first message

    oMessage = oMessageService.GetMessage(oMessageHeader)

    'get subject

    sSubject=oMessage.Subject

    'get Date

    sDate= oMessageHeader.SentDate.ToShortDateString

    'get Time

    sTime= oMessageHeader.SentTime.ToShortTimeString

    'get attachement code key

    iAttachment = oMessage.Attachment
    ```
- `Public Function SendMessage(ByVal pMessage As Message) As MessageHeader` Sends a specified message and returns its header.
  - param `pMessage`: Message input.
  - example note: The following is a VB.NET sample that enables to send an internal message with a single line.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oMessageService As MessagesService

    Dim oMessage As Message

    Dim pMessageDataColumns As MessageDataColumns

    Dim pMessageDataColumn As MessageDataColumn

    Dim oLines As MessageDataLines

    Dim oLine As MessageDataLine

    Dim oRecipientCollection As RecipientCollection

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get msg service

    oMessageService = oCmpSrv.GetBusinessService(ServiceTypes.MessagesService)

    'get the data interface for the new message

    oMessage=oMessageService.GetDataInterface(MessagesServiceDataInterface.msdiMessage)

    'fill subject

    oMessage.Subject = "My Subject"

    'fill text

    oMessage.Text = "My Text"

    'Add Recipient

    oRecipientCollection = oMessage.RecipientCollection

    'Add new a recipient

    oRecipientCollection.Add()

    'send internal message

    oRecipientCollection.Item(0).SendInternal = BoYesNoEnum.tYES

    'add existing user code

    oRecipientCollection.Item(0).UserCode = "manager"

    'get columns data

    pMessageDataColumns = oMessage.MessageDataColumns

    'get column

    pMessageDataColumn = pMessageDataColumns.Add()

    'set column name

    pMessageDataColumn.ColumnName = "My Column Name"

    'get lines

    oLines = pMessageDataColumn.MessageDataLines()

    'add new line

    oLine = oLines.Add()

    'set the line value

    oLine.Value = "My Value"

    'send the message

    oMessageService.SendMessage(oMessage)
    ```

# MobileAddOnSetting (Object)

MobileAddOnSetting Class

## Properties (11)
- `Public Property B1MobileApp() As BoYesNoEnum` [R/W] property B1MobileApp
- `Public Property B1SalesApp() As BoYesNoEnum` [R/W] property B1SalesApp
- `Public Property B1ServiceApp() As BoYesNoEnum` [R/W] property B1ServiceApp
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R/W] property Description
- `Public Property Enable() As BoYesNoEnum` [R/W] property Enable
- `Public Property LogonMethod() As LogonMethodEnum` [R/W] property LogonMethod
- `Public Property Provider() As String` [R/W] property Provider
- `Public Property Type() As MobileAddonSettingTypeEnum` [R/W] property Type
- `Public Property Url() As String` [R/W] property Url
- `Public Property ViewStyle() As ViewStyleTypeEnum` [R/W] property ViewStyle

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# MobileAddOnSettingParams (Object)

MobileAddOnSettingParams Class

## Properties (2)
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R] property Description

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# MobileAddOnSettingParamsCollection (Collection)

MobileAddOnSettingParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As MobileAddOnSettingParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As MobileAddOnSettingParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# MobileAddOnSettingService (Object)

MobileAddOnSettingService Class

## Methods (8)
- `Public Function AddMobileAddOnSetting(ByVal pIMobileAddOnSetting As MobileAddOnSetting) As MobileAddOnSettingParams` AddMobileAddOnSetting
  - param `pIMobileAddOnSetting`: 
- `Public Sub DeleteMobileAddOnSetting(ByVal pIMobileAddOnSettingParams As MobileAddOnSettingParams)` DeleteMobileAddOnSetting
  - param `pIMobileAddOnSettingParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As MobileAddOnSettingServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `MobileAddOnSettingServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetMobileAddOnSetting(ByVal pIMobileAddOnSettingParams As MobileAddOnSettingParams) As MobileAddOnSetting` GetMobileAddOnSetting
  - param `pIMobileAddOnSettingParams`: 
- `Public Function GetMobileAddOnSettingList() As MobileAddOnSettingParamsCollection` GetMobileAddOnSettingList
- `Public Sub UpdateMobileAddOnSetting(ByVal pIMobileAddOnSetting As MobileAddOnSetting)` UpdateMobileAddOnSetting
  - param `pIMobileAddOnSetting`: 

# MobileAppService (Object)

MobileAppService Class

## Methods (17)
- `Public Function GetCurrentServerDateTime() As MobileServerDateTime` GetCurrentServerDateTime
- `Public Function GetDataInterface(ByVal enumMSDI As MobileAppServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `MobileAppServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetDppChangeParams(ByVal pDppChangeParams As DppChangeParams) As DppChangeParams` GetDppChangeParams
  - param `pDppChangeParams`: 
- `Public Function GetEmployeeFullNames(ByVal pEmployeeFullNamesParamsCollection As EmployeeFullNamesParamsCollection) As EmployeeFullNamesParamsCollection` GetFullEmployeeNames
  - param `pEmployeeFullNamesParamsCollection`: 
- `Public Function GetSalesAppSetting(ByVal pSalesAppSettingParams As SalesAppSettingParams) As SalesAppSetting` GetSalesAppSetting
  - param `pSalesAppSettingParams`: 
- `Public Function GetServiceAppReport(ByVal pServiceAppReportParams As ServiceAppReportParams) As ServiceAppReport` GetServiceAppReport
  - param `pServiceAppReportParams`: 
- `Public Function GetServiceAppReportContent(ByVal pServiceAppReportParams As ServiceAppReportParams) As ServiceAppReportContent` GetServiceAppReportContent
  - param `pServiceAppReportParams`: 
- `Public Function GetTechnicianSchedulings(ByVal pITechnicianSchedulingsParams As TechnicianSchedulingsParams) As TechnicianSchedulingsCollection` GetTechnicianSchedulings
  - param `pITechnicianSchedulingsParams`: 
- `Public Function GetTechnicianSettings(ByVal pTechnicianSettingsParams As TechnicianSettingsParams) As TechnicianSettings` GetTechnicianSettings
  - param `pTechnicianSettingsParams`: 
- `Public Function GetTechnicianSettingsGroup(ByVal pTechnicianSettingsGroupParams As TechnicianSettingsGroupParams) As TechnicianSettingsGroup` GetTechnicianSettingsGroup
  - param `pTechnicianSettingsGroupParams`: 
- `Public Sub UpdateSalesAppSetting(ByVal pSalesAppSetting As SalesAppSetting)` UpdateSalesAppSetting
  - param `pSalesAppSetting`: 
- `Public Sub UpdateServiceAppReport(ByVal pServiceAppReport As ServiceAppReport)` UpdateServiceAppReport
  - param `pServiceAppReport`: 
- `Public Sub UpdateServiceAppReportContent(ByVal pServiceAppReportParams As ServiceAppReportParams, ByVal pServiceAppReportContent As ServiceAppReportContent)` UpdateServiceAppReportContent
  - param `pServiceAppReportParams`: 
  - param `pServiceAppReportContent`: 
- `Public Sub UpdateTechnicianSettings(ByVal ppTechnicianSettings As TechnicianSettings)` UpdateTechnicianSettings
  - param `ppTechnicianSettings`: 
- `Public Sub UpdateTechnicianSettingsGroup(ByVal pTechnicianSettingsGroup As TechnicianSettingsGroup)` UpdateTechnicianSettingsGroup
  - param `pTechnicianSettingsGroup`: 

# MobileServerDateTime (Object)

MobileServerDateTime Class

## Properties (2)
- `Public Property Date() As Date` [R] property Date
- `Public Property Time() As Date` [R] property Time

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# MultiLanguageTranslations (Object)

The MultiLanguageTranslation object enables to translate alphanumeric data of specified fields in master data objects (such as, BusinessPartners and Items) to foreign languages and then print documents in the translated language. This functionality is used by companies that trade with foreign business partners that require docouments in their language. Source table: OMLT.

**Remarks:** Prerequisites: - Set MultiLanguageSupportEnable (AdminInfo) to tYES. - Set the UserLanguages object with the required foreign language. - Set LanguageCode (BusinessPartners) to the requied foreign language. To display the form in the application: - Open a master data window (e.g. Business Partner Master Data). - From the menu bar, select View --> Translatable Fields. A globe icon appears next to fields that can be translated. - Click a field for translation and then from the menu bar, select Goto --> Translate.

## Properties (7)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property FieldAlias() As String` [R/W] Sets or returns the field name for which the translation in user language applies. Field name: FieldAlias. Length: 10 characters.
- `Public Property Numerator() As Long` [R] Returns the key (numerator) of the translated field value as assigned by the system when adding a translation to a field value. Field name: TranEntry.
- `Public Property PrimaryKeyofobject() As String` [R/W] Sets or returns the primary key of the object for which the translation in user language applies. For example: CardCode value of a business partner; ItemCode value of an item. Field name: PK. Length: 254 characters.
- `Public Property TableName() As String` [R/W] Sets or returns the table name (e.g. OCRD and OITM) for which the translation in user language applies. Field name: TableName. Length: 20 characters.
- `Public Property TranslationsInUserLanguages() As TranslationsInUserLanguages` [R] Returns the TranslationsInUserLanguages child object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` method Add
  - remarks: Adds a translation for a specified field.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lAbsEntry As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lAbsEntry`: Numerator.
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

# MultiplePayment (Object)

A data structure related to BankStatementService holding properties for a multiple payment on a bank statement line. Source table: BNK1.

## Properties (6)
- `Public Property AmountFC() As Double` [R/W] Sets or returns the payment amount in foriegn currency. Field name: AmntFC.
- `Public Property AmountLC() As Double` [R/W] Sets or returns the payment amount in local currency. Field name: AmntLC.
- `Public Property BankStatmentLineID() As Long` [R] Returns the ID number of the bank statement line connected with the payment. Field name: BSLine.
- `Public Property DocumentIdentifier() As String` [R/W] Sets or returns the ID number of the bank statement document. Field name: DocID.
- `Public Property IsDebit() As BoYesNoEnum` [R/W] Sets or returns a boolean value specifying whether the payment is credit amount or debit amount. Field name: IsDebit.
- `Public Property ListLineID() As Long` [R] Returns the ID number of the payment line. Field name: ListLineID.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# MultiplePayments (Collection)

A data collection of MultiplePayment objects related to the BankStatementService.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As MultiplePayment` Adds an object to the collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As MultiplePayment` Returns reference by index to existing multiple payment in the collection.
  - param `vtIndex`: Specifies the index of the multiple payment you want to get.
- `Public Sub Remove(ByVal vtIndex As Variant)` Deletes the specified record from the data collection.
  - param `vtIndex`: Specifies the index of the record. Specifies the index of the record.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML file.
- `Public Function ToXMLString() As String` Creates XML string that represents the object data.

# NatureOfAssessee (Object)

Represents a type of assessee in order to determine the tax rate for TDS (withholding tax). Source table: ONOA Mandatory properties: Code, Description

**Remarks:** For India only. Mandatory properties: Code, Description

## Properties (4)
- `Public Property AbsEntry() As Long` [R] The nature of assessee key. Field name: AbsID
- `Public Property AssesseeType() As AssesseeTypeEnum` [R/W] The nature of assessee type, either C (Company) or P (Other). The default is C. Field name: AsseType
- `Public Property Code() As String` [R/W] The nature of assessee code. Field name: Code
- `Public Property Description() As String` [R/W] A description for the nature of assessee. Field name: Descr

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# NatureOfAssesseeParams (Object)

Holds the key and code to an existing assessee type. This object is used to pass keys to and retrieve keys from NatureOfAssesseesService methods.

## Properties (3)
- `Public Property AbsEntry() As Long` [R/W] The nature of assessee key. Field name: AbsID
- `Public Property Code() As String` [R] The nature of assessee code. Field name: Code
- `Public Property Description() As String` [R] A description for the nature of assessee. Field name: Descr

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# NatureOfAssesseesParams (Collection)

A collection of NatureOfAssesseeParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As NatureOfAssesseeParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As NatureOfAssesseeParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# NatureOfAssesseesService (Object)

The NatureOfAssesseesService service enables you to add, look up and remove nature of assessees in the nature of assessee master data table. Nature of assessees are used to specify a type of entity subject to TDS (withholding tax). Source table: ONOA

**Remarks:** For India only.

## Methods (8)
- `Public Function AddNatureOfAssessee(ByVal pINatureOfAssessee As NatureOfAssessee) As NatureOfAssesseeParams` Adds a nature of assessee.
  - param `pINatureOfAssessee`: The data for the new nature of assessee.
  - returns: Contains the key (AbsId) of the new nature of assessee.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SAPbobsCOM.NatureOfAssessee oNOA = (SAPbobsCOM.NatureOfAssessee)oNASrv.GetDataInterface(NatureOfAssesseesServiceDataInterfaces.noasNatureOfAssessee);
        oNOA.Code = "COM";
        oNOA.Description = "Company";
        oNOA.AssesseeType = AssesseeTypeEnum.atCompany;
        oNASrv.AddNatureOfAssessee(oNOA);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Sub DeleteNatureOfAssessee(ByVal pINatureOfAssesseeParams As NatureOfAssesseeParams)` Deletes an existing nature of assessee. The nature of assessee is specified by its key (AbsId), which is contained in the NatureOfAssesseeParams object passed to the method.
  - param `pINatureOfAssesseeParams`: The key of the nature of assessee to be deleted.
  - remarks: You cannot delete a nature of assessee that is associated with a withholding tax code (WithholdingTaxCodes).
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SAPbobsCOM.NatureOfAssesseeParams oNOAParams = (SAPbobsCOM.NatureOfAssesseeParams)oNASrv.GetDataInterface(NatureOfAssesseesServiceDataInterfaces.noasNatureOfAssesseeParams);
        oNOAParams.AbsEntry = 1;
        oNASrv.DeleteNatureOfAssessee(oNOAParams);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As NatureOfAssesseesServiceDataInterfaces) As Object` Creates an empty data structure for use with the NatureOfAssesseesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `NatureOfAssesseesServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLFile(Hashtable Properties, String Path)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair In Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        oGeneralData.ToXMLFile(Path);

        //Retrieve XML and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLFile(Path);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLString(Hashtable Properties)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;
        string XMLString;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair in Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        XMLString = oGeneralData.ToXMLString();

        //Retrieve XML string and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLString(XMLString);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetNatureOfAssessee(ByVal pINatureOfAssesseeParams As NatureOfAssesseeParams) As NatureOfAssessee` Retrieves a nature of assessee. The nature of assessee is specified by its key (AbsId), which is contained in the NatureOfAssesseeParams object passed to the method.
  - param `pINatureOfAssesseeParams`: The key of the nature of assessee to retrieve.
  - returns: The nature of assessee with the specified key.
- `Public Function GetNatureOfAssesseeList() As NatureOfAssesseesParams` Retrieves the keys and codes of all nature of assessees.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SAPbobsCOM.NatureOfAssesseesParams oNAList = oNASrv.GetNatureOfAssesseeList();
        String result = "";
        foreach(SAPbobsCOM.NatureOfAssesseeParams oNAPar in oNAList)
        {
            result = oNAPar.Code + " " + oNAPar.Description + "\n";
        }
        Interaction.MsgBox(result, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Sub UpdateNatureOfAssessee(ByVal pINatureOfAssessee As NatureOfAssessee)` Updates an existing nature of assessee. The data for the nature of assessee, including the key of the nature of assessee to be updated, is contained in the NatureOfAssessee passed to the method. To update a nature of assessee, you must first retrieve it using the GetNatureOfAssessee method.
  - param `pINatureOfAssessee`: The data for the nature of assessee to be updated. The NatureOfAssessee object must contain the key of the object to be updated.
  - remarks: If the nature of assessee is associated with a withholding tax code (WithholdingTaxCodes), you cannot update the Code and AssesseeType properties.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SAPbobsCOM.NatureOfAssesseeParams oNOAParams = (SAPbobsCOM.NatureOfAssesseeParams)oNASrv.GetDataInterface(NatureOfAssesseesServiceDataInterfaces.noasNatureOfAssesseeParams);
        oNOAParams.AbsEntry = 1;

        SAPbobsCOM.NatureOfAssessee oNOA = oNASrv.GetNatureOfAssessee(oNOAParams);
        oNOA.Description = "Updated";
        oNASrv.UpdateNatureOfAssessee(oNOA);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```

# NCMCodeSetup (Object)

Represents an NCM code that can be assigned to an item. Source table: ONCM Mandatory properties: NCMCode, Description

**Remarks:** Relevant for Brazil only.

## Properties (4)
- `Public Property AbsEntry() As Long` [R] The key for a specific NCM code. Field name: AbsEntry
- `Public Property Description() As String` [R/W] A description for the NCM code. Field name: Descrip
  - remarks: Cannot be blank.
- `Public Property GroupCode() As String` [R/W] property GroupCode
- `Public Property NCMCode() As String` [R/W] The NCM code. Field name: NcmCode
  - remarks: Cannot be blank.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# NCMCodeSetupParams (Object)

Holds the key and name to an existing NCM code. This object is used to pass keys to and retrieve keys from NCMCodesSetupService methods.

## Properties (3)
- `Public Property AbsEntry() As Long` [R/W] The key for a specific NCM code. Field name: AbsEntry
- `Public Property Description() As String` [R] A description for the NCM code. Field name: Descrip
- `Public Property NCMCode() As String` [R] The NCM code. Field name: NcmCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# NCMCodeSetupParamsCollection (Collection)

A collection of NCMCodeSetupParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As NCMCodeSetupParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As NCMCodeSetupParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# NCMCodesSetupService (Object)

The NCMCodesSetupService service enables you to add, look up and remove NCM codes in the NCM codes master data table. NCM codes can be assigned to items via the NCMCode field of the Items object. To see the list of NCM codes, select Inventory --> Item Master Data, and select an item. In the NCM Code field, select Define New. Source table: ONCM

**Remarks:** Relevant for Brazil only.

## Methods (8)
- `Public Function AddNCMCodeSetup(ByVal pINCMCodeSetup As NCMCodeSetup) As NCMCodeSetupParams` Adds an NCM code.
  - param `pINCMCodeSetup`: The data for the new NCM code.
  - returns: Contains the key (AbsEntry) of the new NCM code.
  - C# example (from SAP's help):
    ```csharp
    NCMCodesSetupService oNCMSrv;
    oNCMSrv = (NCMCodesSetupService)(MainModule.oCmpSrv.GetBusinessService(ServiceTypes.NCMCodesSetupService));

    SAPbobsCOM.NCMCodeSetup addLine;
    addLine = (SAPbobsCOM.NCMCodeSetup)oNCMSrv.GetDataInterface(NCMCodesSetupServiceDataInterfaces.ncmcssNCMCodeSetup);
    addLine.NCMCode = "C1";
    addLine.Description = "Desc C1";

    oNCMSrv.AddNCMCodeSetup(addLine);
    ```
- `Public Sub DeleteNCMCodeSetup(ByVal pINCMCodeSetupParams As NCMCodeSetupParams)` Deletes an existing NCM code. The NCM code is specified by its key (AbsEntry), which is contained in the NCMCodeSetupParams object passed to the method.
  - param `pINCMCodeSetupParams`: The key of the NCM code to be deleted.
  - remarks: You cannot delete an NCM code that is associated with a DNF code, an item, or an item group.
  - C# example (from SAP's help):
    ```csharp
    NCMCodeSetupParams delLine;

    delLine.AbsEntry = 1234;
    oNCMSrv.DeleteNCMCodeSetup(delLine);
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As NCMCodesSetupServiceDataInterfaces) As Object` Creates an empty data structure for use with the NCMCodesSetupService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `NCMCodesSetupServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLFile(Hashtable Properties, String Path)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair In Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        oGeneralData.ToXMLFile(Path);

        //Retrieve XML and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLFile(Path);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLString(Hashtable Properties)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;
        string XMLString;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair in Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        XMLString = oGeneralData.ToXMLString();

        //Retrieve XML string and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLString(XMLString);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetNCMCodeSetup(ByVal pINCMCodeSetupParams As NCMCodeSetupParams) As NCMCodeSetup` Retrieves an NCM code. The NCM code is specified by its key (AbsEntry), which is contained in the NCMCodeSetupParams object passed to the method.
  - param `pINCMCodeSetupParams`: The key of the NCM code to retrieve.
  - returns: The NCM code with the specified key.
- `Public Function GetNCMCodeSetupList() As NCMCodeSetupParamsCollection` Retrieves the keys and names of all the NCM codes.
  - C# example (from SAP's help):
    ```csharp
    NCMCodeSetupParamsCollection getlistParams;
    getlistParams = oNCMSrv.GetNCMCodeSetupList();

    String resultSet = "";

    foreach (NCMCodeSetupParams record in getlistParams)
    {
        resultSet = resultSet + record.NCMCode + "\t" + record.Description + "\n";
        if (record.AbsEntry >= 10)
            break;
    }
    ```
- `Public Sub UpdateNCMCodeSetup(ByVal pINCMCodeSetup As NCMCodeSetup)` Updates an existing NCM code. The data for the NCM code, including the key of the NCM code to be updated, is contained in the NCMCodeSetup object passed to the method. To update a NCM code, you must first retrieve it using the GetNCMCodeSetup method.
  - param `pINCMCodeSetup`: The data for the competitor to be updated. The SalesOpportunityCompetitorSetup object must contain the key of the object to be updated.
  - remarks: You cannot update an NCM code that is associated with a DNF code, an item, or an item group.
  - C# example (from SAP's help):
    ```csharp
    NCMCodeSetupParams getLine;
    SAPbobsCOM.NCMCodeSetup updateLine;
    getLine = (NCMCodeSetupParams)oNCMSrv.GetDataInterface(NCMCodesSetupServiceDataInterfaces.ncmcssNCMCodeSetupParams);

    getLine.AbsEntry = 9789;

    updateLine = oNCMSrv.GetNCMCodeSetup(getLine);
    updateLine.NCMCode = "updated";
    updateLine.Description = "updated description";

    oNCMSrv.UpdateNCMCodeSetup(updateLine);
    ```

# NFModel (Object)

NFModel Class

## Properties (4)
- `Public Property AbsEntry() As String` [R] property AbsEntry
- `Public Property NFMCode() As String` [R/W] property NFMCode
- `Public Property NFMDescription() As String` [R/W] property NFMDescription
- `Public Property NFMName() As String` [R/W] property NFMName

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# NFModelParams (Object)

NFModelParams Class

## Properties (4)
- `Public Property AbsEntry() As String` [R/W] property AbsEntry
- `Public Property NFMCode() As String` [R] property NFMCode
- `Public Property NFMDescription() As String` [R] property NFMDescription
- `Public Property NFMName() As String` [R] property NFMName

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# NFModelsParams (Collection)

NFModelsParams Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As NFModelParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As NFModelParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# NFModelsService (Object)

NFModelsService Class

## Methods (8)
- `Public Function Add(ByVal pINFModel As NFModel) As NFModelParams` Add
  - param `pINFModel`: 
- `Public Sub Delete(ByVal pINFModelParams As NFModelParams)` Delete
  - param `pINFModelParams`: 
- `Public Function Get(ByVal pINFModelParams As NFModelParams) As NFModel` Get
  - param `pINFModelParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As NFModelsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `NFModelsServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As NFModelsParams` GetList
- `Public Sub Update(ByVal pINFModel As NFModel)` Update
  - param `pINFModel`: 

# NFTaxCategoriesService (Object)

NFTaxCategoriesService Class

## Methods (8)
- `Public Function Add(ByVal pINFTaxCategory As NFTaxCategory) As NFTaxCategoryParams` Add
  - param `pINFTaxCategory`: 
- `Public Sub Delete(ByVal pINFTaxCategoryParams As NFTaxCategoryParams)` Delete
  - param `pINFTaxCategoryParams`: 
- `Public Function Get(ByVal pINFTaxCategoryParams As NFTaxCategoryParams) As NFTaxCategory` Get
  - param `pINFTaxCategoryParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As NFTaxCategoriesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `NFTaxCategoriesServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As NFTaxCategoryParamsCollection` GetList
- `Public Sub Update(ByVal pINFTaxCategory As NFTaxCategory)` Update
  - param `pINFTaxCategory`: 

# NFTaxCategory (Object)

NFTaxCategory Class

## Properties (5)
- `Public Property AbsId() As Long` [R] property AbsId
- `Public Property CESTRelevant() As BoYesNoEnum` [R/W] Tax category is relevant for CEST.
- `Public Property Code() As String` [R/W] property Code
- `Public Property GPCId() As Long` [R/W] property GPCId
- `Public Property Locked() As BoYesNoEnum` [R/W] property Locked

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# NFTaxCategoryParams (Object)

NFTaxCategoryParams Class

## Properties (2)
- `Public Property AbsId() As Long` [R/W] property AbsId
- `Public Property Code() As String` [R/W] property Code

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# NFTaxCategoryParamsCollection (Collection)

NFTaxCategoryParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As NFTaxCategoryParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As NFTaxCategoryParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# NotaFiscalCFOP (Object)

Represents CFOP codes for Nota Fiscal documents. CFOP codes describes the business transaction from the tax authorities' point of view. Source table: OCFP

**Remarks:** For Brazil only. To display the form in the application: - Select Administration > Definitions > Financials > Tax > Nota Fiscal > Define CFOP Code.

## Properties (5)
- `Public Property Application() As String` [R/W] The application name. Length: 16 characters Field name: App
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Code() As String` [R/W] The CFOP code. Field name: Code Length: 6 characters
- `Public Property Description() As String` [R/W] A description for the CFOP code. Field name: Descrip Length: 16 characters
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
- `Public Function GetByKey(ByVal ID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ID`: CFOP ID.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data in XML formatted data to a file.
  - param `FileName`: Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# NotaFiscalCST (Object)

Represents CST codes for Nota Fiscal documents. Source table: OTSC

**Remarks:** For Brazil only. To display the form in the application: - Select Administration > Definitions > Financials > Tax > Nota Fiscal > Define CST Code.

## Properties (7)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Code() As String` [R/W] The CST code. Field name: CODE Length: 4 characters
- `Public Property CSTCodeOutgoing() As String` [R/W] The corresponding outgoing CST code for this CST (incoming) code. The size of the value can be one of the following: 2 characters, if the TaxCategory field is IPI (-4), PIS (-8), or COFINS (-9) 4 characters, if the TaxCategory field is ICMS (-6) 20 characters, if the TaxCategory field is set to any other value Field name: CodeOut
- `Public Property DescriptionOutgoing() As String` [R/W] A description for the outgoing CST code specified in the CSTCodeOutgoing property. Field name: OutDesc
- `Public Property Situation() As String` [R/W] The description or tributary situation. Field name: Situation Length: 16 characters
- `Public Property TaxCategory() As Long` [R/W] The tax category for the CST code. Field name: Category This field is a foreign key to the ONFT table.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
- `Public Function GetByKey(ByVal ID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ID`: CST ID.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# NotaFiscalUsage (Object)

Represents a usage for specifying tax codes for Nota Fiscal documents. Source table: OUSG

**Remarks:** To display the form in the application: - In any marketing document's row, click Usage dropdown list , and click Define New.

## Properties (13)
- `Public Property Adjustment() As BoYesNoEnum` [R/W] Adjustment. Field name: Adjustment.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Description() As String` [R/W] property Description
- `Public Property ID() As Long` [R] The ID for the usage. Field name: ID
- `Public Property IncomingImportCFOPCode() As String` [R/W] property IncomingImportCFOPCode
- `Public Property IncomingInStateCFOPCode() As String` [R/W] property IncomingInStateCFOPCode
- `Public Property IncomingOutStateCFOPCode() As String` [R/W] property IncomingOutStateCFOPCode
- `Public Property OutgoingExportCFOPCode() As String` [R/W] property OutgoingExportCFOPCode
- `Public Property OutgoingInStateCFOPCode() As String` [R/W] property OutgoingInStateCFOPCode
- `Public Property OutgoingOutStateCFOPCode() As String` [R/W] property OutgoingOutStateCFOPCode
- `Public Property ThirdParty() As BoYesNoEnum` [R/W] property ThirdParty
- `Public Property Usage() As String` [R/W] The usage name. Field name: Usage Length: 20 characters
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
- `Public Function GetByKey(ByVal ID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ID`: Usage ID.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes the current record.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# OccurenceCode (Object)

OccurenceCode Class

## Properties (6)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R/W] property Description
- `Public Property IsMovement() As BoYesNoEnum` [R/W] property IsMovement
- `Public Property Note() As String` [R/W] property Note
- `Public Property RequestedBoeStatus() As BoBoeStatus` [R/W] property RequestedBoeStatus

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# OccurenceCodeParams (Object)

OccurenceCodeParams Class

## Properties (6)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R] property Description
- `Public Property IsMovement() As BoYesNoEnum` [R/W] property IsMovement
- `Public Property Note() As String` [R] property Note
- `Public Property RequestedBoeStatus() As BoBoeStatus` [R] property RequestedBoeStatus

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# OccurenceCodeParamsCollection (Collection)

OccurenceCodeParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As OccurenceCodeParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As OccurenceCodeParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# OccurrenceCodesService (Object)

OccurrenceCodesService Class

## Methods (8)
- `Public Function Add(ByVal pIOccurenceCode As OccurenceCode) As OccurenceCodeParams` Add
  - param `pIOccurenceCode`: 
- `Public Sub Delete(ByVal pIOccurenceCodeParams As OccurenceCodeParams)` Delete
  - param `pIOccurenceCodeParams`: 
- `Public Function Get(ByVal pIOccurenceCodeParams As OccurenceCodeParams) As OccurenceCode` Get
  - param `pIOccurenceCodeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As OccurrenceCodesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `OccurrenceCodesServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As OccurenceCodeParamsCollection` GetList
- `Public Sub Update(ByVal pIOccurenceCode As OccurenceCode)` Update
  - param `pIOccurenceCode`: 

# OpenningBalanceAccount (Object)

OpenningBalanceAccount is a data structure related to the AccountsService and BusinessPartnersService. The data is stored temporarily in a virtual table.

**Remarks:** Mandatory property: OpenBalanceAccount. To display the form related to the data structure: - Select Administration --> System Initialization --> Openning Balances --> G/L Accounts Openning Balance. or - Select Administration --> System Initialization --> Openning Balances --> Business Partners Openning Balance.

## Properties (6)
- `Public Property BPLID() As Long` [R/W] property BPLID
- `Public Property Date() As Date` [R/W] Sets or returns the posting date of the journal entry.
- `Public Property Details() As String` [R/W] Sets or returns details about the journal entry. Length: 50 characters.
- `Public Property OpenBalanceAccount() As String` [R/W] Sets or returns the openning balance account code from which to credit or debit G/L accounts or business partner accounts. Mandatory property.
- `Public Property Ref1() As String` [R/W] Sets or returns the first reference code of the journal entry. Length: 11 characters.
- `Public Property Ref2() As String` [R/W] Sets or returns the second reference code of the journal entry. Length: 11 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# OriginalItem (Object)

A data structure object holding properties fo the AlternativeItemService.

## Properties (3)
- `Public Property AlternativeItems() As AlternativeItems` [R] Returns a collection of alternative item instances.
- `Public Property ItemCode() As String` [R/W] Sets or returns a string specifying alternative item unique ID.
- `Public Property ItemName() As String` [R] Sets or returs a string specifying alternative item name.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# OriginalItemParams (Object)

This object holds identification properties for the AlternativeItemsService (ItemCode and ItemName).

## Properties (2)
- `Public Property ItemCode() As String` [R/W] Sets or returns a string specifying alternative item unique ID.
- `Public Property ItemName() As String` [R] Sets or returs a string specifying alternative item name.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# PackagesTypes (Object)

PackagesTypes is a business object that represents the list of package types for deliveries in the Inventory and Production module. This object enables you to: - Add a package type. - Retrieve a package type. - Update a package type. - Remove a package type. - Save the object in XML format. Source table: OPKG.

**Remarks:** From the SAP Business One Main Menu, choose Administration --> Setup --> Inventory --> Package Types.

## Properties (22)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Code() As Long` [R] Returns the package type code (key). Field name: PkgCode.
- `Public Property Height1() As Double` [R/W] The height for the unit. Field name: Height1.
- `Public Property Height1Unit() As Long` [R/W] The height UoM. Field name: Hght1Unit.
- `Public Property Height2() As Double` [R/W] The height for the unit. Field name: Height2.
- `Public Property Height2Unit() As Long` [R/W] The height UoM. Field name: Hght2Unit.
- `Public Property Length1() As Double` [R/W] The length for the unit. Field name: Length1.
- `Public Property Length1Unit() As Long` [R/W] The length UoM. Field name: Len1Unit.
- `Public Property Length2() As Double` [R/W] The length for the unit. Field name: Length2.
- `Public Property Length2Unit() As Long` [R/W] The length UoM. Field name: Len2Unit.
- `Public Property Type() As String` [R/W] Sets or returns the package type name. Field name: PkgType. Mandatory property. Length: 30 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property Volume() As Double` [R/W] The volume for the unit. Field name: Volume.
- `Public Property VolumeUnit() As Long` [R/W] The volume UoM. Field name: VolUnit.
- `Public Property Weight1() As Double` [R/W] The weight for the unit. Field name: Weight1.
- `Public Property Weight1Unit() As Long` [R/W] The weight UoM. Field name: WghtUnit.
- `Public Property Weight2() As Double` [R/W] The weight for the unit. Field name: Weight2.
- `Public Property Weight2Unit() As Long` [R/W] The weight UoM. Field name: Wght2Unit.
- `Public Property Width1() As Double` [R/W] The width for the unit. Field name: Width1.
- `Public Property Width1Unit() As Long` [R/W] The width UoM. Field name: Wdth1Unit.
- `Public Property Width2() As Double` [R/W] The width for the unit. Field name: Width2.
- `Public Property Width2Unit() As Long` [R/W] The width UoM. Field name: Wdth2Unit.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lCode`: Package type code (Code).
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

# PartnersSetup (Object)

Define partners for sales opportunities. Source table: OPRT.

## Properties (5)
- `Public Property DefaultRelationship() As Long` [R/W] The relationship type of the partner. Field name: RelatnType.
- `Public Property Details() As String` [R/W] Enter any additional details regarding the partner. Field name: Memo. Length: 50 characters.
- `Public Property Name() As String` [R/W] The name of the partner. Field name: Name. Length: 15 characters.
- `Public Property PartnerID() As Long` [R] The ID of the business partner. Field name: PrtId.
- `Public Property RelatedBP() As String` [R/W] The related business partner code. Field name: RelatCard. Length: 15 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# PartnersSetupParams (Object)

Holds the key to an existing partner. This object is used to pass keys to and retrieve keys from PartnersSetupsService methods.

## Properties (5)
- `Public Property DefaultRelationship() As Long` [R] The relationship type of the partner. Field name: RelatnType.
- `Public Property Details() As String` [R] Enter any additional details regarding the partner. Field name: Memo. Length: 50 characters.
- `Public Property Name() As String` [R] The name of the partner. Field name: Name. Length: 15 characters.
- `Public Property PartnerID() As Long` [R/W] The code of the partner. Field name: PrtId.
- `Public Property RelatedBP() As String` [R] The related business partner code. Field name: RelatCard. Length: 15 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# PartnersSetupsParams (Collection)

A collection of PartnersSetupParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As PartnersSetupParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As PartnersSetupParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

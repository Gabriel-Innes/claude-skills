<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# CustomsGroups (Object)

The CustomsGroups object enables to define custom groups, which specify the customs duty for items purchased abroad that are liable for customs. Source table: OARG.

**Remarks:** To display the form in the application: - Select Administration -->Setup -->Inventory -->Customs Groups.

## Properties (14)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Code() As Long` [R] Returns the key of the customs group as assigned by the system when adding a customs group. Field name: CstGrpCode.
- `Public Property Customs() As Double` [R/W] Sets or returns the customs percentage. Field name: Custom.
- `Public Property CustomsAllocationAccount() As String` [R/W] The account to which the customs duty can be allocated. Field name: cstAllcAcc. Length: 15 characters.
- `Public Property CustomsExpenseAccount() As String` [R/W] The account to which the customs expenses can be posted. Field name: cstExpAcc. Length: 15 characters.
- `Public Property Locked() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum that determines wether or not the Custom Group is locked. Field name: Locked..
- `Public Property Name() As String` [R/W] Sets or returns the customs group name. Field name: CstGrpName. Length: 20 characters.
- `Public Property Number() As String` [R/W] Sets or returns the customs group number. Field name: GroupNum. Length: 20 characters.
- `Public Property Other() As Double` [R/W] Sets or returns the additional tax percentage. Field name: OtherTax.
- `Public Property PortAddress() As String` [R/W] property PortAddress
- `Public Property PortState() As String` [R/W] property PortState
- `Public Property Purchase() As Double` [R/W] Sets or returns the purchase tax percentage. Field name: BuyTax.
- `Public Property Total() As Double` [R/W] Sets or returns the total tax percentage. Field name: TotalTax.
  - remarks: The system calculates the total custom percentage for the customs group, based on Customs, Purchase, Other.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a customs group.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lGroupCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lGroupCode`: Code.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
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

# CycleCountDetermination (Object)

CycleCountDetermination Class

## Properties (3)
- `Public Property CycleBy() As CycleCountDeterminationCycleByEnum` [R/W] Specifies the warehouse sublevel or item group for cycle counting. Field name: CycleBy.
  - remarks: You may not update both the CycleBy Property and CycleCountDeterminationSetup of the same transaction. This means that when updating these two settings in one transaction, the CycleCountDeterminationSetup changes will (by default) be ignored and the CycleBy Property changes will take effect.
- `Public Property CycleCountDeterminationSetupCollection() As CycleCountDeterminationSetupCollection` [R] property CycleCountDeterminationSetupCollection
- `Public Property WarehouseCode() As String` [R/W] The code of a warehouse. Field name: WhsCode.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# CycleCountDeterminationParams (Object)

CycleCountDeterminationParams Class

## Properties (2)
- `Public Property CycleBy() As Long` [R] Specifies the warehouse sublevel or item group for cycle counting. Field name: CycleBy.
- `Public Property WarehouseCode() As String` [R/W] Sets or returns the warehouse code where the item is stored. Field name: WhsCode. Length: 8 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# CycleCountDeterminationParamsCollection (Collection)

CycleCountDeterminationParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As CycleCountDeterminationParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As CycleCountDeterminationParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# CycleCountDeterminationSetup (Object)

This object enables setting up cycle count determination.

## Properties (9)
- `Public Property Alert() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not to activate alert. Field name: Alert.
- `Public Property ChangeExistingItems() As BoYesNoEnum` [R/W] Changes existing items for cycle count determination. Field name: ChangeExist.
- `Public Property CycleCode() As Long` [R/W] Sets or returns the cycle code. Field name: CycleCode.
- `Public Property DestinationUser() As Long` [R/W] Sets or returns the destination user. Field name: DestUser. This is a foreign key to the Users object.
- `Public Property Entry() As Long` [R/W] If the CycleBy Property specified is a warehouse sublevel, the Entry property will be a foreign key to the WarehouseSublevelCode object. If the CycleBy Property specified is an item group, the Entry property will be a foreign key to the ItemGroups object. Field name: Entry.
- `Public Property ExcludeItemsWithZeroQuantity() As BoYesNoEnum` [R/W] Excludes items of zero quantity. Field name: ExcldZrQty.
  - remarks: This property is valid only when the CycleBy Property specified is a warehouse sublevel.
- `Public Property NextCountingDate() As Date` [R] Sets or returns the date of the upcoming inventory cycle. Field name: NextDate.
  - remarks: This property is valid only when the CycleBy Property specified is a warehouse sublevel.
- `Public Property Time() As Date` [R] Sets or returns the time of the upcoming inventory cycle. Field name: Time.
  - remarks: This property is valid only when the CycleBy Property specified is a warehouse sublevel.
- `Public Property WarehouseCode() As String` [R/W] Sets or returns the code of the warehouse where the item is stored. Field name: WhsCode. Length: 8 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# CycleCountDeterminationSetupCollection (Collection)

CycleCountDeterminationSetupCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As CycleCountDeterminationSetup` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As CycleCountDeterminationSetup` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# CycleCountDeterminationsService (Object)

You can setup cycle count determinations via this service. Menu entry: Administration > Setup -> Inventory -> Cycle Count Determination

## Methods (6)
- `Public Function Get(ByVal pICycleCountDeterminationParams As CycleCountDeterminationParams) As CycleCountDetermination` Retrieves a CycleCountDetermination rule.
  - param `pICycleCountDeterminationParams`: 
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetDataInterface(ByVal enumMSDI As CycleCountDeterminationsServiceDataInterfaces) As Object` Creates an empty data structure for use with the CycleCountDeterminationsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `CycleCountDeterminationsServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Retrieves the Data Interface from XML file.
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates data structure from specified XML string.
  - param `bstrXMLString`: 
- `Public Function GetList() As CycleCountDeterminationParamsCollection` Returns the CycleCountDeterminationParamsCollectionCollection data collection that identifies all cycle count determination rules.
- `Public Sub Update(ByVal pICycleCountDetermination As CycleCountDetermination)` Adds an empty object to the collection.
  - param `pICycleCountDetermination`: 
  - C# example (from SAP's help):
    ```csharp
    CycleCountDeterminationsService ccdService = (CycleCountDeterminationsService)oCompany.GetCompanyService().GetBusinessService(ServiceTypes.CycleCountDeterminationsService);
           CycleCountDeterminationParams ccdParams = (CycleCountDeterminationParams)ccdService.GetDataInterface(CycleCountDeterminationsServiceDataInterfaces.ccdsCycleCountDeterminationParams);
           CycleCountDetermination ccd = (CycleCountDetermination)ccdService.GetDataInterface(CycleCountDeterminationsServiceDataInterfaces.ccdsCycleCountDetermination);

           ccdParams.WarehouseCode = "01";
           ccd = ccdService.Get(ccdParams);

           ccd.CycleBy = CycleCountDeterminationCycleByEnum.ccdcbWarehouseSublevel1;
           ccdService.Update(ccd);

           CycleCountDeterminationSetupCollection ccdSetups = ccd.CycleCountDeterminationSetupCollection;
           ccdSetups.Item(1).CycleCode = 2;
           ccdSetups.Item(1).DestinationUser = 2;
           ccdSetups.Item(1).Alert = BoYesNoEnum.tYES;
           ccdSetups.Item(1).ChangeExistingItems = BoYesNoEnum.tYES;
           ccdService.Update(ccd);
    ```

# DashboardPackageImportParams (Object)

DashboardPackageImportParams Class

## Properties (4)
- `Public Property ForceOverwritePackage() As BoYesNoEnum` [R/W] property ForceOverwritePackage
- `Public Property ForceOverwriteQuery() As BoYesNoEnum` [R/W] property ForceOverwriteQuery
- `Public Property ImportQueries() As BoYesNoEnum` [R/W] property ImportQueries
- `Public Property PackageFilePath() As String` [R/W] property PackageFilePath

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# DashboardPackageParams (Object)

DashboardPackageParams Class

## Properties (1)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# DashboardPackagesParams (Collection)

DashboardPackagesParams Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As DashboardPackageParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As DashboardPackageParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# DashboardPackagesService (Object)

DashboardPackagesService Class

## Methods (4)
- `Public Function GetDataInterface(ByVal enumMSDI As DashboardPackagesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `DashboardPackagesServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function ImportDashboardPackage(ByVal pIDashboardPackageImportParams As DashboardPackageImportParams) As DashboardPackageParams` ImportDashboardPackage
  - param `pIDashboardPackageImportParams`: 

# DataBrowser (Object)

The DataBrowser enables to navigate between records that are selected from the database or from XML formatted data. All business objects can call the DataBrowser object using the Browser property. You must use a Recordset object to initialize the DataBrowser object. You cannot create a new DataBrowser object, it is invoked as a Browser property of a business object.

**Remarks:** To use the DataBrowser object, first create a new Recordset object, preform the required query, and then assign the Recordset object to the Recordset property of the DataBrowser object. See Selecting Information Using the Recordset and DataBrowser Objects sample.

## Properties (4)
- `Public Property BoF() As Boolean` [R] Returns a Boolean value that specifies whether or not the pointer is at the beginning of the result set.
- `Public Property EoF() As Boolean` [R] Returns a Boolean value that specifies whether or not the result set has reached the last record.
- `Public Property RecordCount() As Long` [R] Returns the total result count returned by the query.
- `Public Property Recordset(ByVal RHS As Recordset) As Recordset` [W] Sets the Recordset object that you want to link to.
  - remarks: You can link the recordset only if the DoQuery method returned valid data.

## Methods (7)
- `Public Function GetByKeys(ByVal keysStr As String) As Boolean` Returns a DI object that match the unique ID (BusinessObjectInfo.ObjectKey) generated by the UI when FormDataEvent occurs. For more information, please refer to FormDataEvent event in UI Reference.
  - param `keysStr`: Unique ID (BusinessObjectInfo.ObjectKey) of the modified business object, created by UI upon FormDataEvent Event.
- `Public Sub MoveFirst()` Moves the business object that is connected to the first result in the Recordset.
- `Public Sub MoveLast()` Moves the business object that is connected to the last result in the Recordset.
- `Public Sub MoveNext()` Moves the business object that is connected to the next result in the Recordset.
- `Public Sub MovePrevious()` Moves the business object that is connected to the previous result in the Recordset.
- `Public Sub ReadXml(ByVal XmlFileStr As String, ByVal Index As Long)` Browses XML formatted data and enables to update the data.
  - param `XmlFileStr`: Specifies the XML file name or the XML content string depending on the value of the XMLAsString property.
  - param `Index`: Specifies the number of the object that you want to read from the XML data (starts from 0).
  - remarks: The default setting of XmlExportType property is xet_AllNodes (0). This setting supports older DI API versions but cannot be read using the ReadXML method. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3).
- `Public Sub Refresh()` Refreshen the results set. You can use the Refresh method when you want to run a new query with the linked Recordset object.

# DataSensitiveStatus (Object)

DataSensitiveStatus Class

## Properties (1)
- `Public Property DataSensitiveStatus() As DataSensitiveStatusEnum` [R] property DataSensitiveStatus

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# DecimalData (Object)

Represents the data before rounding.

## Properties (3)
- `Public Property Context() As RoundingContextEnum` [R/W] The rounding type. For example, the unit price in item master data is rounded to price type. The price type is defined to have 2 decimal places; therefore, an input of “1.23456789” is rounded to “1.23”.
- `Public Property Currency() As String` [R/W] The currency.
- `Public Property Value() As Double` [R/W] The value of the data before rounding.

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

# DeductionTaxGroups (Object)

Represents withholding tax groups. These groups can be assigned to business partners to determine . Source table: ODDG.

**Remarks:** For Israel only. Mandatory properties: GroupCode, GroupName, and MaxRedin. To display the form in the application: - Select Administration -->Company Details -->Basic Initialization tab. - Select the Hierarchical Deduction at Source check box. - Click the Define Deduction Groups button.

## Properties (7)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property GroupCode() As BoDeductionTaxGroupCodeEnum` [R/W] Sets or returns the code of the tax deduction group. Field name: CstGrpCode. Mandatory property. Length: 2 characters.
- `Public Property GroupExtendedCode() As String` [R/W] property GroupExtendedCode
- `Public Property GroupKey() As Long` [R] Returns the deduction tax group key. Field name: Numerator.
- `Public Property GroupName() As String` [R/W] Sets or returns the name of the tax deduction group. Field name: CstGrpName. Mandatory property. Length: 30 characters.
- `Public Property MaxRedin() As Double` [R/W] Sets or returns the maximum tax deduction percentage. Mandatory property.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (6)
- `Public Function Add() As Long` Adds a tax deduction group.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lGroupKey As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lGroupKey`: 
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

# DeductionTaxHierarchies (Object)

The DeductionTaxHierarchies object enables to define taxation levels to withhold from payments to vendors. This object is part of the Business Partners module. Source table: ODDT.

**Remarks:** Country-specific for Israel. Mandatory properties: BPCode, HierarchyCode, ValidFrom, and ValidUntil. To display the form in the application: - Select Business Partners -->Business Partner Master Data -->Accounting tab -->Tax tab. - Click the Hierarchies button.

## Properties (12)
- `Public Property AbsEntry() As Long` [R] Returns ABS_ENTRY, the Primery key to the Withholding Tax Deduction Hierarchy (ODDT) table. Field name: ABS_ENTRY.
- `Public Property BPCode() As String` [R/W] Sets or returns the business partner identification key in SAP Business One. Field name: CardCode. Mandatory property. Length: 15 characters.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property DeductionPercent() As Double` [R/W] property DeductionPercent
- `Public Property HierarchyCode() As String` [R/W] Sets or returns the hierarchy code. Field name: DateFrom. Mandatory property. Length: 10 characters. TrcCode
- `Public Property HierarchyName() As String` [R/W] Sets or returns the hierarchy name. Field name: DateFrom. Length: 30 characters. TrcName
- `Public Property LastUpdated() As Date` [R] property LastUpdated
- `Public Property Lines() As DeductionTaxHierarchies_Lines` [R] Returns the DeductionTaxHierarchies_Lines child object.
- `Public Property MaximumTotal() As Double` [R/W] property MaximumTotal
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property ValidFrom() As Date` [R/W] Sets or returns the validity start date of the withholding tax deduction certificate. Field name: DateFrom.
  - remarks: SAP Business One does not enable overlapping periods.
- `Public Property ValidUntil() As Date` [R/W] Sets or returns the validity end date of the withholding tax deduction certificate. Field name: DateTo.
  - remarks: SAP Business One does not enable overlapping periods.

## Methods (6)
- `Public Function Add() As Long` Adds a taxation level definition.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lAbsEntry As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lAbsEntry`: Numerator.
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

# DeductionTaxHierarchies_Lines (Object)

The DeductionTaxHierarchies_Lines is a child object of DeductionTaxHierarchies object. It enables to define the deduction percentage and maximum amount for each taxation level. Source table: DDT1.

**Remarks:** Country-specific for Israel. To display the form in the application: - Select Business Partners -->Business Partner Master Data -->Accounting tab -->Tax tab. - Click the Hierarchies button. - Click the Withholding Tax Deduction Hierarchy button.

## Properties (5)
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property DeductionPercent() As Long` [R/W] Sets or returns the Deduction Percent . Field name: DdctPrcnt.
- `Public Property MaximumTotal() As Double` [R/W] Sets or returns the maximum amount for which the deduction percentage applies. Field name: MaxSum.
- `Public Property RowNumber() As Long` [R] Returns the row number of the taxation level. Field name: LineNum.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# DeductionTaxSubGroup (Object)

DeductionTaxSubGroup Class

## Properties (2)
- `Public Property GroupCode() As String` [R/W] property GroupCode
- `Public Property GroupName() As String` [R/W] property GroupName

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

# DeductionTaxSubGroupParams (Object)

DeductionTaxSubGroupParams Class

## Properties (2)
- `Public Property GroupCode() As String` [R/W] property GroupCode
- `Public Property GroupName() As String` [R] property GroupName

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

# DeductionTaxSubGroupsParams (Collection)

DeductionTaxSubGroupsParams Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As DeductionTaxSubGroupParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As DeductionTaxSubGroupParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# DeductionTaxSubGroupsService (Object)

DeductionTaxSubGroupsService Class

## Methods (7)
- `Public Function AddDeductionTaxSubGroup(ByVal pIDeductionTaxSubGroup As DeductionTaxSubGroup) As DeductionTaxSubGroupParams` AddDeductionTaxSubGroup
  - param `pIDeductionTaxSubGroup`: 
- `Public Function GetDataInterface(ByVal enumMSDI As DeductionTaxSubGroupsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `DeductionTaxSubGroupsServiceDataInterfaces` in `../enums/enums-02.md`
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
- `Public Function GetDeductionTaxSubGroup(ByVal pIDeductionTaxSubGroupParams As DeductionTaxSubGroupParams) As DeductionTaxSubGroup` GetDeductionTaxSubGroup
  - param `pIDeductionTaxSubGroupParams`: 
- `Public Function GetDeductionTaxSubGroupList() As DeductionTaxSubGroupsParams` GetDeductionTaxSubGroupList
- `Public Sub UpdateDeductionTaxSubGroup(ByVal pIDeductionTaxSubGroup As DeductionTaxSubGroup)` UpdateDeductionTaxSubGroup
  - param `pIDeductionTaxSubGroup`: 

# DefaultCreditCards (Object)

The DefaultCreditCards is a child object of the UserDefaultGroups object. It enables to link G/L accounts to credit card codes. Source table: UDG2.

**Remarks:** To display the form in the application: - Select Administration -->Setup -->General -->Users. - From the Defaults field, click the Choose From List button. - In the List of User Defaults, click the New button. - In the User Defaults form, select the Credit Cards tab.

## Properties (5)
- `Public Property Code() As String` [R] Returns the code (primary key) of the user defaults group. Field name: Code. Length: 8 characters.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property CreditAccountCode() As String` [R/W] Sets or returns the G/L account code that is linked to the default credit card. Field name: AcctCode. Length: 15 characters. This is a foreign key to the Code of the ChartOfAccounts object.
- `Public Property CreditCardCode() As Long` [R/W] Sets or returns the default credit card code. Field name: CreditCard. This is a foreign key to the CreditCardCode of the CreditCards object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

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

# DefaultElectronicSeriesParams (Object)

DefaultElectronicSeriesParams Class

## Properties (2)
- `Public Property ElectronicSeries() As Long` [R/W] property ElectronicSeries
- `Public Property Series() As Long` [R/W] property Series

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# DefaultElementsforCR (Object)

With default elements in SAP Business One, you can maintain unified translations for Crystal Reports layouts according to different document languages. Source table: OMLP.

**Remarks:** From the SAP Business One Main Menu, choose Administration → Setup → General → Default Elements for SAP Crystal Reports. In the Default Elements for SAP Crystal Reports window, you can: - Find a list of predefined elements and their English and German translations (right-click the element and choose Translate...). - Add default elements.

## Properties (2)
- `Public Property Code() As Long` [R] The code of the predefined elements. Field name: Code.
- `Public Property Name() As String` [R/W] The name of the predefined elements. Field name: Name. Length: 100 characters.

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

# DefaultElementsforCRParams (Object)

Holds the key of a default elements for Crystal Reports. This object is used to pass keys to and retrieve keys from DefaultElementsforCRService methods.

## Properties (2)
- `Public Property Code() As Long` [R/W] The code of the predefined elements. Field name: Code.
- `Public Property Name() As String` [R] The name of the predefined elements. Field name: Name. Length: 100 characters.

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

# DefaultElementsforCRService (Object)

The DefaultElementsforCRService service enables you to add and look up default elements for Crystal Reports. Source table: OMLP.

## Methods (5)
- `Public Function Add(ByVal pIDefaultElementsforCR As DefaultElementsforCR) As DefaultElementsforCRParams` Adds a default element.
  - param `pIDefaultElementsforCR`: The data for the new default element.
- `Public Function Get(ByVal pIDefaultElementsforCRParams As DefaultElementsforCRParams) As DefaultElementsforCR` Retrieves a default element. The default element is specified by its key, which is contained in the DefaultElementsforCRParams object passed to the method.
  - param `pIDefaultElementsforCRParams`: The key of the default element to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As DefaultElementsforCRServiceDataInterfaces) As Object` Creates an empty data structure for use with the DefaultElementsforCRService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `DefaultElementsforCRServiceDataInterfaces` in `../enums/enums-02.md`
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

# DefaultPTICodes (Object)

DefaultPTICodes Class

## Properties (4)
- `Public Property Count() As Long` [R] property Count
- `Public Property DefaultPTICode() As String` [R/W] property DefaultPTICode
- `Public Property DocObjectCode() As BoObjectTypes` [R/W] property DocObjectCode
- `Public Property DocumentSubType() As BoDocumentSubType` [R/W] property DocumentSubType

## Methods (2)
- `Public Sub Add()` method Add
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 

# DefaultReportParams (Object)

Specifies the default report layout for a document type. The default report layout can be designated for a specific user and business partner, or for all users and business partners. Use this object with the GetDefaultReport/SetDefaultReport methods of the ReportLayoutsService. Source table: RDFL

**Remarks:** To specify a default report layout in SAP Business One: - Open a marketing document form (for example, Sales A/R -- Sales Quotation). - Select Tools --> Print Layout Designer (or select the pencil icon on the toolbar). - Select a report layout. - Click Set as Default.

## Properties (4)
- `Public Property CardCode() As String` [R/W] A business partner for which the report layout is the default. If blank, the report layout is default for all business partners. Field name: CardCode Length: 15 characters This is a foreign key to the BusinessPartners object.
- `Public Property LayoutCode() As String` [R/W] The default report layout for the document type specified in the ReportCode property. Field name: DfltReport Length: 8 characters
  - remarks: This is the key of the report layout (LayoutCode property of the ReportLayout object).
- `Public Property ReportCode() As String` [R/W] The document type for which the report layout specified by the LayoutCode property is the default. Field name: DoumntDode. Length: 4 characters.
  - remarks: The Code field of the table RTYP contains valid values.
- `Public Property UserID() As Long` [R/W] A user for which the report layout is the default. If blank, the report layout is default for all users. Field name: UserId Length: 11 characters Returns the identification key of the active user who operates the system.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure. Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data. Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data. Creates an XML string that represents the object data.

# Department (Object)

Represents a department that can be assigned to a user or employee. Source table: OUDP Mandatory properties: Name

## Properties (3)
- `Public Property Code() As Long` [R] The key for a specific department. Field name: Code
- `Public Property Description() As String` [R/W] A description of the department. Field name: Remarks
- `Public Property Name() As String` [R/W] The name of the department. Field name: Name
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

# DepartmentParams (Object)

Holds the key and name of a department. This object is used to pass keys to and retrieve keys from DepartmentsService methods.

## Properties (2)
- `Public Property Code() As Long` [R/W] The key for a specific department. Field name: Code
- `Public Property Name() As String` [R] The name of the department. Field name: Name

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# DepartmentsParams (Collection)

A collection of DepartmentParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As DepartmentParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As DepartmentParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# DepartmentsService (Object)

The DepartmentsService service enables you to add, look up and remove departments in the departments master data table. Users and employees can be assigned to departments. To see the list of departments, do one of the following: - Select Administration --> Setup --> General --> Users, and then select Define New from the Department list. - Select Human Resources --> Employee Master Data, and then select Define New from the Department list. Source table: OUDP

## Methods (8)
- `Public Function AddDepartment(ByVal pIDepartment As Department) As DepartmentParams` Adds a department.
  - param `pIDepartment`: The data for the new department.
  - returns: Contains the key (Code) of the new department.
  - C# example (from SAP's help):
    ```csharp
    DepartmentsService oDeptSrv;
    oDeptSrv = (DepartmentsService)(MainModule.oCmpSrv.GetBusinessService(ServiceTypes.DepartmentsService));

    SAPbobsCOM.Department addLine;
    addLine = (SAPbobsCOM.Department)oDeptSrv.GetDataInterface(DepartmentsServiceDataInterfaces.dsDepartment);

    addLine.Name = "B1";
    addLine.Description = "Business One";
    oDeptSrv.AddDepartment(addLine);
    ```
- `Public Sub DeleteDepartment(ByVal pIDepartmentParams As DepartmentParams)` Deletes an existing department. The department is specified by its key (Code), which is contained in the DepartmentParams object passed to the method.
  - param `pIDepartmentParams`: The key of the department to be deleted.
  - remarks: You cannot delete a department that is linked to a user or employee.
  - C# example (from SAP's help):
    ```csharp
    DepartmentParams delLine;
    delLine = (DepartmentParams)oDeptSrv.GetDataInterface(DepartmentsServiceDataInterfaces.dsDepartmentParams);

    // The Code should be of an existing record.
    delLine.Code = 10;
    oDeptSrv.DeleteDepartment(delLine);
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As DepartmentsServiceDataInterfaces) As Object` Creates an empty data structure for use with the DepartmentsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `DepartmentsServiceDataInterfaces` in `../enums/enums-02.md`
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
- `Public Function GetDepartment(ByVal pIDepartmentParams As DepartmentParams) As Department` Retrieves a department. The department is specified by its key (Code), which is contained in the DepartmentParams object passed to the method.
  - param `pIDepartmentParams`: The key of the department to retrieve.
  - returns: The department with the specified key.
- `Public Function GetDepartmentList() As DepartmentsParams` Retrieves the keys and names of all the departments.
  - C# example (from SAP's help):
    ```csharp
    DepartmentsParams getlistParams;
    getlistParams = oDeptSrv.GetDepartmentList();

    String resultSet = "";

    foreach (DepartmentParams record in getlistParams)
    {
        resultSet = resultSet + record.Code + "\t" + record.Name + "\n";
    }
    ```
- `Public Sub UpdateDepartment(ByVal pIDepartment As Department)` Updates an existing department. The data for the department, including the key of the department to be updated, is contained in the Department object passed to the method. To update a department, you must first retrieve it using the GetDepartment method.
  - param `pIDepartment`: The data for the department to be updated. The Department object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    DepartmentParams getLine;
    SAPbobsCOM.Department updateLine;
    getLine = (DepartmentParams)oDeptSrv.GetDataInterface(DepartmentsServiceDataInterfaces.dsDepartmentParams);

    // Please note that the Code should of an existing record.
    getLine.Code = 10;

    updateLine = oDeptSrv.GetDepartment(getLine);
    updateLine.Name = "A1";
    updateLine.Description = "All in One";
    oDeptSrv.UpdateDepartment(updateLine);
    ```

# Deposit (Object)

Represents the deposits for received checks, credit card vouchers, and cash. Source table: ODPS.

## Properties (49)
- `Public Property AbsEntry() As Long` [R] The internal key of a specific deposit. Field name: AbsEntry.
- `Public Property AllocationAccount() As String` [R/W] The Cash on Hand account from which the deposit is defined. Field name: AllocAcct. Length: 15 characters.
  - remarks: The account is defined in Administration --> Setup --> Financials --> G/L Account Determination --> Sales. If required, you can specify another account.
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property Bank() As String` [R/W] The name of the bank in which the deposit was made. Field name: DpsBank. Length: 30 characters.
- `Public Property BankAccountNum() As String` [R/W] The bank account number of the deposit. Field name: DeposAcct. Length: 50 characters.
- `Public Property BankBranch() As String` [R/W] The branch of the bank in which the deposit was made. Field name: DeposBrnch. Length: 50 characters.
- `Public Property BankReference() As String` [R/W] The reference assigned to the deposit by the bank. Field name: Ref2. Length: 11 characters.
- `Public Property BOEs() As BOELines` [R] Returns the BOELines object which support bills of exchange deposit on line level.
- `Public Property BPLID() As Long` [R/W] property BPLID
- `Public Property CheckDepositType() As BoCheckDepositTypeEnum` [R/W] property CheckDepositType
- `Public Property Checks() As CheckLines` [R] Returns the CheckLines object which support checks deposit on line level.
- `Public Property Commission() As Double` [R/W] The amount of commission to be paid in credit card deposit type. Field name: Comission.
- `Public Property CommissionAccount() As String` [R/W] The account used for commission payment in credit card deposit type. Field name: ComissAct. Length: 15 characters.
- `Public Property CommissionCurrency() As String` [R/W] property CommissionCurrency
- `Public Property CommissionDate() As Date` [R/W] The due date for the commission entry in the transaction. Field name: ComissDate.
- `Public Property CommissionFC() As Double` [R] property CommissionFC
- `Public Property CommissionSC() As Double` [R] property CommissionSC
- `Public Property Credits() As CreditLines` [R] Returns the CreditLines object which support credit cards deposit on line level.
- `Public Property DepositAccount() As String` [R/W] The G/L account if you perform the deposit to a bank account. Field name: BanckAcct. Length: 15 characters.
- `Public Property DepositAccountType() As BoDepositAccountTypeEnum` [R/W] The type of the deposit account: bank account or business partner. Field name: IsCard.
- `Public Property DepositCurrency() As String` [R/W] The currency of the deposit. Field name: DeposCurr.
  - remarks: Once a currency is selected, only checks/credit card vouchers/cash of this currency may be deposited.
- `Public Property DepositDate() As Date` [R/W] The date of the deposit. Field name: DeposDate.
- `Public Property DepositNumber() As Long` [R] The deposit number according to the selected numbering series. Field name: DeposNum.
- `Public Property DepositorName() As String` [R/W] The name of the person who made the deposit. Field name: DpostorNam. Length: 30 characters.
- `Public Property DepositType() As BoDepositTypeEnum` [R/W] The type of the deposit. Field name: DeposType.
- `Public Property DistributionRule() As String` [R/W] The distribution rule for the commission. Field name: OcrCode. Length: 8 characters.
  - remarks: If you define the distribution rule here, it appears in the Distr. Rule field for the corresponding journal entry row. If you leave this field empty, the default distribution rule for the commission G/L account appears in the Distr. Rule field for the corresponding journal entry row.
- `Public Property DistributionRule2() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode2
- `Public Property DistributionRule3() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode3
- `Public Property DistributionRule4() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode4
- `Public Property DistributionRule5() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode5
- `Public Property DocRate() As Double` [R/W] The payment rate. Field name: DocRate.
- `Public Property IncomeTaxAccount() As String` [R/W] property IncomeTaxAccount
- `Public Property IncomeTaxAmount() As Double` [R/W] property IncomeTaxAmount
- `Public Property IncomeTaxAmountFC() As Double` [R] property IncomeTaxAmountFC
- `Public Property IncomeTaxAmountSC() As Double` [R] property IncomeTaxAmountSC
- `Public Property JournalRemarks() As String` [R/W] The remarks relevant to the journal entry created by the deposit. Field name: Memo. Length: 250 characters.
- `Public Property Project() As String` [R/W] The project to which the commission is allocated. Field: Project. Length: 20 characters.
- `Public Property ReconcileAfterDeposit() As BoYesNoEnum` [R/W] Specifies whether to perform reconciliation of the amounts deposited automatically. Field name: ReconAfter.
  - remarks: Only for checks and credit cards.
- `Public Property Series() As Long` [R/W] The numbering series you want to use for the deposit number. Field name: Series.
- `Public Property TaxAccount() As String` [R/W] The tax account, if you need to pay tax for the commission charges in credit card deposit type. Field name: VatAct. Length: 15 characters.
- `Public Property TaxAmount() As Double` [R/W] The tax amount, if you need to pay tax for the commission charges in credit card deposit type. Field name: VatTotal.
- `Public Property TaxAmountFC() As Double` [R] property TaxAmountFC
- `Public Property TaxAmountSC() As Double` [R] property TaxAmountSC
- `Public Property TaxCode() As String` [R/W] The tax code, if you need to pay tax for the commission charges in credit card deposit type. Field name: CommisVat. Length: 8 characters.
  - remarks: Country-specific fields for Europe.
- `Public Property TotalFC() As Double` [R] The total amount of the deposit in foreign currency. Field name: FcTotal.
- `Public Property TotalLC() As Double` [R/W] The total amount of the deposit in local currency. Field name: LocTotal.
- `Public Property TotalSC() As Double` [R] The total amount of the deposit in system currency. Field name: SysTotal.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.
- `Public Property VoucherAccount() As String` [R/W] The credit card vouchers to be deposited. The details are from the incoming payment documents relating to the displayed vouchers. Field name: CrdBankAct. Length: 15 characters.

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

# DepositParams (Object)

Holds the key to an existing deposit. This object is used to pass keys to and retrieve keys from DepositsService methods.

## Properties (3)
- `Public Property AbsEntry() As Long` [R/W] The internal key of a specific deposit. Field name: AbsEntry.
- `Public Property DepositNumber() As Long` [R/W] The deposit number according to the selected numbering series. Field name: DeposNum.
- `Public Property Series() As Long` [R/W] The numbering series you want to use for the deposit number. Field name: Series.

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

# DepositsParams (Collection)

A collection of DepositParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As DepositParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As DepositParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# DepositsService (Object)

The DepositsService service enables you to add, look up, update and cancel deposits for: - Cash - Checks - Credit card vouchers For Chile, France, Italy, Portugal, and Spain localizations, you can view deposited bills of exchange (BoE). Source table: ODPS.

**Remarks:** To access the Deposit window from the SAP Business One application, choose Banking --> Deposits --> Deposit.

## Methods (11)
- `Public Function AddDeposit(ByVal pIDeposit As Deposit) As DepositParams` Adds a deposit.
  - param `pIDeposit`: The data for the new deposit.
  - C# example (from SAP's help):
    ```csharp
    //Get company service
    CompanyService companyService = oCompany.GetCompanyService();

    //Get deposit service
    SAPbobsCOM.DepositService dpService = (SAPbobsCOM.DepositService)companyService.GetBusinessService(ServiceTypes.DepositService);

    //Deposit with Cash
    SAPbobsCOM.Deposit dpsAddCash = (SAPbobsCOM.Deposit)dpService.GetDataInterface(DepositServiceDataInterfaces.dsDeposit);
    //Specify the deposit type
    dpsAddCash.DepositType = BoDepositTypeEnum.dtCash;
    //Set deposit currency type
    dpsAddCash.DepositCurrency = "RMB";
    dpsAddCash.AllocationAccount = "100201";
    dpsAddCash.DepositAccount = "100101";
    dpsAddCash.TotalLC = 233.5;
    dpsAddCash.JournalRemarks = "Adding Deposit with Cash";

    //Add the deposit
    SAPbobsCOM.DepositParams dpsParamAddCash = dpService.AddDeposit(dpsAddCash);
    ```
- `Public Sub CancelCheckRow(ByVal pICancelCheckRowParams As CancelCheckRowParams)` Cancels a check that was received as an incoming payment together with the incoming payment document.
  - param `pICancelCheckRowParams`: The key of the check to be canceled.
- `Public Sub CancelCheckRowbyCurrentSystemDate(ByVal pICancelCheckRowParams As CancelCheckRowParams)` CancelCheckRowbyCurrentSystemDate
  - param `pICancelCheckRowParams`: 
- `Public Sub CancelDeposit(ByVal pIDepositParams As DepositParams)` Cancels an existing deposit.
  - param `pIDepositParams`: The key of the deposit to be canceled.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.DepositsParams ParamsCancel = (SAPbobsCOM.DepositsParams)dpService.GetDepositList();

    if (ParamsCancel.Count > 0)
     {
         foreach (SAPbobsCOM.DepositParams paramC in ParamsCancel)
         {
             //Get the related deposit object
             SAPbobsCOM.Deposit dpsCancel = dpService.GetDeposit(paramC);

             //Cancel deposit
             dpService.CancelDeposit(paramC);

             //Cancel the first deposit
             break;
         }
     }
    ```
- `Public Sub CancelDepositbyCurrentSystemDate(ByVal pIDepositParams As DepositParams)` CancelDepositbyCurrentSystemDate
  - param `pIDepositParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As DepositsServiceDataInterfaces) As Object` Creates an empty data structure for use with the DepositsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `DepositsServiceDataInterfaces` in `../enums/enums-02.md`
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
- `Public Function GetDeposit(ByVal pIDepositParams As DepositParams) As Deposit` Retrieves a deposit. The deposit is specified by its key, which is contained in the DepositParams object passed to the method.
  - param `pIDepositParams`: The key of the deposit to retrieve.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.DepositsParams dpsParamsGet = (SAPbobsCOM.DepositsParams)dpService.GetDepositList();
    if (dpsParamsGet.Count > 0)
    {
        //You can get the "DepositNumber" one by one.
        foreach (SAPbobsCOM.DepositParams dpsParamGet in dpsParamsGet)
        {
            int dpsNumber = dpsParamGet.DepositNumber;
            //Get Deposit
            SAPbobsCOM.Deposit dpsGet = dpService.GetDeposit(dpsParamGet);

           //Any operations as you like.
        }
    }
    ```
- `Public Function GetDepositList() As DepositsParams` Returns the DepositsParams data collection that identify all deposits.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.DepositsParams dpsParamsGet = (SAPbobsCOM.DepositsParams)dpService.GetDepositList();
    if (dpsParamsGet.Count > 0)
    {
        //You can get the "DepositNumber" one by one.
        foreach (SAPbobsCOM.DepositParams dpsParamGet in dpsParamsGet)
        {
            int dpsNumber = dpsParamGet.DepositNumber;
            //Get Deposit
            SAPbobsCOM.Deposit dpsGet = dpService.GetDeposit(dpsParamGet);

           //Any operations as you like.
        }
    }
    ```
- `Public Sub UpdateDeposit(ByVal pIDeposit As Deposit)` Updates an existing deposit. The data for the deposit, including the key of the deposit to be updated, is contained in the Deposit object passed to the method. To update a deposit, you must first retrieve it using the GetDeposit method.
  - param `pIDeposit`: The data for the deposit to be updated. The Deposit object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    //Get an existing deposit object
    SAPbobsCOM.DepositsParams dpsParamsGetForUpdate = (SAPbobsCOM.DepositsParams)dpService.GetDepositList();

    if (dpsParamsGetForUpdate.Count > 0)
    {
        foreach (SAPbobsCOM.DepositParams dpsParamGetForUpdate in dpsParamsGetForUpdate)
        {
            //Get deposit
            SAPbobsCOM.Deposit dpsGetForUpdate = dpService.GetDeposit(dpsParamGetForUpdate);

            //Update deposit journal remarks
            dpsGetForUpdate.JournalRemarks = "Updating existing deposit";

            //Update the deposit
            dpService.UpdateDeposit(dpsGetForUpdate);

            //Change the first deposit only
            break;
         }
    }
    ```

# DepreciationArea (Object)

In SAP Business One, you can use different depreciation areas for showing the value of fixed assets for a specific purpose. Source table: ODPA.

## Properties (13)
- `Public Property AreaType() As AreaTypeEnum` [R/W] The types for the depreciation area. Field name: AreaType.
- `Public Property BPForTaxCorrection() As String` [R/W] property BPForTaxCorrection
- `Public Property Code() As String` [R/W] The unique code for the depreciation area. Field name: Code. Length: 20 characters.
- `Public Property DerivedArea() As String` [R/W] The derived depreciation area of the main depreciation area. Field name: DrvdArea. Length: 15 characters.
- `Public Property Description() As String` [R/W] The description of the depreciation area. Field name: Descr. Length: 100 characters.
- `Public Property DirectRevenuePosting() As BoYesNoEnum` [R/W] Indicates whether to allow direct revenue posting in A/R documents. Field name: DirRevPost.
- `Public Property ItemForTaxCorrection() As String` [R/W] property ItemForTaxCorrection
- `Public Property MainBookingArea() As BoYesNoEnum` [R/W] Indicates whether the depreciation area is the main depreciation area. Field name: MainArea.
- `Public Property PostingOfDepreciation() As PostingOfDepreciationEnum` [R/W] The depreciation posting methods. The field is only for the depreciation areas with the Posting to G/L type. Field name: DirectDpr.
- `Public Property RetirementMethod() As RetirementMethodEnum` [R/W] The retirement posting methods. The field is only for the depreciation areas with the Posting to G/L type. Field name: RetMeth.
- `Public Property TaxCreditControl() As BoYesNoEnum` [R/W] property TaxCreditControl
- `Public Property TaxType() As Long` [R/W] property TaxType
- `Public Property UsageForTaxCorrection() As Long` [R/W] property UsageForTaxCorrection

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

# DepreciationAreaParams (Object)

Holds the key to an existing depreciation area. This object is used to pass keys to and retrieve keys from DepreciationAreasService methods.

## Properties (2)
- `Public Property Code() As String` [R/W] The unique code for the depreciation area. Field name: Code. Length: 20 characters.
- `Public Property Description() As String` [R] The description of the depreciation area. Field name: Descr. Length: 100 characters.

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

# DepreciationAreaParamsCollection (Collection)

A collection of DepreciationAreaParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As DepreciationAreaParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As DepreciationAreaParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# DepreciationAreasService (Object)

The DepreciationAreasService service enables you to create, update, and view depreciation areas. Source table: ODPA.

**Remarks:** To open the Depreciation Areas - Setup window, from the SAP Business One Main Menu, choose Administration --> Setup --> Financials --> Fixed Assets --> Depreciation Areas.

## Methods (8)
- `Public Function Add(ByVal pIDepreciationArea As DepreciationArea) As DepreciationAreaParams` Adds a depreciation area.
  - param `pIDepreciationArea`: The data for the new depreciation area.
- `Public Sub Delete(ByVal pIDepreciationAreaParams As DepreciationAreaParams)` Deletes an existing depreciation area.
  - param `pIDepreciationAreaParams`: The key of the depreciation area to be deleted.
- `Public Function Get(ByVal pIDepreciationAreaParams As DepreciationAreaParams) As DepreciationArea` Retrieves a depreciation area. The depreciation area is specified by its key, which is contained in the DepreciationAreaParams object passed to the method.
  - param `pIDepreciationAreaParams`: The key of the depreciation area to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As DepreciationAreasServiceDataInterfaces) As Object` Creates an empty data structure for use with the DepreciationAreasService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `DepreciationAreasServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As DepreciationAreaParamsCollection` Returns the DepreciationAreaParamsCollection data collection that identifies all depreciation areas.
- `Public Sub Update(ByVal pIDepreciationArea As DepreciationArea)` Updates an existing depreciation area. The data for the depreciation area, including the key of the depreciation area to be updated, is contained in the DepreciationArea object passed to the method. To update a depreciation area, you must first retrieve it using the Get method.
  - param `pIDepreciationArea`: The data for the depreciation area to be updated. The DepreciationArea object must contain the key of the object to be updated.

# DepreciationLevel (Object)

DepreciationLevel is a child object of DepreciationType object. You can view an asset's useful life as several phases and depreciate the asset by a defined rate for each phase. This way, the asset can have a course of depreciation that changes in levels over time. SAP Business One lets you break down an asset's useful life into multiple phases, for each of which you can specify a depreciation rate and a validity period. Source table: DTP1.

## Properties (5)
- `Public Property amount() As Double` [R/W] The amount for the depreciation. Field name: Amount.
- `Public Property DepreciationCalculationBase() As DepreciationCalculationBaseEnum` [R/W] The base for the depreciation calculation in each phase of an asset's useful life. Field name: Base.
- `Public Property Level() As Long` [R] The level of depreciation. SAP Business One lets you specify multiple levels, with each level representing a phase in an asset's useful life. Field name: Level.
- `Public Property NumberOfYears() As Long` [R/W] The number of years in each phase of an asset's useful life. Field name: Years.
- `Public Property Percentage() As Double` [R/W] The annual percentage rate for the depreciation calculation that is valid for each phase. Field name: Percentage.

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

# DepreciationLevelCollection (Collection)

A collection of DepreciationLevel objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As DepreciationLevel` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As DepreciationLevel` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# DepreciationType (Object)

In SAP Business One, you can use depreciation types to define different depreciation calculation methods for your fixed assets. After you create a depreciation type, you can assign it to a specific depreciation area of an asset class. Then, by assigning the asset class to a fixed asset, the depreciation calculation methods are finally applied to the asset. In general, SAP Business One lets you use the following depreciation methods: - Straight Line Method - Straight Line Period Control Method - Declining Balance Method - Multilevel Method - Immediate Write-Off Method - Special Depreciation Method - Manual Depreciation Method - Accelerated Method: Czech Republic and Slovakia Source table: ODTP.

## Properties (44)
- `Public Property AcquisitionPeriodControl() As AcquisitionPeriodControlEnum` [R/W] Specify how the acquisition of an asset determines the asset's depreciation start date. Field name: PerAcq.
- `Public Property AcquisitionProRataType() As AcquisitionProRataTypeEnum` [R/W] Specify one of the PR Temporis Type to determine the depreciation start date. Field name: AcqPRTyp.
- `Public Property CalculationBase() As CalculationBaseEnum` [R/W] The base with which you want to calculate the depreciation of assets. Field name: CalcBase.
- `Public Property Code() As String` [R/W] The code for the depreciation type. Field name: Code. Length: 15 characters.
- `Public Property DecliningChangeTo() As String` [R/W] Specify a depreciation type with the straight line method as the alternative depreciation type. Field name: dAltDprTyp.
- `Public Property DecliningFactor() As Double` [R/W] The factor for calculating the upper limit of an asset's depreciation amount in each period. The upper limit is calculated using the straight-line method and multiplied by this factor. Field name: dFactor.
- `Public Property DecliningPercentage() As Double` [R/W] The annual/monthly percentage rate for the depreciation calculation. Field name: dPercent.
- `Public Property DeltaCoefficient() As Long` [R] The delta coefficient in the accelerated depreciation method. Field name: DeltaCoeff.
  - remarks: The accelerated depreciation method is available in the Czech Republic and Slovakia localizations only.
- `Public Property DepreciationEndAtLastFullYear() As BoYesNoEnum` [R/W] Indicates whether to stop an asset's depreciation at the end of the last full fiscal year of the asset's useful life. Field name: DeprEndLFY.
- `Public Property DepreciationLevelCollection() As DepreciationLevelCollection` [R] Represents the depreciation levels of an asset's useful life.
- `Public Property DepreciationMethod() As DepreciationMethodEnum` [R/W] The depreciation method of the asset. Field name: DprMeth.
- `Public Property DepreciationTypePool() As String` [R/W] Specify a pool to which you want to assign the depreciation type. You must assign a special or manual depreciation type to a pool. Field name: PoolID.
- `Public Property Description() As String` [R/W] The description about the depreciation type. Field name: Descr. Length: 100 characters.
- `Public Property FactorOnlyRelevantToFirstFiscalYear() As BoYesNoEnum` [R/W] Indicates that the factor you specified is effective only in the first fiscal year of an asset's useful life. Field name: FactorFFY.
- `Public Property IncludePreviousDepreciationInCapitalizationPeriod() As BoYesNoEnum` [R/W] Indicates whether to move depreciation of previous periods in the fiscal year to the capitalization period. Field name: AccuPriorP.
- `Public Property IncludeSalvageInDepreciation() As BoYesNoEnum` [R/W] Includes the salvage value in the calculation of an asset's depreciation. Field name: InclSalv.
- `Public Property ManualDepreciationReduceDepreciationBase() As BoYesNoEnum` [R/W] Indicates whether to let manual depreciation affect the calculation of an asset's planned depreciation. Field name: maDecBase.
  - remarks: Once you enable this property, the system automatically reduces the depreciation base by the manual depreciation amount.
- `Public Property MaximumDepreciableValue() As Double` [R/W] the maximum depreciable value of an asset. Field name: MaxDepr.
  - remarks: The field is available only for depreciation types having the Straight Line or Declining Balance method.
- `Public Property MinimumDepreciatedValue() As Double` [R/W] The minimum book value of an asset after depreciation. Field name: DprTo.
- `Public Property PercentageOfDepreciationReversedInRetirementYear() As Double` [R/W] The amount (in percentage) of depreciation you want to reverse for an asset in the retirement year. Field name: PerDpRev.
- `Public Property RetirementPeriodControl() As RetirementPeriodControlEnum` [R/W] Specify how an asset's retirement affects the asset's depreciation. Field name: PerRet.
- `Public Property RetirementProRataType() As RetirementProRataTypeEnum` [R/W] Specify one of the PR Temporis Type to determine the depreciation end date. Field name: RetPRTyp.
- `Public Property RoundingMethod() As DepreciationRoundingMethodEnum` [R/W] The rounding method of Round Year End Book Value. Field name: RoundMeth.
- `Public Property RoundYearEndBookValue() As BoYesNoEnum` [R/W] Rounds the net book values of assets at the end of each fiscal year. Field name: Rounding.
- `Public Property SalvagePercentage() As Double` [R/W] The salvage value percentage. Field name: SalvPerc.
- `Public Property SpecialDepreciationAlternativeDepreciation() As String` [R/W] To compare different depreciation calculations, specify a second depreciation type here. The system calculates the depreciation for this depreciation type in parallel. The result of the alternative calculation is for reference only, and no bookings are carried out in the general ledger. Field name: spAlDpr.
- `Public Property SpecialDepreciationCalculationMethod() As SpecialDepreciationCalculationMethodEnum` [R] The calculation method of special depreciation. Field name: spMeth.
- `Public Property SpecialDepreciationConcessionPeriodYears() As Long` [R/W] The number of years during which the special depreciation is legally permitted. Field name: spConcPer.
- `Public Property SpecialDepreciationMaximumAmount() As Double` [R/W] The maximum depreciation amount allowed in addition to the normal depreciation. The maximum amount is an alternative to the maximum percentage. Field name: spMaxAmnt.
- `Public Property SpecialDepreciationMaximumFlag() As SpecialDepreciationMaximumFlagEnum` [R/W] To optimize depreciation from a tax point of view, you can split the concession period into multiple sub-periods and freely distribute the maximum percentage over these periods. Field name: spMaxFlag.
- `Public Property SpecialDepreciationMaximumPercentage() As Double` [R/W] The percentage rate for calculating the maximum depreciation amount allowed in addition to the normal depreciation. Field name: spMaxPerc.
  - remarks: National legislation specifies this value. The system calculates the maximum special depreciation amount as follows: (Acquisition and Production Costs – Salvage Value) * Maximum Percentage
- `Public Property SpecialDepreciationNormalDepreciation() As String` [R/W] The normal depreciation of the asset. Field name: spAdDpr.
  - remarks: Usually, a certain percentage of the asset value can be depreciated in addition to the normal depreciation amount. The percentage allowed for the special depreciation, as well as the period over which you can carry out the special depreciation, are dependent on national legislation.
- `Public Property StraightLineCalculationMethod() As StraightLineCalculationMethodEnum` [R/W] The calculation method of the straight line period control depreciation method. Field name: sCalcMeth.
- `Public Property StraightLinePercentage() As Double` [R/W] The annual percentage rate for the depreciation calculation. Field name: sPercent.
- `Public Property StraightLinePeriodControlDepreciationPeriods() As StraightLinePeriodControlDepreciationPeriodsEnum` [R/W] The depreciation period of the straight line period control depreciation method. Field name: DprPer.
- `Public Property StraightLinePeriodControlFactor() As Double` [R/W] The factor for the straight line period control depreciation method. Field name: PerFactor.
  - remarks: If you have specified Standard in the StraightLinePeriodControlDepreciationPeriods property, enter a factor for depreciation calculation that is applied to all periods of an asset's useful life. If you have specified Individual in the StraightLinePeriodControlDepreciationPeriods property, enter a factor for depreciation calculation that is taken as the default factor for all periods.
- `Public Property SubsequentAcquisitionPeriodControl() As SubsequentAcquisitionPeriodControlEnum` [R/W] Specify how an asset's subsequent acquisition affects the asset's depreciation. Field name: PerSubAcq.
- `Public Property SubsequentAcquisitionProRataType() As SubsequentAcquisitionProRataTypeEnum` [R/W] Specify one of the PR Temporis Type to determine the depreciation start date. Field name: SubPRTyp.
- `Public Property TransferSourcePeriodControl() As TransferSourcePeriodControlEnum` [R/W] property TransferSourcePeriodControl
- `Public Property TransferSourceProRataType() As TransferSourceProRataTypeEnum` [R/W] property TransferSourceProRataType
- `Public Property TransferTargetPeriodControl() As TransferTargetPeriodControlEnum` [R/W] property TransferTargetPeriodControl
- `Public Property TransferTargetProRataType() As TransferTargetProRataTypeEnum` [R/W] property TransferTargetProRataType
- `Public Property ValidFrom() As Date` [R/W] The valid start date of the depreciation type. Field name: ValidFrom.
- `Public Property ValidTo() As Date` [R/W] The valid to date of the depreciation type. Field name: ValidTo.

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

# DepreciationTypeParams (Object)

DepreciationTypeParams Class

## Properties (2)
- `Public Property Code() As String` [R/W] The code for the depreciation type. Field name: Code. Length: 15 characters.
- `Public Property Description() As String` [R] The description about the depreciation type. Field name: Descr. Length: 100 characters.

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

# DepreciationTypeParamsCollection (Collection)

DepreciationTypeParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As DepreciationTypeParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As DepreciationTypeParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# DepreciationTypePool (Object)

Source table: ODPP.

## Properties (2)
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R/W] property Description

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

# DepreciationTypePoolParams (Object)

DepreciationTypePoolParams Class

## Properties (2)
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R] property Description

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

# DepreciationTypePoolParamsCollection (Collection)

DepreciationTypePoolParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As DepreciationTypePoolParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As DepreciationTypePoolParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# DepreciationTypePoolsService (Object)

Source table: ODPP.

## Methods (8)
- `Public Function Add(ByVal pIDepreciationTypePool As DepreciationTypePool) As DepreciationTypePoolParams` Add
  - param `pIDepreciationTypePool`: 
- `Public Sub Delete(ByVal pIDepreciationTypePoolParams As DepreciationTypePoolParams)` Delete
  - param `pIDepreciationTypePoolParams`: 
- `Public Function Get(ByVal pIDepreciationTypePoolParams As DepreciationTypePoolParams) As DepreciationTypePool` Get
  - param `pIDepreciationTypePoolParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As DepreciationTypePoolsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `DepreciationTypePoolsServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As DepreciationTypePoolParamsCollection` GetList
- `Public Sub Update(ByVal pIDepreciationTypePool As DepreciationTypePool)` Update
  - param `pIDepreciationTypePool`: 

# DepreciationTypesService (Object)

The DepreciationTypesService service enables you to create, update, and view depreciation types. Source table: ODTP.

**Remarks:** To access the Depreciation Types - Setup window, from the SAP Business One Main Menu, choose Administration --> Setup --> Financials --> Fixed Assets --> Depreciation Types.

## Methods (8)
- `Public Function Add(ByVal pIDepreciationType As DepreciationType) As DepreciationTypeParams` Add
  - param `pIDepreciationType`: 
- `Public Sub Delete(ByVal pIDepreciationTypeParams As DepreciationTypeParams)` Delete
  - param `pIDepreciationTypeParams`: 
- `Public Function Get(ByVal pIDepreciationTypeParams As DepreciationTypeParams) As DepreciationType` Get
  - param `pIDepreciationTypeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As DepreciationTypesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `DepreciationTypesServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As DepreciationTypeParamsCollection` GetList
- `Public Sub Update(ByVal pIDepreciationType As DepreciationType)` Update
  - param `pIDepreciationType`: 

# DeterminationCriteria (Object)

The available determination criteria are predefined (you cannot define additional determination criteria): Item Group Item Code Warehouse Code Business Partner Group Ship-to Country Ship-to State You can activate and prioritize the determination criteria to be applied on the inventory G/L account determination. Source table: ODMC.

## Properties (4)
- `Public Property DeterminationCriteria() As String` [R] The determination alias. Field name: DmcAlias.
- `Public Property DmcId() As Long` [R] The determination ID. Field name: DmcId.
- `Public Property IsActive() As BoYesNoEnum` [R/W] The active status of the determination criteria. Field name: Active.
- `Public Property Priority() As Long` [R/W] The determination priority. Field name: Priority.

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

# DeterminationCriteriaParams (Object)

Holds the key to an existing determination criteria. This object is used to pass keys to and retrieve keys from DeterminationCriteriasService methods.

## Properties (1)
- `Public Property DmcId() As Long` [R/W] The determination ID. Field name: DmcId.

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

# DeterminationCriteriaParamsCollection (Collection)

A collection of DeterminationCriteriaParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As DeterminationCriteriaParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As DeterminationCriteriaParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# DeterminationCriteriasService (Object)

The DeterminationCriteriasService service enables you to look up and update determination criteria. Source table: ODMC.

**Remarks:** To open the Determination Criteria window, from the SAP Business One Main Menu, choose Administration -> Setup -> Financials -> G/L Account Determination -> Determination Criteria. This window is available only if the Enable Advanced G/L Account Determination checkbox is selected (Administration -> System Initialization -> Company Details -> Basic Initialization tab).

**Example:**
- VB example (SAP's help labels this C#, but it is Visual Basic - translate before use):
  ```vb
  Dim oDeterminationCriteriasService As DeterminationCriteriasService =
  oCompany.GetCompanyService().GetBusinessService(ServiceTypes. DeterminationCriteriasService)

  Dim oDeterminationCriteria As SAPbobsCOM.DeterminationCriteria =
  oDeterminationCriteriasServices.GetDataInterface
  (DeterminationCriteriasServiceDataInterfaces.dcDeterminationCriteria)

  Dim param As SAPbobsCOM. DeterminationCriteriaParams =
  oDeterminationCriteriasServices.GetDataInterface
  (DeterminationCriteriasServiceDataInterfaces.dcDeterminationCriteriaParams)
          param.DmcId = 1
          oDeterminationCriteria = oDeterminationCriteriasService.Get(param)
          oDeterminationCriteria.IsActive = SAPbobsCOM.BoYesNoEnum.tYES
          oDeterminationCriteria.Priority = 8
          oDeterminationCriteriasService.Update(oDeterminationCriteria)
  ```

## Methods (6)
- `Public Function Get(ByVal pIDeterminationCriteriaParams As DeterminationCriteriaParams) As DeterminationCriteria` Retrieves a determination criteria. The determination criteria is specified by its key, which is contained in the DeterminationCriteriaParams object passed to the method.
  - param `pIDeterminationCriteriaParams`: The key of the determination criteria to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As DeterminationCriteriasServiceDataInterfaces) As Object` Creates an empty data structure for use with the DeterminationCriteriasService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `DeterminationCriteriasServiceDataInterfaces` in `../enums/enums-02.md`
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
- `Public Function GetList() As DeterminationCriteriaParamsCollection` Returns the DeterminationCriteriaParamsCollection data collection that identifies all determination criteria.
- `Public Sub Update(ByVal pIDeterminationCriteria As DeterminationCriteria)` Updates an existing determination criteria.
  - param `pIDeterminationCriteria`: The data for the determination criteria to be updated.

# Dimension (Object)

Represents one of the five system-defined dimensions, which can be assigned to a profit center or distribution rule. Dimensions enables additional options in assigning costs to additional categories and in reporting. Source table: ODIM

**Remarks:** Relevant for China, Japan, Republic of Korea, Singapore, India and Brazil only.

## Properties (5)
- `Public Property DimensionCode() As Long` [R] The key for a specific dimension. Field name: DimCode
- `Public Property DimensionDescription() As String` [R/W] A description for a specific dimension. Field name: DimDesc
- `Public Property DimensionName() As String` [R] The name of a specific dimension. Field name: DimName
- `Public Property IsActive() As BoYesNoEnum` [R/W] Indicates that the dimension is active. Field name: DimActive
  - remarks: You cannot deactivate a dimension if it is assigned to a profit center or distribution rule.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.

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

# DimensionParams (Object)

Holds the key and name of a dimension. This object is used to pass keys to and retrieve keys from DimensionsService methods.

## Properties (2)
- `Public Property DimensionCode() As Long` [R/W] The key for a specific dimension. Field name: DimCode
- `Public Property DimensionName() As String` [R] The name of a specific dimension. Field name: DimName

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

# DimensionsParams (Collection)

A collection of DimensionParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As DimensionParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As DimensionParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# DimensionsService (Object)

The DimensionsService service enables you to activate dimensions, as well as change a dimension's description. To see the list of dimensions, select Financials --> Cost Accounting --> Define Dimensions. Source table: ODIM

**Remarks:** You cannot add or delete dimensions. Relevant for China, Japan, Republic of Korea, Singapore, India and Brazil only.

## Methods (6)
- `Public Function GetDataInterface(ByVal enumMSDI As DimensionsServiceDataInterfaces) As Object` Creates an empty data structure for use with the DimensionsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `DimensionsServiceDataInterfaces` in `../enums/enums-02.md`
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
- `Public Function GetDimension(ByVal pIDimensionParams As DimensionParams) As Dimension` Retrieves a dimension. The dimension is specified by its key (DimCode), which is contained in the DimensionParams object passed to the method.
  - param `pIDimensionParams`: The key of the dimension to retrieve.
  - returns: The dimension with the specified key.
- `Public Function GetDimensionList() As DimensionsParams` Retrieves the keys and names of all the dimensions.
- `Public Sub UpdateDimension(ByVal pIDimension As Dimension)` Updates an existing dimension. The data for the dimension, including the key of the dimension to be updated, is contained in the Dimension object passed to the method. To update a dimension, you must first retrieve it using the GetDimension method.
  - param `pIDimension`: The data for the dimension to be updated. The Dimension object must contain the key of the object to be updated.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    oCmpSrv = oCompany.GetCompanyService()

    oDIMService = oCmpSrv.GetBusinessService(SAPbobsCOM.ServiceTypes.DimensionsService)

    oDIMParams = oDIMService.GetDataInterface(SAPbobsCOM.DimensionsServiceDataInterfaces.dsDimensionParams)

    oDIMParams.DimensionCode = 1

    Try

        oDIM = oDIMService.GetDimension(oDIMParams)

    Catch ex As Exception

        Return

    End Try

    oDIM.IsActive = SAPbobsCOM.BoYesNoEnum.tYES

    Try

        oDIMService.UpdateDimension(oDIM)

    Catch ex As Exception

        MsgBox(ex.Message)

    End Try
    ```

# DiscountGroupLine (Object)

DiscountGroupLine Class

## Properties (8)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property Discount() As Double` [R/W] property Discount
- `Public Property DiscountType() As DiscountGroupDiscountTypeEnum` [R] property DiscountType
- `Public Property FreeQuantity() As Double` [R/W] property FreeQuantity
- `Public Property MaximumFreeQuantity() As Double` [R/W] property MaximumFreeQuantity
- `Public Property ObjectCode() As String` [R/W] property ObjectCode
- `Public Property ObjectType() As DiscountGroupBaseObjectEnum` [R/W] property ObjectType
- `Public Property PaidQuantity() As Double` [R/W] property PaidQuantity

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# DiscountGroupLineCollection (Collection)

DiscountGroupLineCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As DiscountGroupLine` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As DiscountGroupLine` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` method Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# DiscountGroups (Object)

Represents a set of item discounts for a specific business partner. Each business partner can be assigned a set of discounts, and each discount is associated with an item group, property, or manufacturer. If the business partner purchases an item that is associated with one of the specified groups, properties, or manufacturers, the business partner receives the corresponding discount. All of the ObjectEntry keys point to the same type of object -- either group (ItemGroups object), property (ItemProperties object), or manufacturer (Manufacturers object) -- depending on the DiscountBaseObject property of the BusinessPartners object. Source table: OEDG.

**Remarks:** If a business partner has one type of discount groups, for example for item groups, you can define any type of discount groups, for example for item manufacturers, as follows: - Change the DiscountBaseObject of the BusinessPartners object to the new type (for example, item manufacturers). - Add new rows to the DiscountGroups subobject of the BusinessPartners object. - Update the BusinessPartners object. All rows in the DiscountGroups subobject related to the previous type are automatically deleted. For a list of ways for setting discounts and special prices, see SpecialPrices.

## Properties (5)
- `Public Property BaseObjectType() As DiscountGroupBaseObjectEnum` [R] The value of the DiscountBaseObject property for the current object's parent business partner.
- `Public Property BPCode() As String` [R] The key to the current object's parent business partner.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: Returns the total number of records for the current business partner. When adding a new row, the system increments the value of this property automatically.
- `Public Property DiscountPercentage() As Double` [R/W] The discount for a matching item, in percent. Field name: Discount
  - remarks: The value must be between 0 and 100.
- `Public Property ObjectEntry() As String` [R/W] The key to an item group, property, or manufacturer. Any item assigned to the group, property, or manufacturer is assigned the discount in the DiscountPercentage property. The key represents either an item group, property, or manufacturer depending on the DiscountBaseObject property of the current BusinessPartners object. Field name: ObjKey

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oBP As SAPbobsCOM.BusinessPartners

    Dim oDiscountGroup As SAPbobsCOM.DiscountGroups

    oBP = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oBusinessPartners)

    oBP.GetByKey("C1")

    oBP.DiscountBaseObject = SAPbobsCOM.DiscountGroupBaseObjectEnum.dgboItemGroups

    oDiscountGroup = oBP.DiscountGroups

    oDiscountGroup.SetCurrentLine(0)

    oDiscountGroup.Delete()

    oBP.Update()
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# DiscountLine (Object)

Defines a single criteria for applying a cash discount, as well as the discount percentage. Source table: CDC1 Mandatory properties: - Day, Month (if discount is based on the current date) - NumOfDays (if discount is based on payment within a specific number of days after the document posting date)

## Properties (6)
- `Public Property Day() As Long` [R/W] The day of the month on which to apply the discount percentage specified in this line. Field name: Day
  - remarks: Valid values are 1 to 31. A specific CashDiscount object cannot have two lines with the same date. Relevant if the ByDate field of this line's CashDiscount parent object is set to Y.
- `Public Property Discount() As Double` [R/W] The cash discount to grant if the current line's criteria apply. Field name: Discount
  - remarks: Valid values are 0 to 100. If Discount is set to null, the discount is set to 0. NumOfDays and Discount cannot both be 0.
- `Public Property DiscountCode() As String` [R] The key to this line's parent CashDiscount object. Field name: CdcCode
- `Public Property LineId() As Long` [R] The line number for this line. Each line within a specific CashDiscount object is assigned a unique line number. Field name: LineId
- `Public Property Month() As Long` [R/W] The month in which to apply the discount percentage specified in this line. Field name: Month
  - remarks: Valid values are 1 to 31. A specific CashDiscount object cannot have two lines with the same date. Relevant if the ByDate field of this line's CashDiscount parent object is set to Y.
- `Public Property NumOfDays() As Long` [R/W] Specifies the number of days following the document posting date after which this discount no longer applies. Field name: NumOfDays
  - remarks: Must be greater than or equal to 0. A specific CashDiscount object cannot have two lines with the same value for the NumOfDays property. Relevant if the ByDate field of this line's CashDiscount parent object is set to N. NumOfDays and Discount cannot both be 0.

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

<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# ServiceCallBPAddressComponents (Object)

ServiceCallBPAddressComponents Class

## Properties (27)
- `Public Property BillToAddress2() As String` [R/W] property BillToAddress2
- `Public Property BillToAddress3() As String` [R/W] property BillToAddress3
- `Public Property BillToAddressType() As String` [R/W] property BillToAddressType
- `Public Property BillToBlock() As String` [R/W] property BillToBlock
- `Public Property BillToBuilding() As String` [R/W] property BillToBuilding
- `Public Property BillToCity() As String` [R/W] property BillToCity
- `Public Property BillToCountry() As String` [R/W] property BillToCountry
- `Public Property BillToCounty() As String` [R/W] property BillToCounty
- `Public Property BillToGlobalLocationNumber() As String` [R/W] property BillToGlobalLocationNumber
- `Public Property BillToState() As String` [R/W] property BillToState
- `Public Property BillToStreet() As String` [R/W] property BillToStreet
- `Public Property BillToStreetNo() As String` [R/W] property BillToStreetNo
- `Public Property BillToZipCode() As String` [R/W] property BillToZipCode
- `Public Property ShipToAddress2() As String` [R/W] property ShipToAddress2
- `Public Property ShipToAddress3() As String` [R/W] property ShipToAddress3
- `Public Property ShipToAddressType() As String` [R/W] property ShipToAddressType
- `Public Property ShipToBlock() As String` [R/W] property ShipToBlock
- `Public Property ShipToBuilding() As String` [R/W] property ShipToBuilding
- `Public Property ShipToCity() As String` [R/W] property ShipToCity
- `Public Property ShipToCountry() As String` [R/W] property ShipToCountry
- `Public Property ShipToCounty() As String` [R/W] property ShipToCounty
- `Public Property ShipToGlobalLocationNumber() As String` [R/W] property ShipToGlobalLocationNumber
- `Public Property ShipToState() As String` [R/W] property ShipToState
- `Public Property ShipToStreet() As String` [R/W] property ShipToStreet
- `Public Property ShipToStreetNo() As String` [R/W] property ShipToStreetNo
- `Public Property ShipToZipCode() As String` [R/W] property ShipToZipCode
- `Public Property UserFields() As UserFields` [R] property UserFields

# ServiceCallInventoryExpenses (Object)

ServiceCallInventoryExpenses is a child object of the ServiceCalls object in the Service module. Source table: SCL4.

**Remarks:** To display the form in the application: - Select Service --> Service Call. - Select the Expenses tab.

## Properties (9)
- `Public Property Count() As Long` [R] Returns the total rows in the inventory expenses table associated with the service call.
- `Public Property DocEntry() As Long` [R/W] Sets or returns the internal key of the document associated with the service call inventory expenses. Field name: DocAbs.
- `Public Property DocumentNumber() As Long` [R/W] Sets or returns the number of the document associated with the service call inventory expenses. Field name: DocNumber.
- `Public Property DocumentPostingDate() As Date` [R] Returns the date of the document posting. Field name: DocPstDate.
- `Public Property DocumentType() As BoSvcEpxDocTypes` [R/W] Sets or returns a valid value of BoSvcEpxDocTypes that specifies the document type associated with the service call inventory expenses. Field name: Object.
- `Public Property LineNum() As Long` [R] Returns the current row number. Field name: Line.
- `Public Property PartType() As BoSvcExpPartTypes` [R] Not supported. Field name: PartType.
- `Public Property StockTransferDirection() As BoStckTrnDir` [R/W] Sets or returns a valid value of BoStckTrnDir type that specifies the transfer direction of items related to the service call, to or from the technician. Field name: StckTrnDir.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.ServiceCalls oSrvCall;

    // Delete service call expense
    if (oSrvCall.GetByKey(2) == true)
    {
        oSrvCall.Expenses.SetCurrentLine(1);
        oSrvCall.Expenses.Delete();
        oSrvCall.Update();
    }
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# ServiceCallOrigin (Object)

Represents a service call origin, that is, the channel through which a call was made, such as by telephone or via the Web. Source table: OSCO Mandatory properties: Name

## Properties (4)
- `Public Property Active() As BoYesNoEnum` [R/W] property Active
- `Public Property Description() As String` [R/W] A description for the service call origin. Field name: Descriptio
- `Public Property Name() As String` [R/W] The display name for the service call origin. Field name: Name
  - remarks: Must contain at least one non-blank character.
- `Public Property OriginID() As Long` [R] The key of the service call origin. Field name: originID

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

# ServiceCallOriginParams (Object)

Holds the key and name to an existing service call origin. This object is used to pass keys to and retrieve keys from ServiceCallOriginsService methods.

## Properties (2)
- `Public Property Name() As String` [R] The name of a specific service call origin. Field name: Name
- `Public Property OriginID() As Long` [R/W] The key for a specific service call origin. Field name: originID

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

# ServiceCallOriginParamsCollection (Collection)

A collection of ServiceCallOriginParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ServiceCallOriginParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ServiceCallOriginParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ServiceCallOriginsService (Object)

The ServiceCallOriginsService service enables you to add, look up and remove service call origins in the service call origin master data table. Service call origins are used to specify the channel through which a call was made, such as by telephone or via the Web. To see the list of service call origins, select Service --> Service Call, and then select the General tab. The service call origins are listed in the Origin field. Source table: OSCO

## Methods (8)
- `Public Function AddServiceCallOrigin(ByVal pIServiceCallOrigin As ServiceCallOrigin) As ServiceCallOriginParams` Adds a service call origin.
  - param `pIServiceCallOrigin`: The data for the new service call origin.
  - returns: Contains the key (originID) of the new service call origin.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallOrigin callOrigin = callOriginsService.GetDataInterface(ServiceCallOriginsServiceDataInterfaces.scosServiceCallOrigin) as ServiceCallOrigin;

    callOrigin.Name = "a new call origin";
    callOrigin.Description = "description for this origin";

    Console.WriteLine("Add a new service call origin: Name: " + callOrigin.Name + "  Description: " + callOrigin.Description);

    try
    {
        callOriginsService.AddServiceCallOrigin(callOrigin);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Sub DeleteServiceCallOrigin(ByVal pIServiceCallOriginParams As ServiceCallOriginParams)` Deletes an existing service call origin. The service call origin is specified by its key (originID), which is contained in the ServiceCallOriginParams object passed to the method.
  - param `pIServiceCallOriginParams`: The key of the service call origin to be deleted.
  - remarks: If the origin is system defined or is linked to a specific service call, the origin cannot be deleted. An origin is system defined if the Locked field in the OSCO table is set to Y.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallOriginParams originParams = callOriginsService.GetDataInterface(ServiceCallOriginsServiceDataInterfaces.scosServiceCallOriginParams) as ServiceCallOriginParams;
    originParams.OriginID = 3;
    Console.WriteLine("Delete a ServiceCall Origin with id=" + originParams.OriginID);
    try
    {
        callOriginsService.DeleteServiceCallOrigin(originParams);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As ServiceCallOriginsServiceDataInterfaces) As Object` Creates an empty data structure for use with the ServiceCallOriginsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ServiceCallOriginsServiceDataInterfaces` in `../enums/enums-03.md`
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
- `Public Function GetServiceCallOrigin(ByVal pIServiceCallOriginParams As ServiceCallOriginParams) As ServiceCallOrigin` Retrieves a service call origin. The service call origin is specified by its key (originID), which is contained in the ServiceCallOriginParams object passed to the method.
  - param `pIServiceCallOriginParams`: The key of the service call origin to retrieve.
  - returns: The service call origin with the specified key.
- `Public Function GetServiceCallOriginList() As ServiceCallOriginParamsCollection` Retrieves the keys and names of all the service call origins.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallOriginParamsCollection originParamsCollection = callOriginsService.GetServiceCallOriginList();
    int i = 1;
    foreach (ServiceCallOriginParams originParams in originParamsCollection)
    {
        Console.WriteLine("item {0}: originID:{1}, Name:{2}", i++, originParams.OriginID, originParams.Name);
    }
    ```
- `Public Sub UpdateServiceCallOrigin(ByVal pIServiceCallOrigin As ServiceCallOrigin)` Updates an existing service call origin. The data for the service call origin, including the key of the origin to be updated, is contained in the ServiceCallOrigin passed to the method. To update a service call origin, you must first retrieve it using the GetServiceCallOrigin method.
  - param `pIServiceCallOrigin`: The data for the service call origin to be updated. The ServiceCallOrigin object must contain the key of the object to be updated.
  - remarks: You cannot update a system-defined origin. An origin is system defined if the Locked field in the OSCO table is set to Y.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallOriginParams originParams = callOriginsService
        .GetDataInterface(ServiceCallOriginsServiceDataInterfaces.scosServiceCallOriginParams) as ServiceCallOriginParams;

    originParams.OriginID = 3;
    ServiceCallOrigin callOrigin = callOriginsService.GetServiceCallOrigin(originParams);
    callOrigin.Name = "new Name";

    Console.WriteLine("Update a ServiceCall Origin with id=" + originParams.OriginID);

    try
    {
        callOriginsService.UpdateServiceCallOrigin(callOrigin);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```

# ServiceCallProblemSubType (Object)

ServiceCallProblemSubType Class

## Properties (4)
- `Public Property Active() As BoYesNoEnum` [R/W] property Active
- `Public Property Description() As String` [R/W] property Description
- `Public Property Name() As String` [R/W] property Name
- `Public Property ProblemSubTypeID() As Long` [R] property ProblemSubTypeID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ServiceCallProblemSubTypeParams (Object)

ServiceCallProblemSubTypeParams Class

## Properties (2)
- `Public Property Name() As String` [R] property Name
- `Public Property ProblemSubTypeID() As Long` [R/W] property ProblemSubTypeID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ServiceCallProblemSubTypeParamsCollection (Collection)

ServiceCallProblemSubTypeParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As ServiceCallProblemSubTypeParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As ServiceCallProblemSubTypeParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ServiceCallProblemSubTypesService (Object)

ServiceCallProblemSubTypesService Class

## Methods (8)
- `Public Function AddServiceCallProblemSubType(ByVal pIServiceCallProblemSubType As ServiceCallProblemSubType) As ServiceCallProblemSubTypeParams` AddServiceCallProblemSubType
  - param `pIServiceCallProblemSubType`: 
- `Public Sub DeleteServiceCallProblemSubType(ByVal pIServiceCallProblemSubTypeParams As ServiceCallProblemSubTypeParams)` DeleteServiceCallProblemSubType
  - param `pIServiceCallProblemSubTypeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ServiceCallProblemSubTypesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ServiceCallProblemSubTypesServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetServiceCallProblemSubType(ByVal pIServiceCallProblemSubTypeParams As ServiceCallProblemSubTypeParams) As ServiceCallProblemSubType` GetServiceCallProblemSubType
  - param `pIServiceCallProblemSubTypeParams`: 
- `Public Function GetServiceCallProblemSubTypeList() As ServiceCallProblemSubTypeParamsCollection` GetServiceCallProblemSubTypeList
- `Public Sub UpdateServiceCallProblemSubType(ByVal pIServiceCallProblemSubType As ServiceCallProblemSubType)` UpdateServiceCallProblemSubType
  - param `pIServiceCallProblemSubType`: 

# ServiceCallProblemType (Object)

Represents a service call problem type. Source table: OSCP Mandatory properties: Name

## Properties (4)
- `Public Property Active() As BoYesNoEnum` [R/W] property Active
- `Public Property Description() As String` [R/W] A description for the service call problem type. Field name: Descriptio
- `Public Property Name() As String` [R/W] The display name for the service call problem type. Field name: Name
  - remarks: Must contain at least one non-space character.
- `Public Property ProblemTypeID() As Long` [R] The key of the service call problem type. Field name: prblmTypID

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

# ServiceCallProblemTypeParams (Object)

Holds the key and name to an existing service call problem type. This object is used to pass keys to and retrieve keys from ServiceCallProblemTypesService methods.

## Properties (2)
- `Public Property Name() As String` [R] The name of a specific service call problem type. Field name: Name
  - remarks: Must contain at least one non-space character.
- `Public Property ProblemTypeID() As Long` [R/W] The key for a specific service call problem type. Field name: prblmTypID

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

# ServiceCallProblemTypeParamsCollection (Collection)

A collection of ServiceCallProblemTypeParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ServiceCallProblemTypeParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ServiceCallProblemTypeParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ServiceCallProblemTypesService (Object)

The ServiceCallProblemTypesService service enables you to add, look up and remove service call problem types in the service call problem type master data table. Service call problem types are used to classify service calls. To see the list of service call problem types, select Service --> Service Call, and then select the General tab. The service call problem types are listed in the Problem Type field. Source table: OSCP

## Methods (8)
- `Public Function AddServiceCallProblemType(ByVal pIServiceCallProblemType As ServiceCallProblemType) As ServiceCallProblemTypeParams` Adds a service call problem type.
  - param `pIServiceCallProblemType`: The data for the new service call problem type.
  - returns: Contains the key (prblmTypID) of the new service call problem type.
  - C# example (from SAP's help):
    ```csharp
    public void Add()
    {
        ServiceCallProblemType callProblemType;

        callProblemType = callProblemTypesService.GetDataInterface(ServiceCallProblemTypesServiceDataInterfaces.scptsServiceCallProblemType) As ServiceCallProblemType;

        callProblemType.Name = "problem type";
        callProblemType.Description = "problem description";

        try
        {
            callProblemTypesService.AddServiceCallProblemType(callProblemType);
        }
        catch (Exception ex)
        {
            Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
        }
    }
    ```
- `Public Sub DeleteServiceCallProblemType(ByVal pIServiceCallProblemTypeParams As ServiceCallProblemTypeParams)` Deletes an existing service call problem type. The service call problem type is specified by its key (prblmTypID), which is contained in the ServiceCallProblemTypeParams object passed to the method.
  - param `pIServiceCallProblemTypeParams`: The key of the service call problem type to be deleted.
  - remarks: If the problem type is linked to a specific service call, it cannot be deleted.
  - C# example (from SAP's help):
    ```csharp
    public void Delete()
    {
        ServiceCallProblemTypeParams callProblemTypeParams = callProblemTypesService.GetDataInterface(ServiceCallProblemTypesServiceDataInterfaces.scptsServiceCallProblemTypeParams) as ServiceCallProblemTypeParams;
        callProblemTypeParams.ProblemTypeID = 3;

        try
        {
            callProblemTypesService.DeleteServiceCallProblemType(callProblemTypeParams);
        }
        catch (Exception e)
        {
            PrintExceptionMessage(e);
        }
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As ServiceCallProblemTypesServiceDataInterfaces) As Object` Creates an empty data structure for use with the ServiceCallProblemTypesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ServiceCallProblemTypesServiceDataInterfaces` in `../enums/enums-03.md`
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
- `Public Function GetServiceCallProblemType(ByVal pIServiceCallProblemTypeParams As ServiceCallProblemTypeParams) As ServiceCallProblemType` Retrieves a service call problem type. The service call problem type is specified by its key (prblmTypID), which is contained in the ServiceCallProblemTypeParams object passed to the method.
  - param `pIServiceCallProblemTypeParams`: The key of the service call problem type to retrieve.
  - returns: The service call problem type with the specified key.
- `Public Function GetServiceCallProblemTypeList() As ServiceCallProblemTypeParamsCollection` Retrieves the keys and names of all the service call problem types.
  - C# example (from SAP's help):
    ```csharp
    public void GetList()
    {
        ServiceCallProblemTypeParamsCollection callProblemTypeParamsCollection = callProblemTypesService.GetServiceCallProblemTypeList();

        int i = 1;
        foreach (ServiceCallProblemTypeParams callProblemTypeParams in callProblemTypeParamsCollection)
        {
            Console.WriteLine("item {0}: SequenceNo:{1}, Name:{2}", i++, callProblemTypeParams.ProblemTypeID, callProblemTypeParams.Name);
        }
    }
    ```
- `Public Sub UpdateServiceCallProblemType(ByVal pIServiceCallProblemType As ServiceCallProblemType)` Updates an existing service call problem type. The data for the service call problem type, including the key of the problem type to be updated, is contained in the ServiceCallProblemType passed to the method. To update a service call problem type, you must first retrieve it using the GetServiceCallProblemType method.
  - param `pIServiceCallProblemType`: The data for the service call problem type to be updated. The ServiceCallProblemType object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    public void Update()
    {
        ServiceCallProblemTypeParams callProblemTypeParams;
        callProblemTypeParams = callProblemTypesService.GetDataInterface(ServiceCallProblemTypesServiceDataInterfaces.scptsServiceCallProblemTypeParams) as ServiceCallProblemTypeParams;
        callProblemTypeParams.ProblemTypeID = 3;
        ServiceCallProblemType callProblemType = callProblemTypesService.GetServiceCallProblemType(callProblemTypeParams);
        callProblemType.Name = "new Name";
        callProblemType.Description = "new description";

        try
        {
            callProblemTypesService.UpdateServiceCallProblemType(callProblemType);
        }
        catch (Exception e)
        {
            PrintExceptionMessage(e);
        }
    }
    ```

# ServiceCalls (Object)

ServiceCalls is a business object that represents the service calls table in the Service module. This object enables you to: - Add a service call. - Retrieve a service call by its key. - Update a service call. - Remove a service call. - Save the object in XML format. Source table: OSCL.

**Remarks:** Mandatory field in SAP Business One: CustomerCode and Subject. To display the form in the application: - Select Service --> Service Call.

## Properties (90)
- `Public Property Activities() As ServiceCallActivities` [R] Returns the ServiceCallActivities child object.
- `Public Property AddressName() As String` [R/W] property AddressName
- `Public Property AddressType() As BoAddressType` [R/W] property AddressType
- `Public Property AssignedDate() As Date` [R] Returns the assigned date for resolving the service call. Field name: AssignDate.
- `Public Property AssignedTime() As Long` [R] Returns the assigned time for resolving the service call. Field name: AssignTime.
- `Public Property AssigneeCode() As Long` [R/W] Sets or returns the code of the user who is responsible for the service call. Field name: assignee. This is a foreign key to the Users object.
  - remarks: In SAP Business One, the default assignee is the current user that is logged on the system. The list of users is defined in the ASHP table, which is not exposed by the DI API. To apply a service call to an assigned user, first the BelongsToAQueue property to tNO.
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property BelongsToAQueue() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether he service call belongs to a queue or to an assigned user. Field name: isQueue.
- `Public Property BPAddressComponents() As ServiceCallBPAddressComponents` [R] property BPAddressComponents
- `Public Property BPBillToAddress() As String` [R/W] property BPBillToAddress
- `Public Property BPBillToCode() As String` [R/W] property BPBillToCode
- `Public Property BPCellular() As String` [R/W] property BPCellular
- `Public Property BPContactPerson() As String` [R/W] property BPContactPerson
- `Public Property BPeMail() As String` [R/W] property BPeMail
- `Public Property BPFax() As String` [R/W] property BPFax
- `Public Property BPPhone1() As String` [R/W] property BPPhone1
- `Public Property BPPhone2() As String` [R/W] property BPPhone2
- `Public Property BPProjectCode() As String` [R/W] property BPProjectCode
- `Public Property BPShipToAddress() As String` [R/W] property BPShipToAddress
- `Public Property BPShipToCode() As String` [R/W] property BPShipToCode
- `Public Property BPTerritory() As Long` [R/W] property BPTerritory
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CallType() As Long` [R/W] Sets or returns the service call type. Field name: callType. This is a foreign key to the Service Call Types table (OCST), not exposed through the DI API.
- `Public Property City() As String` [R/W] property City
- `Public Property ClosingDate() As Date` [R/W] The date when the service call status is changed to Closed. Field name: closeDate.
- `Public Property ClosingTime() As Long` [R/W] The date when the service call status is changed to Closed. Field name: closeTime.
- `Public Property ClosingTimeEx() As Date` [R/W] property ClosingTimeEx
- `Public Property ContactCode() As Long` [R/W] Sets or returns the code of the contact person from the business partner master data. Field name: contctCode. This is a foreign key to the ContactEmployees object.
- `Public Property ContractEndDate() As Date` [R] Returns the expiration date of the service contract. Field name: cntrctDate. This is a foreign key to the ServiceContracts object.
- `Public Property ContractID() As Long` [R/W] Returns the ID of the service contract. Field name: contractID. This is a foreign key to the ServiceContracts object.
- `Public Property Country() As String` [R/W] property Country
- `Public Property CreationDate() As Date` [R/W] The date when the service call was first opened. Field name: createDate.
- `Public Property CreationTime() As Date` [R/W] The time when the service call was first opened. Field name: createTime.
- `Public Property CustomerCode() As String` [R/W] Sets or returns the customer code, which is the card code in the business partner master data. Mandatory property. Field name: customer. Length: 15 characters. This is a foreign key to the BusinessPartners object.
- `Public Property CustomerName() As String` [R/W] Sets or returns the customer name from the business partner master data. Field name: custmrName. Length: 100 characters. This is a foreign key to the BusinessPartners object.
- `Public Property CustomerRefNo() As String` [R/W] property CustomerRefNo
- `Public Property Description() As String` [R/W] Sets or returns a memo type string that specifies the remarks for the service call. Field name: descrption. Length: 64,000 characters.
- `Public Property DisplayInCalendar() As BoYesNoEnum` [R/W] property DisplayInCalendar
- `Public Property DocNum() As Long` [R/W] property DocNum
- `Public Property Duration() As Double` [R/W] property Duration
- `Public Property DurationType() As BoDurations` [R/W] property DurationType
- `Public Property EndDuedate() As Date` [R/W] property EndDueDate
- `Public Property EndTime() As Date` [R/W] property EndTime
- `Public Property EntitledforService() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not the business partner is entitled for a service based on the existence of a valid contract. Field name: isEntitled.
- `Public Property Expenses() As ServiceCallInventoryExpenses` [R] Returns the ServiceCallInventoryExpenses child object.
- `Public Property HandWritten() As BoYesNoEnum` [R/W] property HandWritten
- `Public Property InternalSerialNum() As String` [R/W] Sets or returns the unique internal serial number of the item. Field name: internalSN. Length: 32 characters.
  - remarks: In SAP Business One, if you set the value of ManufacturerSerialNum, the value of the internal serial number is set automatically, and vice versa.
- `Public Property ItemCode() As String` [R/W] Sets or returns the item code. Field name: itemCode. Length: 20 characters. This is a foreign key to the Items object.
- `Public Property ItemDescription() As String` [R/W] Sets or returns the item description. Field name: itemName. Length: 100 characters.
- `Public Property ItemGroupCode() As Long` [R] Returns the code of the item group. Field name: itemGroup.
- `Public Property Location() As Long` [R/W] property Location
- `Public Property ManufacturerSerialNum() As String` [R/W] Sets or returns the unique manufacturer serial number of the item. Field name: internalSN. Length: 32 characters.
  - remarks: In SAP Business One, if you set the value of InternalSerialNum, the value of the manufacturer serial number is set automatically, and vice versa.
- `Public Property Origin() As Long` [R/W] Sets or returns the means whereby the complaint was received (such as, e-mail, phone, and so on). Field name: origin. This is a foreign key to the Service Call Origins table (OCSO) - not exposed through the DI API.
- `Public Property PeriodIndicator() As String` [R] property PeriodIndicator
- `Public Property Priority() As BoSvcCallPriorities` [R/W] Sets or returns a valid value of BoSvcCallPriorities type that specifies priority of the complaint (low, medium, or high). Field name: priority.
- `Public Property ProblemSubType() As Long` [R/W] property ProblemSubType
- `Public Property ProblemType() As Long` [R/W] Sets or returns the type of the problem as defined in the SAP Business One application. Field name: problemTyp. This is a foreign key to the Service Call Problem Types table (OSCP) - exposed to DI API using the ServiceCallProblemType object.
- `Public Property Queue() As String` [R/W] Sets or returns the queue ID assigned to the service call. Field name: Queue. Length: 20 characters. This is a foreign key to the Queue table (OQUE), not exposed through the DI API).
  - remarks: To assign a queue to a service call, first set the BelongsToAQueue property to tYES.
- `Public Property Reminder() As BoYesNoEnum` [R/W] property Reminder
- `Public Property ReminderPeriod() As Double` [R/W] property ReminderPeriod
- `Public Property ReminderType() As BoDurations` [R/W] property ReminderType
- `Public Property Resolution() As String` [R/W] Sets or returns a memo type string that specifies the description of the resolution. Field name: resolution. Length: 64,000 characters.
- `Public Property ResolutionDate() As Date` [R/W] Sets or returns the maximum date for resolving a service call. SAP Business One calculates the resolution date based on the the service contract ResolutionTime. Field name: resolution.
  - remarks: In SAP Business One the type of ResolutionDate is Read Only, but to maintain DI API backward compatibility the property type of ResolutionDatee is Read Write.
- `Public Property ResolutionOnDate() As Date` [R] Field name: resolution.
  - remarks: SAP Business One can update this date more than once according to the number of required solutions until the service call is closed.
- `Public Property ResolutionOnTime() As Long` [R] Returns the actual resolution time based on setting details in Resolution property or Solutions property. Field name: resolOnTim.
  - remarks: SAP Business One can update this time more than once according to the number of required solutions until the service call is closed.
- `Public Property ResolutionTime() As Date` [R/W] Sets or returns the maximum time for resolving a service call. SAP Business One calculates the resolution time based on the the service contract ResolutionTime. Field name: resolOnTim.
  - remarks: In SAP Business One the type of ResolutionTime is Read Only, but to maintain DI API backward compatibility the property type of ResolutionTime is Read-Write.
- `Public Property Responder() As Long` [R] Returns the user code of the assignee who responded the service call. Field name: responder.
  - remarks: In case the service call was respond with an activity, then the responder is the user assigned for the activity (HandledBy), else the responder is the AssigneeCode.
- `Public Property ResponseAssignee() As Long` [R] Returns the user code of the assignee who was responsible for the service call when it was actually responded by the Responder. Field name: respAssign.
- `Public Property ResponseByDate() As Date` [R] Returns the maximum date for responding to a service call. SAP Business One calculates the response date based on the service contract ResponseTime. Field name: respByDate.
- `Public Property ResponseByTime() As Long` [R] Returns the maximum time for responding to a service call. SAP Business One calculates the response time based on the the service contract ResponseTime. Field name: respByTime.
- `Public Property ResponseOnDate() As Date` [R] Returns the actual response date. Field name: respOnDate.
  - remarks: SAP Business One sets the ResponseOnDate when one of the following events first occurs: - A meeting or a phone call was added and closed. - A resolution or a solution is set.
- `Public Property ResponseOnTime() As Long` [R] Returns the actual response time. Field name: respOnTime.
- `Public Property Room() As String` [R/W] property Room
- `Public Property Schedulings() As ServiceCallSchedulings` [R] property Schedulings
- `Public Property Series() As Long` [R/W] property Series
- `Public Property ServiceBPType() As ServiceTypeEnum` [R/W] property ServiceBPType
- `Public Property ServiceCallID() As Long` [R] Returns the service call identification number. Field name: callID.
  - remarks: When you add a service call, this property is incremented automatically.
- `Public Property Solutions() As ServiceCallSolutions` [R] Returns the ServiceCallSolutions child object.
- `Public Property StartDate() As Date` [R/W] property StartDate
- `Public Property StartTime() As Date` [R/W] property StartTime
- `Public Property State() As String` [R/W] property State
- `Public Property Status() As Long` [R/W] Sets or returns the status of the service call, such as open, pending, or closed as defined in the SAP Business One application. Field name: status. This is a foreign key to the Service Call Statuses table (OSCS), not exposed through the DI API.
- `Public Property Street() As String` [R/W] property Street
- `Public Property Subject() As String` [R/W] Sets or returns a short description of the problem. Mandatory property. Field name: subject. Length: 254 characters.
- `Public Property SupplementaryCode() As String` [R] property SupplementaryCode
- `Public Property TechnicianCode() As Long` [R/W] Sets or returns the technician code as defined in the employee master data. Field name: technician. This is a foreign key to the EmployeesInfo object.
- `Public Property Telephone() As String` [R/W] property Telephone
- `Public Property UpdateDate() As Date` [R] property UpdateDate
- `Public Property UpdatedTime() As Long` [R] Returns the update time of the service call, which is used for the history log. Field name: UpdateTime.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (8)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal ServiceCallID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ServiceCallID`: Specifies the service call ID in the database.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
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
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# ServiceCallSchedulings (Object)

ServiceCallSchedulings Class

## Properties (50)
- `Public Property ActualDuration() As Double` [R/W] property ActualDuration
- `Public Property ActualDurationType() As BoDurations` [R/W] property ActualDurationType
- `Public Property Address2() As String` [R/W] property Address2
- `Public Property Address3() As String` [R/W] property Address3
- `Public Property AddressName() As String` [R/W] property AddressName
- `Public Property AddressText() As String` [R/W] property AddressText
- `Public Property AddressType() As String` [R/W] property AddressType
- `Public Property AddressTypeBS() As BoAddressType` [R/W] property AddressTypeBS
- `Public Property Block() As String` [R/W] property Block
- `Public Property CheckInDate() As Date` [R/W] property CheckInDate
- `Public Property CheckInLatitude() As String` [R/W] property CheckInLatitude
- `Public Property CheckInLocation() As String` [R/W] property CheckInLocation
- `Public Property CheckInLongitude() As String` [R/W] property CheckInLongitude
- `Public Property CheckInTime() As Date` [R/W] property CheckInTime
- `Public Property CheckOutDate() As Date` [R/W] property CheckOutDate
- `Public Property CheckOutTime() As Date` [R/W] property CheckOutTime
- `Public Property City() As String` [R/W] property City
- `Public Property Count() As Long` [R] property Count
- `Public Property Country() As String` [R/W] property Country
- `Public Property County() As String` [R/W] property County
- `Public Property DisplayInCalendar() As BoYesNoEnum` [R/W] property DisplayInCalendar
- `Public Property Duration() As Double` [R/W] property Duration
- `Public Property DurationType() As BoDurations` [R/W] property DurationType
- `Public Property EndDate() As Date` [R/W] property EndDate
- `Public Property EndTime() As Date` [R/W] property EndTime
- `Public Property GlobalLocNum() As String` [R/W] property GlobalLocNum
- `Public Property HandledBy() As Long` [R/W] property HandledBy
- `Public Property IsClosed() As BoYesNoEnum` [R/W] property IsClosed
- `Public Property IsUnscheduled() As BoYesNoEnum` [R/W] property IsUnscheduled
- `Public Property LineNum() As Long` [R] property LineNum
- `Public Property Location() As Long` [R/W] property Location
- `Public Property Remark() As String` [R/W] property Remark
- `Public Property Reminder() As BoYesNoEnum` [R/W] property Reminder
- `Public Property ReminderDate() As Date` [R] property ReminderDate
- `Public Property ReminderPeriod() As Double` [R/W] property ReminderPeriod
- `Public Property ReminderSent() As BoYesNoEnum` [R] property ReminderSent
- `Public Property ReminderTime() As Date` [R] property ReminderTime
- `Public Property ReminderType() As BoDurations` [R/W] property ReminderType
- `Public Property Room() As String` [R/W] property Room
- `Public Property SalesOrders() As String` [R/W] property SalesOrders
- `Public Property SignatureName() As String` [R/W] property SignatureName
- `Public Property StartDate() As Date` [R/W] property StartDate
- `Public Property StartTime() As Date` [R/W] property StartTime
- `Public Property State() As String` [R/W] property State
- `Public Property Street() As String` [R/W] property Street
- `Public Property StreetNo() As String` [R/W] property StreetNo
- `Public Property TaxOffice() As String` [R/W] property TaxOffice
- `Public Property Technician() As Long` [R/W] property Technician
- `Public Property UserFields() As UserFields` [R] property UserFields
- `Public Property ZipCode() As String` [R/W] property ZipCode

## Methods (2)
- `Public Sub Add()` method Add
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 

# ServiceCallSolutions (Object)

ServiceCallSolutions is a child object of the ServiceCalls object in the Service module. The service call solutions are associated with the Knowledge Base Solutions table. Source table: SCL1.

**Remarks:** Mandatory field in SAP Business One: SolutionID. To display the form in the application: - Select Service --> Service Call. - Select the Solutions tab.

## Properties (4)
- `Public Property Count() As Long` [R] Returns the total rows in the solutions table.
- `Public Property LineNum() As Long` [R] Returns the current row number. Field name: line.
- `Public Property SolutionID() As Long` [R/W] KnowledgeBaseSolutionsSets or returns the solution ID. Mandatory property. Field name: solutionID. This is a foreign key to the KnowledgeBaseSolutions object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (3)
- `Public Sub Add()` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.ServiceCalls oSrvCall;

    // Delete service call solution
    if (oSrvCall.GetByKey(2) == true)
    {
        oSrvCall.Solutions.SetCurrentLine(1);
        oSrvCall.Solutions.Delete();
        oSrvCall.Update();
    }
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# ServiceCallSolutionStatus (Object)

Represents a service call solution status. Source table: OSST Mandatory properties: Name

## Properties (4)
- `Public Property Active() As BoYesNoEnum` [R/W] property Active
- `Public Property Description() As String` [R/W] A description for the service call solution status. Field name: Descriptio
- `Public Property Name() As String` [R/W] The display name for the service call solution status. Field name: Name
  - remarks: Must contain at least one non-space character.
- `Public Property StatusId() As Long` [R] The key of the service call solution status. Field name: Number

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

# ServiceCallSolutionStatusParams (Object)

Holds the key and name to an existing service call solution status. This object is used to pass keys to and retrieve keys from ServiceCallSolutionStatusService methods.

## Properties (2)
- `Public Property Name() As String` [R] The name of a specific service call solution status. Field name: Name
  - remarks: Must contain at least one non-space character.
- `Public Property StatusId() As Long` [R/W] The key for a specific service call solution status. Field name: Number

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

# ServiceCallSolutionStatusParamsCollection (Collection)

A collection of ServiceCallSolutionStatusParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ServiceCallSolutionStatusParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ServiceCallSolutionStatusParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ServiceCallSolutionStatusService (Object)

The ServiceCallSolutionStatusService service enables you to add, look up and remove service call solution statuses in the service call solution status master data table. Service call solution statuses are used to specify the status of a solution for a service call. To see the list of service call solution statuses, select Service --> Service Call, and then select the Solutions tab. Create a new solution or edit an existing solution. The service call solution statuses are listed in the Status field. Source table: OSST

## Methods (8)
- `Public Function AddServiceCallSolutionStatus(ByVal pIServiceCallSolutionStatus As ServiceCallSolutionStatus) As ServiceCallSolutionStatusParams` Adds a service call solution status.
  - param `pIServiceCallSolutionStatus`: The data for the new service call solution status.
  - returns: Contains the key (Number) of the new service call solution status.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallSolutionStatus solutionStatus = solutionStatusService.GetDataInterface(ServiceCallSolutionStatusServiceDataInterfaces.scsssServiceCallSolutionStatus) as ServiceCallSolutionStatus;

    solutionStatus.Name = "a solution status";
    solutionStatus.Description = "description";

    Console.WriteLine("Add a new service call solution status: Name: " + solutionStatus.Name + "  Description: " + solutionStatus.Description);

    solutionStatusService.AddServiceCallSolutionStatus(solutionStatus);
    ```
- `Public Sub DeleteServiceCallSolutionStatus(ByVal pIServiceCallSolutionStatusParams As ServiceCallSolutionStatusParams)` Deletes an existing service call solution status. The service call solution status is specified by its key (Number), which is contained in the ServiceCallSolutionStatusParams object passed to the method.
  - param `pIServiceCallSolutionStatusParams`: The key of the service call solution status to be deleted.
  - remarks: If the solution status is linked to a specific service call, it cannot be deleted.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallSolutionStatusParams solutionStatusParams = solutionStatusService.GetDataInterface(ServiceCallSolutionStatusServiceDataInterfaces.scsssServiceCallSolutionStatusParams) as ServiceCallSolutionStatusParams;
    solutionStatusParams.StatusId = 8;

    Console.WriteLine("Delete a ServiceCall Solution Status with id=" + solutionStatusParams.StatusId);

    solutionStatusService.DeleteServiceCallSolutionStatus(solutionStatusParams);
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As ServiceCallSolutionStatusServiceDataInterfaces) As Object` Creates an empty data structure for use with the ServiceCallSolutionStatusService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ServiceCallSolutionStatusServiceDataInterfaces` in `../enums/enums-03.md`
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
- `Public Function GetServiceCallSolutionStatus(ByVal pIServiceCallSolutionStatusParams As ServiceCallSolutionStatusParams) As ServiceCallSolutionStatus` Retrieves a service call solution status. The service call solution status is specified by its key (Number), which is contained in the ServiceCallSolutionStatusParams object passed to the method.
  - param `pIServiceCallSolutionStatusParams`: The key of the service call solution status to retrieve.
  - returns: The service call solution status with the specified key.
- `Public Function GetServiceCallSolutionStatusList() As ServiceCallSolutionStatusParamsCollection` Retrieves the keys and names of all the service call solution statuses.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallSolutionStatusParamsCollection solutionParamsCollection
        = solutionStatusService.GetServiceCallSolutionStatusList();
    int i = 1;
    foreach (ServiceCallSolutionStatusParams solutionStatusParams in solutionParamsCollection)
    {
        Console.WriteLine("item {0}: statusId:{1}, Name:{2}", i++, solutionStatusParams.StatusId, solutionStatusParams.Name);
    }
    ```
- `Public Sub UpdateServiceCallSolutionStatus(ByVal pIServiceCallSolutionStatus As ServiceCallSolutionStatus)` Updates an existing service call solution status. The data for the service call solution status, including the key of the solution status to be updated, is contained in the ServiceCallSolutionStatus passed to the method. To update a service call solution status, you must first retrieve it using the GetServiceCallSolutionStatus method.
  - param `pIServiceCallSolutionStatus`: The data for the service call solution status to be updated. The ServiceCallSolutionStatus object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallSolutionStatusParams solutionStatusParams = solutionStatusService.GetDataInterface(ServiceCallSolutionStatusServiceDataInterfaces
        .scsssServiceCallSolutionStatusParams) as ServiceCallSolutionStatusParams;

    solutionStatusParams.StatusId = 8;
    ServiceCallSolutionStatus solutionStatus = solutionStatusService.GetServiceCallSolutionStatus(solutionStatusParams);
    solutionStatus.Name = "new Name";

    Console.WriteLine("Update a ServiceCall Solution Status with id=" + solutionStatusParams.StatusId);

    solutionStatusService.UpdateServiceCallSolutionStatus(solutionStatus);
    ```

# ServiceCallStatus (Object)

Represents a service call status. Source table: OSCS Mandatory properties: Name

## Properties (4)
- `Public Property Active() As BoYesNoEnum` [R/W] property Active
- `Public Property Description() As String` [R/W] A description for the service call status. Field name: Descriptio
- `Public Property Name() As String` [R/W] The display name for the service call status. Field name: Name
  - remarks: Must contain at least one non-space character.
- `Public Property StatusId() As Long` [R] The key of the service call solution status. Field name: statusID

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

# ServiceCallStatusParams (Object)

Holds the key and name to an existing service call solution status. This object is used to pass keys to and retrieve keys from ServiceCallSolutionStatusService methods.

## Properties (2)
- `Public Property Name() As String` [R] The name of a specific service call status. Field name: Name
  - remarks: Must contain at least one non-space character.
- `Public Property StatusId() As Long` [R/W] The key for a specific service call status. Field name: statusID

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

# ServiceCallStatusParamsCollection (Collection)

A collection of ServiceCallStatusParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ServiceCallStatusParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ServiceCallStatusParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ServiceCallStatusService (Object)

The ServiceCallStatusService service enables you to add, look up and remove service call statuses in the service call status master data table. Service call statuses are used to specify the status of a service call. To see the list of service call statuses, select Service --> Service Call. The service call statuses are listed in the Call Status field. Source table: OSCS

## Methods (8)
- `Public Function AddServiceCallStatus(ByVal pIServiceCallStatus As ServiceCallStatus) As ServiceCallStatusParams` Adds a service call status.
  - param `pIServiceCallStatus`: The data for the new service call status.
  - returns: Contains the key (statusID) of the new service call status.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallStatus callStatus = callStatusService
        .GetDataInterface(ServiceCallStatusServiceDataInterfaces.scssServiceCallStatus) as ServiceCallStatus;

    callStatus.Name = "Thank you";
    callStatus.Description = "Thank you for using our products.";

    Console.WriteLine("Add a new callStatus: Name: " + callStatus.Name + "  Description: " + callStatus.Description);

    callStatusService.AddServiceCallStatus(callStatus);
    ```
- `Public Sub DeleteServiceCallStatus(ByVal pIServiceCallStatusParams As ServiceCallStatusParams)` Deletes an existing service call status. The service call status is specified by its key (statusID), which is contained in the ServiceCallStatusParams object passed to the method.
  - param `pIServiceCallStatusParams`: The key of the service call status to be deleted.
  - remarks: If the status is system defined or is linked to a specific service call, the status cannot be deleted. A status is system defined if the Locked field in the OSCS table is set to Y.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallStatusParams statusParams = callStatusService
        .GetDataInterface(ServiceCallStatusServiceDataInterfaces.scssServiceCallStatusParams) as ServiceCallStatusParams;
    statusParams.StatusId = 11;
    callStatusService.DeleteServiceCallStatus(statusParams);
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As ServiceCallStatusServiceDataInterfaces) As Object` Creates an empty data structure for use with the ServiceCallStatusService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ServiceCallStatusServiceDataInterfaces` in `../enums/enums-03.md`
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
- `Public Function GetServiceCallStatus(ByVal pIServiceCallStatusParams As ServiceCallStatusParams) As ServiceCallStatus` Retrieves a service call status. The service call status is specified by its key (statusID), which is contained in the ServiceCallStatusParams object passed to the method.
  - param `pIServiceCallStatusParams`: The key of the service call status to retrieve.
  - returns: The service call status with the specified key.
- `Public Function GetServiceCallStatusList() As ServiceCallStatusParamsCollection` Retrieves the keys and names of all the service call statuses.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallStatusParamsCollection callStatusParamsCollection = callStatusService.GetServiceCallStatusList();
    int i = 1;
    foreach (ServiceCallStatusParams statusParams in callStatusParamsCollection)
    {
        Console.WriteLine("item {0}: StatusId:{1}, Name:{2}", i++, statusParams.StatusId, statusParams.Name);
    }
    ```
- `Public Sub UpdateServiceCallStatus(ByVal pIServiceCallStatus As ServiceCallStatus)` Updates an existing service call status. The data for the service call status, including the key of the status to be updated, is contained in the ServiceCallStatus passed to the method. To update a service call status, you must first retrieve it using the GetServiceCallStatus method.
  - param `pIServiceCallStatus`: The data for the service call status to be updated. The ServiceCallStatus object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallStatusParams statusParams = callStatusService
        .GetDataInterface(ServiceCallStatusServiceDataInterfaces.scssServiceCallStatusParams) as ServiceCallStatusParams;

    statusParams.StatusId = 9;
    ServiceCallStatus callStatus = callStatusService.GetServiceCallStatus(statusParams);

    callStatus.Name = "new Name";
    callStatusService.UpdateServiceCallStatus(callStatus);
    ```

# ServiceCallType (Object)

Represents a service call type. Source table: OSCT Mandatory properties: Name

## Properties (4)
- `Public Property Active() As BoYesNoEnum` [R/W] property Active
- `Public Property CallTypeID() As Long` [R] The key of the service call type. Field name: callTypeID
- `Public Property Description() As String` [R/W] A description for the service call type. Field name: Descriptio
- `Public Property Name() As String` [R/W] The display name for the service call type. Field name: Name
  - remarks: Must contain at least one non-space character.

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

# ServiceCallTypeParams (Object)

Holds the key and name to an existing service call type. This object is used to pass keys to and retrieve keys from ServiceCallTypesService methods.

## Properties (2)
- `Public Property CallTypeID() As Long` [R/W] The key for a specific service call type. Field name: callTypeID
- `Public Property Name() As String` [R] The name of a specific service call type. Field name: Name

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

# ServiceCallTypeParamsCollection (Collection)

A collection of ServiceCallTypeParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ServiceCallTypeParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ServiceCallTypeParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ServiceCallTypesService (Object)

The ServiceCallTypesService service enables you to add, look up and remove service call types in the service call type master data table. Service call types are used to classify service calls. To see the list of service call types, select Service --> Service Call, and then select the General tab. The service call types are listed in the Call Type field. Source table: OSCT

## Methods (8)
- `Public Function AddServiceCallType(ByVal pIServiceCallType As ServiceCallType) As ServiceCallTypeParams` Adds a service call type.
  - param `pIServiceCallType`: The data for the new service call type.
  - returns: Contains the key (callTypeID) of the new service call type.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallType callType = callTypesService.GetDataInterface(ServiceCallTypesServiceDataInterfaces.sctsServiceCallType) as ServiceCallType;

    callType.Name = "a new call type";
    callType.Description = "description for this type";

    try
    {
         callTypesService.AddServiceCallType(callType);
    }
    catch(Exception ex)
    {
         Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Sub DeleteServiceCallType(ByVal pIServiceCallTypeParams As ServiceCallTypeParams)` Deletes an existing service call type. The service call type is specified by its key (callTypeID), which is contained in the ServiceCallTypeParams object passed to the method.
  - param `pIServiceCallTypeParams`: The key of the service call type to be deleted.
  - remarks: If the type is linked to a specific service call, it cannot be deleted.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallTypeParams callTypeParams = callTypesService.GetDataInterface(ServiceCallTypesServiceDataInterfaces.sctsServiceCallTypeParams) as ServiceCallTypeParams;
    callTypeParams.CallTypeID = 2;

    try
    {
         callTypesService.DeleteServiceCallType(callTypeParams);
    }
    catch (Exception ex)
    {
         Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As ServiceCallTypesServiceDataInterfaces) As Object` Creates an empty data structure for use with the ServiceCallTypesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ServiceCallTypesServiceDataInterfaces` in `../enums/enums-03.md`
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
- `Public Function GetServiceCallType(ByVal pIServiceCallTypeParams As ServiceCallTypeParams) As ServiceCallType` Retrieves a service call type. The service call type is specified by its key (callTypeID), which is contained in the ServiceCallTypeParams object passed to the method.
  - param `pIServiceCallTypeParams`: The key of the service call type to retrieve.
  - returns: The service call type with the specified key.
- `Public Function GetServiceCallTypeList() As ServiceCallTypeParamsCollection` Retrieves the keys and names of all the service call types.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallTypeParamsCollection callTypeParamsCollection = callTypesService.GetServiceCallTypeList();
    int i = 1;
    foreach (ServiceCallTypeParams typeParams in callTypeParamsCollection)
    {
         Console.WriteLine("item {0}: CallTypeId:{1}, Name:{2}", i++, typeParams.CallTypeID, typeParams.Name);
    }
    ```
- `Public Sub UpdateServiceCallType(ByVal pIServiceCallType As ServiceCallType)` Updates an existing service call type. The data for the service call type, including the key of the type to be updated, is contained in the ServiceCallType passed to the method. To update a service call type, you must first retrieve it using the GetServiceCallType method.
  - param `pIServiceCallType`: The data for the service call type to be updated. The ServiceCallType object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallTypeParams callTypeParams = callTypesService.GetDataInterface(ServiceCallTypesServiceDataInterfaces.sctsServiceCallTypeParams) as ServiceCallTypeParams;
    callTypeParams.CallTypeID = 2;
    ServiceCallType callType = callTypesService.GetServiceCallType(callTypeParams);
    callType.Name = "new Name";

    try
    {
         callTypesService.UpdateServiceCallType(callType);
    }
    catch (Exception ex)
    {
         Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```

# ServiceContract_Lines (Object)

ServiceContract_Lines is a child object of the ServiceContracts object that represents the line entries of each service contract. This object is part of the Service module. Source table: CTR1.

**Remarks:** To display the form in the application: - Select Service --> Service Contract. - Select the Items tab.

## Properties (12)
- `Public Property Count() As Long` [R] Returns the total data rows in the table.
  - remarks: When you add a new item or item group, the value of this property is incremented automatically.
- `Public Property EndDate() As Date` [R/W] Sets or returns the end date of the service contract for a specified item group. Field name: EndDate.
  - remarks: SAP Business One automatically sets the service contract end date for the specified item group.
- `Public Property InternalSerialNum() As String` [R/W] Sets or returns the unique internal serial number of the item. Field name: InternalSN. Length: 32 characters.
  - remarks: In SAP Business One, if you set the value of ManufacturerSerialNum, the value of the internal serial number is set automatically, and vice versa.
- `Public Property ItemCode() As String` [R/W] Sets or returns the item code. Field name: ItemCode. Length: 20 characters. This is a foreign key to the Items object.
- `Public Property ItemGroup() As Long` [R/W] Sets or returns the code of the item group. Field name: ItemGroup. This is a foreign key to the ItemGroups object.
- `Public Property ItemGroupName() As String` [R] Returns the name of the ItemGroup. Field name: ItmGrpName. Length: 20 characters.
- `Public Property ItemName() As String` [R/W] Sets or returns the item name. Field name: ItemName. Length: 200 characters.
- `Public Property LineNum() As Long` [R] Returns the current row number. Field name: Line.
- `Public Property ManufacturerSerialNum() As String` [R/W] Sets or returns the unique manufacturer serial number of the item. Field name: ManufSN. Length: 32 characters.
  - remarks: In SAP Business One, if you set the value of InternalSerialNum, the value of the manufacturer serial number is set automatically, and vice versa.
- `Public Property StartDate() As Date` [R/W] Sets or returns the start date of the service contract for a specified item group. Field name: StartDate.
  - remarks: SAP Business One automatically sets the service contract start date for the specified item group.
- `Public Property TerminationDate() As Date` [R/W] Sets or returns the termination date of the service contract. Field name: TermDate.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# ServiceContracts (Object)

ServiceContracts is a business object that represents the service contracts table in the Service module of SAP Business One application. This object enables you to: - Add a service contract. - Retrieve a service contract by its key. - Update a service contract. - Remove a service contract. - Save the object in XML format. Source table: OCTR.

**Remarks:** Mandatory fields in SAP Business One: CustomerCode, EndDate, and ResolutionTime. To display the form in the application: - Select Service --> Service Contract.

## Properties (54)
- `Public Property AttachmentEntry() As Long` [R/W] Sets or returns the identification key of the attachment file, as assigned by SAP Business One when adding an Attachment Entry to alert message. Field name: AtcEntry.
- `Public Property Attachments() As Attachments` [R] Returns the Attachments object.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property ContactCode() As Long` [R/W] Sets or returns the code of the contact person (from the business partner master data). Field name: CntctCode. This is a foreign key to the ContactEmployees object.
- `Public Property ContractID() As Long` [R] Returns the ID of the service contract. Field name: ContractID.
- `Public Property ContractTemplate() As String` [R/W] Sets or returns the name of the contract template. Field name: CntrcTmplt. Length: 20 characters. This is a foreign key to the ContractTemplates object.
- `Public Property ContractType() As BoContractTypes` [R/W] Sets or returns a valid value of BoContractTypes type that specifies the contract type: Customer, Item Group, or Serial Number. Field name: CntrcType.
- `Public Property CustomerCode() As String` [R/W] Sets or returns the customer code, which is the business partner code. Mandatory field in SAP Business One. Field name: CstmrCode. Length: 15 characters. This is a foreign key to the BusinessPartners object.
- `Public Property CustomerName() As String` [R/W] Sets or returns the customer name, which is the business partner name. Field name: CstmrName. Length: 100 characters. This is a foreign key to the BusinessPartners object.
- `Public Property Description() As String` [R/W] Sets or returns a string that describes the service contract. Field name: Descriptio. Length: 254 characters.
- `Public Property DurationOfCoverage() As Long` [R] Sets or returns the duration of the service contract coverage. Field name: duration.
- `Public Property EndDate() As Date` [R/W] Sets or returns the end date of the service contract. Mandatory field in SAP Business One. Field name: EndDate.
  - remarks: SAP Business One calculates the EndDate using the values of the StartDate and DurationOfCovarge properties.
- `Public Property FridayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Fridays to the contract coverage. Field name: FriEnabled.
- `Public Property FridayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Fridays. Field name: FriEnd.
- `Public Property FridayStart() As Date` [R/W] Sets or returns the beginning working hour, for the service coverage, on Fridays. Field name: FriStart.
- `Public Property IncludeHolidays() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include holidays to the service contract coverage. Field name: InclHldays.
- `Public Property IncludeLabor() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include technician's work to the service contract coverage. Field name: InclWork.
- `Public Property IncludeParts() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include replacement parts (items) to the service contract coverage. Field name: InclParts.
- `Public Property IncludeTravel() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include travel to the service contract coverage. Field name: InclTravel.
- `Public Property Lines() As ServiceContract_Lines` [R] Returns the ServiceContract_Lines child object.
- `Public Property MondayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Mondays to the service contract coverage. Field name: WedEnabled.
- `Public Property MondayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Monday. Field name: MonEnd. Sets or returns the ending working hour, for the service coverage, on Mondays. Field name: MonEnd.
- `Public Property MondayStart() As Date` [R/W] Sets or returns the beginning working hour, for the service coverage, on Monday. Field name: MonStart. Sets or returns the beginning working hour, for the service coverage, on Mondays. Field name: MonStart.
- `Public Property Owner() As Long` [R/W] Sets or returns the name or title of the employee that is responsible for the service contract. Field name: Owner. This is a foreign key to the Users Object.
- `Public Property Remarks() As String` [R/W] Sets or returns a memo type string that specifies remarks for the service contract (in addition to the remarks from the contract template). Length: 64,000 characters. Field name: Remarks1.
- `Public Property ReminderTime() As Long` [R/W] Sets or returns the number of days, weeks, or months for the alert to appear prior to the termination of the contract. To enable this reminder, set the Renewal property to tYES. Field name: RemindVal.
- `Public Property RemindUnit() As BoRemindUnits` [R/W] Sets or returns a valid value of BoRemindUnits type that specifies the units (days, weeks, or months) for the ReminderTime property. Field name: RemindUnit.
- `Public Property Renewal() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to renew the service contract. Field name: Renewal.
- `Public Property ResolutionTime() As Long` [R/W] Sets or returns the maximum time, in days or hours, to resolve a service call. Field name: ResponsVal.
- `Public Property ResolutionUnit() As BoResolutionUnits` [R/W] Sets or returns a valid value of BoResolutionUnits type that specifies the units, hours or days, for the ResolutionTime property. Field name: ResponsUnt.
- `Public Property ResponseTime() As Long` [R/W] Sets or returns the maximum time, in hours or days, to respond to a service call. Field name: ResponseV.
- `Public Property ResponseUnit() As BoResponseUnit` [R/W] Sets or returns a valid value of BoResponseUnit type that specifies the units, hours or days, for the ResponseTime property. Field name: ResponseU.
- `Public Property SaturdayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Saturdays to the service contract coverage. Field name: SatEnabled.
- `Public Property SaturdayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Saturday. Field name: SatEnd. Sets or returns the ending working hour, for the service coverage, on Saturdays. Field name: SatEnd.
- `Public Property SaturdayStart() As Date` [R/W] Sets or returns the starting working hour, for the service coverage, on Saturday. Field name: SatStart. Sets or returns the beginning working hour, for the service coverage, on Saturdays. Field name: SatStart.
- `Public Property ServiceBPType() As ServiceTypeEnum` [R/W] property ServiceBPType
- `Public Property ServiceType() As BoServiceTypes` [R/W] Sets or returns a valid value of BoServiceTypes type that specifies the service type of the contract: Regular or Warranty. Field name: SrvcType.
- `Public Property StartDate() As Date` [R/W] Sets or returns the start date of the service contract. Field name: StartDate.
- `Public Property Status() As BoSvcContractStatus` [R/W] Sets or returns a valid value of BoSvcContractStatus type that specifies the status of the service contract (approved, on-hold, or draft). Field name: Status.
- `Public Property SundayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Sundays to the service contract coverage. Field name: SunEnabled.
- `Public Property SundayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Sunday. Field name: SunEnd. Sets or returns the ending working hour, for the service coverage, on Sundays. Field name: SunEnd.
- `Public Property SundayStart() As Date` [R/W] Sets or returns the starting working hour, for the service coverage, on Sunday. Field name: SunStrart. Sets or returns the beginning working hour, for the service coverage, on Sundays. Field name: SunStrart.
- `Public Property TemplateRemarks() As String` [R] Returns a memo type string that specifies remarks for the contract template as defined in the Remarks property of the ContractTemplates object. Field name: Remarks1. Length: 64,000 characters.
- `Public Property TerminationDate() As Date` [R/W] Sets or returns the termination date of the service contract. Field name: TermDate.
- `Public Property ThursdayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Thursdays to the service contract coverage. Field name: ThuEnabled.
- `Public Property ThursdayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Thursdays. Field name: ThuEnd. Sets or returns the ending working hour, for the service coverage, on Thursdays. Field name: ThuEnd.
- `Public Property ThursdayStart() As Date` [R/W] Sets or returns the starting working hour, for the service coverage, on Thursdays. Field name: ThuStart. Sets or returns the beginning working hour of the company on Thursdays. Field name: ThuStart.
- `Public Property TuesdayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Tuesdays to the service contract coverage. Field name: TueEnabled.
- `Public Property TuesdayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Tuesdays. Field name: TueEnd. Sets or returns the ending working hour, for the service coverage, on Tuesdays. Field name: ThuEnd.
- `Public Property TuesdayStart() As Date` [R/W] Sets or returns the starting working hour, for the service coverage, on Tuesdays. Field name: TueStart. Sets or returns the beginning working hour of the company on Tuesdays. Field name: ThuStart.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WednesdayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Wednesdays to the service contract coverage. Field name: WedEnabled.
- `Public Property WednesdayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Wednesdays. Field name: WedEnd. Sets or returns the ending working hour, for the service coverage, on Wednesdays. Field name: WedEnd.
- `Public Property WednesdayStart() As Date` [R/W] Sets or returns the starting working hour, for the service coverage, on Wednesdays. Field name: WedStart. Sets or returns the beginning working hour, for the service coverage, on Wednesdays. Field name: WedStart.

## Methods (8)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal ContractID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ContractID`: Specifies the service contract identification key.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Not supported. Field name: .
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

# ServiceGroup (Object)

Represents a service group that can be used for the automatic determination of tax codes for services. Source table: OSGP.

**Remarks:** Country-specific for Brazil only. The combination of Service Code and Service Group can support some special cases for Tax Code Determination.

## Properties (3)
- `Public Property AbsEntry() As Long` [R] The internal key of a specific service group. Field name: AbsEntry.
- `Public Property Description() As String` [R/W] The description of the service group. Field name: Descrip. Length: 70 characters.
- `Public Property ServiceGroupCode() As String` [R/W] The code of the service group. Field name: ServiceGrp. Length: 3 characters.

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

# ServiceGroupParams (Object)

Holds the key and name to an existing service group. This object is used to pass keys to and retrieve keys from ServiceGroupsService methods.

## Properties (2)
- `Public Property AbsEntry() As Long` [R/W] The internal key that identifies the service group. Field name: AbsEntry.
- `Public Property ServiceGroupCode() As String` [R] The code of the service group. Field name: ServiceGrp.

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

# ServiceGroupsParams (Collection)

A collection of ServiceGroupParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ServiceGroupParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ServiceGroupParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ServiceGroupsService (Object)

The ServiceGroupsService service enables you to add, look up, update, and remove service groups. Source table: OSGP.

**Remarks:** Country-specific for Brazil only. To see the service groups, from the SAP Business One Main Menu, choose Administration --> Setup --> Financials --> Tax --> Item Classification --> Service Group.

## Methods (8)
- `Public Function AddServiceGroup(ByVal pIServiceGroup As ServiceGroup) As ServiceGroupParams` Adds a service group.
  - param `pIServiceGroup`: The data for the new service group.
- `Public Sub DeleteServiceGroup(ByVal pIServiceGroupParams As ServiceGroupParams)` Deletes an existing service group.
  - param `pIServiceGroupParams`: The key of the service group to be deleted.
- `Public Function GetDataInterface(ByVal enumMSDI As ServiceGroupsServiceDataInterfaces) As Object` Creates an empty data structure for use with the ServiceGroupsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ServiceGroupsServiceDataInterfaces` in `../enums/enums-03.md`
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
- `Public Function GetServiceGroup(ByVal pIServiceGroupParams As ServiceGroupParams) As ServiceGroup` Retrieves a service group. The service group is specified by its key, which is contained in the ServiceGroupParams object passed to the method.
  - param `pIServiceGroupParams`: The key of the service group to retrieve.
- `Public Function GetServiceGroupList() As ServiceGroupsParams` Returns the ServiceGroupsParams data collection that identify all service groups.
- `Public Sub UpdateServiceGroup(ByVal pIServiceGroup As ServiceGroup)` Updates an existing service group. The data for the service group, including the key of the service group to be updated, is contained in the ServiceGroup object passed to the method. To update a service group, you must first retrieve it using the GetServiceGroup method.
  - param `pIServiceGroup`: The data for the service group to be updated. The ServiceGroup object must contain the key of the object to be updated.

# ServiceTaxPostingParams (Object)

ServiceTaxPostingParams Class

## Properties (1)
- `Public Property DocEntry() As Long` [R/W] property DocEntry

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ServiceTaxPostingParamsCollection (Collection)

ServiceTaxPostingParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As ServiceTaxPostingParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As ServiceTaxPostingParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ServiceTaxPostingService (Object)

ServiceTaxPostingService Class

## Methods (5)
- `Public Function GetDataInterface(ByVal enumMSDI As ServiceTaxPostingServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ServiceTaxPostingServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetTaxableDeliveries() As ServiceTaxPostingParamsCollection` GetTaxableDeliveries
- `Public Sub PostServiceTax(ByVal pIServiceTaxPostingParams As ServiceTaxPostingParams)` PostServiceTax
  - param `pIServiceTaxPostingParams`: 

# ShippingTypes (Object)

The ShippingTypes object enables to define transportation methods (for example, air cargo and courier) to carry out deliveries. A shipping type can be assigned to a document, item master data, and business partner master data. Source table: OSHP.

**Remarks:** To display the form in the application: - Select Administration -->Setup -->Inventory -->Shipping Types.

## Properties (5)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Code() As Long` [R] Returns the code of the shipping type (primary key). Field name: TrnspCode.
- `Public Property Name() As String` [R/W] Sets or returns the name of the shipping type. Field name: TrnspName. Length: 40 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property Website() As String` [R/W] Sets or returns the web site address for the shipping company. Field name: WebSite. Length: 50 characters.

## Methods (7)
- `Public Function Add() As Long` Adds a shipping type definition.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lCode`: Code.
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

# ShowDifferenceParams (Object)

Holds the key to an existing change log that contains several log instances. This object is used to pass keys to and retrieve keys from the ChangeLogsService methods.

## Properties (5)
- `Public Property LogInstance() As Long` [R/W] The instance number of the first log that you want to compare and show the differences. Field name: Instance. Length: 11 characters.
- `Public Property LogInstance2() As Long` [R/W] The instance number of the second log that you want to compare and show the differences. Field name: Instance2. Length: 11 characters.
- `Public Property Object() As BoChangeLogEnum` [R/W] The unique code of the object that is changed. Field name: ObjectCode. Length: 50 characters.
- `Public Property PrimaryKey() As String` [R/W] The primary number of the document. Note: This field is for non user-defined objects. Field name: PK1. Length: 64 characters.
- `Public Property UDOObjectCode() As String` [R/W] The unique code of the user-defined object that is changed. Field name: UDOObjectCode. Length: 11 characters.

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

# SingleUserConnection (Object)

SingleUserConnection Class

## Properties (2)
- `Public Property Action() As SingleUserConnectionActionEnum` [R/W] property Action
- `Public Property Code() As Long` [R] property Code

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# SingleUserConnectionParams (Object)

SingleUserConnectionParams Class

## Properties (1)
- `Public Property Code() As Long` [R/W] property Code

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# SingleUserConnectionService (Object)

SingleUserConnectionService Class

## Methods (5)
- `Public Function Get(ByVal pISingleUserConnectioParams As SingleUserConnectionParams) As SingleUserConnection` Get
  - param `pISingleUserConnectioParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As SingleUserConnectionServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `SingleUserConnectionServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Sub Update(ByVal pISingleUserConnection As SingleUserConnection)` Update
  - param `pISingleUserConnection`: 

# SNBLines (Object)

SNBLines Class

## Properties (10)
- `Public Property AdmissionDate() As Date` [R] property AdmissionDate
- `Public Property BaseLine() As Long` [R/W] property BaseLine
- `Public Property Count() As Long` [R] Lines Count
- `Public Property DebitCredit() As Double` [R/W] property DebitCredit
- `Public Property ExpirationDate() As Date` [R] property ExpirationDate
- `Public Property LotNumber() As String` [R] property LotNumber
- `Public Property ManufactureNumber() As String` [R] property ManufactureNumber
- `Public Property NewCost() As Double` [R/W] property NewCost
- `Public Property SnbAbsEntry() As Long` [R/W] property SnbAbsEntry
- `Public Property SystemNumber() As Long` [R] property SystemNumber

## Methods (2)
- `Public Sub Add()` Add
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Set the current line
  - param `LineNum`: 

# SpecialPrices (Object)

Represents a discount for a specific item in a specific price list. The discount can apply to a specific business partner or for all business partners. - Specific Partners: To view discounts for specific business partners, select Inventory --> Price Lists --> Special Prices --> Special Prices for Business Partners. - All Business Partners: To view discounts for all business partners, select Inventory --> Price Lists --> Period and Volume Discounts. In previous versions, this was called Hierarchies and Expansions. For a specific business partner, the item and business partner must be unique; for all business partners, the item and price list must be unique. Source table: OSPP Mandatory fields: ItemCode

**Remarks:** For marketing documents, the system checks for special prices in the following order: - Special prices (this object) for the specified business partner - Discount groups (DiscountGroups) for the specified business partner and item - Special prices (this object) for all business partners If no special prices are found, the price is set by the default price list for the business partner.

**Example:**
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
  'Call the object

  Dim vSP As SAPbobsCOM.SpecialPrices

  Set vSP = vCompany.GetBusinessObject(oSpecialPrices)

  'set object's properties

  vSP.CardCode = "D10002"

  vSP.Currency = "Eur"

  vSP.DiscountPercent = 30.3

  vSP.ItemCode = "A00001"

  vSP.Price = 355.3

  vSP.PriceListNum = 0

  'Call the Add method

  Call vSP.Add
  ```
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
  Dim oSpp As SAPbobsCOM.SpecialPrices

  oSpp = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oSpecialPrices)

  oSpp.PriceListNum = 4

  oSpp.ItemCode = "I0001"

  oSpp.Price = 33.033

  oSpp.SpecialPricesDataAreas.PriceListNo = 4

  oSpp.SpecialPricesDataAreas.DateFrom = #10/20/2007 12:14:00 PM#

  oSpp.SpecialPricesDataAreas.Dateto = #11/20/2007 12:14:00 PM#

  oSpp.SpecialPricesDataAreas.Discount = 5

  oSpp.SpecialPricesDataAreas.Add()

  oSpp.SpecialPricesDataAreas.PriceListNo = 4

  oSpp.SpecialPricesDataAreas.DateFrom = #11/21/2007 12:14:00 PM#

  oSpp.SpecialPricesDataAreas.Dateto = #11/30/2007 12:14:00 PM#

  oSpp.SpecialPricesDataAreas.Discount = 6

  oSpp.SpecialPricesDataAreas.Add()

  oSpp.SpecialPricesDataAreas.PriceListNo = 4

  oSpp.SpecialPricesDataAreas.DateFrom = #12/21/2008 12:14:00 PM#

  oSpp.SpecialPricesDataAreas.Dateto = #12/30/2008 12:14:00 PM#

  oSpp.SpecialPricesDataAreas.SpecialPrice = 28.808

  oSpp.SpecialPricesDataAreas.SpecialPricesQuantityAreas.Quantity = 101

  oSpp.SpecialPricesDataAreas.SpecialPricesQuantityAreas.SpecialPrice = 25.012

  oSpp.SpecialPricesDataAreas.SpecialPricesQuantityAreas.Add()

  oSpp.SpecialPricesDataAreas.SpecialPricesQuantityAreas.Quantity = 401

  oSpp.SpecialPricesDataAreas.SpecialPricesQuantityAreas.SpecialPrice = 24.98

  Dim retV As Integer = oSpp.Add()
  ```

## Properties (14)
- `Public Property AutoUpdate() As BoYesNoEnum` [R/W] Specifies whether to change the special price when the price list is updated. Field name: AutoUpdt.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CardCode() As String` [R/W] Sets or returns the business partner to which this discount applies. If blank, the discount applies to all business partners. Field name: CardCode. Length: 15 characters. This is a foreign key to the BusinessPartners object.
- `Public Property Currency() As String` [R/W] Sets or returns the currency of the discount. The currency must match the currency of the specified price list. Field name: Currency. Length: 3 characters.
- `Public Property DiscountPercent() As Double` [R/W] Sets or returns the discount percentage. This property is date-dependent. Field name: Discount.
  - remarks: SAP Business One calculates the special price (Price property) on the basis of the specified price list (PriceListNum property) and discount percentage (DiscountPercent property). If you change the discount percentage, the price is automatically modified and vice versa.
- `Public Property ItemCode() As String` [R/W] Sets or returns the item code to which this discount applies. The item code must be unique. Field name: ItemCode. Length: 20 characters. This is a foreign key to the Items object.
  - remarks: This property is mandatory.
- `Public Property Price() As Double` [R/W] Sets or returns the special price of the item. Field name: Price.
  - remarks: SAP Business One calculates the special price (Price property) on the basis of the specified price list (PriceListNum property) and discount percentage (DiscountPercent property). If you change the discount percentage, the price is automatically modified and vice versa. If you don’t have authorization to view the price, this property will return 0 with the nil="true" attribute in the exported xml file: <Price nil="true">0.000000</Price>.
- `Public Property PriceListNum() As Long` [R/W] Sets or returns the price list. Field name: ListNum. This is a foreign key to the PriceLists object.
  - remarks: The price list is used to calculate the special price. If you do not set a price list, then the special price (Price property) is not calculated on the basis of a price list. Instead, you must set the special price manually.
- `Public Property SourcePrice() As SourceCurrencyEnum` [R/W] property SourcePrice
- `Public Property SpecialPricesDataAreas() As SpecialPricesDataAreas` [R] Returns the SpecialPricesDataAreas child object.
- `Public Property UserFields() As UserFields` [R] property UserFields
- `Public Property Valid() As BoYesNoEnum` [R/W] property Valid
- `Public Property ValidFrom() As Date` [R/W] property ValidFrom
- `Public Property ValidTo() As Date` [R/W] property ValidTo

## Methods (8)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal ItemCode As String, ByVal CardCode As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ItemCode`: The key of the item whose discounts are to be retrieved. This is a foreign key to the Items object.
  - param `CardCode`: The key of the business partner whose discounts are to be retrieved. This is a foreign key to the BusinessPartners object. Specifies the identification key of the business object (CardCode).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function GetByKeyDiscounts(ByVal ItemCode As String, ByVal PriceListNum As Long) As Boolean` Retrieves the discounts for a specific item that apply to all business partners. To retrieve discounts for a specific business partner, use the GetByKey method.
  - param `ItemCode`: The key of the item whose discounts are to be retrieved. This is a foreign key to the Items object.
  - param `PriceListNum`: The key of the price list whose discounts are to be retrieved. This is a foreign key to the PriceLists object.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oSppDel As SAPbobsCOM.SpecialPrices

    oSppDel = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oSpecialPrices)

    Dim bret As Boolean = oSppDel.GetByKeyDiscounts("I0001", "Code1")
    ```
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data.
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

# SpecialPricesDataAreas (Object)

SpecialPricesDataAreas is a child object of SpecialPrices object and represents special prices that are valid only for specified periods such as, holidays and season sales. Source table: SPP1.

**Remarks:** To display the form in the application: - Select Inventory --> Price Lists --> Special Prices --> Special Prices for Business Partners. - Double-click a line number in the Special Prices for Business Partners table.

## Properties (13)
- `Public Property AutoUpdate() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the price is updated automatically when the discount or price list number are modified. Field name: AutoUpdt.
  - remarks: Default value - tYES, SAP Business One calculates the SpecialPrice according to the Discount and the PriceListNo. If you set to tNO, SAP Business One ignores the Discount and PriceListNo properties and you must set the SpecialPrice property.
- `Public Property BPCode() As String` [R] Returns the identification code of the business partner for whom the special price applies. The BPCode returns from the CardCode property of the SpecialPrices object. Field name: CardCode. Length: 15 characters. This is a foreign key to the SpecialPrices object.
- `Public Property Count() As Long` [R] Returns the total rows in the table, that is the total number of records in the object.
- `Public Property DateFrom() As Date` [R/W] Sets or returns the start date of the special price. Field name: FromDate.
- `Public Property Dateto() As Date` [R/W] Sets or returns the end date of the special price. Field name: ToDate.
  - remarks: If you do not set the end date, then the period for the special price is not limited.
- `Public Property Discount() As Double` [R/W] Sets or returns the discount percentage for an item for the specified period. Field name: Discount.
- `Public Property ItemNo() As String` [R] Returns the item code in the inventory for which the special price applies. The ItemNo returns from the ItemCode property of the SpecialPrices object. Field name: ItemCode. This is a foreign key to the SpecialPrices object. Length: 20 characters.
- `Public Property PriceCurrency() As String` [R/W] Sets or returns the currency of the special price. The currency must match to the currency in the specified price list. Field name: Currency. Length: 3 characters.
- `Public Property PriceListNo() As Long` [R/W] Sets or returns the price list number. Field name: ListNum. This is a foreign key to the PriceLists object.
- `Public Property RowNumber() As Long` [R] Returns the current available row number (0-based). Field name: LINENUM.
- `Public Property SpecialPrice() As Double` [R/W] Sets or returns the special price after discount. Field name: Price.
  - remarks: If you don’t have authorization to view the price, this property will return 0 with the nil="true" attribute in the exported xml file: <Price nil="true">0.000000</Price>.
- `Public Property SpecialPricesQuantityAreas() As SpecialPricesQuantityAreas` [R] Returns the SpecialPricesQuantityAreas child object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oOrder As SAPbobsCOM.Documents ' Order object

            Dim lRetCode As Integer ' Return Code

            ' New Order

            oOrder = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oOrders)

            ' Fill Order details

            oOrder.CardCode = "C40000"

            oOrder.CardName = "Earthshaker Corporation"

            oOrder.HandWritten = SAPbobsCOM.BoYesNoEnum.tNO

            oOrder.DocDate = Today()

            oOrder.DocDueDate = Today()

            oOrder.DocCurrency = "USD"

            'Fill 2 lines in the order

            oOrder.Lines.ItemCode = "A00001"

            oOrder.Lines.ItemDescription = "IBM Inforprint 1312"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            oOrder.Lines.Add()

            oOrder.Lines.ItemCode = "A00002"

            oOrder.Lines.ItemDescription = "IBM Infoprint 1222"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            ' Now we want to delete the second line in the Order

            oOrder.Lines.Delete()

            ' The Order will be added without the second line

            lRetCode = oOrder.Add
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

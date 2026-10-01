<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# GeneralService (Object)

The GeneralService provides access to UDOs. With the service, you can add, look up and remove rows from user-defined tables. You can also invoke custom methods on the UDO's custom business implementation DLL.

## Methods (12)
- `Public Function Add(ByVal pIGeneralData As GeneralData) As GeneralDataParams` Adds a row to the database table of the current UDO. The data for the row is contained in the GeneralData object passed to the method.
  - param `pIGeneralData`: The data for the new row.
  - returns: The key of the new row.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oGeneralService As SAPbobsCOM.GeneralService

    Dim oGeneralData As SAPbobsCOM.GeneralData

    Dim oSons As SAPbobsCOM.GeneralDataCollection

    Dim oSon As SAPbobsCOM.GeneralData

    Dim sCmp As SAPbobsCOM.CompanyService

    sCmp = oCompany.GetCompanyService

    'Get a handle to the SM_MOR UDO

    oGeneralService = sCmp.GetGeneralService("SM_MOR")

    'Specify data for main UDO

    oGeneralData = oGeneralService.GetDataInterface(SAPbobsCOM.GeneralServiceDataInterfaces.gsGeneralData)

    oGeneralData.SetProperty("U_Room", "1")

    oGeneralData.SetProperty("U_Price", "20")

    oGeneralData.SetProperty("U_Name", "David")

    'Specify data for child UDO

    oSons = oGeneralData.Child("SM_MOR1")

    oSon = oSons.Add

    oSon.SetProperty("U_MainDish", "Chicken")

    oSon.SetProperty("U_SideDish", "Fries")

    oSon.SetProperty("U_Drink", "Cola")

    'Add records

    oGeneralService.Add(oGeneralData)
    ```
- `Public Sub Cancel(ByVal pIGeneralDataParams As GeneralDataParams)` Cancels a row in the database table of the current UDO.
  - param `pIGeneralDataParams`: Contains a property whose value is the key of the row to cancel. For example, for a UDO for a master data table, the object contains a property called Code whose value is the key of the row to cancel.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oGeneralService As SAPbobsCOM.GeneralService

    Dim oGeneralParams As SAPbobsCOM.GeneralDataParams

    'Get a handle to the SM_MOR UDO

    oGeneralService = sCmp.GetGeneralService("SM_MOR")

    'Cancel UDO record

    oGeneralParams = oGeneralService.GetDataInterface(SAPbobsCOM.GeneralServiceDataInterfaces.gsGeneralDataParams)

    oGeneralParams.SetProperty("DocEntry", "2")

    oGeneralService.Cancel(oGeneralParams)
    ```
- `Public Sub Close(ByVal pIGeneralDataParams As GeneralDataParams)` Closes a row in the database table of the current UDO.
  - param `pIGeneralDataParams`: Contains a property whose value is the key of the row to close. For example, for a UDO for a document table, the object contains a property called DocEntry whose value is the key of the row to close.
  - remarks: For document-type UDOs only.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oGeneralService As SAPbobsCOM.GeneralService

    Dim oGeneralParams As SAPbobsCOM.GeneralDataParams

    'Get a handle to the SM_MOR UDO

    oGeneralService = sCmp.GetGeneralService("SM_MOR")

    'Close UDO record

    oGeneralParams = oGeneralService.GetDataInterface(SAPbobsCOM.GeneralServiceDataInterfaces.gsGeneralDataParams)

    oGeneralParams.SetProperty("DocEntry", "2")

    oGeneralService.Close(oGeneralParams)
    ```
- `Public Sub Delete(ByVal pIGeneralDataParams As GeneralDataParams)` Deletes a row in the database table of the current UDO.
  - param `pIGeneralDataParams`: Contains a property whose value is the key of the row to delete. For example, for a UDO for a master data table, the object contains a property called Code whose value is the key of the row to delete.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oGeneralService As SAPbobsCOM.GeneralService

    Dim oGeneralParams As SAPbobsCOM.GeneralDataParams

    Dim sCmp As SAPbobsCOM.CompanyService

    sCmp = oCompany.GetCompanyService

    'Get a handle to the SM_MOR UDO

    oGeneralService = sCmp.GetGeneralService("SM_MOR")

    'Delete UDO record

    oGeneralParams = oGeneralService.GetDataInterface(SAPbobsCOM.GeneralServiceDataInterfaces.gsGeneralDataParams)

    oGeneralParams.SetProperty("DocEntry", "2")

    oGeneralService.Delete(oGeneralParams)
    ```
- `Public Function DoCommand(ByVal pGeneralData As GeneralData, ByVal Command_Name As String) As GeneralData` DoCommand
  - param `pGeneralData`: 
  - param `Command_Name`: 
- `Public Function GetByParams(ByVal pIGeneralDataParams As GeneralDataParams) As GeneralData` Gets a row from the database table of the current UDO. The row is specified by passing its key to the method.
  - param `pIGeneralDataParams`: Contains a property whose value is the key of the row to return. For example, for a UDO for a master data table, the object contains a property called Code whose value is the key of the row to return.
  - returns: The data for the returned row.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oGeneralService As SAPbobsCOM.GeneralService

    Dim oGeneralData As SAPbobsCOM.GeneralData

    Dim oGeneralParams As SAPbobsCOM.GeneralDataParams

    Dim sCmp As SAPbobsCOM.CompanyService

    sCmp = oCompany.GetCompanyService

    'Get a handle to the SM_MOR UDO

    oGeneralService = sCmp.GetGeneralService("SM_MOR")

    'Get UDO record

    oGeneralParams = oGeneralService.GetDataInterface(SAPbobsCOM.GeneralServiceDataInterfaces.gsGeneralDataParams)

    oGeneralParams.SetProperty("DocEntry", "2")

    oGeneralData = oGeneralService.GetByParams(oGeneralParams)
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As GeneralServiceDataInterfaces) As Object` Creates an empty data structure for use with the GeneralService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/GeneralServiceDataInterfaces.md`
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
- `Public Function GetList() As GeneralCollectionParams` Returns the keys for all the rows in the main table for a specific UDO. For example, if the UDO MealOrders was linked to the user-defined table @SM_OMOR table, and the service was instantiated for the MealOrders UDO, then this method would return the keys for all the rows in @SM_OMOR.
  - returns: A collection of GeneralDataParams objects is returned. Each object contains the key for one row in the table. For example, for a UDO for a master data table, each object contains a property called Code whose value is the key of a row in the table.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oGeneralService As SAPbobsCOM.GeneralService

    Dim oGeneralData As SAPbobsCOM.GeneralData

    Dim oGeneralParams As SAPbobsCOM.GeneralDataParams

    Dim oGeneralList As SAPbobsCOM.GeneralCollectionParams

    Dim lRet As Long

    'Create handle to "MUSIC" UDO

    oGeneralService = sCmp.GetGeneralService("MUSIC")

    'Add first record

    oGeneralData = oGeneralService.GetDataInterface(gsGeneralData)

    oGeneralData.SetProperty("Code", "First")

    oGeneralData.SetProperty("U_Data", "my data")

    oGeneralService.Add(oGeneralData)

    'Add second record

    oGeneralData = oGeneralService.GetDataInterface(gsGeneralData)

    oGeneralData.SetProperty("Code", "Second")

    oGeneralData.SetProperty("U_Data", "my data")

    oGeneralService.Add(oGeneralData)

    'Get list of all records

    oGeneralList = oGeneralService.GetList
    ```
- `Public Function InvokeMethod(ByVal pIInvokeParams As InvokeParams, ByVal pIGeneralData As GeneralData) As InvokeParams` Executes the InvokeMethod method of your UDO's custom business implementation DLL. The InvokeMethod has the following signature: TCHAR* InvokeMethod(CSboBusinessObject * refObj, const TCHAR* sInput) The CSboBusinessObject object receives data from the GeneralData parameter of this method, which represents a record of this UDO. The TCHAR object receives the string from the InvokeParams parameter of this method. You can use the InvokeMethod method as a dispatcher to other methods in your DLL, and use this string to determine how to dispatch to other functions in the DLL.
  - param `pIInvokeParams`: A string to be used by InvokeMethod method as needed and defined by the InvokeMethod method, which you create.
  - param `pIGeneralData`: A row in the database table that is linked to this GeneralService instance. You can obtain a GeneralData object for a specific row, for example, by calling the GetByParams method. Any changes to the CSboBusinessObject in the DLL's InvokeMethod does not affect the data in the GeneralData object that is passed. When control returns to your add-on from the DLL, the data in the GeneralData object is unchanged. This can cause a situation where the data in the GeneralData object is not up to date.
  - returns: A string returned from the DLL's InvokeMethod.
  - example note: You can invoke a custom method written in an implementation DLL for your UDO.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.GeneralService oGeneralService;
    SAPbobsCOM.GeneralData oGeneralData;
    SAPbobsCOM.InvokeParams oInvokeInput;
    SAPbobsCOM.InvokeParams oInvokeOutput;

    // Get GeneralService
    oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);

    // Get data interface
    oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);
    oInvokeInput = (InvokeParams)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsInvokeParams);

    oInvokeInput.Value = InvokeInputString;

    // Use invoke method
    oInvokeOutput = oGeneralService.InvokeMethod(oInvokeInput, oGeneralData);
    ```
- `Public Sub Update(ByVal pIGeneralData As GeneralData)` Updates an existing row in the database table of the current UDO. The data for the row, including the key of the row to be updated, is contained in the GeneralData passed to the method.
  - param `pIGeneralData`: The data for the row to be updated. The GeneralData object must contain the key of the object to be updated.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oGeneralService As SAPbobsCOM.GeneralService

    Dim oGeneralData As SAPbobsCOM.GeneralData

    Dim oGeneralParams As SAPbobsCOM.GeneralDataParams

    Dim sCmp As SAPbobsCOM.CompanyService

    sCmp = oCompany.GetCompanyService

    'Get a handle to the SM_MOR UDO

    oGeneralService = sCmp.GetGeneralService("SM_MOR")

    'Get UDO record

    oGeneralParams = oGeneralService.GetDataInterface(SAPbobsCOM.GeneralServiceDataInterfaces.gsGeneralDataParams)

    oGeneralParams.SetProperty("DocEntry", "2")

    oGeneralData = oGeneralService.GetByParams(oGeneralParams)

    'Update UDO record

    oGeneralData.SetProperty("U_Room", "2")

    oGeneralData.SetProperty("U_Price", "40")

    oGeneralData.SetProperty("U_Name", "Guy")

    oGeneralService.Update(oGeneralData)
    ```

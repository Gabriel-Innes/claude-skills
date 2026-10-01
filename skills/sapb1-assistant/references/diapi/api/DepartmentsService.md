<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
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
  - enum: `../enums/DepartmentsServiceDataInterfaces.md`
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

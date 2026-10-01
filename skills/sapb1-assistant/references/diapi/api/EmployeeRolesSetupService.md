<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EmployeeRolesSetupService (Object)

The EmployeeRolesSetupService service enables you to add, look up and remove roles in the employee roles master data table. To see the list of employee roles and create a new one, select Human Resources --> Employee Master Data, and select the Membership tab. Source table: OHTY

**Remarks:** This service affects the employee roles master data. The role for a specific employee can be retrieved from the EmployeeRolesInfo object of an employee's EmployeesInfo object. System roles have their Locked field set to Y. System roles cannot be updated or deleted.

## Methods (8)
- `Public Function AddEmployeeRoleSetup(ByVal pIEmployeeRoleSetup As EmployeeRoleSetup) As EmployeeRoleSetupParams` Adds an employee role.
  - param `pIEmployeeRoleSetup`: The data for the new employee role
  - returns: Contains the key (TypeID) of the new role.
  - C# example (from SAP's help):
    ```csharp
    public void AddEmployeeRole()
    {
        try
        {
            EmployeeRolesSetupService oRoleSrv;
            oRoleSrv = (SAPbobsCOM.EmployeeRolesSetupService)(MainModule.oCmpSrv.GetBusinessService(ServiceTypes.EmployeeRolesSetupService));

            EmployeeRoleSetup addLine;
            addLine = (EmployeeRoleSetup)oRoleSrv.GetDataInterface(EmployeeRolesSetupServiceDataInterfaces.erssEmployeeRoleSetup);

            addLine.Name = "Role1";
            addLine.Description = "Desc1";
            oRoleSrv.AddEmployeeRoleSetup(addLine);

        }
        catch (Exception ex)
        {
            Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
        }
    }
    ```
- `Public Sub DeleteEmployeeRoleSetup(ByVal pIEmployeeRoleSetupParams As EmployeeRoleSetupParams)` Deletes an existing employee role. The role is specified by its key (TypeID), which is contained in the EmployeeRoleSetupParams object passed to the method.
  - param `pIEmployeeRoleSetupParams`: The key of the role to be deleted
  - remarks: System roles -- those with their Locked field set to Y -- cannot be deleted. Roles that have been assigned to an employee, via the EmployeeRolesInfo object, cannot be deleted.
  - C# example (from SAP's help):
    ```csharp
    public void delete()
    {
      try
      {
          EmployeeRoleSetupParams delLine;
          delLine = (EmployeeRoleSetupParams)oRoleSrv.GetDataInterface(SAPbobsCOM.EmployeeRolesSetupServiceDataInterfaces.erssEmployeeRoleSetupParams);

          //delete a record
          //please note that the typeID should be the typeID of an existing record.
          delLine.TypeID = 19;
          //delete
          oRoleSrv.DeleteEmployeeRoleSetup(delLine);
      }
      catch (Exception ex)
      {
          Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
      }
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As EmployeeRolesSetupServiceDataInterfaces) As Object` Creates an empty data structure for use with the EmployeeRolesSetupService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/EmployeeRolesSetupServiceDataInterfaces.md`
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
- `Public Function GetEmployeeRoleSetup(ByVal pIEmployeeRoleSetupParams As EmployeeRoleSetupParams) As EmployeeRoleSetup` Retrieves a specific employee role. The role is specified by its key (TypeID), which is contained in the EmployeeRoleSetupParams object passed to the method.
  - param `pIEmployeeRoleSetupParams`: The key of the role to retrieve.
  - returns: The role with the specified key.
- `Public Function GetEmployeeRoleSetupList() As EmployeeRoleSetupParamsCollection` Retrieves the keys and names of all the employee roles.
  - C# example (from SAP's help):
    ```csharp
    public void getlist()
    {
      try
      {
          EmployeeRoleSetupParamsCollection getlistParams;
          getlistParams = oRoleSrv.GetEmployeeRoleSetupList();

          String resultSet = "";

          foreach (EmployeeRoleSetupParams record in getlistParams)
          {
              resultSet = resultSet + record.TypeID + "\t" + record.Name + "\n";
          }

          Interaction.MsgBox(resultSet, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
      }
      catch (Exception ex)
      {
          Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
      }
    }
    ```
- `Public Sub UpdateEmployeeRoleSetup(ByVal pIEmployeeRoleSetup As EmployeeRoleSetup)` Updates an existing employee role. The data for the role, including the key of the role to be updated, is contained in the EmployeeRoleSetup passed to the method. To update a role, you must first retrieve it using the GetEmployeeRoleSetup method.
  - param `pIEmployeeRoleSetup`: The data for the role to be updated. The EmployeeRoleSetup object must contain the key of the object to be updated.
  - remarks: System roles -- those with their Locked field set to Y -- cannot be updated.

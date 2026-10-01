<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BranchesService (Object)

The BranchesService service enables you to add, look up and remove branches in the branches master data table. Branches can be assigned to users and employees. To see the list of branches and create a new one, select Administration --> Setup --> General --> Users, and then select the Branch field. Source table: OUBR

## Methods (8)
- `Public Function AddBranch(ByVal pIBranch As Branch) As BranchParams` Adds a branch.
  - param `pIBranch`: The data for the new branch.
  - returns: Contains the key (Code) of the new branch.
  - C# example (from SAP's help):
    ```csharp
    public void add()
    {
        try
        {
            BranchesService oBranchSrv;
            oBranchSrv = (BranchesService)(MainModule.oCmpSrv.GetBusinessService(ServiceTypes.BranchesService));
            SAPbobsCOM.Branch addLine;
            addLine = (SAPbobsCOM.Branch)oBranchSrv.GetDataInterface(BranchesServiceDataInterfaces.bsBranch);
            //full addition
            addLine.Name = "X";
            addLine.Description = "X Branch";
            oBranchSrv.AddBranch(addLine);
        }
        catch (Exception ex)
        {
            Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
        }
    }
    ```
- `Public Sub DeleteBranch(ByVal pIBranchParams As BranchParams)` Deletes an existing branch. The branch is specified by its key (Code), which is contained in the BranchParams object passed to the method.
  - param `pIBranchParams`: The key of the branch to be deleted.
  - remarks: System branches cannot be updated. Branches that have been assigned to a user or employee cannot be deleted.
  - C# example (from SAP's help):
    ```csharp
    public void delete()
    {
        try
        {
            BranchParams delLine;
            delLine = (BranchParams)oBranchSrv.GetDataInterface(BranchesServiceDataInterfaces.bsBranchParams);

            //delete a record
            //please note that the code should be of an existing record.
            delLine.Code = 5;

            //delete
            oBranchSrv.DeleteBranch(delLine);
        }
        catch (Exception ex)
        {
            Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
        }
    }
    ```
- `Public Function GetBranch(ByVal pIBranchParams As BranchParams) As Branch` Retrieves a specific branch. The branch is specified by its key (Code), which is contained in the BranchParams object passed to the method.
  - param `pIBranchParams`: The key of the branch to retrieve.
  - returns: The branch with the specified key.
  - C# example (from SAP's help):
    ```csharp
    public void update()
    {
        try
        {
            BranchParams getLine;
            SAPbobsCOM.Branch updateLine;
            getLine = (BranchParams)oBranchSrv.GetDataInterface(BranchesServiceDataInterfaces.bsBranchParams);

            //update a record
            //please note that the code should be of an existing record.
            getLine.Code = 5;

            updateLine = oBranchSrv.GetBranch(getLine);
            updateLine.Name = "T";
            updateLine.Description = "Y branch";
            oBranchSrv.UpdateBranch(updateLine);
        }
        catch (Exception ex)
        {
            Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
        }
    }
    ```
- `Public Function GetBranchList() As BranchesParams` Retrieves the keys and names of all the branches.
  - C# example (from SAP's help):
    ```csharp
    public void getlist()
    {
        try
        {
            BranchesParams getlistParams;
            getlistParams = oBranchSrv.GetBranchList();

            String resultSet = "";

            foreach (BranchParams record in getlistParams)
            {
                resultSet = resultSet + record.Code + "\t" + record.Name + "\n";
            }

            Interaction.MsgBox(resultSet, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
        }
        catch (Exception ex)
        {
            Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
        }
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As BranchesServiceDataInterfaces) As Object` Creates an empty data structure for use with the BranchesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BranchesServiceDataInterfaces.md`
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
- `Public Sub UpdateBranch(ByVal pIBranch As Branch)` Updates an existing branch. The data for the branch, including the key of the role to be updated, is contained in the Branch passed to the method. To update a branch, you must first retrieve it using the GetBranch method.
  - param `pIBranch`: The data for the branch to be updated. The Branch object must contain the key of the object to be updated.
  - remarks: System branches cannot be updated.

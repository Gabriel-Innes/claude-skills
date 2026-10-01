<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# StatesService (Object)

The StatesService service enables you to add, look up and remove states in the states master data table. States are assigned to business partners and other objects as part of the address information. Each state is associated with a specific country. To see the list of states, select Administration --> System Initialization --> Company Details --> General tab --> Local Language tab --> State combobox --> Define new Source table: OCST

## Methods (8)
- `Public Function AddState(ByVal pIState As State) As StateParams` Adds a state.
  - param `pIState`: The data for the new state.
  - returns: Contains the key (Code, Country) of the new state.
  - C# example (from SAP's help):
    ```csharp
    // Get states service
    CompanyService oCompanyService = oCompany.GetCompanyService();
    StatesService oStatesService = (StatesService)oCompanyService.GetBusinessService(ServiceTypes.StatesService);

    // Add a State
    SAPbobsCOM.State oState = (SAPbobsCOM.State)oStatesService.GetDataInterface
        (StatesServiceDataInterfaces.ssState);

    oState.Code = "Z1";
    oState.Country = "US";
    oState.Name = "ZZ4";

    oStatesService.AddState(oState);
    ```
- `Public Sub DeleteState(ByVal pIStateParams As StateParams)` Deletes an existing state. The state is specified by its key (Code, Country), which is contained in the StateParams object passed to the method.
  - param `pIStateParams`: The key of the state to be deleted.
  - C# example (from SAP's help):
    ```csharp
    // Get states service
    CompanyService oCompanyService = oCompany.GetCompanyService();
    StatesService oStatesService = (StatesService)oCompanyService.GetBusinessService(ServiceTypes.StatesService);

    // Delete a state
    SAPbobsCOM.StateParams oStateParams = (SAPbobsCOM.StateParams)oStatesService.GetDataInterface
        (StatesServiceDataInterfaces.ssStateParams);

    oStateParams.Code = "ZZ1";
    oStateParams.Country = "US";

    oStatesService.DeleteState(oStateParams);
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As StatesServiceDataInterfaces) As Object` Creates an empty data structure for use with the StatesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/StatesServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
- `Public Function GetState(ByVal pIStateParams As StateParams) As State` Retrieves a state. The state is specified by its key (Code, Country), which is contained in the StateParams object passed to the method.
  - param `pIStateParams`: The key of the state to retrieve.
  - returns: The state with the specified key.
- `Public Function GetStateList() As StatesParams` Retrieves the keys and names of all the states.
  - C# example (from SAP's help):
    ```csharp
    // Get states service
    CompanyService oCompanyService = oCompany.GetCompanyService();
    StatesService oStatesService = (StatesService)oCompanyService.GetBusinessService(ServiceTypes.StatesService);

    // Get list of states
    SAPbobsCOM.StatesParams oStatesList = oStatesService.GetStateList();
    ```
- `Public Sub UpdateState(ByVal pIState As State)` Updates an existing state. The data for the state, including the key of the state to be updated, is contained in the State passed to the method. To update a state, you must first retrieve it using the GetState method.
  - param `pIState`: The data for the state to be updated. The State object must contain the key (Code, Country) of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    // Get states service
    CompanyService oCompanyService = oCompany.GetCompanyService();
    StatesService oStatesService = (StatesService)oCompanyService.GetBusinessService(ServiceTypes.StatesService);

    // Update a State
    SAPbobsCOM.StateParams oStateParams = (SAPbobsCOM.StateParams)oStatesService.GetDataInterface
        (StatesServiceDataInterfaces.ssStateParams);

    oStateParams.Code = "ZZ1";
    oStateParams.Country = "US";

    SAPbobsCOM.State oState = oStatesService.GetState(oStateParams);
    oState.Name = "ZZ9";

    oStatesService.UpdateState(oState);
    ```

<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ChangeLogsService (Object)

You can use the change log to gain an overview of changes in most windows of SAP Business One. Each time you update, for example, tax groups, withholding tax, house banks, freight, credit card, authorizations, sales, purchasing documents, production orders, charts of accounts, or UDOs, you can use the ChangeLogsService service to look up the change logs and show the differences between two change logs. Source table: OGCL.

**Remarks:** To access the change log in the SAP Business One application, open a window and make changes, if necessary; then (with the window still open) choose Tools --> Change Log.... To display the differences between two change log instances, select the instances and choose the Show Differences button.

**Example:**
- C# example (from SAP's help):
  ```csharp
  // This sample shows how to use the change log service
  // We will get the change log of business partner with BP Code "BPID01"
  // We will show the differences between 2 ChangeLog instances
  ChangeLogsService cl = (ChangeLogsService)vCompSvr.GetBusinessService(SAPbobsCOM.ServiceTypes.ChangeLogsService);
  GetChangeLogParams GetChLgParam = (GetChangeLogParams)cl.GetDataInterface(ChangeLogsServiceDataInterfaces.clsGetChangeLogParams);
  ChangeLogsParams ChLgParams;

  GetChLgParam.Object = BoChangeLogEnum.clCards; //BusinessPartners
  GetChLgParam.PrimaryKey = "BPID01"; // Card Code

  // Get Change Log
  ChLgParams = cl.GetChangeLog(GetChLgParam);

  // Show the first 2 changes
  // Change Instance 1
  MessageBox.Show("Instance 1: " + ChLgParams.Item(0).LogInstance +
      ", Object Code: " + ChLgParams.Item(0).ObjectCode +
      ", Update Date: " + ChLgParams.Item(0).UpdatedDate +
      ", User Name: " + ChLgParams.Item(0).UserName);

  // Change Instance 2
  MessageBox.Show("Instance 2: " + ChLgParams.Item(1).LogInstance +
      ", Object Code: " + ChLgParams.Item(1).ObjectCode +
      ", Update Date: " + ChLgParams.Item(1).UpdatedDate +
      ", User Name: " + ChLgParams.Item(1).UserName);

  // Show the differences between the instances

  ShowDifferenceParams param = (ShowDifferenceParams)cl.GetDataInterface(ChangeLogsServiceDataInterfaces.clsShowDifferenceParams);

  param.Object = BoChangeLogEnum.clCards; // BusinessPartners
  param.PrimaryKey = "BPID01"; // Card Code

  // We will get the differences of these 2 instances
  param.LogInstance = 1;
  param.LogInstance2 = 2;

  ChangeLogDifferencesParams retparams = null;
  // Get differences
  retparams = cl.GetChangeLogDifferences(param);

  // Show the differences
  for (int i = 0; i < retparams.Count; i++)
  {
      MessageBox.Show("User Name: " + retparams.Item(i).UserName +
      ", Date: " + retparams.Item(i).Date +
      ", Changed Field: " + retparams.Item(i).ChangedField +
      ", New Value: " + retparams.Item(i).NewValue +
      ", Old Value: " + retparams.Item(i).OldValue +
      ", Line Number: " + retparams.Item(i).LineNumber +
      ", Array Offset: " + retparams.Item(i).ArrayOffset);
  }
  ```

## Methods (5)
- `Public Function GetChangeLog(ByVal pIGetChangeLogParams As GetChangeLogParams) As ChangeLogsParams` Retrieves a change log. The change log is specified by its key, which is contained in the GetChangeLogParams object passed to the method.
  - param `pIGetChangeLogParams`: The key of the change log to retrieve.
- `Public Function GetChangeLogDifferences(ByVal pIShowDifferenceParams As ShowDifferenceParams) As ChangeLogDifferencesParams` Retrieves the differences between two change logs. The change log difference is specified by its key, which is contained in the ShowDifferenceParams object passed to the method.
  - param `pIShowDifferenceParams`: The key of the change log differences to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As ChangeLogsServiceDataInterfaces) As Object` Creates an empty data structure for use with the ChangeLogsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ChangeLogsServiceDataInterfaces.md`
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

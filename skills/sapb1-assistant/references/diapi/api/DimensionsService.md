<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DimensionsService (Object)

The DimensionsService service enables you to activate dimensions, as well as change a dimension's description. To see the list of dimensions, select Financials --> Cost Accounting --> Define Dimensions. Source table: ODIM

**Remarks:** You cannot add or delete dimensions. Relevant for China, Japan, Republic of Korea, Singapore, India and Brazil only.

## Methods (6)
- `Public Function GetDataInterface(ByVal enumMSDI As DimensionsServiceDataInterfaces) As Object` Creates an empty data structure for use with the DimensionsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/DimensionsServiceDataInterfaces.md`
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

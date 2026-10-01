<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CertificateSeriesService (Object)

The CertificateSeriesService service enables you to add, look up and remove certificate series. Certificate series are used for TDS (withholding tax) reports. To see the list of certificate series and create a new one, select Administration --> Setup --> Financials --> TDS --> Certificate Series. Source table: OCSN

**Remarks:** For India only.

## Methods (8)
- `Public Function AddCertificateSeries(ByVal pICertificateSeries As CertificateSeries) As CertificateSeriesParams` Adds a branch.
  - param `pICertificateSeries`: The data for the new certificate series.
  - returns: Contains the key (AbsId) of the new certificate series.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.CertificateSeries oCS = (SAPbobsCOM.CertificateSeries)oCSSrv
        .GetDataInterface(CertificateSeriesServiceDataInterfaces.cssCertificateSeries);

    oCS.Code = "EDU";
    oCS.DefaultSeries = 1;
    oCS.Location = 2;
    oCS.Section = 3;
    oCS.SeriesLines.Add();
    oCS.SeriesLines.Item(0).FirstNum = 1;
    oCS.SeriesLines.Item(0).LastNum = 99;
    oCS.SeriesLines.Item(0).Prefix = "C";

    oCS.SeriesLines.Add();
    oCS.SeriesLines.Item(1).FirstNum = 0;
    oCS.SeriesLines.Item(1).LastNum = 1000;
    oCS.SeriesLines.Item(1).Prefix = "P";

    oCSSrv.AddCertificateSeries(oCS);
    ```
- `Public Sub DeleteCertificateSeries(ByVal pICertificateSeriesParams As CertificateSeriesParams)` Deletes an existing certificate series. The certificate series is specified by its key (AbsId), which is contained in the CertificateSeriesParams object passed to the method.
  - param `pICertificateSeriesParams`: The key of the certificate series to be deleted.
  - remarks: If a certificate series is in use, it cannot be deleted.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.CertificateSeriesParams oCSParams = (SAPbobsCOM.CertificateSeriesParams)oCSSrv
        .GetDataInterface(CertificateSeriesServiceDataInterfaces.cssCertificateSeriesParams);
    oCSParams.AbsEntry = 4;
    oCSSrv.DeleteCertificateSeries(oCSParams);
    ```
- `Public Function GetCertificateSeries(ByVal pICertificateSeriesParams As CertificateSeriesParams) As CertificateSeries` Retrieves a specific certificate series. The certificate series is specified by its key (AbsId), which is contained in the CertificateSeriesParams object passed to the method.
  - param `pICertificateSeriesParams`: The key of the certificate series to retrieve.
  - returns: The certificate series with the specified key.
- `Public Function GetCertificateSeriesList() As CertificateSeriesParamsCollection` Retrieves the keys and names of all the certificate series.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.CertificateSeriesParamsCollection oCSList;
    oCSList = oCSSrv.GetCertificateSeriesList();
    String result = "";
    foreach (SAPbobsCOM.CertificateSeriesParams oItem in oCSList)
    {
        result = oItem.AbsEntry + " " + oItem.Code + " " + oItem.Section;
        Interaction.MsgBox(result, (Microsoft.VisualBasic.MsgBoxStyle)0, null);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As CertificateSeriesServiceDataInterfaces) As Object` Creates an empty data structure for use with the CertificateSeriesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/CertificateSeriesServiceDataInterfaces.md`
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
- `Public Sub UpdateCertificateSeries(ByVal pICertificateSeries As CertificateSeries)` Updates an existing certificate series. The data for the certificate series, including the key of the certificate series to be updated, is contained in the CertificateSeries passed to the method. To update a certificate series, you must first retrieve it using the GetCertificateSeries method.
  - param `pICertificateSeries`: The data for the certificate series to be updated. The CertificateSeries object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.CertificateSeriesParams oCSParams = (SAPbobsCOM.CertificateSeriesParams)oCSSrv
        .GetDataInterface(CertificateSeriesServiceDataInterfaces.cssCertificateSeriesParams);

    oCSParams.AbsEntry = 4;
    SAPbobsCOM.CertificateSeries oCS = oCSSrv.GetCertificateSeries(oCSParams);

    oCS.Location = 0;
    oCS.SeriesLines.Remove(1);

    oCSSrv.UpdateCertificateSeries(oCS);
    ```

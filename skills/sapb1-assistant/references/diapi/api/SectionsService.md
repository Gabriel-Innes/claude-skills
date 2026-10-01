<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SectionsService (Object)

The SectionsService service enables you to add, look up and remove sections in the section master data table. Sections are used to specify a type of business transaction subject to TDS (withholding tax). Source table: OSEC

**Remarks:** For India only.

## Methods (8)
- `Public Function AddSection(ByVal pISection As Section) As SectionParams` Adds a section.
  - param `pISection`: The data for the new section.
  - returns: Contains the key (AbsId) of the new section.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.Section oSec = (SAPbobsCOM.Section)oSectionSrv.GetDataInterface(SectionsServiceDataInterfaces.ssSection);

    oSec.Code = "192J";
    oSec.Description = "HUM";
    oSec.ECode = "92J";
    oSectionSrv.AddSection(oSec);
    ```
- `Public Sub DeleteSection(ByVal pISectionParams As SectionParams)` Deletes an existing section. The section is specified by its key (AbsId), which is contained in the SectionParams object passed to the method.
  - param `pISectionParams`: The key of the section to be deleted.
  - remarks: You cannot delete a section that is associated with a withholding tax code (WithholdingTaxCodes) or certificate series (CertificateSeries).
  - C# example (from SAP's help):
    ```csharp
    try
    {
         SAPbobsCOM.SectionParams oSecPara = (SAPbobsCOM.SectionParams)oSectionSrv.GetDataInterface(SectionsServiceDataInterfaces.ssSectionParams);
         oSecPara.AbsEntry = 10;
         oSectionSrv.DeleteSection(oSecPara);
    }
    catch (Exception ex)
    {
         Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As SectionsServiceDataInterfaces) As Object` Creates an empty data structure for use with the SectionsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/SectionsServiceDataInterfaces.md`
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
- `Public Function GetSection(ByVal pISectionParams As SectionParams) As Section` Retrieves a section. The section is specified by its key (AbsId), which is contained in the SectionParams object passed to the method.
  - param `pISectionParams`: The key of the section to retrieve.
  - returns: The section with the specified key.
- `Public Function GetSectionList() As SectionsParams` Retrieves the keys and codes of all the sections.
  - C# example (from SAP's help):
    ```csharp
    SectionsParams oSecList = oSectionSrv.GetSectionList();

    String result = "";
    foreach (SAPbobsCOM.SectionParams oItem in oSecList)
    {
        result += oItem.AbsEntry + " " + oItem.Code + " " + oItem.Description + "\n";
    }

    Interaction.MsgBox(result, (Microsoft.VisualBasic.MsgBoxStyle)0, null);
    ```
- `Public Sub UpdateSection(ByVal pISection As Section)` Updates an existing section. The data for the section, including the key of the section to be updated, is contained in the Section passed to the method. To update a section, you must first retrieve it using the GetSection method.
  - param `pISection`: The data for the section to be updated. The Section object must contain the key of the object to be updated.
  - remarks: If the section is associated with a withholding tax code (WithholdingTaxCodes) or certificate series (CertificateSeries), you cannot update the Code and ECode properties.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SAPbobsCOM.SectionParams oSecPara = (SAPbobsCOM.SectionParams)oSectionSrv.GetDataInterface(SectionsServiceDataInterfaces.ssSectionParams);

        oSecPara.AbsEntry = 10;
        SAPbobsCOM.Section oSec = oSectionSrv.GetSection(oSecPara);
        oSec.ECode = "09J";
        oSec.Description = "Human";
        oSectionSrv.UpdateSection(oSec);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```

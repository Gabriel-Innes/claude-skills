<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AddressService (Object)

The AddressService service enables you to retrieve Address Format and full address. Source table: OADF.

**Remarks:** From the SAP Business One Main Menu, choose Administration → Setup → Business Partners → Address Formats, create a new Address Formats.

**Example:**
- C# example (from SAP's help):
  ```csharp
              oCompany.StartTransaction();
              CompanyService cs = oCompany.GetCompanyService();

              SAPbobsCOM.AddressService addrService = (SAPbobsCOM.AddressService)cs.GetBusinessService(SAPbobsCOM.ServiceTypes.AddressService);
              SAPbobsCOM.AddressParams addrParam = (SAPbobsCOM.AddressParams)addrService.GetDataInterface(AddressServiceDataInterfaces.asAddressParams);
              SAPbobsCOM.AddressReturnParams addrRetParam = (SAPbobsCOM.AddressReturnParams)addrService.GetDataInterface(AddressServiceDataInterfaces.asAddressReturnParams);
              SAPbobsCOM.AddressFormatParams addrFormatParam = (SAPbobsCOM.AddressFormatParams)addrService.GetDataInterface(AddressServiceDataInterfaces.asAddressFormatParams);

              //GetAddressFormat
              addrFormatParam.Code = 16;
              SAPbobsCOM.AddressFormat addrFormat = addrService.GetAddressFormat(addrFormatParam);
              MessageBox.Show(addrFormat.Format);
              if (!string.IsNullOrEmpty(addrFormat.Format))
              {
                  MessageBox.Show("created!");
                  oCompany.EndTransaction(SAPbobsCOM.BoWfTransOpt.wf_Commit);
              }

              //GetFullAddress
              addrParam.Country = "CN";
              addrParam.City = "Shanghai";
              addrParam.Street = "Chenhui";
              addrParam.Block = "1001";

              addrRetParam = addrService.GetFullAddress(addrParam);

              MessageBox.Show(addrRetParam.FullAddress);
              if (!string.IsNullOrEmpty(addrRetParam.FullAddress))
              {
                  MessageBox.Show("created!");
                  oCompany.EndTransaction(SAPbobsCOM.BoWfTransOpt.wf_Commit);
              }
  ```

## Methods (5)
- `Public Function GetAddressFormat(ByVal pIAddressFormatParams As AddressFormatParams) As AddressFormat` Retrieves an address format. The address format is specified by its key, which is contained in the AddressFormatParams object passed to the method.
  - param `pIAddressFormatParams`: The key of the address format to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As AddressServiceDataInterfaces) As Object` AddressService data interfaces. Creates an empty data structure for use with the GeneralService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/AddressServiceDataInterfaces.md`
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
- `Public Function GetFullAddress(ByVal pIAddressParams As AddressParams) As AddressReturnParams` Retrieves a full address. The full address is specified by its key, which is contained in the AddressReturnParams object passed to the method.
  - param `pIAddressParams`: The key of the full address to retrieve.

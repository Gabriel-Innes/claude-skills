<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PaymentBlocksService (Object)

The PaymentBlocksService service enables you to add, look up, update, and remove payment blocks. Source table: OPYB.

**Remarks:** To see the list of payment blocks: - From the SAP Business One Main Menu, choose Business Partner --> Business Partner Master Data --> Payment System. - Select Payment Blocks. - In the field on the right, choose Define New. The Payment Blocks – Setup window appears.

## Methods (8)
- `Public Function AddPaymentBlock(ByVal pIPaymentBlock As PaymentBlock) As PaymentBlockParams` Adds a payment block.
  - param `pIPaymentBlock`: The data for the new payment block.
- `Public Sub DeletePaymentBlock(ByVal pIPaymentBlockParams As PaymentBlockParams)` Deletes an existing payment block.
  - param `pIPaymentBlockParams`: The key of the payment block to be deleted.
- `Public Function GetDataInterface(ByVal enumMSDI As PaymentBlocksServiceDataInterfaces) As Object` Creates an empty data structure for use with the PaymentBlocksService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/PaymentBlocksServiceDataInterfaces.md`
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
- `Public Function GetPaymentBlock(ByVal pIPaymentBlockParams As PaymentBlockParams) As PaymentBlock` Retrieves a payment block. The payment block is specified by its key, which is contained in the PaymentBlockParams object passed to the method.
  - param `pIPaymentBlockParams`: The key of the payment block to retrieve.
- `Public Function GetPaymentBlockList() As PaymentBlocksParams` Returns the PaymentBlocksParams data collection that identify all payment blocks.
- `Public Sub UpdatePaymentBlock(ByVal pIPaymentBlock As PaymentBlock)` Updates an existing payment block. The data for the payment block, including the key of the payment block to be updated, is contained in the PaymentBlock object passed to the method. To update a payment block, you must first retrieve it using the GetPaymentBlock method.
  - param `pIPaymentBlock`: The data for the payment block to be updated. The PaymentBlock object must contain the key of the object to be updated.

<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# MaterialRevaluationFIFOService (Object)

The MaterialRevaluationFIFOService service enables you to retrieve the FIFO layers for a specific item and location. You can then use information about the FIFO layers to specify specific layers to revalue (FIFOLayers) and provide these to the MaterialRevaluation object. To perform material revaluation, select Inventory --> Inventory Transactions --> Inventory Revaluation.

**Example:**
- C# example (from SAP's help):
  ```csharp
  SAPbobsCOM.MaterialRevaluation m_MaterialRev;
  SAPbobsCOM.MaterialRevaluation_lines m_MaterialRevLines;
  SAPbobsCOM.FIFOLayers m_FIFOLayers;

  SAPbobsCOM.MaterialRevaluationFIFOService m_MRVFIFOService;
  SAPbobsCOM.MaterialRevaluationFIFO m_MRVFIFO;
  SAPbobsCOM.MaterialRevaluationFIFOParams m_MRVFIFOParam;

  SAPbobsCOM.Items m_FIFOItems;
  SAPbobsCOM.Documents m_APInvoice;
  SAPbobsCOM.Document_Lines m_APInvoice_Line;

  SAPbobsCOM.BusinessPartners m_Vendor;

  m_MaterialRev = (MaterialRevaluation)m_Company.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oMaterialRevaluation);
  m_MaterialRev.DocDate = DateTime.Now;
  m_MaterialRev.RevalType = "P";

  // Line sub object:
  m_MaterialRevLines = m_MaterialRev.Lines;
  m_MaterialRevLines.SetCurrentLine(0);
  m_MaterialRevLines.ItemCode = m_FIFOItems.ItemCode;

  // Layer sub object
  m_FIFOLayers = m_MaterialRevLines.FIFOLayers;

  // Get Company Service
  m_companyService = (CompanyService)m_Company.GetCompanyService();

  // Get Material Revaluation FIFO Service
  m_MRVFIFOService = (MaterialRevaluationFIFOService)m_companyService.GetBusinessService(SAPbobsCOM.ServiceTypes.MaterialRevaluationFIFOService);

  // Create Material Revaluation FIFO Service parameters
  m_MRVFIFOParam = (MaterialRevaluationFIFOParams)m_MRVFIFOService.GetDataInterface(SAPbobsCOM.MaterialRevaluationFIFOServiceDataInterfaces.mrfifosMaterialRevaluationFIFOParams);
  m_MRVFIFOParam.ItemCode = m_FIFOItems.ItemCode;
  m_MRVFIFOParam.LocationCode = "01";
  m_MRVFIFOParam.LocationType = "64";
  m_MRVFIFOParam.ShowIssuedLayers = BoYesNoEnum.tNO;

  // Process FIFO layers
  m_MRVFIFO = m_MRVFIFOService.GetMaterialRevaluationFIFO(m_MRVFIFOParam);
  // Process first layer
  m_FIFOLayers.LayerID = m_MRVFIFO.Layers.Item(0).LayerID;
  m_FIFOLayers.TransactionSequenceNum = m_MRVFIFO.Layers.Item(0).TransactionSequenceNum;
  String strNewPrice = NewPriceTxt.Text;
  m_FIFOLayers.Price = 500;
  // Process other layers
  int LayerNum = m_MRVFIFO.Layers.Count;
  for (int i = 1; i < LayerNum ; ++i)
  {
       m_FIFOLayers.Add();
       m_FIFOLayers.SetCurrentLine(i);
       m_FIFOLayers.LayerID = m_MRVFIFO.Layers.Item(i).LayerID;
       m_FIFOLayers.TransactionSequenceNum = m_MRVFIFO.Layers.Item(i).TransactionSequenceNum;
       m_FIFOLayers.Price = 500;
  }
  m_MaterialRev.Add();
  ```

## Methods (4)
- `Public Function GetDataInterface(ByVal enumMSDI As MaterialRevaluationFIFOServiceDataInterfaces) As Object` Creates an empty data structure for use with the MaterialRevaluationFIFOService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/MaterialRevaluationFIFOServiceDataInterfaces.md`
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
- `Public Function GetMaterialRevaluationFIFO(ByVal pIMaterialRevaluationFIFOParams As MaterialRevaluationFIFOParams) As MaterialRevaluationFIFO` Retrieves the FIFO layers for a specific item and location.
  - param `pIMaterialRevaluationFIFOParams`: The parameters for specifying the FIFO layers to retrieve
  - returns: The retrieved FIFO layers
  - remarks: If you specify a non-FIFO item, an exception is thrown.

<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PredefinedTextsService (Object)

The PredefinedTextsService service enables you to add, look up and remove predefined texts in the predefined texts master data table. Predefined texts are stored text strings that can be added as remarks in marketing documents. To see the list of predefined texts, select Administration --> Setup --> General --> Predefined Text. You can also view a table of all predefined texts by opening a marketing document, selecting Goto --> Opening and Closing Remarks, and clicking Insert Predefined Texts. Source table: OPDT

## Methods (8)
- `Public Function AddPredefinedText(ByVal pIPredefinedText As PredefinedText) As PredefinedTextParams` Adds a predefined text.
  - param `pIPredefinedText`: The data for the new predefined text.
  - returns: The key (AbsEntry) of the new predefined text.
  - C# example (from SAP's help):
    ```csharp
    // Get predefined text service
    PredefinedTextsService textService;
    companyService = company.GetCompanyService();
    textService = (PredefinedTextsService)companyService.GetBusinessService(ServiceTypes.PredefinedTextsService);

    // Add predefined text
    PredefinedText text = textService.GetDataInterface(PredefinedTextsServiceDataInterfaces.ptsPredefinedText) As PredefinedText;
    text.TextCode = "Thank you";
    text.Text = "Thank you for using our products.";
    textService.AddPredefinedText(text);
    ```
- `Public Sub DeletePredefinedText(ByVal pIPredefinedTextParams As PredefinedTextParams)` Deletes an existing predefined text. The predefined text is specified by its key (AbsEntry), which is contained in the PredefinedTextParams object passed to the method.
  - param `pIPredefinedTextParams`: The key of the predefined text to be deleted.
  - C# example (from SAP's help):
    ```csharp
    // Get predefined text service
    PredefinedTextsService textService;
    companyService = company.GetCompanyService();
    textService = (PredefinedTextsService)companyService.GetBusinessService(ServiceTypes.PredefinedTextsService);

    PredefinedText text = textService.GetDataInterface(PredefinedTextsServiceDataInterfaces.ptsPredefinedText) as PredefinedText;
    PredefinedTextParams textParams = textService.GetDataInterface(PredefinedTextsServiceDataInterfaces.ptsPredefinedTextParams) as PredefinedTextParams;

    // Specify the key of the predefined text to delete
    textParams.Numerator = 2;

    // Delete text
    textService.DeletePredefinedText(textParams);
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As PredefinedTextsServiceDataInterfaces) As Object` Creates an empty data structure for use with the PredefinedTextsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/PredefinedTextsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
- `Public Function GetPredefinedText(ByVal pIPredefinedTextParams As PredefinedTextParams) As PredefinedText` Retrieves a predefined text. The predefined text is specified by its key (AbsEntry), which is contained in the PredefinedTextParams object passed to the method.
  - param `pIPredefinedTextParams`: The key of the predefined text to retrieve.
  - returns: The predefined text with the specified key.
- `Public Function GetPredefinedTextList() As PredefinedTextsParams` Retrieves the keys and names of all the predefined texts.
  - C# example (from SAP's help):
    ```csharp
    // Get list of predefined text
    PredefinedTextsParams textsParams = textService.GetPredefinedTextList();

    int i = 1;

    // Print the list
    foreach (PredefinedTextParams textParams In textsParams)
    {
        Console.WriteLine("item {0}: Numerator:{1}, TextCode:{2}", i++, textParams.Numerator, textParams.TextCode);
    }
    ```
- `Public Sub UpdatePredefinedText(ByVal pIPredefinedText As PredefinedText)` Updates an existing predefined text. The data for the predefined text, including the key of the predefined text to be updated, is contained in the PredefinedText passed to the method. To update a predefined text, you must first retrieve it using the GetPredefinedText method.
  - param `pIPredefinedText`: The data for the predefined text to be updated. The PredefinedText object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    // Get predefined text service
    PredefinedTextsService textService;
    companyService = company.GetCompanyService();
    textService = (PredefinedTextsService)companyService.GetBusinessService(ServiceTypes.PredefinedTextsService);

    PredefinedText text = textService.GetDataInterface(PredefinedTextsServiceDataInterfaces.ptsPredefinedText) as PredefinedText;
    PredefinedTextParams textParams = textService.GetDataInterface(PredefinedTextsServiceDataInterfaces.ptsPredefinedTextParams) as PredefinedTextParams;

    // Get the predefined text to update
    textParams.Numerator = 2;
    PredefinedText text = textService.GetPredefinedText(textParams);

    // Update text
    text.Text = "new Text";
    textService.UpdatePredefinedText(text);
    ```

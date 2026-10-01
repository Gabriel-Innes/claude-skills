<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CashDiscountsService (Object)

The CashDiscountsService service enables you to add, look up and remove cash discount policies. Each policy specifies a set of discounts and the conditions for applying the discount. To view the current cash discounts, select Administration --> Setup --> Business Partners --> Payment Terms, and select Define New in the Cash Discount Name field. Source table: OCDC

## Methods (8)
- `Public Function AddCashDiscount(ByVal pICashDiscount As CashDiscount) As CashDiscountParams` Adds a cash discount.
  - param `pICashDiscount`: The data for the new cash discount.
  - returns: Contains the key (Code) of the new cash discount.
  - C# example (from SAP's help):
    ```csharp
    CashDiscountsService oCDCSrv;
    oCDCSrv = (CashDiscountsService)(MainModule.oCmpSrv.GetBusinessService(ServiceTypes.CashDiscountsService));

    SAPbobsCOM.CashDiscount addLine;
    addLine = (SAPbobsCOM.CashDiscount)oCDCSrv.GetDataInterface(CashDiscountsServiceDataInterfaces.cdsCashDiscount);

    addLine.Code = "Code";
    addLine.Name = "Name";
    addLine.ByDate = BoYesNoEnum.tNO;
    addLine.DiscountLines.Add();
    addLine.DiscountLines.Item(0).NumOfDays = 4;
    addLine.DiscountLines.Item(0).Discount = 4;

    addLine.DiscountLines.Add();
    addLine.DiscountLines.Item(1).NumOfDays = 5;

    oCDCSrv.AddCashDiscount(addLine);
    ```
- `Public Sub DeleteCashDiscount(ByVal pICashDiscountParams As CashDiscountParams)` Deletes an existing cash discount. The cash discount is specified by its key (Code), which is contained in the CashDiscountParams object passed to the method.
  - param `pICashDiscountParams`: The key of the cash discount to be deleted.
  - remarks: Cash discounts that have been assigned to a payment term, via the PaymentTermsTypes object, cannot be deleted.
  - C# example (from SAP's help):
    ```csharp
    CashDiscountParams delLine;
    delLine = (CashDiscountParams)oCDCSrv.GetDataInterface(SAPbobsCOM.CashDiscountsServiceDataInterfaces.cdsCashDiscountParams);

    delLine.Code = "Code";
    oCDCSrv.DeleteCashDiscount(delLine);
    ```
- `Public Function GetCashDiscount(ByVal pICashDiscountParams As CashDiscountParams) As CashDiscount` Retrieves a specific cash discount. The cash discount is specified by its key (Code), which is contained in the CashDiscountParams object passed to the method.
  - param `pICashDiscountParams`: The key of the cash discount to retrieve.
  - returns: The cash discount with the specified key.
- `Public Function GetCashDiscountList() As CashDiscountsParams` Retrieves the keys and names of all the cash discounts.
  - C# example (from SAP's help):
    ```csharp
    CashDiscountsParams getParams;
    getParams = oCDCSrv.GetCashDiscountList();

    String resultSet = "";

    foreach (CashDiscountParams record in getParams)
    {
        resultSet = resultSet + record.Code + "\t" + record.Name + "\n";
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As CashDiscountsServiceDataInterfaces) As Object` Creates an empty data structure for use with the CashDiscountsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/CashDiscountsServiceDataInterfaces.md`
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
- `Public Sub UpdateCashDiscount(ByVal pICashDiscount As CashDiscount)` Updates an existing cash discount. The data for the cash discount, including the key of the cash discount to be updated, is contained in the CashDiscount passed to the method. To update a cash discount, you must first retrieve it using the GetCashDiscount method.
  - param `pICashDiscount`: The data for the cash discount to be updated. The CashDiscount object must contain the key of the object to be updated.
  - remarks: If the ByDate property is changed, all old lines in DiscountLines must first be deleted.
  - C# example (from SAP's help):
    ```csharp
    CashDiscountParams getLine;
    SAPbobsCOM.CashDiscount updateLine;
    getLine = (CashDiscountParams)oCDCSrv.GetDataInterface(SAPbobsCOM.CashDiscountsServiceDataInterfaces.cdsCashDiscountParams);

    getLine.Code = "Code";
    updateLine = oCDCSrv.GetCashDiscount(getLine);
    updateLine.Name = "NewName";

    oCDCSrv.UpdateCashDiscount(updateLine);
    ```

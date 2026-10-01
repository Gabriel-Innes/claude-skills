<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# GLAccountAdvancedRulesService (Object)

The GLAccountAdvancedRulesService service enables you to add, look up, update, and remove advanced G/L account determination rules. Source table: OGAR.

**Remarks:** To open the Advanced G/L Account Determination Rules window, from the SAP Business One Main Menu, choose Administration -> Setup -> Financials -> G/L Account Determination; in the G/L Account Determination window, choose the Advanced button.

**Example:**
- VB example (SAP's help labels this C#, but it is Visual Basic - translate before use):
  ```vb
  Dim oGLAccountAdvancedRulesService As GLAccountAdvancedRulesService =
  oCompany.GetCompanyService().GetBusinessService(ServiceTypes.glaarGLAccountAdvancedRulesService)

  Dim oGLAccountAdvancedRule As SAPbobsCOM.GLAccountAdvancedRule=
      oGLAccountAdvancedRulesService.GetDataInterface
  (oGLAccountAdvancedRulesServiceDataInterfaces.glaarGLAccountAdvancedRule)

      oGLAccountAdvancedRule.Period = "2012"
      oGLAccountAdvancedRule.Itemcode = "i001"
      oGLAccountAdvancedRule.ExpenseAccount = "1000"
      oGLAccountAdvancedRule.Code = "100"
      oGLAccountAdvancedRulesService.Add(oGLAccountAdvancedRule)

  Dim param As SAPbobsCOM. GLAccountAdvancedRuleParams =
         oGLAccountAdvancedRulesService.GetDataInterface
  (oGLAccountAdvancedRulesServiceDataInterfaces. glaarGLAccountAdvancedRuleParams)
         param. AbsoluteEntry = 1
         oGLAccountAdvancedRule = oGLAccountAdvancedRulesService.Get(param)
         oGLAccountAdvancedRule. ExpenseAccount = "2000"
         oGLAccountAdvancedRulesService.Update(oGLAccountAdvancedRule)

         param. AbsoluteEntry = 1
         oGLAccountAdvancedRulesService.Delete(param)
  ```

## Methods (8)
- `Public Function Add(ByVal pIGLAccountAdvancedRule As GLAccountAdvancedRule) As GLAccountAdvancedRuleParams` Adds an advanced G/L account determination rule.
  - param `pIGLAccountAdvancedRule`: The data for the new advanced G/L account determination rule.
- `Public Sub Delete(ByVal pIGLAccountAdvancedRuleParams As GLAccountAdvancedRuleParams)` Deletes an existing advanced G/L account determination rule.
  - param `pIGLAccountAdvancedRuleParams`: The key of the advanced G/L account determination rule to be deleted.
- `Public Function Get(ByVal pIGLAccountAdvancedRuleParams As GLAccountAdvancedRuleParams) As GLAccountAdvancedRule` Retrieves an advanced G/L account determination rule. The advanced G/L account determination rule is specified by its key, which is contained in the GLAccountAdvancedRuleParams object passed to the method.
  - param `pIGLAccountAdvancedRuleParams`: The key of the advanced G/L account determination rule to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As GLAccountAdvancedRulesServiceDataInterfaces) As Object` Creates an empty data structure for use with the GLAccountAdvancedRulesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/GLAccountAdvancedRulesServiceDataInterfaces.md`
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
- `Public Function GetList() As GLAccountAdvancedRuleParamsCollection` Returns the GLAccountAdvancedRuleParamsCollection data collection that identifies all advanced G/L account determination rules.
- `Public Sub Update(ByVal pIGLAccountAdvancedRule As GLAccountAdvancedRule)` Updates an existing advanced G/L account determination rule.
  - param `pIGLAccountAdvancedRule`: The data for the advanced G/L account determination rule to be updated. The GLAccountAdvancedRule object must contain the key of the object to be updated.

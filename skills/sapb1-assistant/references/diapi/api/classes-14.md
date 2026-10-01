<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# GLAccountAdvancedRule (Object)

The set of rules according to which the G/L account determination takes place. The advanced G/L account determination rules are defined per posting period. Source table: OGAR.

**Remarks:** For detailed information about the structure of this window and the different settings, see the How To Setup and Work with Advanced G/L Account Determination guide in the documentation resource center.

## Properties (81)
- `Public Property AbsoluteEntry() As Long` [R] The key of the advanced G/L account determination rule. Field name: AbsEntry.
- `Public Property BeginningofFinancialYear() As Date` [R/W] The beginning date of the financial year. Field name: FinancYear.
- `Public Property BPCode() As String` [R/W] property BPCode
- `Public Property BPGroup() As Long` [R/W] The code of the business partner group. Field name: BPGrpCod. Length: 6 characters.
- `Public Property BusinessPartnerType() As BoBusinessPartnerTypes` [R/W] property BusinessPartnerType
- `Public Property Code() As String` [R/W] The code of the advanced G/L account determination rule. Field name: RuleCode. Length: 20 characters.
- `Public Property CostAccount() As String` [R/W] Cost of Goods Sold Account Field name: COGM_Act.
- `Public Property CostInflationAccount() As String` [R/W] Cost Inflation Account Field name: CostRevAct.
- `Public Property CostInflationOffsetAccount() As String` [R/W] Cost Inflation Offset Account Field name: CostOffAct.
- `Public Property DecreasingAccount() As String` [R/W] property DecreasingAccount
- `Public Property Description() As String` [R/W] The description. Field name: Comments. Length: 254 characters.
- `Public Property EUExpensesAccount() As String` [R/W] EU Expenses Account Field name: ECExepnses.
- `Public Property EUPurchaseCreditAcc() As String` [R/W] property EUPurchaseCreditAcc
- `Public Property EURevenuesAccount() As String` [R/W] EU Revenues Account Field name: ECIncome.
- `Public Property ExchangeRateDifferencesAcct() As String` [R/W] Exchange Rate Differences Account Field name: ExDiffAct.
- `Public Property ExemptedCredits() As String` [R/W] Tax Exempt Credit Account Field name: ARCMExpAct.
- `Public Property ExemptIncomeAcc() As String` [R/W] Tax Exempt Revenue Account Field name: ExmptIncom.
- `Public Property ExpenseClearingAct() As String` [R/W] Expense Clearing Account Field name: ExpClrAct.
- `Public Property ExpenseOffsettingAccount() As String` [R/W] Expense Offset Account Field name: ExpOfstAct.
- `Public Property ExpensesAccount() As String` [R/W] Expenses Account Field name: DfltExpn.
- `Public Property FederalTaxID() As String` [R/W] The federal tax ID. Field name: LicTradNum. Length: 32 characters.
- `Public Property FinancialYear() As Long` [R/W] The financial year. Field name: Year.
- `Public Property ForeignExpensAcc() As String` [R/W] Foreign Expenses Account Field name: ForgnExpn.
- `Public Property ForeignPurchaseCreditAcc() As String` [R/W] Purchase Credit Account - Foreign Field name: APCMFrnAct.
- `Public Property ForeignRevenueAcc() As String` [R/W] Foreign Revenues Account Field name: ForgnIncm.
- `Public Property FromDate() As Date` [R/W] Field name: FromDate.
- `Public Property FromDocumentDate() As Date` [R/W] Field name: F_TaxDate.
- `Public Property FromDueDate() As Date` [R/W] Field name: F_DueDate.
- `Public Property FromPostingDate() As Date` [R/W] Field name: F_RefDate.
- `Public Property GetGLAccountBy() As GetGLAccountByEnum` [R/W] The methods to get the G/L account. Field name: GLMethod.
- `Public Property GLDecreaseAcct() As String` [R/W] G/L Decrease Account Field name: DecresGlAc.
- `Public Property GLIncreaseAcct() As String` [R/W] G/L Increase Account Field name: IncresGlAc.
- `Public Property GoodsClearingAcct() As String` [R/W] Goods Clearing Account Field name: BalanceAct.
- `Public Property IncreasingAccount() As String` [R/W] property IncreasingAccount
- `Public Property InventoryAccount() As String` [R/W] Inventory Account Field name: StockAct.
- `Public Property InventoryOffsetProfitAndLossAccount() As String` [R/W] Inventory Offset Profit and Loss Account Field name: StockOffst.
- `Public Property IsActive() As BoYesNoEnum` [R/W] The active status of the advanced G/L account determination rule. Field name: Active.
- `Public Property ItemCode() As String` [R/W] The code of the item. Field name: ItemCode. Length: 20 characters.
- `Public Property ItemGroup() As Long` [R/W] The code of the item group. Field name: ItmsGrpCod. Length: 6 characters.
- `Public Property NegativeInventoryAdjustmentAccount() As String` [R/W] Negative Inventory Adjustment Account Field name: NegStckAct.
- `Public Property NumberOfPeriods() As Long` [R/W] Number of periods. Field name: PeriodNum.
- `Public Property PAReturnAcct() As String` [R/W] Purchase Return Account Field name: PaReturnAc.
- `Public Property Period() As String` [R/W] The period category. Field name: PeriodCat. Length: 10 characters.
- `Public Property PeriodName() As String` [R/W] The name of the period. Field name: PeriodName. Length: 20 characters.
- `Public Property PriceDifferenceAcc() As String` [R/W] Price Difference Account Field name: PricDifAct.
- `Public Property PurchaseAcct() As String` [R/W] Purchase Account Field name: PurchseAct.
- `Public Property PurchaseBalanceAccount() As String` [R/W] Purchase Balance Account Field name: PurBalAct.
- `Public Property PurchaseCreditAcc() As String` [R/W] Purchase Credit Account Field name: APCMAct.
- `Public Property PurchaseOffsetAcct() As String` [R/W] Purchase Offset Account Field name: PaOffsetAc.
- `Public Property ReturningAccount() As String` [R/W] Sales Returns Account Field name: RturnngAct.
- `Public Property RevenuesAccount() As String` [R/W] Revenues Account Field name: DfltIncom.
- `Public Property SalesCreditAcc() As String` [R/W] Sales Credit Account Field name: ARCMAct.
- `Public Property SalesCreditEUAcc() As String` [R/W] Sales Credit Account - EU Field name: ARCMEUAct.
- `Public Property SalesCreditForeignAcc() As String` [R/W] Sales Credit Account - Foreign Field name: ARCMFrnAct.
- `Public Property ShippedGoodsAccount() As String` [R/W] Shipped Goods Account Field name: ShpdGdsAct.
- `Public Property ShipToCountry() As String` [R/W] The ship-to country. Field name: ShipCountr. Length: 3 characters.
- `Public Property ShipToState() As String` [R/W] The ship-to state. Field name: ShipState. Length: 3 characters.
- `Public Property StockInflationAdjustAccount() As String` [R/W] Inventory Inflation Adjustment Account Field name: StockRvAct.
- `Public Property StockInflationOffsetAccount() As String` [R/W] Inventory Inflation Offset Account Field name: StkRvOfAct.
- `Public Property StockInTransitAccount() As String` [R/W] Stock In Transit Account Field name: StkInTnAct.
- `Public Property SubPeriodType() As BoSubPeriodTypeEnum` [R/W] The type of the sub period. Field name: SubType.
- `Public Property ToDate() As Date` [R/W] Field name: ToDate.
- `Public Property ToDocumentDate() As Date` [R/W] Field name: T_TaxDate.
- `Public Property ToDueDate() As Date` [R/W] Field name: T_DueDate.
- `Public Property ToPostingDate() As Date` [R/W] Field name: T_RefDate.
- `Public Property TransferAccount() As String` [R/W] property TransferAccount
- `Public Property UDF1() As String` [R/W] property UDF1
- `Public Property UDF2() As String` [R/W] property UDF2
- `Public Property UDF3() As String` [R/W] property UDF3
- `Public Property UDF4() As String` [R/W] property UDF4
- `Public Property UDF5() As String` [R/W] property UDF5
- `Public Property Usage() As Long` [R/W] property Usage
- `Public Property VarienceAccount() As String` [R/W] Variance Account Field name: VariancAct.
- `Public Property VatGroup() As String` [R/W] property VATGroup
- `Public Property VATInRevenueAccount() As String` [R/W] VAT in Revenue Account Field name: VatRevAct.
- `Public Property Warehouse() As String` [R/W] The code of the warehouse. Field name: WhsCode. Length: 8 characters.
- `Public Property WHIncomingCenvatAccount() As String` [R/W] Incoming CENVAT Account (Warehouse) Field name: WhICenAct.
- `Public Property WHOutgoingCenvatAccount() As String` [R/W] Outgoing CENVAT Account (Warehouse) Field name: WhOCenAct.
- `Public Property WipAccount() As String` [R/W] WIP Inventory Account Field name: WipAcct.
- `Public Property WipOffsetProfitAndLossAccount() As String` [R/W] WIP Offset Profit and Loss Account Field name: WipOffset.
- `Public Property WipVarianceAccount() As String` [R/W] WIP Inventory Variance Account Field name: WipVarAcct.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# GLAccountAdvancedRuleParams (Object)

Holds the key to an existing advanced G/L account determination rule. This object is used to pass keys to and retrieve keys from GLAccountAdvancedRulesService methods.

## Properties (10)
- `Public Property AbsoluteEntry() As Long` [R/W] The key of the advanced G/L account determination rule. Field name: AbsEntry.
- `Public Property BPGroup() As Long` [R/W] The code of the business partner group. Field name: BPGrpCod. Length: 6 characters.
- `Public Property Code() As String` [R/W] The code of the advanced G/L account determination rule. Field name: RuleCode. Length: 20 characters.
- `Public Property FederalTaxID() As String` [R/W] The federal tax ID. Field name: LicTradNum. Length: 32 characters.
- `Public Property ItemCode() As String` [R/W] The code of the item. Field name: ItemCode. Length: 20 characters.
- `Public Property ItemGroup() As Long` [R/W] The code of the item group. Field name: ItmsGrpCod. Length: 6 characters.
- `Public Property Period() As String` [R/W] The period category. Field name: PeriodCat. Length: 10 characters.
- `Public Property ShipToCountry() As String` [R/W] The ship-to country. Field name: ShipCountr. Length: 3 characters.
- `Public Property ShipToState() As String` [R/W] The ship-to state. Field name: ShipState. Length: 3 characters.
- `Public Property Warehouse() As String` [R/W] The code of the warehouse. Field name: WhsCode. Length: 8 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# GLAccountAdvancedRuleParamsCollection (Collection)

A collection of GLAccountAdvancedRuleParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As GLAccountAdvancedRuleParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As GLAccountAdvancedRuleParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

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
  - enum: `GLAccountAdvancedRulesServiceDataInterfaces` in `../enums/enums-02.md`
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

# GLAccounts (Collection)

GLAccounts is a collection of GLAccount data structures.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of GLAccount data structures in the collection.

## Methods (5)
- `Public Function Add() As GLAccount` Adds a data structure (Item in the collection) and returns a reference to it (Index starting from 0).
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As GLAccount` Returns a reference to an existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the new item, which was added to the collection.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` method ToXMLString

# GovPayCode (Object)

GovPayCode Class

## Properties (6)
- `Public Property AbsId() As Long` [R] property AbsId
- `Public Property Authorities() As GovPayCodeAuthorities` [R] property Authorities
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R/W] property Description
- `Public Property Periodicity() As GovPayCodePeriodicityEnum` [R/W] property Periodicity
- `Public Property StateTax() As BoYesNoEnum` [R/W] property StateTax

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# GovPayCodeAuthorities (Collection)

GovPayCodeAuthorities Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As GovPayCodeAuthority` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As GovPayCodeAuthority` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` method Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# GovPayCodeAuthority (Object)

GovPayCodeAuthority Class

## Properties (4)
- `Public Property AbsId() As Long` [R] property AbsId
- `Public Property BPLID() As Long` [R/W] property BPLId
- `Public Property CardCode() As String` [R/W] property CardCode
- `Public Property State() As String` [R/W] property State

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# GovPayCodeParams (Object)

GovPayCodeParams Class

## Properties (2)
- `Public Property AbsId() As Long` [R/W] property AbsId
- `Public Property Code() As String` [R/W] property Code

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# GovPayCodeParamsCollection (Collection)

GovPayCodeParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As GovPayCodeParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As GovPayCodeParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# GovPayCodesService (Object)

GovPayCodesService Class

## Methods (8)
- `Public Function Add(ByVal pIGovPayCode As GovPayCode) As GovPayCodeParams` Add
  - param `pIGovPayCode`: 
- `Public Sub Delete(ByVal pIGovPayCodeParams As GovPayCodeParams)` Delete
  - param `pIGovPayCodeParams`: 
- `Public Function Get(ByVal pIGovPayCodeParams As GovPayCodeParams) As GovPayCode` Get
  - param `pIGovPayCodeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As GovPayCodesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `GovPayCodesServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As GovPayCodeParamsCollection` GetList
- `Public Sub Update(ByVal pIGovPayCode As GovPayCode)` Update
  - param `pIGovPayCode`: 

# GTIParams (Object)

GTIParams Class

## Properties (2)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property InboundFile() As String` [R/W] property InboundFile

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# GTIParamsCollection (Collection)

GTIParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As GTIParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As GTIParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# GTIsService (Object)

GTIsService Class

## Methods (4)
- `Public Function GetDataInterface(ByVal enumMSDI As GTIsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `GTIsServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function Import(ByVal pIGTIParams As GTIParams) As GTIParamsCollection` Import
  - param `pIGTIParams`: 

# Holiday (Object)

Specify a set of company holidays. Source table: OHLD.

## Properties (7)
- `Public Property HolidayCode() As String` [R/W] The code of the holiday. You can enter holidays for each country you work with. Field name: HldCode. Length: 20 characters.
- `Public Property HolidayDates() As HolidayDates` [R] Holiday dates.
- `Public Property SetWeekendsAsWorkDays() As String` [R/W] Considers weekend days as business days while calculating due dates for payments. Field name: ignrWnd.
  - remarks: The calculation of a purchase invoice's due date takes the company's own holiday into consideration. The calculation of a sales invoice's due date takes the customer's holiday into consideration.
- `Public Property ValidForOneYearOnly() As BoYesNoEnum` [R/W] Applies the holiday table only to the year specified in the holiday dates. Deselect to define the holiday table as year independent. Field name: isCurYear.
- `Public Property WeekendFrom() As BoWeekEnum` [R/W] Select days for the weekend. Field name: WndFrm.
- `Public Property WeekendTO() As BoWeekEnum` [R/W] Select days for the weekend. Field name: WndTo.
- `Public Property WeekNoRule() As BoWeekNoRuleEnum` [R/W] The rule of calculating week numbers. Field name: WeekNoRule.
  - remarks: The definition impacts the week numbers and the first day of the week in forecasts and MRP recommendations based on weeks.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# HolidayDate (Object)

Specify a set of company holiday dates as defined in the Holiday Dates window. Source table: HLD1.

## Properties (4)
- `Public Property EndDate() As Date` [R/W] The end date of the holiday period. Field name: EndDate.
- `Public Property HolidayCode() As String` [R/W] The name of the holidays group. Field name: HldCode. Length: 20 characters.
- `Public Property Remarks() As String` [R/W] The remarks regarding the holidays or weekends. Field name: Rmrks. Length: 50 characters.
- `Public Property StartDate() As Date` [R/W] The start date of the holiday period. Field name: StrDate.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# HolidayDates (Collection)

A collection of HolidayDate objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As HolidayDate` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As HolidayDate` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# HolidayParams (Object)

Holds the key of a holiday. This object is used to pass keys to and retrieve keys from HolidayService methods.

## Properties (1)
- `Public Property HolidayCode() As String` [R/W] The code of the holiday.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# HolidayService (Object)

The HolidayService service enables you to add, look up, remove, and update holidays. Source table: OHLD.

## Methods (8)
- `Public Function AddHoliday(ByVal pIHoliday As Holiday) As HolidayParams` Adds a new holiday.
  - param `pIHoliday`: The data for the new holiday.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.Holiday hd1 = holidayService.GetDataInterface(SAPbobsCOM.HolidayServiceDataInterfaces.hsHoliday);
    hd1.HolidayCode = "holiday1";
    hd1.WeekendFrom = SAPbobsCOM.BoWeekEnum.Sunday;
    hd1.WeekendTO = SAPbobsCOM.BoWeekEnum.Monday;
    hd1.ValidForOneYearOnly = SAPbobsCOM.BoYesNoEnum.tNO;
    hd1.SetWeekendsAsWorkDays = "Y";
    hd1.WeekNoRule = SAPbobsCOM.BoWeekNoRuleEnum.fromFirstFourDayWeek;

    SAPbobsCOM.HolidayDate hdDate = hd1.HolidayDates.Add();
    hdDate.StartDate = new DateTime(2020, 10, 1);
    hdDate.EndDate = new DateTime(2020, 10, 6);
    hdDate.Remarks = "holiday1";
    try
    {
        SAPbobsCOM.HolidayParams hdParams1 = holidayService.AddHoliday(hd1);
    }
    catch (Exception ex)
    {
        Console.WriteLine(ex.Message);
    }
    ```
- `Public Sub DeleteHoliday(ByVal pIHolidayParams As HolidayParams)` Deletes an existing holiday.
  - param `pIHolidayParams`: The key of the holiday to be deleted.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.HolidayParams hdParams2 = holidayService.GetDataInterface(HolidayServiceDataInterfaces.hsHolidayParams);
    hdParams2.HolidayCode = "holiday1";

    try
    {
        holidayService.DeleteHoliday(hdParams2);
    }
    catch (Exception ex)
    {
        Console.WriteLine(ex.Message);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As HolidayServiceDataInterfaces) As Object` Creates an empty data structure for use with the HolidayService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `HolidayServiceDataInterfaces` in `../enums/enums-02.md`
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
- `Public Function GetHoliday(ByVal pIHolidayParams As HolidayParams) As Holiday` Retrieves a holiday. The holiday is specified by its key, which is contained in the HolidayParams object passed to the method.
  - param `pIHolidayParams`: The key of the holiday to retrieve.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.HolidayParams hdParam = holidayService.GetDataInterface(SAPbobsCOM.HolidayServiceDataInterfaces.hsHolidayParams);
    hdParam.HolidayCode = "2007 Feiertage";
    SAPbobsCOM.Holiday hd = holidayService.GetHoliday(hdParam);
    Console.WriteLine(hd.HolidayCode);
    Console.WriteLine(hd.WeekendFrom);
    Console.WriteLine(hd.WeekendTO);
    Console.WriteLine(hd.ValidForOneYearOnly);
    Console.WriteLine(hd.SetWeekendsAsWorkDays);
    Console.WriteLine(hd.WeekNoRule);
    for (int i = 0; i < hd.HolidayDates.Count; i++)
    {
        Console.WriteLine(" " + hd.HolidayDates.Item(i).StartDate);
        Console.WriteLine(" " + hd.HolidayDates.Item(i).EndDate);
        Console.WriteLine(" " + hd.HolidayDates.Item(i).Remarks);
    }
    ```
- `Public Function GetHolidayList() As HolidaysParams` Returns the HolidaysParams data collection that identify all holidays.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.CompanyService oCmpSrv = oCompany.GetCompanyService();
    SAPbobsCOM.HolidayService holidayService = oCmpSrv.GetBusinessService(SAPbobsCOM.ServiceTypes.HolidayService);
    SAPbobsCOM.HolidaysParams hdList = holidayService.GetHolidayList();
    for (int i = 0; i < hdList.Count; i++)
    {
        Console.WriteLine(hdList.Item(i).HolidayCode);
    }
    ```
- `Public Sub UpdateHoliday(ByVal pIHoliday As Holiday)` Updates an existing holiday. The data for the holiday, including the key of the holiday to be updated, is contained in the Holiday object passed to the method. To update a holiday, you must first retrieve it using the GetHoliday method.
  - param `pIHoliday`: The data for the holiday to be updated. The Holiday object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.HolidayParams hdParams = holidayService.GetDataInterface(HolidayServiceDataInterfaces.hsHolidayParams);
    hdParams.HolidayCode = "holiday1";
    SAPbobsCOM.Holiday hd2 = holidayService.GetHoliday(hdParams);

    hd2.WeekNoRule = BoWeekNoRuleEnum.fromFirstFullWeek;

    int count = hd2.HolidayDates.Count;
    SAPbobsCOM.HolidayDate hdDate1 = hd2.HolidayDates.Item(0);
    hdDate1.Remarks = "new remarks";

    try
    {
        holidayService.UpdateHoliday(hd2);
    }
    catch (Exception ex)
    {
        Console.WriteLine(ex.Message);
    }
    ```

# HolidaysParams (Collection)

A collection of HolidayParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As HolidayParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As HolidayParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# HouseBankAccounts (Object)

The HouseBankAccounts object enables to define the company bank accounts. Source table: DSC1.

**Remarks:** Mandatory fields in SAP Business One: BankKey. To display the form in the application: - Select Administration -->Setup -->Banking -->House Bank Accounts.

## Properties (64)
- `Public Property AbsoluteEntry() As Long` [R] Returns the identification key of the house bank account as assigned by the system when adding a new entry. Field name: AbsEntry.
- `Public Property AccNo() As String` [R/W] Sets or returns the account number of the house bank. Field name: Account. Length: 50 characters.
- `Public Property AccountCheckDigit() As String` [R/W] Sets or returns the account check digit. Field name: AccountChk. Length: 1 character.
- `Public Property AccountName() As String` [R/W] The name of the bank account. Field: AcctName. Length: 250 characters.
- `Public Property AddressType() As String` [R/W] Sets or returns the address type, such as, City or Street. This property is applicable for cluster B only (country-specific for Brazil).
- `Public Property AgreementNumber() As String` [R/W] Sets or returns the agreement number. Field name: AgreeNum. Length: 4 characters.
- `Public Property BankCode() As String` [R] Returns the bank code as defined in the Banks object. Field name: BankCode. Length: 30 characters.
- `Public Property BankKey() As Long` [R/W] Sets or returns the foreign key of the bank as defined in the Banks object. Field name: BankKey. Mandatory property.
- `Public Property BankonCollection() As String` [R/W] Sets or returns the G/L account for bank on collection of bill-of-exchange transactions. Field name: BankCollec. Length: 15 characters.
  - remarks: Applicable for localizations that use a Bill-of-Exchange as a payment method.
- `Public Property BankonDiscounted() As String` [R/W] Sets or returns the G/L account for bank on discounted bill-of-exchange transactions. Field name: BankDiscou. Length: 15 characters.
  - remarks: Applicable for localizations that use a Bill-of-Exchange as a payment method.
- `Public Property BICSwiftCode() As String` [R/W] The BIC/SWIFT code to be used in transactions and messages between banks. Field: SwiftNum. Length: 50 characters.
  - remarks: The default BIC/SWIFT code is taken from the Banks - Setup window of the selected bank code.
- `Public Property BISR() As BoYesNoEnum` [R/W] Determines whether or not to enable printing the bank name and address on BISR invoices. Field name: BISR.
  - remarks: Country-specific for Switzerland.
- `Public Property Block() As String` [R/W] Sets or returns the block of the house bank address. Field name: Block. Length: 100 characters.
- `Public Property Branch() As String` [R/W] Sets or returns the branch of the house bank. Field name: Branch. Length: 50 characters.
- `Public Property BranchCheckDigit() As String` [R/W] property BranchCheckDigit
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Building() As String` [R/W] Sets or returns the Building/Floor/Room details of the house bank address. Field name: Building. Length: 64,000 characters.
- `Public Property City() As String` [R/W] Sets or returns the city of the house bank address. Field name: City. Length: 100 characters.
- `Public Property CollectionCode() As String` [R/W] property CollectionCode
- `Public Property ControlKey() As String` [R/W] Returns control key of the house bank. Field name: ControlKey. Length: 2 characters.
  - remarks: The control key specifies the type of account, for example: 01 indicates Checking Account, 02 indicates Saving Account, and so on. Source code !UNRECOGNISED ELEMENT TYPE 'sourcecode'! " -->Example!UNRECOGNISED ELEMENT TYPE 'filtereditemlist'!" -->See Also !UNRECOGNISED ELEMENT TYPE 'filtereditemlist'! " -->
- `Public Property Country() As String` [R] Sets or returns the country code of the house bank (for example: DE). Field name: Country. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
  - remarks: You can set only country codes that are defined in the Countries table (OCRY - not exposed through the DI API).
- `Public Property County() As String` [R/W] Sets or returns the county of the house bank address. Field name: County. Length: 100 characters. This is a foreign key to the States table (OCST - not exposed through the DI API).
- `Public Property CustomerIdNumber() As String` [R/W] Sets or returns the customer's Id number. Field name: CustIdNum.
  - remarks: This property is applicable if ISRType is set to BISR.
- `Public Property DaysInAdvance() As Long` [R/W] Sets or returns the number of days in advance. Field name: DaysInAdva.
  - remarks: Applicable for localizations that use a Bill-of-Exchange as a payment method.
- `Public Property DebtofDiscountedBillofExc() As String` [R/W] Sets or returns the G/L account for debt of discounted bill-of-exchange transactions. Field name: DscountBOE. Length: 15 characters.
  - remarks: Applicable for localizations that use a Bill-of-Exchange as a payment method.
- `Public Property DiscountAccount() As String` [R/W] property DiscountAccount
- `Public Property DiscountLimit() As Double` [R/W] Sets or returns the maximum discount allowed in a bill-of-exchage payment. Field name: DscntLimit.
  - remarks: Applicable for localizations that use a Bill-of-Exchange as a payment method.
- `Public Property ECheck() As BoYesNoEnum` [R/W] Specifies whether the account is relevant for e-check functionality or not. Field name: ECheck.
- `Public Property FileSeqNextNumber() As Long` [R/W] property FileSeqNextNumber
- `Public Property FineAccount() As String` [R/W] property FineAccount
- `Public Property GLAccount() As String` [R/W] Sets or returns the G/L account number related to the house bank. This is a foreign key to ChartOfAccounts object. Field name: GLAccount. Lentgh: 15 characters.
- `Public Property GLInterimAccount() As String` [R/W] Sets or returns the G/L account number for intermidiate transactions related to the house bank. G/L accounts are defined through the ChartOfAccounts object. Field name: GLIntriAct. Lentgh: 15 characters.
- `Public Property IBAN() As String` [R/W] Sets or returns the International Bank Account Number (IBAN). Field name: IBAN. Length: 50 characters.
- `Public Property ImportFileName() As String` [R/W] Sets or returns the XML file format from which the system downloads the bank statement data of the bank account. Field name: FilePlug. Length: 50 characters.
  - remarks: To enable automatic download from the XML file format, in the application, the ImpStmt field (Imported Bank Statement) must be selected. This property is applicable only if the BankStatementInstalled property of AdminInfo object (OADM) is set to tYes.
- `Public Property IncomingPaymentSeries() As Long` [R/W] Sets or returns the numbering series to be used for incoming payment documents that are created through bank statement processing. This is a foreign key to the Series object. Field name: InSeri.
  - remarks: This property is applicable only if: - The BankStatementInstalled property of AdminInfo object (OADM) is set to tYes. - The field Permit More than One Document Type per Series (DocNmMtd of CINF) must be set to No. This field is not exposed by the DI API.
- `Public Property InterestAccount() As String` [R/W] property InterestAccount
- `Public Property IOFTaxAccount() As String` [R/W] property IOFTaxAccount
- `Public Property ISRBillerID() As String` [R/W] Sets or returns the ISRBillerId. (country-specific for Switzerland only). Field name: ISRBillerI.
- `Public Property ISRType() As Long` [R/W] Sets or returns a valid value that determines this house bank account ISR type. Country-specific for Switzerland only. Field name: ISRType.
- `Public Property JournalEntrySeries() As Long` [R/W] Sets or returns the numbering series to be used for journal entries that are posted through bank statement processing. This is a foreign key to the Series object. Field name: JDTSeri.
  - remarks: This property is applicable only if: - The BankStatementInstalled property of AdminInfo object (OADM) is set to tYes. - The field Permit More than One Document Type per Series (DocNmMtd of CINF) must be set to No. This field is not exposed by the DI API.
- `Public Property LockChecksPrinting() As BoYesNoEnum` [R/W] Determines whether or not to prevent printing checks of the same house bank account by different users simultaneously. Field name: LockChk.
- `Public Property MaxAmountofBillofExchan() As Double` [R/W] Sets or returns the maximum amount allowed in a bill-of-exchange payment. Field name: MaxAmntBOE.
  - remarks: Applicable for localizations that use a Bill-of-Exchange as a payment method.
- `Public Property MaximumLines() As Long` [R/W] Sets or returns the maximum lines to print in the check stub. Field name: MaxChkLine.
- `Public Property MinAmountofBillofExchang() As Double` [R/W] Sets or returns the minimum amount allowed in a bill-of-exchange payment. Field name: MinAmntBOE.
  - remarks: Applicable for localizations that use Bill-of-Exchange as a payment method.
- `Public Property NextCheckNo() As Long` [R/W] Sets or returns the number for the next check. Field name: NextCheck.
- `Public Property NoValidationForStartingEndingBal() As BoYesNoEnum` [R/W] Define whether you can finalize a bank statement even if the difference does not equal zero; and whether the starting balance of your current bank statement can be different to the ending balance of the previous one. Field name: NoValidBal.
  - remarks: No - You can finalize a bank statement only when the difference equals zero; and the starting balance of your current bank statement must be the same to the ending balance of the previous one. Yes - You can finalize a bank statement even if the difference does not equal zero; and the starting balance of your current bank statement can be different to the ending balance of the previous one.
- `Public Property OtherExpensesAccount() As String` [R/W] property OtherExpensesAccount
- `Public Property OtherIncomesAccount() As String` [R/W] property OtherIncomesAccount
- `Public Property OurNumber() As Long` [R/W] Sets or returns the house bank number for Boleto method of payment. This property is applicable for cluser B (country-specific for Brazil). Field name: OurNum.
  - remarks: Boleto is a method of payment, which uses the structure and functions for bills of exchange (BOE).
- `Public Property OutgoingPaymentSeries() As Long` [R/W] Sets or returns the numbering series to be used for outgoing payment documents that are created through bank statement processing. This is a foreign key to the Series object. Field name: OutSeri.
  - remarks: This property is applicable only if: - The BankStatementInstalled property of AdminInfo object (OADM) is set to tYes. - The field Permit More than One Document Type per Series (DocNmMtd of CINF) must be set to No. This field is not exposed by the DI API.
- `Public Property PrintOn() As PrintOnEnum` [R/W] Determines the paper type and printing method of payment checks. Field name: LockChk.
  - remarks: To display the form in thwe application: - Select Administration --> System Initialization --> Print Preferences --> Per Document tab. - From the Document drop-down list, select Checks for Payment.
- `Public Property RetornoFileName() As String` [R/W] property RetornoFileName
- `Public Property ServiceFeeAccount() As String` [R/W] property ServiceFeeAccount
- `Public Property State() As String` [R/W] Sets or returns the state code of the house bank. This is a foreign key to the States table (OCST), which is not exposed through the DI API. Field name: State. Length: 3 characters.
  - remarks: Only state codes that are defined in the States table are applicable.
- `Public Property Street() As String` [R/W] Sets or returns the street of the house bank address. Field name: Street. Length: 100 characters.
- `Public Property StreetNo() As String` [R/W] Sets or returns the street number of the house bank address. This property is applicable for cluster B only (country-specific for Brazil).
- `Public Property TemplateName() As String` [R/W] Sets or returns the layout code of the checks template. The layout code is the key of the ReportLayoutParams object. Field name: TmpltName. Lentgh: 8 characters.
  - remarks: The House Bank Accounts form displays the template name such as, stub-check-stub, check-stub-stub, checks not based on invoice (US), but the TemplateName property actually contains the layout code (for example, CHO10001). The list of templates is a result of a system query that retrieves from the RDOC table all the templates that start with CHO, and then displays their names.
- `Public Property ToleranceDays() As Long` [R/W] Sets or returns the number of days earlier than the calculated due date to start expecting the bill-of-exchange payment. Field name: TolrnceDay.
  - remarks: For example: If the payment due date is October 1, and the value of ToleranceDays is 5, the payment is expected to be received starting from September 26. Applicable for localizations that use a Bill-of-Exchange as a payment method.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserNo1() As String` [R/W] Sets or returns the first number or password, defined by the user, for identifying a payment file for the specific account. Field name: UsrNumber1. Length: 25 characters.
- `Public Property UserNo2() As String` [R/W] Sets or returns the second number or password, defined by the user, for identifying a payment file for the specific account. Field name: UsrNumber2. Length: 25 characters.
- `Public Property UserNo3() As String` [R/W] Sets or returns the third number or password, defined by the user, for identifying a payment file for the specific account. Field name: UsrNumber3. Length: 25 characters.
- `Public Property UserNo4() As String` [R/W] Sets or returns the forth number or password, defined by the user, for identifying a payment file for the specific account. Field name: UsrNumber4. Length: 25 characters.
- `Public Property ZipCode() As String` [R/W] Sets or returns the zip code of the house bank address. Field name: ZipCode. Length: 20 characters.

## Methods (7)
- `Public Function Add() As Long` Adds a new record of house bank accounts table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lAbsEntry As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lAbsEntry`: 
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes the current record.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal bstrFileName As String)` Save the object to a file as XML data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef pbstrFileName As String)` Saves the object data to XML formatted data.
  - param `pbstrFileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# IdentificationCode (Object)

IdentificationCode Class

## Properties (6)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property Code() As String` [R/W] property Code
- `Public Property Codelist() As IdentificationCodeTypeEnum` [R/W] property Codelist
- `Public Property Description() As String` [R/W] property Description
- `Public Property SchemaCode() As String` [R/W] property SchemaCode
- `Public Property SchemaDesc() As String` [R/W] property SchemaDesc

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# IdentificationCodeParams (Object)

IdentificationCodeParams Class

## Properties (1)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# IdentificationCodes (Collection)

IdentificationCodes Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As IdentificationCode` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As IdentificationCode` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# IdentificationCodeService (Object)

IdentificationCodeService Class

## Methods (8)
- `Public Function Add(ByVal pIIdentificationCode As IdentificationCode) As IdentificationCodeParams` Add
  - param `pIIdentificationCode`: 
- `Public Function GetByParams(ByVal pIIdentificationCodeParams As IdentificationCodeParams) As IdentificationCode` GetByParams
  - param `pIIdentificationCodeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As IdentificationCodeServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `IdentificationCodeServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As IdentificationCodes` GetList
- `Public Sub Remove(ByVal pIIdentificationCodeParams As IdentificationCodeParams)` Remove
  - param `pIIdentificationCodeParams`: 
- `Public Sub Update(ByVal pIIdentificationCode As IdentificationCode)` Update
  - param `pIIdentificationCode`: 

# ImportDetermination (Object)

ImportDetermination Class

## Properties (9)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R/W] property Code
- `Public Property DefaultDigitalSeries() As Long` [R/W] property DefaultDigitalSeries
- `Public Property FieldType() As ImportFieldTypeEnum` [R/W] property FieldType
- `Public Property FieldTypeXPath() As String` [R/W] property FieldTypeXPath
- `Public Property ImportFormat() As Long` [R/W] property ImportFormat
- `Public Property LineNumber() As Long` [R/W] property LineNumber
- `Public Property ObjectType() As String` [R/W] property ObjectType
- `Public Property ObjectTypeXPath() As String` [R/W] property ObjectTypeXPath

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ImportDeterminationParams (Object)

ImportDeterminationParams Class

## Properties (3)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R/W] property Code
- `Public Property ObjectType() As String` [R/W] property ObjectType

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ImportDeterminationsCollection (Collection)

ImportDeterminationsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As ImportDetermination` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As ImportDetermination` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ImportDeterminationService (Object)

ImportDeterminationService Class

## Methods (8)
- `Public Sub AddDetermination(ByVal pIImportDetermination As ImportDetermination)` AddDetermination
  - param `pIImportDetermination`: 
- `Public Sub DeleteDetermination(ByVal pIImportDeterminationParams As ImportDeterminationParams)` DeleteDetermination
  - param `pIImportDeterminationParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ImportDeterminationServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ImportDeterminationServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetDetermination(ByVal pIImportDeterminationParams As ImportDeterminationParams) As ImportDetermination` GetDetermination
  - param `pIImportDeterminationParams`: 
- `Public Function GetDeterminations(ByVal pIImportDeterminationsParams As ImportDeterminationsParams) As ImportDeterminationsCollection` GetDeterminations
  - param `pIImportDeterminationsParams`: 
- `Public Sub UpdateDetermination(ByVal pIImportDetermination As ImportDetermination)` UpdateDetermination
  - param `pIImportDetermination`: 

# ImportDeterminationsParams (Object)

ImportDeterminationsParams Class

## Properties (1)
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R/W] property Code

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ImportFileParam (Object)

Borrows an existing field to input the EFM file path. It is an input parameter for the AddElectronicFileFormat method.

## Properties (1)
- `Public Property FilePath() As String` [R/W] The destination file path for the electronic file. Field name: OutPath.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ImportProcesses (Object)

Source table: DOC17.

## Properties (11)
- `Public Property AdditionalFreightToNavyAuthority() As Double` [R/W] Enter the Additional Freight to Navy Authority amount. This amount is only relevant if you chose the 1 - Maritime option in the Transport Route field in the Import Process window. Field name: AddFrNavyA.
- `Public Property AdditionalItemDiscountValue() As Double` [R/W] Additional Item Discount Value. Field name: AddItmDV.
- `Public Property AdditionalItemSequentialNumber() As Long` [R/W] Enter the Additional Item Sequential Number for the Import Process. Field name: nSeqAdic.
- `Public Property AdditionalNumber() As String` [R/W] Additional Number. Field name: AdditNum. Length: 30 characters.
- `Public Property CustomsClearanceDate() As Date` [R/W] Date of Customs Clearance. Field name: CustClrDat.
- `Public Property DateOfRegistry_DI_DSI_DA() As Date` [R/W] Date of Registry DI/DSI/DA. Field name: DateOfReg.
- `Public Property DrawbackRegimeConcessionAccountNumber() As String` [R/W] Drawback Concession Acct Number. Field name: ConcActNum. Length: 30 characters.
- `Public Property DrawbackSuspensionRegime() As String` [R/W] Drawback Suspension Regime. Field name: DrawSReg. Length: 11 characters.
- `Public Property ImportationDocumentNumber() As String` [R/W] Importation Document Number. Field name: ImpDocNum. Length: 10 characters.
- `Public Property ImportationDocumentTypeCode() As String` [R/W] Type of Importation Document. Field name: ImpDocType. Length: 1 characters.
- `Public Property TypeOfImport() As String` [R/W] Type of Import. Field name: TypeOfImp. Length: 1 characters.

# IndiaHsn (Object)

India HSN master data. Source table: OCHP.

**Remarks:** Inventory --> Item Master Data --> General tab --> HSN field (for India only)

## Properties (6)
- `Public Property AbsEntry() As Long` [R] Primary key for HSN. Field name: AbsEntry.
- `Public Property Chapter() As String` [R/W] Chapter string. Field name: Chapter. Length: 20 characters.
- `Public Property ChapterID() As String` [R] HSN. Field name: ChapterID. Length: 64 characters.
- `Public Property Description() As String` [R/W] Description of HSN. Field name: Dscription. Length: 120 characters.
- `Public Property Heading() As String` [R/W] Heading string. Field name: Heading. Length: 20 characters.
- `Public Property SubHeading() As String` [R/W] Subheading string. Field name: SubHeading. Length: 20 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# IndiaHsnParams (Object)

The parameters needed for searching HSN

## Properties (2)
- `Public Property AbsEntry() As Long` [R/W] Primary key for HSN. Field name: AbsEntry.
- `Public Property ChapterID() As String` [R] HSN. Field name: ChapterID. Length: 64 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# IndiaHsnParamsCollection (Collection)

IndiaHsnParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As IndiaHsnParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As IndiaHsnParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# IndiaHsnService (Object)

India HSN master data. Source table: OCHP.

**Remarks:** Inventory --> Item Master Data --> General tab --> HSN field (for India only)

**Example:**
- C# example (from SAP's help):
  ```csharp
  SAPbobsCOM.IndiaHsnService hsnService = (SAPbobsCOM.IndiaHsnService)cmpy.GetCompanyService().GetBusinessService(SAPbobsCOM.ServiceTypes.IndiaHsnService);
  SAPbobsCOM.IndiaHsn hsn = (SAPbobsCOM.IndiaHsn)hsnService.GetDataInterface(IndiaHsnServiceDataInterfaces.iscIndiaHsn);

  hsn.Chapter = ""22"";
  hsn.Heading = ""02"";
  hsn.SubHeading = ""0102"";
  hsn.Description = ""Add "" + hsn.Chapter + hsn.Heading + hsn.SubHeading + "" from DI"";

  var hsnParams = hsnService.Add(hsn);
  ```

## Methods (8)
- `Public Function Add(ByVal pIIndiaHsn As IndiaHsn) As IndiaHsnParams` Add
  - param `pIIndiaHsn`: 
- `Public Sub Delete(ByVal pIIndiaHsnParams As IndiaHsnParams)` Delete
  - param `pIIndiaHsnParams`: 
- `Public Function Get(ByVal pIIndiaHsnParams As IndiaHsnParams) As IndiaHsn` Get
  - param `pIIndiaHsnParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As IndiaHsnServiceDataInterfaces) As Object` Creates an empty data structure for use with the IndiaHsnService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `IndiaHsnServiceDataInterfaces` in `../enums/enums-02.md`
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
- `Public Function GetList() As IndiaHsnParamsCollection` GetList
- `Public Sub Update(ByVal pIIndiaHsn As IndiaHsn)` Update
  - param `pIIndiaHsn`: 

# IndiaSacCode (Object)

IndiaSacCode Class

## Properties (3)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property ServiceCode() As String` [R/W] property ServiceCode
- `Public Property ServiceName() As String` [R/W] property ServiceName

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# IndiaSacCodeParams (Object)

IndiaSacCodeParams Class

## Properties (2)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property ServiceCode() As String` [R/W] property ServiceCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# IndiaSacCodeParamsCollection (Collection)

IndiaSacCodeParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As IndiaSacCodeParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As IndiaSacCodeParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# IndiaSacCodeService (Object)

IndiaSacCodeService Class

## Methods (8)
- `Public Function Add(ByVal pIIndiaSacCode As IndiaSacCode) As IndiaSacCodeParams` Add
  - param `pIIndiaSacCode`: 
- `Public Sub Delete(ByVal pIIndiaSacCodeParams As IndiaSacCodeParams)` Delete
  - param `pIIndiaSacCodeParams`: 
- `Public Function Get(ByVal pIIndiaSacCodeParams As IndiaSacCodeParams) As IndiaSacCode` Get
  - param `pIIndiaSacCodeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As IndiaSacCodeServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `IndiaSacCodeServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As IndiaSacCodeParamsCollection` GetList
- `Public Sub Update(ByVal pIIndiaSacCode As IndiaSacCode)` Update
  - param `pIIndiaSacCode`: 

# IndividualCounter (Object)

Individual counters conduct independent counting of an item at a storage location. Source table: INC8.

## Properties (6)
- `Public Property CounterID() As Long` [R/W] The ID of the counter. Field name: CounterId.
- `Public Property CounterName() As String` [R] The name of the counter. Field name: CounteName.
- `Public Property CounterNumber() As Long` [R/W] The number of the counter. Field name: CounteNum.
- `Public Property CounterType() As CounterTypeEnum` [R/W] The type of the counter. Field name: CounteType.
- `Public Property CounterVisualOrder() As Long` [R] The visual order number of the counter. The value for the first row is null, and from the second row the number starts from 1. Field name: VisOrder.
- `Public Property DocumentEntry() As Long` [R] The internal key of the inventory counting. Field name: DocEntry.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# IndividualCounters (Collection)

A collection of IndividualCounter objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As IndividualCounter` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As IndividualCounter` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub Remove(ByVal vtIndex As Variant)` Removes the object at the specified index.
  - param `vtIndex`: The index of the object to be removed.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# Industries (Object)

Industries is a business object that represents the industries list from which an industry can be associated with a sales opportunity. This object enables you to: - Add an industry to the list. - Retrieve an industry by its key. - Update an industry. - Save the object in XML format. Source table: OOND.

**Remarks:** To display the form in the application: - Select Sales Opportunities --> Sales Opportunity. - In the General tab, from the Industry list box, select Define New.

## Properties (5)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property IndustryCode() As Long` [R] Returns the industry ID number. SAP Business One assigns this number when adding an industry to the industries list. IndCode Field name: IndCode.
- `Public Property IndustryDescription() As String` [R/W] Sets or returns the industry description. Field name: IndDesc. Length: 120 characters.
- `Public Property IndustryName() As String` [R/W] Sets or returns the industry name. Field name: IndName. Length: 40 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (6)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal Code As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `Code`: Industry code (IndustryCode).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# IntegrationPackageConfigure (Object)

IntegrationPackageConfigure Class

## Properties (4)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property Code() As String` [R] property Code
- `Public Property IsEnable() As BoYesNoEnum` [R/W] property IsEnable
- `Public Property Name() As String` [R] property Name

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# IntegrationPackageParams (Object)

IntegrationPackageParams Class

## Properties (1)
- `Public Property Code() As String` [R/W] property Code

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# IntegrationPackagesConfigureService (Object)

IntegrationPackagesConfigureService Class

## Methods (6)
- `Public Function Get(ByVal pIIntegrationPackageParams As IntegrationPackageParams) As IntegrationPackageConfigure` Get
  - param `pIIntegrationPackageParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As IntegrationPackagesConfigureServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `IntegrationPackagesConfigureServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As IntegrationPackagesParams` GetList
- `Public Sub Update(ByVal pIIntegrationPackageConfigure As IntegrationPackageConfigure)` Update
  - param `pIIntegrationPackageConfigure`: 

# IntegrationPackagesParams (Collection)

IntegrationPackagesParams Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As IntegrationPackageParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As IntegrationPackageParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# InternalReconciliation (Object)

InternalReconciliation Class

## Properties (8)
- `Public Property CancelAbs() As Long` [R] property CancelAbs
- `Public Property CardOrAccount() As CardOrAccountEnum` [R] property CardOrAccount
- `Public Property ElectronicProtocols() As ElectronicProtocolCollection` [R] property ElectronicProtocols
- `Public Property InternalReconciliationRows() As InternalReconciliationRows` [R] property InternalReconciliationRows
- `Public Property ReconDate() As Date` [R] property ReconDate
- `Public Property ReconNum() As Long` [R] property ReconNum
- `Public Property ReconType() As ReconTypeEnum` [R] property ReconType
- `Public Property Total() As Double` [R] property Total

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# InternalReconciliationBP (Object)

InternalReconciliationBP Class

## Properties (1)
- `Public Property BPCode() As String` [R/W] property BPCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# InternalReconciliationBPs (Collection)

InternalReconciliationBPs Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As InternalReconciliationBP` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As InternalReconciliationBP` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# InternalReconciliationOpenTrans (Object)

InternalReconciliationOpenTrans Class

## Properties (5)
- `Public Property BPLID() As Long` [R/W] property BPLId
- `Public Property CardOrAccount() As CardOrAccountEnum` [R/W] property CardOrAccount
- `Public Property ElectronicProtocols() As ElectronicProtocolCollection` [R] property ElectronicProtocols
- `Public Property InternalReconciliationOpenTransRows() As InternalReconciliationOpenTransRows` [R] property InternalReconciliationOpenTransRows
- `Public Property ReconDate() As Date` [R/W] property ReconDate

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# InternalReconciliationOpenTransParams (Object)

InternalReconciliationOpenTransParams Class

## Properties (7)
- `Public Property AccountNo() As String` [R/W] property AccountNo
- `Public Property CardOrAccount() As CardOrAccountEnum` [R/W] property CardOrAccount
- `Public Property DateType() As ReconSelectDateTypeEnum` [R/W] property DateType
- `Public Property FromDate() As Date` [R/W] property FromDate
- `Public Property InternalReconciliationBPs() As InternalReconciliationBPs` [R] property InternalReconciliationBPs
- `Public Property ReconDate() As Date` [R/W] property ReconDate
- `Public Property ToDate() As Date` [R/W] property ToDate

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# InternalReconciliationOpenTransRow (Object)

InternalReconciliationOpenTransRow Class

## Properties (9)
- `Public Property CashDiscount() As Double` [R/W] property CashDiscount
- `Public Property CreditOrDebit() As CreditOrDebitEnum` [R] property CreditOrDebit
- `Public Property ReconcileAmount() As Double` [R/W] property ReconcileAmount
- `Public Property Selected() As BoYesNoEnum` [R/W] property Selected
- `Public Property ShortName() As String` [R] property ShortName
- `Public Property SrcObjAbs() As Long` [R] property SrcObjAbs
- `Public Property SrcObjTyp() As String` [R] property SrcObjTyp
- `Public Property TransId() As Long` [R/W] property TransId
- `Public Property TransRowId() As Long` [R/W] property TransRowId

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# InternalReconciliationOpenTransRows (Collection)

InternalReconciliationOpenTransRows Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As InternalReconciliationOpenTransRow` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As InternalReconciliationOpenTransRow` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# InternalReconciliationParams (Object)

InternalReconciliationParams Class

## Properties (1)
- `Public Property ReconNum() As Long` [R/W] property ReconNum

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# InternalReconciliationRow (Object)

InternalReconciliationRow Class

## Properties (9)
- `Public Property CashDiscount() As Double` [R] property CashDiscount
- `Public Property CreditOrDebit() As CreditOrDebitEnum` [R] property CreditOrDebit
- `Public Property LineSeq() As Long` [R] property LineSeq
- `Public Property ReconcileAmount() As Double` [R] property ReconcileAmount
- `Public Property ShortName() As String` [R] property ShortName
- `Public Property SrcObjAbs() As Long` [R] property SrcObjAbs
- `Public Property SrcObjTyp() As String` [R] property SrcObjTyp
- `Public Property TransId() As Long` [R] property TransId
- `Public Property TransRowId() As Long` [R] property TransRowId

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# InternalReconciliationRows (Collection)

InternalReconciliationRows Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As InternalReconciliationRow` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As InternalReconciliationRow` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# InternalReconciliationsService (Object)

InternalReconciliationsService Class

## Methods (9)
- `Public Function Add(ByVal pIInternalReconciliationOpenTrans As InternalReconciliationOpenTrans) As InternalReconciliationParams` Add
  - param `pIInternalReconciliationOpenTrans`: 
- `Public Sub Cancel(ByVal pIInternalReconciliationParams As InternalReconciliationParams)` Cancel
  - param `pIInternalReconciliationParams`: 
- `Public Function Get(ByVal pIInternalReconciliationParams As InternalReconciliationParams) As InternalReconciliation` Get
  - param `pIInternalReconciliationParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As InternalReconciliationsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `InternalReconciliationsServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetOpenTransactions(ByVal pInternalReconciliationOpenTransParams As InternalReconciliationOpenTransParams) As InternalReconciliationOpenTrans` GetOpenTransactions
  - param `pInternalReconciliationOpenTransParams`: 
- `Public Sub RequestApproveCancellation(ByVal pIInternalReconciliationParams As InternalReconciliationParams)` RequestApproveCancellation
  - param `pIInternalReconciliationParams`: 
- `Public Sub Update(ByVal pIInternalReconciliation As InternalReconciliation)` Update
  - param `pIInternalReconciliation`: 

# IntrastatConfiguration (Object)

IntrastatConfiguration Class

## Properties (14)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property Code() As String` [R/W] property Code
- `Public Property ConfID() As String` [R] property Configuration ID
- `Public Property ConfType() As IntrastatConfigurationEnum` [R/W] property Configuration Type
- `Public Property Country() As String` [R/W] property Country
- `Public Property Description() As String` [R/W] property Description
- `Public Property PercentageValue() As Double` [R/W] property Percentage Value
- `Public Property StatisticalCode() As String` [R/W] property Statistical Code
- `Public Property SupplementaryUnit() As Long` [R/W] property Supplementary Unit
- `Public Property TriangDeal() As IntrastatConfigurationTriangDealEnum` [R/W] property Triangulate Deal
- `Public Property ValidExport() As BoYesNoEnum` [R/W] property Valid for Export
- `Public Property ValidFrom() As Date` [R/W] property Valid From
- `Public Property ValidImport() As BoYesNoEnum` [R/W] property Valid for Import
- `Public Property ValidTo() As Date` [R/W] property Valid To

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# IntrastatConfigurationCollectionParams (Collection)

IntrastatConfigurationCollectionParams Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As IntrastatConfigurationParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As IntrastatConfigurationParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# IntrastatConfigurationParams (Object)

IntrastatConfigurationParams Class

## Properties (6)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property Code() As String` [R/W] property Code
- `Public Property ConfType() As IntrastatConfigurationEnum` [R/W] property Configuration Type
- `Public Property Country() As String` [R/W] property Country
- `Public Property StatisticalCode() As String` [R/W] property Statistical Code
- `Public Property ValidFrom() As Date` [R/W] property Valid From

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# IntrastatConfigurationService (Object)

IntrastatConfigurationService Class

## Methods (8)
- `Public Function Add(ByVal pIIntrastatConfiguration As IntrastatConfiguration) As IntrastatConfigurationParams` Add
  - param `pIIntrastatConfiguration`: 
- `Public Sub Delete(ByVal pIIntrastatConfigurationParams As IntrastatConfigurationParams)` Delete
  - param `pIIntrastatConfigurationParams`: 
- `Public Function Get(ByVal pIIntrastatConfigurationParams As IntrastatConfigurationParams) As IntrastatConfiguration` Get
  - param `pIIntrastatConfigurationParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As IntrastatConfigurationServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `IntrastatConfigurationServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As IntrastatConfigurationCollectionParams` GetList
- `Public Sub Update(ByVal pIIntrastatConfiguration As IntrastatConfiguration)` Update
  - param `pIIntrastatConfiguration`: 

# InventoryCounting (Object)

You can use this object to specify items for inventory counting and record the counting results. Source table: OINC.

## Properties (22)
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property BranchID() As Long` [R/W] The branch for which you want to create the document, just for the Brazilian localization. Field name: BPLId.
- `Public Property CountDate() As Date` [R/W] The date when inventory was counted. Field name: CountDate.
  - remarks: You cannot set a future date and time. Once you update the count date and time, SAP Business One updates the in-warehouse quantities on the count date accordingly.
- `Public Property CountingType() As CountingTypeEnum` [R/W] The counting type. Field name: CountType.
- `Public Property CountTime() As Date` [R/W] The exact time when the counting began. Field name: Time.
  - remarks: You cannot set a future date and time. Once you update the count date and time, SAP Business One updates the in-warehouse quantities on the count date accordingly.
- `Public Property DocObjectCodeEx() As String` [R] The type of the document. Field name: ObjType.
- `Public Property DocumentEntry() As Long` [R] The internal key of the inventory counting. Field name: DocEntry.
- `Public Property DocumentNumber() As Long` [R] The document number of the inventory counting transaction. Field name: DocNum.
- `Public Property DocumentReferences() As InventoryCountingDocumentReferences` [R] property DocumentReferences
- `Public Property DocumentStatus() As CountingDocumentStatusEnum` [R] The status of this document. Default status is Open. Field name: Status.
- `Public Property FinancialPeriod() As Long` [R] The financial period.
- `Public Property IndividualCounters() As IndividualCounters` [R] Individual counters conduct independent counting of an item at a storage location.
  - remarks: SAP Business One supports the following counting scenarios: A single counter Multiple counters: Individual counting where individual counters conduct independent counting of an item at a storage location Team counting where a group of counters' counting results of an item at a storage location add up to its total quantity A combination of individual counting and team counting
- `Public Property InventoryCountingLines() As InventoryCountingLines` [R] The line entries of an inventory counting transaction.
- `Public Property PeriodIndicator() As String` [R] The financial period indicator, a foreign key to OPID.
- `Public Property Reference2() As String` [R/W] The second reference code of the document. Field name: Ref2. Length: 11 characters.
- `Public Property Remarks() As String` [R/W] The remarks of the inventory counting document. Field name: Remarks. Length: 16 characters.
- `Public Property Series() As Long` [R/W] The auto-number series that generated the document number. Field name: Series.
- `Public Property SingleCounterID() As Long` [R/W] The ID of the single counter. Field name: Taker1Id.
- `Public Property SingleCounterType() As CounterTypeEnum` [R/W] The type of the single counter. Field name: Taker1Type.
- `Public Property TeamCounters() As TeamCounters` [R] A group of counters' counting results of an item at a storage location add up to its total quantity.
  - remarks: SAP Business One supports the following counting scenarios: A single counter Multiple counters: Individual counting where individual counters conduct independent counting of an item at a storage location Team counting where a group of counters' counting results of an item at a storage location add up to its total quantity A combination of individual counting and team counting
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.
- `Public Property YearEndDate() As Date` [R/W] property YearEndDate

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# InventoryCountingBatchNumber (Object)

InventoryCountingBatchNumber is a child object of the InventoryCountingLine object and enables you to count inventory by batch number. Source table: BTNT1.

## Properties (16)
- `Public Property AddmisionDate() As Date` [R/W] The creation date of the batch number. Field name: InDate.
- `Public Property BaseLineNumber() As Long` [R/W] The base sub line number. Field name: DocLineNum.
- `Public Property BatchNumber() As String` [R/W] The batch number.
- `Public Property CounterID() As Long` [R/W] The ID of the counter. Field name: CounterId.
- `Public Property CounterType() As CounterTypeEnum` [R/W] The type of the counter. Field name: CounteType.
- `Public Property DocumentEntry() As Long` [R] The internal key of the inventory counting. Field name: DocEntry.
- `Public Property ExpiryDate() As Date` [R/W] The expiry date of the batch number. Field name: ExpDate.
- `Public Property InternalSerialNumber() As String` [R/W] The internal serial number.
- `Public Property Location() As String` [R/W] The location of the item in the warehouse. Field name: Location. Length: 100 characters.
- `Public Property ManufactureDate() As Date` [R/W] The date on which the item was manufactured. Field name: MnfDate.
- `Public Property ManufacturerSerialNumber() As String` [R/W] The manufacturer serial number. Field name: MnfSerial. Length: 36 characters.
- `Public Property MultipleCounterRole() As MultipleCounterRoleEnum` [R/W] The role of the multiple counters, that is, the multiple counters conduct the inventory counting individually or as a team. Field name: CounteRole.
- `Public Property Notes() As String` [R/W] Specify any free text regarding batch numbers. Field name: Notes. Length: 16 characters.
- `Public Property Quantity() As Double` [R/W] The number of units that is included in the batch. Field name: Quantity.
- `Public Property TrackingNote() As Long` [R/W] property TrackingNote
- `Public Property TrackingNoteLine() As Long` [R/W] property TrackingNoteLine

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# InventoryCountingBatchNumbers (Collection)

A collection of InventoryCountingBatchNumber objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As InventoryCountingBatchNumber` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As InventoryCountingBatchNumber` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub Remove(ByVal vtIndex As Variant)` Removes the object at the specified index.
  - param `vtIndex`: The index of the object to be removed.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# InventoryCountingDocumentReference (Object)

InventoryCountingDocumentReference Class

## Properties (8)
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property ExternalReferencedDocNumber() As String` [R/W] property ExternalReferencedDocNumber
- `Public Property IssueDate() As Date` [R/W] property IssueDate
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property ReferencedDocEntry() As Long` [R/W] property ReferencedDocEntry
- `Public Property ReferencedDocNumber() As Long` [R] property ReferencedDocNumber
- `Public Property ReferencedObjectType() As ReferencedObjectTypeEnum` [R/W] property ReferencedObjectType
- `Public Property Remark() As String` [R/W] property Remark

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# InventoryCountingDocumentReferences (Collection)

InventoryCountingDocumentReferences Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As InventoryCountingDocumentReference` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As InventoryCountingDocumentReference` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` method Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# InventoryCountingLine (Object)

InventoryCountingLine is a child object of the InventoryCounting object and represents the line entries of the inventory counting transaction. Source table: INC1V, INC1. INC1V table is a virtual table to store the line data for inventory counting transaction.

## Properties (39)
- `Public Property BarCode() As String` [R/W] The barcode of the item. Field name: BarCode. Length: 16 characters.
  - remarks: If you use multiple UoMs (sub object InventoryCountingLineUoM), the value in this property will be ignored.
- `Public Property BinEntry() As Long` [R/W] The bin location for the item you want to count. Mandatory property if you use bin. Field name: BinEntry.
- `Public Property CostingCode() As String` [R/W] The distribution rule for dimension 1 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode. Length: 8 characters.
- `Public Property CostingCode2() As String` [R/W] The distribution rule for dimension 2 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode2. Length: 8 characters.
- `Public Property CostingCode3() As String` [R/W] The distribution rule for dimension 3 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode3. Length: 8 characters.
- `Public Property CostingCode4() As String` [R/W] The distribution rule for dimension 4 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode4. Length: 8 characters.
- `Public Property CostingCode5() As String` [R/W] The distribution rule for dimension 5 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode5. Length: 8 characters.
- `Public Property Counted() As BoYesNoEnum` [R/W] Indicates whether the item was counted, and vice versa. Field name: Counted.
- `Public Property CountedQuantity() As Double` [R/W] The quantity of the item as counted in actual warehouses. Field name: CountQty.
  - remarks: If you use multiple UoM (sub object InventoryCountingLineUoM), the value in this property will be ignored.
- `Public Property CounterID() As Long` [R/W] The ID of the counter. Field name: CounterId.
- `Public Property CounterType() As CounterTypeEnum` [R/W] The type of the counter. Field name: CounteType.
- `Public Property DocumentEntry() As Long` [R] The internal key of the inventory counting. Field name: DocEntry.
- `Public Property Freeze() As BoYesNoEnum` [R/W] Specify whether you want to freeze an item, that is, prevent any transaction (except inventory posting) that affects the in-warehouse quantity of the item in the selected warehouse and bin. Field name: Freeze.
- `Public Property InventoryCountingBatchNumbers() As InventoryCountingBatchNumbers` [R] The sub object to count inventory by batch number.
- `Public Property InventoryCountingLineUoMs() As InventoryCountingLineUoMs` [R] The sub object to count inventory by unit of measure.
- `Public Property InventoryCountingSerialNumbers() As InventoryCountingSerialNumbers` [R] The sub object to count inventory by serial number.
- `Public Property InWarehouseQuantity() As Double` [R] The quantities of an item in warehouses as recorded by the system on the selected count date and time. Field name: InWhsQty.
- `Public Property ItemCode() As String` [R/W] The code of the item that you specified for the inventory. Mandatory property. Not mandatory only if BarCode is specified and is unique. Field name: ItemCode. Length: 20 characters.
- `Public Property ItemDescription() As String` [R/W] The description of the item that you specified for the inventory. Field name: ItemDesc. Length: 100 characters.
- `Public Property ItemsPerUnit() As Double` [R] The calculated value from the group UoM definition of the item. Inventory Items per Unit = Base Qty ÷ Alt. QQty Field name: ItmsPerUnt.
- `Public Property LineNumber() As Long` [R/W] The line number of the inventory counting document. Field name: LineNum.
- `Public Property LineStatus() As CountingLineStatusEnum` [R/W] Determines this document is open or close. Field name: LineStatus.
- `Public Property Manufacturer() As Long` [R/W] The manufacturer code of the item (foreign key of the Manufacturers object). Field name: FirmCode.
- `Public Property MultipleCounterRole() As MultipleCounterRoleEnum` [R/W] The role of the multiple counters, that is, the multiple counters conduct the inventory counting individually or as a team. Field name: CounteRole.
- `Public Property PreferredVendor() As String` [R/W] The preferred vendor for the item. Field name: PrefVendor. Length: 15 characters.
- `Public Property ProjectCode() As String` [R/W] The project code related to the document. Field name: ProjCode. Length: 20 characters.
- `Public Property Remarks() As String` [R/W] The remarks of the inventory counting document line. Field name: Remark. Length: 254 characters.
- `Public Property SupplierCatalogNo() As String` [R/W] The vendor catalog number. Field name: SuppCatNum. Length: 17 characters.
- `Public Property TargetEntry() As Long` [R] The target document internal ID. Field name: TargetEntr.
- `Public Property TargetLine() As Long` [R] The target document line. Field name: TargetLine.
- `Public Property TargetReference() As String` [R] The target document reference. Field name: TargetRef.
- `Public Property TargetType() As Long` [R] The target document type. Field name: TargetType.
- `Public Property UoMCode() As String` [R/W] The UoM code. Field name: UomCode. Length: 20 characters.
  - remarks: If you use multiple UoM (sub object InventoryCountingLineUoM), the value in this property will be ignored.
- `Public Property UoMCountedQuantity() As Double` [R/W] The counted quantity in the specified UoM. Field name: UomQty.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.
- `Public Property Variance() As Double` [R] Displays the difference between the in-warehouse quantity on the count date and the counted quantity. Field name: Difference.
- `Public Property VariancePercentage() As Double` [R] Displays the absolute variance percentage between the in-warehouse quantity on the count date and the counted quantity. Field name: DiffPercen.
- `Public Property VisualOrder() As Long` [R] The visual order number. The value for the first row is null, and from the second row the number starts from 1. Field name: VisOrder.
- `Public Property WarehouseCode() As String` [R/W] The code of the warehouse where the item locates. Mandatory property. Field name: WhsCode. Length: 8 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# InventoryCountingLines (Collection)

A collection of InventoryCountingLine objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As InventoryCountingLine` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As InventoryCountingLine` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub Remove(ByVal vtIndex As Variant)` Removes the object at the specified index.
  - param `vtIndex`: The index of the object to be removed.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# InventoryCountingLineUoM (Object)

InventoryCountingLineUoM is a child object of the InventoryCountingLine object and enables you to count inventory by unit of measure (UoM). Source table: INC2V, INC2. INC2V table contains information of multiple UoMs.

## Properties (12)
- `Public Property BarCode() As String` [R/W] The barcode of the item. Field name: BarCode. Length: 16 characters.
- `Public Property ChildNumber() As Long` [R] ChildNum indicates for one "UoM Code" + "Bar Code". Field name: ChildNum.
- `Public Property CountedQuantity() As Double` [R/W] The item quantity in the warehouse as counted in the inventory taking. Field name: CountQty.
- `Public Property CounterID() As Long` [R/W] The ID of the counter. Field name: CounterId.
- `Public Property CounterType() As CounterTypeEnum` [R/W] The type of the counter. Field name: CounteType.
- `Public Property DocumentEntry() As Long` [R] The internal key of the inventory counting. Field name: DocEntry.
- `Public Property ItemsPerUnit() As Double` [R] The calculated value from the group UoM definition of the item. Inventory Items per Unit = Base Qty ÷ Alt. QQty Field name: ItmsPerUnt.
- `Public Property LineNumber() As Long` [R/W] The line number of the inventory counting document. Field name: LineNum.
- `Public Property MultipleCounterRole() As MultipleCounterRoleEnum` [R/W] The role of the multiple counters, that is, the multiple counters conduct the inventory counting individually or as a team. Field name: CounteRole.
- `Public Property UoMCode() As String` [R/W] The UoM code. Field name: UomCode. Length: 20 characters.
- `Public Property UoMCountedQuantity() As Double` [R/W] The counted quantity in the specified UoM. Field name: UomQty.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# InventoryCountingLineUoMs (Collection)

A collection of InventoryCountingLineUoM objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As InventoryCountingLineUoM` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As InventoryCountingLineUoM` Returns the object at the specified index.
  - param `vtIndex`: Specifies the index of the object.
- `Public Sub Remove(ByVal vtIndex As Variant)` Removes the object at the specified index.
  - param `vtIndex`: The index of the object to be removed.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# InventoryCountingParams (Object)

Holds the key to an existing inventory counting transaction. This object is used to pass keys to and retrieve keys from InventoryCountingsService methods.

## Properties (2)
- `Public Property DocumentEntry() As Long` [R/W] The internal key of the inventory counting. Field name: DocEntry.
- `Public Property DocumentNumber() As Long` [R] The document number of the inventory counting transaction. Field name: DocNum.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data. The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: Specifies the path and file name of the XML data. The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The XML from which to retrieve the object's data. The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# InventoryCountingParamsCollection (Collection)

A collection of InventoryCountingParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As InventoryCountingParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As InventoryCountingParams` Returns the object at the specified index.
  - param `vtIndex`: Specifies the index of the object. The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The XML from which to retrieve the object's data. The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# InventoryCountingSerialNumber (Object)

InventoryCountingSerialNumber is a child object of the InventoryCountingLine object and enables you to count inventory by serial number. Source table: SRNT1.

## Properties (19)
- `Public Property BaseLineNumber() As Long` [R/W] The base sub line number. Field name: DocLineNum.
- `Public Property BatchID() As String` [R/W] The batch number.
- `Public Property CounterID() As Long` [R/W] The ID of the counter. Field name: CounterId.
- `Public Property CounterType() As CounterTypeEnum` [R/W] The type of the counter. Field name: CounteType.
- `Public Property DocumentEntry() As Long` [R] The internal key of the inventory counting. Field name: DocEntry.
- `Public Property ExpiryDate() As Date` [R/W] The expiry date of the serial number. Field name: ExpDate.
- `Public Property InternalSerialNumber() As String` [R/W] The internal serial number.
- `Public Property Location() As String` [R/W] The location of the item in the warehouse. Field name: Location. Length: 100 characters.
- `Public Property ManufactureDate() As Date` [R/W] The date on which the item was manufactured. Field name: MnfDate.
- `Public Property ManufacturerSerialNumber() As String` [R/W] The manufacturer serial number. Field name: MnfSerial. Length: 36 characters.
- `Public Property MultipleCounterRole() As MultipleCounterRoleEnum` [R/W] The role of the multiple counters, that is, the multiple counters conduct the inventory counting individually or as a team. Field name: CounteRole.
- `Public Property Notes() As String` [R/W] Specify any free text regarding serial numbers. Field name: Notes. Length: 16 characters.
- `Public Property Quantity() As Double` [R/W] The total number of serial numbers for the item. Field name: Quantity.
- `Public Property ReceptionDate() As Date` [R/W] The creation date of the serial number. Field name: InDate.
- `Public Property SystemSerialNumber() As Long` [R/W] The system serial number.
- `Public Property TrackingNote() As Long` [R/W] property TrackingNote
- `Public Property TrackingNoteLine() As Long` [R/W] property TrackingNoteLine
- `Public Property WarrantyEnd() As Date` [R/W] The end of the warranty dates for the serial numbers, if a manufacturer warranty exists. Field name: GrntExp.
- `Public Property WarrantyStart() As Date` [R/W] The start of the warranty dates for the serial numbers, if a manufacturer warranty exists. Field name: GrntStart.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: Specifies the path and file name of the XML data. The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The XML from which to retrieve the object's data. The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# InventoryCountingSerialNumbers (Collection)

A collection of InventoryCountingSerialNumber objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As InventoryCountingSerialNumber` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As InventoryCountingSerialNumber` Returns the object at the specified index.
  - param `vtIndex`: Specifies the index of the object.
- `Public Sub Remove(ByVal vtIndex As Variant)` Removes the object at the specified index.
  - param `vtIndex`: The index of the object to be removed.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The XML from which to retrieve the object's data.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# InventoryCountingsService (Object)

The InventoryCountingsService service enables you to add, look up, update, and close inventory counting transactions. Source table: OINC.

**Remarks:** To open the Inventory Counting window, from the SAP Business One Main Menu, choose Inventory --> Inventory Transactions --> Inventory Counting Transactions --> Inventory Counting.

## Methods (8)
- `Public Function Add(ByVal pIInventoryCounting As InventoryCounting) As InventoryCountingParams` Adds an inventory counting transaction.
  - param `pIInventoryCounting`: The data for the new inventory counting transaction.
- `Public Sub Close(ByVal pIInventoryCountingParams As InventoryCountingParams)` Closes an existing inventory counting transaction.
  - param `pIInventoryCountingParams`: The key of the inventory counting transaction to be closed.
- `Public Function Get(ByVal pIInventoryCountingParams As InventoryCountingParams) As InventoryCounting` Retrieves an inventory counting transaction. The inventory counting transaction is specified by its key, which is contained in the InventoryCountingParams object passed to the method.
  - param `pIInventoryCountingParams`: The key of the inventory counting transaction to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As InventoryCountingsServiceDataInterfaces) As Object` Creates an empty data structure for use with the InventoryCountingsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `InventoryCountingsServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object. The path and name of the XML file with which to create the object.
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
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` The XML with which to create the object.
  - param `bstrXMLString`: The XML with which to create the object.
- `Public Function GetList() As InventoryCountingParamsCollection` Returns the InventoryCountingParamsCollection data collection that identifies all inventory counting transactions.
- `Public Sub Update(ByVal pIInventoryCounting As InventoryCounting)` Updates an existing inventory counting transaction.
  - param `pIInventoryCounting`: The data for the inventory counting transaction to be updated. The InventoryCounting object must contain the key of the object to be updated.

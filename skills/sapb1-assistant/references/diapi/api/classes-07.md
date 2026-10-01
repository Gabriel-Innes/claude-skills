<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# CESTCodeService (Object)

The CESTCodeService service enables you to add, look up, update and remove CEST code data. Source table: OCEST.

**Remarks:** From the SAP Business One Main Menu, choose Inventory -> Item Master Data. On the General tab, define a new CEST code.

## Methods (7)
- `Public Function Add(ByVal pICESTCodeData As CESTCodeData) As CESTCodeParams` Adds a CEST code.
  - param `pICESTCodeData`: The data for the new CEST code.
- `Public Sub Delete(ByVal pICESTCodeParams As CESTCodeParams)` Deletes an existing CEST code.
  - param `pICESTCodeParams`: The key of the CEST code to be deleted.
- `Public Function GetByParams(ByVal pICESTCodeParams As CESTCodeParams) As CESTCodeData` Retrieves a CEST code. The CEST code is specified by its key, which is contained in the CESTCodeParams object passed to the method.
  - param `pICESTCodeParams`: The key of the CEST code to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As CESTCodeServiceDataInterfaces) As Object` Creates an empty data structure for use with the CESTCodeService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `CESTCodeServiceDataInterfaces` in `../enums/enums-02.md`
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
- `Public Sub Update(ByVal pICESTCodeData As CESTCodeData)` Updates an existing CEST code.
  - param `pICESTCodeData`: The data for the CEST code to be updated. The CESTCodeData object must contain the key of the object to be updated.

# ChangeLogDifferenceParams (Object)

Holds the detailed change information about the selected instances.

## Properties (7)
- `Public Property ArrayOffset() As Long` [R] The array table in which the changed data is located. Field name: OffSet.
- `Public Property ChangedField() As String` [R] The field that was changed. Field name: FieldName.
- `Public Property Date() As Date` [R] The date on which the change was made. Field name: UpdateDate.
- `Public Property LineNumber() As String` [R] The document line to which you have made changes. Field name: LineNum.
- `Public Property NewValue() As String` [R] Value of the field after the change. Field name: NewValue.
- `Public Property OldValue() As String` [R] Value of the field before the change. Field name: OldValue.
- `Public Property UserName() As String` [R] The name of the user who made this change. Field name: UserName.

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

# ChangeLogDifferencesParams (Collection)

A collection of ChangeLogDifferencesParam objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ChangeLogDifferenceParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ChangeLogDifferenceParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ChangeLogParams (Object)

Holds the detailed log information of an object.

## Properties (4)
- `Public Property LogInstance() As Long` [R] The sequential number of the change made. 1 is assigned to the first change, 2 is assigned to the second change, and so on. Field name: Instance.
- `Public Property ObjectCode() As String` [R] The unique code of the object that is changed. Field name: ObjectCode.
- `Public Property UpdatedDate() As Date` [R] The date on which the object was updated. Field name: UpdateDate.
- `Public Property UserName() As String` [R] The name of the user who updated the object. Field name: UserName.

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

# ChangeLogsParams (Collection)

A collection of ChangeLogParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ChangeLogParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ChangeLogParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ChangeLogsService (Object)

You can use the change log to gain an overview of changes in most windows of SAP Business One. Each time you update, for example, tax groups, withholding tax, house banks, freight, credit card, authorizations, sales, purchasing documents, production orders, charts of accounts, or UDOs, you can use the ChangeLogsService service to look up the change logs and show the differences between two change logs. Source table: OGCL.

**Remarks:** To access the change log in the SAP Business One application, open a window and make changes, if necessary; then (with the window still open) choose Tools --> Change Log.... To display the differences between two change log instances, select the instances and choose the Show Differences button.

**Example:**
- C# example (from SAP's help):
  ```csharp
  // This sample shows how to use the change log service
  // We will get the change log of business partner with BP Code "BPID01"
  // We will show the differences between 2 ChangeLog instances
  ChangeLogsService cl = (ChangeLogsService)vCompSvr.GetBusinessService(SAPbobsCOM.ServiceTypes.ChangeLogsService);
  GetChangeLogParams GetChLgParam = (GetChangeLogParams)cl.GetDataInterface(ChangeLogsServiceDataInterfaces.clsGetChangeLogParams);
  ChangeLogsParams ChLgParams;

  GetChLgParam.Object = BoChangeLogEnum.clCards; //BusinessPartners
  GetChLgParam.PrimaryKey = "BPID01"; // Card Code

  // Get Change Log
  ChLgParams = cl.GetChangeLog(GetChLgParam);

  // Show the first 2 changes
  // Change Instance 1
  MessageBox.Show("Instance 1: " + ChLgParams.Item(0).LogInstance +
      ", Object Code: " + ChLgParams.Item(0).ObjectCode +
      ", Update Date: " + ChLgParams.Item(0).UpdatedDate +
      ", User Name: " + ChLgParams.Item(0).UserName);

  // Change Instance 2
  MessageBox.Show("Instance 2: " + ChLgParams.Item(1).LogInstance +
      ", Object Code: " + ChLgParams.Item(1).ObjectCode +
      ", Update Date: " + ChLgParams.Item(1).UpdatedDate +
      ", User Name: " + ChLgParams.Item(1).UserName);

  // Show the differences between the instances

  ShowDifferenceParams param = (ShowDifferenceParams)cl.GetDataInterface(ChangeLogsServiceDataInterfaces.clsShowDifferenceParams);

  param.Object = BoChangeLogEnum.clCards; // BusinessPartners
  param.PrimaryKey = "BPID01"; // Card Code

  // We will get the differences of these 2 instances
  param.LogInstance = 1;
  param.LogInstance2 = 2;

  ChangeLogDifferencesParams retparams = null;
  // Get differences
  retparams = cl.GetChangeLogDifferences(param);

  // Show the differences
  for (int i = 0; i < retparams.Count; i++)
  {
      MessageBox.Show("User Name: " + retparams.Item(i).UserName +
      ", Date: " + retparams.Item(i).Date +
      ", Changed Field: " + retparams.Item(i).ChangedField +
      ", New Value: " + retparams.Item(i).NewValue +
      ", Old Value: " + retparams.Item(i).OldValue +
      ", Line Number: " + retparams.Item(i).LineNumber +
      ", Array Offset: " + retparams.Item(i).ArrayOffset);
  }
  ```

## Methods (5)
- `Public Function GetChangeLog(ByVal pIGetChangeLogParams As GetChangeLogParams) As ChangeLogsParams` Retrieves a change log. The change log is specified by its key, which is contained in the GetChangeLogParams object passed to the method.
  - param `pIGetChangeLogParams`: The key of the change log to retrieve.
- `Public Function GetChangeLogDifferences(ByVal pIShowDifferenceParams As ShowDifferenceParams) As ChangeLogDifferencesParams` Retrieves the differences between two change logs. The change log difference is specified by its key, which is contained in the ShowDifferenceParams object passed to the method.
  - param `pIShowDifferenceParams`: The key of the change log differences to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As ChangeLogsServiceDataInterfaces) As Object` Creates an empty data structure for use with the ChangeLogsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ChangeLogsServiceDataInterfaces` in `../enums/enums-02.md`
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

# ChartOfAccounts (Object)

ChartOfAccounts is a business object that represents the General Ledger (G/L) accounts in the Finance module. This object enables you to: - Add a G/L account. - Retrieve a G/L account by its key. - Update a G/L account. - Remove a G/L account. - Save the object in XML format. Source table: OACT.

**Remarks:** The Chart of Accounts is an index of all G/L accounts that are used by one or more companies. For every G/L account there is an account number, an account description, and information that determines the function of the account. You have to assign a Chart of Accounts to every company. This Chart of Accounts becomes operative after you carry out posting for these businesses in your daily business. After choosing the most suitable Chart of Accounts, you can customize your choice by adding, adjusting, and changing. However, once posting were made to Chart of Accounts you cannot delete it. Mandatory fields in SAP Business One: Code or FormatCode (when working with account segmentation), and FatherAccountKey. To display the form in the application: - Select Financials --> Chart of Accounts (or Edit Chart of Accounts).

## Properties (78)
- `Public Property AccountLevel() As Long` [R] Returns the level of the account. Field name: Levels.
  - remarks: Level 1 is the drawer level. Levels 2 to 4 are for either titles or accounts. Only an active account can be defined in level 5.
- `Public Property AccountPurposeCode() As SPEDContabilAccountPurposeCode` [R/W] property AccountPurposeCode
- `Public Property AccountType() As BoAccountTypes` [R/W] Sets or returns a valid value of BoAccountTypes that specifies the account type (revenues, expenses, or other) for active accounts only. Field name: ActType.
- `Public Property AcctCurrency() As String` [R/W] Sets or returns the currency in which all the journal entries for that account are recorded. Field name: ActCurr. Length: 3 characters.
  - remarks: In case a journal entry is not connected to the current account, you can update this property to multi-currency only (value ##). In case a journal entry is connected to the current account, you cannot update this property (if you try to update this property, SAP Business One generates an error).
- `Public Property ActiveAccount() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether the account is an active account or just a title. title is used to organize and display data in financial reports, and can summarize several active accounts or several active accounts and titles together. Field name: Postable.
  - remarks: Set tYES for active account. Set tNO for title. You can set up to two levels of titles. The third level must be an active account.
- `Public Property AllowChangeVatGroup() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to allow change of the VAT group. Field name: VatChange.
- `Public Property AllowMultipleLinking() As BoYesNoEnum` [R/W] Specify whether to link this account more than once within the same financial template. Field: MultiLink.
- `Public Property Balance() As Double` [R] Returns the account balance in local currency. Field name: CurrTotal.
  - remarks: The account balance is calculated after recording journal entries. The account balance is displayed in the currency defined for the account (local currency or any foreign currency).
- `Public Property Balance_FrgnCurr() As Double` [R] Returns the account balance in foreign currency. Field name: FcTotal.
- `Public Property Balance_syscurr() As Double` [R] Returns the account balance in system currency. Field name: SysTotal).
- `Public Property BlockManualPosting() As BoYesNoEnum` [R/W] property BlockManualPosting
- `Public Property BPLID() As Long` [R/W] property BPLID
- `Public Property BPLName() As String` [R] property BPLName
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property BudgetAccount() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the account (active account only) is relevant to budget management.
- `Public Property CashAccount() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether the account is a monetary account or indexed account. Field name: CashBox.
  - remarks: Relevant to active accounts only and can be added only to the first two drawers in Chart of Accounts: Assets and Liabilities.
- `Public Property CashFlowRelevant() As BoYesNoEnum` [R/W] property CashFlowRelevant
- `Public Property Category() As Long` [R/W] Sets or returns this chart of account category. Field name: category. This is a foreign key to the OACG object.
- `Public Property Code() As String` [R/W] Sets or returns the G/L account code. Field name: AcctCode. Mandatory field in SAP Business One when not working with segmentation. Length: 15 characters.
- `Public Property CostAccountingOnly() As BoYesNoEnum` [R/W] property CostAccountingOnly
- `Public Property CostElementCode() As String` [R/W] property CostElementCode
- `Public Property CostElementRelevant() As BoYesNoEnum` [R/W] property CostElementRelevant
- `Public Property DataExportCode() As String` [R/W] Sets or returns an alternate code for identifying the account in data that is exported to other programs. Field name: ExportCode. Length: 10 characters.
- `Public Property DatevAccount() As String` [R/W] Property DatevAccount
- `Public Property DatevAutoAccount() As BoYesNoEnum` [R/W] Property DatevAutoAccount
- `Public Property DatevFirstDataEntry() As BoYesNoEnum` [R/W] Property DatevFirstDataEntry
- `Public Property DefaultVatGroup() As String` [R/W] Sets or returns the default VAT group. Field name: DfltVat. Length: 8 characters. This is a foreign key to the VatGroups object.
  - remarks: The VAT groups are defined in SAP Business One and stored in the OVTG table, which is not exposed by the DI API. Country-specific for Europe. Source code !UNRECOGNISED ELEMENT TYPE 'sourcecode'! " -->Example!UNRECOGNISED ELEMENT TYPE 'filtereditemlist'!" -->See Also !UNRECOGNISED ELEMENT TYPE 'filtereditemlist'! " -->
- `Public Property Details() As String` [R/W] Sets or returns details about the account. Field name: Details. Length: 254 characters.
- `Public Property DistributionRule2Relevant() As BoYesNoEnum` [R/W] Specify whether the G/L account is relevant to the distribution rules of corresponding dimensions. Field: Dim2Relvnt.
  - remarks: To use multiple distribution rules, from the SAP Business One Main Menu, choose Administration --> System Initialization --> General Settings, and on the Cost Accounting tab, select the Use Multidimensions checkbox.
- `Public Property DistributionRule3Relevant() As BoYesNoEnum` [R/W] Specify whether the G/L account is relevant to the distribution rules of corresponding dimensions. Field: Dim3Relvnt.
  - remarks: To use multiple distribution rules, from the SAP Business One Main Menu, choose Administration --> System Initialization --> General Settings, and on the Cost Accounting tab, select the Use Multidimensions checkbox.
- `Public Property DistributionRule4Relevant() As BoYesNoEnum` [R/W] Specify whether the G/L account is relevant to the distribution rules of corresponding dimensions. Field: Dim4Relvnt.
  - remarks: To use multiple distribution rules, from the SAP Business One Main Menu, choose Administration --> System Initialization --> General Settings, and on the Cost Accounting tab, select the Use Multidimensions checkbox.
- `Public Property DistributionRule5Relevant() As BoYesNoEnum` [R/W] Specify whether the G/L account is relevant to the distribution rules of corresponding dimensions. Field: Dim5Relvnt.
  - remarks: To use multiple distribution rules, from the SAP Business One Main Menu, choose Administration --> System Initialization --> General Settings, and on the Cost Accounting tab, select the Use Multidimensions checkbox.
- `Public Property DistributionRuleRelevant() As BoYesNoEnum` [R/W] Specify whether the G/L account is relevant to the distribution rules of corresponding dimensions. Field: Dim1Relvnt.
  - remarks: Distribution rule fields are for G/L accounts of Sales or Expenditure type only.
- `Public Property ExpenseClassificationCategory() As Long` [R/W] property ExpenseClassificationCategory
- `Public Property ExpenseClassificationType() As Long` [R/W] property ExpenseClassificationType
- `Public Property ExternalCode() As String` [R/W] Sets or returns an additional code that is used for information only. The external code allows you to refine queries when generating customized reports. Field name: AccntntCod. Length: 12 characters.
- `Public Property ExternalReconNo() As Long` [R] Returns the external reconciliation number. Field name: ExtrMatch.
  - remarks: SAP Business One provides this number when comparing business accounts with external data such as bank statements.
- `Public Property FatherAccountKey() As String` [R/W] Sets or returns the parent account key that is used to define the G/L account location in drawer. Field name: FatherNum. Mandatory property. Length: 15 characters.
- `Public Property ForeignName() As String` [R/W] Sets or returns an alternative account name (for example in foreign language). Field name: FrgnName. Length: 100 characters.
- `Public Property FormatCode() As String` [R/W] Sets or returns the account number when account segmentation is defined in SAP Business One. Field name: FormatCode. Length: 210 characters. Mandatory field in SAP Business One when working with account segmentation
  - remarks: Retrieving an account that operates with account segmentation When working with segmentation, SAP Business One ignores the account Code and uses only the FormatCode that its value represents the account number in Chart Of Accounts. To retrieve an account that operates with account segmentation: 1. Find the account key using the method GetObjectKeyBySingleValue. 2. Use the returned Recordset to retrieve the value of the key (for example, _SYS00000000010). 3. Call the method GetByKey with this value (for example, _SYS00000000010) to retrieve the account. FormatCode Structure The FormatCode can include up to 10 segments. The default account segmentation format in US databases includes four segments as follows: - Natural account - 8 numbers (for example: 11100000) - Division - 2 numbers (for example: 01) - Region - 3 numbers (for example: 001) - Department - 2 numbers (for example: 03) The complete FormatCode is in the example listed above is: 11100000-01-001-03.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim sStr As String

        Dim vRs As SAPbobsCOM.Recordset

        Dim vBOB As SAPbobsCOM.SBObob

        Dim vCH As SAPbobsCOM.ChartOfAccounts

        Set vCH = Vcmp.GetBusinessObject(oChartOfAccounts)

        Set vBOB = Vcmp.GetBusinessObject(BoBridge)

        Set vRs = Vcmp.GetBusinessObject(BoRecordset)

        Set vRs = vBOB.GetObjectKeyBySingleValue(oBusinessPartners, "CardName", "aaa", bqc_Equal)

        ' When working with segmentation use this function

        ' to find the account key in the ChartOfAccount object

        Set vRs = vBOB.GetObjectKeyBySingleValue(oChartOfAccounts, "FormatCode", "125100000100101", bqc_Equal)

        'The Recordset retrieves the value of the key (for example,  sStr = _SYS00000000010).

        sStr = vRs.Fields.Item(0).Value

        'Call the method GetByKey with this value (for example, sStr =_SYS00000000010) to 'retrieve the account

        vCH.GetByKey (sStr)
    ```
- `Public Property FrozenFor() As BoYesNoEnum` [R/W] property FrozenFor
- `Public Property FrozenFrom() As Date` [R/W] property FrozenFrom
- `Public Property FrozenRemarks() As String` [R/W] property FrozenRemarks
- `Public Property FrozenTo() As Date` [R/W] property FrozenTo
- `Public Property IncomeClassificationCategory() As Long` [R/W] property IncomeClassificationCategory
- `Public Property IncomeClassificationType() As Long` [R/W] property IncomeClassificationType
- `Public Property InternalReconNo() As Long` [R] Returns the internal reconciliation number (internal reconciliation are also known as financial statement analyses). Field name: IntrMatch.
  - remarks: SAP Business One provides this number when comparing the credit and debit sides of the accounts and adjust them according to the status of the invoices.
- `Public Property LiableForAdvances() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the account is liable for advances. Field name: Advance.
- `Public Property LoadingFactorCode() As String` [R/W] The distribution rule for dimension 1 for allocating this account to one or more profit centers. Field name: OverCode This is a foreign key to the DistributionRule object.
  - remarks: To set this field, LoadingType must be set to true.
- `Public Property LoadingFactorCode2() As String` [R/W] The distribution rule for dimension 2 for allocating this account to one or more profit centers. Field name: OverCode2 This is a foreign key to the DistributionRule object.
  - remarks: To set this field, LoadingType must be set to true.
- `Public Property LoadingFactorCode3() As String` [R/W] The distribution rule for dimension 3 for allocating this account to one or more profit centers. Field name: OverCode3 This is a foreign key to the DistributionRule object.
  - remarks: To set this field, LoadingType must be set to true.
- `Public Property LoadingFactorCode4() As String` [R/W] The distribution rule for dimension 4 for allocating this account to one or more profit centers. Field name: OverCode4 This is a foreign key to the DistributionRule object.
  - remarks: To set this field, LoadingType must be set to true.
- `Public Property LoadingFactorCode5() As String` [R/W] The distribution rule for dimension 5 for allocating this account to one or more profit centers. Field name: OverCode5 This is a foreign key to the DistributionRule object.
  - remarks: To set this field, LoadingType must be set to true.
- `Public Property LoadingType() As BoYesNoEnum` [R/W] Indicates whether the chart of accounts is associated with distribution rules, which are defined in the LoadFactorCode properties. Field name: OverType
- `Public Property LockManualTransaction() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the account (active account only) can be added to the first two drawers in Chart of Accounts: Assets and Liabilities. Field name: LocManTran.
- `Public Property Name() As String` [R/W] Sets or returns the account name. Field name: AcctName. Length: 100 characters.
- `Public Property PCN874ReportRelevant() As BoYesNoEnum` [R/W] property PCN874ReportRelevant
- `Public Property PlanningLevel() As String` [R/W] The planning level that reflects the typical financial transactions and explains the origin of the data. Field name: PlngLevel. Length: 2 characters.
  - remarks: The property is for SAP Business One integration for SAP NetWeaver - Subsidiary Integration.
- `Public Property PrimaryAccount() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not the account is a primary account (fixed). Field name: Fixed.
- `Public Property PrimaryClosingAccount() As String` [R/W] property PrimaryClosingAccount
- `Public Property ProjectCode() As String` [R/W] Sets or returns the project code related to the account. Field name: Project. Length: 8 characters. This is a foreign key to the Countries table OPRJ (not exposed through the DI API).
  - remarks: In SAP Business One, you can relate business transactions to projects. This can help you to create cost/income analyzes reports based on projects.
- `Public Property ProjectRelevant() As BoYesNoEnum` [R/W] Specify whether the G/L account is relevant to a project. Field: PrjRelvnt.
- `Public Property Protected() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the account is confidential. Field name: Protected.
  - remarks: Confidential accounts are protected so that unauthorized users cannot view or update these accounts.
- `Public Property RateConversion() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include the account (active account only) in the calculation of conversion rate differences. Field name: RateTrans.
  - remarks: Relevant to companies where the currency defined in the system is different than the local currency.
- `Public Property ReconciledAccount() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the account is a reconciliation account. Field name: RealAcct.
  - remarks: Reconciliation accounts, such as tax accounts and goods receipt clearing accounts, cannot be posted manually. The total balance of the customers/vendors must be equal to the control accounts receivables/payables. Manual posting would lead to inconsistencies in the balance sheet/trial balance.
- `Public Property ReferentialAccountCode() As String` [R/W] property ReferentialAccountCode
- `Public Property RevaluationCoordinated() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the account is coordinated with revaluation. Field name: RevalMatch.
  - remarks: This property is relevant for companies where the defined currency is other than the local currency. Set to tYES, to adjust the balance of the account in the system currency to the balance in the account currency.
- `Public Property StandardAccountCode() As String` [R/W] property StandardAccountCode
- `Public Property TaxExemptAccount() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the account is VAT exempted. Field name: ExmIncome.
- `Public Property TaxLiableAccount() As BoYesNoEnum` [R/W] Field name: . Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the account is liable to VAT. Field name: .
- `Public Property TaxonomyCode() As String` [R/W] property TaxonomyCode
- `Public Property TransactionCode() As String` [R/W] Sets or returns this ChartOfAccount transaction code. Field name: TransCode. Length: 4 characters. This is a foreign key to the OTRC object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property ValidFor() As BoYesNoEnum` [R/W] property ValidFor
- `Public Property ValidFrom() As Date` [R/W] property ValidFrom
- `Public Property ValidRemarks() As String` [R/W] property ValidRemarks
- `Public Property ValidTo() As Date` [R/W] property ValidTo
- `Public Property VATRegNum() As String` [R] property VATRegNum

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal AccountCode As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `AccountCode`: Specifies the account code (see Code property).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Not supported.
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

# CheckLine (Object)

Represents the deposits for received checks. Source table: OCHH.

## Properties (15)
- `Public Property AccountNumber() As String` [R] The account number for which the check was created. Field name: AcctNum.
- `Public Property Bank() As String` [R] The house bank code of the deposit. Field name: BankCode.
- `Public Property Branch() As String` [R] The house bank branch of the deposit. Field name: Branch.
- `Public Property CashCheck() As String` [R] The check with due date earlier than or the same as the date entered in the Considered Until field. Field name: CashCheck.
- `Public Property CheckAmount() As Double` [R] The total amount of the check. Field name: CheckSum.
- `Public Property CheckCurrency() As String` [R] The currency of the check. Field name: Currency.
- `Public Property CheckDate() As Date` [R] The date of the check. Field name: CheckDate.
- `Public Property CheckKey() As Long` [R/W] The key of the check. Field name: CheckKey.
- `Public Property CheckNumber() As Long` [R] The check number for printed checks. If the check is not printed yet this field displays 0 (=zero). Field name: CheckNum.
- `Public Property Customer() As String` [R] The code of the customer. Field name: CardCode.
- `Public Property Deposited() As BoDepositCheckEnum` [R] The deposit status of the check. Field name: Deposited.
- `Public Property FiscalID() As String` [R] property FiscalID
- `Public Property OriginallyIssuedBy() As String` [R] property OriginallyIssuedBy
- `Public Property RejectedByBank() As BoYesNoEnum` [R] property RejectedByBank
- `Public Property Transferred() As BoYesNoEnum` [R] Indicates whether the deposit of the check is transferred to the next year or not. Field name: Transfered.

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

# CheckLineParams (Object)

Holds the key of a received check. This object is used to pass keys to and retrieve keys from CheckLinesService methods.

## Properties (1)
- `Public Property CheckKey() As Long` [R/W] The key of the check. Field name: CheckKey.

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

# CheckLines (Collection)

A data collection of CheckLine objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As CheckLine` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As CheckLine` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# CheckLinesParams (Collection)

A data collection of CheckLineParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As CheckLineParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As CheckLineParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# CheckLinesService (Object)

The CheckLinesService service enables you to get deposits for received checks. Source table: OCHH.

**Remarks:** To view details on a deposited check, from SAP Business One, choose Banking --> Deposits --> Deposit --> Check.

## Methods (5)
- `Public Function GetCheckLine(ByVal pICheckLineParams As CheckLineParams) As CheckLine` Retrieves a deposit for a received check. The check is specified by its key, which is contained in the CheckLineParams object passed to the method.
  - param `pICheckLineParams`: The key of the check to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As CheckLinesServiceDataInterfaces) As Object` Creates an empty data structure for use with the CheckLinesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `CheckLinesServiceDataInterfaces` in `../enums/enums-02.md`
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
- `Public Function GetValidCheckLineList() As CheckLinesParams` Returns the CheckLinesParams data collection that identify all deposits of checks.

# ChecksforPayment (Object)

Represents checks that are not tied to a document. SAP Business One updates the balances of vendor accounts each time you add a check for payment. This object is part of the Banking module. Checks tied to documents are represented by the Payments_Checks object. This object enables you to: - Add checks for payment. - Retrieve a check details by its key. - Update checks for payment. - Save the object in XML format. Source table: OCHO.

**Remarks:** Mandatory fields in SAP Business One: BankCode, CustomerAccountCode, CountryCode, and RowTotal (from ChecksforPaymentLines object). To display the form in the application: - Select Banking --> Outgoing Payments --> Checks for Payment.

## Properties (44)
- `Public Property AccountNumber() As String` [R/W] Sets or returns the bank account number of the check for payment. Field name: AcctNum. Length: 50 characters.
- `Public Property Address() As String` [R/W] Sets or returns the mailing address of the vendor. Field name: Address. Length: 254 characters.
- `Public Property AddressName() As String` [R/W] Sets or returns the name of the address (Bill To address, Main address, Ship To address, and so on). Field name: AddrName. Length: 50 characters.
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property BankCode() As String` [R/W] Sets or returns the bank code of the check. Field name: BankNum. Mandatory property. Length: 30 characters.
- `Public Property BankName() As String` [R] Returns the bank name of the payment check. Field name: BankName. Length: 15 characters.
- `Public Property Branch() As String` [R/W] Sets or returns the branch number of the payment check. Field name: Branch. Length: 50 characters.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Canceled() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not the check is canceled. Field name: Canceled.
- `Public Property CardOrAccount() As BoCpCardAcct` [R/W] Sets or returns a valid value of BoCpCardAcct type that specifies whether the payment check is to a vendor card or to a G/L account. Field name: CardOrAcct.
  - remarks: If Card, then you must set the value for the vendor code. If Account, then you must set the value for the account. SAP Business One validates the vendor code or the account.
- `Public Property CheckAmount() As Double` [R] Returns the total amount of the check. This number must be positive. Field name: CheckSum.
- `Public Property CheckCurrency() As String` [R] Returns the currency of the check. SAP Business One performs a validation check. Length: 3 characters. Field name: Currency.
- `Public Property CheckDate() As Date` [R/W] Sets or returns the due date for the check. Field name: CheckDate.
  - remarks: This date is also the value date, if a posting is created in accounting when the transaction is carried out. If you do not set the CheckDate property, the system sets the current date.
- `Public Property CheckKey() As Long` [R] Returns the sequence number of the check for payment. Field name: CheckKey. This number is assigned by SAP Business One automatically.
- `Public Property CheckNumber() As Long` [R/W] Sets or returns the check number for payment. Field name: CheckNum.
- `Public Property CountryCode() As String` [R/W] Sets or returns the country code of the bank. Field name: CountryCod. Mandatory property. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
- `Public Property CreateJournalEntry() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to create a journal entry when adding the current check. Field name: CreateJdt.
- `Public Property CreationDate() As Date` [R] Returns the date of creation of the check. Field name: CreateDate.
  - remarks: This property is internal in SAP Business One.
- `Public Property CustomerAccountCode() As String` [R/W] Sets or returns the credited G/L account code. Field name: CheckAcct. Mandatory property. Length: 210 characters.
  - remarks: SAP Business One validates this property with G/L account details.
- `Public Property DeductionRefundAmount() As Double` [R/W] Sets or returns the deduction refund amount. Field name: Deduction.
- `Public Property Details() As String` [R/W] Sets or returns the journal remarks of the check for payment. Field name: Details. Length: 50 characters.
  - remarks: SAP Business One automatically generates a remark that is copied to the accounting document. You can change or delete this text if necessary.
- `Public Property DocumentReferences() As ChecksforPaymentDocumentReferences` [R] Returns an instance of the document references of checks for payment.
- `Public Property ECheck() As BoYesNoEnum` [R/W] Specifies whether the account is relevant for e-check functionality or not. Field name: ECheck.
- `Public Property JournalEntryReference() As String` [R/W] Sets or returns the reference number for a payment to a vendor (outgoing payment) that is already created in SAP Business One. If the reference number does not exist, SAP Business One sets the transaction key. Field name: TransRef.
- `Public Property Lines() As ChecksforPaymentLines` [R] Returns ChecksforPaymentLines child object.
- `Public Property ManualCheck() As BoYesNoEnum` [R/W] Sets or returns a valid value that specifies whether or not to set the check number manually. Used in case the check is not printed through SAP Business One, but written manually. Relevant for outgoing payments only.
- `Public Property PaymentDate() As Date` [R/W] Sets or returns the posting date. If you do not set this date, SAP Business One sets the current date as the posting date for the transaction. Field name: PmntDate.
- `Public Property PaymentNo() As Long` [R] Returns the payment number of the check. Field name: PmntNum.
- `Public Property PrintConfirm() As BoYesNoEnum` [R/W] Confirms whether a check is printed or not. Field name: PrnConfrm.
- `Public Property Printed() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the check was printed. Field name: Printed.
- `Public Property PrintedBy() As Long` [R] Returns the ID of the user that prints the check. Field name: PrintedBy.
- `Public Property PrintStatus() As ChecksforPaymentPrintStatus` [R] The column Print Status in the Check Number Confirmation window.
- `Public Property Signature() As String` [R/W] Sets or returns the authorizing signature, such as the name of the responsible person, for approving the payment. Field name: Signature. Length: 30 characters.
- `Public Property TaxDate() As Date` [R] Returns the date for the tax payment. Field name: TaxDate.
- `Public Property TaxTotal() As Double` [R] Returns the total tax, such as VAT, added to the payment. Field name: VatTotal.
  - remarks: SAP Business One calculates the tax according to the tax group defined using the Document_LinesAdditionalExpenses object (source table: DRF3).
- `Public Property TotalinWords() As String` [R/W] Sets or returns the total amount is words. SAP Business One enters this value automatically according to the CheckAmount. Field name: TotalWords. Length: 100 characters.
- `Public Property TransactionNumber() As Long` [R] Returns the transaction code that SAP Business One creates for the payment check. Field name: TransNum.
- `Public Property Transferable() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the check can be endorsed. If the value is set to No (not endorsable), SAP Business One includes the text "Non-negotiable" in the printout. Field name: Trnsfrable.
- `Public Property UpdateDate() As Date` [R] Returns the date when the check details were last updated. Field name: UpdateDate.
  - remarks: Internal property in SAP Business One.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VendorCode() As String` [R/W] Sets or returns the vendor number or G/L account for the payment. SAP Business One validates this number. Field name: VendorCode. Length: 15 characters.
- `Public Property VendorName() As String` [R] Returns the name of the vendor that appears in the "Pay to Order of" field of the check. Field name: VendorName. Length: 100 characters.
- `Public Property WithholdingTaxAmount() As Double` [R] property WithholdingTaxAmount
- `Public Property WithholdingTaxPercentage() As Double` [R/W] property WithholdingTaxPercentage

## Methods (9)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Cancel() As Long` Not supported.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal CheckKey As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `CheckKey`: Specifies the sequence number of the check for payment (see CheckKey property).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Not supported.
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

# ChecksforPaymentDocumentReferences (Object)

The document references of checks for payment. Source table: CHO3.

## Properties (9)
- `Public Property Count() As Long` [R] The count of rows. Field name: LogInstanc.
- `Public Property DocEntry() As Long` [R] The index (Primary Key). Field name: DocEntry.
- `Public Property ExternalReferencedDocNumber() As String` [R/W] External referenced document number. Field name: ExtDocNum. Length: 100 characters.
- `Public Property IssueDate() As Date` [R/W] Issue date. Field name: IssueDate.
- `Public Property LineNumber() As Long` [R] The row number (Primary Key). Field name: LineNum.
- `Public Property ReferencedDocEntry() As Long` [R/W] Referenced document internal number. Field name: RefDocEntr.
- `Public Property ReferencedDocNumber() As Long` [R] Referenced document number. Field name: RefDocNum.
- `Public Property ReferencedObjectType() As ReferencedObjectTypeEnum` [R/W] Referenced object type. Field name: RefObjType. Length: 20 characters.
- `Public Property Remark() As String` [R/W] Field name: Remark. Length: 254 characters.

## Methods (2)
- `Public Sub Add()` method Add
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 

# ChecksforPaymentLines (Object)

ChecksforPaymentLines is a child object of the ChecksforPayment object that represents the appendix of the check. Source table: CHO1.

**Remarks:** Mandatory field in SAP Business One: RowTotal. To display the form in the application: - Select Banking --> Outgoing Payments --> Checks for Payment.

## Properties (10)
- `Public Property Count() As Long` [R] Returns the total data rows of the ChecksforPaymentLines object.
- `Public Property CreditedAccount() As String` [R/W] Sets or returns the G/L account to debit. Field name: CredAcct. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
- `Public Property LineTotal() As Double` [R] Returns the total amount (including tax) per row. Field name: LinesSum.
  - remarks: SAP Business One calculates the total amount per row using the RowTotal and TaxPercent properties.
- `Public Property RowCurrency() As String` [R/W] Sets or returns the currency for the row. Field name: LineCurr. Length: 3 characters.
- `Public Property RowDetails() As String` [R/W] Sets or returns the row details. Field name: LineDitail. Length: 40 characters.
- `Public Property RowNumber() As Long` [R] Returns the current available row number (starts from 1). Field name: Line_ID.
- `Public Property RowTotal() As Double` [R/W] Sets or returns the total amount in the row. Field name: LineMoney. Mandatory property.
- `Public Property TaxDefinition() As String` [R/W] Sets or returns the tax group for the row. Field name: Code. Length: 8 characters. This is a foreign key to the VatGroups object.
- `Public Property TaxPercent() As Double` [R] Returns the tax percentage according to the tax group (TaxDefinition). Field name: VatPercent.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# ChecksforPaymentPrintStatus (Object)

Represents the print status of Checks for Payment. Source table: CHO2.

**Remarks:** To display the form in the application: Select Banking --> Outgoing Payments --> Check Number Confirmation.

**Example:**
- C# example (from SAP's help):
  ```csharp
  ChecksforPayment.PrintStatus.PrintStatus = ""V"";
  ChecksforPayment.PrintStatus.CheckNumber = ""1"";
  ChecksforPayment.PrintStatus.DocEntry = ""1"";
  ChecksforPayment.PrintStatus.LineNumber = ""1"";
  ChecksforPayment.PrintStatus.PrintedBy = 0;
  ChecksforPayment.PrintStatus.Count;
  ```

## Properties (6)
- `Public Property CheckNumber() As Long` [R/W] The check number. Field name: ChkNum.
- `Public Property Count() As Long` [R] The count of rows. Field name: LogInstanc.
- `Public Property DocEntry() As Long` [R/W] The index (Primary Key). Field name: AbsEntry.
- `Public Property LineNumber() As Long` [R/W] The row number (Primary Key). Field name: LineNum.
- `Public Property PrintedBy() As Long` [R/W] The ID of a user. Field name: PrnBy.
- `Public Property PrintStatus() As String` [R/W] The print status of checks. Field name: Status. Length: 1 characte. Values: D=Details, N=Not Confirmed, O=Overflow, T=Not Printed, V=Void.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# ChooseFromList (Object)

The ChooseFromList object enables to set the display of the Choose From List for a specified object. Source table: OCHF.

**Remarks:** Mandatory field in SAP Business One: ObjectName. For example, to display the Choose From List Settings form of business partners (object name: OCRD): - Select a document, click the Customer field and then press the Tab key. The BP List window opens. - From the main menu, select Tools --> Form Settings.

## Properties (4)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property ChooseFromList_Lines() As ChooseFromList_Lines` [R] Returns the ChooseFromList_Lines child object.
- `Public Property ObjectName() As String` [R/W] Sets or returns the table name to which the Choose from List Settings applies. For example, OCRD for business partners. Field name: ObjName. Length: 20 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a Choose from List Settings for a specified object.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal bstrObjectName As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `bstrObjectName`: ObjectName.
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

# ChooseFromList_Lines (Object)

ChooseFromList_Lines is a child object of ChooseFromList. Source table: CHFL.

## Properties (9)
- `Public Property Count() As Long` [R] Returns the total rows in the database table.
- `Public Property DisplayedName() As String` [R/W] Sets or returns name displayed in the column header. Field name: DispName. Length: 30 characters.
- `Public Property FieldNo() As String` [R/W] Sets or returns column number in the specified database table. Field name: FldNum. Length: 10 characters.
- `Public Property GroupBy() As BoYesNoEnum` [R/W] Determines whether or not to group all the rows by the specified field. Field name: GroupBy.
  - remarks: You can set up to three groups for a specified object. Set to Y - to group all the rows for the specified field. The user can expand or collapse all the records. Set to N - to display all the records.
- `Public Property ShowType() As BoYesNoEnum` [R/W] Determines whether to display the valid value description or the valid value. For example, for BP Type, set Y to display Customer or set N to display C. Field name: DispDesc.
  - remarks: Applicable only for properties that contain valid values.
- `Public Property SortOrder() As SortOrderEnum` [R/W] Sets or returns the sort order - Ascending or Descending - of the columns in the Choose from List form. Field name: SortOrder.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property Visible() As BoYesNoEnum` [R/W] Determines whether or not to display the column. Field name: Visible.
- `Public Property VisualIndex() As Long` [R/W] Sets or returns the display order number of the column. Field name: VisIndex.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# ClosingDateProcedure (Object)

The ClosingDateProcedure object enables to retrieve the closing date procedure definition. This object is applicable for cluster B (country-specific for Japan only). Source table: OCDP.

**Remarks:** To display the form in the application: - Select Administration > Definitions > Business Partners > Define Closing Date Procedure. The application logic is similar to the Payment Terms calculation for the Closing date. In addition, the Closing Date is always greater or equal to Baseline Date (posting date or system date). When Closing Date is earlier than Baseline date, the month of Closing date will be added by 1. For example, Closing Date is every 20th, when posting date is April 19, Closing Date is April 20; when posting date is April 21, Closing Date is May 20.

## Properties (8)
- `Public Property BaselineDate() As BoClosingDateProcedureBaseDateEnum` [R] Returns the reference date for executing a transaction: Posting Date or System Date. Field name: BsLineDate.
  - remarks: Default: System Date.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property ClosingDateCode() As String` [R] Returns the code of the closing date procedure. Field name: ClsDtCode. Length: 30 characters.
- `Public Property ClosingDateNum() As Long` [R] Returns the closing date procedure number. Field name: ClsDateNum.
- `Public Property DueMonth() As BoClosingDateProcedureDueMonthEnum` [R] Returns the start from date for calculating the transaction due date: begining date of the month, middle date of the month, or end date of the month. Field name: DueMonth.
- `Public Property ExtraDay() As Long` [R] Returns the number of additional days for calculating the due date. Field name: ExtraDay.
- `Public Property ExtraMonth() As Long` [R] Returns the number of additional months for calculating the due date. Field name: ExtraMonth.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (4)
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
- `Public Function GetByKey(ByVal ClosingDateNum As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ClosingDateNum`: ClosingDateNum.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data.
- `Public Sub SaveXML(ByRef FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data.

# Cockpit (Object)

Represents a cockpit, which is a personalized work center where you can view, search, organize, and perform your regular work and related activities. Source table: OCPT.

## Properties (10)
- `Public Property AbsEntry() As Long` [R] The key for the cockpit. Field name: AbsEntry.
- `Public Property CockpitType() As BoCockpitTypeEnum` [R] property CockpitType
- `Public Property Code() As Long` [R] The code of a specific cockpit. Field name: Code.
- `Public Property Date() As Date` [R] The publication date of the cockpit. Field name: Date.
- `Public Property Description() As String` [R/W] The description of the cockpit. Field name: Descr. Length: 100 characters.
- `Public Property Manufacturer() As String` [R/W] The provider of the cockpit. Field name: Mnfacturer.
- `Public Property Name() As String` [R/W] The name of the cockpit. Field name: Name. Length: 20 characters.
- `Public Property Publisher() As String` [R] The user who publishes the cockpit. Field name: Pubby.
- `Public Property Time() As Date` [R] The publication time of the cockpit. Field name: Time.
- `Public Property UserSignature() As Long` [R] Represents the user who owns the cockpit. Field name: UserSign.
  - remarks: Value -1 represents that the cockpit is published. To publish a user-created cockpit from SAP Business One: - From the menu bar, choose Tools --> Cockpit --> Cockpit Management. - In the Cockpit Management - Setup window, select the cockpit and choose the Publish button.

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

# CockpitParams (Object)

Holds the key to an existing cockpit. This object is used to pass keys to and retrieve keys from CockpitsService methods.

## Properties (2)
- `Public Property AbsEntry() As Long` [R/W] The key of a specific cockpit. Field name: AbsEntry.
- `Public Property CockpitType() As BoCockpitTypeEnum` [R] property CockpitType

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

# CockpitsParams (Collection)

A collection of CockpitParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As CockpitParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As CockpitParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# CockpitsService (Object)

The CockpitsService service enables you to add, look up, update, and remove cockpits. Source table: OCPT.

**Remarks:** Note: - If you log on to an SAP Business One company with the cockpit enabled, and you connect to the same company via DI-API, the changes you make to the cockpits via DI-API are lost after you exit the SAP Business One application. It does not affect add/delete operations, only the update operations of the existing cockpits. You can update the cockpits successfully via DI-API without running the SAP Business One application that connects to the same company database. - If you make changes via DI-API to the database tables, the GUI of the SAP Business One application does not get updated immediately. To see the changes you have made via DI-API, re-open the Cockpit Management window. To open the Cockpit Management window, from the SAP Business One menu bar, choose Tools --> Cockpit --> Cockpit Management. Changes via DI-API are also available when you log on again to the company, or restart the SAP Business One application and connect to the company.

## Methods (11)
- `Public Function AddCockpit(ByVal pICockpit As Cockpit) As CockpitParams` Adds a cockpit.
  - param `pICockpit`: The data for the new cockpit.
  - returns: Contains the key (AbsEntry) of the new cockpit.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.Cockpit cptAdd = (SAPbobsCOM.Cockpit)cockService.GetDataInterface(CockpitsServiceDataInterfaces.csCockpit);

    cptAdd.Name = "Name";
    cptAdd.Description = "Description";

    SAPbobsCOM.CockpitParams cockParamAdd = cockService.AddCockpit(cptAdd);
    ```
- `Public Sub DeleteCockpit(ByVal pICockpitParams As CockpitParams)` Deletes an existing cockpit.
  - param `pICockpitParams`: The key of the cockpit to be deleted.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.CockpitsParams cockParamsDelete = cockService.GetCockpitList();

    if (cockParamsDelete.Count > 0)
    {
          //Delete the first one.
          SAPbobsCOM.CockpitParams cockParamDelete = cockParamsDelete.Item(0);
          cockService.DeleteCockpit(cockParamDelete);
    }
    ```
- `Public Function GetCockpit(ByVal pICockpitParams As CockpitParams) As Cockpit` Retrieves a specific cockpit.
  - param `pICockpitParams`: The key of the cockpit to retrieve.
  - returns: The cockpit with the specified key.
- `Public Function GetCockpitList() As CockpitsParams` Retrieves the keys and names of all the cockpits.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.CockpitsParams cockParams = cockService.GetCockpitList();
    if (cockParams.Count > 0)
    {
         foreach (SAPbobsCOM.CockpitParams cockParam in cockParams)
         {
               SAPbobsCOM.Cockpit cpt = cockService.GetCockpit(cockParam);
         }
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As CockpitsServiceDataInterfaces) As Object` Creates an empty data structure for use with the CockpitsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `CockpitsServiceDataInterfaces` in `../enums/enums-02.md`
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
- `Public Function GetTemplateCockpitList() As CockpitsParams` GetTemplateCockpitList
- `Public Function GetUserCockpitList() As CockpitsParams` GetUserCockpitList
- `Public Sub PublishCockpit(ByVal pICockpit As Cockpit)` PublishCockpit
  - param `pICockpit`: 
- `Public Sub UpdateCockpit(ByVal pICockpit As Cockpit)` Updates an existing cockpit.
  - param `pICockpit`: The data for the cockpit to be updated. The Cockpit object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.CockpitsParams cockParamsUpdate = cockService.GetCockpitList();

    if (cockParamsUpdate.Count > 0)
    {
          //Update the first one.
          SAPbobsCOM.CockpitParams cockParamUpdate = cockParamsUpdate.Item(0);
          SAPbobsCOM.Cockpit cptUpdate = cockService.GetCockpit(cockParamUpdate);
          cptUpdate.Description = "The updated description.";

          cockService.UpdateCockpit(cptUpdate);
    }
    ```

# ColumnPreferences (Object)

ColumnPreferences is a Data structure related to the FormPreferencesService. Source table: CPRF.

**Remarks:** To display the Form Preferences settings in the application: - Select a form. - From the main menu, select Tools --> Form Settings.

## Properties (11)
- `Public Property Column() As String` [R/W] Sets or returns the column identification key. Field name: ColumnId. Mandatory property for Table fields. The default value is -1 (Title field). Length: 10 characters.
- `Public Property EditableInExpanded() As BoYesNoEnum` [R/W] Determines whether or not the item in the form can be edited in expanded display mode. Field name: EditInEXP.
- `Public Property EditableInForm() As BoYesNoEnum` [R/W] Determines whether or not the item in the form can be edited in normal display mode (that is, not expanded mode). Property type Read-write property " --> Field name: EditInForm.
- `Public Property ExpandedIndex() As Long` [R/W] Sets or returns the expanded index of this column. Field name: ExpandIndx.
- `Public Property FormID() As String` [R/W] Sets or returns the form identification key. Field name: FormID. Mandatory property. Length: 20 characters.
  - remarks: The entered value must be a valid form ID (the system does not validate the entered value). To display the form ID in the application status bar: - From the main menu, select View --> System Information.
- `Public Property ItemNumber() As String` [R/W] Sets or returns the ID of the field or the table in a form (primary key with FormID). Field name: ItemID. Mandatory property. Length: 10 characters.
  - remarks: The entered value must be a valid item ID (the system does not validate the entered value). In case the ItemID specifies a table, set also the Column, otherwise the system sets the value -1. To display the item ID in the application status bar: - From the main menu, select View --> System Information.
- `Public Property TabsLayout() As Long` [R/W] Sets or returns the display order of the item in the form. For example, set 1 to display the form item in the first column in the table (starting from left). Property type Read-write property " --> Field name: VisualIndx.
- `Public Property User() As Long` [R/W] Sets or returns the signature of the user that sets this column. Field name: UserSign. This is a foreign key to the Users object.
- `Public Property VisibleInExpanded() As BoYesNoEnum` [R/W] Determines whether or not the item in the form is visible in expanded display mode. Field name: VisInExpnd.
- `Public Property VisibleInForm() As BoYesNoEnum` [R/W] Determines whether or not the item is visible in the form in normal display mode (that is, not expanded mode). Field name: VisInForm.
- `Public Property Width() As Long` [R/W] Sets or returns the number of characters to determine the column width. Mandatory property. Field name: Width.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# ColumnsPreferences (Collection)

ColumnsPreferences is a collection of ColumnPreferences data structures.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the total items in the collection.

## Methods (5)
- `Public Function Add() As ColumnPreferences` Adds a column preferences data structure to the collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ColumnPreferences` Returns a reference to an existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the new item, which was added to the collection.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# ColumnsPreferencesParams (Object)

The ColumnsPreferencesParams specifies the identification key combination (user and FormId) for which the FormPreferencesService is related. Source table: CPRF.

**Remarks:** To display the Form Preferences settings in the application: - Select a form. - From the main menu, select Tools --> Form Settings.

## Properties (2)
- `Public Property FormID() As String` [R/W] Sets or returns the form identification key. Field name: FormID. Mandatory property. Length: 20 characters.
  - remarks: The entered value must be a valid form ID (the system does not validate the entered value). To display the form ID in the application status bar: - From the main menu, select View --> System Information.
- `Public Property User() As Long` [R/W] Sets or returns the identification key of the user to whom this form preferences applies. Mandatory property. Field name: UserSign.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data. Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data. Creates an XML string that represents the object data.

# Command (Object)

The Command object enables to run SQL stored procedures located in the company database. This object is called by the Recordset object.

## Properties (2)
- `Public Property Name() As String` [R/W] Sets or returns the name of the stored procedure.
  - remarks: After setting the Name property, the object's parameters are immediatly filled with the associated parameters of the stored procedure.
- `Public Property Parameters() As CommandParams` [R] Returns the CommandParams child object.

## Methods (1)
- `Public Sub Execute()` Executes the stored procedure with the Parameters.
  - remarks: If the stored procedure uses a SELECT statement the Recordset is filled with the returned parameters. Otherwise, the stored procedure returns an Out Parameter.

# CommandParam (Object)

CommandParam is a child object of the Command object and used to retrieve single parameter of the stored procedure.

## Properties (4)
- `Public Property Direction() As BoRecCommParamTypes` [R] Returns the direction of the parameter, In or Out. The Command object supports single Out parameter only.
- `Public Property Name() As String` [R] Returns the parameter name.
- `Public Property Type() As BoFieldTypes` [R] Returns the parameter field type.
- `Public Property Value() As Variant` [R/W] Sets or returns the parameter value.

# CommandParams (Collection)

CommandParams is a collection of CommandParam objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the total items in the collection.

## Methods (1)
- `Public Function Item(ByVal Index As Variant) As CommandParam` Retrieves a single item, of a command parameter, from the stored procedure parameters collection .
  - param `Index`: Specifies the item number (starts from 0).

# CommissionGroups (Object)

The CommissionGroups object enables to define commission groups for a sales employee, an item, or a customer. Source table: OCOG.

**Remarks:** The commission is determined when a sales document is entered and saved for all the rows in the document. The Commission Groups define the commissions that are given internally to the Sales Employees. The commissions are calculated in a report and are not posted to any accounts. To display the form in the application: - Select Administration -->Setup -->General -->Commission Groups.

## Properties (5)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CommissionGroupCode() As Long` [R] Returns the code of the commission group as assigned by the system when adding a commission group. Field name: GroupCode.
- `Public Property CommissionGroupName() As String` [R/W] Sets or returns the name of the commission group. Field name: GroupName. Length: 30 characters.
- `Public Property CommissionPercentage() As Double` [R/W] Sets or returns the commission percentage. Field name: Commission.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a commission group.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lGroupCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lGroupCode`: Item property code (Number).
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

# Company (Object)

Company is the primary DI API object that represents a single SAP Business One company database. This object enables you to connect to the company database and to create business objects to use with the company database.

**Remarks:** The Company object is the only object of the DI API that you can create directly (for example, with New in Visual Basic). You can then use the Company object to create all other DI API objects. To enable your add-on to support the side-by-side model, see Versions Compatibility.

## Properties (28)
- `Public Property AddonIdentifier() As String` [R/W] Sets or returns a string identifier that your add-on must use to connect to SAP Business One database.
  - remarks: You can generate the string identifier through SAP Business One application only (Administration > License > Add-on Identifier Generator).
- `Public Property Application(ByVal RHS As Object) As Object` [W] To connect with SAP Business One, you can set this property to a SAPbouiCOM.Application object, and then call the Connect method without specifying any other connection properties -- the properties are taken from the UI API Application object.
  - remarks: Creating a connection with this property is only relevant when an instance of the SAP Business One application on the same machine is open and connected to a company.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Private WithEvents SBO_Application As SAPbouiCOM.Application

    Dim oSboGuiApi As SAPbouiCOM.SboGuiApi

    Dim sConnectionString As String

    Dim oApplication As SAPbouiCOM.Application

    Dim oCompany As SAPbobsCOM.Company

    Dim nResult As Long

    oSboGuiApi = New SAPbouiCOM.SboGuiApi

    ' The connection string is passed to the add-on as a command line argument

    sConnectionString = Environment.GetCommandLineArgs.GetValue(1)

    ' Set an add-on identifier (this identifier is for development license)

    oSboGuiApi.AddonIdentifier = "4CC5B8A4E0213A68489E38CB4052855EE8678CD237F64D1C11C22707A54DBD2D5D5F6E4050A09B9F9FB80FAC44F6"

    ' Connect to a running SBO Application

    oSboGuiApi.Connect(sConnectionString)

    ' Get an initialized application object

    oApplication = oSboGuiApi.GetApplication()

    oCompany = New SAPbobsCOM.Company

    ' Set UI Application object to Company object

    oCompany.Application = oApplication

    ' Connect to current B1 company

    nResult = oCompany.Connect
    ```
- `Public Property AttachMentPath() As String` [R] Returns the path to all the company's saved mail attachments and all contact related files.
  - remarks: Specify the directory of the attachments such as, customer web pages.
- `Public Property BitMapPath() As String` [R] Returns the path to all the picture files of the company, which are related to the Picture property of Items object, Picture property of BusinessPartners object, and documents.
- `Public Property CompanyDB() As String` [R/W] Sets or returns the name of the company SQL database .
  - remarks: Use this property to specify the database name to which you want to connect. You must set this property before you use the Connect method to establish a connection to the database. This database must be a SAP Business One database that is compatible with the SAP Business One server database (SBO-Common).
- `Public Property CompanyName() As String` [R] Returns the company name as defined in the database.
  - remarks: After establishing a connection, this property contains the company name that is specified in the database.
- `Public Property Connected() As Boolean` [R] Returns a Boolean value that specifies whether or not the Company object is connected to the database.
  - remarks: You can use this property to check if the operation of the Connect or Disconnect methods was successful.
- `Public Property DbPassword() As String` [R/W] Sets or returns the password for establishing a connection to the database server. The field is not mandatory, as the database credentials are stored in the System Landscape Directory (SLD) server and you can use these values instead.
  - remarks: When you retrieve the value of the DbPassword field, ****** is returned. If you set a value to the DbUserName field, then that value is returned when you get a value from this field. If you connected without providing a database user name (relying on the credentials stored in the license server), then an empty string is returned.
- `Public Property DbServerType() As BoDataServerTypes` [R/W] The database type.
- `Public Property DbUserName() As String` [R/W] Sets or returns the user name for establishing a connection to the database server. The field is not mandatory, as the database credentials are stored in the System Landscape Directory (SLD) server and you can use these values instead.
  - remarks: If you set a value to the DbUserName field, then that value is returned when you get a value from this field. If you connected without providing a database user name (relying on the credentials stored in the license server), then an empty string is returned.
- `Public Property DTCTransactionObject() As Unknown` [R/W] This interface supports Distributed Transactions for MS-SQL database that are controlled by MS-DTC engine (Microsoft Distributed Transaction Coordinator). DTC is a system service that coordinates transactions so that work can be committed as an atomic transaction even if it spans multiple resource managers on multiple computers, regardless of failures. This interface is applicable for the following environment: - MS-SQL database server - C/C++ interface - ODBC connection type - DI API only (and not by DI Server)
  - remarks: Usage - Create a distributed transaction object externally to the application using the DTC interface. GetDTCInterface (&g_pTransactionDispenser); g_pTransactionDispenser-> BeginTransaction(NULL, ISOLATIONLEVEL_ISOLATED, ISOFLAG_RETAIN_DONTCARE, NULL, (::ITransaction**)&g_pTransaction); - The DI COM module receives a handle to a live transaction that is created by the MS-DTC. ICompanyPtr pCmp; pCmp->put_DTCTransactionObject (g_pTransaction); - The DI performs a validation of the transaction object by verifying its Isolation Level. After the validation succeeds, the DB module is notified that the current transaction is an outside object and managed externally. - The transaction process is performed as usual, and the change in the flow is transparent to the user. During a DTC Transaction, do not call StartTransaction() and EndTransaction(), otherwise the system returns an error. - To end the DTC transaction, assign a NULL value to the DTC Transaction handle: pCmp->put_DTCTransactionObject (NULL); - To get the current DTC handle that is set in SAP Business One, call: IUnknown* ptr = NULL; HRESULT hr = pCmp ->get_DTCTransactionObject(&ptr); - To check whether a DTC Transaction is set, call: bool isDTCSet; pCmp->IsDTCTransactionObjectSet(&isDTCSet); Notes - In case an operation fails during a DTC transaction, SAP Business One performs a rollback, which forces other systems under the same distributed transaction to rollback. - The DTC transaction scope (the Begin/End user transaction equivalent) is determined by the calls to put_DTCTransactionObject (). As long as there is a transaction object set, every operation is performed under this transaction context. It is the Client's responsibility to make sure a valid DTC transaction is assigned, and to assign NULL value when the DTC transaction ends. - StartTransaction() and EndTransaction() must not be called during a DTC Transaction. - put_DTCTransactionObject () must not be called during a live user transaction.
- `Public Property ExcelDocsPath() As String` [R] Returns the path to the Microsoft Excel documents exported from the SAP Business One application.
- `Public Property InTransaction() As Boolean` [R] Returns a Boolean value that specifies whether or not the transaction is active.
  - remarks: In case the add-on is not connected to the database, SAP Business One returns exception Not Connected (exception number: -106).
- `Public Property language() As BoSuppLangs` [R/W] Sets or returns the resource language of the object.
  - remarks: If you do not specify a language, the system automatically selects the first language that it finds. If the language you specified is not supported by SAP Business One, the Connect method will fail when trying to establish connection with the SAP Business One server.
- `Public Property LicenseServer() As String` [R/W] Deprecated in DI API 9.2 PL05. Please use SLDServer instead. The DI API will continue to support this property for backward compatibility. The license server name and port for connecting to the company database. The value is in the format myServer:30000. If no value is given, the default license server and port are used. If a server is given but no port is given, 30000 is used for the port.
  - remarks: Previously, the default license for all clients was stored in the SLIC table of the SBO-COMMON database. From release 8.8, the default license file is stored in the b1-local-machine.xml file, which is located by default in c:\Program Files\SAP\SAP Business One DI API\Conf.
- `Public Property MinimalSupportedVersion() As Long` [R] Returns the minimal version of the Company database that the Add-on supports.
  - remarks: For example, an Add-on that its minimal supported version is 6.5 can connect only to a Company database of version 6.5 and up.
- `Public Property Password() As String` [R/W] Sets or returns the SAP Business One password issued to the user.
  - remarks: The password corresponds to the user name the in SAP Business One application.
- `Public Property SecurityCode() As String` [R/W] property SecurityCode
- `Public Property Server() As String` [R/W] Sets or returns the SQL server to which the object connects.
  - remarks: Before establishing a connection with the database, you must specify the SQL server that you want to use. This server must be installed with the SBO-Common database.
- `Public Property SLDServer() As String` [R/W] Set the System Landscape Directory (SLD) server address to connect to the company database and to retrieve the real license address from the SLD server.
  - remarks: As of SAP Business One 9.2 PL05, License Servere will register its URL into the SLD Server.
- `Public Property UserName() As String` [R/W] Sets or returns the user ID, which is used for log on to the SAP Business One application.
  - remarks: This is the user name used for log on to the system (not the user name to access the database server). The UserName property must correspond to the Password property. In the SAP Business One application, a user is specific to the server (Server) and company database (CompanyDB).
- `Public Property UserSignature() As Long` [R] Returns the identification key of the active user who operates the system.
- `Public Property UserTables() As UserTables` [R] Returns the UserTables object, which is the interface to the tables defined by the user. This object allows you to access to the user tables as if they were regular business objects.
- `Public Property UseTrusted() As Boolean` [R/W] Sets or returns a Boolean value that specifies whether the Company object uses NT authentication, or the internal SQL Server user ObsCommon, to establish a connection with the SQL Server.
  - remarks: Set this property to FALSE to log on using ObsCommon. Set this property to TRUE to log on using the current NT user.
- `Public Property Version() As Long` [R] Returns the version of the Company database.
  - remarks: The version of the Company database always equals to the versions of the OBServer.dll and SBOcommon database. The version is stored in the CINF table of the Company database and also in the SINF table of the SBO Common database. The OBServer.dll can be found in the user temporary folder after connecting to the company database. To view its version, open the file properties dialog box and click the Version tab. See also Versions Compatibility.
- `Public Property WordDocsPath() As String` [R] Returns the path to the Microsoft Word documents exported from the SAP Business One application. This directory also contains Microsoft Word templates, which are used for exporting data to Word documents.
- `Public Property XMLAsString() As Boolean` [R/W] Sets or returns a Boolean value that determines whether the XML data will be saved as a file or transferred as a string.
  - remarks: The default value is False - XML as files. This setting is compatible with older versions of the DI API.
- `Public Property XmlExportType() As BoXmlExportTypes` [R/W] Sets or returns a valid value of BoXmlExportTypes that specifies the types for exporting data from the database to XML format.
  - remarks: The default setting is xet_AllNodes (0). This setting supports older DI API versions but cannot be read using the ReadXml method. To use ReadXML method later, set the XmlExportType to xet_ExportImportMode (3).

## Methods (28)
- `Public Function AuthenticateUser(ByVal bstrUserName As String, ByVal bstrPassword As String) As AuthenticateUserResultsEnum` Checks whether a pair of username and password exist and match in the current SAP Business One company . Note: this method is for superuser only.
  - param `bstrUserName`: The username to be tested.
  - param `bstrPassword`: The password to be tested.
- `Public Function ChangePassword(ByVal NewPassword As String) As Long` Changes the password of the actual user connected to SAP Business One. The system verifies whether the new password complies to the company password policy and if not, the system returns an error.
  - param `NewPassword`: Specifies the new password.
- `Public Function Connect() As Long` Connects to the SAP Business One company database.
  - returns: 0 if the method succeeds; otherwise, an error code. You can retrieve the last error code and its description with the method GetLastError.
  - remarks: Before calling this method, set proper values to the following properties: Server, CompanyDB, UserName Password, DbUserName, DbPassword, UseTrusted, and AddonIdentifier. From version 8.8, you can connect without supplying database credentials. The new security mechanism stores the database credentials in the System Landscape Directory (SLD) server. Related Tasks - To retrieve a list of company databases for a specific server, use the GetCompanyList method. - To check if the connection to the database is successful, use the Connected property.
- `Public Sub Disconnect()` Disconnects an active connection with the company database.
  - remarks: Use this method to disconnect the channel between the database and the client. Before disconnecting from the company database, you can use the Connected property to check whether or not the connection is active.
- `Public Sub EndTransaction(ByVal endType As BoWfTransOpt)` Ends a global transaction that started with the StartTransaction method.
  - param `endType`: one of the enumeration's values (see the enum file)
  - remarks: You can only use the StartTransaction and EndTransaction methods when the connection with the database is active. If an exception occurs when you call EndTransaction, the changes are not committed. To correct this: - Troubleshoot and fix the exception. - Call StartTransaction. - Resubmit the changes (by calling the Add, Update, and Delete methods). - Call EndTransaction.
  - enum: `BoWfTransOpt` in `../enums/enums-02.md`
- `Public Function GetBusinessObject(ByVal Object As BoObjectTypes) As Object` Creates a new business object.
  - param `Object`: one of the enumeration's values (see the enum file)
  - returns: The GetBusinessObject method returns the object type specified in the method's parameter. The returned object is empty and contains only the default values specified in the company database.
  - remarks: You can use this method to create business objects such as, BusinessPartners, Items, and so on. Then, to use the created object (to call methods such as, Add, Update, GetByKey, and so on) you must set the appropriate values to the object's properties (including the mandatory properties). To load an existing object from an XML file, call the GetBusinessObjectFromXML method. To release an object after using it, use the code line: Set object = Nothing
  - enum: `BoObjectTypes` in `../enums/enums-01.md`
- `Public Function GetBusinessObjectFromXML(ByVal FileName As String, ByVal Index As Long) As Object` Creates a new business object based on a valid XML file.
  - param `FileName`: Specifies the full path and file name of the XML file that contains the business object data.
  - param `Index`: Specifies the offset of the object within the file when using an XML file that contains more than one business object. Otherwise, set the value 0.
  - remarks: You can use this method to create business objects such as, BusinessPartners, Items, and so on. To create an empty object instead of an existing one from an XML file, you can use the GetBusinessObject method. To release an object after using it, use the code line: Set vbps = Nothing To obtain the number of business objects included in the XML file, use the GetXMLelementCount method. For more information and a sample, see Exchanging Data Using the DI API XML Capabilities and Loading Data from XML.
- `Public Function GetBusinessObjectXmlSchema(ByVal Object As BoObjectTypes) As String` Retrieves the XML schema that is used by the object to validate the input XML files.
  - param `Object`: one of the enumeration's values (see the enum file)
  - remarks: Schemes use a dynamic cache mechanism so that when the first specified schema is called, the schema is created and updated dynamically with the user fields related to the object. For more information, see Exchanging Data Using the DI API XML Capabilities.
  - enum: `BoObjectTypes` in `../enums/enums-01.md`
- `Public Function GetCompanyDate() As Date` Get Company DATE
- `Public Function GetCompanyList() As Recordset` Retrieves a list of the company databases located on the specified server.
  - returns: This method returns a Recordset object that contains a list of available companies on the server. The list includes the following four fields: - dbName - represents the database name. - cmpName - represents the company name. - versStr - represents the version number of the company database. - dbUser - represents the database owner.
  - remarks: This method is commonly used at start-up phase, when you are not sure which company databases exist on the server. Alternatively, you can use this method to allow users to choose the company database. Before using this method, you must set the correct value to the Server property. After retrieving the company databases list, you can use the Connect method to set up a connection with a specific company database.
- `Public Function GetCompanyService() As CompanyService` Creates a new CompanyService.
- `Public Function GetCompanyTime() As String` Get Company Time
- `Public Function GetContextCookie() As String` Creates a cookie that consists of the current DI API session for Sign-on Procedure.
- `Public Function GetDBServerDate() As Date` method GetDBServerDate
- `Public Function GetDBServerTime() As String` method GetDBServerTime
- `Public Sub GetLastError(ByRef errCode As Long, ByRef errMsg As String)` Retrieves the error code and message for the last error for any object tied to the Company object.
  - param `errCode`: The error code. If no error occurred, the code is 0.
  - param `errMsg`: The error message. If no error occurred, the message is an empty string. When applicable, the message also contains the application error code, for example, 10001090 - Posting period missing. More information about the error with this code can be found in the application help, accessible in the application via the Help --> Documentation --> Online Help. In the help, you can search for the error code or you can navigate to SAP Business One --> Message Documentation.
  - remarks: You must call this method immediately after the API call that caused the error. The error information is lost when you call other methods. If an error is associated with a system error, a description of the system error is included. Error Codes Code (errCode) Description (errMsg) 0 (Empty string - no error was found) -103 Connection to the company database has failed. -104 Connection to the license database has failed. -105 The observer.dll init has failed. -106 You are not connected to a company. -107 Wrong username and/or password. -108 Error reading company definitions. -109 Error copying dll to temp directory. -110 Error opening observer.dll. -111 Connection to SBO-Common has failed. -112 Error extracting dll from cab. -113 Error creating temporary dll folder. -114 No server defined. -115 No database defined. -116 Already connected to a company database. -117 Language is not supported. -118 Exceeded the number of max concurrent users. -1001 The field is to small to accept the data -1002 Invalid row. -1103 Object not supported. -1104 Invalid XML file. -1105 Invalid index. -1106 Invalid field name. -1107 Wrong object state. -1108 The transaction is already active. -1109 There is no active transaction in progress. -1110 Invalid user entered. -1111 Invalid file name. -1112 Could not save the XML file. -1113 Function not implemented. -1114 XML validation failed. -1115 No XML schema was found to support this object. -1120 Ref count for this object is higher then 0. -1130 Invalid edit state. -2000 SQL native error. -2050 No query string entered. -2051 No value found. -2052 No records found. -2053 Invalid object. -2054 Either BOF or EOF have been reached. -2055 The value entered is invalid. -3000 The logged on user does not have permission to use this object. -3001 You do not have a permission to view this fields data. -8004 Company connection is dead. -8005 Server connection is dead. -8006 Error opening language resource. -8007 License failure. -8008 Error initializing the DB layer. -8009 Too many users connected. -8010 No valid license is present. -8011 Error initializing Business objects layer. -8012 Company version mismatch. -8013 Error initializing the application environment. -8014 Invalid command. -8015 Missing parameter. . -8016 Unsupported object. -8017 Invalid command for this object. -8018 Internal permission error. -8019 Dll is not initialized. -8020 Language init error. -8021 Timeout encountered. -8022 Init error. -8023 Wrong user or password.
- `Public Function GetLastErrorCode() As Long` Retrieves the last error code issued by any object related to the Company object.
  - remarks: You can use this method, instead of GetLastError, for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Function GetLastErrorContext() As String` method GetLastErrorContext
- `Public Function GetLastErrorDescription() As String` Retrieves the description of the last error issued by any object related to the Company object.
  - remarks: You can use this method, instead of GetLastError, for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub GetNewObjectCode(ByRef ObjectCode As String)` Retrieves the key of the last added record.
  - param `ObjectCode`: Gets the key of the last object that you have created.
  - remarks: After you create a new object such as, BusinessPartners and Items objects, you can use this method to retrieve the object key. If no new object is found, the method returns an empty string in the ObjectCode parameter. You can use this method, for example, to create a payment based on an invoice: - Create invoice. - Get the key for identifying the invoice (Invoices property of the Payments object). - Create the payment.
- `Public Function GetNewObjectKey() As String` Retrieves the key of the last added record.
  - remarks: You can use this method, instead of GetNewObjectCode, for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Function GetNewObjectType() As String` Gets the last added object type.
  - remarks: After the global flag EnableApprovalProcedureInDI is turned on, we strongly recommend that you call this method each time you add any document or payment to make sure that your Documents(Payments) have been added as Document(Payment) or Draft(PaymentDraft).
  - VB example (SAP's help labels this C#, but it is Visual Basic - translate before use):
    ```vb
    ' Preconditions: Approval template should be set in order to make every invoice pass approval process.
    Dim dockey As String = String.Empty
    Dim docType As String = String.Empty
    Dim oInv As SAPbobsCOM.Documents = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oInvoices)

    oInv.CardCode = "BP1"
    oInv.DocDate = Date.Today

    oInv.Lines.ItemCode = "Item1"
    oInv.Lines.Quantity = 2
    oInv.Lines.Price = 5
    oInv.Lines.TaxCode = "tx001"

    ' This call must be done after all properties were filled
    ' User can change remark if they need

    ' Fill Approval Request sub object
    oInv.GetApprovalTemplates()
    oInv.Document_ApprovalRequests.Remarks = "Some Remarks for approval"

    Dim ret As Integer
    'Invoice was added as draft
    ret = oInv.Add()

    If ret = 0 Then
        'Get new added object key and type
        dockey = oCompany.GetNewObjectKey()
        docType = oCompany.GetNewObjectType()
    End If
    ```
- `Public Function GetRegisteredServersList() As Recordset` Retrieves a list of servers registered with the System Landscape Directory (SLD) server. Use this method when creating a window for logging into SAP Business One. Create a dropdown list of servers and allow the user to select the server to which to connect.
  - C# example (from SAP's help):
    ```csharp
    Company oCompany = new SAPbobsCOM.Company();
    oCompany.SLDServer = "myServer:40000";

    Recordset oRecordset = oCompany.GetRegisteredServersList();

    while (!oRecordset.EoF)
    {
        Console.WriteLine(oRecordset.Fields.Item(0).Value.ToString());
        oRecordset.MoveNext();
    }
    ```
- `Public Function GetXMLelementCount(ByVal FileName As String) As Long` Retrieves the number of business objects described in an XML file.
  - param `FileName`: Specifies the full path and file name of the XML file containing the Business objects.
  - remarks: Use this method find out how many business objects are described in the XML file when using the method GetBusinessObjectFromXML, and you want to . For more information, see Exchanging Data Using the DI API XML Capabilities.
- `Public Function GetXMLobjectType(ByVal FileName As String, ByVal Index As Long) As BoObjectTypes` Retrieves the type of business object described in an XML file on a specific offset specified by the Index parameter.
  - param `FileName`: Specifies the full path and file name of the XML file containing the Business objects.
  - param `Index`: Specifies the offset of the Business object within the file, when using an XML file containing more the one Business object. Otherwise, you can enter the value 0.
  - remarks: Before using the GetXMLobjectType method, use the GetXMLelementCount to find out the number of business objects described in the XML file.
- `Public Function IsDTCTransactionObjectSet() As Boolean` Checks whether or not the DTCTransactionObject is set.
- `Public Function SetSboLoginContext(ByVal conStr As String) As Long` Decodes the encrypted connection information received from the UI API -- based on the cookie created by the GetContextCookie method -- and then sets the connection information for log on to the Company database. See Sign-on Procedure.
  - param `conStr`: Specifies the connection information string.
- `Public Sub StartTransaction()` Starts a transaction, allowing you to perform data operations on several business objects. Use the EndTransaction method to end the transaction and free locked records, allowing other users to access them.
  - remarks: Use this method when you want to perform data operations on several business objects: - If the operations succeed, either commit the transaction to save the data in the database, or roll back to discard the changes. - If one of the operations fail, the DI API rolls back the transaction, which discards the changes. After a failed DI API call in the transaction, you must immediately exit the transaction (see the example below).
  - example note: When working with transactions, make sure to check the return code when executing SAP Business One APIs and, if an error occurs, immediately exit the transaction. If a call fails, SAP Business One automatically ends the transaction with a rollback (of all actions up to that point); if you do not exit the transaction code, all subsequent code is still executed even though an error occurred.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        int errorCode = 0;
        bool findItem = false;
        string errorMessage = string.Empty;
        SAPbobsCOM.Company company = new SAPbobsCOM.Company();

        company.Server = "PVGD50059267A";//mandatory property
        //mandatory property in release 8.8 and afterwards. Before release 8.8, dst_MSSQL (SQL Server 2000) is the default value.
        company.DbServerType = SAPbobsCOM.BoDataServerTypes.dst_MSSQL2005;
        company.CompanyDB = "2009";//mandatory property
        company.UserName = "manager";//mandatory property
        company.Password = "1234";//mandatory property

        company.DbUserName = "sa"; //optional in release 8.8 and afterwards
        company.DbPassword = "sasa"; //optional in release 8.8 and afterwards
        company.UseTrusted = false; //optional in release 8.8 and afterwards
        company.language = SAPbobsCOM.BoSuppLangs.ln_English; //optional
        //Optional, default value is from DI configuration file in release 8.8 and afterwards
        company.SLDServer = "PVGD50059267A:40000";
        errorCode = company.Connect();
        if (errorCode != 0)
        {
            //You can also use GetLastError to get the error code and error message at the same time.
            errorMessage = company.GetLastErrorDescription();
            MessageBox.Show("Fail to conect to SAP Business One. " + "Error Code: " + errorCode.ToString() + " Error Message: " + errorMessage);
            return;
        }

        company.StartTransaction();
        SAPbobsCOM.Items item = company.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oItems) as SAPbobsCOM.Items;
        findItem = item.GetByKey("itemcode");
        if (!findItem)
        {
            MessageBox.Show("Can not find the item.");
            return;
        }
        item.BarCode = "1234567";
        errorCode = item.Update();
        if (errorCode != 0)
        {
            company.GetLastError(out errorCode, out errorMessage);
            MessageBox.Show("Fail to update item master data. " + "Error Code: " + errorCode.ToString() + " Error Message: " + errorMessage);
            //transaction started has been rolled back by SAP Business One automaticly. Just return the code and do your error handling.
            return;
        }

        // Get predefined text service
        SAPbobsCOM.CompanyService companyService = company.GetCompanyService();
        SAPbobsCOM.PredefinedTextsService textService = companyService.GetBusinessService(SAPbobsCOM.ServiceTypes.PredefinedTextsService) as SAPbobsCOM.PredefinedTextsService;

        // Add predefined text
        SAPbobsCOM.PredefinedText text = textService.GetDataInterface(SAPbobsCOM.PredefinedTextsServiceDataInterfaces.ptsPredefinedText) as SAPbobsCOM.PredefinedText;
        text.TextCode = "text code";
        text.Text = "test content";
        try
        {
            SAPbobsCOM.PredefinedTextParams param = textService.AddPredefinedText(text);
        }
        catch (System.Runtime.InteropServices.COMException ex)
        {
            MessageBox.Show(ex.ErrorCode.ToString());
            MessageBox.Show(ex.Message);
            //transaction started has been rolled back by SAP Business One automaticly. Just return the code and do your error handling.
            return;
        }

        company.EndTransaction(SAPbobsCOM.BoWfTransOpt.wf_Commit);
        company.Disconnect();
    }
    catch (Exception ex)
    {
        // ... unexpected error
    }
    ```

## Events (1)
- `Public Event ProgressIndicator(ByVal MaxValue As Long, ByVal CurrentValue As Long)` Progress indicator for long process execution. To be supported in future releases.

# CompanyInfo (Object)

The CompanyInfo is a data structure related to the CompanyService. It includes initial parameters related to the company. The default values of part of the properties vary according to the country localization. Source table: CINF.

## Properties (35)
- `Public Property AutoCreateCustomerEqCard() As BoYesNoEnum` [R/W] Determines whether or not to create automatically customer equipment card when assigning a unique serial number. Field name: AutoCrIns.
  - remarks: Field name in the application: Auto. Create Customer Equipment Card. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Inventory tab --> Items tab.
- `Public Property AutoSRICreationOnReceipt() As BoYesNoEnum` [R/W] Determines whether or not to create automatically consecutive serial numbers on receipt of items to the inventory (system numerartor). This flag is applicable only if the inventory management method is On Release Only. Field name: SriCreatIn.
  - remarks: Field name in the application: Automatic Serial Number Creation on Receipt. To display the form in the application: - Select Administration -->System Initialization -->General Settings -->Inventory tab -->Items tab.
- `Public Property B1iTimeOut() As Long` [R/W] property B1iTimeOut
- `Public Property BaseDateForExchangeRate() As BoBaseDateRateEnum` [R/W] Determines whether the exchange rate is based on the Posting Date (P) or the Tax Date (T). Field name: RateBase.
  - remarks: Field name in the application: Base Date for Exchange Rate. To display the form in the application: - Select Administration -->System Initialization -->General Settings -->Inventory tab -->Items TAB.
- `Public Property BISRBankAccount() As String` [R] BISRBnkAcDetermines whether the exchange rate is based on the Posting Date (P) or the Tax Date (T). Field name: BISRBnkAc.
  - remarks: Field name in the application: BISR Bank Account. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Accounting Data tab.
- `Public Property BISRBankActKey() As Long` [R/W] Set or returns the BISR bank account key. Field name: BisBnkAcKy. This is a foreign key to the HouseBankAccounts object (AbsoluteEntry).
- `Public Property BISRBankCountry() As String` [R] Sets the country code (3 characters) of the company house bank (BISR bank in Switzerland companies). This flag is valid only when EnbPayRef is set to Y. Field name: BISBnkCnt.
  - remarks: Field name in the application: BISR Bank Country. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Accounting Data tab.
- `Public Property BISRBankNo() As String` [R] Sets the code of the of the company house bank (BISR bank in Switzerland companies). This flag is valid only when EnbPayRef is set to Y. Field name: BISRBnkCd.
  - remarks: Field name in the application: BISR Bank No. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Accounting Data tab.
- `Public Property BISRBranch() As String` [R] Sets the branch number of the of the company house bank (BISR bank - applicable for Switzerland). This flag is valid only when EnbPayRef is set to Y. Field name: BISRBranch.
  - remarks: Field name in the application: BISR Branch. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Accounting Data tab.
- `Public Property BlockStockNegativeQuantity() As BoYesNoEnum` [R/W] Determines whether or not to block documents that would cause negative inventory level. Field name: BlockZeroQ.
  - remarks: Field name in the application: Block Below Negative Quantity. To display the form in the application: - Select Administration -->System Initialization -->Document Setting -->General tab.
- `Public Property CompanyName() As String` [R] Returns this company name . Field name: CompnyName. Length: 100 characters.
- `Public Property DataOwnershipIndication() As BoYesNoEnum` [R/W] Determines whether or not to block documents that would cause negative inventory level. Field name: BlockZeroQ.
  - remarks: Field name in the application: Block Below Negative Quantity. To display the form in the application: - Select Administration -->System Initialization -->Document Setting -->General tab.
- `Public Property DefaultDaysForOrdCanc() As Long` [R/W] Sets the default number of days before cancelling a sales order. After this date the goods are not to be eccepted by the customer. The default value is 30 days after the Delivery Date. Field name: DaysOrdCnc.
  - remarks: Field name in the application: Default Days for Order Cancellation. To display the form in the application: - Select Administration -->System Initialization -->Document Setting -->Per Document tab.
- `Public Property DefaultStampTax() As String` [R/W] Sets the default stamp tax code for incoming payments. Applicable for Portugal. Field name: stampTax.
  - remarks: Field name in the application: Default Stamp Tax Code. To display the form in the application: - Select Administration -->System Initialization -->Document Setting -->Per Document tab.
- `Public Property DisplayTransactionsByDflt() As BoYesNoEnum` [R/W] Determines whether or not to display all transactions by default for incoming and outgoing payments. Field name: DispTrByDf.
  - remarks: Field name in the application: Display All Transactions by Default. To display the form in the application: - Select Administration -->System Initialization -->Document Setting -->Per Document tab.
- `Public Property EnableAccountSegmentation() As BoYesNoEnum` [R/W] Determines whether or not to enable account segmentation. Field name: EnbSgmnAct.
  - remarks: Field name in the application: Enable Accounts Segmentation. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Basic Initialization tab.
- `Public Property EnableBillOfExchange() As BoYesNoEnum` [R/W] Determines whether or not to enable bill-of-exchange payment method. Applicable for Spain, Italy, France, and Portugal. Field name: EnableBOE.
  - remarks: Field name in the application:Use Bill of Exchange. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Basic Initialization tab.
- `Public Property EnableCheckQuantityInRDR() As BoYesNoEnum` [R/W] Determines whether or not to check automatically the availabllity of item quantities before adding the quantity in sales orders. The default setting is Y. In case the available quantity is less than the quantity specified in the sales order, the system displays several options. Field name: ChkQunty.
  - remarks: Field name in the application: Activate Automatic Availability Check (in Sales Orders). To display the form in the application: - Select Administration -->System Initialization -->Document Setting -->Per Document tab.
- `Public Property EnableConversionDifferentAcct() As BoYesNoEnum` [R] Determines whether or not to enable the conversion different accounts. Field name: ConvDifAct.
- `Public Property EnableExpensesManagement() As BoYesNoEnum` [R/W] Determines whether or not to enable additional expenses management Field name: EnblExpns.
  - remarks: Field name in the application: Enable Expenses Management. To display the form in the application: - Select Administration -->System Initialization -->Document Setting -->General tab.
- `Public Property EnableStockRelNoCostPrice() As BoYesNoEnum` [R/W] Determines whether or not to allow stock release without the item cost price. Field name: RelStkNoPr.
  - remarks: Field name in the application: Max. Number Of Documents In Payment. To display the form in the application: - Select Administration -->System Initialization -->Document Setting -->Per Document tab.
- `Public Property EnableTransactionNotification() As BoYesNoEnum` [R/W] property EnableTransactionNotification
- `Public Property GroupLinesInVATCalculation() As BoYesNoEnum` [R] Returns a valid value that determines whether or not the Tax Engine System groups the lines when calculating the tax. Field name: CalcVatGrp.
- `Public Property IEPSPayer() As BoYesNoEnum` [R/W] Determines whether or not the company is liable to IEPS Payer (indirect tax). Applicable for Mexico, Costa Rica, and Guatemala. Companies defined as liable for IEPS Payer must maintain special IEPS posting, printing forms and declaration for authorities in all A/R documents. Note: For Mexico only, when this filed is set to Y, the IEPS Payer option is available also in the Item Master Data -->General tab. Field name: IepsPayer.
  - remarks: Field name in the application: IEPS Payer. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Accounting Data tab.
- `Public Property LanguageCode() As BoSuppLangs` [R/W] property LanguageCode
- `Public Property Localization() As String` [R] property Localization
  - remarks: Administration --> Choose Company --> Find your DB: localization column.
- `Public Property MaxNumberOfDocumentsInPmt() As Long` [R/W] Sets the maximum number of invoices for outgoing payments by check. Field name: MxDcsInPmt.
  - remarks: Field name in the application: Max. Number Of Documents In Payment. To display the form in the application: - Select Administration -->System Initialization -->Document Setting -->Per Document tab.
- `Public Property MaxRecordsInChooseFromList() As Long` [R/W] Sets the maximum number of records to display in the Choose From List form. Field name: MaxChoose.
  - remarks: Field name in the application: No. of Choose from list Rows. To display the form in the application: - Select Administration -->System Initialization -->General Settings -->Display tab.
- `Public Property MinimumAmountForAnnualList() As Double` [R/W] Sets the minimum amount above which a document is included in the annual sales report. This report is used for VAT declaration regarding customers only. The report covers all the customers who have federal tax ID that starts with a Belgium ISO code, and all the sales transactions that are VAT liable such as A/R invoices, A/R credit memos, down payments and manual journal entries created for sales purposes. Applicable for Belgium. Field name: MinAmntAL.
  - remarks: Field name in the application: Minimum Amount for Annual Sales List. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Accounting Data tab.
- `Public Property MinimumAmountForAppndixOP() As Double` [R/W] Sets the minimum amount above which a document is included in the annual sales report. This report is used for VAT declaration regarding customers only. The report covers all the customers who have federal tax ID that starts with a Belgium ISO code, and all the sales transactions that are VAT liable such as A/R invoices, A/R credit memos, down payments and manual journal entries created for sales purposes. Applicable for Belgium. Field name: MinAmntAL.
  - remarks: Field name in the application: Minimum Amount for Annual Sales List. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Accounting Data tab.
- `Public Property MinimumBaseAmountPerDoc() As Double` [R/W] Determines whether or not to enable generatiion of reports that include only documents with minimum base amount. Applicable for Portugal. Field name: MinBaseDoc.
  - remarks: Field name in the application: Minimum Base Amount per Document. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Accounting Data tab.
- `Public Property PercentOfTotalAcquisition() As Double` [R/W] Determines whether or not to enable generatiion of reports that include only documents with minimum base amount. Applicable for Portugal. Field name: MinBaseDoc.
  - remarks: Field name in the application: Minimum Base Amount per Document. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Accounting Data tab.
- `Public Property SRIManagementSystem() As BoManageMethod` [R/W] Determines the default management method for serial numbers and batches. The options are: A - On Every Transaction. The user must assign serial or batch numbers on every inventory transaction. R - On Release Only. The user must assign serial or batch numbers only on release (it is optional for other transactions). Field name: SriMngSys.
  - remarks: Field name in the application: SRI Management System. To display the form in the application: - Select Administration -->System Initialization -->General Settings -->Inventory tab -->Items tab.
- `Public Property TaxCalculationSystem() As TaxCalcSysEnum` [R] Returns a valid value that determines the type of tax calculation system to be used by the Tax Calculation Engine. Field name: TaxSysType).
- `Public Property Version() As Long` [R] Returns the version of SAP Business One application used by the company. Field name: Version.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# BOEDocumentTypesService (Object)

This service manages document types in SAP Business One. Mandatory properties: DocDescription, DocType. Source table: ODTY.

## Methods (8)
- `Public Function AddBOEDocumentType(ByVal pIBOEDocumentType As BOEDocumentType) As BOEDocumentTypeParams` Adds a DocumentType with DocType and DocDescription as specified in the BOEDocumentType data structure.
  - param `pIBOEDocumentType`: Specifies the BOE document type to be added.
- `Public Sub DeleteBOEDocumentType(ByVal pIBOEDocumentTypeParams As BOEDocumentTypeParams)` Deletes a DocumentType with DocEntry specified in BOEDocumentTypeParams.
  - param `pIBOEDocumentTypeParams`: BOEDocumentTypeParams
- `Public Function GetBOEDocumentType(ByVal pIBOEDocumentTypeParams As BOEDocumentTypeParams) As BOEDocumentType` Returns an instance of the BOEDocumentType data structure.
  - param `pIBOEDocumentTypeParams`: BOEDocumentType
- `Public Function GetBOEDocumentTypeList() As BOEDocumentTypesParams` Returns a collection of instances for the BOEDocumentTypes data structure.
- `Public Function GetDataInterface(ByVal enumMSDI As BOEDocumentTypesServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `BOEDocumentTypesServiceDataInterfaces` in `../enums/enums-01.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates a data structure from specified XML file.
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates a data structure from a specified XML string.
  - param `bstrXMLString`: 
- `Public Sub UpdateBOEDocumentType(ByVal pIBOEDocumentType As BOEDocumentType)` Replaces DocType and DocDescription of DocumentType with the specified BOEDocumentTypes data structure.
  - param `pIBOEDocumentType`: 

# BOEInstruction (Object)

A data structure object holding properties for the BOEInstructionsService.

## Properties (4)
- `Public Property InstructionCode() As String` [R/W] Sets or returns a string specifying the instruction code. Field name: InstrCode.
- `Public Property InstructionDesc() As String` [R/W] Sets or returns a string specifying the instruction description. Field name: InstrDespt.
- `Public Property InstructionEntry() As Long` [R] Returns a number specifying the instruction entry. Field name: AbsEntry.
- `Public Property IsCancelInstruction() As BoYesNoEnum` [R/W] property IsCancelInstruction

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the string of the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# BOEInstructionParams (Object)

This object holds identification properties for the BOEInstructionsService object.

## Properties (2)
- `Public Property InstructionCode() As String` [R] Returns a string specifying the instruction code. Field name: InstrCode.
- `Public Property InstructionEntry() As Long` [R/W] Sets or returns a number specifying the instruction entry. Field name: AbsEntry.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the string of the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# BOEInstructions (Collection)

This is a data collection of BOEInstruction data structure.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the total objects in the collection.

## Methods (5)
- `Public Function Add() As BOEInstruction` Adds a new object to the collection.
- `Public Function GetXMLSchema() As String` Retreives the XML schema of the data structrue.
- `Public Function Item(ByVal vtIndex As Variant) As BOEInstruction` Returns a reference to a specified object in the collection.
  - param `vtIndex`: Specifies the index of the object.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# BOEInstructionsParams (Collection)

This is a data collection of BOEInstructionParams data structure.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the total objects in the collection.

## Methods (5)
- `Public Function Add() As BOEInstructionParams` Adds a new object to the collection.
- `Public Function GetXMLSchema() As String` Retreives the XML schema of the data structrue.
- `Public Function Item(ByVal vtIndex As Variant) As BOEInstructionParams` Returns a reference to a specified object in the collection.
  - param `vtIndex`: Specifies the index of the object.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# BOEInstructionsService (Object)

This service manages instructions in SAP Business One. Mandatory properties: InstructionCode, InstructionDesc. Source table: OIST.

## Methods (8)
- `Public Function AddBOEInstruction(ByVal pIBOEInstruction As BOEInstruction) As BOEInstructionParams` Adds an Instruction with InstructionCode and InstructionDesc as specified in the BOEInstruction data structure.
  - param `pIBOEInstruction`: Specifies the BOE instruction to be added.
- `Public Sub DeleteBOEInstruction(ByVal pIBOEInstructionParams As BOEInstructionParams)` Deletes Instruction with InstructionEntry specified in BOEInstructionParams.
  - param `pIBOEInstructionParams`: BOEInstructionParams
- `Public Function GetBOEInstruction(ByVal pIBOEInstructionParams As BOEInstructionParams) As BOEInstruction` Returns an instance of the BOEInstruction data structure.
  - param `pIBOEInstructionParams`: BOEInstructionParams
- `Public Function GetBOEInstructionList() As BOEInstructionsParams` Returns a collection of instances for the BOEInstruction data structure.
- `Public Function GetDataInterface(ByVal enumMSDI As BOEInstructionsServiceDataInterfaces) As Object` Creates empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `BOEInstructionsServiceDataInterfaces` in `../enums/enums-01.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates data structure from specified XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates data structure from specified XML string.
  - param `bstrXMLString`: XML string.
- `Public Sub UpdateBOEInstruction(ByVal pIBOEInstruction As BOEInstruction)` Replaces InstructionCode and InstructionDesc of Instruction with the specified BOEInstruction data structure.
  - param `pIBOEInstruction`: Specifies the BOE instruction to be updated.

# BOELine (Object)

Represents the deposits for bills of exchange. Source table: OBOE.

**Remarks:** A bill of exchange is a document addressed by the vendor to the customer requiring the latter to pay a certain amount on the due date.

## Properties (9)
- `Public Property AccountNumber() As String` [R] The bank account of the deposit. Field name: DpstAcct.
- `Public Property amount() As Double` [R] The total amount of the bill of exchange. Field name: BoeSum.
- `Public Property Bank() As String` [R] The house bank code of the deposit. Field name: DpsBankCod.
- `Public Property BOEKey() As Long` [R] The key of the bill of exchange. Field name: BoeKey.
- `Public Property BOENumber() As Long` [R] The number of the bill of exchange. Field name: BoeNum.
- `Public Property BOEStatus() As BoBoeStatus` [R] The status of the bill of exchange. Field name: BoeStatus.
- `Public Property Branch() As String` [R] The house bank branch of the deposit. Field name: DpstBranch.
- `Public Property DueDate() As Date` [R] The due date of the bill of exchange. Field name: DueDate.
- `Public Property Transferred() As BoYesNoEnum` [R] Indicates whether the bill of exchange is transferred to the next year or not. Field name: Transfered.

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

# BOELineParams (Object)

Holds the key of a bill of exchange. This object is used to pass keys to and retrieve keys from BOELinesService methods.

## Properties (1)
- `Public Property BOEKey() As Long` [R/W] The key of the bill of exchange. Field name: BoeKey.

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

# BOELines (Collection)

A data collection of BOELine objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As BOELine` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As BOELine` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# BOELinesParams (Collection)

A data collection of BOELineParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As BOELineParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As BOELineParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# BOELinesService (Object)

The BOELinesService service enables you to get a deposit for bill of exchange. Source table: OBOE.

**Remarks:** To view details on deposited bills of exchange, from SAP Business One, choose Banking --> Deposits --> Deposit. Then, select a deposit created for a bill of exchange.

## Methods (4)
- `Public Function GetBOELine(ByVal pIBOELineParams As BOELineParams) As BOELine` Retrieves a deposit for bill of exchange. The bill of exchange is specified by its key, which is contained in the BOELineParams object passed to the method.
  - param `pIBOELineParams`: The key of the bill of exchange to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As BOELinesServiceDataInterfaces) As Object` Creates an empty data structure for use with the BOELinesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `BOELinesServiceDataInterfaces` in `../enums/enums-01.md`
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

# BOEPortfolio (Object)

A data structure object holding properties for the BOEPortfoliosService. Source table: OPTF.

## Properties (5)
- `Public Property PortfolioCode() As String` [R/W] Sets or returns a string specifying the portfolio code. Field name: PtfCode.
- `Public Property PortfolioDescription() As String` [R/W] Sets or returns a string specifying the portfolio description. Field name: PtfDespt.
- `Public Property PortfolioEntry() As Long` [R] Returns a number specifying the portfolio entry. Field name: AbsEntry.
- `Public Property PortfolioID() As String` [R/W] Sets or returns a string specifying the internal portfolio id. Field name: PtfId.
- `Public Property PortfolioNum() As String` [R/W] Sets or returns a string specifying the portfolio number. Field name: PtfNum.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the string of the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# BOEPortfolioParams (Object)

This object holds identification properties for the BOEPortfoliosService object.

## Properties (3)
- `Public Property PortfolioCode() As String` [R] Returns a number specifying the portfolio code. Field name: PtfCode.
- `Public Property PortfolioEntry() As Long` [R/W] Sets or returns a string specifying the portfolio entry. Field name: AbsEntry.
- `Public Property PortfolioID() As String` [R] Returns a number specifying the internal portfolio id. Field name: PtfId.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the string of the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# BOEPortfolios (Collection)

This is a data collection of BOEPortfolio data structures.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the total objects in the collection.

## Methods (5)
- `Public Function Add() As BOEPortfolio` Adds a new object to the collection.
- `Public Function GetXMLSchema() As String` Retreives the XML schema of the data structrue.
- `Public Function Item(ByVal vtIndex As Variant) As BOEPortfolio` Returns a reference to a specified object in the collection.
  - param `vtIndex`: Specifies the index of the object.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# BOEPortfoliosParams (Collection)

This object is a collection of BOEPortfolioParams.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the total objects in the collection.

## Methods (5)
- `Public Function Add() As BOEPortfolioParams` Adds a new object to the collection.
- `Public Function GetXMLSchema() As String` Retreives the XML schema of the data structrue.
- `Public Function Item(ByVal vtIndex As Variant) As BOEPortfolioParams` Returns a reference to a specified object in the collection.
  - param `vtIndex`: Specifies the index of the object.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# BOEPortfoliosService (Object)

This service manages Portfolios in SAP Business One. Mandatory properties: PortfolioCode, PortfolioDescription, PortfolioID, PortfolioNum. Source table: OPTF.

## Methods (8)
- `Public Function AddBOEPortfolio(ByVal pIBOEPortfolio As BOEPortfolio) As BOEPortfolioParams` Adds a Portfolio with data as specified in the BOEPortfolio data structure.
  - param `pIBOEPortfolio`: Specifies the BOE portfolio to be added.
- `Public Sub DeleteBOEPortfolio(ByVal pIBOEPortfolioParams As BOEPortfolioParams)` Deletes Portfolio with PortfolioEntry specified in BOEPortfolioParams.
  - param `pIBOEPortfolioParams`: BOEPortfolioParams
- `Public Function GetBOEPortfolio(ByVal pIBOEPortfolioParams As BOEPortfolioParams) As BOEPortfolio` Returns an instance of the BOEPortfolio data structure.
  - param `pIBOEPortfolioParams`: BOEPortfolio
- `Public Function GetBOEPortfolioList() As BOEPortfoliosParams` Returns a collection of instances for the BOEPortfolio data structure.
- `Public Function GetDataInterface(ByVal enumMSDI As BOEPortfoliosServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `BOEPortfoliosServiceDataInterfaces` in `../enums/enums-01.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` BOEPortfoliosService Object
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates a data structure from a specified XML string.
  - param `bstrXMLString`: 
- `Public Sub UpdateBOEPortfolio(ByVal pIBOEPortfolio As BOEPortfolio)` Replaces fields of Portfolio with the specified BOEPortfolio data structure.
  - param `pIBOEPortfolio`: Specifies the BOE portfolio to be updated.

# Boxes1099 (Object)

Boxes1099 is a child object of the Forms1099 object. It enables to add 1099 reporting boxes to a specified 1099 Form type. Source table: TNN1.

**Remarks:** Country-specific for USA only. To display the form in the application: - Select Administration -->Setup -->Financials -->1099 Table. - Double-click the number on the left of the 1099 Form type for which you want to add 1099 Boxes.

## Properties (6)
- `Public Property Box1099() As String` [R/W] Sets or returns the name of the 1099 reporting box. Field name: Box1099. Length: 20 characters.
- `Public Property BoxDescription() As String` [R/W] Sets or returns the description of the 1099 reporting box. Field name: BoxDescr. Length: 100 characters.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property FormCode() As Long` [R] Returns the identification key of the 1099 Form type as assigned by the system when adding a new 1099 Form type. Field name: FormCode.
- `Public Property Minimum1099Amount() As Double` [R/W] Sets or returns the minimum amount to include in the 1099 report.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# BPAccountReceivablePayble (Object)

BPAccountReceivablePayble is a child object of the BusinessPartners object and represents the Business Partner Account Receivable Payable table in the Business Partner module. This object enables you to add a business partner account. Source table: CRD3.

**Remarks:** To display the form in the application: - Select Business Partners --> Business Partner Master Data. - In the Accounting tab, click the button [...] next to Control Accounts.

## Properties (4)
- `Public Property AccountCode() As String` [R/W] Sets or returns the G/L account code of the business partner as defined in Chart of Accounts. Field name: AcctCode. Length: 15 characters.
  - remarks: To set the AccountCode value when working with segmentation, use the FormatCode to find its key value (for example, _SYS00000000010) as follows: 1. Find the account key using the method GetObjectKeyBySingleValue. 2. Use the returned Recordset to retrieve the value of the key (for example, _SYS00000000010).
- `Public Property AccountType() As BoBpAccountTypes` [R/W] Sets or returns a valid value of BoBpAccountTypes that specifies the account type of the business partner. Field name: AcctType.
- `Public Property BPCode() As String` [R] The key to the current object's parent business partner.
- `Public Property Count() As Long` [R] Returns the number of records in the BPAccountReceivablePayble object. Field name: .

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# BPAddresses (Object)

BPAddresses is a child object of the BusinessPartners and represents the Ship To and Bill To addresses list of the business partner. This object is part of the Business Partner module. You can retrieve or set this object by using the Addresses property of the BusinessPartners object. This object enables you to add Ship To, Bill To, and multiple addresses to the business partner master data. Source table: CRD1.

**Remarks:** Mandatory field in SAP Business One: AddressName. To display the form in the application: - Select Business Partners --> Business Partner Master Data --> Addresses tab.

**Example:**
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
  Dim bp As SAPbobsCOM.BusinessPartners

  Set bp = DIcompany.GetBusinessObject(oBusinessPartners)

  Dim bpA As SAPbobsCOM.BPAddresses

  Set bpA = bp.Addresses

  bp.CardName = "C009"

  bp.CardCode = "C009"

  bp.CardType = SAPbobsCOM.BoCardTypes.cCustomer

  bp.Addresses.AddressName = "Address1"

  bp.Addresses.Block = "1"

  bp.Addresses.Street = "street 1"

  bp.Addresses.City = "City 1"

  bp.Addresses.Country = "DE"

  bp.Addresses.AddressType = SAPbobsCOM.BoAddressType.bo_BillTo

  bp.Addresses.Add

  bp.Addresses.AddressName = "Address2"

  bp.Addresses.Block = "2"

  bp.Addresses.Street = "street 2"

  bp.Addresses.City = "City 2"

  bp.Addresses.Country = "DE"

  bp.Addresses.AddressType = SAPbobsCOM.BoAddressType.bo_BillTo

  bp.Addresses.Add

  bp.Addresses.AddressName = "Address3"

  bp.Addresses.Block = "3"

  bp.Addresses.Street = "street 3"

  bp.Addresses.City = "City 3"

  bp.Addresses.Country = "DE"

  bp.Addresses.AddressType = SAPbobsCOM.BoAddressType.bo_BillTo

  bp.Addresses.Add

  bp.Add

  bp.GetByKey ("C009")

  Set bpA = bp.Addresses

  bpA.SetCurrentLine (1)
  ```

## Properties (29)
- `Public Property AddressName() As String` [R/W] Sets or returns the name of the address (Bill To address, Main address, Ship To address, and so on). Field name: Address. Mandatory property. Length: 50 characters.
- `Public Property AddressName2() As String` [R/W] Sets or returns the BP second, alternative Address. Field name: Address2. Length: 50 characters.
- `Public Property AddressName3() As String` [R/W] Sets or returns the BP third, alternative Address. Field name: Address3. Length: 50 characters.
- `Public Property AddressType() As BoAddressType` [R/W] Sets or returns a valid value of BoAddressType type that specifies the type of the business partner's address: Ship To or Bill To. Field name: AdresType.
  - remarks: Default address type: Ship To.
- `Public Property Block() As String` [R/W] Sets or returns the block address. Field name: Block. Length: 100 characters.
- `Public Property BPCode() As String` [R] The key to the current object's parent business partner.
- `Public Property BuildingFloorRoom() As String` [R/W] Sets or returns the additional address details, such as building number, floor number, and room number. Field name: Building. Length: 64,000 characters.
- `Public Property City() As String` [R/W] Sets or returns the city. Field name: City. Length: 100 characters.
- `Public Property Count() As Long` [R] Returns the number of addresses in the object.
- `Public Property Country() As String` [R/W] Sets or returns the country code (for example, DE). Field name: City. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
  - remarks: You can set any country code that is defined in the Countries table (OCRY - not exposed through the DI API).
- `Public Property County() As String` [R/W] Sets or returns the county. Field name: County. Length: 100 characters.
- `Public Property CreateDate() As Date` [R] property CreateDate
- `Public Property CreateTime() As Date` [R] property CreateTime
- `Public Property FederalTaxID() As String` [R/W] Sets or returns the federal tax ID of the business partner. Field name: LicTradNum. Length: 32 characters.
- `Public Property GlobalLocationNumber() As String` [R/W] property GlobalLocationNumber
- `Public Property GSTIN() As String` [R/W] property GSTIN
- `Public Property GstType() As BoGSTRegnTypeEnum` [R/W] property GstType
- `Public Property MYFType() As BoMYFTypeEnum` [R/W] property MYFType
- `Public Property Nationality() As String` [R/W] property Nationality
- `Public Property RowNum() As Long` [R] The line number within the lines of the current object's parent business partner.
- `Public Property State() As String` [R/W] Sets or returns the state code of the business partner. Field name: State. Length: 3 characters. This is a foreign key to the States table (OCST), which is not exposed through the DI API.
  - remarks: Only state codes that are defined in the States table are applicable.
- `Public Property Street() As String` [R/W] Sets or returns the street of the business partner address. Field name: Street. Length: 100 characters.
- `Public Property StreetNo() As String` [R/W] The street number. Field name: StreetNo
  - remarks: For Brazil only.
- `Public Property TaasEnabled() As BoYesNoEnum` [R/W] property TaasEnabled
- `Public Property TaxCode() As String` [R/W] Sets or returns the sales tax code. Field name: TaxCode. Length: 8 characters.
  - remarks: Country-specific property for USA. The tax code represents the sales tax related to specific locations where the business transaction occurs. Tax codes are defined in SAP Business One.
- `Public Property TaxOffice() As String` [R/W] property TaxOffice
- `Public Property TypeOfAddress() As String` [R/W] The address type. Field name: AddrType
  - remarks: For Brazil only.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property ZipCode() As String` [R/W] Sets or returns the zip code. Field name: ZipCode. Length: 20 characters.

## Methods (3)
- `Public Sub Add()` Adds a new Address record. To save the information to the database, use the Add method in the BusinessPartners object.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.BusinessPartners oBP;

    // Delete BP address
    if (oBP.GetByKey("11") == true)
    {
        oBP.Addresses.SetCurrentLine(2);
        oBP.Addresses.Delete();
        oBP.Update();
    }
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# BPBankAccounts (Object)

BPBankAccounts is a business object that represents the bank accounts of the business partner. Source table: OCRB.

**Remarks:** To display the form in the application: - Select Business Partners --> Business Partner Master Data. - Select Payment Terms tab. - Near the Bank Country field, click the Choose icon.

## Properties (36)
- `Public Property ABARoutingNumber() As String` [R/W] The ABA routing number to identify the financial institution upon which payment was drawn. Field name: ABARoutNum. Length: 25 characters.
- `Public Property AccountName() As String` [R/W] Returns the Business partner's Account Name. Field name: AcctName. Length: 100 characters. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia)
- `Public Property AccountNo() As String` [R/W] Sets or returns the bank account number. Field name: Account. Length: 50 characters.
- `Public Property BankCode() As String` [R/W] Sets or returns the bank code as defined in the Banks object. Field name: BankCode. Length: 30 characters.
- `Public Property BICSwiftCode() As String` [R/W] The BIC/SWIFT code to be used in transactions and messages between banks. Field name: SwiftNum. Length: 50 characters.
  - remarks: The default BIC/SWIFT code is taken from the Banks - Setup window of the selected bank code.
- `Public Property BIK() As String` [R/W] Returns the Business partner's Bank Identification Key. Field name: BIK. Length: 15 characters. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia)
- `Public Property Block() As String` [R/W] Sets or returns the block address of the bank. Field name: Block. Length: 100 characters.
- `Public Property BPCode() As String` [R/W] Sets or returns the business partner identification code. Field name: CardCode. Length: 15 characters.
- `Public Property Branch() As String` [R/W] Sets or returns the branch number. Field name: Branch. Length: 50 characters.
- `Public Property BuildingFloorRoom() As String` [R/W] Sets or returns the additional bank address details, such as building number, floor number, and room number. Field name: Building. Length: 64,000 characters.
- `Public Property City() As String` [R/W] Sets or returns the city of the bank address. Field name: City. Length: 100 characters.
- `Public Property ControlKey() As String` [R/W] Sets or returns the bank control key of the business partner. Field name: ControlKey. Length: 2 characters.
  - remarks: The control key specifies the type of account, for example: 01 indicates Checking Account, 02 indicates Saving Account, and so on.
- `Public Property CorrespondentAccount() As String` [R/W] Returns a G/L account number for the the Business partner's Correspondent Account. Field name: CorresAcct. Field name: CorresAcct. Length: 30 characters. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia)
- `Public Property Count() As Long` [R] Returns the total number of bank accounts of the business partners.
- `Public Property Country() As String` [R/W] Sets or returns the country code of the bank. Field name: Country. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
- `Public Property County() As String` [R/W] Sets or returns the county of the bank. Field name: County. Length: 100 characters.
- `Public Property CustomerIdNumber() As String` [R/W] Sets or returns the customer Id. number. Field name: CustIdNum. Field name: CustIdNum. Length: 254 characters.
- `Public Property Fax() As String` [R/W] Returns the Business partner's Bank FAX number. Field name: FAX. Length: 25 characters. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia)
- `Public Property IBAN() As String` [R/W] Sets or returns the International Bank Account Number (IBAN) for the business partner. Field name: IBAN. Length: 50 characters.
  - remarks: Europe only.
- `Public Property InternalKey() As Long` [R/W] Sets or returns the internal key identifier of the bank. Field name: AbsEntry.
- `Public Property ISRBillerID() As String` [R/W] Sets or returns the business partner ISR biller Id. Field name: ISRBillerI. Length: 9 characters.
- `Public Property ISRType() As Long` [R/W] Sets or returns the ISR type. Field name: ISRType.
- `Public Property LogInstance() As Long` [R/W] Sets or returns the key identifier of the log instance. Each activity with the BPBankAccount is logged to the ACRB log table with the LogInstance identifier. Field name: LogInstanc. Length: 3 characters.
- `Public Property MandateExpDate() As Date` [R/W] property MandateExpDate
- `Public Property MandateID() As String` [R/W] The code to identify the direct debit mandate between the business partner and the company. Field name: MandateID. Length: 35 characters.
- `Public Property Phone() As String` [R/W] Returns the Business partner's Bank Phone number. Field name: Phone. Length: 50 characters. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia)
- `Public Property SEPASeqType() As SEPASequenceTypeEnum` [R/W] property SEPASeqType
- `Public Property SignatureDate() As Date` [R/W] The date on which the mandate is signed. Field name: SignDate.
- `Public Property State() As String` [R/W] Sets or returns the state code of the business partner bank account. Field name: State. Length: 3 characters. This is a foreign key to the States table (OCST), which is not exposed through the DI API.
  - remarks: Only state codes that are defined in the States table are applicable.
- `Public Property Street() As String` [R/W] Sets or returns the street of the bank address. Field name: State. Length: 100 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserNo1() As String` [R/W] Sets or returns the payee bank user number 1 or password. User numbers 1 - 4 are used to identify the payment file. Field name: UsrNumber1. Length: 25 characters.
- `Public Property UserNo2() As String` [R/W] Sets or returns the payee bank user number 2 or password. User numbers 1 - 4 are used to identify the payment file. Field name: UsrNumber2. Length: 25 characters.
- `Public Property UserNo3() As String` [R/W] Sets or returns the payee bank user number 3 or password. User numbers 1 - 4 are used to identify the payment file. Field name: UsrNumber3. Length: 25 characters.
- `Public Property UserNo4() As String` [R/W] Sets or returns the payee bank user number 4 or password. User numbers 1 - 4 are used to identify the payment file. Field name: UsrNumber4. Length: 25 characters.
- `Public Property ZipCode() As String` [R/W] Sets or returns the zip code of the bank address. Field name: ZipCode. Length: 20 characters.

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - remarks: If you delete the default bank account for a business partner, the first bank account in the remaining list becomes the default.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.BusinessPartners oBP;

    // Delete BP bank account
    if (oBP.GetByKey("11") == true)
    {
        oBP.BPBankAccounts.SetCurrentLine(1);
        oBP.BPBankAccounts.Delete();
        oBP.Update();
    }
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# BPBlockSendingMarketingContents (Object)

Block sending marketing contnet to the business partner.

## Properties (3)
- `Public Property CardCode() As String` [R] The business partner code. Field name: CardCode. Length: 15 characters.
- `Public Property Choose() As BoYesNoEnum` [R/W] Choose to block sending marketing contnet to the business partner.
- `Public Property CommunicationMediaId() As Long` [R/W] Communication media code. Field name: CommCode. Length: 50 characters.

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oOrder As SAPbobsCOM.Documents ' Order object

            Dim lRetCode As Integer ' Return Code

            ' New Order

            oOrder = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oOrders)

            ' Fill Order details

            oOrder.CardCode = "C40000"

            oOrder.CardName = "Earthshaker Corporation"

            oOrder.HandWritten = SAPbobsCOM.BoYesNoEnum.tNO

            oOrder.DocDate = Today()

            oOrder.DocDueDate = Today()

            oOrder.DocCurrency = "USD"

            'Fill 2 lines in the order

            oOrder.Lines.ItemCode = "A00001"

            oOrder.Lines.ItemDescription = "IBM Inforprint 1312"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            oOrder.Lines.Add()

            oOrder.Lines.ItemCode = "A00002"

            oOrder.Lines.ItemDescription = "IBM Infoprint 1222"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            ' Now we want to delete the second line in the Order

            oOrder.Lines.Delete()

            ' The Order will be added without the second line

            lRetCode = oOrder.Add
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# BPBranchAssignment (Object)

BPBranchAssignment Class

## Properties (4)
- `Public Property BPCode() As String` [R] property BPCode
- `Public Property BPLID() As Long` [R/W] property BPLID
- `Public Property Count() As Long` [R] property Count
- `Public Property DisabledForBP() As BoYesNoEnum` [R/W] property DisabledForBP

## Methods (3)
- `Public Sub Add()` method Add
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 

# BPCode (Object)

BPCode is a data structure related to the BusinessPartnersService. Source table: OPB1.

**Remarks:** To display the form related to the data structure: - Select Administration --> System Initialization --> Openning Balances --> Busines Partners Openning Balance.

## Properties (10)
- `Public Property BpCtrlAcct() As String` [R/W] property BpCtrlAcct
- `Public Property Code() As String` [R/W] Sets or returns the business partner code for which to create an opening balance. Field name: CardCode. Length: 15 characters.
- `Public Property Credit() As Double` [R/W] Sets or returns the amount to credit the business partner account.
- `Public Property Debit() As Double` [R/W] Sets or returns the amount to debit the business partner account.
- `Public Property DueDate() As Date` [R/W] Sets or returns the due date of the transaction.
- `Public Property ForeignCredit() As Double` [R/W] Sets or returns the amount, in foreign currency, to credit the business partner account.
- `Public Property ForeignCurrency() As String` [R/W] Sets or returns the foreign currency code used in the transaction. Length: 3 characters.
- `Public Property ForeignDebit() As Double` [R/W] Sets or returns the amount, in foreign currency, to debit the business partner account.
- `Public Property SystemCredit() As Double` [R/W] Sets or returns the amount, in system currency, to credit the business partner account.
- `Public Property SystemDebit() As Double` [R/W] Sets or returns the amount, in system currency, to debit the business partner account.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# BPCodes (Collection)

BPCodes is a collection of BPCode data structures.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of BPCode data structures in the BPCodes data collection.

## Methods (5)
- `Public Function Add() As BPCode` Add a new BPCode data structure to the to the BPCodes collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As BPCode` Returns a reference to the BPCode that you want to get.
  - param `vtIndex`: Specifies the number of the BPCode in the collection (starts from 0).
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# BPCurrencies (Object)

Business Partners currency. Source table: CRD13.

**Example:**
- C# example (from SAP's help):
  ```csharp
  SAPbobsCOM.BusinessPartners bp = (SAPbobsCOM.BusinessPartners)oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oBusinessPartners);
  bp.GetByKey("C10000");
  bp.BPCurrencies.SetCurrentLine(5);
  bp.BPCurrencies.Include = BoYesNoEnum.tNO;
  bp.Update();
  ```

## Properties (3)
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property CurrencyCode() As String` [R] Field name: CurrCode. Length: 3 characters.
- `Public Property Include() As BoYesNoEnum` [R/W] Field name: INCLUDE.

## Methods (1)
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# BPFiscalRegistryID (Object)

BPFiscalRegistryID is a data structure related to the BusinessPartnersService. BPFiscalRegistryID describes the type of the company's business activity (this information is required in some Brazilian legal reports). Moreover, government use the information to calculate the percentage of the companies related to a certain economic activity. This object enables you to add the Fiscal Registry ID for companies or business partners. Source table: OCNA.

**Remarks:** - This Object is specific to Cluster 2B (Country specific property for Brazil only). - The Term 4SS refers to the document repository, RDF model and related services. - 4SS stands for 4 Suite Server, appears in some documents and throughout the software.

## Properties (5)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CNAECode() As String` [R/W] Sets or returns the business partner CNAE (Change Notification Agent) Code. Field name: CNAECode. Length: 9 characters.
- `Public Property Description() As String` [R/W] Sets or returns the business partner's fiscal description. Field name: Descrip. Length: 64,000 characters.
- `Public Property Numerator() As Long` [R] Returns the absolute entry of the fiscal registry Id. Field name: AbsId.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a new record to the OCNA table.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
- `Public Function GetByKey(ByVal lGroupCode As Long) As Boolean` Retrieves the values of the object's properties by the object's absolute key from the Company database.
  - param `lGroupCode`: Specifies the required object's properties according to object's absolute key in Company database.
- `Public Function Remove() As Long` method Remove
- `Public Sub SaveToFile(ByVal bstrFileName As String)` Save the object to a file as XML data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub SaveXML(ByRef pbstrFileName As String)` Saves the object data to XML formatted data.
  - param `pbstrFileName`: Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates the object data in the company database.

# BPFiscalTaxID (Object)

BPFiscalTaxID is a child object of the BusinessPartners and indicates the Brazilian Fiscal IDs info for each business partner. You can retrieve or set this object by using the FiscalTaxID property of the BusinessPartners object. This object enables you to: - Add the Fiscal IDs of the business partner. - Define the Fiscal TAX IDs for Business Partner Master Data. Source table: CRD7

**Remarks:** This Object is specific to Cluster 2B (Country specific property for Brazil only).

## Properties (22)
- `Public Property Address() As String` [R/W] Sets or returns the Business Partner address. Field name: Address. Length: 50 characters.
- `Public Property AddrType() As BoAddressType` [R] Indicates the type of address for this fiscal ID.
- `Public Property AuthorizationForRetrieveFromSEFAZ() As BoYesNoEnum` [R/W] Authorization for retrieve from SEFAZ. Field name: AToRetrNFe.
- `Public Property BPCode() As String` [R] The key to the current object's parent business partner.
- `Public Property CNAECode() As Long` [R/W] Sets or returns the Brazil CNAE code. Field name: CNAEId. This is a foreign key to the CNAE (Change Notification Agent Code) table (OCNA), not exposed through the DI API.
- `Public Property Count() As Long` [R] Returns the number of Fiscal IDs for current BusinessPartner.
- `Public Property TaxId0() As String` [R/W] Sets or returns the Fiscal Tax ID 0. Field name: TaxId0. Length: 100 characters.
  - remarks: For India localizations, this number represents the PAN number. If the SubjectToWithholdingTax property of the BusinessPartners object is set to yes, then TaxId0 is mandatory and must be set to a 10-character value.
- `Public Property TaxId1() As String` [R/W] Sets or returns the Fiscal Tax ID 1. Field name: TaxId1. Length: 100 characters.
- `Public Property TaxId10() As String` [R/W] Sets or returns the Fiscal Tax ID 10. Field name: TaxId10. Length: 100 characters.
- `Public Property TaxId11() As String` [R/W] Sets or returns the Fiscal Tax ID 11. Field name: TaxId11. Length: 100 characters.
- `Public Property TaxId12() As String` [R/W] Sets or returns the Fiscal Tax ID 12. Field name: TaxId12. Length: 50 characters.
- `Public Property TaxId13() As String` [R/W] Sets or returns the Deductee Ref. No. in India. Field name: TaxId13. Length: 100 characters.
- `Public Property TaxId14() As String` [R/W] Sets or returns the ITR Filing. Field name: TaxId14. Length: 250 characters.
- `Public Property TaxId2() As String` [R/W] Sets or returns the Fiscal Tax ID 2. Field name: TaxId2. Length: 100 characters.
- `Public Property TaxId3() As String` [R/W] Sets or returns the Fiscal Tax ID 3. Field name: TaxId3. Length: 100 characters.
- `Public Property TaxId4() As String` [R/W] Sets or returns the Fiscal Tax ID 4. Field name: TaxId4. Length: 100 characters.
- `Public Property TaxId5() As String` [R/W] Sets or returns the Fiscal Tax ID 5. Field name: TaxId5. Length: 100 characters.
- `Public Property TaxId6() As String` [R/W] Sets or returns the Fiscal Tax ID 6. Field name: TaxId6. Length: 100 characters.
- `Public Property TaxId7() As String` [R/W] Sets or returns the Fiscal Tax ID 7. Field name: TaxId7. Length: 100 characters.
- `Public Property TaxId8() As String` [R/W] Sets or returns the Fiscal Tax ID 8. Field name: TaxId8. Length: 100 characters.
- `Public Property TaxId9() As String` [R/W] Sets or returns the Fiscal Tax ID 9. Field name: TaxId9. Length: 100 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new record to the CRD7 table.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# BPIntrastatExtension (Object)

BPIntrastatExtension Class

## Properties (9)
- `Public Property CardCode() As String` [R] property CardCode
- `Public Property CustomsProcedure() As Long` [R/W] property CustomsProcedure
- `Public Property DomesticOrForeignID() As String` [R/W] property DomesticOrForeignID
- `Public Property Incoterms() As Long` [R/W] property Incoterms
- `Public Property IntrastatRelevant() As BoYesNoEnum` [R/W] property IntrastatRelevant
- `Public Property NatureOfTransactions() As Long` [R/W] property NatureOfTransactions
- `Public Property PortOfEntryOrExit() As Long` [R/W] property PortOfEntryOrExit
- `Public Property StatisticalProcedure() As Long` [R/W] property StatisticalProcedure
- `Public Property TransportMode() As Long` [R/W] property TransportMode

# BPPaymentDates (Object)

BPPaymentDates is a child object of BusinessPartners object that represents the payment days in the month for the business partner. Source table: CRD5.

**Remarks:** To display the form in the application: - Select Business Partners --> Business Partner Master Data. - Select Payment Terms tab. - Click Payment Dates.

## Properties (4)
- `Public Property BPCode() As String` [R] The key to the current object's parent business partner.
- `Public Property Count() As Long` [R] Returns the total number of records in the object.
- `Public Property PaymentDate() As String` [R/W] Sets or returns the payment day in the month to the business partner. Field name: PmntDate. Length: 2 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.BusinessPartners oBP;

    // Delete BP payment date
    if (oBP.GetByKey("11") == true)
    {
        oBP.BPPaymentDates.SetCurrentLine(1);
        oBP.BPPaymentDates.Delete();
        oBP.Update();
    }
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# BPPaymentMethods (Object)

BPPaymentMethods is a child object of the BusinessPartners object that represents the payment methods related to the business partner. Source table: CRD2.

## Properties (5)
- `Public Property BPCode() As String` [R] The key to the current object's parent business partner.
- `Public Property Count() As Long` [R] Returns the number of payment methods related to the business partner. Returns the total number of records in the object.
- `Public Property PaymentMethodCode() As String` [R/W] Sets or returns the payment method related to the business partner. Field name: PymCode. This is a foreign key to the WizardPaymentMethods Object. Length: 15 characters.
- `Public Property RowNumber() As Long` [R] Returns the available row number. Field name: LineNum.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (3)
- `Public Sub Add()` Add a new PaymentMethod to the object. Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the row specified by the parameter to be the current active row. Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# BPPriorities (Object)

The BPPriorities object enables to define business partner priorities for payment terms. Source table: OBPP.

**Remarks:** The list of priorities will appear as a selection list in the Priority field of the Payment Terms tab of the business partner master card. To display the form in the application: - Select Administration -->Setup -->Business Partners -->Business Partner Priorities.

## Properties (4)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Priority() As Long` [R/W] Sets or returns the priority code. Field name: PrioCode.
- `Public Property PriorityDescription() As String` [R/W] Sets or returns the priority description. Field name: PrioDesc. Length: 10 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a business partner priority to the object.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lCode`: Specifies the code of the item.
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

# BPVatExemptions (Object)

BPVatExemptions Class

## Properties (4)
- `Public Property AbsoluteEntry() As Long` [R] property AbsoluteEntry
- `Public Property BPCode() As String` [R/W] property BPCode
- `Public Property BPVatExemptionsLines() As BPVatExemptionsLines` [R] property BPVatExemptionsLines
- `Public Property Remarks() As String` [R/W] property Remarks

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# BPVatExemptionsLine (Object)

BPVatExemptionsLine Class

## Properties (15)
- `Public Property AbsoluteEntry() As Long` [R] property AbsoluteEntry
- `Public Property ApplyAllItems() As BoYesNoEnum` [R/W] property ApplyAllItems
- `Public Property AuthoritiesName() As String` [R/W] property AuthoritiesName
- `Public Property ExemptionDocNum() As String` [R/W] property ExemptionDocNum
- `Public Property ExemptionType() As Long` [R/W] property ExemptionType
- `Public Property IssueDate() As Date` [R/W] property IssueDate
- `Public Property IssueTime() As Date` [R/W] property IssueTime
- `Public Property ItemCode() As String` [R/W] property ItemCode
- `Public Property ItemDescription() As String` [R] property ItemDescription
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property TaxCode() As String` [R/W] property TaxCode
- `Public Property ValidFrom() As Date` [R/W] property ValidFrom
- `Public Property ValidTo() As Date` [R/W] property ValidTo
- `Public Property VATRate() As Double` [R/W] property VATRate
- `Public Property VisualOrder() As Long` [R] property VisualOrder

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# BPVatExemptionsLines (Collection)

BPVatExemptionsLines Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As BPVatExemptionsLine` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As BPVatExemptionsLine` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` method Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# BPVatExemptionsParams (Object)

BPVatExemptionsParams Class

## Properties (2)
- `Public Property AbsoluteEntry() As Long` [R/W] property AbsoluteEntry
- `Public Property BPCode() As String` [R] property BPCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# BPVatExemptionsParamsCollection (Collection)

BPVatExemptionsParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As BPVatExemptionsParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As BPVatExemptionsParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# BPVatExemptionsService (Object)

BPVatExemptionsService Class

## Methods (8)
- `Public Function Add(ByVal pIBPVatExemptions As BPVatExemptions) As BPVatExemptionsParams` Add
  - param `pIBPVatExemptions`: 
- `Public Sub Delete(ByVal pIBPVatExemptionsParams As BPVatExemptionsParams)` Delete
  - param `pIBPVatExemptionsParams`: 
- `Public Function Get(ByVal pIBPVatExemptionsParams As BPVatExemptionsParams) As BPVatExemptions` Get
  - param `pIBPVatExemptionsParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As BPVatExemptionsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `BPVatExemptionsServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As BPVatExemptionsParamsCollection` GetList
- `Public Sub Update(ByVal pIBPVatExemptions As BPVatExemptions)` Update
  - param `pIBPVatExemptions`: 

# BPWithholdingTax (Object)

BPWithholdingTax is a child object of the BusinessPartners object that represents the withholding tax data related to the business partner. Source table: CRD4.

## Properties (4)
- `Public Property BPCode() As String` [R] The key to the current object's parent business partner.
- `Public Property Count() As Long` [R] Returns the total number of records in the object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WTCode() As String` [R/W] Sets or returns the withholding tax code assigned to the business partner. Field name: WTCode. Length: 4 characters. This is a foreign key to the WithholdingTaxCodes object.
  - remarks: This is a foreign key to WithholdingTaxCodes object. Country-specific property for Germany, Switzerland, Netherlands, Norway, Finland, Denmark, Austria, UK, Sweden, Spain, Italy, India, and Portugal. For India localizations, if this property is set to yes, then the TaxId0 property of the BPFiscalTaxID object is mandatory and must be set to a 10-character value.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# Branch (Object)

Represents a branch. Source table: OUBR Mandatory properties: Name

## Properties (3)
- `Public Property Code() As Long` [R] The key for the branch. Field name: Code
- `Public Property Description() As String` [R/W] A description for the branch. Field name: Remarks
- `Public Property Name() As String` [R/W] The display name of the branch. Field name: Name

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

# BranchesParams (Collection)

A collection of BranchParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As BranchParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As BranchParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# BranchesService (Object)

The BranchesService service enables you to add, look up and remove branches in the branches master data table. Branches can be assigned to users and employees. To see the list of branches and create a new one, select Administration --> Setup --> General --> Users, and then select the Branch field. Source table: OUBR

## Methods (8)
- `Public Function AddBranch(ByVal pIBranch As Branch) As BranchParams` Adds a branch.
  - param `pIBranch`: The data for the new branch.
  - returns: Contains the key (Code) of the new branch.
  - C# example (from SAP's help):
    ```csharp
    public void add()
    {
        try
        {
            BranchesService oBranchSrv;
            oBranchSrv = (BranchesService)(MainModule.oCmpSrv.GetBusinessService(ServiceTypes.BranchesService));
            SAPbobsCOM.Branch addLine;
            addLine = (SAPbobsCOM.Branch)oBranchSrv.GetDataInterface(BranchesServiceDataInterfaces.bsBranch);
            //full addition
            addLine.Name = "X";
            addLine.Description = "X Branch";
            oBranchSrv.AddBranch(addLine);
        }
        catch (Exception ex)
        {
            Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
        }
    }
    ```
- `Public Sub DeleteBranch(ByVal pIBranchParams As BranchParams)` Deletes an existing branch. The branch is specified by its key (Code), which is contained in the BranchParams object passed to the method.
  - param `pIBranchParams`: The key of the branch to be deleted.
  - remarks: System branches cannot be updated. Branches that have been assigned to a user or employee cannot be deleted.
  - C# example (from SAP's help):
    ```csharp
    public void delete()
    {
        try
        {
            BranchParams delLine;
            delLine = (BranchParams)oBranchSrv.GetDataInterface(BranchesServiceDataInterfaces.bsBranchParams);

            //delete a record
            //please note that the code should be of an existing record.
            delLine.Code = 5;

            //delete
            oBranchSrv.DeleteBranch(delLine);
        }
        catch (Exception ex)
        {
            Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
        }
    }
    ```
- `Public Function GetBranch(ByVal pIBranchParams As BranchParams) As Branch` Retrieves a specific branch. The branch is specified by its key (Code), which is contained in the BranchParams object passed to the method.
  - param `pIBranchParams`: The key of the branch to retrieve.
  - returns: The branch with the specified key.
  - C# example (from SAP's help):
    ```csharp
    public void update()
    {
        try
        {
            BranchParams getLine;
            SAPbobsCOM.Branch updateLine;
            getLine = (BranchParams)oBranchSrv.GetDataInterface(BranchesServiceDataInterfaces.bsBranchParams);

            //update a record
            //please note that the code should be of an existing record.
            getLine.Code = 5;

            updateLine = oBranchSrv.GetBranch(getLine);
            updateLine.Name = "T";
            updateLine.Description = "Y branch";
            oBranchSrv.UpdateBranch(updateLine);
        }
        catch (Exception ex)
        {
            Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
        }
    }
    ```
- `Public Function GetBranchList() As BranchesParams` Retrieves the keys and names of all the branches.
  - C# example (from SAP's help):
    ```csharp
    public void getlist()
    {
        try
        {
            BranchesParams getlistParams;
            getlistParams = oBranchSrv.GetBranchList();

            String resultSet = "";

            foreach (BranchParams record in getlistParams)
            {
                resultSet = resultSet + record.Code + "\t" + record.Name + "\n";
            }

            Interaction.MsgBox(resultSet, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
        }
        catch (Exception ex)
        {
            Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
        }
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As BranchesServiceDataInterfaces) As Object` Creates an empty data structure for use with the BranchesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `BranchesServiceDataInterfaces` in `../enums/enums-02.md`
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
- `Public Sub UpdateBranch(ByVal pIBranch As Branch)` Updates an existing branch. The data for the branch, including the key of the role to be updated, is contained in the Branch passed to the method. To update a branch, you must first retrieve it using the GetBranch method.
  - param `pIBranch`: The data for the branch to be updated. The Branch object must contain the key of the object to be updated.
  - remarks: System branches cannot be updated.

# BranchParams (Object)

Holds the key and name to an existing branch. This object is used to pass keys to and retrieve keys from BranchesService methods.

## Properties (2)
- `Public Property Code() As Long` [R/W] The key for a specific branch. Field name: Code
- `Public Property Name() As String` [R] The display name of a specific branch. Field name: Name

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

# BrazilBeverageIndexer (Object)

BrazilBeverageIndexer Class

## Properties (4)
- `Public Property BeverageCommercialBrandCode() As Long` [R/W] property BeverageCommercialBrandCode
- `Public Property BeverageGroupCode() As String` [R/W] property BeverageGroupCode
- `Public Property BeverageID() As Long` [R] property BeverageID
- `Public Property BeverageTableCode() As String` [R/W] property BeverageTableCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# BrazilBeverageIndexerParams (Object)

BrazilBeverageIndexerParams Class

## Properties (3)
- `Public Property BeverageCommercialBrandCode() As Long` [R/W] property BeverageCommercialBrandCode
- `Public Property BeverageGroupCode() As String` [R/W] property BeverageGroupCode
- `Public Property BeverageTableCode() As String` [R/W] property BeverageTableCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# BrazilBeverageIndexersParams (Collection)

BrazilBeverageIndexersParams Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As BrazilBeverageIndexerParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As BrazilBeverageIndexerParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# BrazilBeverageIndexersService (Object)

BrazilBeverageIndexersService Class

## Methods (7)
- `Public Function Add(ByVal pIBrazilBeverageIndexer As BrazilBeverageIndexer) As BrazilBeverageIndexerParams` Add
  - param `pIBrazilBeverageIndexer`: 
- `Public Sub Delete(ByVal pIBrazilBeverageIndexerParams As BrazilBeverageIndexerParams)` Delete
  - param `pIBrazilBeverageIndexerParams`: 
- `Public Function Get(ByVal pIBrazilBeverageIndexerParams As BrazilBeverageIndexerParams) As BrazilBeverageIndexer` Get
  - param `pIBrazilBeverageIndexerParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As BrazilBeverageIndexersServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `BrazilBeverageIndexersServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As BrazilBeverageIndexersParams` GetList

# BrazilFuelIndexer (Object)

BrazilFuelIndexer Class

## Properties (4)
- `Public Property Description() As String` [R/W] property Description
- `Public Property FuelCode() As String` [R/W] property FuelCode
- `Public Property FuelGroupCode() As Long` [R/W] property FuelGroupCode
- `Public Property FuelID() As Long` [R] property FuelID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# BrazilFuelIndexerParams (Object)

BrazilFuelIndexerParams Class

## Properties (4)
- `Public Property Description() As String` [R] property Description
- `Public Property FuelCode() As String` [R] property FuelCode
- `Public Property FuelGroupCode() As Long` [R] property FuelGroupCode
- `Public Property FuelID() As Long` [R/W] property FuelID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# BrazilFuelIndexersParams (Collection)

BrazilFuelIndexersParams Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As BrazilFuelIndexerParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As BrazilFuelIndexerParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# BrazilFuelIndexersService (Object)

BrazilFuelIndexersService Class

## Methods (7)
- `Public Function Add(ByVal pIBrazilFuelIndexer As BrazilFuelIndexer) As BrazilFuelIndexerParams` Add
  - param `pIBrazilFuelIndexer`: 
- `Public Sub Delete(ByVal pIBrazilFuelIndexerParams As BrazilFuelIndexerParams)` Delete
  - param `pIBrazilFuelIndexerParams`: 
- `Public Function Get(ByVal pIBrazilFuelIndexerParams As BrazilFuelIndexerParams) As BrazilFuelIndexer` Get
  - param `pIBrazilFuelIndexerParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As BrazilFuelIndexersServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `BrazilFuelIndexersServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As BrazilFuelIndexersParams` GetList

# BrazilMultiIndexer (Object)

BrazilMultiIndexer Class

## Properties (7)
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R/W] property Description
- `Public Property FirstRefIndexerCode() As String` [R/W] property FirstRefIndexerCode
- `Public Property ID() As Long` [R] property ID
- `Public Property IndexerType() As BrazilMultiIndexerTypes` [R/W] property IndexerType
- `Public Property SecondRefIndexerCode() As String` [R/W] property SecondRefIndexerCode
- `Public Property ThirdRefIndexerCode() As String` [R/W] property ThirdRefIndexerCode

## Methods (6)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetReferencedIndexerType(ByVal referenceIndex As Long, ByRef penumRsltType As BrazilIndexerTypes, ByRef plRsltValue As Long) As Boolean` method GetReferencedIndexerType
  - param `referenceIndex`: 
  - param `penumRsltType`: one of the enumeration's values (see the enum file)
  - param `plRsltValue`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# BrazilMultiIndexerParams (Object)

BrazilMultiIndexerParams Class

## Properties (6)
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R] property Description
- `Public Property FirstRefIndexerCode() As String` [R] property FirstRefIndexerCode
- `Public Property IndexerType() As BrazilMultiIndexerTypes` [R/W] property IndexerType
- `Public Property SecondRefIndexerCode() As String` [R] property SecondRefIndexerCode
- `Public Property ThirdRefIndexerCode() As String` [R] property ThirdRefIndexerCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# BrazilMultiIndexersParams (Collection)

BrazilMultiIndexersParams Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As BrazilMultiIndexerParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As BrazilMultiIndexerParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# BrazilMultiIndexersService (Object)

BrazilMultiIndexersService Class

## Methods (7)
- `Public Function Add(ByVal pIBrazilMultiIndexer As BrazilMultiIndexer) As BrazilMultiIndexerParams` Add
  - param `pIBrazilMultiIndexer`: 
- `Public Sub Delete(ByVal pIBrazilMultiIndexerParams As BrazilMultiIndexerParams)` Delete
  - param `pIBrazilMultiIndexerParams`: 
- `Public Function Get(ByVal pIBrazilMultiIndexerParams As BrazilMultiIndexerParams) As BrazilMultiIndexer` Get
  - param `pIBrazilMultiIndexerParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As BrazilMultiIndexersServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `BrazilMultiIndexersServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetIndexerTypeList(ByVal pIBrazilMultiIndexerParams As BrazilMultiIndexerParams) As BrazilMultiIndexersParams` GetIndexerTypeList
  - param `pIBrazilMultiIndexerParams`: 

# BrazilNumericIndexer (Object)

BrazilNumericIndexer Class

## Properties (4)
- `Public Property Code() As Long` [R/W] property Code
- `Public Property Description() As String` [R/W] property Description
- `Public Property ID() As Long` [R] property ID
- `Public Property IndexerType() As BrazilNumericIndexerTypes` [R/W] property IndexerType

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# BrazilNumericIndexerParams (Object)

BrazilNumericIndexerParams Class

## Properties (3)
- `Public Property Code() As Long` [R/W] property Code
- `Public Property Description() As String` [R] property Description
- `Public Property IndexerType() As BrazilNumericIndexerTypes` [R/W] property IndexerType

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# BrazilNumericIndexersParams (Collection)

BrazilNumericIndexersParams Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As BrazilNumericIndexerParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As BrazilNumericIndexerParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# BrazilNumericIndexersService (Object)

BrazilNumericIndexersService Class

## Methods (7)
- `Public Function Add(ByVal pIBrazilNumericIndexer As BrazilNumericIndexer) As BrazilNumericIndexerParams` Add
  - param `pIBrazilNumericIndexer`: 
- `Public Sub Delete(ByVal pIBrazilNumericIndexerParams As BrazilNumericIndexerParams)` Delete
  - param `pIBrazilNumericIndexerParams`: 
- `Public Function Get(ByVal pIBrazilNumericIndexerParams As BrazilNumericIndexerParams) As BrazilNumericIndexer` Get
  - param `pIBrazilNumericIndexerParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As BrazilNumericIndexersServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `BrazilNumericIndexersServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetIndexerTypeList(ByVal pIBrazilNumericIndexerParams As BrazilNumericIndexerParams) As BrazilNumericIndexersParams` GetIndexerTypeList
  - param `pIBrazilNumericIndexerParams`: 

# BrazilStringIndexer (Object)

BrazilStringIndexer Class

## Properties (4)
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R/W] property Description
- `Public Property ID() As Long` [R] property ID
- `Public Property IndexerType() As BrazilStringIndexerTypes` [R/W] property IndexerType

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# BrazilStringIndexerParams (Object)

BrazilStringIndexerParams Class

## Properties (3)
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R] property Description
- `Public Property IndexerType() As BrazilStringIndexerTypes` [R/W] property IndexerType

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# BrazilStringIndexersParams (Collection)

BrazilStringIndexersParams Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As BrazilStringIndexerParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As BrazilStringIndexerParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# BrazilStringIndexersService (Object)

BrazilStringIndexersService Class

## Methods (7)
- `Public Function Add(ByVal pIBrazilStringIndexer As BrazilStringIndexer) As BrazilStringIndexerParams` Add
  - param `pIBrazilStringIndexer`: 
- `Public Sub Delete(ByVal pIBrazilStringIndexerParams As BrazilStringIndexerParams)` Delete
  - param `pIBrazilStringIndexerParams`: 
- `Public Function Get(ByVal pIBrazilStringIndexerParams As BrazilStringIndexerParams) As BrazilStringIndexer` Get
  - param `pIBrazilStringIndexerParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As BrazilStringIndexersServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `BrazilStringIndexersServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetIndexerTypeList(ByVal pIBrazilStringIndexerParams As BrazilStringIndexerParams) As BrazilStringIndexersParams` GetIndexerTypeList
  - param `pIBrazilStringIndexerParams`: 

# Budget (Object)

Budget is a business object that represents the budget management in the Finance module. The budget management tracks company expenses and allows to block transactions when the budget exceeds. This object enables you to: - Add a budget object. - Retrieve a budget object by its key. - Update a budget object. - Save the object in XML format. Source table: OBGT.

**Remarks:** To initialize the budget management: - Select Administration --> System Initialization --> General Settings. - In the Budget tab, select Budget Initialization. - Set the budget initialization parameters and click OK. To display the form in the application: - Select Financials --> Budget --> Define Budget. - In the Define Budget dialog box, select a scenario and click OK. The budget management window opens.

## Properties (27)
- `Public Property AccountCode() As String` [R/W] Sets or returns the G/L account code as defined in Chart of Accounts. Field name: AcctCode. Length: 15 characters.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property BudgetBalanceCreditLoc() As Double` [R] Returns the budget balance in local currency of the revenue account (credit side), based on the journal transactions. Field name: CrdRLTotal.
- `Public Property BudgetBalanceCreditSys() As Double` [R] Returns the budget balance in system currency of the revenue account (credit side), based on the journal transactions. Field name: CrdRSTotal.
- `Public Property BudgetBalanceDebitLoc() As Double` [R] Returns the budget balance in local currency of the account (debit side), based on the journal transactions. Field name: CrdRSTotal.
- `Public Property BudgetBalanceDebitSys() As Double` [R] Returns the budget balance in system currency of the account (debit side), based on the journal transactions. Field name: DebRSTotal.
- `Public Property BudgetScenario() As Long` [R/W] Sets or returns the budget scenario ID number. Field name: Instance. This is a foreign key to the BudgetScenarios object.
- `Public Property CostAccountingLines() As BudgetCostAccounting_Lines` [R] property CostAccountingLines
- `Public Property DivisionCode() As Long` [R/W] Sets or returns the code of the budget distribution method. Field name: BgdCode. This is a foreign key to the BudgetDistribution object.
- `Public Property FutureAnnualExpensesCreditLoc() As Double` [R] Returns the total annual amount (in local currency) of open purchase orders and purchase delivery notes related to the revenue account (credit side). Field name: FtrODRLSum.
- `Public Property FutureAnnualExpensesCreditSys() As Double` [R] Returns the total annual amount (in system currency) of open purchase orders and purchase delivery notes related to the revenue account (credit side). Field name: FtrODRSSum.
- `Public Property FutureAnnualExpensesDebitLoc() As Double` [R] Returns the total annual amount (in local currency) of open purchase orders and purchase delivery notes related to the account (debit side). Field name: FtrOCRLSum.
- `Public Property FutureAnnualExpensesDebitSys() As Double` [R] Returns the total annual amount (in system currency) of open purchase orders and purchase delivery notes related to the account (debit side). Field name: FtrOCRSSum.
- `Public Property FutureAnnualRevenuesCredit() As Double` [R] Returns the future annual income related to the revenue account (credit side). Field name: FtrIDRSSum.
- `Public Property FutureAnnualRevenuesDebit() As Double` [R] Returns the future annual revenue related to the account (debit side). Field name: FtrIDRLSum.
- `Public Property FutureRevenuesDebitLoc() As Double` [R] Returns the future revenue in local currency related to the account (debit side). Field name: FtrICRLSum.
- `Public Property FutureRevenuesDebitSys() As Double` [R] Returns the future revenue in system currency related to the account (debit side). Field name: FtrICRSSum.
- `Public Property Lines() As Budget_Lines` [R] Returns the Budget_Lines object.
- `Public Property Numerator() As Long` [R] Returns the identification key of the budget as assigned by SAP Business One. Field name: SCNCounter.
- `Public Property ParentAccountKey() As String` [R/W] Sets or returns the parent G/L account code as defined in Chart of Accounts. This property is used for automatic calculation of the budget for the account (AccountCode), as a percentage (ParentAccPercent) of the parent account budget. Field name: FatherCode. Length: 15 characters.
- `Public Property ParentAccPercent() As Double` [R/W] Sets or returns the percentage of the parent account budget. Field name: FthrPrcnt.
- `Public Property StartofFiscalYear() As Date` [R] Returns the start date of the fiscal year (financial year). Field name: FinancYear.
- `Public Property TotalAnnualBudgetCreditLoc() As Double` [R/W] Returns the total annual budget in local currency of the revenue account (credit side). Field name: CrdRLTotal.
  - remarks: You must define either the TotalAnnualBudgetCreditLoc Property or the TotalAnnualBudgetDebitLoc Property. The value must be: TotalAnnualBudgetCreditLoc = total values of 12 BudgetTotCredit budget lines
- `Public Property TotalAnnualBudgetCreditSys() As Double` [R/W] Returns the total annual budget in system currency of the revenue account (credit side). Field name: CrdRSTotal.
  - remarks: The value must be: TotalAnnualBudgetCreditSys = total values of 12 BudgetSysTotCredit budget lines
- `Public Property TotalAnnualBudgetDebitLoc() As Double` [R/W] Returns the total annual budget in local currency (debit side). Field name: CredSTotal.
  - remarks: You must define either the TotalAnnualBudgetDebitLoc Property or the TotalAnnualBudgetCreditLoc Property. The value must be: TotalAnnualBudgetDeditLoc = total values of 12 BudgetTotDebit budget lines
- `Public Property TotalAnnualBudgetDebitSys() As Double` [R/W] Returns the total annual budget in system currency (debit side). Field name: DebSTotal.
  - remarks: The value must be: TotalAnnualBudgetDeditSys = total values of 12 BudgetSysTotDebit budget lines
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal Key As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `Key`: Budget ID number (Numerator).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
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

# Budget_Lines (Object)

Budget_Lines is a child object of Budget object and represents the budget item details of an account. Source table: BGT1.

**Remarks:** The budget item details of an account contains 12 lines, one for each monthly budget. The monthly budget percentage (PrecentOfAnnualBudgetAmount) depends on the budget distribution method (DivisionCode). To initialize the budget management: - Select Administration --> System Initialization --> General Settings. - In the Budget tab, select Budget Initialization. - Set the budget initialization parameters and click OK. To display the form in the application: - Select Financials --> Budget --> Define Budget. - In the Define Budget dialog box, select a scenario and click OK. The budget management window opens. - Click the number of a budget entry in the budget management table. The budget item details window opens.

## Properties (23)
- `Public Property AccountCode() As String` [R] Returns the G/L account code as defined in Chart of Accounts. Field name: AcctCode. Length: 15 characters.
- `Public Property BalSysTotCredit() As Double` [R] Returns the line budget balance in system currency of the revenue account (credit side), based on the journal transactions. Field name: CredSTotal.
- `Public Property BalSysTotDebit() As Double` [R] Returns the line budget balance in system currency of the account (debit side), based on the journal transactions. Field name: DebSTotal.
- `Public Property BalTotCredit() As Double` [R] Returns the line budget balance in local currency of the revenue account (credit side), based on the journal transactions. Field name: CredLTotal.
- `Public Property BalTotDebit() As Double` [R] Returns the line budget balance in local currency of the account (debit side), based on the journal transactions. Field name: DebLTotal.
- `Public Property BudgetKey() As Long` [R] Returns the identification key of the budget as assigned by SAP Business One. Field name: BudgId. This is a foreign key to the Budget object.
- `Public Property BudgetSysTotCredit() As Double` [R/W] Returns the budget in the line in system currency of the revenue account (credit side). Field name: CredSTotal.
- `Public Property BudgetSysTotDebit() As Double` [R/W] Returns the budget in the line in system currency of the account (debit side). Field name: DebSTotal.
- `Public Property BudgetTotCredit() As Double` [R/W] Returns the budget in the line in local currency of the revenue account (credit side). Field name: CrdRLTotal.
- `Public Property BudgetTotDebit() As Double` [R/W] Returns the budget in the line in local currency of the account (debit side). Field name: DebRLTotal.
- `Public Property Count() As Long` [R] Returns the total budget rows.
- `Public Property FutExpenCredit() As Double` [R] Returns the expense amount in the line (in local currency) of open purchase orders and purchase delivery notes related to the revenue account (credit side). Field name: FtrOCRLSum.
- `Public Property FutExpenDebit() As Double` [R] Returns the expense amount in the line (in local currency) of open purchase orders and purchase delivery notes related to the account (debit side). Field name: FtrODRLSum.
- `Public Property FutExpenSysCredit() As Double` [R] Returns the expense amount in the line (in system currency) of open purchase orders and purchase delivery notes related to the revenue account (credit side). Field name: FtrOCRSSum.
- `Public Property FutExpenSysDebit() As Double` [R] Returns the expense amount in the line (in system currency) of open purchase orders and purchase delivery notes related to the account (debit side). Field name: FtrODRSSum.
- `Public Property FutIncomesCredit() As Double` [R] Returns the future income in the line (in local currency) related to the revenue account (credit side). Field name: FtrICRLSum.
- `Public Property FutIncomesSysCredit() As Double` [R] Returns the future income in the line (in system currency) related to the revenue account (credit side). Field name: FtrICRSSum.
- `Public Property FutIncomesSysDebit() As Double` [R] Returns the future revenue in the line (in system currency) related to the account (debit side). Field name: FtrIDRSSum.
- `Public Property FutureIncomeDeb() As Double` [R] Returns the future revenue in the line (in local currency) related to the account (debit side). Field name: FtrIDRLSum.
- `Public Property PrecentOfAnnualBudgetAmount() As Double` [R] Returns the percentage of the annual budget amount for calculating the monthly budget. The value of this property depends on the budget distribution method (DivisionCode). Field name: MonthPrcnt.
- `Public Property RowDetails() As String` [R/W] Sets or returns a description about the monthly budget. Length: 50 characters. Field name: LineMemo.
- `Public Property RowNumber() As Long` [R] Returns the current available row number (month). Field name: Line_ID.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# BudgetCostAccounting_Lines (Object)

BudgetCostAccounting_Lines Class

## Properties (8)
- `Public Property Count() As Long` [R] property Count
- `Public Property Dimension() As Long` [R/W] property Dimension
- `Public Property DistrRuleCode() As String` [R/W] property DistrRuleCode
- `Public Property DistrRuleCreditLC() As Double` [R/W] property DistrRuleCreditLC
- `Public Property DistrRuleCreditSC() As Double` [R/W] property DistrRuleCreditSC
- `Public Property DistrRuleDebitLC() As Double` [R/W] property DistrRuleDebitLC
- `Public Property DistrRuleDebitSC() As Double` [R/W] property DistrRuleDebitSC
- `Public Property UserFields() As UserFields` [R] property UserFields

## Methods (3)
- `Public Sub Add()` method Add
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 

# BudgetDistribution (Object)

BudgetDistribution is a business object that represents the budget distribution methods used by the budget management in the Finance module. This object enables you to: - Add a budget distribution method. - Retrieve a budget distribution method by its key. - Update a budget distribution method. - Save the object in XML format. Source table: OBGD.

**Remarks:** To initialize the budget management: - Select Administration --> System Initialization --> General Settings. - In the Budget tab, select Budget Initialization. - Set the budget initialization parameters and click OK. To display the form in the application: - Select Financials --> Budget --> Define Budget Distribution Method.

## Properties (17)
- `Public Property April() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property August() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property BudgetAmount() As Double` [R/W] Returns the total of the 12 monthly factors. Field name: BgdTotal.
- `Public Property December() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property Description() As String` [R/W] Sets or returns the name of the budget distribution method. Field name: BgdName. Length: 30 characters.
- `Public Property DivisionCode() As Long` [R] Returns the budget distribution code. Field name: BgdCode.
- `Public Property February() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property January() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property July() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property June() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property March() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property May() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property November() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property October() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property September() As Double` [R/W] Sets or returns the the monthly factor. The total monthly factors must match the BudgetAmount.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (8)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Cancel() As Long` Cancels a record from the object table.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lBgdCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lBgdCode`: Budget distribution code (DivisionCode).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
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

# BudgetScenarios (Object)

BudgetScenarios is a business object that represents the budget scenarios used by the budget management in the Finance module. This object enables you to: - Add a budget scenario. - Remove a budget scenario. - Retrieve a budget scenario by its key. - Update a budget scenario. - Cancel a budget scenario. - Close a budget scenario. - Save the object in XML format. Source table: OBGS.

**Remarks:** Budget scenarios are used for the budgetary reports. Scenarios are used to create a prognosis of a particular situation in the company budget and to obtain important information about what the budgetary balance would be according to the selected scenario. Each budget scenario is assigned to a particular financial period. To initialize the budget management: - Select Administration --> System Initialization --> General Settings. - In the Budget tab, select Budget Initialization. - Set the budget initialization parameters and click OK. To display the form in the application: - Select Financials --> Budget --> Budget Scenarios.

## Properties (14)
- `Public Property BasicBudget() As Long` [R/W] Sets or returns the basis scenario that is used for defining the current scenario. Field name: BaseId.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property DistributionRule() As String` [R/W] property DistributionRule
- `Public Property DistributionRule2() As String` [R/W] property DistributionRule2
- `Public Property DistributionRule3() As String` [R/W] property DistributionRule3
- `Public Property DistributionRule4() As String` [R/W] property DistributionRule4
- `Public Property DistributionRule5() As String` [R/W] property DistributionRule5
- `Public Property InitialRatioPercentage() As Double` [R/W] Sets or returns the percentage of the defined budget in relation to the base budget. Field name: InitRate.
- `Public Property Name() As String` [R/W] Sets or returns the name of the budget scenario. Field name: Name. Length: 100 characters.
  - remarks: The scenario name must be unique for the financial period (StartofFiscalYear).
- `Public Property Numerator() As Long` [R] Returns the budget scenario ID number (unique key). Field name: AbsId.
- `Public Property Project() As String` [R/W] property Project
- `Public Property RoundingMethod() As BoRoundingMethod` [R/W] Sets or returns a valid value of BoRoundingMethod type that specifies the rounding method of the budget amount. Field name: RoundSys.
- `Public Property StartofFiscalYear() As Date` [R/W] Returns the start date of the fiscal year (financial year). Field name: FinancYear.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (8)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Cancel() As Long` Cancels a record from the object table.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lAbsID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lAbsID`: Scenario ID number (Numerator).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
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

# BusinessPartnerGroups (Object)

BusinessPartnerGroups represents the setup of customer and vendor Groups. Used for classifing business partners according to groups, such as, sector or size. Source table: OCRG.

**Remarks:** To display the form in the application: - Select Administration --> Setup --> Business Partners --> Customer Groups (or Vendor Groups).

## Properties (5)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Code() As Long` [R] Returns the group code of the current Business Partner Group. Field name: GroupCode.
- `Public Property Name() As String` [R/W] Sets or returns the name of current Business Partner Groups. Field name: GroupName. Length: 20 characters.
- `Public Property Type() As BoBusinessPartnerGroupTypes` [R/W] Sets or returns a valid value of BoBusinessPartnerGroupTypes that determines wether current group is a Customer Group or a Vendor Group. Field name: GroupType.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the OCRG table.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
- `Public Function GetByKey(ByVal lGroupCode As Long) As Boolean` Retrieves the values of the object's properties by the object's absolute key from the Company database.
  - param `lGroupCode`: Specifies the required object's properties according to object's absolute key in Company database.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal bstrFileName As String)` Save the object to a file as XML data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub SaveXML(ByRef pbstrFileName As String)` Saves the object data to XML formatted data.
  - param `pbstrFileName`: Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates the object data in the company database.

# BusinessPartnerPropertiesParams (Collection)

A collection of BusinessPartnerPropertyParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As BusinessPartnerPropertyParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As BusinessPartnerPropertyParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# BusinessPartnerPropertiesService (Object)

The BusinessPartnerPropertiesService service enables you to update and look up business partner properties in the business partner properties master data table. There are 64 properties. You can set the name of each property, and assign each property to a business partner as a flag. To see the list of properties, select Select Administration --> Setup --> Business Partners --> Business Partner Properties. Source table: OCQG

## Methods (6)
- `Public Function GetBusinessPartnerProperty(ByVal pIBusinessPartnerPropertyParams As BusinessPartnerPropertyParams) As BusinessPartnerProperty` Retrieves a business partner property. The business partner property is specified by its key (GroupCode), which is contained in the BusinessPartnerPropertyParams object passed to the method.
  - param `pIBusinessPartnerPropertyParams`: The key of the business partner property to retrieve.
  - returns: The business partner property with the specified key.
- `Public Function GetBusinessPartnerPropertyList() As BusinessPartnerPropertiesParams` Retrieves the keys and names of all the business partner properties.
  - C# example (from SAP's help):
    ```csharp
    try
    {
         BusinessPartnerPropertiesParams getParams;
         getParams = oBPPropSrv.GetBusinessPartnerPropertyList();

         String resultSet = "";

         foreach (BusinessPartnerPropertyParams record in getParams)
         {
              resultSet = resultSet + record.PropertyCode + "\t" + record.PropertyName + "\n";
         }
         Interaction.MsgBox(resultSet, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    catch (Exception ex)
    {
         Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As BusinessPartnerPropertiesServiceDataInterfaces) As Object` Creates an empty data structure for use with the BusinessPartnerPropertiesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `BusinessPartnerPropertiesServiceDataInterfaces` in `../enums/enums-02.md`
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
- `Public Sub UpdateBusinessPartnerProperty(ByVal pIBusinessPartnerProperty As BusinessPartnerProperty)` Updates an existing business partner property. The data for the business partner property, including the key of the business partner property to be updated, is contained in the BusinessPartnerProperty object passed to the method. To update a business partner property, you must first retrieve it using the GetBusinessPartnerProperty method.
  - param `pIBusinessPartnerProperty`: The data for the business partner property to be updated. The BusinessPartnerProperty object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    try
    {
         oBPPropSrv = (BusinessPartnerPropertiesService)(MainModule.oCmpSrv.GetBusinessService(ServiceTypes.BusinessPartnerPropertiesService));
         BusinessPartnerPropertyParams getLine;
         BusinessPartnerProperty updateLine;

         getLine = (BusinessPartnerPropertyParams)oBPPropSrv.GetDataInterface(BusinessPartnerPropertiesServiceDataInterfaces.bppsBusinessPartnerPropertyParams);

         // update
         getLine.PropertyCode = 5;
         updateLine = oBPPropSrv.GetBusinessPartnerProperty(getLine);
         updateLine.PropertyName = "New Value";
         oBPPropSrv.UpdateBusinessPartnerProperty(updateLine);
    }
    catch (Exception ex)
    {
         Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```

# BusinessPartnerProperty (Object)

Represents a business partner property that can be assigned to a business partner. Source table: OCQG Mandatory properties: PropertyName

## Properties (3)
- `Public Property PropertyCode() As Long` [R] The key for a specific business partner property. Field name: GroupCode
- `Public Property PropertyName() As String` [R/W] The name of the business partner property. Field name: GroupName
  - remarks: Cannot be blank.
- `Public Property UserFields() As Fields` [R] Get User Fields

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

# BusinessPartnerPropertyParams (Object)

Holds the key and name of a business partner property. This object is used to pass keys to and retrieve keys from BusinessPartnerPropertiesService methods.

## Properties (2)
- `Public Property PropertyCode() As Long` [R/W] The key for a specific business partner property. Field name: GroupCode
- `Public Property PropertyName() As String` [R] The name of the business partner property. Field name: GroupName

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

<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# PartnersSetupsService (Object)

The PartnersSetupsService service enables you to add, look up, update, and remove partners. Source table: OPRT.

**Remarks:** To open the Partners - Setup window, from the SAP Business One Main Menu, choose Administration --> Setup --> Sales Opportunities --> Partners.

## Methods (8)
- `Public Function Add(ByVal pIPartnersSetup As PartnersSetup) As PartnersSetupParams` Adds a partner.
  - param `pIPartnersSetup`: The data for the new partner.
- `Public Sub Delete(ByVal pIPartnersSetupParams As PartnersSetupParams)` Deletes an existing partner.
  - param `pIPartnersSetupParams`: The key of the partner to be deleted.
- `Public Function Get(ByVal pIPartnersSetupParams As PartnersSetupParams) As PartnersSetup` Retrieves a partner. The partner is specified by its key, which is contained in the PartnersSetupParams object passed to the method.
  - param `pIPartnersSetupParams`: The key of the partner to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As PartnersSetupsServiceDataInterfaces) As Object` Creates an empty data structure for use with the PartnersSetupsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `PartnersSetupsServiceDataInterfaces` in `../enums/enums-03.md`
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
- `Public Function GetList() As PartnersSetupsParams` Returns the PartnersSetupsParams data collection that identifies all partners.
- `Public Sub Update(ByVal pIPartnersSetup As PartnersSetup)` Updates an existing partner.
  - param `pIPartnersSetup`: The data for the partner to be updated. The PartnersSetup object must contain the key of the object to be updated.

# PathAdmin (Object)

An object for setting and getting directory paths for storing various files. Source tables: OADP

**Remarks:** To set paths in the application, go to Administration --> System Initialization --> General Settings --> Path tab.

**Example:**
- C# example (from SAP's help):
  ```csharp
  // Get the path admin object
  CompanyService com_service = DICompany.GetCompanyService();
  oPathAdmin = com_service.GetPathAdmin();

  // Set new paths
  oPathAdmin.WordTemplateFolderPath = "c:\Documnets\Templates\";
  oPathAdmin.PicturesFolderPath = "c:\Documnets\Pictures\";
  oPathAdmin.AttachmentsFolderPath = "c:\Documnets\Data\";
  oPathAdmin.ExtensionsFolderPath = "c:\Documnets\Extention\";

  // Update paths
  com_service.UpdatePathAdmin(oPathAdmin);
  ```

## Properties (5)
- `Public Property AttachmentsFolderPath() As String` [R/W] Sets or returns the path to the folder for storing attachments, such as customer Web pages. Field name: AttachPath
- `Public Property ExtensionsFolderPath() As String` [R/W] Sets or returns the path to the folder for storing secured images. Secured images include official stamps, which, due to legal requirements, can be saved on your computer as *.dll files only, and not in regular picture formats. Field name: ExtPath
- `Public Property PicturesFolderPath() As String` [R/W] Sets or returns the path to the folder for storing store images, such as company logos. Field name: BitmapPath
- `Public Property PrintId() As String` [R] The key for the set of path settings. For internal use. Field name: PrintId
- `Public Property WordTemplateFolderPath() As String` [R/W] Sets or returns the path to the folder for storing Microsoft Word templates when exporting data to Word. Field name: WordPath

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

# PaymentAmountParams (Object)

PaymentAmountParams Class

## Properties (10)
- `Public Property CashDiscountAmount() As Double` [R] property CashDiscountAmount
- `Public Property CashDiscountAmountFC() As Double` [R] property CashDiscountAmountFC
- `Public Property CashDiscountAmountSC() As Double` [R] property CashDiscountAmountSC
- `Public Property CashDiscountPercentage() As Double` [R] property CashDiscountPercentage
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property DocType() As PaymentInvoiceTypeEnum` [R] property DocType
- `Public Property InstallmentId() As Long` [R] property InstallmentId
- `Public Property TotalPaymentAmount() As Double` [R] property TotalPaymentAmount
- `Public Property TotalPaymentAmountFC() As Double` [R] property TotalPaymentAmountFC
- `Public Property TotalPaymentAmountSC() As Double` [R] property TotalPaymentAmountSC

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PaymentAmountParamsCollection (Collection)

PaymentAmountParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PaymentAmountParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PaymentAmountParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PaymentBlock (Object)

Represents the payment blocks. Source table: OPYB.

**Remarks:** If you use the payment wizard to automatically issue and create incoming and outgoing payments, there might be cases in which you would want to exclude a specific business partner from the payment run. For this purpose you assign a payment block that indicates the reason for the exclusion.

## Properties (2)
- `Public Property AbsEntry() As Long` [R] The internal key of a specific payment block. Field name: AbsEntry.
- `Public Property PaymentBlockCode() As String` [R/W] The reason for the payment block. Field name: PayBlock. Length: 50 characters.

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

# PaymentBlockParams (Object)

Holds the key and name to an existing payment block. This object is used to pass keys to and retrieve keys from PaymentBlocksService methods.

## Properties (2)
- `Public Property AbsEntry() As Long` [R/W] The internal key that identifies the payment block. Field name: AbsEntry.
- `Public Property PaymentBlockCode() As String` [R] The code of the payment block. Field name: PayBlock.

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

# PaymentBlocksParams (Collection)

A collection of PaymentBlockParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As PaymentBlockParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As PaymentBlockParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

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
  - enum: `PaymentBlocksServiceDataInterfaces` in `../enums/enums-03.md`
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

# PaymentBPCode (Object)

PaymentBPCode Class

## Properties (2)
- `Public Property BPCode() As String` [R/W] property BPCode
- `Public Property Date() As Date` [R/W] property Date

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PaymentCalculationService (Object)

PaymentCalculationService Class

## Methods (4)
- `Public Function GetDataInterface(ByVal enumMSDI As PaymentCalculationServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `PaymentCalculationServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetPaymentAmount(ByVal pIPaymentBPCode As PaymentBPCode, ByVal pIPaymentInvoiceEntries As PaymentInvoiceEntries) As PaymentAmountParamsCollection` GetPaymentAmount
  - param `pIPaymentBPCode`: 
  - param `pIPaymentInvoiceEntries`: 

# PaymentInvoiceEntries (Collection)

PaymentInvoiceEntries Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PaymentInvoiceEntry` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PaymentInvoiceEntry` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PaymentInvoiceEntry (Object)

PaymentInvoiceEntry Class

## Properties (4)
- `Public Property DocEntry() As Long` [R/W] property DocEntry
- `Public Property DocNum() As Long` [R] property DocNum
- `Public Property DocType() As PaymentInvoiceTypeEnum` [R/W] property DocType
- `Public Property InstallmentId() As Long` [R/W] property InstallmentId

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PaymentReasonCode (Object)

Source table: OPTR.

## Properties (1)
- `Public Property Code() As String` [R/W] Payment reason code. Field name: PymntRsnCd. Length: 3 characters.

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

# PaymentReasonCodeParams (Object)

PaymentReasonCodeParams Class

## Properties (1)
- `Public Property Code() As String` [R/W] Payment reason code. Field name: PymntRsnCd. Length: 3 characters.

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

# PaymentReasonCodeService (Object)

Source table: OPTR.

**Remarks:** For the Italy localization only. Navigation path 1: Administration → Setup → Financial → Tax → Withholding Tax, and go to the column Payment Reason Code. Navigation path 2: Business Partner Master Data → Accounting → Tax, select the checkbox Subject to Withholding Tax, choose the browser button next to the Specific WTax Amounts Setup field, and go to the column Payment Reason Code.

## Methods (7)
- `Public Function AddPaymentReasonCode(ByVal pIPaymentReasonCode As PaymentReasonCode) As PaymentReasonCodeParams` AddPaymentReasonCode
  - param `pIPaymentReasonCode`: 
- `Public Sub DeletePaymentReasonCode(ByVal pIPaymentReasonCodeParams As PaymentReasonCodeParams)` DeletePaymentReasonCode
  - param `pIPaymentReasonCodeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As PaymentReasonCodeServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `PaymentReasonCodeServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetPaymentReasonCode(ByVal pIPaymentReasonCodeParams As PaymentReasonCodeParams) As PaymentReasonCode` GetPaymentReasonCode
  - param `pIPaymentReasonCodeParams`: 
- `Public Function GetPaymentReasonCodeList() As PaymentReasonCodesParams` GetPaymentReasonCodeList

# PaymentReasonCodesParams (Collection)

PaymentReasonCodesParams Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As PaymentReasonCodeParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As PaymentReasonCodeParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# PaymentRunExport (Object)

PaymentRunExport is a business object that enables you to export data of automatic payments for both incoming payments and outgoing payments to vendors. The automatic payments data is generated by running the Payment Wizard in SAP Business One. The property type of all properties in this object is read-only. This object enables you to: - Retrieve a payment by its key. - Save the object in XML format. Source table: OPEX.

**Remarks:** To check whether or not the payment is closed, see the Status property. Mandatory fields in SAP Business One: None.

## Properties (97)
- `Public Property AdditionalIdNumber() As String` [R] Returns the additional ID number. Field name: AddIdNum. Length: 32 characters.
- `Public Property BankAccount() As String` [R] Returns the bank account to which the payment is posted. Field name: PymBnkAcct. Length: 50 characters.
- `Public Property BankCode() As String` [R] Returns the bank code of the payment. Field name: PayBnkCode. Length: 30 characters.
- `Public Property BankCountry() As String` [R] Returns the payment bank country. Field name: Country. Length: 3 characters.
- `Public Property BankIBAN() As String` [R] Returns the International Bank Account Number (IBAN). Field name: PymBnkIBAN. Length: 50 characters.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CollectionAuthorization() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not to verify the signature for each payment. Field name: CllctAutho.
  - remarks: In SAP Business One, during the payment run process, the system compares this value to the value in payment method. This option is available only for customers.
- `Public Property CompanyAddress() As String` [R] Returns the company address. Field name: CompAddres. Length: 254 characters.
- `Public Property CompanyBlock() As String` [R] Returns the company's block, part of company address. Field name: CompBlock. Length: 100 characters.
- `Public Property CompanyCity() As String` [R] Returns the company's city, part of company address. Field name: CompCity. Length: 100 characters.
- `Public Property CompanyCounty() As String` [R] Returns this payment company's county. Field name: CompCounty. Field name: . Length: 100 characters.
- `Public Property CompanyName() As String` [R] Returns the company name. Field name: . Length: 100 characters.
- `Public Property CompanyState() As String` [R] Returns this payment company's state. Field name: Compstate. Length: 3 characters. This is a foreign key to the OCST object.
- `Public Property CompanyStreet() As String` [R] Returns this payment company's street. Field name: CompStreet. Length: 100 characters.
- `Public Property CompanyTaxNum() As String` [R] Returns the company tax number. Field name: CompTaxNum. Length: 32 characters.
- `Public Property CompanyZipCode() As String` [R] Returns this payment company's zip code. Field name: CompZip. Length: 20 characters.
- `Public Property CompIsrBillerID() As String` [R] Returns the ID of the company ISR biller. Field name: CompISRBil. Length: 9 characters.
  - remarks: Country-specific property for Switzerland only.
- `Public Property Countery() As String` [R] Returns the country name (in short, for example: EU, USA). Field name: CompISRBil. Length: 3 characters.
- `Public Property Currency() As String` [R] Returns the main currency. Field name: Currency. Length: 3 characters.
- `Public Property CustomerNum() As String` [R] Returns the customer number. Field name: CustNum. Length: 15 characters.
- `Public Property DebitMemo() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not to send a debit memo. Field name: DebitMemo.
- `Public Property DocAmountForign() As Double` [R] Returns the payment document amount in foreign currency. Field name: PymDcAmtFC.
- `Public Property DocAmountLocal() As Double` [R] Returns the payment document amount in local currency. Field name: PymDocAmnt.
- `Public Property DocCashDiscount() As Double` [R] Returns the cash discount in payment document. Field name: PymCshDsct.
- `Public Property DocCashDiscountForign() As Double` [R] Returns the cash discount in payment document in foreign currency. Field name: PyCshDscFC.
- `Public Property DocCurrnecy() As String` [R] Returns the payment document currency. Field name: PymDocCurr. Length: 3 characters.
- `Public Property DocNum() As Long` [R] Returns the payment document number. Field name: PaymDocNum.
- `Public Property DocNumOffieldPaid() As Long` [R] Returns the number of paid items. Field name: PymNumOfPa.
- `Public Property DocRate() As Double` [R] Returns the payment document exchange rate. Field name: PymDocRate.
- `Public Property EUInternalTransfer() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not the total amount is smaller then 12,500.01 EUR, AND if both the business partner country and the company country belong to the European localization. Field name: EuInTrnsfr.
- `Public Property FilePath() As String` [R] Returns the destination path for the bank transfer file. Field name: FilePath. Length: 16 characters.
- `Public Property FiscalYear() As Date` [R] Returns the fiscal year (date type). Field name: FiscalYear.
- `Public Property FormatName() As String` [R] Returns the file format name for the payment run. Field name: FormatName. Length: 100 characters.
  - remarks: The value of this property is defined in SAP Business One in the Administration module (Define Payment Methods).
- `Public Property FreeText1() As String` [R] property FreeText1
- `Public Property FreeText2() As String` [R] property FreeText2
- `Public Property FreeText3() As String` [R] property FreeText3
- `Public Property GLAccount() As String` [R] Returns the General Ledger (G/L) account. Field name: PymGLAcct. Length: 15 characters.
- `Public Property InstructionKey() As String` [R] Returns the instruction key that is used as an additional indicator for the business partner. Field name: InstrucKey. Length: 30 characters.
- `Public Property Lines() As PaymentRunExport_Lines` [R] Returns the PaymentRunExport_Lines child object.
- `Public Property OrderingParty() As String` [R] Returns the ordering party. Field name: OrderParty. Length: 30 characters.
- `Public Property OrganizationNumber() As String` [R] Returns the organization number. Field name: CompOrgNum. Length: 50 characters.
- `Public Property PayeeBankAccount() As String` [R] Returns the payee bank account. Field name: PayBankAct. Length: 50 characters
- `Public Property PayeeBankBISR() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not to print the bank name and address on the BISR Invoice. Field name: PayBnkBISR.
  - remarks: Country-specific for Switzerland. The return value can be Yes, only when the House bank is defined.
- `Public Property PayeeBankBlock() As String` [R] Returns the block address of the payee bank. Field name: PayBnkBlck. Length: 100 characters.
- `Public Property PayeeBankBranch() As String` [R] Returns the payee bank branch. Field name: PayBnkBrnc. Length: 50 characters
- `Public Property PayeeBankCity() As String` [R] Returns the payee bank city. Field name: PayBnkCnty. Length: 100 characters
- `Public Property PayeeBankCode() As String` [R] Returns the payee bank code. Field name: PayBnkCode. Length: 30 characters
- `Public Property PayeeBankCountry() As String` [R] Returns the payee bank country. Field name: PayBnkCntr. Length: 3 characters
- `Public Property PayeeBankCounty() As String` [R] Returns the payee bank county. Field name: PayBnkCnty. Length: 100 characters
- `Public Property PayeeBankCtrlKey() As String` [R] Returns the payee bank control key. The control key is used when adding more than one branch or account for a bank Field name: PayBnkCtrl. Length: 2 characters.
- `Public Property PayeeBankHouseBank() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not to represent the bank, when defining the bank details, as the company bank. Field name: PayBnkHsBk.
- `Public Property PayeeBankIBAN() As String` [R] Returns the payee International Bank Account Number (IBAN). Field name: PayBnkIBAN. Length: 50 characters.
- `Public Property PayeeBankName() As String` [R] Returns the payee bank name. Field name: PayBnkName. Length: 32 characters
- `Public Property PayeeBankNextCheckNumber() As Long` [R] Returns the number of the next check. Field name: PayBnkChNo.
- `Public Property PayeeBankPostOffice() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not the post office serves as the payee bank. Field name: PayBnkPost.
- `Public Property PayeeBankState() As String` [R] Returns the payee bank state. Field name: PayBnkStat. Length: 3 characters
- `Public Property PayeeBankStreet() As String` [R] Returns the payee bank street. Field name: PayBnkStr. Length: 100 characters
- `Public Property PayeeBankSwiftNum() As String` [R] Returns the payee bank swift code. Field name: PayBnkSwif. Length: 50 characters.
- `Public Property PayeeBankUserNum1() As String` [R] Returns the payee bank user number 1 or password. User numbers 1 - 4 are used to identify a payment file for a certain account. Field name: PymBnkUsr1. Length: 25 characters.
- `Public Property PayeeBankUserNum2() As String` [R] Returns the payee bank user number 2 or password. User numbers 1 - 4 are used to identify a payment file for a certain account. Field name: PymBnkUsr2. Length: 25 characters.
- `Public Property PayeeBankUserNum3() As String` [R] Returns the payee bank user number 3 or password. User numbers 1 - 4 are used to identify a payment file for a certain account. Field name: PymBnkUsr3. Length: 25 characters.
- `Public Property PayeeBankUserNum4() As String` [R] Returns the payee bank user number 4 or password. User numbers 1 - 4 are used to identify a payment file for a certain account. Field name: PymBnkUsr4. Length: 25 characters.
- `Public Property PayeeBankZip() As String` [R] Returns the payee bank zip code. Field name: PayBankZip. Length: 20 characters
- `Public Property PayeeCity() As String` [R] Returns the payee city. Field name: PayeeCity. Length: 100 characters
- `Public Property PayeeCountry() As String` [R] Returns the payee country. Field name: PayCountry. Length: 3 characters
- `Public Property PayeeName() As String` [R] Returns the payee name. Field name: PayeeName. Length: 100 characters
- `Public Property PayeePostalCode() As String` [R] Returns the payee zip code. Field name: PayBnkPost. Length: 20 characters
- `Public Property PayeeReferenceDetails() As String` [R] Returns the payee reference details. Field name: PayRefDtls. Length: 20 characters.
- `Public Property PayeeState() As String` [R] Returns the payee state. Field name: PayeeState. Length: 3 characters
- `Public Property PayeeStreet() As String` [R] Returns the payee street. Field name: PayeeStree. Length: 100 characters
- `Public Property PayeeTaxNumber() As String` [R] Returns the payee tax number. Field name: PayeeTaxNo. Length: 32 characters.
- `Public Property PaymentBankBranch() As String` [R] Returns the payment bank branch. Field name: PymBnkBrnc. Length: 50 characters
- `Public Property PaymentBankCharges() As String` [R] Returns this payment bank charges. Field name: PymBCACode. Length: 3 characters. This is a foreign key to the OBCA object.
- `Public Property PaymentBankChargesAllocationCode() As String` [R] Returns the payment bank charges, allocation code. Field name: PymBCACode. Length: 3 characters. This is a foreign key to the Bank Charges Allocation Codes table (OBCA), not exposed through the DI API.
- `Public Property PaymentBankControlKey() As String` [R] Returns the payment bank control key. Field name: PayBnkCtrl. Length: 2 characters.
- `Public Property PaymentBankUserNo1() As String` [R] Returns the payment bank user number 1 or password. Field name: PymBnkUsr1. Length: 25 characters.
- `Public Property PaymentBankUserNo2() As String` [R] Returns the payment bank user number 2 or password. Field name: PymBnkUsr2. Length: 25 characters.
- `Public Property PaymentBankUserNo3() As String` [R] Returns the payment bank user number 3 or password . Field name: PymBnkUsr3. Length: 25 characters.
- `Public Property PaymentBankUserNo4() As String` [R] Returns the payment bank user number 4 or password. Field name: PymBnkUsr4. Length: 25 characters.
- `Public Property PaymentDonewithCheck() As BoYesNoEnum` [R] Determines whether or not this Payment Done with Check. Field name: CheckPmnt.
- `Public Property PaymentFormat() As String` [R] Returns the code of the file format for the payment run. Field name: PaymFormat. Length: 20 characters.
  - remarks: The value of this property is defined in SAP Business One in the Administration module (Define Payment Methods).
- `Public Property PaymentKeyCode() As String` [R] Returns the payment key code. Field name: PymKeyCode. Length: 6 characters.
- `Public Property PaymentMethod() As String` [R] Returns the payment method (check, bank transfer, etc.). Field name: PaymMethod. Length: 15 characters.
- `Public Property PaymentOrderNum() As Long` [R] property PaymentOrderNum
- `Public Property PostingDate() As Date` [R] Returns the posting date. Field name: PymPostDat.
- `Public Property RowType() As PaymentRunExportRowTypeEnum` [R] property RowType
- `Public Property RunDate() As Date` [R] Returns the date of the payment run. Field name: PayRunDate.
- `Public Property Status() As BoOpexStatus` [R] Returns a valid value of BoOpexStatus type that specifies the status, open or close, for each row in the payment run table (OPEX). Field name: Status.
- `Public Property UIPCode() As String` [R] property UIPCode
- `Public Property UserDepartment() As Long` [R] Returns the user department number. Field name: Department.
- `Public Property UserEMail() As String` [R] Returns the user e-mail. Field name: UserEmail. Length: 100 characters
- `Public Property UserFaxNumber() As String` [R] Returns the user fax number. Field name: UserFax. Length: 20 characters
- `Public Property UserMobilePhoneNumber() As String` [R] Returns the user mobile phone number. Field name: UserPortNo. Length: 50 characters
- `Public Property UserName() As String` [R] Returns the user name. Field name: UserName. Length: 30 characters
- `Public Property VendorIsrBillerID() As String` [R] Returns the ID of the vendor ISR biller. Field name: CompISRBil. Length: 9 characters.
  - remarks: Country-specific property for Switzerland.
- `Public Property VendorNum() As String` [R] Returns the vendor number. Field name: VendorNum. Length: 15 characters.
- `Public Property WizCode() As Long` [R] Returns the payment run ID (wizard code). Field name: PaymWizCod.

## Methods (4)
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal PaymentRunExportCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `PaymentRunExportCode`: Specifies the Payment Key Code (see PaymentKeyCode property).
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

# PaymentRunExport_Lines (Object)

PaymentRunExport_Lines is a child object of the PaymentRunExport object and represents the line entries of each payment. Source table: PEX1.

## Properties (32)
- `Public Property BPDebitPayableAccount() As String` [R] Returns the account of the business partner debtor/payable Field name: . Length: 15 characters.
- `Public Property Count() As Long` [R] Returns the total rows in the payment run.
- `Public Property CustomerNumber() As String` [R] Returns the customer number. Field name: CustNum. Length: 15 characters. This is a foreign key to the
- `Public Property DateOfPaymentRun() As Date` [R] Returns the date of the payment run. Field name: PayRunDate.
- `Public Property DocumentCurrency() As String` [R] Returns the document currency. Field name: DocCurr. Length: 3 characters.
- `Public Property DocumentLocalCurrency() As String` [R] Returns the document local currency. Field name: DocLocCurr. Length: 3 characters.
- `Public Property DocumentNumber() As Long` [R] Returns the Document Number of the payment in this line. Field name: DocNum.
- `Public Property DocumentObjectType() As Long` [R] Returns the document object type. Field name: ObjType. Length: 20 characters.
- `Public Property DocumentObjectTypeEx() As String` [R] Returns the document object type.
- `Public Property DocumentPaymentTerms() As Long` [R] Returns the document payment terms. Field name: DocPrmTerm. This is a foreign key to the PaymentTermsTypes Object.
- `Public Property DocumentPostingDate() As Date` [R] Returns the document posting date. Field name: DocDate.
- `Public Property DocumentRate() As Double` [R] Returns the document rate. Field name: DocRate.
- `Public Property DocumentRemarks() As String` [R] Returns the document remarks. Field name: DocRemarks. Length: 254 characters.
- `Public Property DocumentTaxAmount() As Double` [R] Returns the document tax amount in local currency. Field name: DocTaxAmnt.
- `Public Property DocumentTaxAmountFC() As Double` [R] Returns the document tax amount in foreign currency. Field name: DoxTxAmtFC.
- `Public Property DocumentTaxDate() As Date` [R] Returns the document tax date. Field name: TaxDate.
- `Public Property DocumentTotal() As Double` [R] Returns the document total in local currency. Field name: DocTotal.
- `Public Property DocumentTotalFC() As Double` [R] Returns the document total in foreign currency. Field name: DocTotalFC.
- `Public Property FiscalYear() As Date` [R] Returns the fiscal year (date type). Field name: FiscalYear.
- `Public Property FreeText1() As String` [R] property FreeText1
- `Public Property FreeText2() As String` [R] property FreeText2
- `Public Property FreeText3() As String` [R] property FreeText3
- `Public Property PaymentDocNum() As Long` [R] Returns the payment document number. Field name: DocNum.
- `Public Property PaymentDocReference() As String` [R] Returns the payment document reference. Field name: DocPymRef. Length: 27 characters.
- `Public Property PaymentMeans() As String` [R] Returns the payment method (check, bank transfer, etc.). Field name: PaymMethod. Length: 15 characters. This is a foreign key to the WizardPaymentMethods object.
- `Public Property PaymentNumber() As Long` [R] Returns the payment number. Field name: PymNum. Length: 11 characters.
- `Public Property PaymentOrderNum() As Long` [R] property PaymentOrderNum
- `Public Property PaymentTermsPeriod() As Long` [R] Returns the payment terms period. Field name: PymTermPer. Length: 15 characters.
- `Public Property PaymentWizardCode() As String` [R] Returns the payment run ID (wizard code). Field name: PaymWizCod. Length: 15 characters.
- `Public Property RowNumber() As Long` [R] Returns the current available row number (starts from 1). Field name: LineId.
- `Public Property VendorNumber() As String` [R] Returns the vendor code. Field name: VendorNum. Length: 15 characters.
- `Public Property VendorRefNum() As String` [R] Returns the vendor reference number. Field name: VendRefNum. Length: 16 characters.

## Methods (1)
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# Payments (Object)

Payments is a business object that represents payment methods in the Banking module. This object defines the incoming payments from customers and outgoing payments to vendors. Available payment methods are cash, credit cards, checks, or bank transfers. Source tables: ORCT (incoming payments) and OVPM (outgoing payments).

**Remarks:** Mandatory fields in SAP Business One: CardCode, CashSum, TransferAccount, and TransferSum. To display the form in the application: - For the ORCT table, select Banking --> Incoming Payments --> Incoming Payments. - For the OVPM table, select Banking --> Outgoing Payments --> Payments to Vendors.

## Properties (101)
- `Public Property AccountPayments() As Payments_Accounts` [R] Returns the Payments_Accounts object that represents the payments through account transfers.
- `Public Property Address() As String` [R/W] Sets or returns the Bill To address of the business partner. Field name: Address. Length: 254 characters.
  - remarks: Default value: Bill To address from BusinessPartners object.
- `Public Property ApplyVAT() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to apply a tax to this payment. Field name: ApplyVAT.
  - remarks: Country specific field for Singapore only. If set to tYES, you must specify the VatGroup property in Payments_Accounts child object.
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property AuthorizationStatus() As PaymentsAuthorizationStatusEnum` [R] Returns the status of the authorization for this payment. Field name: wddStatus.
- `Public Property BankAccount() As String` [R/W] Sets or returns the bank account number used for this payment. Field name: BankAcct. Length: 50 characters.
  - remarks: In SAP Business One, payments through accounts is used for payments to third-parties that are not part of your customers or vendors. Country-specific property for Poland.
- `Public Property BankChargeAmount() As Double` [R/W] Sets or returns the bank charge amount. Field name: BcgSum.
- `Public Property BankChargeAmountInFC() As Double` [R] Returns the bank charge amount in foreign currency. Field name: BcgSumFC.
- `Public Property BankChargeAmountInSC() As Double` [R] Returns the bank charge amount in system currency. Field name: BcgSumSy.
- `Public Property BankCode() As String` [R/W] Sets or returns the bank code for bank transfer. Field name: BankCode. Length: 30 characters.
  - remarks: In SAP Business One, payments through accounts is used for payments to third-parties that are not part of your customers or vendors. Country-specific property for Poland.
- `Public Property BillOfExchange() As BillOfExchange` [R] Returns the BillOfExchange object.
  - remarks: Country-specific property for Italy, Spain, and Portugal.
- `Public Property BillOfExchangeAgent() As String` [R/W] Sets or returns the code of the company employee responsible for the collection and management of bill of exchange transactions. Field name: BoeAgent. Length: 32 characters. This is a foreign key to the Agent Name table (OAGP), not exposed through the DI API).
  - remarks: Country-specific property for Italy, Spain, and Portugal.
- `Public Property BillOfExchangeAmount() As Double` [R/W] Sets or returns the total amount of payment using a Bill Of Exchange document in local currency. Field name: BoeSum.
  - remarks: Country-specific property for Italy, Spain, and Portugal.
- `Public Property BillOfExchangeAmountFC() As Double` [R] Returns the total amount of payment using a Bill Of Exchange document in foreign currency. Field name: BoeSumFc.
  - remarks: Country-specific property for Italy, Spain, and Portugal.
- `Public Property BillOfExchangeAmountSC() As Double` [R] Returns the total amount of payment using a Bill Of Exchange document in system currency. Field name: BoeSumSc.
  - remarks: Country-specific property for Italy, Spain, and Portugal.
- `Public Property BillofExchangeStatus() As BoBoeStatus` [R/W] Sets or returns a valid value of BoBoeStatus type that specifies the status of the Bill Of Exchange. Field name: BoeStatus.
  - remarks: Country-specific property for Italy, Spain, and Portugal.
- `Public Property BlanketAgreement() As Long` [R/W] property BlanketAgreement
- `Public Property BoeAccount() As String` [R/W] Sets or returns the control G/L account that is used in the Bill Of Exchange transactions. Field name: BoeAcc. Length: 15 characters.
  - remarks: Country-specific property for Italy, Spain, and Portugal.
- `Public Property BPLID() As Long` [R/W] property BPLID
- `Public Property BPLName() As String` [R] property BPLName
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Cancelled() As BoYesNoEnum` [R] Indicates whether the payment was cancelled.
- `Public Property CardCode() As String` [R/W] Sets or returns the business partner code or the account code. Field name: CardCode. Length: 15 characters. This is a foreign key to the BusinessPartnersService object.
  - remarks: Mandatory property. The card code is the primary key of business partners records in SAP Business One. Use this property to list, search, and display business partners records. When the payment is to/by an account, the property will contain the account number accordingly.
- `Public Property CardName() As String` [R/W] Sets or returns the business partner's full name. Field name: CardFName. Length: 100 characters.
  - remarks: You can use this property to represent company's name, organization name, person name, or any other entity that represents the business partner. Field name: CardName.
- `Public Property CashAccount() As String` [R/W] Sets or returns the cash G/L account used for this payment. Field name: CashAcct. Length: 15 characters.
- `Public Property CashSum() As Double` [R/W] Sets or returns the amount of cash in the current payment in local currency. Field name: CashSum. Mandatory property.
  - remarks: Use this property to record the payment amount in cash payments. The value must be positive or 0.
- `Public Property CashSumFC() As Double` [R] Returns the amount of cash in the current payment in foreign currency. Field name: CashSumFC.
- `Public Property CashSumSys() As Double` [R] Returns the amount of cash in the current payment in system currency. Field name: CheckSumSy.
- `Public Property CertificationNumber() As String` [R] property CertificationNumber
- `Public Property CheckAccount() As String` [R/W] Sets or returns the check G/L account used for this payment. Field name: CheckAcct. Length: 15 characters.
- `Public Property Checks() As Payments_Checks` [R] Returns the Payments_Checks child object that represents the payments through checks.
- `Public Property Cig() As Long` [R/W] property Cig
- `Public Property ContactPersonCode() As Long` [R/W] Sets or returns the contact person code of the specified business partner in this payment. Field name: CntctCode. This is a foreign key to the ContactEmployees object.
  - remarks: The default value is according to the value of ContactPerson property of the BusinessPartners object. You can choose only the contact person that belongs to the specified business partner.
- `Public Property ControlAccount() As String` [R/W] The control account for this document. Field name: BpAct This is a foreign key to the ChartOfAccounts object.
- `Public Property CounterReference() As String` [R/W] Sets or returns reference information about the payment. Field name: CounterRef. Length: 8 characters.
- `Public Property CreditCards() As Payments_CreditCards` [R] Returns the Payments_CreditCards child object that represents the payments through credit cards.
- `Public Property Cup() As Long` [R/W] property Cup
- `Public Property DeductionPercent() As Double` [R/W] Sets or returns the deduction percentage. Field name: DdctPrcnt.
  - remarks: Country-specific field for Israel.
- `Public Property DeductionSum() As Double` [R/W] Sets or returns the calculated deduction amount. Field name: DdctSum.
  - remarks: Country-specific field for Israel.
- `Public Property DocCurrency() As String` [R/W] Sets or returns the document code of the currency used in this payment. Field name: DocCurr. Length: 3 characters.
  - remarks: Valid values: local currency, system currency, card currency, or any other currency. For multi-currency the valid values are taken from the Currencies object.
- `Public Property DocDate() As Date` [R/W] Sets or returns the posting date of the payment document. Field name: VatDate.
  - remarks: Default date: system date. Valid values: not later than the system date.
- `Public Property DocEntry() As Long` [R] Returns the document entry key that uniquely identifies the payment document. Property type Read-only property " --> Field name: DocEntry.
- `Public Property DocNum() As Long` [R/W] Sets or returns the payment document number. Field name: DocNum.
  - remarks: This is a unique number (greater than 0) used as an entry key for identifying the payment document. Mandatory field in SAP Business One only in case the value of the HandWritten property is tYES. In case the value of HandWritten property is tNo, SAP Business One sets the next available number.
- `Public Property DocObjectCode() As BoPaymentsObjectType` [R/W] Sets or returns a valid value of BoPaymentsObjectType type that specifies the payments document type.
- `Public Property DocRate() As Double` [R/W] Sets or returns the exchange rate (greater than 0) related to the local currency. Field name: DocRate.
  - remarks: Mandatory in case the payment document does not use the local currency. You can get the recommended exchange rate using the GetCurrencyRate method.
- `Public Property DocType() As BoRcptTypes` [R/W] Sets or returns a valid value of BoRcptTypes type that specifies the payment recipient (replaces the DocTypte property). Field name: DocType.
- `Public Property DocTypte() As BoRcptTypes` [R/W] Sets or returns a valid value of BoRcptTypes type that specifies the payment recipient.
  - remarks: Note: This property is replaced by DocType, but remains in the collection due to backward compatibility.
- `Public Property DocumentReferences() As Payments_DocumentReferences` [R] property DocumentReferences
- `Public Property DueDate() As Date` [R/W] Sets or returns the due date of the check. Field name: DueDate.
- `Public Property ElectronicProtocols() As ElectronicProtocols` [R] property ElectronicProtocols
- `Public Property HandWritten() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this payment is based on a handwritten document. Field name: Handwrtten.
- `Public Property Invoices() As Payments_Invoices` [R] Returns the Payments_Invoices child object that represents the invoice data for this payment.
- `Public Property IsPayToBank() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether to specify the bank details or only the PaytoCode for the outgoing payment. Field name: IsPaytoBnk.
- `Public Property JournalRemarks() As String` [R/W] Sets or returns the remarks to the journal entry of this payment. Field name: . Length: 50 characters.
  - remarks: Default value is auto-completed when setting the CardCode property.
- `Public Property LocalCurrency() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the payment uses local currency. Field name: DiffCurr.
- `Public Property LocationCode() As Long` [R/W] Sets or returns the location code in incoming and outgoing payments. Applicable for cluster B. Field name: LocCode.
- `Public Property PaymentByWTCertif() As BoYesNoEnum` [R/W] property PaymentByWTCertif
- `Public Property PaymentPriority() As BoPaymentPriorities` [R/W] Sets or returns a valid value of BoPaymentPriorities type that specifies the payment priority. Field name: PaPriority.
- `Public Property Payments_ApprovalRequests() As Payments_ApprovalRequests` [R] Returns the Payments_ApprovalRequests object.
- `Public Property PaymentType() As BoORCTPaymentTypeEnum` [R/W] Sets or returns a valid value of Payment Type (Object Type). Field name: ObjType.
- `Public Property PayToBankAccountNo() As String` [R/W] Sets or returns the bank account number for the outgoing payment. Field name: PBnkAccnt. Length: 50 characters.
  - remarks: Relevant only if IsPaytoBank property is set to tYES.
- `Public Property PayToBankBranch() As String` [R/W] Sets or returns the bank branch for the outgoing payment. Field name: PBnkBranch. Length: 50 characters.
  - remarks: Relevant only if IsPaytoBank property is set to tYES.
- `Public Property PayToBankCode() As String` [R/W] Sets or returns the bank code for the outgoing payment. Field name: PBnkCode. Length: 30 characters.
  - remarks: Relevant only if IsPaytoBank property is set to tYES.
- `Public Property PayToBankCountry() As String` [R/W] Sets or returns the bank country for the outgoing payment. Field name: PBnkCnt. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
  - remarks: Relevant only if IsPaytoBank property is set to tYES.
- `Public Property PayToCode() As String` [R/W] Sets or returns the destination code for the outgoing payment. Field name: PayToCode. Length: 50 characters.
  - remarks: Relevant only if IsPaytoBank property is set to tNO.
- `Public Property PrimaryFormItems() As CashFlowAssignments` [R] property PrimaryFormItems
- `Public Property Printed() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not the payment document was printed. Field name: Printed.
- `Public Property PrivateKeyVersion() As Long` [R] property PrivateKeyVersion
- `Public Property Proforma() As BoYesNoEnum` [R/W] Returns a valid value of BoYesNoEnum type that specifies whether or not the payment refers to a Pro-Forma invoice. Field name: Proforma.
  - remarks: Country-specific field for Italy and Spain. Applies to outgoing payments to vendors only. A Pro-Forma invoice is a draft document sent to the company by a vendor who provides services, other than goods or items.
- `Public Property ProjectCode() As String` [R/W] Sets or returns the project code that the payment refers to. Field name: PrjCode. Length: 8 characters. This is a foreign key to the Projects table (OPRJ - not exposed through the DI API).
  - remarks: Editing project code in the Journal Entry header does not affect the project code assigned to Journal Entry lines. To enforce the change on the lines, you must set JournalEntries_Lines.ProjectCode.
- `Public Property Reference1() As String` [R/W] Sets or returns the first reference code of the payment. Field name: Ref1. Length: 11 characters.
  - remarks: Default value from DocNum property.
- `Public Property Reference2() As String` [R/W] Sets or returns the second reference code of the payment. Field name: Ref2. Length: 8 characters.
- `Public Property Remarks() As String` [R/W] Sets or returns the remarks to this payment. Field name: Comments. Length: 254 characters.
- `Public Property Series() As Long` [R/W] Sets or returns the auto-number series that generated the document number. Field name: Series. This is a foreign key to the Series object.
  - remarks: This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property SignatureDigest() As String` [R] property SignatureDigest
- `Public Property SignatureInputMessage() As String` [R] property SignatureInputMessage
- `Public Property TaxDate() As Date` [R/W] Sets or returns the date for the tax calculation or payment. Field name: TaxDate.
  - remarks: Default: current date retrieved from the system server. This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property TaxGroup() As String` [R/W] Sets or returns the VAT group. Field name: VatGroup. Length: 8 characters. This is a foreign key to the VatGroups object.
  - remarks: The VAT groups are defined in SAP Business One and stored in the OVTG table, which is not exposed by the DI API. Country-specific for Europe. Source code !UNRECOGNISED ELEMENT TYPE 'sourcecode'! " -->Example!UNRECOGNISED ELEMENT TYPE 'filtereditemlist'!" -->See Also !UNRECOGNISED ELEMENT TYPE 'filtereditemlist'! " -->
- `Public Property TransactionCode() As String` [R/W] Sets or returns the transaction code of incoming payment. Field name: TransCode. This is a foreign key to the Journal Entry Codes table (OTRC), not exposed through the DI API).
- `Public Property TransferAccount() As String` [R/W] Sets or returns the G/L account number for the payment Transfer Account. Field name: TrsfrAcct. Length: 15 characters.
  - remarks: When using payments through a bank transfer, you must set also the TransferDate, TransferReference, and TransferSum properties.
- `Public Property TransferDate() As Date` [R/W] Sets or returns the date of the payment transfer to the bank. Field name: TrsfrDate.
  - remarks: In payments through bank transfer, also set the TransferReference and TransferSum properties. The transfer date must be within the same period of the DocDate property.
- `Public Property TransferRealAmount() As Double` [R/W] Sets or returns the Transfer Real Amount in payment document. Field name: TfrRealAmt. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia).
- `Public Property TransferReference() As String` [R/W] Sets or returns the reference information for the payment transfer to the bank. Field name: PaymentRef. Length: 27 characters.
  - remarks: In payments via bank transfer, also set the TransferDate and TransferSum properties.
- `Public Property TransferSum() As Double` [R/W] Sets or returns the total payments Transfer Amount. Field name: TrsfrSum. Mandatory property.
  - remarks: When using payments through a bank transfer, you must set also the TransferDate and TransferReference properties. The value must be positive.
- `Public Property UnderOverpaymentdifference() As Double` [R] Sets or returns the Under / Over payment Difference. Field name: UndOvDiff.
- `Public Property UnderOverpaymentdiffFC() As Double` [R] property UnderOverpaymentdiffFC
- `Public Property UnderOverpaymentdiffSC() As Double` [R] Sets or returns the Under / Overpayment Difference in System Currency. Field name: UndOvDiffS.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VatDate() As Date` [R/W] Sets or returns the Vat payment date (Document Date). Field name: TaxDate.
- `Public Property VATRegNum() As String` [R] property VATRegNum
- `Public Property WithholdingTaxCertificates() As WithholdingTaxCertificates` [R] property WithholdingCertificate
- `Public Property WithholdingTaxDataWTX() As WithholdingTaxDataWTX` [R] property WithholdingTaxDataWTX
- `Public Property WTAccount() As String` [R] Returns the withholding account. Field name: WtAccount. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
  - remarks: Country-specific property for Germany, Switzerland, Netherlands, Norway, Finland, Denmark, Austria, UK, Sweden, Spain, Italy, India, and Portugal. For India localizations, if this property is set to yes, then the TaxId0 property of the BPFiscalTaxID object is mandatory and must be set to a 10-character value.
- `Public Property WTAmount() As Double` [R/W] Sets or returns the total withholding tax amount (in local currency) related to the payment. Field name: WtSum.
  - remarks: Applies to payments to vendors only. To set this property you must first set the WTCode property as defined in the Withholding Tax Code definition in SAP Business One. WTAmount = WTTaxableAmount * tax rate as defined for the WTCode. Country-specific property for Germany, Switzerland, Netherlands, Norway, Finland, Denmark, Austria, UK, Sweden, Spain, Italy, and Portugal.
- `Public Property WTAmountFC() As Double` [R] Returns the total withholding tax amount (in foreign currency) related to the payment. Field name: WtSumFrgn.
- `Public Property WTAmountSC() As Double` [R] Returns the total withholding tax amount (in system currency) related to the payment. Field name: WtSumSys.
- `Public Property WtBaseSum() As Double` [R/W] Sets or returns the Base sum for vat calculation. Field name: WtBaseSum.
- `Public Property WtBaseSumFC() As Double` [R] Sets or returns the Withholding Tax Base Sum in Foreign Currency. Field name: WtBaseSumF.
- `Public Property WtBaseSumSC() As Double` [R] Sets or returns the Withholding Tax Base Sum in System Currency. Field name: WtSumSys.
- `Public Property WTCode() As String` [R/W] Sets or returns the withholding tax code assigend to the payment. Length: 4 characters. This is a foreign key to WithholdingTaxCodes object. Field name: WtCode.
- `Public Property WTTaxableAmount() As Double` [R] Returns the withholding taxable amount of the payment. Field name: WtBaseAmnt.
  - remarks: Applies to payments to vendors only. The default value of WTTaxableAmount property depends on the Base Amount percentage as defined for the specified WTCode. Country-specific property for Germany, Switzerland, Netherlands, Norway, Finland, Denmark, Austria, UK, Sweden, Spain, Italy, and Portugal.

## Methods (13)
- `Public Function Add() As Long` Adds a new Payment object to SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Cancel() As Long` Cancels a payment transaction. The cancellation date of the transaction is the original document date.
- `Public Function CancelbyCurrentSystemDate() As Long` method CancelbyCurrentSystemDate
- `Public Function Close() As Long` Closes a record of the object in SAP Business One database.
  - example note: The following sample shows how to close a document record. Use this sample as a basis to all business objects of document type (not master data type).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Sub CloseDocument()

        Dim RetVal    As Long

        Dim ErrCode   As Long

        Dim ErrMsg    As String

        Dim vOrder As SAPbobsCOM.Documents

        Set vOrder = vCmp.GetBusinessObject(oOrders)

        'Retrieve the document record to close from the database

        RetVal = vOrder.GetByKey("55")

        If RetVal <> 0 Then

            vCmp.GetLastError ErrCode, ErrMsg

            MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

                Exit Sub

        End If

        'Close the record

        RetVal = vOrder.Close

        If RetVal <> 0 Then

            vCmp.GetLastError ErrCode, ErrMsg

            MsgBox "Failed to Close the record " & ErrCode & " " & ErrMsg

        End If

    End Sub
    ```
- `Public Function GetApprovalTemplates() As Long` Gets the related approval template.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal RctEntry As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `RctEntry`: Specifies the document entry key (DocEntry).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Function RequestApproveCancellation() As Long` method RequestApproveCancellation
- `Public Function SaveDraftToDocument() As Long` Converts an approved draft document to a valid document.
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

# Payments_Accounts (Object)

Payments_Accounts is a child object of the Payments object and represents the payments through account transfers in the Banking module. Source tables: RCT4 (incoming payments) and VPM4 (outgoing payments).

**Remarks:** Mandatory fields in SAP Business One: AccountCode and SumPaid. For account segmentation add the string _SYS00. To display the form in the application: - For RCT4 table, select Banking --> Incoming Payments --> Incoming Payments. - or - For VPM4 table, select Banking --> Outgoing Payments --> Payments to Vendors. - Select Account document type (instead of Customer or Vendor).

## Properties (18)
- `Public Property AccountCode() As String` [R/W] Sets or returns the G/L account code of the business partner as defined in Chart of Accounts. Field name: AcctCode. Mandatory property. Length: 15 characters. This is a foreign key to the ChartOfAccounts Object.
  - remarks: To set the AccountCode value when working with segmentation, use the FormatCode to find its key value (for example, _SYS00000000010) as follows: 1. Find the account key using the method GetObjectKeyBySingleValue. 2. Use the returned Recordset to retrieve the value of the key (for example, _SYS00000000010).
- `Public Property AccountName() As String` [R/W] Returns the G/L account name of the business partner as defined in Chart of Accounts. Field name: AcctName. Length: 100 characters.
- `Public Property Count() As Long` [R] Returns the number of lines in this document.
- `Public Property Decription() As String` [R/W] Sets or returns a description about the account. Field name: Descrip. Length: 250 characters.
- `Public Property EqualizationVatAmount() As Double` [R] Equalization tax amount. Field name: EquVatSum
  - remarks: For Spain only.
- `Public Property GrossAmount() As Double` [R/W] Sets or returns this payment account Gross amount. Field name: GrossAmnt
- `Public Property LineNum() As Long` [R] Returns the number of the current line. Field name: LineId.
- `Public Property LocationCode() As Long` [R] Returns the location code in incoming and outgoing payments. Applicable for cluster B. Field name: LocCode.
- `Public Property ProfitCenter() As String` [R/W] A distribution rule for dimension 1. Field name: OcrCode Length: 8 characters. This is a foreign key to the DistributionRule object.
- `Public Property ProfitCenter2() As String` [R/W] A distribution rule for dimension 2. Field name: OcrCode2 Length: 8 characters. This is a foreign key to the DistributionRule object.
- `Public Property ProfitCenter3() As String` [R/W] A distribution rule for dimension 3. Field name: OcrCode3 Length: 8 characters. This is a foreign key to the DistributionRule object.
- `Public Property ProfitCenter4() As String` [R/W] A distribution rule for dimension 4. Field name: OcrCode4 Length: 8 characters. This is a foreign key to the DistributionRule object.
- `Public Property ProfitCenter5() As String` [R/W] A distribution rule for dimension 5. Field name: OcrCode5 Length: 8 characters. This is a foreign key to the DistributionRule object.
- `Public Property ProjectCode() As String` [R/W] Sets or returns the project code. Field name: Project. Length: 8 characters. This is a foreign key to the OPRJ object.
- `Public Property SumPaid() As Double` [R/W] Sets or returns the amount paid. Field name: SumApplied. Mandatory property.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VatAmount() As Double` [R/W] Sets or returns the VAT amount of incoming or outgoing payments. Field name: VatAmnt.
- `Public Property VatGroup() As String` [R/W] Sets or returns the VAT group for this payment. Field name: VatGroup. Length: 8 characters. This is a foreign key to the VatGroups object.
  - remarks: The VAT group specifies how much VAT the payment is liable to.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# Payments_ApprovalRequests (Object)

Payments_ApprovalRequests is a child object of the Payments object. You can set the remarks field of the approval request. Source table: OWDDV.

## Properties (5)
- `Public Property ActiveForUpdate() As BoYesNoEnum` [R] property ActiveForUpdate
- `Public Property ApprovalTemplatesID() As Long` [R] The ID of the approval template. Field: WtmCode.
- `Public Property ApprovalTemplatesName() As String` [R] property ApprovalTemplatesName
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.
- `Public Property Remarks() As String` [R/W] Remarks made by the originator that are included with the approval request. Field: Remarks. Length: 100 characters.

## Methods (1)
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# Payments_Checks (Object)

Represents checks that are tied to an outgoing payment document. Checks that are not tied to a document are represented by the ChecksforPayment object. Source tables: RCT1 (incoming payments) and VPM1 (outgoing payments).

**Remarks:** Mandatory fields in SAP Business One: BankCode and CheckSum. To display the form in the application: - For RCT1 table, select Sales - A/R --> A/R Invoice. - or - For VPM1 table, select Purchasing - A/P --> A/P Invoice. - On the toolbar, click the Payment Means icon (or press CTRL+Y). - Select the Check tab.

## Properties (20)
- `Public Property AccounttNum() As String` [R/W] Sets or returns the bank account number of the check. Field name: AcctNum. Length: 50 characters.
- `Public Property BankCode() As String` [R/W] Sets or returns the bank code of the check. Field name: BankCode. Mandatory property. Length: 30 characters.
- `Public Property Branch() As String` [R/W] Sets or returns the branch name of the bank. Field name: Branch. Length: 50 characters.
- `Public Property CheckAbsEntry() As Long` [R] Returns the absolute entry of this Check. Field name: CheckAbs. This is a foreign key to the Payments Object
- `Public Property CheckAccount() As String` [R/W] Sets or returns the G/L account associated with this Check Account. Field name: CheckAct. Length: 15 characters.
- `Public Property CheckNumber() As Long` [R/W] Sets or returns this check number. Field name: CheckNum.
- `Public Property CheckSum() As Double` [R/W] Sets or returns the amount of the check. Mandatory property. Field name: CheckSum.
- `Public Property Count() As Long` [R] Returns the number of checks in this payment.
  - remarks: The value of this property updates automatically, after you add new lines to the document.
- `Public Property CountryCode() As String` [R/W] Sets or returns the country code of the bank. Field name: CountryCod. Length: 3 characters. This is a foreign key to the Countries table (OCRY) - not exposed through the DI API.
  - remarks: You can set any country code that is defined in the Countries table in SAP Business One.
- `Public Property Details() As String` [R/W] Sets or returns a description of the check. Field name: Details. Length: 254 characters.
- `Public Property DueDate() As Date` [R/W] Sets or returns the due date of the check. Field name: DueDate.
- `Public Property ECheck() As BoYesNoEnum` [R/W] Specify whether the account is relevant for e-check functionality or not. Field name: ECheck.
- `Public Property EndorsableCheckNo() As Long` [R/W] property EndorsableCheckNo
- `Public Property Endorse() As BoYesNoEnum` [R/W] property Endorse
- `Public Property FiscalID() As String` [R/W] property FiscalID
- `Public Property LineNum() As Long` [R] Returns the number of the current line in the document. Field name: LineID.
- `Public Property ManualCheck() As BoYesNoEnum` [R/W] Indicates that the check number was entered manually. Field name: ManualChk
- `Public Property OriginallyIssuedBy() As String` [R/W] property OriginallyIssuedBy
- `Public Property Trnsfrable() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the check can be transferred to a third-party. Field name: Trnsfrable.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# Payments_CreditCards (Object)

Payments_CreditCards is a child object of the Payments object and represents the payments by credit cards in the Banking module. Source tables: RCT3 (incoming payments) and VPM3 (outgoing payments).

**Remarks:** Mandatory fields in SAP Business One: CardValidUntil, CreditCard, CreditCardNumber, and CreditSum. To display the form in the application: - For RCT3 table, select Sales - A/R --> A/R Invoice. - or - For VPM3 table, select Purchasing - A/P --> A/P Invoice. - On the toolbar, click the Payment Means icon. - Select the Credit Card tab.

## Properties (20)
- `Public Property AdditionalPaymentSum() As Double` [R/W] Sets or returns the payment amount added to the first payment, due to rounding results. Field name: AddPmntSum.
  - remarks: SAP Business One uses the amount due, number of payments, and first partial payment amount to calculate the amount that is to be paid with the further payments. Rounding results are added to the first payment.
- `Public Property CardValidUntil() As Date` [R/W] Sets or returns the credit card expiration date. Mandatory property. Field name: CardValid.
- `Public Property ConfirmationNum() As String` [R/W] Sets or returns the confirmation number for the payment through a credit card. Field name: ConfNum. Length: 20 characters.
- `Public Property Count() As Long` [R] Returns the number of lines in this document.
  - remarks: The value of this property increases automatically, after you add lines to the document.
- `Public Property CreditAcct() As String` [R/W] Sets or returns the credit account number. Field name: CreditAcct. Length: 15 characters.
- `Public Property CreditCard() As Long` [R/W] Sets or returns the key of a credit card. Mandatory property. Field name: CreditCard. This is a foreign key to the CreditCards object.
- `Public Property CreditCardNumber() As String` [R/W] Sets or returns the credit card number. Field name: CrCardNum. Mandatory property. Length: 20 characters.
- `Public Property CreditSum() As Double` [R/W] Sets or returns the total payment amount. Mandatory property. Field name: CreditSum.
  - remarks: Credit card payment can be divided into several installments. The AdditionalPaymentSum property represents any additional installments. For the first payment, use the FirstPaymentSum property. The total number of payments is set in the NumOfPayments property, and the total payment amount is set in the CreditSum property.
- `Public Property CreditType() As BoRcptCredTypes` [R/W] Sets or returns a valid value of BoRcptCredTypes type that specifies the way for providing the credit card details (directly or by phone). Field name: CreditType.
- `Public Property FirstPaymentDue() As Date` [R/W] Sets or returns the due date of the first payment. Field name: FirstDue.
  - remarks: Applies only if the payment method allows partial payments.
- `Public Property FirstPaymentSum() As Double` [R/W] Sets or returns the amount of the first payment, when the transaction is divided to installments. Field name: FirstSum.
  - remarks: Credit card payment can be divided into several installments. The AdditionalPaymentSum property represents any additional installments. For the first payment, use the FirstPaymentSum property. The total number of payments is set in the NumOfPayments property, and the total payment amount is set in the CreditSum property. Applies only if the payment method allows partial payments.
- `Public Property LineNum() As Long` [R] Returns the number of the current line. Field name: LineID.
- `Public Property NumOfCreditPayments() As Long` [R/W] Sets or returns the number of payments through the credit card. Field name: NumOfPmnts.
- `Public Property NumOfPayments() As Long` [R/W] Sets or returns the number of installments. Field name: NumOfPmnts.
  - remarks: Credit card payment can be divided into several installments. The AdditionalPaymentSum property represents any additional installments. For the first payment, use the FirstPaymentSum property. The total number of payments is set in the NumOfPayments property, and the total payment amount is set in the CreditSum property. Applies only if the payment method allows partial payments.
- `Public Property OwnerIdNum() As String` [R/W] Sets or returns the ID number of the credit card owner. Field name: OwnerIdNum. Length: 15 characters.
- `Public Property OwnerPhone() As String` [R/W] Sets or returns the phone number of the credit card owner. Field name: OwnerPhone. Length: 50 characters.
- `Public Property PaymentMethodCode() As Long` [R/W] Sets or returns the key of the credit payment method. Field name: CrTypeCode. This is a foreign key to the CreditPaymentMethods object.
- `Public Property SplitPayments() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to split the payment for the transaction into separate rows. Field name: SpiltCred.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VoucherNum() As String` [R/W] Sets or returns the number of the credit document. Field name: VoucherNum. Length: 20 characters.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# Payments_DocumentReferences (Object)

Payments_DocumentReferences Class

## Properties (9)
- `Public Property Count() As Long` [R] property Count
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property ExternalReferencedDocNumber() As String` [R/W] property ExternalReferencedDocNumber
- `Public Property IssueDate() As Date` [R/W] property IssueDate
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property ReferencedDocEntry() As Long` [R/W] property ReferencedDocEntry
- `Public Property ReferencedDocNumber() As Long` [R] property ReferencedDocNumber
- `Public Property ReferencedObjectType() As ReferencedObjectTypeEnum` [R/W] property ReferencedObjectType
- `Public Property Remark() As String` [R/W] property Remark

## Methods (3)
- `Public Sub Add()` method Add
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 

# Payments_Invoices (Object)

Payments_Invoices is a child object of the Payments object and represents the invoices related to the payments in the Banking module. Source tables: RCT2 (incoming payments) and VPM2 (outgoing payments).

**Remarks:** Mandatory field in SAP Business One: DocEntry. To display the form in the application: - For RCT2 table, select Banking --> Incoming Payments --> Incoming Payments. - For VPM2 table, select Banking --> Outgoing Payments --> Payments to Vendors.

## Properties (24)
- `Public Property AppliedFC() As Double` [R/W] Sets or returns the amount paid in foreign currency. Field name: AppliedFC.
  - remarks: If the invoice does not use foreign currency, enter 0 in this field.
- `Public Property Count() As Long` [R] Returns the number of lines in this document.
  - remarks: The value of this property increases automatically, after adding a new line to the document.
- `Public Property DiscountPercent() As Double` [R/W] Sets or returns the discount percentage you specify for a customer, or the discount percentage a supplier specifies for you. Field name: Discount. Sets or returns the discount percentage you specify for a customer, or the discount percentage a supplier specifies for you. Field name: Discount.
  - remarks: The default value is retrieved from DiscountPercent property of the BusinessPartners object. You can update the value of the DiscountPercent property only in sales quotations, sales orders, purchase quotations, and purchase orders. This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types. The default value is retrieved from DiscountPercent property of the BusinessPartners object. You can update the value of the DiscountPercent property only in sales quotations, sales orders, purchase quotations, and purchase orders. This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types. This property is not relevant when using Down Payment.
- `Public Property DistributionRule() As String` [R/W] The distribution rule for dimension 1 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode This is a foreign key to the DistributionRule object.
- `Public Property DistributionRule2() As String` [R/W] The distribution rule for dimension 2 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode2 This is a foreign key to the DistributionRule object.
- `Public Property DistributionRule3() As String` [R/W] The distribution rule for dimension 3 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode3 This is a foreign key to the DistributionRule object.
- `Public Property DistributionRule4() As String` [R/W] The distribution rule for dimension 4 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode4 This is a foreign key to the DistributionRule object.
- `Public Property DistributionRule5() As String` [R/W] The distribution rule for dimension 5 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode5 This is a foreign key to the DistributionRule object.
- `Public Property DocEntry() As Long` [R/W] Sets or returns the invoice key. Mandatory property. Field name: DocEntry. This is a foreign key to the Documents object.
  - remarks: You can use this key to as a reference to an invoice.
- `Public Property DocLine() As Long` [R/W] Sets or returns the row key in the invoice document. Field name: DocLine.
- `Public Property DocNum() As Long` [R] Document number. Field name: DocNum.
- `Public Property InstallmentId() As Long` [R/W] Sets or returns the installment ID of the invoice payment. Field name: InstId.
- `Public Property InvoiceType() As BoRcptInvTypes` [R/W] Sets or returns a valid value of BoRcptInvTypes type that specifies the invoice type (incoming payment, tax invoice, correction invoice, and so on). Field name: InvType. Length: 20 characters.
- `Public Property LineNum() As Long` [R] Returns the active row number. Field name: DocLine.
- `Public Property LinkDate() As Date` [R] Returns the date when the payment was connected to the invoice. Field name: DpmPosted.
  - remarks: Country-specific for Poland only. This property is used when a payment is made before receiving the invoice. For example, when a payment is made upon a proforma invoice and the invoice is received later.
- `Public Property PaidSum() As Double` [R] Returns the amount (of the invoice) paid that applies to the 1099 report. Field name: PaidSum.
  - remarks: Country-specific field for US.
- `Public Property SumApplied() As Double` [R/W] Sets or returns the amount (of the invoice) paid. Field name: SumApplied.
- `Public Property TotalDiscount() As Double` [R/W] The total discount (from the cash discount settings) in local currency. Field name: DcntSum
  - remarks: If TotalDiscount, DiscountPercent and SumApplied are provided, then DiscountPercent is recalculated. If DiscountPercent and SumApplied are provided, then TotalDiscount is calculated. If TotalDiscount and DiscountPercent are provided, then SumApplied is calculated. DiscountPercent is recalculated beause TotalDiscount has higher priority than DiscountPercent.
- `Public Property TotalDiscountFC() As Double` [R/W] The total discount (from the cash discount settings) in foreign currency. Field name: DcntSumFC
  - remarks: For more information on the business logic, see TotalDiscount.
- `Public Property TotalDiscountSC() As Double` [R] The total discount (from the cash discount settings) in system currency. Field name: DcntSumSy
  - remarks: For more information on the business logic, see TotalDiscount.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WitholdingTaxApplied() As Double` [R] Returns the amount of the withholding tax that was applied for the invoice (in local currency). Field name: WtAppld.
  - remarks: The posting date of the withholding tax depends on the withholding category as defined in SAP Business One: - Payment Category: Withholding tax is posted upon payment. - Invoice Category: Withholding tax is posted upon invoice.
- `Public Property WitholdingTaxAppliedFC() As Double` [R] Returns the amount of the withholding tax that applied for the invoice (in foreign currency). Field name: WtAppldFC.
- `Public Property WitholdingTaxAppliedSC() As Double` [R] Returns the amount of the withholding tax that applied for the invoice (in system currency). Field name: WtAppldSC.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# PaymentTermsTypes (Object)

PaymentTermsTypes is a business object that represents the types of payment terms in the Banking module. The payment terms define typical agreements that apply to transactions with customers and vendors. This object enables you to: - Add a payment term type. - Retrieve a payment term type by its key. - Update a payment term type. - Remove a payment term type. - Save the object in XML format. Source table: OCTG.

**Remarks:** Mandatory field in SAP Business One: PaymentTermsGroupName. To display the form in the application: - Select Business Partners --> Business Partner Master Data. - Select Payment Terms tab. - Click the arrow to open the Define Payment Terms window.

## Properties (18)
- `Public Property BaselineDate() As BoBaselineDate` [R/W] Sets or returns a valid value of BoBaselineDate type that specifies the reference date for executing a payment transaction. Field name: BslineDate.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CreditLimit() As Double` [R/W] Sets or returns the maximum credit allowed. Field name: CredLimit.
  - remarks: SAP Business One validates the maximum credit value only if Credit Limit is selected in the Customer Activity Restrictions definitions (in Administrations -> System Initialization -> General Settings -> Sales). The value of this property is used as a default in the Business Partner master card and its related documents.
- `Public Property DiscountCode() As String` [R/W] Sets or returns the discount code (type) as defined in Cash Discount (based on the payment due date). Field name: DiscCode. Length: 20 characters. This is a foreign key to the Cash Discount table (OCDC), not exposed through the DI API.
- `Public Property DunningCode() As String` [R/W] Sets or returns the dunning code as defined in the Dunning System. The dunning code sets the type of interest calculation for late payments. Field name: DunningCod. Length: 20 characters. This is a foreign key to the Dunning Interest Rate table (ORIT), not exposed through the DI API.
- `Public Property GeneralDiscount() As Double` [R/W] Sets or returns the general discount percentage for the total amount in a document. Field name: VolumDscnt.
  - remarks: The value of this property is used as a default in the Business Partner master card and its related documents.
- `Public Property GroupNumber() As Long` [R] Returns the internal number, as assigned by the system, for the payment terms type. Field name: GroupNum.
- `Public Property InterestOnArrears() As Double` [R/W] Sets or returns the interest for late payments. The value of this property is for information only. Field name: LatePyChrg.
  - remarks: The value of this property is used as a default in the Business Partner master card and its related documents.
- `Public Property LoadLimit() As Double` [R/W] Sets or returns the maximum allowed debt (CreditLimit + Postdated Checks). Field name: ObligLimit.
  - remarks: The value of this property is used as a default in the Business Partner master card and its related documents.
- `Public Property NumberOfAdditionalDays() As Long` [R/W] Sets or returns the number of additional days for calculating the document due date. Field name: ExtraDays.
  - remarks: SAP Business One calculates the payment due date as follows: Payment due date = StartFrom + NumberOfAdditionalMonths + NumberOfAdditionalDays.
- `Public Property NumberOfAdditionalMonths() As Long` [R/W] Sets or returns the number of additional months for calculating the document due date. Field name: ExtraMonth.
  - remarks: SAP Business One calculates the payment due date as follows: Payment due date = StartFrom + NumberOfAdditionalMonths + NumberOfAdditionalDays.
- `Public Property NumberOfInstallments() As Long` [R] Returns the number of installments for the payment terms as defined in Installments in SAP Business One. Field name: InstNum.
  - remarks: Each installment creates as an exclusive record in payments, journal entries, reconciliations, and reports.
- `Public Property NumberOfToleranceDays() As Long` [R/W] Sets or returns the number of days earlier than the calculated due date to start expecting the payment. Field name: TolDays.
  - remarks: For example: If the payment due date is October 1, and the value of the Tolerance Days is 5, the payment is expected to be received starting from September 26.
- `Public Property OpenReceipt() As BoOpenIncPayment` [R/W] Sets or returns a valid value of BoOpenIncPayment type that specifies default means of payment from customers. OpenRcpt Field name: OpenRcpt.
- `Public Property PaymentTermsGroupName() As String` [R/W] Sets or returns the name of the payment terms type. Field name: PymntGroup. Length: 100 characters. Mandatory field in SAP Business One.
- `Public Property PriceListNo() As Long` [R/W] Sets or returns the Price List index to link to the business partner. Field name: ListNum. This is a foreign key to the PriceLists object.
  - remarks: The value of this property is used as a default in the Business Partner master card and its related documents.
- `Public Property StartFrom() As BoPayTermDueTypes` [R/W] Sets or returns a valid value of BoPayTermDueTypes type that specifies start time for calculating the payment due date. Field name: PayDuMonth.
  - remarks: SAP Business One calculates the payment due date as follows: Payment due date = StartFrom + NumberOfAdditionalMonths + NumberOfAdditionalDays.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (9)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal GroupNum As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `GroupNum`: Specifies the group number (see GroupNumber property).
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
- `Public Function UpdateWithBPs() As Long` method UpdateWithBPs

# PeriodCategory (Object)

The PeriodCategory object is a data structure related to the CompanyService. The PeriodCategory object provides two types of properties: - Properties that access existing Accounts and function as foreign keys to ChartOfAccounts Object. - Properties that defines new accounts by using Posting and Sub-Period definitions.

**Remarks:** Mandatory field in SAP Business One: PeriodCategory. To create a new period category through the application: - Select Administration --> System Initialization --> General Settings --> Posting Periods tab. - Click the New Period button. When creating a new period category, the system sets new G/L accounts related for this period category. To display the G/L Accounts related to the new period category: - Select Administration --> System Initialization --> General Settings --> Posting Periods tab. - Select the new period entry and then click the Set as Current button. - Select Administration --> Setup --> Financials --> G/L Account Determination.

## Properties (127)
- `Public Property AccountforCashReceipt() As String` [R/W] Sets or returns the code of the Cash Receipt account Field name: LinkAct_3. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property AccountforCreditMemoPayme() As String` [R/W] Sets or returns the code of the Credit Memo Payment account Field name: LinkAct_13. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property AccountforOutgoingChecks() As String` [R/W] Sets or returns the code of the Account for Outgoing Checks account. Field name: LinkAct_2. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property AcountforOpeningWHBalance() As String` [R/W] Sets or returns the code of the Acount for Opening WH Balance account. Field name: DftStockOB. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property AllocationAcc() As String` [R/W] Sets or returns the code of the AllocationAcc account. Field name: AlocCstAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property APCashDiscountAccount() As String` [R/W] Sets or returns the code of the A/P Cash Discount Account. Field name: LinkAct_19. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property APCashDiscountInterim() As String` [R/W] property APCashDiscountInterim
- `Public Property APExRateInterim() As String` [R/W] property APExRateInterim
- `Public Property APGainRealizedConversionDiff() As String` [R/W] Sets or returns the code of the A/P Gain Realized Conversion Diff. account. Field name: APConDiffG. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property APGainRealizedExchngeDif() As String` [R/W] Sets or returns the code of the A/P Gain Realized Exch. Diff. account. Field name: LinkAct_25. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property APLossCashDiscountAccount() As String` [R/W] Sets or returns the code of the A/P Loss Cash Discount Account. Field name: LinkAct_20. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property APLossRealizedConversionDiff() As String` [R/W] Sets or returns the code of the A/P Loss Realized Conversion Diff. account. Field name: APConDiffL. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property APLossRealizedExchangeDif() As String` [R/W] Sets or returns the code of the A/P Loss Realized Exch. account. Field name: LinkAct_21. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property ARCashDiscountAccount() As String` [R/W] Sets or returns the code of the A/R Cash Discount Account. Field name: LinkAct_22. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property ARCashDiscountInterim() As String` [R/W] property ARCashDiscountInterim
- `Public Property ARExRateInterim() As String` [R/W] property ARExRateInterim
- `Public Property ARGainRealizedConversionDiff() As String` [R/W] Sets or returns the code of the A/R Gain Realized Conversion Diff. account. Field name: ARConDiffG. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property ARGainRealizedExchngeDif() As String` [R/W] Sets or returns the code of the A/R Gain Realized Exchnge Dif.account. Field name: LinkAct_25. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property ARLossRealizedConversionDiff() As String` [R/W] Sets or returns the code of the A/R Loss Realized Conversion Diff. account. Field name: ARConDiffL. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property ARLossRealizedExchangeDi() As String` [R/W] Sets or returns the code of the A/R Loss Realized Exch. Diff. account. Field name: LinkAct_23. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property BeginningofFinancialYear() As Date` [R/W] Sets or returns the code of the A/P Gain Realized Exch. Diff.. account Field name: LinkAct_25. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property BillofExchangeAccountsRece() As String` [R/W] Sets or returns the code of the A/R Gain Realized Exch. Diff.. account Field name: LinkAct_26. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property BoEAccountsPayable() As String` [R/W] Sets or returns the code of the BoE Accounts Payable. account Field name: VAsstBoEPy. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property BoEAccountsPayable2() As String` [R/W] Sets or returns the code of the BoE Accounts Payable account. Field name: VAsstBoEPy. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property CommissionAccountDefault() As String` [R/W] Sets or returns the code of the Commission Account Default account. Field name: ComissAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property CostOfGoodsSold() As String` [R/W] Sets or returns the code of the Cost Of Goods Sold account. Field name: COGM_Act. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property CostofSaleRevaluationAcct() As String` [R/W] Sets or returns the code of the Cost of Sale Revaluation Acct. account Field name: CostRevAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property CostofSaleRevOffsetAcct() As String` [R/W] Sets or returns the code of the Cost of Sale Rev. Offset Acct account. Field name: CostOffAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property CreditorsFollowUpAccount() As String` [R/W] Sets or returns the code of the Creditors Follow-Up Account. Field name: LinkAct_10. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property CustBillofExchangeonC() As String` [R/W] Sets or returns the code of the Customer BoE on Collection. Field name: CBoEOnClct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property CustomerBillofExchangePres() As String` [R/W] Sets or returns the code of the Customer Bill of Exchange Pres account. Field name: CBoEPresnt. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property CustomerBillofExchngeDisc() As String` [R/W] Sets or returns the code of the Customer Bill of Exchange Disc account. Field name: CBoEDiscnt. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property CustomerDoubtfulDebtsAcct() As String` [R/W] Sets or returns the code of the Customer Doubtful Debts Acct account. Field name: COpenDebts. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property CustomerDownPaymentsAccount() As String` [R/W] Sets or returns the code of the Down Payment Sales Clearing Ac account. Field name: CDownPymnt. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property CustomersDeductionatSource() As String` [R/W] Sets or returns the code of the Customer's Deduction at Source account. Field name: LinkAct_6. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property CustomerUnpaidBoE() As String` [R/W] Sets or returns the code of the Customer Unpaid BoE. account Field name: CUnpaidBoE. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property DebitorsFollowUpAccount() As String` [R/W] Sets or returns the code of the Debitors Follow-Up Account. Field name: LinkAct_1. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property DecreaseGLAcc() As String` [R/W] Sets or returns the code of the BoE Accounts Payable account. Field name: VAsstBoEPy. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property DefaultSaleAccount() As String` [R/W] Sets or returns the code of the Default Sale Account account. Field name: DfltIncom. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property DownPaymentPClearingAcct() As String` [R/W] Sets or returns the code of the Down Payment Purchasing Clearing account. Field name: DpmPurAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property DownPaymentSClearingAcct() As String` [R/W] Sets or returns the code of the Down Payment Sales Clearing Ac account. Field name: DpmSalAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property DownPaymentVATAcctPurch() As String` [R/W] Sets or returns the code of the Down Payment VAT Acct Purchasing account. Field name: PurcVatOff. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property DownPaymentVATAcctSale() As String` [R/W] Sets or returns the code of the Down Payment VAT Acct Sales account. Field name: SaleVatOff. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property DunningFeeAccount() As String` [R/W] property DunningFeeAccount
- `Public Property DunningInterestAccount() As String` [R/W] property DunningInterestAccount
- `Public Property EOYControlAccount() As String` [R/W] Sets or returns the code of the EoY Control Account&. Field name: LinkAct_28. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property EUAccountsPayable() As String` [R/W] The EU accounts payable account. Field name: EUPayAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property EUAccountsReceivable() As String` [R/W] The EU accounts payable account. Field name: EURecvAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property EUExpenseAccount() As String` [R/W] Sets or returns the code of the EU Expense Account. Field name: ECExepnses. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property EUPurchaseCreditAcc() As String` [R/W] Sets or returns the code of the EU Purchase Credit Acct account. Field name: APCMEUAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property ExchangeRateDifferencesAcct() As String` [R/W] Sets or returns the code of the Exchange Rate Differences Acct account. Field name: ExDiffAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property ExemptedCredits() As String` [R/W] Sets or returns the code of the Tax Exempt Credits account. Field name: ARCMExpAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property ExhRatesDiffAcctLnWTax() As String` [R/W] property ExhRatesDiffAcctLnWTax
- `Public Property ExpenseAccountDefault() As String` [R/W] Sets or returns the code of the Expense Account Default account. Field name: DfltExpn. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property ExpenseClearingAccount() As String` [R/W] Sets or returns the code of the Expense Clearing Account. Field name: ExpClrAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property ExpenseOffsetAccount() As String` [R/W] Sets or returns the code of the Expense Offset Account. Field name: ExpOfstAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property ExpensesAccountForeign() As String` [R/W] Sets or returns the code of the Expenses Account Foreign account. Field name: ForgnExpn. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property ExpenseVarianceAccount() As String` [R/W] Sets or returns the code of the Expense Variance Account. Field name: ExpVarAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property FinancialYear() As Long` [R/W] Sets or returns the beginning of financial year date. Field name: FinancYear.
- `Public Property ForeignAccountsReceivables() As String` [R/W] Sets or returns the code of the Foreign Accounts Receivables account. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property ForeignPurchaseCreditAcc() As String` [R/W] Sets or returns the code of the Foreign Purchase Credit Acct account. Field name: APCMFrnAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property FromDocumentDate() As Date` [R/W] Sets or returns the code of the Document Date From account. Field name: F_TaxDate. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property FromDueDate() As Date` [R/W] Sets or returns the Due Date From of the account. Field name: F_DueDate. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property FromPostingDate() As Date` [R/W] Sets or returns the code of the Posting Date From account. Field name: F_RefDate. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property GLGainRealizedConversionDiff() As String` [R/W] Sets or returns the code of the G/L Gain Realized Conversion Diff. account. Field name: GLConDiffG. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property GLLossRealizedConversionDiff() As String` [R/W] Sets or returns the code of the G/L Gain Realized Conversion Diff. account. Field name: GLConDiffG. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property GLRevaluationOffsetAccount() As String` [R/W] Sets or returns the code of the G/L Revaluation Offset Account account. Field name: GlRvOffAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property GoodsClearingAcc() As String` [R/W] Sets or returns the code of the Goods Clearing Acct account. Field name: BalanceAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property IncreaseGLAccount() As String` [R/W] Sets or returns the code of the G/L Increase Acct account. Field name: IncresGlAc. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property InputTaxAccount() As String` [R/W] Sets or returns the code of the Input Tax Account. Field name: LinkAct_14. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property InventoryOffsetDecrease() As String` [R/W] Sets or returns the code of the Inventory Offset - Decrease account. Field name: DfltLoss. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property InventoryOffsetIncrease() As String` [R/W] Sets or returns the code of the Inventory Offset - Increase account. Field name: DfltProfit. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property InventoryOffsetProfitAndLossAccount() As String` [R/W] An offsetting account (contra-account) to an inventory account used within production transactions and for change of value of the inventory account during the production process. Field name: StockOffst. Length: 15 characters.
  - remarks: Apply for the Czech Republic, Hungary, and Slovakia localizations.
- `Public Property InvoicePaymentBP() As String` [R/W] Sets or returns the code of the Invoice and Payment BP account. Field name: DfltCard. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property NegativeInventoryAdjustmentAccount() As String` [R/W] Sets or returns the code of the Negative Stock Adjustment account. Field name: NegStckAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property NumberOfPeriods() As Long` [R/W] Sets or returns the Number Of Sub Periods defined in current account. Field name: PeriodNum.
- `Public Property OpeningBalancesAccount() As String` [R/W] Sets or returns the code of the Opening Balance Account. Field name: LinkAct_18. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property OutgoingCashAccount() As String` [R/W] Sets or returns the code of the Outgoing Cash Account. Field name: LinkAct_12. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property OutgoingChecksAccount() As String` [R/W] Sets or returns the code of the Account for Outgoing Checks. account Field name: LinkAct_2. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property OutgoingTaxAccount() As String` [R/W] Sets or returns the code of the outgoing tax account. Field name: LinkAct_5. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property OverpaymentsAPAccount() As String` [R/W] Sets or returns the code of the Overpayment A/P Account. Field name: OverpayAP. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property OverpaymentsARAccount() As String` [R/W] Sets or returns the code of the Overpayment A/P Account. Field name: OverpayAP. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property PeriodCategory() As String` [R/W] Sets or returns the Period Category of current account. Field name: PeriodCat. Length: 10 characters.
- `Public Property PeriodName() As String` [R/W] Sets or returns the PeriodName of the account. Field name: period. Length: 20 characters.
- `Public Property PriceDifferenceAccount() As String` [R/W] Sets or returns the code of the Price Difference Account. Field name: PricDifAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property PurchaseAccount() As String` [R/W] Sets or returns the code of the Purchase Account account. Field name: PurchseAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property PurchaseCreditAcc() As String` [R/W] Sets or returns the code of the Purchase Credit Acct. account Field name: APCMAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property PurchaseDownPaymentInterimAccount() As String` [R/W] The default G/L account for A/P down payments. When creating a vendor business partner, the DownPaymentInterimAccount property is automatically set to this account.
- `Public Property PurchaseInterimAcctLnWTax() As String` [R/W] property PurchaseInterimAcctLnWTax
- `Public Property PurchaseOffsetAccount() As String` [R/W] Sets or returns the code of the Purchase Offset Account. Field name: PaOffsetAc. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property PurchaseReturnAccount() As String` [R/W] Sets or returns the code of the Purchase Return Account. Field name: PaReturnAc. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property PurchaseTax() As String` [R/W] Sets or returns the code of the . This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property RateDifferencesDefaultAcc() As String` [R/W] Sets or returns the code of the Rate Differences Default Acct account. Field name: DfltRateDi. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property ReconciliationDifference() As String` [R/W] Sets or returns the code of the Reconciliation Difference account. Field name: LinkAct_27. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property RepomoAccount() As String` [R/W] Sets or returns the code of the Repomo Account. Field name: RepomoAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property RevenuesAccountForeign() As String` [R/W] Sets or returns the code of the Revenue Account Foreign account. Field name: ForgnIncm. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property RoundingAccount() As String` [R/W] Sets or returns the code of the Rounding Account account. Field name: LinkAct_24. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property SalesCreditAcc() As String` [R/W] Sets or returns the code of the Sales Credit Acct account. Field name: ARCMAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property SalesCreditEUAcc() As String` [R/W] Sets or returns the code of the Sales Credit EU Acct account. Field name: ARCMEUAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property SalesCreditForeignAcc() As String` [R/W] Sets or returns the code of the Sales Credit Foreign Acct account. Field name: ARCMFrnAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property SalesDownPaymentInterimAccount() As String` [R/W] The default G/L account for A/R down payments. When creating a customer business partner, the DownPaymentInterimAccount property is automatically set to this account.
- `Public Property SalesInterimAcctLnWTax() As String` [R/W] property SalesInterimAcctLnWTax
- `Public Property SalesReturns() As String` [R/W] Sets or returns the code of the Sales Returns account. Field name: RturnngAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property SalesRevenueEU() As String` [R/W] Sets or returns the code of the Sales Revenue - EU account. Field name: ECIncome. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property SelfInvoiceExpenseAccount() As String` [R/W] Sets or returns the code of the Self Invoice Expense Account. Field name: SlfInvExpn. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property SelfInvoiceRevenueAccount() As String` [R/W] Sets or returns the code of the Self Invoice Revenue Account. Field name: SlfInvIncm. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property StockAccount() As String` [R/W] Sets or returns the code of the Inventory Revaluation Account. Field name: StockRvAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property StockInTransitAccount() As String` [R/W] The stock in transit G/L account for this posting period.
- `Public Property StockRevaluationAccount() As String` [R/W] Sets or returns the code of the Inventory Revaluation Account . Field name: StockRvAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property StockRevaluationOffsetAcct() As String` [R/W] Sets or returns the code of the Inventory Revaluation Account. Field name: StockRvAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property SubPeriodType() As BoSubPeriodTypeEnum` [R/W] Sets or returns the sub period type of current account. Field name: SubType. Length: 1 characters.
  - remarks: Posible values are: - Y Year - Q Quarters - M Months - D Days
- `Public Property TaxDefinition() As String` [R/W] Sets or returns the code of the Tax Definition. Field name: LinkAct_15. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property TaxExemptRevenuesDefault() As String` [R/W] Sets or returns the code of the Tax-Exempt Revenue Default account. Field name: ExmptIncom. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property ToDocumentDate() As Date` [R/W] Sets or returns the code of the Document Date To account. Field name: T_TaxDate. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property ToDueDate() As Date` [R/W] Sets or returns the code of the Due Date To account. Field name: T_DueDate. Length: 15 characters.
- `Public Property ToPostingDate() As Date` [R/W] Sets or returns the code of the Posting Date To account. Field name: T_RefDate. Length: 8 characters.
- `Public Property UnderpaymentsAPAccount() As String` [R/W] Sets or returns the code of the Overpayment A/P Account. Field name: OverpayAR. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property UnderpaymentsARAccount() As String` [R/W] Sets or returns the code of the Underpayment A/R Account. Field name: UndrpayAR. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property VarianceAcc() As String` [R/W] Sets or returns the code of the Expense Variance Account. Field name: ExpVarAct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property VendorAssetsAccount() As String` [R/W] Sets or returns the code of the Vendor Assets Account. Field name: VAssets. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property VendorDoubtfulDebtsAcct() As String` [R/W] Sets or returns the code of the Vendor Doubtful Debts Acct account. Field name: VOpenDebts. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property VendorDownPaymentsAccount() As String` [R/W] Sets or returns the code of the Vendor Down Payments Account. Field name: VDownPymnt. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property WIPMappingCollection() As WIPMappingCollection` [R] property WIPMappingCollection
- `Public Property WIPMaterialAccount() As String` [R/W] Sets or returns the code of the WIP Material Variance Account. Field name: WipVarAcct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property WIPMaterialVarianceAccount() As String` [R/W] Sets or returns the code of the WIP Material Variance Account. Field name: WipVarAcct. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.
- `Public Property WipOffsetProfitAndLossAccount() As String` [R/W] An offsetting account (contra-account) to a WIP (work in progress) account used within production transactions and for change of value of the WIP account during the production process. Field name: WipOffset. Length: 15 characters.
  - remarks: Apply for the Czech Republic, Hungary, and Slovakia localizations.
- `Public Property WithholodingTax() As String` [R/W] Sets or returns the code of the Withholding Tax account. Field name: LinkAct_16. This is a foreign key to the ChartOfAccounts object. Length: 15 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML string that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.</p
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# PeriodCategoryParams (Object)

The PeriodCategoryParams specifies the identification key (AbsoluteEntry) for which the DocumentSeriesParams service is related. .

## Properties (1)
- `Public Property AbsoluteEntry() As Long` [R/W] Sets or return the key of the period category as assigned by the system when creating a new period category. Field name: AbsEntry.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# PeriodCategoryParamsCollection (Collection)

PeriodCategoryParamsCollection is a collection of PeriodCategoryParams identification keys.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of PeriodCategoryParams identification keys in the PeriodCategoryParamsCollection.

## Methods (5)
- `Public Function Add() As PeriodCategoryParams` Adds a new record to the table.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As PeriodCategoryParams` Returns a reference to an existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the PeriodCategoryParams in the collection.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# PickLists (Object)

The PickLists object supports the picking process of items from the warehouse. The picking process is applicable only for items that are already approved in sales orders. Source table: OPKL.

**Remarks:** To display the form in the application, select Inventory --> Pick and Pack --> Pick List.

## Properties (12)
- `Public Property AbsoluteEntry() As Long` [R] Returns the pick list number (sequential) as assigned by the system. Field name: AbsEntry.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Lines() As PickLists_Lines` [R] Returns the PickLists_Lines child object.
- `Public Property Name() As String` [R/W] Sets or returns the name of the employee who is responsible for the picking (picker). Field name: Name. Length: 30 characters.
- `Public Property ObjectType() As String` [R] Returns the type of the table (in this case OPKL). Field name: ObjType. Length: 20 characters.
- `Public Property OwnerCode() As Long` [R/W] Sets or returns the code of the user who prepares the pick list. This is a foreign key to the Users object (see InternalKey). Field name: OwnerCode. This is a foreign key to the Users object.
- `Public Property OwnerName() As String` [R] Returns the name of the user who prepares the pick list. Field name: OwnerName. Length: 30 characters.
- `Public Property PickDate() As Date` [R/W] Sets or returns the planned delivery date. Field name: PickDate.
- `Public Property Remarks() As String` [R/W] Sets or returns the remarks related to the pick list. Field name: Remarks. Length: 64,000 characters.
- `Public Property Status() As BoPickStatus` [R] Returns a valid value that specifies the status of the pick list. For example: released for picking, already picked, and so on. Field name: Status.
- `Public Property UseBaseUnits() As BoYesNoEnum` [R/W] property UseBaseUnits
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (9)
- `Public Function Add() As Long` method Add
  - remarks: Adds a pick list.
- `Public Function Close() As Long` Closes a record of the object in SAP Business One database.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
- `Public Function GetByKey(ByVal lAbsEntry As Long) As Boolean` Retrieves the values of the object's properties by the object's absolute key from the Company database. Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lAbsEntry`: AbsoluteEntry.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function GetReleasedAllocation(ByVal lAbsEntry As Long) As Boolean` GetReleasedAllocation
  - param `lAbsEntry`: 
- `Public Sub SaveToFile(ByVal bstrFileName As String)` Save the object to a file as XML data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub SaveXML(ByRef pbstrFileName As String)` Saves the object data to XML formatted data.
  - param `pbstrFileName`: Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates the object data in the company database.
- `Public Function UpdateReleasedAllocation() As Long` method UpdateReleasedAllocation

# PickLists_Lines (Object)

The PickLists_Lines is a child object of the PickLists object. Each line represents an order and its picking details in the pick list. Source table: PKL1.

**Remarks:** To display the form in the application: - Select Inventory --> Pick and Pack --> Pick List.

## Properties (14)
- `Public Property AbsoluteEntry() As Long` [R] Returns the identification key of the pick list row as assinged by SAP Business One when adding a new enrty. Field name: AbsEntry. This is a foreign key to the PickLists object.
- `Public Property BaseObjectType() As String` [R/W] Sets or returns the type of object on which the pick lists entry is based. Field name: BaseObject.
  - remarks: A pick list can be based on one of the following values: 17 - Sales orders. oOrders. 13 - Reserve invoices. oInvoices that their ReserveInvoice value is tYES.
- `Public Property BatchNumbers() As BatchNumbers` [R] property BatchNumbers
- `Public Property BinAllocations() As DocumentLinesBinAllocations` [R] property BinAllocations
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
- `Public Property LineNumber() As Long` [R] Returns the current row number in the pick list. Field name: PickEntry.
- `Public Property OrderEntry() As Long` [R/W] Sets or returns the number of the sales order. Field name: OrderEntry.
  - remarks: DocEntry of Documents(oOrders).
- `Public Property OrderRowID() As Long` [R/W] Sets or returns the LineNum in the document. Field name: OrderLine.
- `Public Property PickedQuantity() As Double` [R/W] Sets or returns the quantity of the items that were picked. Field name: PickQtty.
- `Public Property PickStatus() As BoPickStatus` [R] Returns a valid value that specifies the status of the order row in the pick list. Field name: PickStatus.
- `Public Property PreviouslyReleasedQuantity() As Double` [R] Returns the quantity of the items that were released in the previous pick. Field name: PrevReleas.
- `Public Property ReleasedQuantity() As Double` [R/W] Sets or returns the quantity of the items that were released. Field name: RelQtty.
- `Public Property SerialNumbers() As SerialNumbers` [R] property SerialNumbers
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new record to the PKL1 table.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# PM_ActivitiesCollection (Collection)

PM_ActivitiesCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PM_ActivityData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PM_ActivityData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PM_ActivityData (Object)

Source table: PMG6.

## Properties (4)
- `Public Property ActivityID() As Long` [R/W] property ActivityID
- `Public Property LineId() As Long` [R] property LineID
- `Public Property StageID() As Long` [R/W] property StageID
- `Public Property UserFields() As Fields` [R] property User Fields

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PM_DocAttachement (Object)

Source table: OPMG.AtcEntry.

## Properties (6)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property AttachementDate() As Date` [R/W] property AttachementDate
- `Public Property FileExtension() As String` [R/W] property FileExtension
- `Public Property FileName() As String` [R/W] property FileName
- `Public Property LineId() As Long` [R] property LineID
- `Public Property SourcePath() As String` [R/W] property SourcePath

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PM_DocAttachements (Collection)

PM_DocAttachements Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PM_DocAttachement` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PM_DocAttachement` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

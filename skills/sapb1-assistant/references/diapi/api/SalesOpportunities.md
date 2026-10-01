<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SalesOpportunities (Object)

SalesOpportunities is a business object that represents the sales opportunities data in SAP Business One. Sales opportunities include potential sale volumes that may arise from business with customers and interested parties. This object enables you to: - Add a sales opportunity. - Retrieve a sales opportunity by its key. - Update a sales opportunity with the progress of the sales activities and negotiations. - Remove a sales opportunity. - Save the object in XML format. Source table: OOPR.

**Remarks:** Mandatory fields in SAP Business One: CardCode and StartDate. To display the form in the application: - Select Sales Opportunities --> Sales Opportunity.

## Properties (55)
- `Public Property AttachmentEntry() As Long` [R/W] Sets or returns the identification key of the attachment file, as assigned by SAP Business One when adding an Attachment Entry to alert message. Field name: AtcEntry.
- `Public Property BPChanelCode() As String` [R/W] Sets or returns the distribution channel code for the sales opportunity. Field name: ChnCrdCode. Length: 15 characters. This is a foreign key to the BusinessPartners Object.
- `Public Property BPChanelName() As String` [R/W] Sets or returns the distribution channel card name for the sales opportunity. Field name: ChnCrdName. Length: 100 characters.
- `Public Property BPChannelContact() As Long` [R/W] Sets or returns the contact person of the distribution channel for the sales opportunity. Property type Read-write property " --> Field name: ChnCrdCon. This is a foreign key to the ContactEmployees Object.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CardCode() As String` [R/W] Sets or returns the business partner code. Mandatory property. Length: 15 characters. Field name: CardCode.
  - remarks: The type of the business partner code must be Lead or Customer (but not Vendor).
- `Public Property ClosingDate() As Date` [R/W] The closing date of the sales opportunity. Field name: CloseDate.
- `Public Property ClosingGrossProfitLocal() As Double` [R] Returns the closing gross profit in local currency. Field name: RealProfL.
  - remarks: SAP Business One calculates the ClosingGrossProfitLocal property as follows: ClosingGrossProfitLocal = ClosingPercentage * TotalAmountLocal.
- `Public Property ClosingGrossProfitSystem() As Double` [R] Returns the closing gross profit in system currency. Field name: RealProfS.
  - remarks: SAP Business One calculates the ClosingGrossProfitLocal property as follows: ClosingGrossProfitSystem = ClosingPercentage * TotalAmountSystem.
- `Public Property ClosingPercentage() As Double` [R] Sets or returns the propability percentage for closing the sales opportunity. Field name: CloPrcnt.
- `Public Property ClosingType() As BoSoClosedInTypes` [R/W] Sets or returns a valid value of BoSoClosedInTypes type that specifies the date types (days, weeks, or months) for the ClosingDate. Field name: DifType.
- `Public Property Competition() As SalesOpportunitiesCompetition` [R] Returns the SalesOpportunitiesCompetition child object.
- `Public Property ContactPerson() As Long` [R/W] Sets or returns the customer contact person code. Field name: CprCode. This is a foreign key to the ContactEmployees object.
- `Public Property CurrentStageNo() As Double` [R] Returns the current stage number. Field name: StepLast. This is a foreign key to the SalesStages object.
- `Public Property CurrentStageNumber() As Long` [R] property CurrentStageNumber
- `Public Property CustomerName() As String` [R/W] Sets or returns the business partner name who is related to the sales opportunity. Field name: Name. Length: 100 characters.
- `Public Property DataOwnershipfield() As Long` [R/W] Sets or returns the employee ID who is responsible for the sales opportunity. Field name: Owner. This is a foreign key to the Employees table (OHEM), not exposed through the DI API.
- `Public Property DocumentCheckbox() As String` [R] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not restrict the search range for the business partner's documents. Field name: DocChkbox.
- `Public Property GrossProfit() As Double` [R/W] Sets or returns the gross profit percentage. Field name: PrcnProf.
- `Public Property GrossProfitTotalLocal() As Double` [R/W] Sets or returns the total gross profit in local currency. Field name: SumProfL.
  - remarks: SAP Business One calculates the GrossProfitTotalLocal property as follows: GrossProfitTotalLocal = GrossProfit * MaxLocalTotal.
- `Public Property GrossProfitTotalSystem() As Double` [R] Sets or returns the total gross profit in system currency. Field name: SumProfS.
  - remarks: SAP Business One calculates the GrossProfitTotalSystem property as follows: GrossProfitTotalSystem = GrossProfit * MaxSystemTotal.
- `Public Property Industry() As Long` [R/W] Sets or returns the industry ID number. Field name: Industry. This is a foreign key to the Industries object.
- `Public Property InterestField1() As Long` [R/W] Sets or returns the main interest range for the sales opportunity. Field name: IntCat1. This is a foreign key to the Interest table (ooin), not exposed through the DI API.
- `Public Property InterestField2() As Long` [R/W] Sets or returns the secondary interest range for the sales opportunity. Field name: IntCat2. This is a foreign key to the Interest table (ooin), not exposed through the DI API.
- `Public Property InterestField3() As Long` [R/W] Sets or returns the additional interest range for the sales opportunity. Field name: IntCat3. This is a foreign key to the Interest table (ooin), not exposed through the DI API.
- `Public Property InterestLevel() As Long` [R/W] Sets or returns the interest level (for example: warm, cold, general interest, and so on) for the sales opportunity. Field name: IntRate. This is a foreign key to the Interest table (OOIR), not exposed through the DI API.
- `Public Property Interests() As SalesOpportunitiesInterests` [R] Returns the SalesOpportunitiesInterests child object.
- `Public Property Lines() As SalesOpportunitiesLines` [R] Returns the SalesOpportunitiesLines child object.
- `Public Property LinkedDocumentNumber() As String` [R] Sets or returns the document number that is linked to the sales opportunity. Field name: DocNum. Length: 20 characters.
- `Public Property LinkedDocumentType() As Long` [R] Sets or returns the type of the document that is linked to the sales opportunity. For example: sales quotation, sales order, delivery, or A/R invoice. Field name: DocType. Length: 2 characters.
- `Public Property MaxLocalTotal() As Double` [R] Sets or returns the total predicted sales in local currency. Field name: MaxSumLoc.
- `Public Property MaxSystemTotal() As Double` [R] Sets or returns the total predicted sales in system currency. Field name: MaxSumSys.
- `Public Property OpportunityName() As String` [R/W] Sets or returns the opportunity name. Field name: Name. Length: 100 characters.
- `Public Property OpportunityType() As OpportunityTypeEnum` [R/W] property OpportunityType
- `Public Property Partners() As SalesOpportunitiesPartners` [R] Returns the SalesOpportunitiesPartners child object.
- `Public Property PredictedClosingDate() As Date` [R/W] Sets or returns the predicted closing date. Field name: PredDate.
  - remarks: SAP Business One checks predicted closing date that it is grater or equal to the start date of the sales opportunity.
- `Public Property ProjectCode() As String` [R/W] Sets or returns the project code as defined in the Projects object. This is a foreign key to the Projects table (OPRJ). Length: 8 characters. Field name: PrjCode.
- `Public Property ReasonForClosing() As Long` [R/W] Sets or returns the reason for closing (exists only if the status is "Missed"). Field name: Reason. This is a foreign key to the Defect Cause table (OOFR), not exposed through the DI API).
- `Public Property Reasons() As SalesOpportunitiesReasons` [R] Returns the SalesOpportunitiesReasons child object.
- `Public Property Remarks() As String` [R/W] Sets or returns a memo type string that specifies remarks of the sales opportunity. Field name: Memo. Length:64,000 characters.
- `Public Property SalesPerson() As Long` [R/W] Sets or returns the sales person code. Field name: SlpCode. This is a foreign key to the SalesPersons object.
  - remarks: The sales employees can be defined through the SalesPersons object (see SalesEmployeeCode).
- `Public Property SequentialNo() As Long` [R] Returns the key identifier of the sales opportunity record. SAP Business One assigns this key number automatically when adding a sales opportunity. Field name: OpprId.
- `Public Property Source() As Long` [R/W] Sets or returns the source of the sales opportunity, for example, Internet, exposition, consultant, and so on. Field name: Source This is a foreign key to the Information Source table (OOSR), which is exposed via the SalesOpportunitySourcesSetupService object.
- `Public Property StartDate() As Date` [R/W] Sets or returns the start date of the sales opportunity. Mandatory property. Field name: OpenDate.
  - remarks: Default: current date.
- `Public Property Status() As BoSoOsStatus` [R/W] Sets or returns a valid value of BoSoOsStatus type that specifies the summary status of the sales opportunity (Open, Lost, or Won). Field name: Status.
- `Public Property StatusRemarks() As String` [R/W] Sets or returns the status remarks. Length: 30 characters. Field name: StatusRem.
- `Public Property Territory() As Long` [R/W] Sets or returns the sales opportunity territory (segment of the market). Field name: Territory. This is a foreign key to the Territories object. Sets or returns the business partner territory as defined in SAP Business One. Relevant to business partners of customer type only. Field name: Territory. This is a foreign key to the Territories object.
- `Public Property TotalAmounSystem() As Double` [R] Sets or returns the closing total amount of sales in system currency. Field name: RealSumSys.
- `Public Property TotalAmountLocal() As Double` [R/W] Sets or returns the closing total amount of sales in local currency. Field name: SumProfL.
- `Public Property UpdateDate() As Date` [R] property UpdateDate
- `Public Property UpdateTime() As Date` [R] property UpdateTime
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserSignature() As Long` [R] Returns the ID of the user who enters the sales opportunity details. Field name: UserSign. This is a foreign key to the Users object.
- `Public Property WeightedSumLC() As Double` [R] Sets or returns the weighted predicted sales in local currency. Field name: WtSumLoc.
  - remarks: SAP Business One calculates the WeightedSumLC property as follows: WeightedSumLC = ClosingPercentage * MaxLocalTotal.
- `Public Property WeightedSumSC() As Double` [R] Sets or returns the weighted predicted sales in system currency. Field name: WtSumSys.
  - remarks: SAP Business One calculates the WeightedSumSC property as follows: WeightedSumSC = ClosingPercentage * MaxSystemTotal.

## Methods (8)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
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
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal OpprId As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `OpprId`: Specifies the sales opportunity ID (SequentialNo).
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

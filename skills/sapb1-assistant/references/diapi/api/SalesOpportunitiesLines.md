<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SalesOpportunitiesLines (Object)

SalesOpportunityLines is a child object of the SalesOpportunities object and represents the stages of the sales opportunity. Source table: OPR1.

**Remarks:** To display the form in the application: - Select Sales Opportunities --> Sales Opportunity. - Select the Stages tab.

## Properties (24)
- `Public Property BPChanelCode() As String` [R/W] Sets or returns the distribution channel code for the stage of the sales opportunity. Field name: ChnCrdCode. Length: 15 characters. This is a foreign key to the BusinessPartners object.
- `Public Property BPChanelName() As String` [R/W] Sets or returns the distribution channel name for the stage of the sales opportunity. Field name: ChnCrdName. Length: 100 characters.
- `Public Property BPChannelContact() As Long` [R/W] Sets or returns the contact person of the distribution channel for the sales opportunity stage. Property type Read-write property " --> Field name: ChnCrdCon. This is a foreign key to the ContactEmployees object.
- `Public Property ClosingDate() As Date` [R/W] Sets or returns the actual date of closing the sales opportunity in the current stage. Field name: CloseDate.
  - remarks: SAP Business One checks this date. The closing date in the last stage must be before or equal to PredictedClosingDate, otherwise, SAP Business One changes the PredictedClosingDate to the actual closing date.
- `Public Property Contact() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies the whether or not the sales opportunity of the current stage is active. Field name: Linked.
- `Public Property ContactPerson() As Long` [R/W] Sets or returns the contact person for the sales opportunity stage. Property type Read-write property " --> Field name: CntctCode. This is a foreign key to the ContactEmployees object.
- `Public Property Count() As Long` [R] Returns the total rows in the SalesOpportunitiesLines list.
  - remarks: When you add a sales opportunity, the Count value is incremented automatically.
- `Public Property DataOwnershipfield() As Long` [R/W] Sets or returns the employee ID who is responsible for the sales opportunity stage. Field name: Owner. This is a foreign key to the EmployeesInfo object.
- `Public Property DocumentCheckbox() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not restrict the search range for the business partner's documents. Field name: DocChkbox.
- `Public Property DocumentNumber() As Long` [R/W] Sets or returns the document ID. Field name: DocNumber.
- `Public Property DocumentType() As BoAPARDocumentTypes` [R/W] Sets or returns the type of Sales - A/R and Purchasing - A/P document.
- `Public Property LineNum() As Long` [R] Returns the current row number in the sales opportunity table. Field name: Line.
- `Public Property MaxLocalTotal() As Double` [R/W] Sets or returns the total predicted sales, in local currency, for the current stage. Field name: MaxSumLoc.
  - remarks: MaxLocalTotal of the last stage must be equal to MaxLocalTotal defined in the SalesOpportunity object (OOPR table), otherwise, SAP Business One updates the MaxLocalTotal defined in OOPR table.
- `Public Property MaxSystemTotal() As Double` [R] Sets or returns the total predicted sales, in system currency, for the current stage. Field name: MaxSumSys.
  - remarks: MaxSystemTotal of the last stage must be equal to MaxSystemTotal defined in the SalesOpportunity object (OOPR table), otherwise, SAP Business One updates the MaxSystemTotal defined in OOPR table.
- `Public Property PercentageRate() As Double` [R/W] Sets or returns the probability percentage to complete the sales stage successfully. Field name: ClosePrcnt.
  - remarks: If the StageKey value is set, SAP Business One automatically sets the PercentageRate value as defined in the ClosingPercentage (of the SalesStages object), however, you can override the PercentageRate value. The PercentageRate in the last stage must be equal to the ClosingPercentage.
- `Public Property Remarks() As String` [R/W] Sets or returns a memo type string that specifies remarks of the sales opportunity for the current stage. Field name: Memo. Length: 64,000 characters.
- `Public Property SalesPerson() As Long` [R/W] Sets or returns the sales person code. Field name: SlpCode. This is a foreign key to the SalesPersons object.
  - remarks: The sales employees can be defined through the SalesPersons object (see SalesEmployeeCode).
- `Public Property SequenceNo() As Long` [R] Returns the sales opportunity unique ID (primary key). Field name: OpportId. Returns the sales opportunity unique ID (primary key). Field name: OpportId.
- `Public Property StageKey() As Long` [R/W] Sets or returns the foreign key of the sales stage. Field name: Step_Id. This is a foreign key to the SalesStages.
  - remarks: The stage code represents a stage name such as, Lead, 1st meeting, Negotiation, and so on. The stage code also defines the PercentageRate.
- `Public Property StartDate() As Date` [R/W] Sets or returns the date of starting the sales opportunity in the current stage. Field name: OpenDate.
  - remarks: SAP Business One checks this date. The start date must be before the close date specified in the last stage, otherwise, SAP Business One sends an error.
- `Public Property Status() As BoSoStatus` [R] Sets or returns a valid value of BoSoStatus type that specifies the sales opportunity status for the current stage (open, missed, or sold). Field name: Status.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WeightedAmountLocal() As Double` [R] Sets or returns the weighted sales, in local currency, for the current stage. Field name: WtSumLoc.
  - remarks: WeightedAmountLocal of the last stage must be equal to WeightedSumLC (predicted amount) defined in the SalesOpportunity object (OOPR table), otherwise, SAP Business One updates the WeightedSumLC.
- `Public Property WeightedAmountSystem() As Double` [R] Sets or returns the weighted sales, in system currency, for the current stage. Field name: WtSumSys.
  - remarks: WeightedAmountSystem of the last stage must be equal to WeightedSumSC (predicted amount) defined in the SalesOpportunity object (OOPR table), otherwise, SAP Business One updates the WeightedSumSC.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

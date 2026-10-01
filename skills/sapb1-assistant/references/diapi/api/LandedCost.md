<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# LandedCost (Object)

Represents a landed costs document, which is used for recording and allocating the costs incurred when importing goods. Source table: OIPF.

**Remarks:** To access the window, from the SAP Business One main menu, choose Purchasing A/P --> Landed Costs.

## Properties (40)
- `Public Property ActualCustoms() As Double` [R/W] The actual customs amount. Actual customs are calculated as follows: Actual customs = (FOB + included for customs landed costs) x fixed customs rate %. The fixed customs rate is defined in the Customs Group field on the Purchasing Data tab of the item master data. Field name: ActCustom.
- `Public Property ActualCustomsFC() As Double` [R/W] The actual customs amount in foreign currency. Field name: AcCustomFC.
- `Public Property AmountToBalance() As Double` [R] Difference between the sum of amounts on the Costs tab and the Total Freight Charges value on the Items tab. Field name: Cost_Match.
  - remarks: In perpetual inventory, you can only post the document if the value is zero.
- `Public Property AmountToBalanceFC() As Double` [R] Difference between the sum of amounts on the Costs tab and the Total Freight Charges value on the Items tab in foreign currency. Field name: C_Match_FC.
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property BeforeTax() As Double` [R] Sum of base document price + (expenditure*quantity) + projected customs Field name: BeforeVat.
- `Public Property BeforeTaxFC() As Double` [R] Before tax in foreign currency. Field name: BeforVatFC.
- `Public Property BillofLadingNumber() As String` [R/W] The number of the bill of lading attached to the landed costs document Field name: BillOfLad. Length: 20 characters.
- `Public Property Broker() As String` [R/W] The code of the broker hired to assist with the import and customs procedures. Field name: AgentCode. Length: 15 characters.
- `Public Property BrokerName() As String` [R/W] The name of the broker hired to assist with the import and customs procedures. Field name: AgentName. Length: 100 characters.
- `Public Property ClosedDocument() As LandedCostDocStatusEnum` [R/W] Specify the field when you finish processing a landed costs document. Field name: DocStatus.
- `Public Property CustomsAffectsInventory() As BoYesNoEnum` [R/W] Specifies whether the customs fees affect the inventory value. Field name: incCustom.
  - remarks: This field is only available for companies managing a perpetual inventory.
- `Public Property DocEntry() As Long` [R] The internal ID of the landed costs. Field name: DocEntry.
- `Public Property DocumentCurrency() As String` [R/W] The currency used for the document. Field name: DocCur. Length: 3 characters.
- `Public Property DocumentRate() As Double` [R/W] The exchange rate used for the document. You must enter an exchange rate; otherwise, you are not able to continue recording the landed costs document. After you specify an exchange rate, you can choose either the vendor currency or your local currency. Your selection determines the currency in which monetary values are displayed in the document. Field name: DocRate.
- `Public Property DueDate() As Date` [R/W] Specify the due date for the document. The default value is the date on which the landed costs document is created. If required, change the date. Field name: DocDueDate.
- `Public Property FileNumber() As String` [R/W] Number of the landed costs document, as provided by your broker. Field name: AgentNum. Length: 16 characters.
- `Public Property JournalRemarks() As String` [R/W] The remarks for the journal entry, which is used to fill the journal entry memo field (OJDT.Memo). Field name: JdtMemo. Length: 50 characters.
- `Public Property LandedCost_CostLines() As LandedCost_CostLines` [R] Returns the LandedCost_CostLine object.
- `Public Property LandedCost_ItemLines() As LandedCost_ItemLines` [R] Returns the LandedCost_ItemLine object.
- `Public Property LandedCostNumber() As Long` [R] The landed costs document number, which is a sequential number automatically assigned by SAP Business One according to the definition in the system initialization (see Administration --> System Initialization --> Document Numbering). Field name: DocNum.
- `Public Property PostingDate() As Date` [R/W] Specify the posting date. The default value is the date on which the landed costs document is created. If required, change the date. Field name: DocDate.
- `Public Property ProjectedCustoms() As Double` [R] Projected customs, which are calculated automatically as follows: Projected customs = (FOB + included for customs landed costs) x fixed customs rate % Field name: ExpCustom.
- `Public Property ProjectedCustomsFC() As Double` [R] Projected customs in foreign currency. Field name: ExCustomFC.
- `Public Property Reference() As String` [R/W] Additional reference number for the document, if defined. Field name: Ref1. Length: 11 characters.
- `Public Property Remarks() As String` [R/W] Displays the reference numbers or the vendor numbers for the goods receipt PO used in the landed costs document, and depends on the default settings made. You can change the remarks, if necessary. Field name: Descr. Length: 250 characters.
- `Public Property Series() As Long` [R/W] Specify a numbering series. Field name: Series.
- `Public Property Tax1() As Double` [R/W] The tax amount relevant for the imported items. This has no impact on the journal entry. Field name: Vat1.
- `Public Property Tax1FC() As Double` [R/W] The tax amount in foreign currency relevant for the imported items. Field name: Vat1FC.
- `Public Property Tax2() As Double` [R/W] The tax amount relevant for the landed costs. This has no impact on the journal entry. Field name: Vat2.
- `Public Property Tax2FC() As Double` [R/W] The tax amount in foreign currency relevant for the landed costs. Field name: Vat2FC.
- `Public Property Total() As Double` [R] The overall amount of the document (before Tax+Tax 1+Tax 2). Field name: DocTotal.
- `Public Property TotalFC() As Double` [R] The overall amount of the document (before Tax+Tax 1+Tax 2) in foreign currency. Field name: DocTotalFC.
- `Public Property TotalFreightCharges() As Double` [R] Sum of expenditure * quantity for all lines. Field name: CostSum.
  - remarks: For perpetual inventory, this is the sum of total costs
- `Public Property TotalFreightChargesFC() As Double` [R] Total freight charges in foreign currency. Field name: CostSumFC.
- `Public Property TransactionNumber() As Long` [R] Number of the journal entry created for the landed costs. This is a foreign key to the JournalEntries object. Field name: JdtNum.
- `Public Property TransportType() As Long` [R/W] Specify the shipping type. It is a foreign key to the ShippingTypes object. Field name: TrnspCode.
- `Public Property UserFields() As Fields` [R] property User Fields
- `Public Property VendorCode() As String` [R/W] Codes of the vendors related to the landed costs document. Field name: CardCode. Length: 15 characters.
- `Public Property VendorName() As String` [R/W] Names of the vendors related to the landed costs document. Field name: SuppName. Length: 100 characters.

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

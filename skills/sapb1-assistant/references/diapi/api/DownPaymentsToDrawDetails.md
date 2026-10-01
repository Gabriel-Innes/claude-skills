<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DownPaymentsToDrawDetails (Object)

Represents detail lines for the DownPaymentsToDraw object. Source tables: INV11, PCH11, RIN11, RPC11, DRF11

**Example:**
- C# example (from SAP's help):
  ```csharp
  // Update PeriodCategory with SalesDownPaymentInterimAccount and PurchaseDownPaymentInterimAccount
  PeriodCategoryParamsCollection oPeriodCategoryColl;
  PeriodCategory oPerCategory;

  // Get Period Category Collection
  oPeriodCategoryColl = MainModule.oCmpSrv.GetPeriods();

  // Get the current period category, e.g. the first category
  oPerCategory = MainModule.oCmpSrv.GetPeriod(oPeriodCategoryColl.Item(0));

  // SalesDownPaymentInterimAccount is a new property, mandatory for DownPayment process
  oPerCategory.SalesDownPaymentInterimAccount = "2000";

  // PurchaseDownPaymentInterimAccount is a new property, mandatory for DownPayment process
  oPerCategory.PurchaseDownPaymentInterimAccount = "2000";
  MainModule.oCmpSrv.UpdatePeriod(oPerCategory);

  // Add a BP
  SAPbobsCOM.BusinessPartners oBP;
  oBP = (SAPbobsCOM.BusinessPartners)MainModule.oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oBusinessPartners);
  oBP.CardCode = "efrat";

  // DownPaymentClearAct is an existing property, mandatory for DownPayment process
  oBP.DownPaymentClearAct = "1000";
  //DownPaymentInterimAccount is a new property, mandatory for DownPayment process
  oBP.DownPaymentInterimAccount = "1000";
  oBP.Add();

  // Add two items
  SAPbobsCOM.Items oItem1, oItem2;
  oItem1 = (SAPbobsCOM.Items)MainModule.oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oItems);
  oItem1.ItemCode = "item1";
  oItem1.InventoryItem = BoYesNoEnum.tNO;
  oItem1.Add();
  oItem2 = (SAPbobsCOM.Items)MainModule.oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oItems);
  oItem2.ItemCode = "item2";
  oItem2.InventoryItem = BoYesNoEnum.tNO;
  oItem2.Add();

  // Add a DownPayment invoice
  SAPbobsCOM.Documents oDP;
  oDP = (SAPbobsCOM.Documents)MainModule.oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oDownPayments);
  // Set Down Payment Header Values
  oDP.CardCode = "efrat";
  oDP.DownPaymentType = DownPaymentTypeEnum.dptInvoice;

  // Set Down Payment Line Values
  // For VatGroup A1, the DownPayment has a line with 1 item1 of unit price $10.
  oDP.Lines.ItemCode = "item1";
  oDP.Lines.Quantity = 1;
  oDP.Lines.UnitPrice = 10;
  oDP.Lines.VatGroup = "A1";
  oDP.Lines.Add();

  //For VatGroup A2, the DownPayment has a line with 1 item2 of unit price $10.
  oDP.Lines.ItemCode = "item2";
  oDP.Lines.Quantity = 1;
  oDP.Lines.UnitPrice = 10;
  oDP.Lines.VatGroup = "A2";
  oDP.Add();

  string sNewObjCode = "";
  // Retrieve the key of the last added record, here the DocNum of DownPayment invoice created in the step
  MainModule.oCompany.GetNewObjectCode(out sNewObjCode);
  int tmpKey = Convert.ToInt32(sNewObjCode);

  // Pay the DownPayment invoice
  SAPbobsCOM.Payments oPay;
  oPay = (SAPbobsCOM.Payments)MainModule.oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oIncomingPayments);
  oPay.CardCode = "efrat";
  // Set the Downpayment we created to be paid
  oPay.Invoices.DocEntry = tmpKey;
  oPay.Invoices.InvoiceType = BoRcptInvTypes.it_DownPayment;
  oPay.CashAccount = "1000";
  oPay.CashSum = 30;
  oPay.Add();

  // Add invoice with down payment
  SAPbobsCOM.Documents oINV;
  oINV = (SAPbobsCOM.Documents)MainModule.oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oInvoices);
  oINV.CardCode = "efrat";
  oINV.DocType = SAPbobsCOM.BoDocumentTypes.dDocument_Items;

  // For VatGroup A1, the invoice has 1 item1 with unit price $10.
  oINV.Lines.ItemCode = "item1";
  oINV.Lines.Quantity = 1;
  oINV.Lines.UnitPrice = 10;
  oINV.Lines.VatGroup = "A1";
  oINV.Lines.Add();
  // For VatGroup A2, the invoice has 1 item2 with unit price $20.
  oINV.Lines.ItemCode = "item2";
  oINV.Lines.Quantity = 1;
  // ... (truncated)
  ```

## Properties (19)
- `Public Property AmountToDraw() As Double` [R/W] The net amount (without tax) drawn to the invoice for this line. Field name: LineTotal
- `Public Property AmountToDrawFC() As Double` [R/W] The net amount (without tax) drawn to the invoice for this line in foreign currency. Field name: TotalFrgn
- `Public Property AmountToDrawSC() As Double` [R/W] The net amount (without tax) drawn to the invoice for this line in system currency. Field name: TotalSumSy
- `Public Property Count() As Long` [R] The number of downpayment detail lines in the collection.
- `Public Property DocEntry() As Long` [R] An internal key to the down payment document. Field name: BaseAbs This is a foreign key to the Documents (down payments) object.
- `Public Property DocInternalID() As Long` [R] A key to the invoice for which the down payment is used. Field name: DocEntry This is a foreign key to the Documents (invoices) object.
- `Public Property GrossAmountToDraw() As Double` [R/W] The gross amount (with tax) drawn to the invoice for this line. Field name: Gross
- `Public Property GrossAmountToDrawFC() As Double` [R/W] The gross amount (with tax) drawn to the invoice for this line in foreign currency. Field name: GrossFc
- `Public Property GrossAmountToDrawSC() As Double` [R/W] The gross amount (with tax) drawn to the invoice for this line in system currency. Field name: GrossSc
- `Public Property IsGrossLine() As BoYesNoEnum` [R] Indicates whether the gross amount was entered and all other fields were calculated based on the gross amount. Field name: IsGross
- `Public Property LineType() As LineTypeEnum` [R/W] The type of detail line. Field name: LineType
- `Public Property RowNum() As Long` [R/W] The row number of the parent DownPaymentsToDraw object within its collection. Field name: LineNum
- `Public Property SeqNum() As Long` [R] The sequence number of the current drawn payment detail in the collection. Field name: LineSeq
- `Public Property Tax() As Double` [R/W] The part of the drawn downpayment in this line to be used for tax. Field name: VatSum
- `Public Property TaxAdjust() As BoYesNoEnum` [R] TaxAdjust
- `Public Property TaxFC() As Double` [R/W] The part of the drawn downpayment in this line to be used for tax in foreign currency. Field name: VatSumFrgn
- `Public Property TaxSC() As Double` [R/W] The part of the drawn downpayment in this line to be used for tax in system currency. Field name: VatSumSys
- `Public Property VatGroupCode() As String` [R/W] The tax code to which this downpayment line applied. Field name: VatGroup This is a foreign key to the VatGroups object.
- `Public Property VatPercent() As Double` [R] The tax rate for the tax code in the VatGroupCode property. Field name: VatPrcnt

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

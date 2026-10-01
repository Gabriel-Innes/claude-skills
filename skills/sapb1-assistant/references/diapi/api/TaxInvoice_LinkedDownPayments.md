<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxInvoice_LinkedDownPayments (Object)

Link to tax invoices from down payments for Russia localization. The whole "Linked Down Payments" subobject is read-only, meaning it is completed automatically during the adding of Tax Invoices (no matter if via UI or DI) and user can read the values via DI API using this subobject (LinkedDownPayments). Source table: TSI4 for A/R tax invoices, TPI4 for A/P tax invoices.

**Remarks:** Sales - A/R -> A/R Tax Invoice -> option Down Payments Purchasing - A/P -> A/P Tax Invoice -> option Down Payments

**Example:**
- C# example (from SAP's help):
  ```csharp
  SAPbobsCOM.TaxInvoices taxInvoice = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oSalesTaxInvoice) as SAPbobsCOM.TaxInvoices;
                  taxInvoice.GetByKey(1);
                  SAPbobsCOM.TaxInvoice_LinkedDownPayments taxInvoiceDPMs = taxInvoice.LinkedDownPayments;
                  if (taxInvoiceDPMs.Count < 1)
                  {
                      Console.WriteLine(""no linked down payments found"");
                  }
                  else
                  {
                      Console.WriteLine(""count: "" + taxInvoiceDPMs.Count);
                      for (int line = 0; line < taxInvoiceDPMs.Count; line++)
                      {
                          taxInvoiceDPMs.SetCurrentLine(line);
                          Console.WriteLine(""line "" + (line + 1) + "":"");
                          Console.WriteLine("" DocEntry: "" + taxInvoiceDPMs.DocEntry);
                          Console.WriteLine("" LineNum: "" + taxInvoiceDPMs.LineNum);
                          Console.WriteLine("" DownPaymentType: "" + taxInvoiceDPMs.DownPaymentType);
                          Console.WriteLine("" DownPaymentEntry: "" + taxInvoiceDPMs.DownPaymentEntry;
                          Console.WriteLine("" DownPaymentNum: "" + taxInvoiceDPMs.DownPaymentNum);
                          Console.WriteLine("" PaymentType: "" + taxInvoiceDPMs.PaymentType);
                          Console.WriteLine("" PaymentEntry: "" + taxInvoiceDPMs.PaymentEntry;
                          Console.WriteLine("" PaymentNum: "" + taxInvoiceDPMs.PaymentNum);
                          Console.WriteLine("" PaymentTaxDate: "" + taxInvoiceDPMs.PaymentTaxDate);
                          Console.WriteLine("" TransferDate: "" + taxInvoiceDPMs.TransferDate);
                          Console.WriteLine("" TransferReference: "" + taxInvoiceDPMs.TransferReference;
                          Console.WriteLine("" AmountToDraw: "" + taxInvoiceDPMs.AmountToDraw);
                          Console.WriteLine("" AmountToDrawFC: "" + taxInvoiceDPMs.AmountToDrawFC);
                          Console.WriteLine("" AmountToDrawSC: "" + taxInvoiceDPMs.AmountToDrawSC);
                          Console.WriteLine("" DocCurrency: "" + taxInvoiceDPMs.DocCurrency);
                      }
                  }
  ```

## Properties (22)
- `Public Property AmountToDraw() As Double` [R] The amount of the down payment that is used. Field name: DrawnSum.
- `Public Property AmountToDrawFC() As Double` [R] The amount of the down payment that is used in foreign currency. Field name: DrawnSumFc.
- `Public Property AmountToDrawSC() As Double` [R] The amount of the down payment that is used in system currency. Field name: DrawnSumSc.
- `Public Property Count() As Long` [R] Number of records in a LinkedDownPayments collection.
- `Public Property DocCurrency() As String` [R] Document currency code (руб, EUR). Field name: DocCur.
- `Public Property DocEntry() As Long` [R] Absolute ID of the current Tax Invoice. Field name: DocEntry.
- `Public Property DownPaymentEntry() As Long` [R] Down payment entry. (203: A/R Down Payment, 204: A/P Down Payment); on UI just the Document Number is visible with link arrow to DPM called "Down Payment No." Field name: DpmDocEntr.
- `Public Property DownPaymentNum() As Long` [R] Down payment number. (203: A/R Down Payment, 204: A/P Down Payment); on UI just the Document Number is visible with link arrow to DPM called "Down Payment No." Field name: DpmDocNum.
- `Public Property DownPaymentType() As Long` [R] Down payment object type. (203: A/R Down Payment, 204: A/P Down Payment); on UI just the Document Number is visible with link arrow to DPM called "Down Payment No." Field name: DpmObjType.
- `Public Property GrossAmountToDraw() As Double` [R] The gross amount of the down payment that is used. Field name: Gross.
- `Public Property GrossAmountToDrawFC() As Double` [R] The gross amount of the down payment that is used in foreign currency. Field name: GrossFc.
- `Public Property GrossAmountToDrawSC() As Double` [R] The gross amount of the down payment that is used in system currency. Field name: GrossSc.
- `Public Property LineNum() As Long` [R] Line number in a LinkedDownPayments collection. Field name: LineNum.
- `Public Property PaymentEntry() As Long` [R] Payment entry. (24: Incoming Payment, 46: Outgoing Payment); on UI just the Document Number is visible with link arrow to Payment called "Payment No." Field name: PmnDocEntr.
- `Public Property PaymentNum() As Long` [R] Payment number. (24: Incoming Payment, 46: Outgoing Payment); on UI just the Document Number is visible with link arrow to Payment called "Payment No." Field name: PmnDocNum.
- `Public Property PaymentTaxDate() As Date` [R] Date of payment. Field name: PmnTaxDate.
- `Public Property PaymentType() As Long` [R] Type of payment object. (24: Incoming Payment, 46: Outgoing Payment); on UI just the Document Number is visible with link arrow to Payment called "Payment No." Field name: PmnObjType.
- `Public Property Tax() As Double` [R] Tax amount. Field name: Vat.
- `Public Property TaxFC() As Double` [R] Tax amount in foreign currency. Field name: VatFc.
- `Public Property TaxSC() As Double` [R] Tax amount in system currency. Field name: VatSc.
- `Public Property TransferDate() As Date` [R] Date of transfer. Copied from the payment of the linked DPM, when using Bank Transfer payment method. Field name: TrsfrDate.
- `Public Property TransferReference() As String` [R] Reference of transfer. Copied from the payment of the linked DPM, when using Bank Transfer payment method. Field name: TrsfrRef.

## Methods (1)
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

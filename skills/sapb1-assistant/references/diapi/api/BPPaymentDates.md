<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
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

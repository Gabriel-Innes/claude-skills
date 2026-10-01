<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
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

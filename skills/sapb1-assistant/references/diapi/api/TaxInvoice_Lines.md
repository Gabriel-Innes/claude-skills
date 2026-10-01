<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxInvoice_Lines (Object)

TaxInvoice_Lines is a child object of the TaxInvoices object that represents the line entries of each tax invoice document. Source table: TSI1 for sales invoices, TPI1 for purchase invoices, or TXD1 for journal entry.

**Remarks:** Country-specific for Russia.

## Properties (6)
- `Public Property BaseEntry() As Long` [R] Returns the key of the source document. Field name: BaseEntry.
- `Public Property BaseType() As BoTaxInvoiceTypes` [R] Returns a valid value of BoTaxInvoiceTypes type that specifies the type of the base document: Invoice, Payment, or Journal Entry. Field name: DocType.
- `Public Property Count() As Long` [R] Returns the total data rows in the table.
- `Public Property LineNum() As Long` [R] Returns the row number. Field name: LineNum.
- `Public Property Reference() As Long` [R/W] Sets or returns the key of the referenced document. Field name: RefEntry1.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0. Specifies the row number. The count starts from 0.

<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# StockTransfer_TaxExtension (Object)

StockTransfer_TaxExtension is a child object of the StockTransfer object. It represents the tax extension of stock tranfers. Applicable for cluster B only (country-specific for India). Source table: WTR12.

## Properties (4)
- `Public Property FormNumber() As String` [R/W] Sets or returns the form number used for the transaction category in Warehouse Transfer. Field name: FormNo.
- `Public Property SupportVAT() As BoYesNoEnum` [R/W] Sets or returns a valid value to identify Stock transfers created for Sales Tax purposes in Warehouse Transfer. Field name: Vat.
- `Public Property TransactionCategory() As String` [R/W] Sets or returns the transaction category. This property is a foreign key of Transaction Category table (OTNC - not exposed through the DI API). Field name: TransCat.
  - remarks: Dealer has to issue declarations in which form printed and supplied by the Sales Tax authorities in Warehouse Transfer.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

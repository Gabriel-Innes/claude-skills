<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CurrencyRestrictions (Object)

The CurrencyRestrictions is a child object of the WizardPaymentMethods object. This object enables to allow or restrict currencies in the payment method. Source table: PYM1.

**Remarks:** To display the form in the application: - Select Administration -->Setup -->Banking -->Payment Methods. - Click the [...] button near the Currency Restriction field. The CurrencyRestrictions object is applicable when the CurrencyRestriction property of the WizardPaymentMethods object is set to tYES.

## Properties (6)
- `Public Property Choose() As BoYesNoEnum` [R/W] Determines whether to allow (Y) or to restrict (N) the currency in the payment method. Field name: Choose.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property CurrencyCode() As String` [R/W] Sets or returns the currency code as defined through the Currencies object. Field name: CurrCode. This is a foreign key to the Currencies object. Length: 3 characters.
- `Public Property CurrencyName() As String` [R] Returns the currency name as defined through the Currencies object. Field name: CurrName. Length: 20 characters.
- `Public Property PaymentMethodCode() As String` [R] Returns the payment method code as defined in the WizardPaymentMethods object. Field name: PymCode. This is a foreign key to the WizardPaymentMethods object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

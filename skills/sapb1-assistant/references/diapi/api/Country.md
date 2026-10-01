<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Country (Object)

A data structure object holding properties for the CountriesService object. Source table: OCRY.

## Properties (19)
- `Public Property AddressFormat() As Long` [R/W] Sets or returns the postal address format used by the country. The postal address format must be already presented in the Address Formats table (foreign key to OADF). Field name: AddrFormat.
- `Public Property BankAccountDigits() As Long` [R/W] Sets or returns the number of digits for the bank account number. Used for bank account validation. If greater than zero, it determines how many digits or characters has a valid bank account number for the specific country. If zero, the number of digits is not validated for bank account numbers for the specific country. Field name: BnkActDgts.
- `Public Property BankBranchDigits() As Long` [R/W] Sets or returns the number of digits for the bank branch number. Used for bank account validation. If greater than zero, it determines how many digits or characters has a valid bank branch number for the specific country. If zero, the number of digits is not validated for bank branch numbers for the specific country. Field name: BnkBchDgts.
- `Public Property BankCodeDigits() As Long` [R/W] Sets or returns the number of digits for the bank code. Used for bank account validation. If greater than zero, it determines how many digits or characters has a valid bank branch number for the specific country. If zero, the number of digits is not validated for bank branch numbers for the specific country. Field name: BnkCodDgts.
- `Public Property BankControlKeyDigits() As Long` [R/W] Sets or returns the number of digits for the bank control key. Used for bank account validation. If greater than zero, it determines how many digits or characters has a valid bank control key for the specific country. If zero, the number of digits is not validated for bank control key numbers for the specific country. Field name: BnkCtKDgts.
- `Public Property Blacklisted() As BoYesNoEnum` [R/W] property Blacklisted
- `Public Property Code() As String` [R/W] Sets or returns the country code. Field name: code. Character length: 3.
- `Public Property CodeForReports() As String` [R/W] Sets or returns the country code for the reports. Field name: ReportCode. Character length: 3.
- `Public Property DomesticAccountValidation() As DomesticBankAccountValidationEnum` [R/W] Sets or returns a valid value for special validation of specific countries' bank accounts. If set to one of the valid values, it activates a country specific bank account number validation algorithm. The algorithms usually performs additional validations that are more complex than simple number of digits checks. These algorithms are currently available for certain countries in SAP Business One. If empty or XX, not country specific bank account number validation is performed.
- `Public Property EAEU() As BoYesNoEnum` [R/W] property EAEU
- `Public Property EU() As BoYesNoEnum` [R/W] Sets or returns a valid value that specifies whether or not the country is a member of the European Union.
- `Public Property IbanValidation() As BoYesNoEnum` [R/W] Sets or returns a valid value that specifies whether or not to perform IBAN validation for the specified country.
- `Public Property ISOAlpha2Code() As String` [R/W] 2 character ISO country code. Field name: ISO2Code. Length: 2.
- `Public Property ISOAlpha3Code() As String` [R/W] 3 character ISO country code. Field name: ISO3Code. Length: 3.
- `Public Property ISONumeric() As String` [R/W] 3 numeric ISO country code. Field name: ISONumeric. Length: 3.
- `Public Property Name() As String` [R/W] Sets or returns the name of the country. Field name: Name. Character length: 100.
- `Public Property NumberOfDigitsForTaxID() As Long` [R/W] Sets or returns the number of digits of a valid Tax ID in the specified country. Field name: TaxIdDigts.
- `Public Property UICCountryCode() As String` [R/W] UIC country code. Field name: UICCode. Length: 3.
- `Public Property UserFields() As Fields` [R] Get User Fields

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML data. Specifies the the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

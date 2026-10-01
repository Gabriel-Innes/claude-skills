<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# WTaxTypeCodeService (Object)

Source table: OWXT.

**Remarks:** For the Italy localization only. Navigation path: Business Partner Master Data → Accounting → Tax, select the checkbox Subject to Withholding Tax, choose the browser button next to the Specific WTax Amounts Setup field, and go to the column WTax Type Code.

## Methods (8)
- `Public Function AddWTaxTypeCode(ByVal pIWTaxTypeCode As WTaxTypeCode) As WTaxTypeCodeParams` AddWTaxTypeCode
  - param `pIWTaxTypeCode`: 
- `Public Sub DeleteWTaxTypeCode(ByVal pIWTaxTypeCodeParams As WTaxTypeCodeParams)` DeleteWTaxTypeCode
  - param `pIWTaxTypeCodeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As WTaxTypeCodeServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/WTaxTypeCodeServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetWTaxTypeCode(ByVal pIWTaxTypeCodeParams As WTaxTypeCodeParams) As WTaxTypeCode` GetWTaxTypeCode
  - param `pIWTaxTypeCodeParams`: 
- `Public Function GetWTaxTypeCodeList() As WTaxTypeCodesParams` GetWTaxTypeCodeList
- `Public Sub UpdateWTaxTypeCode(ByVal pIWTaxTypeCode As WTaxTypeCode)` UpdateWTaxTypeCode
  - param `pIWTaxTypeCode`:

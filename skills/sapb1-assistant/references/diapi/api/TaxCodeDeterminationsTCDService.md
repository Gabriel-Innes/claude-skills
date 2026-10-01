<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxCodeDeterminationsTCDService (Object)

TaxCodeDeterminationsTCDService Class

## Methods (6)
- `Public Function GetDataInterface(ByVal enumMSDI As TaxCodeDeterminationsTCDServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/TaxCodeDeterminationsTCDServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetTaxCodeDeterminationTCD(ByVal pITaxCodeDeterminationTCDParams As TaxCodeDeterminationTCDParams) As TaxCodeDeterminationTCD` GetTaxCodeDeterminationTCD
  - param `pITaxCodeDeterminationTCDParams`: 
- `Public Function GetTaxCodeDeterminationTCDList() As TaxCodeDeterminationsTCDParams` GetTaxCodeDeterminationTCDList
- `Public Sub UpdateTaxCodeDeterminationTCD(ByVal pITaxCodeDeterminationTCD As TaxCodeDeterminationTCD)` UpdateTaxCodeDeterminationTCD
  - param `pITaxCodeDeterminationTCD`:

<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ServiceTaxPostingService (Object)

ServiceTaxPostingService Class

## Methods (5)
- `Public Function GetDataInterface(ByVal enumMSDI As ServiceTaxPostingServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ServiceTaxPostingServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetTaxableDeliveries() As ServiceTaxPostingParamsCollection` GetTaxableDeliveries
- `Public Sub PostServiceTax(ByVal pIServiceTaxPostingParams As ServiceTaxPostingParams)` PostServiceTax
  - param `pIServiceTaxPostingParams`:

<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# LegalDataService (Object)

LegalDataService Class

## Methods (6)
- `Public Function Add(ByVal pILegalData As LegalData) As LegalDataParams` Add
  - param `pILegalData`: 
- `Public Function Get(ByVal pILegalDataParams As LegalDataParams) As LegalData` Get
  - param `pILegalDataParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As LegalDataServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/LegalDataServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Sub Update(ByVal pILegalData As LegalData)` Update
  - param `pILegalData`:

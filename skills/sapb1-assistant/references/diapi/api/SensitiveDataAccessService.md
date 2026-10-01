<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SensitiveDataAccessService (Object)

SensitiveDataAccessService Class

## Methods (5)
- `Public Function Access(ByVal pISensitiveDataAccess As SensitiveDataAccess) As SensitiveDataAccess` Access
  - param `pISensitiveDataAccess`: 
- `Public Function GetDataInterface(ByVal enumMSDI As SensitiveDataAccessServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/SensitiveDataAccessServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function IsDataSensitive(ByVal pISensitiveDataAccess As SensitiveDataAccess) As DataSensitiveStatus` IsDataSensitive
  - param `pISensitiveDataAccess`:

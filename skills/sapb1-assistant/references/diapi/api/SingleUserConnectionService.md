<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SingleUserConnectionService (Object)

SingleUserConnectionService Class

## Methods (5)
- `Public Function Get(ByVal pISingleUserConnectioParams As SingleUserConnectionParams) As SingleUserConnection` Get
  - param `pISingleUserConnectioParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As SingleUserConnectionServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/SingleUserConnectionServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Sub Update(ByVal pISingleUserConnection As SingleUserConnection)` Update
  - param `pISingleUserConnection`:

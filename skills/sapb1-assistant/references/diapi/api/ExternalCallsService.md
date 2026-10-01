<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ExternalCallsService (Object)

External Call Service is used as an communication mechanism between Business One and any 3rd party or external applications. When Business One application is initiating an operation that requires real time external application (e.g. Business One integration), an external call request record is added to OREQ table. External applications could access this request via External Call Service, update the status of the request and attach response messages to the request. Mandatory properties: ID, Category, Status. Source table: OREQ.

## Methods (6)
- `Public Function GetCall(ByVal pIExternalCallParams As ExternalCallParams) As ExternalCall` Returns an instance of an external call by ID.
  - param `pIExternalCallParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ExternalCallsServiceDataInterfaces) As Object` Creates an empty data interface. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ExternalCallsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Retrieves the Data Interface from XML file.
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Retrieves the Data Interface from XML string.
  - param `bstrXMLString`: 
- `Public Function SendCall(ByVal pIExternalCall As ExternalCall) As ExternalCallParams` Creates a new Call.
  - param `pIExternalCall`: 
- `Public Sub UpdateCall(ByVal pIExternalCall As ExternalCall)` Updates a call.
  - param `pIExternalCall`:

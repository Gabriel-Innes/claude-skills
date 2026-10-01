<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TransportationDocumentService (Object)

TransportationDocumentService Class

## Methods (7)
- `Public Function AddTransportationDocument(ByVal pITransportationDocumentData As TransportationDocumentData) As TransportationDocumentParams` AddTransportationDocument
  - param `pITransportationDocumentData`: 
- `Public Sub CancelTransportationDocument(ByVal pITransportationDocumentParams As TransportationDocumentParams)` CancelTransportationDocument
  - param `pITransportationDocumentParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As TransportationDocumentServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/TransportationDocumentServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetTransportationDocument(ByVal pITransportationDocumentParams As TransportationDocumentParams) As TransportationDocumentData` GetTransportationDocument
  - param `pITransportationDocumentParams`: 
- `Public Sub UpdateTransportationDocument(ByVal pITransportationDocumentData As TransportationDocumentData)` UpdateTransportationDocument
  - param `pITransportationDocumentData`:

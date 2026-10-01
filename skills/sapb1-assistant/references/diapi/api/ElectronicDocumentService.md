<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ElectronicDocumentService (Object)

ElectronicDocumentService Class

## Methods (16)
- `Public Sub AddImportEntry(ByVal pIEDFImportEntry As EDFImportEntry)` Import electronic document.
  - param `pIEDFImportEntry`: Electronic document import file.
- `Public Sub AddLog(ByVal pIEDFEntryLogInputParams As EDFEntryAddLogInputParams)` AddLog
  - param `pIEDFEntryLogInputParams`: 
- `Public Sub ExportEntryLog(ByVal pIEDFEntryLogInputParams As EDFEntryLogInputParams)` ExportEntryLog
  - param `pIEDFEntryLogInputParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ElectronicDocumentServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ElectronicDocumentServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetDocMappingList(ByVal pIEDFDocMappingInputParams As EDFDocMappingInputParams) As EDFDocMappingsCollection` GetDocMappingList
  - param `pIEDFDocMappingInputParams`: 
- `Public Function GetEntry(ByVal pIEDFEntryInputParams As EDFEntryInputParams) As EDFEntry` GetEntry
  - param `pIEDFEntryInputParams`: 
- `Public Function GetEntryList(ByVal pIEDFEntryListInputParams As EDFEntryListInputParams) As EDFEntriesCollection` GetEntryList
  - param `pIEDFEntryListInputParams`: 
- `Public Function GetLastLog(ByVal pIEDFEntryLogInputParams As EDFEntryLogInputParams) As EDFEntryLog` GetLastLog
  - param `pIEDFEntryLogInputParams`: 
- `Public Function GetLogs(ByVal pIEDFEntryLogInputParams As EDFEntryLogInputParams) As EDFEntryLogsCollection` GetLogs
  - param `pIEDFEntryLogInputParams`: 
- `Public Function GetMappingByHash(ByVal pIEDFMappingInputParams As EDFMappingInputParams) As EDFMapping` GetMappingByHash
  - param `pIEDFMappingInputParams`: 
- `Public Function GetProtocol(ByVal pIEDFProtocolInputParams As EDFProtocolInputParams) As EDFProtocol` GetProtocol
  - param `pIEDFProtocolInputParams`: 
- `Public Function GetProtocolParameters(ByVal pIEDFProtocolInputParams As EDFProtocolInputParams) As EDFProtocolWithParameters` GetProtocolParameters
  - param `pIEDFProtocolInputParams`: 
- `Public Function GetProtocols() As EDFProtocolsCollection` GetProtocols
- `Public Sub UpdateEntry(ByVal pIEDFEntry As EDFEntry)` UpdateEntry
  - param `pIEDFEntry`:

<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# JournalEntryDocumentTypeService (Object)

JournalEntryDocumentTypeService Class

## Methods (8)
- `Public Function Add(ByVal pIJournalEntryDocumentType As JournalEntryDocumentType) As JournalEntryDocumentTypeParams` Add
  - param `pIJournalEntryDocumentType`: 
- `Public Sub Delete(ByVal pIJournalEntryDocumentTypeParams As JournalEntryDocumentTypeParams)` Delete
  - param `pIJournalEntryDocumentTypeParams`: 
- `Public Function Get(ByVal pIJournalEntryDocumentTypeParams As JournalEntryDocumentTypeParams) As JournalEntryDocumentType` Get
  - param `pIJournalEntryDocumentTypeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As JournalEntryDocumentTypeServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/JournalEntryDocumentTypeServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As JournalEntryDocumentTypeParamsCollection` GetList
- `Public Sub Update(ByVal pIJournalEntryDocumentType As JournalEntryDocumentType)` Update
  - param `pIJournalEntryDocumentType`:

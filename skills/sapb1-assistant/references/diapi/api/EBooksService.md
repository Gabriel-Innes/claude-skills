<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EBooksService (Object)

Source table: OEBK.

## Methods (7)
- `Public Function Get(ByVal pIEBooksParams As EBooksParams) As EBooks` Get
  - param `pIEBooksParams`: 
- `Public Function GetByDocKey(ByVal pIEBooksParams As EBooksParams) As EBooksParamsCollection` Return the object which is linked with a certain document.
  - param `pIEBooksParams`: 
- `Public Function GetByMark(ByVal pIEBooksParams As EBooksParams) As EBooks` Return the object by EBK.
  - param `pIEBooksParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As EBooksServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/EBooksServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Sub Update(ByVal pIEBooks As EBooks)` Update
  - param `pIEBooks`:

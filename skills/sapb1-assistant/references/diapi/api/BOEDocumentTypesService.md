<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BOEDocumentTypesService (Object)

This service manages document types in SAP Business One. Mandatory properties: DocDescription, DocType. Source table: ODTY.

## Methods (8)
- `Public Function AddBOEDocumentType(ByVal pIBOEDocumentType As BOEDocumentType) As BOEDocumentTypeParams` Adds a DocumentType with DocType and DocDescription as specified in the BOEDocumentType data structure.
  - param `pIBOEDocumentType`: Specifies the BOE document type to be added.
- `Public Sub DeleteBOEDocumentType(ByVal pIBOEDocumentTypeParams As BOEDocumentTypeParams)` Deletes a DocumentType with DocEntry specified in BOEDocumentTypeParams.
  - param `pIBOEDocumentTypeParams`: BOEDocumentTypeParams
- `Public Function GetBOEDocumentType(ByVal pIBOEDocumentTypeParams As BOEDocumentTypeParams) As BOEDocumentType` Returns an instance of the BOEDocumentType data structure.
  - param `pIBOEDocumentTypeParams`: BOEDocumentType
- `Public Function GetBOEDocumentTypeList() As BOEDocumentTypesParams` Returns a collection of instances for the BOEDocumentTypes data structure.
- `Public Function GetDataInterface(ByVal enumMSDI As BOEDocumentTypesServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BOEDocumentTypesServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates a data structure from specified XML file.
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates a data structure from a specified XML string.
  - param `bstrXMLString`: 
- `Public Sub UpdateBOEDocumentType(ByVal pIBOEDocumentType As BOEDocumentType)` Replaces DocType and DocDescription of DocumentType with the specified BOEDocumentTypes data structure.
  - param `pIBOEDocumentType`:

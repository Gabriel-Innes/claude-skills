<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CustomsDeclarationService (Object)

The CustomsDeclarationService enables to manage the Cargo Customs Declarations (CCD). The service enables to add, update, get and delete CCDs. Mandatory properties: CCDNum (primary key). Source table: OCCD.

## Methods (7)
- `Public Function AddCustomsDeclaration(ByVal pICustomsDeclaration As CustomsDeclaration) As CustomsDeclarationParams` Defines a new CCD entry.
  - param `pICustomsDeclaration`: The data for the new customs declaration.
- `Public Sub DeleteCustomsDeclaration(ByVal pICustomsDeclarationParams As CustomsDeclarationParams)` Deletes an existing CCD entry specified in CustomsDeclarationParams.
  - param `pICustomsDeclarationParams`: The key of the customs declaration to be deleted.
- `Public Function GetCustomsDeclaration(ByVal pICustomsDeclarationParams As CustomsDeclarationParams) As CustomsDeclaration` Retrieves information about an existing CCD entry specified in CustomsDeclarationParams.
  - param `pICustomsDeclarationParams`: The key of the customs declaration to be retrieved.
- `Public Function GetDataInterface(ByVal enumMSDI As CustomsDeclarationServiceDataInterfaces) As Object` Creates an empty data interface. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/CustomsDeclarationServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Retrieves the Data Interface from XML file.
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Retrieves the Data Interface from XML string.
  - param `bstrXMLString`: 
- `Public Sub UpdateCustomsDeclaration(ByVal pICustomsDeclaration As CustomsDeclaration)` Updates an existing CCD entry.
  - param `pICustomsDeclaration`: The data for the customs declaration to be updated.

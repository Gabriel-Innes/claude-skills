<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ExtendedTranslationsService (Object)

ExtendedTranslationsService Class

## Methods (8)
- `Public Function AddExtendedTranslation(ByVal pIExtendedTranslation As ExtendedTranslation) As ExtendedTranslationParams` AddExtendedTranslation
  - param `pIExtendedTranslation`: 
- `Public Sub DeleteExtendedTranslation(ByVal pIExtendedTranslationParams As ExtendedTranslationParams)` DeleteExtendedTranslation
  - param `pIExtendedTranslationParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ExtendedTranslationsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ExtendedTranslationsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetExtendedTranslation(ByVal pIExtendedTranslationParams As ExtendedTranslationParams) As ExtendedTranslation` GetExtendedTranslation
  - param `pIExtendedTranslationParams`: 
- `Public Function GetExtendedTranslationList() As ExtendedTranslationsParams` GetExtendedTranslationList
- `Public Sub UpdateExtendedTranslation(ByVal pIExtendedTranslation As ExtendedTranslation)` UpdateExtendedTranslation
  - param `pIExtendedTranslation`:

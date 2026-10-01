<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CampaignResponseTypeService (Object)

CampaignResponseTypeService Class

## Methods (8)
- `Public Function AddResponseType(ByVal pICampaignResponseType As CampaignResponseType) As CampaignResponseTypeParams` AddResponseType
  - param `pICampaignResponseType`: 
- `Public Sub DeleteResponseType(ByVal pICampaignResponseTypeParams As CampaignResponseTypeParams)` DeleteResponseType
  - param `pICampaignResponseTypeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As CampaignResponseTypeServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/CampaignResponseTypeServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetResponseType(ByVal pICampaignResponseTypeParams As CampaignResponseTypeParams) As CampaignResponseType` GetResponseType
  - param `pICampaignResponseTypeParams`: 
- `Public Function GetResponseTypeList() As CampaignResponseTypeParamsCollection` GetResponseTypeList
- `Public Sub UpdateResponseType(ByVal pICampaignResponseType As CampaignResponseType)` UpdateResponseType
  - param `pICampaignResponseType`:

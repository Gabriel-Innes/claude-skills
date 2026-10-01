<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# IntegrationPackagesConfigureService (Object)

IntegrationPackagesConfigureService Class

## Methods (6)
- `Public Function Get(ByVal pIIntegrationPackageParams As IntegrationPackageParams) As IntegrationPackageConfigure` Get
  - param `pIIntegrationPackageParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As IntegrationPackagesConfigureServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/IntegrationPackagesConfigureServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As IntegrationPackagesParams` GetList
- `Public Sub Update(ByVal pIIntegrationPackageConfigure As IntegrationPackageConfigure)` Update
  - param `pIIntegrationPackageConfigure`:

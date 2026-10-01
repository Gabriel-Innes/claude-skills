<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DashboardPackagesService (Object)

DashboardPackagesService Class

## Methods (4)
- `Public Function GetDataInterface(ByVal enumMSDI As DashboardPackagesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/DashboardPackagesServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function ImportDashboardPackage(ByVal pIDashboardPackageImportParams As DashboardPackageImportParams) As DashboardPackageParams` ImportDashboardPackage
  - param `pIDashboardPackageImportParams`:

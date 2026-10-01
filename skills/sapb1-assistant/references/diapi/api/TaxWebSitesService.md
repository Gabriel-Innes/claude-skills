<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxWebSitesService (Object)

TaxWebSitesService Class

## Methods (10)
- `Public Function AddTaxWebSite(ByVal pITaxWebSite As TaxWebSite) As TaxWebSiteParams` AddTaxWebSite
  - param `pITaxWebSite`: 
- `Public Function GetDataInterface(ByVal enumMSDI As TaxWebSitesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/TaxWebSitesServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetDefaultWebSite() As TaxWebSiteParams` GetDefaultWebSite
- `Public Function GetTaxWebSite(ByVal pITaxWebSiteParams As TaxWebSiteParams) As TaxWebSite` GetTaxWebSite
  - param `pITaxWebSiteParams`: 
- `Public Function GetTaxWebSiteList() As TaxWebSitesParams` GetTaxWebSiteList
- `Public Sub RemoveTaxWebSite(ByVal pITaxWebSiteParams As TaxWebSiteParams)` RemoveTaxWebSite
  - param `pITaxWebSiteParams`: 
- `Public Sub SetAsDefault(ByVal pITaxWebSiteParams As TaxWebSiteParams)` SetAsDefault
  - param `pITaxWebSiteParams`: 
- `Public Sub UpdateTaxWebSite(ByVal pITaxWebSite As TaxWebSite)` UpdateTaxWebSite
  - param `pITaxWebSite`:

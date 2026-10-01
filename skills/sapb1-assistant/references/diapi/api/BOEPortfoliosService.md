<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BOEPortfoliosService (Object)

This service manages Portfolios in SAP Business One. Mandatory properties: PortfolioCode, PortfolioDescription, PortfolioID, PortfolioNum. Source table: OPTF.

## Methods (8)
- `Public Function AddBOEPortfolio(ByVal pIBOEPortfolio As BOEPortfolio) As BOEPortfolioParams` Adds a Portfolio with data as specified in the BOEPortfolio data structure.
  - param `pIBOEPortfolio`: Specifies the BOE portfolio to be added.
- `Public Sub DeleteBOEPortfolio(ByVal pIBOEPortfolioParams As BOEPortfolioParams)` Deletes Portfolio with PortfolioEntry specified in BOEPortfolioParams.
  - param `pIBOEPortfolioParams`: BOEPortfolioParams
- `Public Function GetBOEPortfolio(ByVal pIBOEPortfolioParams As BOEPortfolioParams) As BOEPortfolio` Returns an instance of the BOEPortfolio data structure.
  - param `pIBOEPortfolioParams`: BOEPortfolio
- `Public Function GetBOEPortfolioList() As BOEPortfoliosParams` Returns a collection of instances for the BOEPortfolio data structure.
- `Public Function GetDataInterface(ByVal enumMSDI As BOEPortfoliosServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BOEPortfoliosServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` BOEPortfoliosService Object
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates a data structure from a specified XML string.
  - param `bstrXMLString`: 
- `Public Sub UpdateBOEPortfolio(ByVal pIBOEPortfolio As BOEPortfolio)` Replaces fields of Portfolio with the specified BOEPortfolio data structure.
  - param `pIBOEPortfolio`: Specifies the BOE portfolio to be updated.

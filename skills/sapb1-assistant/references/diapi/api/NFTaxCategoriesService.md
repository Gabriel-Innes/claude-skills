<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# NFTaxCategoriesService (Object)

NFTaxCategoriesService Class

## Methods (8)
- `Public Function Add(ByVal pINFTaxCategory As NFTaxCategory) As NFTaxCategoryParams` Add
  - param `pINFTaxCategory`: 
- `Public Sub Delete(ByVal pINFTaxCategoryParams As NFTaxCategoryParams)` Delete
  - param `pINFTaxCategoryParams`: 
- `Public Function Get(ByVal pINFTaxCategoryParams As NFTaxCategoryParams) As NFTaxCategory` Get
  - param `pINFTaxCategoryParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As NFTaxCategoriesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/NFTaxCategoriesServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As NFTaxCategoryParamsCollection` GetList
- `Public Sub Update(ByVal pINFTaxCategory As NFTaxCategory)` Update
  - param `pINFTaxCategory`:

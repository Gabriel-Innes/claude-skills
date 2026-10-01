<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PostingTemplatesService (Object)

PostingTemplatesService Class

## Methods (8)
- `Public Function Add(ByVal pIPostingTemplates As PostingTemplates) As PostingTemplatesParams` Add
  - param `pIPostingTemplates`: 
- `Public Sub Delete(ByVal pIPostingTemplatesParams As PostingTemplatesParams)` Delete
  - param `pIPostingTemplatesParams`: 
- `Public Function Get(ByVal pIPostingTemplatesParams As PostingTemplatesParams) As PostingTemplates` Get
  - param `pIPostingTemplatesParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As PostingTemplatesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/PostingTemplatesServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As PostingTemplatesParamsCollection` GetList
- `Public Sub Update(ByVal pIPostingTemplates As PostingTemplates)` Update
  - param `pIPostingTemplates`:

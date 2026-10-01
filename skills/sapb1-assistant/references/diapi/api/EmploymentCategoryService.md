<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EmploymentCategoryService (Object)

Source table: OETC.

**Remarks:** For the Italy localization only. Navigation path: Business Partner Master Data → Accounting → Tax, select the checkbox Subject to Withholding Tax and go to the field Employment Category.

## Methods (7)
- `Public Function AddEmploymentCategory(ByVal pIEmploymentCategory As EmploymentCategory) As EmploymentCategoryParams` AddEmploymentCategory
  - param `pIEmploymentCategory`: 
- `Public Function GetDataInterface(ByVal enumMSDI As EmploymentCategoryServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/EmploymentCategoryServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetEmploymentCategory(ByVal pIEmploymentCategoryParams As EmploymentCategoryParams) As EmploymentCategory` GetEmploymentCategory
  - param `pIEmploymentCategoryParams`: 
- `Public Function GetEmploymentCategoryList() As EmploymentCategorysParams` GetEmploymentCategoryList
- `Public Sub UpdateEmploymentCategory(ByVal pIEmploymentCategory As EmploymentCategory)` UpdateEmploymentCategory
  - param `pIEmploymentCategory`:

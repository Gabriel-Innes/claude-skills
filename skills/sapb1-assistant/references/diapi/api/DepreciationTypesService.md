<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DepreciationTypesService (Object)

The DepreciationTypesService service enables you to create, update, and view depreciation types. Source table: ODTP.

**Remarks:** To access the Depreciation Types - Setup window, from the SAP Business One Main Menu, choose Administration --> Setup --> Financials --> Fixed Assets --> Depreciation Types.

## Methods (8)
- `Public Function Add(ByVal pIDepreciationType As DepreciationType) As DepreciationTypeParams` Add
  - param `pIDepreciationType`: 
- `Public Sub Delete(ByVal pIDepreciationTypeParams As DepreciationTypeParams)` Delete
  - param `pIDepreciationTypeParams`: 
- `Public Function Get(ByVal pIDepreciationTypeParams As DepreciationTypeParams) As DepreciationType` Get
  - param `pIDepreciationTypeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As DepreciationTypesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/DepreciationTypesServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As DepreciationTypeParamsCollection` GetList
- `Public Sub Update(ByVal pIDepreciationType As DepreciationType)` Update
  - param `pIDepreciationType`:

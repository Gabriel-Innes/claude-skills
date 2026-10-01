<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DepreciationAreasService (Object)

The DepreciationAreasService service enables you to create, update, and view depreciation areas. Source table: ODPA.

**Remarks:** To open the Depreciation Areas - Setup window, from the SAP Business One Main Menu, choose Administration --> Setup --> Financials --> Fixed Assets --> Depreciation Areas.

## Methods (8)
- `Public Function Add(ByVal pIDepreciationArea As DepreciationArea) As DepreciationAreaParams` Adds a depreciation area.
  - param `pIDepreciationArea`: The data for the new depreciation area.
- `Public Sub Delete(ByVal pIDepreciationAreaParams As DepreciationAreaParams)` Deletes an existing depreciation area.
  - param `pIDepreciationAreaParams`: The key of the depreciation area to be deleted.
- `Public Function Get(ByVal pIDepreciationAreaParams As DepreciationAreaParams) As DepreciationArea` Retrieves a depreciation area. The depreciation area is specified by its key, which is contained in the DepreciationAreaParams object passed to the method.
  - param `pIDepreciationAreaParams`: The key of the depreciation area to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As DepreciationAreasServiceDataInterfaces) As Object` Creates an empty data structure for use with the DepreciationAreasService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/DepreciationAreasServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As DepreciationAreaParamsCollection` Returns the DepreciationAreaParamsCollection data collection that identifies all depreciation areas.
- `Public Sub Update(ByVal pIDepreciationArea As DepreciationArea)` Updates an existing depreciation area. The data for the depreciation area, including the key of the depreciation area to be updated, is contained in the DepreciationArea object passed to the method. To update a depreciation area, you must first retrieve it using the Get method.
  - param `pIDepreciationArea`: The data for the depreciation area to be updated. The DepreciationArea object must contain the key of the object to be updated.

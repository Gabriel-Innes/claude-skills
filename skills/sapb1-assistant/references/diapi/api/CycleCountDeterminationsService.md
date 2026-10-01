<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CycleCountDeterminationsService (Object)

You can setup cycle count determinations via this service. Menu entry: Administration > Setup -> Inventory -> Cycle Count Determination

## Methods (6)
- `Public Function Get(ByVal pICycleCountDeterminationParams As CycleCountDeterminationParams) As CycleCountDetermination` Retrieves a CycleCountDetermination rule.
  - param `pICycleCountDeterminationParams`: 
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetDataInterface(ByVal enumMSDI As CycleCountDeterminationsServiceDataInterfaces) As Object` Creates an empty data structure for use with the CycleCountDeterminationsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/CycleCountDeterminationsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Retrieves the Data Interface from XML file.
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates data structure from specified XML string.
  - param `bstrXMLString`: 
- `Public Function GetList() As CycleCountDeterminationParamsCollection` Returns the CycleCountDeterminationParamsCollectionCollection data collection that identifies all cycle count determination rules.
- `Public Sub Update(ByVal pICycleCountDetermination As CycleCountDetermination)` Adds an empty object to the collection.
  - param `pICycleCountDetermination`: 
  - C# example (from SAP's help):
    ```csharp
    CycleCountDeterminationsService ccdService = (CycleCountDeterminationsService)oCompany.GetCompanyService().GetBusinessService(ServiceTypes.CycleCountDeterminationsService);
           CycleCountDeterminationParams ccdParams = (CycleCountDeterminationParams)ccdService.GetDataInterface(CycleCountDeterminationsServiceDataInterfaces.ccdsCycleCountDeterminationParams);
           CycleCountDetermination ccd = (CycleCountDetermination)ccdService.GetDataInterface(CycleCountDeterminationsServiceDataInterfaces.ccdsCycleCountDetermination);

           ccdParams.WarehouseCode = "01";
           ccd = ccdService.Get(ccdParams);

           ccd.CycleBy = CycleCountDeterminationCycleByEnum.ccdcbWarehouseSublevel1;
           ccdService.Update(ccd);

           CycleCountDeterminationSetupCollection ccdSetups = ccd.CycleCountDeterminationSetupCollection;
           ccdSetups.Item(1).CycleCode = 2;
           ccdSetups.Item(1).DestinationUser = 2;
           ccdSetups.Item(1).Alert = BoYesNoEnum.tYES;
           ccdSetups.Item(1).ChangeExistingItems = BoYesNoEnum.tYES;
           ccdService.Update(ccd);
    ```

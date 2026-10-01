<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# Resource (Object)

A resource is defined as a commodity, machine, labor, or other asset used to produce goods and services. As opposed to items, resources have capacity available throughout a period of time which can be consumed in a production process. Resources (resource capacity) can therefore be assigned to production orders. Resource capacity is always viewed within a period of time called "capacity period". Consumption of resources in a production process contributes to the overall production costs and can be split into underlying cost elements for further accounting purposes. Source table: ORSC.

**Remarks:** From the SAP Business One Main Menu, choose Resources → Resource Master Data.

**Example:**
- C# example (from SAP's help):
  ```csharp
  SAPbobsCOM.CompanyService oCS = (SAPbobsCOM.CompanyService)oCompany.GetCompanyService();
  SAPbobsCOM.ResourcesService srvResources = (SAPbobsCOM.ResourcesService)oCS.GetBusinessService(SAPbobsCOM.ServiceTypes.ResourcesService);
  SAPbobsCOM.Resource res = (SAPbobsCOM.Resource)srvResources.GetDataInterface(SAPbobsCOM.ResourcesServiceDataInterfaces.rsdiResource);

  res.VisCode = "r1";
  SAPbobsCOM.ResourceWarehouse Whs = res.Warehouses.Add();
  Whs.Warehouse = "01";

  SAPbobsCOM.ResourceDailyCapacity DC = res.DailyCapacities.Add();
  DC.Weekday = SAPbobsCOM.ResourceDailyCapacityWeekdayEnum.rdcwFirst;
  DC.Factor1 = 1;

  SAPbobsCOM.ResourceParams ret = srvResources.Add(res);
  ```
- C# example (from SAP's help):
  ```csharp
  SAPbobsCOM.ResourceParams par = (SAPbobsCOM.ResourceParams)srvResources.GetDataInterface(SAPbobsCOM.ResourcesServiceDataInterfaces.rsdiResourceParams);
  par.Code = ret.Code; //"r1";
  SAPbobsCOM.Resource res2 = srvResources.Get(par);
  res2.Name = "name";
  srvResources.Update(res2);
  ```

## Properties (110)
- `Public Property Active() As BoYesNoEnum` [R/W] Determines whether the resource is actvie. Field name: validFor.
- `Public Property ActiveFrom() As Date` [R/W] The start date of the active period for the resource. Field name: validFrom.
- `Public Property ActiveRemarks() As String` [R/W] Remarks for the avtive resource. Field name: ValidComm. Length: 30 characters.
- `Public Property ActiveTo() As Date` [R/W] The end date of the active period for the resource. Field name: validTo.
- `Public Property Allocation() As ResourceAllocationEnum` [R/W] Determines how the resource is allocated. Field name: ResAlloc.
- `Public Property AttachmentEntry() As String` [R/W] The attachment for the resource. Field name: Attachment. Length: 16 characters.
- `Public Property Code() As String` [R] The resource code. Field name: ResCode.
- `Public Property CodeBar() As String` [R/W] Bar code for the resource. You can only enter one bar code per resource. Field name: CodeBars. Length: 254 characters.
- `Public Property Cost1() As Double` [R/W] Resource cost 1. Field name: StdCost1.
  - remarks: Consumption of resources on a production order automatically adds these separate resource costs to separate WIP and expense accrual accounts.
- `Public Property Cost10() As Double` [R/W] Resource cost 10. Field name: StdCost10.
- `Public Property Cost2() As Double` [R/W] Resource cost 2. Field name: StdCost2.
- `Public Property Cost3() As Double` [R/W] Resource cost 3. Field name: StdCost3.
- `Public Property Cost4() As Double` [R/W] Resource cost 4. Field name: StdCost4.
- `Public Property Cost5() As Double` [R/W] Resource cost 5. Field name: StdCost5.
- `Public Property Cost6() As Double` [R/W] Resource cost 6. Field name: StdCost6.
- `Public Property Cost7() As Double` [R/W] Resource cost 7. Field name: StdCost7.
- `Public Property Cost8() As Double` [R/W] Resource cost 8. Field name: StdCost8.
- `Public Property Cost9() As Double` [R/W] Resource cost 9. Field name: StdCost9.
- `Public Property DailyCapacities() As ResourceDailyCapacities` [R] The total daily standard capacity is automatically calculated in this field by multiplying the factors.
- `Public Property DefaultWarehouse() As String` [R/W] The default warehouse for the resource. Field name: DfltWH. Length: 8 characters.
- `Public Property Employees() As ResourceEmployees` [R] If the resource type is Labor, you can associate employees with the resource.
- `Public Property FixedAssets() As ResourceFixedAssets` [R] If the resource type is Machine, you can associate fixed assets with the resource.
- `Public Property ForeignName() As String` [R/W] The resource description in foreign language. Field name: FrgnName. Length: 100 characters.
- `Public Property Group() As Long` [R/W] The group to which you want to assign the resource. Field name: ResGrpCod.
- `Public Property Inactive() As BoYesNoEnum` [R/W] Determines whether the resource is freezed. Field name: frozenFor.
- `Public Property InactiveFrom() As Date` [R/W] The start date of the period for which you freeze the resource. Field name: frozenFrom.
- `Public Property InactiveRemarks() As String` [R/W] Remarks for the inavtive resource. Field name: FrozenComm. Length: 30 characters.
- `Public Property InactiveTo() As Date` [R/W] The end date of the period for which you freeze the resource. Field name: frozenTo.
- `Public Property IssueMethod() As ResourceIssueMethodEnum` [R/W] The issue method for the resource consumption. Field name: IssueMthd.
- `Public Property LinkedItem() As String` [R] Displays the non-inventory item that is linked to this resource. The item code of the non-inventory item is the same as the resource code of the linked resource. Field name: LinkItm.
- `Public Property Name() As String` [R/W] The resource description. Field name: ResName. Length: 100 characters.
- `Public Property Number() As Long` [R] The resource number. Field name: Number.
- `Public Property Picture() As String` [R/W] The picture for the resource. Field name: PicturName. Length: 200 characters.
- `Public Property Property1() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup1.
- `Public Property Property10() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup10.
- `Public Property Property11() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup11.
- `Public Property Property12() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup12.
- `Public Property Property13() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup13.
- `Public Property Property14() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup14.
- `Public Property Property15() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup15.
- `Public Property Property16() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup16.
- `Public Property Property17() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup17.
- `Public Property Property18() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup18.
- `Public Property Property19() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup19.
- `Public Property Property2() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup2.
- `Public Property Property20() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup20.
- `Public Property Property21() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup21.
- `Public Property Property22() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup22.
- `Public Property Property23() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup23.
- `Public Property Property24() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup24.
- `Public Property Property25() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup25.
- `Public Property Property26() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup26.
- `Public Property Property27() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup27.
- `Public Property Property28() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup28.
- `Public Property Property29() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup29.
- `Public Property Property3() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup3.
- `Public Property Property30() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup30.
- `Public Property Property31() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup31.
- `Public Property Property32() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup32.
- `Public Property Property33() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup33.
- `Public Property Property34() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup34.
- `Public Property Property35() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup35.
- `Public Property Property36() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup36.
- `Public Property Property37() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup37.
- `Public Property Property38() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup38.
- `Public Property Property39() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup39.
- `Public Property Property4() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup4.
- `Public Property Property40() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup40.
- `Public Property Property41() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup41.
- `Public Property Property42() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup42.
- `Public Property Property43() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup43.
- `Public Property Property44() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup44.
- `Public Property Property45() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup45.
- `Public Property Property46() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup46.
- `Public Property Property47() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup47.
- `Public Property Property48() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup48.
- `Public Property Property49() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup49.
- `Public Property Property5() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup5.
- `Public Property Property50() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup50.
- `Public Property Property51() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup51.
- `Public Property Property52() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup52.
- `Public Property Property53() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup53.
- `Public Property Property54() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup54.
- `Public Property Property55() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup55.
- `Public Property Property56() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup56.
- `Public Property Property57() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup57.
- `Public Property Property58() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup58.
- `Public Property Property59() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup59.
- `Public Property Property6() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup6.
- `Public Property Property60() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup60.
- `Public Property Property61() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup61.
- `Public Property Property62() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup62.
- `Public Property Property63() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup63.
- `Public Property Property64() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup64.
- `Public Property Property7() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup7.
- `Public Property Property8() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup8.
- `Public Property Property9() As BoYesNoEnum` [R/W] The properties to the resource. Field name: QryGroup9.
- `Public Property RelevantForSingleRun1() As BoYesNoEnum` [R/W] Specify whether the factor is relevant to the calculation of Single Run Capacity which is automatically calculated by multiplying all relevant factors. Field name: RelCap1.
  - remarks: Single Run Capacity is introduced on the assumption that a single production order will only be able to be produced on a single machine. It reflects the number of capacity hours a production order can consume on each working day.
- `Public Property RelevantForSingleRun2() As BoYesNoEnum` [R/W] Specify whether the factor is relevant to the calculation of Single Run Capacity which is automatically calculated by multiplying all relevant factors. Field name: RelCap2.
- `Public Property RelevantForSingleRun3() As BoYesNoEnum` [R/W] Specify whether the factor is relevant to the calculation of Single Run Capacity which is automatically calculated by multiplying all relevant factors. Field name: RelCap3.
- `Public Property RelevantForSingleRun4() As BoYesNoEnum` [R/W] Specify whether the factor is relevant to the calculation of Single Run Capacity which is automatically calculated by multiplying all relevant factors. Field name: RelCap4.
- `Public Property Remarks() As String` [R/W] Comments and remarks for the resource. Field name: UserText. Length: 16 characters.
- `Public Property Series() As Long` [R/W] Sets or returns the auto-number series that generated the document number. Field name: Series. This is a foreign key to the Series object.
- `Public Property TimePerUnits() As Long` [R/W] The time per resource units in the <hours:minutes:seconds> format. This field is related to the UnitsPerTime field. Field name: TimeResUn.
- `Public Property Type() As ResourceTypeEnum` [R/W] The resource type. The default value is defined by the selected resource group. Field name: ResType.
- `Public Property UnitOfMeasure() As String` [R/W] A unit of measure for expressing resource capacity. For example, machine cycle, hour, or minute. Field name: UnitOfMsr. Length: 100 characters.
- `Public Property UnitsPerTime() As Long` [R/W] The number of resource units to which the TimePerUnits field relates. The default value is 1. Field name: NumResUnit.
  - remarks: Example: You have a machine that works in cycles. Each cycle takes 15 minutes and it can process 3 items in 1 cycle (3 capacity units within 15 minutes.) In TimePerUnits enter 00:15:00, and in UnitsPerTime enter 3. Alternatively, you can define TimePerUnits as 00:05:00, and UnitsPerTime as 1.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.
- `Public Property VisCode() As String` [R/W] The resource number. Field name: VisResCode. Length: 50 characters.
- `Public Property Warehouses() As ResourceWarehouses` [R] The warehouses for the resource.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ResourceCapacitiesService (Object)

ResourceCapacitiesService Class

## Methods (8)
- `Public Function Add(ByVal pIResourceCapacity As ResourceCapacity) As ResourceCapacityParams` Add
  - param `pIResourceCapacity`: 
- `Public Function Get(ByVal pIResourceCapacityParams As ResourceCapacityParams) As ResourceCapacity` Get
  - param `pIResourceCapacityParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ResourceCapacitiesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ResourceCapacitiesServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As ResourceCapacityParamsCollection` GetList
- `Public Function GetListWithFilter(ByVal pIResourceCapacityWithFilterParams As ResourceCapacityWithFilterParams) As ResourceCapacityParamsCollection` GetListWithFilter
  - param `pIResourceCapacityWithFilterParams`: 
- `Public Sub Update(ByVal pIResourceCapacity As ResourceCapacity)` Update
  - param `pIResourceCapacity`: 

# ResourceCapacity (Object)

Source table: ORCJ.

**Remarks:** From the SAP Business One Main Menu, choose Resources → Resource Capacity.

## Properties (24)
- `Public Property Action() As ResourceCapacityActionEnum` [R/W] property Action
- `Public Property BaseEntry() As Long` [R/W] property BaseEntry
- `Public Property BaseLineNum() As Long` [R/W] property BaseLineNum
- `Public Property BaseType() As ResourceCapacityBaseTypeEnum` [R/W] property BaseType
- `Public Property Capacity() As Double` [R/W] property Capacity
- `Public Property Code() As String` [R/W] property Code
- `Public Property Date() As Date` [R/W] property Date
- `Public Property ID() As Long` [R] property Id
- `Public Property Memo() As String` [R/W] property Memo
- `Public Property MemoSource() As ResourceCapacityMemoSourceEnum` [R/W] property MemoSource
- `Public Property OwningEntry() As Long` [R/W] property OwningEntry
- `Public Property OwningLineNum() As Long` [R/W] property OwningLineNum
- `Public Property OwningType() As ResourceCapacityOwningTypeEnum` [R/W] property OwningType
- `Public Property RevertedEntry() As Long` [R/W] property RevertedEntry
- `Public Property RevertedLineNum() As Long` [R/W] property RevertedLineNum
- `Public Property RevertedType() As ResourceCapacityRevertedTypeEnum` [R/W] property RevertedType
- `Public Property SingleRunCapacity() As Double` [R/W] property SingleRunCapacity
- `Public Property SingleRunMemo() As String` [R/W] property SingleRunMemo
- `Public Property SingleRunMemoSource() As ResourceCapacityMemoSourceEnum` [R/W] property SingleRunMemoSource
- `Public Property SourceEntry() As Long` [R/W] property SourceEntry
- `Public Property SourceLineNum() As Long` [R/W] property SourceLineNum
- `Public Property SourceType() As ResourceCapacitySourceTypeEnum` [R/W] property SourceType
- `Public Property Type() As ResourceCapacityTypeEnum` [R/W] The resource capacity types. Field name: CapType.
- `Public Property Warehouse() As String` [R/W] property Warehouse

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ResourceCapacityParams (Object)

ResourceCapacityParams Class

## Properties (24)
- `Public Property Action() As ResourceCapacityActionEnum` [R] property Action
- `Public Property BaseEntry() As Long` [R] property BaseEntry
- `Public Property BaseLineNum() As Long` [R] property BaseLineNum
- `Public Property BaseType() As ResourceCapacityBaseTypeEnum` [R] property BaseType
- `Public Property Capacity() As Double` [R] property Capacity
- `Public Property Code() As String` [R] property Code
- `Public Property Date() As Date` [R] property Date
- `Public Property ID() As Long` [R/W] property Id
- `Public Property Memo() As String` [R] property Memo
- `Public Property MemoSource() As ResourceCapacityMemoSourceEnum` [R] property MemoSource
- `Public Property OwningEntry() As Long` [R] property OwningEntry
- `Public Property OwningLineNum() As Long` [R] property OwningLineNum
- `Public Property OwningType() As ResourceCapacityOwningTypeEnum` [R] property OwningType
- `Public Property RevertedEntry() As Long` [R] property RevertedEntry
- `Public Property RevertedLineNum() As Long` [R] property RevertedLineNum
- `Public Property RevertedType() As ResourceCapacityRevertedTypeEnum` [R] property RevertedType
- `Public Property SingleRunCapacity() As Double` [R] property SingleRunCapacity
- `Public Property SingleRunMemo() As String` [R] property SingleRunMemo
- `Public Property SingleRunMemoSource() As ResourceCapacityMemoSourceEnum` [R] property SingleRunMemoSource
- `Public Property SourceEntry() As Long` [R] property SourceEntry
- `Public Property SourceLineNum() As Long` [R] property SourceLineNum
- `Public Property SourceType() As ResourceCapacitySourceTypeEnum` [R] property SourceType
- `Public Property Type() As ResourceCapacityTypeEnum` [R] property Type
- `Public Property Warehouse() As String` [R] property Warehouse

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ResourceCapacityParamsCollection (Collection)

ResourceCapacityParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ResourceCapacityParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ResourceCapacityParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ResourceCapacityWithFilterParams (Object)

ResourceCapacityWithFilterParams Class

## Properties (4)
- `Public Property Code() As String` [R/W] property Code
- `Public Property Date() As Date` [R/W] property Date
- `Public Property Type() As ResourceCapacityTypeEnum` [R/W] property Type
- `Public Property Warehouse() As String` [R/W] property Warehouse

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ResourceDailyCapacities (Collection)

A collection of ResourceDailyCapacity objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As ResourceDailyCapacity` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ResourceDailyCapacity` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub Remove(ByVal vtIndex As Variant)` Removes the object at the specified index.
  - param `vtIndex`: The index of the object to be removed.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ResourceDailyCapacity (Object)

You can plan daily internal capacity which you can later set as default values in the Resources --> Set Daily Internal Capacity window. Source table: RSC6.

**Remarks:** From the SAP Business One Main Menu, choose Resources → Resource Master Data, and choose the Planning Data tab. To set or update daily internal capacity, from the SAP Business One Main Menu, choose Resources Set Daily Internal Capacities. You can access this window from the Resource Capacity window by choosing the Set Daily Internal Capacities button. In this case, all the selection criteria fields inherit the values from the Resource Capacity window.

## Properties (9)
- `Public Property Code() As String` [R] The resource code. Field name: ResCode.
- `Public Property Factor1() As Double` [R/W] Enter up to four daily capacity factors in numbers that determine the overall daily capacity of the resource. Field name: CapFactor1.
- `Public Property Factor2() As Double` [R/W] Enter up to four daily capacity factors in numbers that determine the overall daily capacity of the resource. Field name: CapFactor2.
- `Public Property Factor3() As Double` [R/W] Enter up to four daily capacity factors in numbers that determine the overall daily capacity of the resource. Field name: CapFactor3.
- `Public Property Factor4() As Double` [R/W] Enter up to four daily capacity factors in numbers that determine the overall daily capacity of the resource. Field name: CapFactor4.
- `Public Property Remarks() As String` [R/W] Comments and remarks. Field name: Remarks. Length: 100 characters.
- `Public Property SingleRun() As Double` [R/W] Single run capacity, which reflects the number of capacity hours a production order can consume on each working day. Field name: SngRunCap.
- `Public Property Total() As Double` [R/W] Total daily capacity. Field name: CapTotal.
- `Public Property Weekday() As ResourceDailyCapacityWeekdayEnum` [R/W] Days in a week. Field name: WeekDay.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ResourceEmployee (Object)

If the resource type is Labor, you can associate employees with the resource. Source table: RSC4.

## Properties (2)
- `Public Property Code() As String` [R] The resource that you associate employees with. Field name: ResCode.
- `Public Property Employee() As Long` [R/W] The employee that you associate resource with. Field name: EmpID. Length: 11 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ResourceEmployees (Collection)

A collection of ResourceEmployee objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As ResourceEmployee` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ResourceEmployee` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub Remove(ByVal vtIndex As Variant)` Removes the object at the specified index.
  - param `vtIndex`: The index of the object to be removed.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ResourceFixedAsset (Object)

If the resource type is Machine, you can associate fixed assets with the resource. Source table: RSC3.

## Properties (2)
- `Public Property Code() As String` [R] The resource that you associate fixed assets with. Field name: ResCode.
- `Public Property ItemCode() As String` [R/W] The item that you associate resource with. Field name: ItemCode. Length: 50 characters.
  - remarks: One resource can be associated with multiple fixed assets, but one fixed asset can be associated with one resource only.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ResourceFixedAssets (Collection)

A collection of ResourceFixedAsset objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As ResourceFixedAsset` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ResourceFixedAsset` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub Remove(ByVal vtIndex As Variant)` Removes the object at the specified index.
  - param `vtIndex`: The index of the object to be removed.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ResourceGroup (Object)

ResourceGroup Class

## Properties (24)
- `Public Property Code() As Long` [R] property Code
- `Public Property Cost1() As Double` [R/W] property Cost 1
- `Public Property Cost10() As Double` [R/W] property Cost 10
- `Public Property Cost2() As Double` [R/W] property Cost 2
- `Public Property Cost3() As Double` [R/W] property Cost 3
- `Public Property Cost4() As Double` [R/W] property Cost 4
- `Public Property Cost5() As Double` [R/W] property Cost 5
- `Public Property Cost6() As Double` [R/W] property Cost 6
- `Public Property Cost7() As Double` [R/W] property Cost 7
- `Public Property Cost8() As Double` [R/W] property Cost 8
- `Public Property Cost9() As Double` [R/W] property Cost 9
- `Public Property CostName1() As String` [R/W] property Cost Name 1
- `Public Property CostName10() As String` [R/W] property Cost Name 10
- `Public Property CostName2() As String` [R/W] property Cost Name 2
- `Public Property CostName3() As String` [R/W] property Cost Name 3
- `Public Property CostName4() As String` [R/W] property Cost Name 4
- `Public Property CostName5() As String` [R/W] property Cost Name 5
- `Public Property CostName6() As String` [R/W] property Cost Name 6
- `Public Property CostName7() As String` [R/W] property Cost Name 7
- `Public Property CostName8() As String` [R/W] property Cost Name 8
- `Public Property CostName9() As String` [R/W] property Cost Name 9
- `Public Property Name() As String` [R/W] property Name
- `Public Property NumOfUnitsText() As String` [R/W] property NumOfUnitsText
- `Public Property Type() As ResourceTypeEnum` [R/W] property Type

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ResourceGroupParams (Object)

ResourceGroupParams Class

## Properties (2)
- `Public Property Code() As Long` [R/W] property Code
- `Public Property Name() As String` [R] property Name

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ResourceGroupParamsCollection (Collection)

ResourceGroupParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ResourceGroupParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ResourceGroupParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ResourceGroupsService (Object)

ResourceGroupsService Class

## Methods (8)
- `Public Function Add(ByVal pIResourceGroup As ResourceGroup) As ResourceGroupParams` Add
  - param `pIResourceGroup`: 
- `Public Sub Delete(ByVal pIResourceGroupParams As ResourceGroupParams)` Delete
  - param `pIResourceGroupParams`: 
- `Public Function Get(ByVal pIResourceGroupParams As ResourceGroupParams) As ResourceGroup` Get
  - param `pIResourceGroupParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ResourceGroupsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ResourceGroupsServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As ResourceGroupParamsCollection` GetList
- `Public Sub Update(ByVal pIResourceGroup As ResourceGroup)` Update
  - param `pIResourceGroup`: 

# ResourceParams (Object)

This object is used to pass keys to and retrieve keys from ResourcesService methods.

## Properties (1)
- `Public Property Code() As String` [R/W] The resource code. Field name: ResCode. Length: 50 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ResourceParamsCollection (Collection)

A collection of ResourceParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ResourceParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ResourceParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ResourcePropertiesService (Object)

ResourcePropertiesService Class

## Methods (6)
- `Public Function Get(ByVal pIResourcePropertyParams As ResourcePropertyParams) As ResourceProperty` Get
  - param `pIResourcePropertyParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ResourcePropertiesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ResourcePropertiesServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As ResourcePropertyParamsCollection` GetList
- `Public Sub Update(ByVal pIResourceProperty As ResourceProperty)` Update
  - param `pIResourceProperty`: 

# ResourceProperty (Object)

Source table: ORSG.

## Properties (2)
- `Public Property Code() As Long` [R] property Code
- `Public Property Name() As String` [R/W] property Name

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ResourcePropertyParams (Object)

ResourcePropertyParams Class

## Properties (2)
- `Public Property Code() As Long` [R/W] property Code
- `Public Property Name() As String` [R] property Name

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ResourcePropertyParamsCollection (Collection)

ResourcePropertyParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ResourcePropertyParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ResourcePropertyParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ResourcesService (Object)

The ResourcesService service enables you to add, look up, update, and delete resources in SAP Business One. Source table: ORSC.

**Example:**
- C# example (from SAP's help):
  ```csharp
  SAPbobsCOM.CompanyService oCS = (SAPbobsCOM.CompanyService)oCompany.GetCompanyService();
  SAPbobsCOM.ResourcesService srvResources = (SAPbobsCOM.ResourcesService)oCS.GetBusinessService(SAPbobsCOM.ServiceTypes.ResourcesService);
  SAPbobsCOM.Resource res = (SAPbobsCOM.Resource)srvResources.GetDataInterface(SAPbobsCOM.ResourcesServiceDataInterfaces.rsdiResource);

  res.VisCode = "r1";
  SAPbobsCOM.ResourceWarehouse Whs = res.Warehouses.Add();
  Whs.Warehouse = "01";

  SAPbobsCOM.ResourceDailyCapacity DC = res.DailyCapacities.Add();
  DC.Weekday = SAPbobsCOM.ResourceDailyCapacityWeekdayEnum.rdcwFirst;
  DC.Factor1 = 1;

  SAPbobsCOM.ResourceParams ret = srvResources.Add(res);
  ```
- C# example (from SAP's help):
  ```csharp
  SAPbobsCOM.ResourceParams par = (SAPbobsCOM.ResourceParams)srvResources.GetDataInterface(SAPbobsCOM.ResourcesServiceDataInterfaces.rsdiResourceParams);
  par.Code = ret.Code; //"r1";
  SAPbobsCOM.Resource res2 = srvResources.Get(par);
  res2.Name = "name";
  srvResources.Update(res2);
  ```

## Methods (9)
- `Public Function Add(ByVal pIResource As Resource) As ResourceParams` Adds a new resource.
  - param `pIResource`: The data for the new resource.
- `Public Sub CreateLinkedItem(ByVal pIResourceParams As ResourceParams)` Creates a non-inventory item that links to the resource.
  - param `pIResourceParams`: The key of the resource to be linked.
  - remarks: By linking resources to non-inventory items, you can purchase and sell these resources in AP/AR order documents (via the existing non-inventory item functionality). This is especially helpful for service-based businesses.
- `Public Sub Delete(ByVal pIResourceParams As ResourceParams)` Deletes an existing resource.
  - param `pIResourceParams`: The key of the resource to be deleted.
- `Public Function Get(ByVal pIResourceParams As ResourceParams) As Resource` Retrieves a resource. The resource is specified by its key, which is contained in the ResourceParams object passed to the method.
  - param `pIResourceParams`: The key of the resource to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As ResourcesServiceDataInterfaces) As Object` Creates an empty data structure for use with the ResourcesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ResourcesServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLFile(Hashtable Properties, String Path)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair In Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        oGeneralData.ToXMLFile(Path);

        //Retrieve XML and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLFile(Path);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLString(Hashtable Properties)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;
        string XMLString;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair in Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        XMLString = oGeneralData.ToXMLString();

        //Retrieve XML string and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLString(XMLString);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetList() As ResourceParamsCollection` Returns the ResourceParamsCollection data collection that identify all resources.
- `Public Sub Update(ByVal pIResource As Resource)` Updates an existing resource. The data for the resource, including the key of the resource to be updated, is contained in the Resource object passed to the method. To update a resource, you must first retrieve it using the Get method.
  - param `pIResource`: The data for the resource to be updated. The Resource object must contain the key of the object to be updated.

# ResourceWarehouse (Object)

Define warehouses for the resource. Source table: RSC1.

## Properties (4)
- `Public Property Code() As String` [R] The resource code. Field name: ResCode.
- `Public Property Locked() As BoYesNoEnum` [R/W] The warehouse for the resource is locked. Thus prevents you from adding the resource from this warehouse to production orders. Field name: Locked.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.
- `Public Property Warehouse() As String` [R/W] The warehouse code. Field name: WhsCode. Length: 8 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ResourceWarehouses (Collection)

A collection of ResourceWarehouse objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As ResourceWarehouse` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ResourceWarehouse` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub Remove(ByVal vtIndex As Variant)` Removes the object at the specified index.
  - param `vtIndex`: The index of the object to be removed.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# RetornoCode (Object)

RetornoCode Class

## Properties (8)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property BankCode() As String` [R/W] property BankCode
- `Public Property BOEStatus() As BoBoeStatus` [R/W] property BoeStatus
- `Public Property Color() As Long` [R/W] property Color
- `Public Property Description() As String` [R/W] property Description
- `Public Property FileFormat() As String` [R/W] property FileFormat
- `Public Property MovementCode() As Long` [R/W] property MovementCode
- `Public Property OccurenceCode() As Long` [R/W] property OccurenceCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# RetornoCodeParams (Object)

RetornoCodeParams Class

## Properties (8)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property BankCode() As String` [R] property BankCode
- `Public Property BOEStatus() As BoBoeStatus` [R] property BoeStatus
- `Public Property Color() As Long` [R] property Color
- `Public Property Description() As String` [R] property Description
- `Public Property FileFormat() As String` [R] property FileFormat
- `Public Property MovementCode() As Long` [R] property MovementCode
- `Public Property OccurenceCode() As Long` [R] property OccurenceCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# RetornoCodeParamsCollection (Collection)

RetornoCodeParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As RetornoCodeParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As RetornoCodeParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# RetornoCodesService (Object)

RetornoCodesService Class

## Methods (8)
- `Public Function Add(ByVal pIRetornoCode As RetornoCode) As RetornoCodeParams` Add
  - param `pIRetornoCode`: 
- `Public Sub Delete(ByVal pIRetornoCodeParams As RetornoCodeParams)` Delete
  - param `pIRetornoCodeParams`: 
- `Public Function Get(ByVal pIRetornoCodeParams As RetornoCodeParams) As RetornoCode` Get
  - param `pIRetornoCodeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As RetornoCodesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `RetornoCodesServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As RetornoCodeParamsCollection` GetList
- `Public Sub Update(ByVal pIRetornoCode As RetornoCode)` Update
  - param `pIRetornoCode`: 

# RoundedData (Object)

Represents the data after rounding.

## Properties (1)
- `Public Property Value() As Double` [R] The value of the data after rounding.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# RouteStage (Object)

RouteStage Class

## Properties (6)
- `Public Property Code() As String` [R/W] property Code
- `Public Property CreationDate() As Date` [R] property CreationDate
- `Public Property DateOfUpdate() As Date` [R] property DateOfUpdate
- `Public Property Description() As String` [R/W] property Description
- `Public Property GenerationTime() As Date` [R] property GenerationTime
- `Public Property InternalNumber() As Long` [R] property InternalNumber

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# RouteStageParams (Object)

RouteStageParams Class

## Properties (6)
- `Public Property Code() As String` [R] property Code
- `Public Property CreationDate() As Date` [R] property CreationDate
- `Public Property DateOfUpdate() As Date` [R] property DateOfUpdate
- `Public Property Description() As String` [R] property Description
- `Public Property GenerationTime() As Date` [R] property GenerationTime
- `Public Property InternalNumber() As Long` [R/W] property InternalNumber

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# RouteStageParamsCollection (Collection)

RouteStageParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As RouteStageParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As RouteStageParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# RouteStagesService (Object)

RouteStagesService Class

## Methods (8)
- `Public Function Add(ByVal pIRouteStage As RouteStage) As RouteStageParams` Add
  - param `pIRouteStage`: 
- `Public Sub Delete(ByVal pIRouteStageParams As RouteStageParams)` Delete
  - param `pIRouteStageParams`: 
- `Public Function Get(ByVal pIRouteStageParams As RouteStageParams) As RouteStage` Get
  - param `pIRouteStageParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As RouteStagesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `RouteStagesServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As RouteStageParamsCollection` GetList
- `Public Sub Update(ByVal pIRouteStage As RouteStage)` Update
  - param `pIRouteStage`: 

# RoutingDateCalculationInput (Object)

RoutingDateCalculationInput Class

## Properties (9)
- `Public Property CalculateFromDate() As Date` [R/W] property CalculateFromDate
- `Public Property CalculateUntilDate() As Date` [R/W] property CalculateUntilDate
- `Public Property CapacitySum() As Double` [R/W] property CapacitySum
- `Public Property FirstDateProportion() As Double` [R/W] property FirstDateProportion
- `Public Property ResourceAlloc() As ResourceAllocationEnum` [R/W] property ResourceAlloc
- `Public Property ResourceCode() As String` [R/W] property ResourceCode
- `Public Property WarehouseCode() As String` [R/W] property WarehouseCode
- `Public Property WORLine() As Long` [R/W] property WORLine
- `Public Property WORObjAbs() As Long` [R/W] property WORObjAbs

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# RoutingDateCalculationOutput (Object)

RoutingDateCalculationOutput Class

## Properties (2)
- `Public Property Proportion() As Double` [R] property Proportion
- `Public Property ResultDate() As Date` [R] property ResultDate

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# RoutingDateCalculationService (Object)

RoutingDateCalculationService Class

## Methods (4)
- `Public Function Calculate(ByVal pIRoutingDateCalculationInput As RoutingDateCalculationInput) As RoutingDateCalculationOutput` Calculate
  - param `pIRoutingDateCalculationInput`: 
- `Public Function GetDataInterface(ByVal enumMSDI As RoutingDateCalculationServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `RoutingDateCalculationServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 

# SalesAppSetting (Object)

SalesAppSetting Class

## Properties (4)
- `Public Property AdvancedDashBoard() As Long` [R/W] property AdvancedDashBoard
- `Public Property Code() As Long` [R] property Code
- `Public Property CustomerAdvancedDashBoard() As Long` [R/W] property CustomerAdvancedDashBoard
- `Public Property Name() As String` [R/W] property Name

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# SalesAppSettingParams (Object)

SalesAppSettingParams Class

## Properties (2)
- `Public Property Code() As Long` [R/W] property Code
- `Public Property Name() As String` [R/W] property Name

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# SalesForecast (Object)

SalesForecast is a business object that represents the sales forecast for a specified period. The sales forecast is required for planning the purchase and production of items in the MRP module. This object enables you to: - Add a sales forecast. - Retrieve a sales forecast by its key. - Update a sales forecast. - Remove a sales forecast. - Save the object in XML format. Source table: OFCT.

**Remarks:** Mandatory fields in SAP Business One: ForecastCode and ForecastName. To display the form in the application: - Select MRP --> Define Forecasts.

## Properties (9)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property ForecastCode() As String` [R/W] Sets or returns the sales forecast code. Field name: Code Mandatory property. Length: 16 characters.
- `Public Property ForecastEndDate() As Date` [R/W] Sets or returns the end date for the sales forecast. The default is the last day of the current year. Field name: EndDate
  - remarks: Default: end date of current year.
- `Public Property ForecastName() As String` [R/W] Sets or returns the sales forecast name. Mandatory property. Field name: Name Length: 100 characters.
- `Public Property ForecastStartDate() As Date` [R/W] Sets or returns the start date for the sales forecast. The default is the current date. Field name: StartDate
  - remarks: Default: current date.
- `Public Property Lines() As SalesForecast_Lines` [R] Returns the SalesForecast_Lines child object.
- `Public Property Numerator() As Long` [R] Returns the sales forecast absolute ID. Field name: AbsID
  - remarks: This is a sequential number assigned by SAP Business One when adding a sales forecast.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property View() As ForecastViewTypeEnum` [R/W] Indicates whether the lines represent daily, weekly, or monthly forecasts. The default is daily. Field name: FormView
  - remarks: The field cannot be changed after adding the forecast. If you select weeks, the ForecastStartDate and ForecastEndDate must be the start and end of a week. The week is defined at Administration --> System Initialization --> Company Detail --> Accouting Data tab --> Holiday field. If you select months, the ForecastStartDate and ForecastEndDate must be the start and end of a month.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lID`: Sales forecast absolute ID (Numerator).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# SalesForecast_Lines (Object)

SalesForecast_Lines is a child object of SalesForecast object and represents sales forecast of items and their quantity for a specified day. Source table: FCT1.

## Properties (6)
- `Public Property Count() As Long` [R] Returns the total rows in the SalesForecast_Lines list.
- `Public Property ForecastedDay() As Date` [R/W] Sets or returns the forecast date for the specified Quantity. Field name: Date.
  - remarks: If the forecast View property is weekly, the date must be the first day of a week. If the forecast View property is monthly, the date must be the first day of a month.
- `Public Property ItemNo() As String` [R/W] Sets or returns the item code in the inventory. Field name: ItemCode. Length: 20 characters. This is a foreign key to the Items object.
- `Public Property Quantity() As Double` [R/W] Sets or returns the sales forecast quantity of ItemNo for the ForecastedDay. Field name: Quantity.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property Warehouse() As String` [R/W] property Warehouse

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oOrder As SAPbobsCOM.Documents ' Order object

            Dim lRetCode As Integer ' Return Code

            ' New Order

            oOrder = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oOrders)

            ' Fill Order details

            oOrder.CardCode = "C40000"

            oOrder.CardName = "Earthshaker Corporation"

            oOrder.HandWritten = SAPbobsCOM.BoYesNoEnum.tNO

            oOrder.DocDate = Today()

            oOrder.DocDueDate = Today()

            oOrder.DocCurrency = "USD"

            'Fill 2 lines in the order

            oOrder.Lines.ItemCode = "A00001"

            oOrder.Lines.ItemDescription = "IBM Inforprint 1312"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            oOrder.Lines.Add()

            oOrder.Lines.ItemCode = "A00002"

            oOrder.Lines.ItemDescription = "IBM Infoprint 1222"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            ' Now we want to delete the second line in the Order

            oOrder.Lines.Delete()

            ' The Order will be added without the second line

            lRetCode = oOrder.Add
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# SalesOpportunities (Object)

SalesOpportunities is a business object that represents the sales opportunities data in SAP Business One. Sales opportunities include potential sale volumes that may arise from business with customers and interested parties. This object enables you to: - Add a sales opportunity. - Retrieve a sales opportunity by its key. - Update a sales opportunity with the progress of the sales activities and negotiations. - Remove a sales opportunity. - Save the object in XML format. Source table: OOPR.

**Remarks:** Mandatory fields in SAP Business One: CardCode and StartDate. To display the form in the application: - Select Sales Opportunities --> Sales Opportunity.

## Properties (55)
- `Public Property AttachmentEntry() As Long` [R/W] Sets or returns the identification key of the attachment file, as assigned by SAP Business One when adding an Attachment Entry to alert message. Field name: AtcEntry.
- `Public Property BPChanelCode() As String` [R/W] Sets or returns the distribution channel code for the sales opportunity. Field name: ChnCrdCode. Length: 15 characters. This is a foreign key to the BusinessPartners Object.
- `Public Property BPChanelName() As String` [R/W] Sets or returns the distribution channel card name for the sales opportunity. Field name: ChnCrdName. Length: 100 characters.
- `Public Property BPChannelContact() As Long` [R/W] Sets or returns the contact person of the distribution channel for the sales opportunity. Property type Read-write property " --> Field name: ChnCrdCon. This is a foreign key to the ContactEmployees Object.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CardCode() As String` [R/W] Sets or returns the business partner code. Mandatory property. Length: 15 characters. Field name: CardCode.
  - remarks: The type of the business partner code must be Lead or Customer (but not Vendor).
- `Public Property ClosingDate() As Date` [R/W] The closing date of the sales opportunity. Field name: CloseDate.
- `Public Property ClosingGrossProfitLocal() As Double` [R] Returns the closing gross profit in local currency. Field name: RealProfL.
  - remarks: SAP Business One calculates the ClosingGrossProfitLocal property as follows: ClosingGrossProfitLocal = ClosingPercentage * TotalAmountLocal.
- `Public Property ClosingGrossProfitSystem() As Double` [R] Returns the closing gross profit in system currency. Field name: RealProfS.
  - remarks: SAP Business One calculates the ClosingGrossProfitLocal property as follows: ClosingGrossProfitSystem = ClosingPercentage * TotalAmountSystem.
- `Public Property ClosingPercentage() As Double` [R] Sets or returns the propability percentage for closing the sales opportunity. Field name: CloPrcnt.
- `Public Property ClosingType() As BoSoClosedInTypes` [R/W] Sets or returns a valid value of BoSoClosedInTypes type that specifies the date types (days, weeks, or months) for the ClosingDate. Field name: DifType.
- `Public Property Competition() As SalesOpportunitiesCompetition` [R] Returns the SalesOpportunitiesCompetition child object.
- `Public Property ContactPerson() As Long` [R/W] Sets or returns the customer contact person code. Field name: CprCode. This is a foreign key to the ContactEmployees object.
- `Public Property CurrentStageNo() As Double` [R] Returns the current stage number. Field name: StepLast. This is a foreign key to the SalesStages object.
- `Public Property CurrentStageNumber() As Long` [R] property CurrentStageNumber
- `Public Property CustomerName() As String` [R/W] Sets or returns the business partner name who is related to the sales opportunity. Field name: Name. Length: 100 characters.
- `Public Property DataOwnershipfield() As Long` [R/W] Sets or returns the employee ID who is responsible for the sales opportunity. Field name: Owner. This is a foreign key to the Employees table (OHEM), not exposed through the DI API.
- `Public Property DocumentCheckbox() As String` [R] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not restrict the search range for the business partner's documents. Field name: DocChkbox.
- `Public Property GrossProfit() As Double` [R/W] Sets or returns the gross profit percentage. Field name: PrcnProf.
- `Public Property GrossProfitTotalLocal() As Double` [R/W] Sets or returns the total gross profit in local currency. Field name: SumProfL.
  - remarks: SAP Business One calculates the GrossProfitTotalLocal property as follows: GrossProfitTotalLocal = GrossProfit * MaxLocalTotal.
- `Public Property GrossProfitTotalSystem() As Double` [R] Sets or returns the total gross profit in system currency. Field name: SumProfS.
  - remarks: SAP Business One calculates the GrossProfitTotalSystem property as follows: GrossProfitTotalSystem = GrossProfit * MaxSystemTotal.
- `Public Property Industry() As Long` [R/W] Sets or returns the industry ID number. Field name: Industry. This is a foreign key to the Industries object.
- `Public Property InterestField1() As Long` [R/W] Sets or returns the main interest range for the sales opportunity. Field name: IntCat1. This is a foreign key to the Interest table (ooin), not exposed through the DI API.
- `Public Property InterestField2() As Long` [R/W] Sets or returns the secondary interest range for the sales opportunity. Field name: IntCat2. This is a foreign key to the Interest table (ooin), not exposed through the DI API.
- `Public Property InterestField3() As Long` [R/W] Sets or returns the additional interest range for the sales opportunity. Field name: IntCat3. This is a foreign key to the Interest table (ooin), not exposed through the DI API.
- `Public Property InterestLevel() As Long` [R/W] Sets or returns the interest level (for example: warm, cold, general interest, and so on) for the sales opportunity. Field name: IntRate. This is a foreign key to the Interest table (OOIR), not exposed through the DI API.
- `Public Property Interests() As SalesOpportunitiesInterests` [R] Returns the SalesOpportunitiesInterests child object.
- `Public Property Lines() As SalesOpportunitiesLines` [R] Returns the SalesOpportunitiesLines child object.
- `Public Property LinkedDocumentNumber() As String` [R] Sets or returns the document number that is linked to the sales opportunity. Field name: DocNum. Length: 20 characters.
- `Public Property LinkedDocumentType() As Long` [R] Sets or returns the type of the document that is linked to the sales opportunity. For example: sales quotation, sales order, delivery, or A/R invoice. Field name: DocType. Length: 2 characters.
- `Public Property MaxLocalTotal() As Double` [R] Sets or returns the total predicted sales in local currency. Field name: MaxSumLoc.
- `Public Property MaxSystemTotal() As Double` [R] Sets or returns the total predicted sales in system currency. Field name: MaxSumSys.
- `Public Property OpportunityName() As String` [R/W] Sets or returns the opportunity name. Field name: Name. Length: 100 characters.
- `Public Property OpportunityType() As OpportunityTypeEnum` [R/W] property OpportunityType
- `Public Property Partners() As SalesOpportunitiesPartners` [R] Returns the SalesOpportunitiesPartners child object.
- `Public Property PredictedClosingDate() As Date` [R/W] Sets or returns the predicted closing date. Field name: PredDate.
  - remarks: SAP Business One checks predicted closing date that it is grater or equal to the start date of the sales opportunity.
- `Public Property ProjectCode() As String` [R/W] Sets or returns the project code as defined in the Projects object. This is a foreign key to the Projects table (OPRJ). Length: 8 characters. Field name: PrjCode.
- `Public Property ReasonForClosing() As Long` [R/W] Sets or returns the reason for closing (exists only if the status is "Missed"). Field name: Reason. This is a foreign key to the Defect Cause table (OOFR), not exposed through the DI API).
- `Public Property Reasons() As SalesOpportunitiesReasons` [R] Returns the SalesOpportunitiesReasons child object.
- `Public Property Remarks() As String` [R/W] Sets or returns a memo type string that specifies remarks of the sales opportunity. Field name: Memo. Length:64,000 characters.
- `Public Property SalesPerson() As Long` [R/W] Sets or returns the sales person code. Field name: SlpCode. This is a foreign key to the SalesPersons object.
  - remarks: The sales employees can be defined through the SalesPersons object (see SalesEmployeeCode).
- `Public Property SequentialNo() As Long` [R] Returns the key identifier of the sales opportunity record. SAP Business One assigns this key number automatically when adding a sales opportunity. Field name: OpprId.
- `Public Property Source() As Long` [R/W] Sets or returns the source of the sales opportunity, for example, Internet, exposition, consultant, and so on. Field name: Source This is a foreign key to the Information Source table (OOSR), which is exposed via the SalesOpportunitySourcesSetupService object.
- `Public Property StartDate() As Date` [R/W] Sets or returns the start date of the sales opportunity. Mandatory property. Field name: OpenDate.
  - remarks: Default: current date.
- `Public Property Status() As BoSoOsStatus` [R/W] Sets or returns a valid value of BoSoOsStatus type that specifies the summary status of the sales opportunity (Open, Lost, or Won). Field name: Status.
- `Public Property StatusRemarks() As String` [R/W] Sets or returns the status remarks. Length: 30 characters. Field name: StatusRem.
- `Public Property Territory() As Long` [R/W] Sets or returns the sales opportunity territory (segment of the market). Field name: Territory. This is a foreign key to the Territories object. Sets or returns the business partner territory as defined in SAP Business One. Relevant to business partners of customer type only. Field name: Territory. This is a foreign key to the Territories object.
- `Public Property TotalAmounSystem() As Double` [R] Sets or returns the closing total amount of sales in system currency. Field name: RealSumSys.
- `Public Property TotalAmountLocal() As Double` [R/W] Sets or returns the closing total amount of sales in local currency. Field name: SumProfL.
- `Public Property UpdateDate() As Date` [R] property UpdateDate
- `Public Property UpdateTime() As Date` [R] property UpdateTime
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserSignature() As Long` [R] Returns the ID of the user who enters the sales opportunity details. Field name: UserSign. This is a foreign key to the Users object.
- `Public Property WeightedSumLC() As Double` [R] Sets or returns the weighted predicted sales in local currency. Field name: WtSumLoc.
  - remarks: SAP Business One calculates the WeightedSumLC property as follows: WeightedSumLC = ClosingPercentage * MaxLocalTotal.
- `Public Property WeightedSumSC() As Double` [R] Sets or returns the weighted predicted sales in system currency. Field name: WtSumSys.
  - remarks: SAP Business One calculates the WeightedSumSC property as follows: WeightedSumSC = ClosingPercentage * MaxSystemTotal.

## Methods (8)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Close() As Long` Closes a record of the object in SAP Business One database.
  - example note: The following sample shows how to close a document record. Use this sample as a basis to all business objects of document type (not master data type).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Sub CloseDocument()

        Dim RetVal    As Long

        Dim ErrCode   As Long

        Dim ErrMsg    As String

        Dim vOrder As SAPbobsCOM.Documents

        Set vOrder = vCmp.GetBusinessObject(oOrders)

        'Retrieve the document record to close from the database

        RetVal = vOrder.GetByKey("55")

        If RetVal <> 0 Then

            vCmp.GetLastError ErrCode, ErrMsg

            MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

                Exit Sub

        End If

        'Close the record

        RetVal = vOrder.Close

        If RetVal <> 0 Then

            vCmp.GetLastError ErrCode, ErrMsg

            MsgBox "Failed to Close the record " & ErrCode & " " & ErrMsg

        End If

    End Sub
    ```
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal OpprId As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `OpprId`: Specifies the sales opportunity ID (SequentialNo).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# SalesOpportunitiesCompetition (Object)

SalesOpportunityCompetition is a child object of the SalesOpportunities object that represents the competitors of the sales opportunity. Source table: OPR3.

**Remarks:** To display the form in the application: - Select Sales Opportunities --> Sales Opportunity. - Select the Competitors tab.

## Properties (8)
- `Public Property Competition() As Long` [R/W] Sets or returns the Competitors Id. This is a foreign key to the Competitors table (OCMT), which is exposed via the SalesOpportunityCompetitorSetup object. Field name: CompetId.
- `Public Property Count() As Long` [R] Returns the total number of rows in the SalesOpportunitiesCompetition list.
- `Public Property Details() As String` [R/W] Sets or returns the details for the sales opportunity competition. Field name: Details. Length: 50 characters.
- `Public Property RowNo() As Long` [R] Returns the current available row number (starts from 1). Field name: Line.
- `Public Property SequenceNo() As Long` [R] Returns the sales opportunity unique ID (primary key). Field name: OpportId.
- `Public Property ThreatLevel() As ThreatLevelEnum` [R/W] The threat level for a sales opportunity competitor. Field name: ThreatLevl.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WonOrLost() As String` [R/W] Sets or returns a valid value that determines whether the company won or lost the sales opportunity. Field name: Won. Length: 1 character.
  - remarks: Valid values: Y - Won. N - Lost.

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oOrder As SAPbobsCOM.Documents ' Order object

            Dim lRetCode As Integer ' Return Code

            ' New Order

            oOrder = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oOrders)

            ' Fill Order details

            oOrder.CardCode = "C40000"

            oOrder.CardName = "Earthshaker Corporation"

            oOrder.HandWritten = SAPbobsCOM.BoYesNoEnum.tNO

            oOrder.DocDate = Today()

            oOrder.DocDueDate = Today()

            oOrder.DocCurrency = "USD"

            'Fill 2 lines in the order

            oOrder.Lines.ItemCode = "A00001"

            oOrder.Lines.ItemDescription = "IBM Inforprint 1312"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            oOrder.Lines.Add()

            oOrder.Lines.ItemCode = "A00002"

            oOrder.Lines.ItemDescription = "IBM Infoprint 1222"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            ' Now we want to delete the second line in the Order

            oOrder.Lines.Delete()

            ' The Order will be added without the second line

            lRetCode = oOrder.Add
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# SalesOpportunitiesInterests (Object)

SalesOpportunitiesInterests is a child object of the SalesOpportunities object and represents the interests range of sales opportunity. Source table: OPR4.

**Remarks:** To display the form in the application: - Select Sales Opportunities --> Sales Opportunity. - Select the Potential tab (the Interset Range table is enabled only when the sales opportunity status is Open).

## Properties (6)
- `Public Property Count() As Long` [R] Returns the total rows in the SalesOpportunitiesInterests list.
- `Public Property InterestId() As Long` [R/W] Sets or returns the interest ID. This is a foreign key to the Interest table (OOIN), which is exposed via the SalesOpportunityInterestsSetupService object. Field name: IntId.
- `Public Property PrimaryInterest() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the sales opportunity interset is primary. Field name: Prmry.
- `Public Property RowNo() As Long` [R] Returns the current available row number (starts from 1). Field name: Line. Returns the current available row number (starts from 1). Field name: Line_ID.
- `Public Property SequenceNo() As Long` [R] Returns the sales opportunity unique ID (primary key). Field name: OpportId.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oOrder As SAPbobsCOM.Documents ' Order object

            Dim lRetCode As Integer ' Return Code

            ' New Order

            oOrder = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oOrders)

            ' Fill Order details

            oOrder.CardCode = "C40000"

            oOrder.CardName = "Earthshaker Corporation"

            oOrder.HandWritten = SAPbobsCOM.BoYesNoEnum.tNO

            oOrder.DocDate = Today()

            oOrder.DocDueDate = Today()

            oOrder.DocCurrency = "USD"

            'Fill 2 lines in the order

            oOrder.Lines.ItemCode = "A00001"

            oOrder.Lines.ItemDescription = "IBM Inforprint 1312"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            oOrder.Lines.Add()

            oOrder.Lines.ItemCode = "A00002"

            oOrder.Lines.ItemDescription = "IBM Infoprint 1222"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            ' Now we want to delete the second line in the Order

            oOrder.Lines.Delete()

            ' The Order will be added without the second line

            lRetCode = oOrder.Add
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# SalesOpportunitiesLines (Object)

SalesOpportunityLines is a child object of the SalesOpportunities object and represents the stages of the sales opportunity. Source table: OPR1.

**Remarks:** To display the form in the application: - Select Sales Opportunities --> Sales Opportunity. - Select the Stages tab.

## Properties (24)
- `Public Property BPChanelCode() As String` [R/W] Sets or returns the distribution channel code for the stage of the sales opportunity. Field name: ChnCrdCode. Length: 15 characters. This is a foreign key to the BusinessPartners object.
- `Public Property BPChanelName() As String` [R/W] Sets or returns the distribution channel name for the stage of the sales opportunity. Field name: ChnCrdName. Length: 100 characters.
- `Public Property BPChannelContact() As Long` [R/W] Sets or returns the contact person of the distribution channel for the sales opportunity stage. Property type Read-write property " --> Field name: ChnCrdCon. This is a foreign key to the ContactEmployees object.
- `Public Property ClosingDate() As Date` [R/W] Sets or returns the actual date of closing the sales opportunity in the current stage. Field name: CloseDate.
  - remarks: SAP Business One checks this date. The closing date in the last stage must be before or equal to PredictedClosingDate, otherwise, SAP Business One changes the PredictedClosingDate to the actual closing date.
- `Public Property Contact() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies the whether or not the sales opportunity of the current stage is active. Field name: Linked.
- `Public Property ContactPerson() As Long` [R/W] Sets or returns the contact person for the sales opportunity stage. Property type Read-write property " --> Field name: CntctCode. This is a foreign key to the ContactEmployees object.
- `Public Property Count() As Long` [R] Returns the total rows in the SalesOpportunitiesLines list.
  - remarks: When you add a sales opportunity, the Count value is incremented automatically.
- `Public Property DataOwnershipfield() As Long` [R/W] Sets or returns the employee ID who is responsible for the sales opportunity stage. Field name: Owner. This is a foreign key to the EmployeesInfo object.
- `Public Property DocumentCheckbox() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not restrict the search range for the business partner's documents. Field name: DocChkbox.
- `Public Property DocumentNumber() As Long` [R/W] Sets or returns the document ID. Field name: DocNumber.
- `Public Property DocumentType() As BoAPARDocumentTypes` [R/W] Sets or returns the type of Sales - A/R and Purchasing - A/P document.
- `Public Property LineNum() As Long` [R] Returns the current row number in the sales opportunity table. Field name: Line.
- `Public Property MaxLocalTotal() As Double` [R/W] Sets or returns the total predicted sales, in local currency, for the current stage. Field name: MaxSumLoc.
  - remarks: MaxLocalTotal of the last stage must be equal to MaxLocalTotal defined in the SalesOpportunity object (OOPR table), otherwise, SAP Business One updates the MaxLocalTotal defined in OOPR table.
- `Public Property MaxSystemTotal() As Double` [R] Sets or returns the total predicted sales, in system currency, for the current stage. Field name: MaxSumSys.
  - remarks: MaxSystemTotal of the last stage must be equal to MaxSystemTotal defined in the SalesOpportunity object (OOPR table), otherwise, SAP Business One updates the MaxSystemTotal defined in OOPR table.
- `Public Property PercentageRate() As Double` [R/W] Sets or returns the probability percentage to complete the sales stage successfully. Field name: ClosePrcnt.
  - remarks: If the StageKey value is set, SAP Business One automatically sets the PercentageRate value as defined in the ClosingPercentage (of the SalesStages object), however, you can override the PercentageRate value. The PercentageRate in the last stage must be equal to the ClosingPercentage.
- `Public Property Remarks() As String` [R/W] Sets or returns a memo type string that specifies remarks of the sales opportunity for the current stage. Field name: Memo. Length: 64,000 characters.
- `Public Property SalesPerson() As Long` [R/W] Sets or returns the sales person code. Field name: SlpCode. This is a foreign key to the SalesPersons object.
  - remarks: The sales employees can be defined through the SalesPersons object (see SalesEmployeeCode).
- `Public Property SequenceNo() As Long` [R] Returns the sales opportunity unique ID (primary key). Field name: OpportId. Returns the sales opportunity unique ID (primary key). Field name: OpportId.
- `Public Property StageKey() As Long` [R/W] Sets or returns the foreign key of the sales stage. Field name: Step_Id. This is a foreign key to the SalesStages.
  - remarks: The stage code represents a stage name such as, Lead, 1st meeting, Negotiation, and so on. The stage code also defines the PercentageRate.
- `Public Property StartDate() As Date` [R/W] Sets or returns the date of starting the sales opportunity in the current stage. Field name: OpenDate.
  - remarks: SAP Business One checks this date. The start date must be before the close date specified in the last stage, otherwise, SAP Business One sends an error.
- `Public Property Status() As BoSoStatus` [R] Sets or returns a valid value of BoSoStatus type that specifies the sales opportunity status for the current stage (open, missed, or sold). Field name: Status.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WeightedAmountLocal() As Double` [R] Sets or returns the weighted sales, in local currency, for the current stage. Field name: WtSumLoc.
  - remarks: WeightedAmountLocal of the last stage must be equal to WeightedSumLC (predicted amount) defined in the SalesOpportunity object (OOPR table), otherwise, SAP Business One updates the WeightedSumLC.
- `Public Property WeightedAmountSystem() As Double` [R] Sets or returns the weighted sales, in system currency, for the current stage. Field name: WtSumSys.
  - remarks: WeightedAmountSystem of the last stage must be equal to WeightedSumSC (predicted amount) defined in the SalesOpportunity object (OOPR table), otherwise, SAP Business One updates the WeightedSumSC.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# SalesOpportunitiesPartners (Object)

SalesOpportunityPartner is a child object of the SalesOpportunities object that represents the partners of the sales opportunity. Source table: OPR2.

**Remarks:** To display the form in the application: - Select Sales Opportunities --> Sales Opportunity. - Select the Partners tab.

## Properties (7)
- `Public Property Count() As Long` [R] Returns the total rows in the SalesOpportunitiesPartners list.
  - remarks: When you add a partner to the sales opportunity, the Count value is incremented automatically.
- `Public Property Details() As String` [R/W] Sets or returns the details for the sales opportunity partner. Field name: Memo. Length: 50 characters.
- `Public Property Partners() As Long` [R/W] Sets or returns the partners table. Field name: ParterId. This is a foreign key to the Partners table (OPRT).
- `Public Property RelationshipCode() As Long` [R/W] Sets or returns the relationship ID number. Field name: OrlCode. This is a foreign key to the Relationships object.
- `Public Property RowNo() As Long` [R] Returns the current row number. Field name: Line.
- `Public Property SequenceNo() As Long` [R] Returns the sales opportunities partners, sequence no. Field name: OpportId. Returns the sales opportunity unique ID (primary key). Field name: OpportId.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oOrder As SAPbobsCOM.Documents ' Order object

            Dim lRetCode As Integer ' Return Code

            ' New Order

            oOrder = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oOrders)

            ' Fill Order details

            oOrder.CardCode = "C40000"

            oOrder.CardName = "Earthshaker Corporation"

            oOrder.HandWritten = SAPbobsCOM.BoYesNoEnum.tNO

            oOrder.DocDate = Today()

            oOrder.DocDueDate = Today()

            oOrder.DocCurrency = "USD"

            'Fill 2 lines in the order

            oOrder.Lines.ItemCode = "A00001"

            oOrder.Lines.ItemDescription = "IBM Inforprint 1312"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            oOrder.Lines.Add()

            oOrder.Lines.ItemCode = "A00002"

            oOrder.Lines.ItemDescription = "IBM Infoprint 1222"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            ' Now we want to delete the second line in the Order

            oOrder.Lines.Delete()

            ' The Order will be added without the second line

            lRetCode = oOrder.Add
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# SalesOpportunitiesReasons (Object)

SalesOpportunitiesReasons is a child object of the SalesOpportunities object and represents the reasons for failures of sales opportunity. Source table: OPR5.

**Remarks:** To display the form in the application: - Select Sales Opportunities --> Sales Opportunity. - Select the Summary tab. - Select the opportunity status Lost.

## Properties (5)
- `Public Property Count() As Long` [R] Returns the total rows in the SalesOpportunitiesReasons list.
- `Public Property Reason() As Long` [R/W] Sets or returns the reason ID for failure. This is a foreign key to the Defect Cause table (OOFR), which is exposed via the SalesOpportunityReasonsSetupService object. Field name: ReasondId.
- `Public Property RowNo() As Long` [R] Returns the current available row number (starts from 1). Field name: Line.
- `Public Property SequenceNo() As Long` [R] Returns the sales opportunity unique ID (primary key). Field name: OpportId.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oOrder As SAPbobsCOM.Documents ' Order object

            Dim lRetCode As Integer ' Return Code

            ' New Order

            oOrder = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oOrders)

            ' Fill Order details

            oOrder.CardCode = "C40000"

            oOrder.CardName = "Earthshaker Corporation"

            oOrder.HandWritten = SAPbobsCOM.BoYesNoEnum.tNO

            oOrder.DocDate = Today()

            oOrder.DocDueDate = Today()

            oOrder.DocCurrency = "USD"

            'Fill 2 lines in the order

            oOrder.Lines.ItemCode = "A00001"

            oOrder.Lines.ItemDescription = "IBM Inforprint 1312"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            oOrder.Lines.Add()

            oOrder.Lines.ItemCode = "A00002"

            oOrder.Lines.ItemDescription = "IBM Infoprint 1222"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            ' Now we want to delete the second line in the Order

            oOrder.Lines.Delete()

            ' The Order will be added without the second line

            lRetCode = oOrder.Add
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# SalesOpportunityCompetitorSetup (Object)

Represents a competitor. Source table: OCMT Mandatory properties: Name

**Remarks:** The SalesOpportunitiesCompetition object represents the competitor assigned to a specific sales opportunity.

## Properties (4)
- `Public Property Details() As String` [R/W] A comment about the competitor. Field name: Memo
- `Public Property Name() As String` [R/W] The name of the competitor. Field name: Name
  - remarks: Cannot be blank.
- `Public Property SequenceNo() As Long` [R] The key for a specific competitor. Field name: CompetId
- `Public Property ThreatLevel() As ThreatLevelEnum` [R/W] The threat level for the competitor, either low (1), medium (2), or high (3). The default is low. Field name: ThreatLevl

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# SalesOpportunityCompetitorSetupParams (Object)

Holds the key and name to an existing competitor. This object is used to pass keys to and retrieve keys from SalesOpportunityCompetitorsSetupService methods.

## Properties (3)
- `Public Property Name() As String` [R] The name of the competitor. Field name: Name
- `Public Property SequenceNo() As Long` [R/W] The key for a specific competitor. Field name: CompetId
- `Public Property ThreatLevel() As ThreatLevelEnum` [R] The threat level for the competitor, either low (1), medium (2), or high (3). The default is low. Field name: ThreatLevl

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# SalesOpportunityCompetitorSetupParamsCollection (Collection)

A collection of SalesOpportunityCompetitorSetup objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As SalesOpportunityCompetitorSetupParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As SalesOpportunityCompetitorSetupParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# SalesOpportunityCompetitorsSetupService (Object)

The SalesOpportunityCompetitorsSetupService service enables you to add, look up and remove competitors in the competitors master data table. Competitors can be assigned to sales opportunities. To see the list of competitors, select Sales Opportunities --> Sales Opportunity, select a sales opportunity and select the Competitors tab. In the Name column, select Define New. Source table: OCMT

## Methods (8)
- `Public Function AddSalesOpportunityCompetitorSetup(ByVal pISalesOpportunityCompetitorSetup As SalesOpportunityCompetitorSetup) As SalesOpportunityCompetitorSetupParams` Adds a competitor.
  - param `pISalesOpportunityCompetitorSetup`: The data for the new competitor.
  - returns: Contains the key (CompetId) of the new competitor.
  - C# example (from SAP's help):
    ```csharp
    try
    {
         SalesOpportunityCompetitorsSetupService oCompetSrv;
         oCompetSrv = (SalesOpportunityCompetitorsSetupService)
             (MainModule.oCmpSrv.GetBusinessService(ServiceTypes.SalesOpportunityCompetitorsSetupService));

         SalesOpportunityCompetitorSetup addLine;
         addLine = (SalesOpportunityCompetitorSetup)oCompetSrv.GetDataInterface(
              SalesOpportunityCompetitorsSetupServiceDataInterfaces.socssSalesOpportunityCompetitorSetup);

         addLine.Name = "competitor1";
         addLine.ThreatLevel = ThreatLevelEnum.Medium;
         addLine.Details = "Discount";
         oCompetSrv.AddSalesOpportunityCompetitorSetup(addLine);
    }
    catch (Exception ex)
    {
         Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Sub DeleteSalesOpportunityCompetitorSetup(ByVal pISalesOpportunityCompetitorSetupParams As SalesOpportunityCompetitorSetupParams)` Deletes an existing competitor. The competitor is specified by its key (CompetId), which is contained in the SalesOpportunityCompetitorSetupParams object passed to the method.
  - param `pISalesOpportunityCompetitorSetupParams`: The key of the competitor to be deleted.
  - remarks: You cannot delete a sales opportunity competitor that is associated with a sales opportunity.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SalesOpportunityCompetitorSetupParams delLine;
        delLine = (SalesOpportunityCompetitorSetupParams)oCompetSrv.GetDataInterface(SalesOpportunityCompetitorsSetupServiceDataInterfaces.socssSalesOpportunityCompetitorSetupParams);

        // Delete a record
        // The SequenceNo should be the competitor ID of a record in the DB
        delLine.SequenceNo = 31;
        oCompetSrv.DeleteSalesOpportunityCompetitorSetup(delLine);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As SalesOpportunityCompetitorsSetupServiceDataInterfaces) As Object` Creates an empty data structure for use with the SalesOpportunityCompetitorsSetupService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `SalesOpportunityCompetitorsSetupServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLFile(Hashtable Properties, String Path)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair In Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        oGeneralData.ToXMLFile(Path);

        //Retrieve XML and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLFile(Path);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLString(Hashtable Properties)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;
        string XMLString;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair in Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        XMLString = oGeneralData.ToXMLString();

        //Retrieve XML string and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLString(XMLString);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetSalesOpportunityCompetitorSetup(ByVal pISalesOpportunityCompetitorSetupParams As SalesOpportunityCompetitorSetupParams) As SalesOpportunityCompetitorSetup` Retrieves a competitor. The competitor is specified by its key (CompetId), which is contained in the SalesOpportunityCompetitorSetupParams object passed to the method.
  - param `pISalesOpportunityCompetitorSetupParams`: The key of the competitor to retrieve.
  - returns: The competitor with the specified key.
- `Public Function GetSalesOpportunityCompetitorSetupList() As SalesOpportunityCompetitorSetupParamsCollection` Retrieves the keys and names of all the competitors.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SalesOpportunityCompetitorSetupParamsCollection getlistParams;
        getlistParams = oCompetSrv.GetSalesOpportunityCompetitorSetupList();

        String resultSet = "";

        foreach(SalesOpportunityCompetitorSetupParams record in getlistParams)
        {
            resultSet = resultSet + record.SequenceNo + "\t" + record.Name + "\t" + record.ThreatLevel + "\n";
            Interaction.MsgBox(resultSet, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
        }
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Sub UpdateSalesOpportunityCompetitorSetup(ByVal pISalesOpportunityCompetitorSetup As SalesOpportunityCompetitorSetup)` Updates an existing competitor. The data for the competitor, including the key of the competitor to be updated, is contained in the SalesOpportunityCompetitorSetup object passed to the method. To update a competitor, you must first retrieve it using the GetSalesOpportunityCompetitorSetup method.
  - param `pISalesOpportunityCompetitorSetup`: The data for the competitor to be updated. The SalesOpportunityCompetitorSetup object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SalesOpportunityCompetitorSetupParams getLine;
        SalesOpportunityCompetitorSetup updateLine;
        getLine = (SalesOpportunityCompetitorSetupParams)oCompetSrv.GetDataInterface(SalesOpportunityCompetitorsSetupServiceDataInterfaces.socssSalesOpportunityCompetitorSetupParams);

        //update a record
        //please note that the SequenceNo should be the Competitor ID of a record in DB
        getLine.SequenceNo = 30;

        updateLine = oCompetSrv.GetSalesOpportunityCompetitorSetup(getLine);
        updateLine.Details = "updated memo";
        updateLine.Name = "updated name";
        updateLine.ThreatLevel = ThreatLevelEnum.High;
        oCompetSrv.UpdateSalesOpportunityCompetitorSetup(updateLine);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```

# SalesOpportunityInterestSetup (Object)

Represents an area of interest for the sales opportunity. Source table: OOIN Mandatory properties: Description

**Remarks:** The SalesOpportunitiesInterests object represents the interests of a specific sales opportunity.

## Properties (3)
- `Public Property Description() As String` [R/W] The description of the interest. Field name: Descript
  - remarks: Cannot be blank.
- `Public Property SequenceNo() As Long` [R] The key for a specific interest. Field name: Num
- `Public Property Sort() As Long` [R/W] A value for determining in what order to display the items in the user interface. Default is 100. Field name: SortOrder
  - remarks: Cannot be negative. If two or more items have the same sort value, these items are sorted in alphabetical order. When a user starts to add a new item, the application automatically sets the sort value to one more than the current highest sort value. If the user clears this suggested value and adds the record with no sort value, the application automatically sets the sort value to 100.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# SalesOpportunityInterestSetupParams (Object)

Holds the key and name to an interest. This object is used to pass keys to and retrieve keys from SalesOpportunityInterestsSetupService methods.

## Properties (2)
- `Public Property Description() As String` [R] The description of the interest. Field name: Descript
- `Public Property SequenceNo() As Long` [R/W] The key for a specific interest. Field name: Num

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# SalesOpportunityInterestSetupParamsCollection (Collection)

A collection of SalesOpportunityInterestSetupParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As SalesOpportunityInterestSetupParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As SalesOpportunityInterestSetupParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

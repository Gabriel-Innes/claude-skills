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

<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TargetGroupsService (Object)

The TargetGroupsService service enables you to add, look up, update, and remove target groups. Source table: OTTG.

**Remarks:** To create a target group, proceed as follows: From the SAP Business One Main Menu, choose Administration --> Set Up --> Business Partners --> Target Group. In the Target Group – Set Up window, specify the Target Group Code and the Target Group Name for the new group and choose Update. In the # column, double-click the gray sequence number area corresponding to the target group you created in step 2. The Target Group Details window appears.

## Methods (8)
- `Public Function Add(ByVal pITargetGroup As TargetGroup) As TargetGroupParams` Adds a target group.
  - param `pITargetGroup`: The data for the new target group.
- `Public Sub Delete(ByVal pITargetGroupParams As TargetGroupParams)` Deletes an existing target group.
  - param `pITargetGroupParams`: The key of the target group to be deleted.
- `Public Function Get(ByVal pITargetGroupParams As TargetGroupParams) As TargetGroup` Retrieves a target group. The target group is specified by its key, which is contained in the TargetGroupParams object passed to the method.
  - param `pITargetGroupParams`: The key of the target group to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As TargetGroupsServiceDataInterfaces) As Object` Creates an empty data structure for use with the TargetGroupsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/TargetGroupsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As TargetGroupsParams` Returns the TargetGroupsParams data collection that identifies all target groups.
- `Public Sub Update(ByVal pITargetGroup As TargetGroup)` Updates an existing target group.
  - param `pITargetGroup`: The data for the target group to be updated. The TargetGroup object must contain the key of the object to be updated.

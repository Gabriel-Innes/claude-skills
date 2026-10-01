<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CashFlowLineItemsService (Object)

CashFlowLineItemsService Class

## Methods (5)
- `Public Function GetCashFlowLineItem(ByVal pICashFlowLineItemParams As CashFlowLineItemParams) As CashFlowLineItem` GetCashFlowLineItem
  - param `pICashFlowLineItemParams`: 
- `Public Function GetCashFlowLineItemList() As CashFlowLineItemsParams` GetCashFlowLineItemList
- `Public Function GetDataInterface(ByVal enumMSDI As CashFlowLineItemsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/CashFlowLineItemsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`:

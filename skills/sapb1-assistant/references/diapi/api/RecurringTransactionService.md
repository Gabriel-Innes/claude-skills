<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# RecurringTransactionService (Object)

RecurringTransactionService Class

## Methods (7)
- `Public Sub DeleteRecurringTransactions(ByVal pIRclRecurringTransactionParamsCollection As RclRecurringTransactionParamsCollection)` DeleteRecurringTransactions
  - param `pIRclRecurringTransactionParamsCollection`: 
- `Public Function ExecuteRecurringTransactions(ByVal pIRclRecurringTransactionParamsCollection As RclRecurringTransactionParamsCollection, ByVal pIRclRecurringExecutionParams As RclRecurringExecutionParams) As RclRecurringTransactionCollection` ExecuteRecurringTransactions
  - param `pIRclRecurringTransactionParamsCollection`: 
  - param `pIRclRecurringExecutionParams`: 
- `Public Function GetAvailableRecurringTransactions() As RclRecurringTransactionCollection` GetAvailableRecurringTransactions
- `Public Function GetDataInterface(ByVal enumMSDI As RecurringTransactionServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/RecurringTransactionServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetRecurringTransaction(ByVal pIRclRecurringTransactionParams As RclRecurringTransactionParams) As RclRecurringTransaction` GetRecurringTransaction
  - param `pIRclRecurringTransactionParams`:

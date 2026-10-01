<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EmployeeTransfersService (Object)

EmployeeTransfersService is a business object that manages employee master data transfers from SAP Business One to the DATEV HR client application. Source table: OHET.

**Remarks:** To transfer employee information from SAP Business One: - Choose Human Resources --> Human Resources Reports --> Employee List. - Select the desired employee from the list. - Choose the Transfer button.

## Methods (8)
- `Public Function AddEmployeeTransfer(ByVal pIEmployeeTransfer As EmployeeTransfer) As EmployeeTransferParams` Adds an employee transfer.
  - param `pIEmployeeTransfer`: The data for the new employee transfer.
  - returns: Contains the key of the new employee transfer.
  - C# example (from SAP's help):
    ```csharp
    EmployeeTransfersService oTrans = (EmployeeTransfersService)oCompany.GetCompanyService().GetBusinessService(ServiceTypes.EmployeeTransfersService);
    EmployeeTransfer oTransfer = (EmployeeTransfer) oTrans.GetDataInterface(EmployeeTransfersServiceDataInterfaces.etsEmployeeTransfer);

    oTransfer.TransStartDate = DateTime.Today;
    oTransfer.TransStartTime = DateTime.Now;
    oTransfer.TransEndDate = DateTime.Today;
    oTransfer.TransEndTime = DateTime.Now;

    oTransfer.Status = EmployeeTransferStatusEnum.ets_New;

    oTransfer.EmployeeTransferDetails.Add();
    oTransfer.EmployeeTransferDetails.Item(0).EmployeeID = 1;
    oTransfer.EmployeeTransferDetails.Item(0).TransferedDate = DateTime.Today;
    oTransfer.EmployeeTransferDetails.Item(0).TransferedTime = DateTime.Now;
    oTransfer.EmployeeTransferDetails.Item(0).Status = EmployeeTransferProcessingStatusEnum.etps_New;

    oTransfer.EmployeeTransferDetails.Add();
    oTransfer.EmployeeTransferDetails.Item(1).EmployeeID = 2;
    oTransfer.EmployeeTransferDetails.Item(1).TransferedDate = DateTime.Today;
    oTransfer.EmployeeTransferDetails.Item(1).TransferedTime = DateTime.Now;
    oTransfer.EmployeeTransferDetails.Item(1).Status = EmployeeTransferProcessingStatusEnum.etps_New;

    oTrans.AddEmployeeTransfer(oTransfer);
    ```
- `Public Sub DeleteEmployeeTransfer(ByVal pIEmployeeTransferParams As EmployeeTransferParams)` Deletes an existing employee transfer.
  - param `pIEmployeeTransferParams`: The key of the employee transfer to be deleted.
- `Public Function GetDataInterface(ByVal enumMSDI As EmployeeTransfersServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default settings/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/EmployeeTransfersServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates a data structure from a specified XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates a data structure from a specified XML string.
  - param `bstrXMLString`: Specifies the XML String.
- `Public Function GetEmployeeTransfer(ByVal pIEmployeeTransferParams As EmployeeTransferParams) As EmployeeTransfer` Retrieves an employee transfer.
  - param `pIEmployeeTransferParams`: The key of the employee transfer to retrieve.
  - returns: The employee transfer with the specified key.
- `Public Function GetEmployeeTransferList() As EmployeeTransfersParams` Retrieves the list of employee transfers.
- `Public Sub UpdateEmployeeTransfer(ByVal pIEmployeeTransfer As EmployeeTransfer)` Updates an existing employee transfer.
  - param `pIEmployeeTransfer`: The data for the employee transfer to be updated.
  - C# example (from SAP's help):
    ```csharp
    EmployeeTransfersService oTrans = (EmployeeTransfersService)oCompany.GetCompanyService().GetBusinessService(ServiceTypes.EmployeeTransfersService);
    EmployeeTransferParams oTransParams = (EmployeeTransferParams)oTrans.GetDataInterface(EmployeeTransfersServiceDataInterfaces.etsEmployeeTransferParams);

    oTransParams.TransferID = 1;

    EmployeeTransfer oTransfer = oTrans.GetEmployeeTransfer(oTransParams);

    oTransfer.TransEndDate = DateTime.Today;
    oTransfer.TransEndTime = DateTime.Now;
    oTransfer.Status = EmployeeTransferStatusEnum.ets_Sent;

    oTransfer.EmployeeTransferDetails.Item(0).TransferedDate = DateTime.Today;
    oTransfer.EmployeeTransferDetails.Item(0).TransferedTime = DateTime.Now;
    oTransfer.EmployeeTransferDetails.Item(0).Status = EmployeeTransferProcessingStatusEnum.etps_Sent;

    oTransfer.EmployeeTransferDetails.Item(1).TransferedDate = DateTime.Today;
    oTransfer.EmployeeTransferDetails.Item(1).TransferedTime = DateTime.Now;
    oTransfer.EmployeeTransferDetails.Item(1).Status = EmployeeTransferProcessingStatusEnum.etps_Sent;

    oTrans.UpdateEmployeeTransfer(oTransfer);
    ```

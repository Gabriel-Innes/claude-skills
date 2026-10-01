<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AlertManagementService (Object)

AlertManagementService is a business object that manages alert system for SAP Business One application. This object enables you to: - Manage system and user alerts. - Manage alert's recipients. - Define event driven alerts and cyclic alerts. - Delivere alerts by the use of email, SMS or FAX. - Save the object in XML format. Source table: OALT.

**Remarks:** To use the service: - Connect to a valid company. - Call the CompanyService, which is the main DI service that you must call before using any other service. - Call the method GetBusinessService for the required service. - Create an empty data structure related to the required service. - or- You can create a data structure from an XML file or XML string. - Set the required properties of the specified data structure. - Call the required service method. To display the form in the application: Administration--Alert Management.

## Methods (7)
- `Public Function AddAlertManagement(ByVal pAlertManagement As AlertManagement) As AlertManagementParams` Creates new instance of AlertManagementParams (Code, Name and Type) Object that match the input parameter AlertManagement.
  - param `pAlertManagement`: Specifies the required AlertManagement.
  - example note: Add a user alert
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    'get alert

    Dim oAlertManagement As AlertManagement

    Dim oAlertManagementParams As AlertManagementParams

    Dim oAlertManagementRecipients As AlertManagementRecipients

    Dim oAlertRecipient As AlertManagementRecipient

    'Assuming that oAlertManagementService is already defined!

    'Get alert

    oAlertManagement  =

    oAlertManagementService.GetDataInterface(AlertManagementServiceDataInterfaces.atsdiAlertManagement)

    'set alert name

    oAlertManagement.Name = Alert1

    'set query

    oAlertManagement.QueryID = 34

    'activate the alert

    oAlertManagement.Active = BoYesNoEnum.tYES

    'set priority

    oAlertManagement .Priority = AlertManagementPriorityEnum.atp_High

    'Set the Frequency

    oAlertManagement .FrequencyInterval = 1

    ' set the Frequency type to hours

    oAlertManagement.FrequencyType = AlertManagementFrequencyType.atfi_Hours

    'get Recipients collection

    oAlertManagementRecipients = oAlertManagement.AlertManagementRecipients

    'add recipient

    oAlertRecipient = oAlertManagementRecipients.Add()

    'set recipient code(manager=1)

    oAlertRecipient.UserCode = 1

    'set internal message

    oAlertRecipient.SendInternal = BoYesNoEnum.tYES

    'add alert

    oAlertManagementParams=oAlertManagementService. AddAlertManagement (oAlertManagement )
    ```
- `Public Function GetAlertManagement(ByVal pAlertManagementParams As AlertManagementParams) As AlertManagement` Gets instance of AlertManagement Object according to AlertManagementParams (Code, Name and Type).
  - param `pAlertManagementParams`: Specifies the AlertManagementParams identification key combination (Code, Name and Type).
- `Public Function GetAlertManagementList(ByVal pAlertManagementParams As AlertManagementParams) As AlertManagementParamsCollection` Returns a AlertManagementParamsCollection object, a data collection of all the instances of AlertManagementParams Identification keys that match a given AlertManagementParams identification key (Code, Name and Type).
  - param `pAlertManagementParams`: The AlertManagementParams Identification key that function as a filter.
  - example note: Get a list of System alerts
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oAlertManagementParamsCollection As AlertManagementParamsCollection

    Dim oAlertManagementParams As AlertManagementParams

    'Assuming that oAlertManagementService is already defined!

    'get Alert Params

    oAlertManagementParams = oAlertManagementService.GetDataInterface(AlertManagementServiceDataInterfaces.atsdiAlertManagementParams)

    'set the type of the alarm to system

    oAlertManagementParams.Type = AlertManagementTypeEnum.att_System

    'get collection of system alerts

    oAlertManagementParamsCollection = oAlertManagementService.GetAlertManagementList(oAlertManagementParams)
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As AlertManagementServiceDataInterfaces) As Object` Creates empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/AlertManagementServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates data structure from specified XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates data structure from specified XML string.
  - param `bstrXMLString`: Specifies the XML string.
- `Public Sub UpdateAlertManagement(ByVal pIAlertManagement As AlertManagement)` Update this ApprovalTemplate by another ApprovalTemplate.
  - param `pIAlertManagement`: Specifies the target ApprovalTemplate.
  - example note: Update a system alert
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oAlertManagement As AlertManagement

    Dim AlertManagementParams As AlertManagementParams

    Dim OAlertManagementRecipients As AlertManagementRecipients

    Dim oAlertRecipient As AlertManagementRecipient

    Dim j As Integer

    'Assuming that oAlertManagementService is already defined!

    'get alert params

    AlertManagementParams = oAlertManagementService.GetDataInterface(AlertManagementServiceDataInterfaces.atsdiAlertManagementParams)

    'set system alert code

    AlertManagementParams.Code = -5

    'get alert

    oAlertManagement = oAlertManagementService.GetAlertManagement(AlertManagementParams)

    oAlertManagement.Active = BoYesNoEnum.tYES

    'set % Discount

    oAlertManagement.Param = 15

    'set priority

    oAlertManagement.Priority = AlertManagementPriorityEnum.atp_High

    'choose Quotation document

    For j = 0 To oAlertManagement.AlertManagementDocuments.Count - 1

        If oAlertManagement.AlertManagementDocuments.Item(j).Document =                                   AlertManagementDocumentEnum.atd_Quotations Then

            oAlertManagement.AlertManagementDocuments.Item(j).Active =BoYesNoEnum.tYES

            Exit For

        End If

    Next j

    'get recipient collection

    OAlertManagementRecipients = oAlertManagement.AlertManagementRecipients

    'add recipient

    oAlertRecipient = oAlertManagementRecipients.Add()

    'set recipient code(manager=1)

    oAlertRecipient.UserCode = 1

    'set internal message

    oAlertRecipient.SendInternal = BoYesNoEnum.tYES

    'update system alert

    Call oAlertManagementService.UpdateAlertManagement(oAlertManagement)
    ```

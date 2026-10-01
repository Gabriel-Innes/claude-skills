<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# MessagesService (Object)

This service enables to manage the Inbox and Outbox messages, and to send messages.

**Remarks:** To use the service: - Connect to a valid company. - Call the CompanyService, which is the main DI service that you must call before using any other service. - Call the method GetBusinessService for the required service. - Create an empty data structure related to the required service. - or- You can create a data structure from an XML file or XML string. - Set the required properties of the specified data structure. - Call the required service method.

## Methods (8)
- `Public Function GetDataInterface(ByVal enumMSDI As MessagesServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/MessagesServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - example note: This is a VB.NET sample that shows how to get a Message Inbox from an existing XML file.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oMessageService As MessagesService

    Dim oMessageInbox As MessageHeaders

    Dim oInboxFromFile As MessageHeaders

    Dim oInboxFromString As MessageHeaders

    Dim oMessageHeader As MessageHeader

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get msg service

    oMessageService = oCmpSrv.GetBusinessService(ServiceTypes.MessagesService)

    'get message inbox

    oMessageInbox = oMessageService.GetInbox

    'save inbox to file

    oMessageInbox.ToXMLFile("c:\MyInbox.xml")

    'create a new inbox data structure and fill it with the data from

    'the xml file

    oInboxFromFile = oMessageService.GetDataInterfaceFromXMLFile("c:\MyInbox.xml")

    'get first message header

    oMessageHeader = oInboxFromFile.Item(0)
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates a data structure from a specified XML string.
  - param `bstrXMLString`: XML string.
  - example note: This is a VB.NET sample that shows how to get a Message Inbox from an existing XMLstring.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oMessageService As MessagesService

    Dim oMessageInbox As MessageHeaders

    Dim sInboxXmlString As String

    Dim oInboxFromString As MessageHeaders

    Dim oMessageHeader As MessageHeader

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get msg service

    oMessageService = oCmpSrv.GetBusinessService(ServiceTypes.MessagesService)

    'get inbox

    oMessageInbox = oMessageService.GetInbox

    'retrieve the inbox as xml string

    sInboxXmlString = oMessageInbox.ToXMLString

    'create a new inbox data structure and fill it with the data from

    'the xml string

    oInboxFromString = oMessageService.GetDataInterfaceFromXMLString(sInboxXmlString)

    'get first message header

    oMessageHeader = oInboxFromString.Item(0)
    ```
- `Public Function GetInbox() As MessageHeaders` Retrieves the Inbox messages.
  - example note: The following is a VB.NET sample that retrieves the Inbox messages (similar to the Messages Overview in the application).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oMessageService As MessagesService

    Dim oUserInbox As MessageHeaders

    Dim oMessageHeader As MessageHeader

    Dim oMessage As Message

    Dim sUserCode As String

    Dim iAttachment As integer

    Dim sSubject As string

    Dim sReceivedDate As String

    Dim eReadMail As BoYesNoEnum

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get msg service

    oMessageService = oCmpSrv.GetBusinessService(ServiceTypes.MessagesService)

    'get inbox

    oUserInbox = oMessageService.GetInbox

    'get first message header

    oMessageHeader = oUserInbox.Item(0)

    'get the first message

    oMessage = oMessageService.GetMessage(oMessageHeader)

    'get subject

    sSubject=oMessage.Subject

    'get Date

    sReceivedDate=oMessageHeader.ReceivedDate

    'get the user's code

    sUserCode =oMessage.User

    'get read confirmation

    eReadMail=oMessageHeader.Read

    'get attachement code key

    iAttachment = oMessage.Attachment
    ```
- `Public Function GetMessage(ByVal pMessageHeader As MessageHeader) As Message` Retrieves a message by its header.
  - param `pMessageHeader`: Message Header input.
- `Public Function GetOutbox() As MessageHeaders` Retrieves the Outbox messages.
  - example note: The following is a VB.NET sample that retrievs the Outbox messages (similar to the Messages Overview in the application).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oMessageService As MessagesService

    Dim oUserOutbox As MessageHeaders

    Dim oMessageHeader As MessageHeader

    Dim oMessage As Message

    Dim iAttachment As Integer

    Dim sSubject As string

    Dim sDate As String

    Dim sTime As String

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get msg service

    oMessageService =         oCmpSrv.GetBusinessService(ServiceTypes.MessagesService)

    'get inbox

    oUserOutbox = oMessageService.GetOutbox

    'get first message header

    oMessageHeader = oUserOutbox.Item(0)

    'get the first message

    oMessage = oMessageService.GetMessage(oMessageHeader)

    'get subject

    sSubject=oMessage.Subject

    'get Date

    sDate= oMessageHeader.SentDate.ToShortDateString

    'get Time

    sTime= oMessageHeader.SentTime.ToShortTimeString

    'get attachement code key

    iAttachment = oMessage.Attachment
    ```
- `Public Function GetSentMessages() As MessageHeaders` Retrieves the Sent messages.
  - example note: The following is a VB.NET sample that retrievs the Sent messages (similar to the Message Overview in the application).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oMessageService As MessagesService

    Dim oUserSendMsgs As MessageHeaders

    Dim oMessageHeader As MessageHeader

    Dim oMessage As Message

    Dim iAttachment As Integer

    Dim sSubject As string

    Dim sDate As String

    Dim sTime As String

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get msg service

    oMessageService =         oCmpSrv.GetBusinessService(ServiceTypes.MessagesService)

    'get Sent Messages

    oUserSendMsgs = oMessageService.GetSentMessages

    'get first message header

    oMessageHeader = oUserSendMsgs.Item(0)

    'get the first message

    oMessage = oMessageService.GetMessage(oMessageHeader)

    'get subject

    sSubject=oMessage.Subject

    'get Date

    sDate= oMessageHeader.SentDate.ToShortDateString

    'get Time

    sTime= oMessageHeader.SentTime.ToShortTimeString

    'get attachement code key

    iAttachment = oMessage.Attachment
    ```
- `Public Function SendMessage(ByVal pMessage As Message) As MessageHeader` Sends a specified message and returns its header.
  - param `pMessage`: Message input.
  - example note: The following is a VB.NET sample that enables to send an internal message with a single line.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oMessageService As MessagesService

    Dim oMessage As Message

    Dim pMessageDataColumns As MessageDataColumns

    Dim pMessageDataColumn As MessageDataColumn

    Dim oLines As MessageDataLines

    Dim oLine As MessageDataLine

    Dim oRecipientCollection As RecipientCollection

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get msg service

    oMessageService = oCmpSrv.GetBusinessService(ServiceTypes.MessagesService)

    'get the data interface for the new message

    oMessage=oMessageService.GetDataInterface(MessagesServiceDataInterface.msdiMessage)

    'fill subject

    oMessage.Subject = "My Subject"

    'fill text

    oMessage.Text = "My Text"

    'Add Recipient

    oRecipientCollection = oMessage.RecipientCollection

    'Add new a recipient

    oRecipientCollection.Add()

    'send internal message

    oRecipientCollection.Item(0).SendInternal = BoYesNoEnum.tYES

    'add existing user code

    oRecipientCollection.Item(0).UserCode = "manager"

    'get columns data

    pMessageDataColumns = oMessage.MessageDataColumns

    'get column

    pMessageDataColumn = pMessageDataColumns.Add()

    'set column name

    pMessageDataColumn.ColumnName = "My Column Name"

    'get lines

    oLines = pMessageDataColumn.MessageDataLines()

    'add new line

    oLine = oLines.Add()

    'set the line value

    oLine.Value = "My Value"

    'send the message

    oMessageService.SendMessage(oMessage)
    ```

<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# FiscalPrinterService (Object)

FiscalPrinterService Class

## Methods (8)
- `Public Function AddFiscalPrinter(ByVal pIFiscalPrinter As FiscalPrinter) As FiscalPrinterParams` AddFiscalPrinter
  - param `pIFiscalPrinter`: 
- `Public Sub DeleteFiscalPrinter(ByVal pIFiscalPrinterParams As FiscalPrinterParams)` DeleteFiscalPrinter
  - param `pIFiscalPrinterParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As FiscalPrinterServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/FiscalPrinterServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetFiscalPrinter(ByVal pIFiscalPrinterParams As FiscalPrinterParams) As FiscalPrinter` GetFiscalPrinter
  - param `pIFiscalPrinterParams`: 
- `Public Function GetFiscalPrinterList() As FiscalPrintersParams` GetFiscalPrinterList
- `Public Sub UpdateFiscalPrinter(ByVal pIFiscalPrinter As FiscalPrinter)` UpdateFiscalPrinter
  - param `pIFiscalPrinter`:

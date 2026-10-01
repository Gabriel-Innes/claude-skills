<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxInvoiceReportService (Object)

TaxInvoiceReportService Class

## Methods (6)
- `Public Sub CancelTaxInvoiceReport(ByVal pITaxInvoiceReportParams As TaxInvoiceReportParams)` CancelTaxInvoiceReport
  - param `pITaxInvoiceReportParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As TaxInvoiceReportServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/TaxInvoiceReportServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetTaxInvoiceReport(ByVal pITaxInvoiceReportParams As TaxInvoiceReportParams) As TaxInvoiceReport` GetTaxInvoiceReport
  - param `pITaxInvoiceReportParams`: 
- `Public Sub UpdateTaxInvoiceReport(ByVal pITaxInvoiceReport As TaxInvoiceReport)` UpdateTaxInvoiceReport
  - param `pITaxInvoiceReport`:

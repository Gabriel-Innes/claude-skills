<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BoAlertTypeforWHStockEnum (Enumeration)

Specifies the system's response when the inventory level falls below this minimum as the result of a sales document, such as a delivery note or an invoice.

| Member | Value | Description |
|---|---|---|
| atfwhs_WarningOnly | 0 | A warning message appears when the sales document is entered. |
| atfwhs_Block | 1 | The sales document is blocked (default). |
| atfwhs_NoMessage | 2 | No system response is triggered. |

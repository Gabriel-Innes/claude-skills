<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BoProductionOrderStatusEnum (Enumeration)

Specifies the status options of a production order.

| Member | Value | Description |
|---|---|---|
| boposPlanned | 0 | Indicates the initial stage of the production. |
| boposReleased | 1 | Indicates the release state of the product. That is, the order to the production floor for work. This is the status at which receipts and issues are transacted. |
| boposClosed | 2 | Closed: you close the production order when all transactions have been completed. |
| boposCancelled | 3 | Cancelled: the production order is removed from the list before the production process starts |

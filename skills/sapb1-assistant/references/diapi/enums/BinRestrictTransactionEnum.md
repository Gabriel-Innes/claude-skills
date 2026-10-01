<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BinRestrictTransactionEnum (Enumeration)

The transaction restriction status of the bin location.

| Member | Value | Description |
|---|---|---|
| brtNoRestrictions | 0 | No restriction - the bin location can be used in any relevant transactions. |
| brtAllTrans | 1 | All transactions - the bin location is restricted from all transactions, that is, the bin location cannot be used in any transactions. |
| brtInboundTrans | 2 | Inbound transactions - the bin location is restricted from inbound transactions, that is, the bin location cannot be used to store any incoming flow of goods. |
| brtOutboundTrans | 3 | Outbound transactions - the bin location is restricted from outbound transactions, that is, the bin location cannot be used during the issuing of goods. |
| brtAllExceptInventoryTrans | 4 | All except inventory transfer and counting - the bin location is restricted to inventory transfer, counting and posting only. That is, the bin location can only be used during inventory transfer, counting and posting. |

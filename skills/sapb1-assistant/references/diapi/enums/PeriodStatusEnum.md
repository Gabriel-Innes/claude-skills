<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PeriodStatusEnum (Enumeration)

Statuses for finance periods.

| Member | Value | Description |
|---|---|---|
| ltUnlocked | 0 | All types of transactions and documents. |
| ltUnlockedExceptSales | 1 | All types of transactions and documents, except for the documents under the Sales (A/R) module. |
| ltPeriodClosing | 2 | Users who have period closing authorization can post all types of transactions and documents. |
| ltLocked | 3 | Neither transactions nor documents can be posted. |

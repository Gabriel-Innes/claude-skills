<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BoBlockBudget (Enumeration)

Specifies the options for managing deviations from budget in documents.

| Member | Value | Description |
|---|---|---|
| bb_OnlyAnnualAlert | 0 | Without Warning - Enables to add transactions that have exceeded the budget. The system does not issue any alert for these transactions. |
| bb_MonthlyAlertOnly | 1 | Warning - the system issues a warning message for any transaction that exceeds the budget. Authorized users can ignore the message. Unauthorized users have to confirm the transaction by an authorized user. |
| bb_Block | 2 | Blocks the option to add transactions to accounts for which the budget was exceeded. |

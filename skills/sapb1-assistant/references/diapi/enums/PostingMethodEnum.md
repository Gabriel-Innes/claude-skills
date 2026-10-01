<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PostingMethodEnum (Enumeration)

Posting methods for bank statements.

| Member | Value | Description |
|---|---|---|
| pmGLAccountBankAccount | 0 | G/L Account from/to Bank Account. Indicates: - An incoming or outgoing payment from or to the G/L account is created. - External reconciliation takes place between the bank statement row and the G/L account. |
| pmBussinessPartnerBankAccount | 1 | Business Partner from/to Bank Account. Indicates: - An incoming or outgoing payment from or to the business partner is created. - Internal reconciliation takes place on the business partner side (if possible). - External reconciliation takes place between the bank statement row and the G/L account. |
| pmInterimAccountBankAccount | 2 | Bank Interim Account from/to Bank Account. Creates a journal entry that is internally reconciled on the interim bank account side, and externally reconciled on the bank account side. |
| pmExternalReconciliation | 3 | External Reconciliation. Indicates that only external reconciliation is performed on the bank account side, but that no transaction is posted. |
| pmIgnore | 4 | Ignore. Prevents any of the automatic actions described above. |

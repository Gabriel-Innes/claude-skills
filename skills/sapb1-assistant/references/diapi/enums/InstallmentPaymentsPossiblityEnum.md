<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# InstallmentPaymentsPossiblityEnum (Enumeration)

Installment options for payments.

| Member | Value | Description |
|---|---|---|
| ippYes | 0 | The system allows installments. |
| ippNo | 1 | The system does not allow installments. |
| ippCr | 2 | Credit - The system allows equal installments related to the payment by the customer. However, the system writes a single row in the accounting document for this transaction, because the credit card company pays the entire amount with a single payment. |
| ippRd | 3 | Reduction - The system allows installments but also enables to change the first installment of the related payment by the customer. However, the system writes a single row in the accounting document for this transaction, because the credit card company pays the entire amount with a single payment. |

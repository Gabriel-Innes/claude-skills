<!-- source: Pastel.Evolution.chm, Pastel.Evolution SDK 11.0.0.10 | verified: 2026-10-02 -->

# AccountAgeingMethod (Enumeration)

Describes an account's ageing method.

| Member | Value | Description |
|---|---|---|
| `OpenItem` | 0 | Each transaction on the account is allocated and aged individually. |
| `BalanceForward` | 1 | Transaction balances on the account are automatically offset by other transactions in the same or previous periods. |

# AgeingDate (Enumeration)

Specifies the date to use when ageing transactions on an ageing reports.

| Member | Value | Description |
|---|---|---|
| `InvoiceDate` | 0 | The actual transaction date is used during age calculation. |
| `StatementDate` | 1 | The statement date (typically the last day of the month in which the transaction was processed) is used to determine transaction ages. |

# AgingIntervalOption (Enumeration)

| Member | Value | Description |
|---|---|---|

# AgingModule (Enumeration)

| Member | Value | Description |
|---|---|---|

# AgingTypeOption (Enumeration)

| Member | Value | Description |
|---|---|---|

# AutoPaymentMethod (Enumeration)

Describes the automatic payment method available to supplier accounts.

| Member | Value | Description |
|---|---|---|

# Bank.AccountType (Enumeration)

Describes a bank account type.

| Member | Value | Description |
|---|---|---|

# CashbookBatchDetail.Module (Enumeration)

| Member | Value | Description |
|---|---|---|

# CashbookBatchDetail.SplitLineType (Enumeration)

| Member | Value | Description |
|---|---|---|

# CashbookBatchDetailCollection.CashbookBatchDetailChangeAction (Enumeration)

| Member | Value | Description |
|---|---|---|

# CashbookBatchSplitCollection.CashbookBatchDetailChangeAction (Enumeration)

| Member | Value | Description |
|---|---|---|

# Contract.ContractBillingType (Enumeration)

| Member | Value | Description |
|---|---|---|

# DocumentState (Enumeration)

Describes an inventory document's state.

| Member | Value | Description |
|---|---|---|

# DocumentTotalRoundingStrategy (Enumeration)

| Member | Value | Description |
|---|---|---|

# DocumentType (Enumeration)

Describes an inventory document's type.

| Member | Value | Description |
|---|---|---|

# DrCrTransaction.FcCalcElement (Enumeration)

| Member | Value | Description |
|---|---|---|

# EvolutionVersion.SpecialBuilds (Enumeration)

| Member | Value | Description |
|---|---|---|

# FieldCollectionManager.FieldType (Enumeration)

| Member | Value | Description |
|---|---|---|
| `Default` | 0 | All fields; flagged dirty when modifying. |
| `Modified` | 1 | All dirty fields. |
| `ReadOnly` | 2 | Read-only (key) fields. |
| `Writable` | 3 | All fields except those marked as read-only. Default - read-only = writable |
| `User` | 4 | All fields not defined by the template. They are all considered writable! |
| `Raw` | 5 | Exactly the same as Default, but not flagged dirty when setting. Used for internal loading |

# GLAccount.AccountType (Enumeration)

Defines general ledger account types.

| Member | Value | Description |
|---|---|---|

# GLBatch.BatchChangeAction (Enumeration)

| Member | Value | Description |
|---|---|---|

# Incident.IncidentStatus (Enumeration)

Describes the status of the incident.

| Member | Value | Description |
|---|---|---|
| `NotStarted` | 1 | The incident has been logged but not yet actioned. |
| `InProgress` | 2 | The indicent has been actioned by not yet closed. |
| `Complete` | 3 | The incident has been closed. |

# IncidentLogAction (Enumeration)

| Member | Value | Description |
|---|---|---|

# InventoryCostingMethod (Enumeration)

Inventory costing method.

| Member | Value | Description |
|---|---|---|

# InventoryIntegrationMethod (Enumeration)

Inventory costing method.

| Member | Value | Description |
|---|---|---|

# InventoryOperation (Enumeration)

| Member | Value | Description |
|---|---|---|

# JobCard.JobStatus (Enumeration)

| Member | Value | Description |
|---|---|---|

# JobDetail.TransactionKind (Enumeration)

| Member | Value | Description |
|---|---|---|

# JobDetail.TransactionSource (Enumeration)

| Member | Value | Description |
|---|---|---|

# JobDetailCollection.JobDetailChangeAction (Enumeration)

| Member | Value | Description |
|---|---|---|

# JobPostingMethod (Enumeration)

| Member | Value | Description |
|---|---|---|

# JobStatus (Enumeration)

| Member | Value | Description |
|---|---|---|

# JournalBatchDetailCollection.JournalBatchDetailChangeAction (Enumeration)

| Member | Value | Description |
|---|---|---|

# Module (Enumeration)

| Member | Value | Description |
|---|---|---|

# ModuleID (Enumeration)

Evolution module ID as it appears in the posting tables. Mainly used internally.

| Member | Value | Description |
|---|---|---|

# OrderDetailCollection.OrderDetailChangeAction (Enumeration)

| Member | Value | Description |
|---|---|---|

# PropertyDirection (Enumeration)

Describes whether a Property's Direction is a Value or Percentage.

| Member | Value | Description |
|---|---|---|

# PurchaseOrder.GrvPhase (Enumeration)

| Member | Value | Description |
|---|---|---|

# SerialNumberLocation (Enumeration)

Describes an inventory number's location.

| Member | Value | Description |
|---|---|---|
| `OutOfStock` | 3 | Lost (Adjusted out) |

# SerialNumberTransaction.SerialNumberMovement (Enumeration)

| Member | Value | Description |
|---|---|---|
| `Purchased` | 8 | Takes place during a supplier invoice. |
| `Returned` | 3 | Takes place during a return to supplier |
| `Sold` | 7 | Takes place during a customer invoice |
| `Credited` | 1 | Takes place during a customer credit note. |

# SplitAllocationCollection.OrderDetailChangeAction (Enumeration)

| Member | Value | Description |
|---|---|---|

# TaxMode (Enumeration)

| Member | Value | Description |
|---|---|---|

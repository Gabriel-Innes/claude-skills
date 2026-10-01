<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PrintOnEnum (Enumeration)

Paper types for printing checks.

| Member | Value | Description |
|---|---|---|
| poBlankPaper | 0 | Prints checks on a blank paper. For example, can be used for printing draft checks. |
| poOverflowCheckStock | 1 | Prints checks on a check stock paper and in case of overflow (that is, the number of lines in the stub exceeds the value of MaximumLines) then the system prints VOID on the next check and cancels its number (the number of the voided check cannot be used). |
| poOverflowBlankPaper | 2 | Prints checks on a check paper and in case of overflow (that is, the number of lines in the appendix exceedes the value of MaximumLines) the system displays a message to change to plain paper, then prints the remaining lines on the plain paper. This enables to keep consecutive check numbers without voiding checks. |
| poDefault | 3 | Prints checks on a check paper, which includes an appendix for each check. |

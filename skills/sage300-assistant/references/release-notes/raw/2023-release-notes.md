<!-- source: https://help.sage300.com/en-us/2023/classic/Content/ReleaseDocs/ReleaseNotes.htm | version: Sage 300 2023 | page published: December 29, 2025 | extracted: 2026-09-23 by scripts/extract_release_notes.py -->

# Sage 300 2023 Release Notes

Thank you for choosing a Sage business management solution.

These release notes contain important information about Sage 300, including information about product changes that are not in the documentation.

Product updates contain modified versions of one or more Sage 300 program components. A product update is not a full upgrade or a product replacement. Each product update is valid only until we release the next product update or the next version of Sage 300.

Depending on your purchase agreement, some features described here may not be available in your product.

For more information about feature availability, see Sage Knowledgebase article 220924460105946 .

## What's new in Product Update 10

### Program fixes

This product update includes program fixes. See the list of fixed issues in Technical Information for more information.

## What's new in Product Update 9

This section contains a summary of new features and changes in Product Update 9.

### General improvements

This release includes the following new features and improvements in both Sage 300 web screens and Sage 300 classic screens:

#### Accounts Payable

We have updated the T5018 (CPRS) forms for Tax Year 2024.

### Program fixes

This product update also includes program fixes. See the list of fixed issues in Technical Information for more information.

## What's new in Product Update 8

This product update includes program fixes. See the list of fixed issues in Technical Information.

## What's new in Product Update 7

This product update includes program fixes. See the list of fixed issues in Technical Information.

### General Improvements

This release includes the following new features and improvements in both Sage 300 web screens and Sage 300 classic screens:

This product update supports HR Integration.

- In addition to installing and activating 2023.7 Product Update, you will need to install and activate Sage HR Integration v8.0.

- In a Workstation Setup environment, you will need to register each workstation by performing wssetup.cmd.

- Refer to Sage 300 Online Help for more information.

Tip: To avoid issues before you begin running Sage HR integration on the workstation, ensure Payroll 8.0 has at least tax update “C” installed on the server.

To begin:

- If applicable, uninstall the existing workstation setup.

- Install the workstation setup (wssetup.exe) that comes with the product update.

- Run the wssetup.cmd

## What's new in Product Update 6

This product update includes program fixes. See the list of fixed issues in Technical Information.

## What's new in Product Update 5

### General improvements

This release includes the following new features and improvements in both Sage 300 web screens and Sage 300 classic screens:

#### Accounts Payable

- Five new fields have been added for 1099 purposes: First Name, Last Name, FATCA, Second TIN Notice, and Tax Withholding State. These fields also appear in Inquiry Reporting.

- Sage 300 now supports Form 1099-Div in the AP 1099 Filing screen.

## What's new in Product Update 4

This section contains a summary of new features and changes in Product Update 4.

### General improvements

This release includes the following new features and improvements in both Sage 300cloud web screens and Sage 300 classic screens:

#### System Manager

There have been improvements made in the Lanpak user handling, especially when using the Current Users screen.

#### Bank Services

The Singapore Tax Report module now has efile capability.

## What's new in Product Update 3

This section contains a summary of new features and changes in Product Update 3.

### General improvements

This release includes the following new features and improvements in both Sage 300cloud web screens and Sage 300 classic screens:

#### Sage 300 is more secure

Continuing from Product Update 2, this update includes additional improvements to application security and requires a multi-step installation process and changes to the system setup. Please review all instructions before beginning any update. Additionally, some third-party applications may be impacted by these changes. Please check with your third-party add-on providers for compatibility.

## What's new in Product Update 2

This section contains a summary of new features and changes in Product Update 2.

### General improvements

This release includes the following new features and improvements in both Sage 300cloud web screens and Sage 300 classic screens:

#### Sage 300 is more secure

This update makes significant improvements to application security and requires a multi-step installation process and changes to the system setup. Please review all instructions before beginning any update. Additionally, some third-party applications may be impacted by these changes. Please check with your third-party add-on providers for compatibility. For more information, see Sage Knowledgebase article 119319 .

## What's new in Product Update 1

This section contains a summary of new features and changes in Product Update 1.

### Sage 300 desktop screens new features

This product update includes the following new features in Sage 300 classic desktop screens:

- User Activity Report. This feature is only available to the Sage 300 administrator user, and users who are granted login/logout information permissions in the Administrative Services module. This report prints a user activity log for the companies in the system database, which includes the following:

- Login

- Logout

- Open a screen

- Close a screen

- Eviction

The report displays the following columns:

- Date and Time

- Company ID

- Action

- Platform

- Screen ID

- Screen Name

- Computer Name / Address

### Sage 300 desktop screens improvements

This product update includes the following improvements in Sage 300 classic desktop screens:

- User Activity Report database setup. A new checkbox was added for Sage 300 classic desktop screens only. The checkbox is called Enable User Activity Logs and was added to the existing Database Setup desktop screen when editing the system database. This allows Sage 300 to start or stop recording user activity for companies in this system database.

- Form 1099 and Aatrix integration. With the 2023.1 update, released in December 2022, Sage 300 desktop supports three types of Form 1099's:

- Interest Income form: 1099-INT
- Miscellaneous Information form: 1099-MISC
- Nonemployee Compensation form: 1099-NEC

- Important changes include:

- More amount types were added to support the 1099-INT form.

- The A/P Electronic Filing screen was removed.

- Some fields on the A/P 1099 Filing screen were renamed, and new buttons were added:

- Process - Button added

- History - Button added

- Title - Field added

- Transfer Agent - Field added

- The following report can be used to integrate with Aatrix:

- 1099 Filing report: A/P Vendor Reports > Select 1099 Filing

- Complete the applicable fields and continue to the 1099 Setup Wizard.

- The integration between the 1099 Form and Aatrix is as follows:

- From the A/P 1099 / CPRS Codes screen, set up your codes and map them to the correct amount types.

- From the A/P Vendors screen, assign a 1099 Code to the vendor.

- Enter the A/P Invoice for the vendor with 1099 amounts and post the invoice.

- Apply A/P Payment for the invoice and post the payment.

- From the 1099 / CPRS Inquiry screen, verify that the 1099 amounts for the vendor is correct.

- When the user is ready to file the 1099, go to A/P 1099 Filing, enter the information and click on Process. Follow the steps through the Aatrix Wizard.

### Sage 300cloud web screens improvements

This release includes the option to install Sage 300cloud web screens: modernized versions of Sage 300 screens that you can use in a web browser.

Web screens run in parallel with Sage 300 desktop screens, so there's no need to choose between desktop or web. Everyone in your organization can use the interface that best suits their needs, while working seamlessly with a single shared set of company data.

Here's a quick overview of what's new in Sage 300cloud web screens:

- New Project and Job Costing web screens. This release includes the following new web screens for Project and Job Costing:

- Revise Estimates. Use this screen to enter changes to project estimates.
- Project and Job Costing also has a Post Transactions screen. For the 2023.1 release we made Revise Estimates** available for posting.

- **New Inventory Control web screens**. This release includes the following new web screens for Inventory Control:

- **Bills of Material**. Use this screen to set up bills of material if you plan to assemble or repackage inventory items to create a supply of 'master items' to sell.
- **Assemblies/Disassemblies**. Use this screen to enter and post assemblies and disassemblies of master items from component items.

- Inventory Control web screens (continued). Related functions are now available on other screens in Inventory Control. All screens listed below are in Inventory Control:

- On the **Post Transactions** screen, post assemblies/disassemblies.
- On the **Posting Journals** screen, print posting journals for assemblies/disassemblies.
- On the **Transaction Listings** screen, print transaction listings for assemblies/disassemblies.
- On the **Transaction History Inquiry** screen, allow a drill down to assemblies/disassemblies documents.
- On the **Stock Transaction Inquiry** screen, allow a drill down to assemblies/disassemblies documents.

Important! To use Sage 300cloud web screens, data must be protected with Secure Socket Layer (SSL). When using Sage 300cloud web screens over an external network or the internet, additional security measures are required, such as a Virtual Private Network (VPN). To determine appropriate security measures, consult with your information technology (IT) professional or Sage Business Partner.

Web screens are available in English, French, Spanish, and Chinese (Simplified and Traditional).

Help and documentation for web screens are available in English and French.

Release Notes are available in English, French and Chinese (Simplified).

## What's new in Sage 300 2023

This section contains a summary of new features and changes in the 2023 release.

### General improvements

This release includes the following new features and improvements in both Sage 300cloud web screens and Sage 300 classic screens:

- Sage 300 is more secure:

- User passwords. In Sage 300 Database Setup, on the Advanced Security Settings screen, there is now only one option to require complex passwords. The complexity requirements are increased so passwords must include at least one of each of the following:

- Lower case letter
- Upper case letter
- Number
- Special character (such as * or #)
If you require complex passwords and you use Sage Fixed Assets integrated with Sage 300, you must update your system as explained in Sage Knowledgebase article 115839 .
For more information, see Setting Up Global Security.

- System and databases. We've made some technical upgrades and enhancements to improve overall security. If you are upgrading from a previous version of Sage 300, you may need to make some corresponding changes to your system setup. For more information, see Solution ID 240208215144570 .

### Sage 300cloud web screens improvements

This release includes the option to install Sage 300cloud web screens: modernized versions of Sage 300 screens that you can use in a web browser.

Web screens run in parallel with Sage 300 desktop screens, so there's no need to choose between desktop or web. Everyone in your organization can use the interface that best suits their needs, while working seamlessly with a single shared set of company data.

Here's a quick overview of what's new in Sage 300cloud web screens:

- New Inventory Control web screens. This release includes the following new web screens for Inventory Control:

- Assemblies/Disassemblies. Use this screen to enter and post assemblies and disassemblies of master items from component items.
Also, related functions are now available on other screens:

- On the Post Transactions screen, post assemblies/disassemblies.
- On the Posting Journals screen, print posting journals for assemblies/disassemblies.
- On the Transaction Listings screen, print transaction listings for assemblies/disassemblies.
- Bills of Material. Use this screen to set up bills of material if you plan to assemble or repackage inventory items to create a supply of "master items" to sell.
- Lot Recalls/Releases. Use this screen to process recall documents for lotted items that you withdraw from sales, and subsequent release documents if you restore the availability of recalled items.
- Serial Numbers. Use this screen to view and edit details for serial numbers.

- New Project and Job Costing web screens. This release includes the following new web screens for Project and Job Costing:

- Account Sets. Use this screen to create groups of general ledger accounts, which you assign to contracts to identify the general ledger accounts to which you post Project and Job Costing transactions for each contract.
- Charges. Use this screen to record amounts that you charge your customers for services or fees for which you have not incurred any costs directly (such as registration fees or prepayments on a project).
- Revise Estimates. Use this screen to enter changes to estimates for projects, categories, and resources.
- Update Retainage. If you use retainage accounting, use this screen to enter opening retainage balances for contracts you are transferring to Sage 300 Project and Job Costing from another job-costing system. You also use this screen to update the retainage payable or retainage receivable for contracts, projects, and categories.

- New setup report web screens. For the following Sage 300cloud applications, setup reports are now available in web screens:

- Accounts Payable
- Accounts Receivable
- General Ledger
- Tax Services
- Bank Services
- Inventory Control
- Order Entry
- Purchase Orders
- Project and Job Costing

- Use your keyboard to open screens from the navigation menu. New keyboard shortcuts for the navigation menu let you move around the menu and open screens from it.

To learn more about new web screens and features available in this release, see the following documentation and resources:

- Sage 300cloud web screens online help

- Sage 300cloud web screens getting started guide

Important! To use Sage 300cloud web screens, data must be protected with Secure Socket Layer (SSL). When using Sage 300cloud web screens over an external network or the internet, additional security measures are required, such as a Virtual Private Network (VPN). To determine appropriate security measures, consult with your information technology (IT) professional or Sage Business Partner.

Web screens are available in English, French, Spanish, and Chinese (Simplified and Traditional). Help and documentation for web screens is available in English and French.

### Improvements on the Windows Start menu

We've improved the organization of Sage 300 items on the Windows Start menu so you can find things more easily. Instead of a single Sage menu, there are now three menus: Sage 300, Sage 300 Admin Utilities, and Sage 300 Support Utilities.

Also, we've added some new items (in the Sage 300 Admin Utilities menu) so you can use features without needing to open Sage 300:

- Data Activation

- License Manager

- Current Users

To get the best experience with the improved Start menu, uninstall your previous version of Sage 300 before installing Sage 300 2023. If you don't do this, the Start menu will show both the old menu and the new menus.

### CRM Integration improvements

- On the E/W Sage CRM Setup screen, in the Sage CRM Server Name field you can now enter up to 60 characters.
Note: If Sage 300 and Sage CRM are on two separate servers, the Access-Control-Allow-Origin setting in the Online\web.config file no longer defaults to * (an asterisk). Instead, the specified Sage CRM Server Name is appended to this setting. For more information, see Sage Knowledgebase article 250505210452003.

- If you use Sage CRM integrated with Sage 300, if you change the customer contact name (on the Contact tab of the A/R Customers screen) you can indicate whether and how to update information in Sage CRM.

Published: December 29, 2025

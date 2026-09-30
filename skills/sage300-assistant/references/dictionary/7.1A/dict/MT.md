# MT module - compiled AOM dictionary

## MTCONC - Contacts (view MT0100)
Keys (first = PK; D=dups allowed, M=modifiable): IDCONTACT
Fields (NAME type description [values]):
  IDCONTACT String*24 Contact Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATEINAC Date Inactive Date
  SWACTV Integer Status [0=Inactive,1=Active]
  DATELASTMN Date Date Last Maintained
  SALUTATION String*10 Salutation
  FIRSTNAME String*60 First Name
  MIDDLENAME String*60 Middle Name
  LASTNAME String*60 Last Name
  TITLE String*60 Title
  TEXTSTRE1 String*60 Address Line 1
  TEXTSTRE2 String*60 Address Line 2
  TEXTSTRE3 String*60 Address Line 3
  TEXTSTRE4 String*60 Address Line 4
  NAMECITY String*30 City
  CODESTTE String*30 State/Prov.
  CODEPSTL String*30 Zip/Postal Code
  CODECTRY String*30 Country
  SWOKEMAIL Integer Consents to Receive Email [0=No,1=Yes]
  TEXTPHON1 String*30 Phone Number 1
  TEXTPHON2 String*30 Phone Number 2
  TEXTPHON3 String*30 Phone Number 3
  TEXTFAX String*30 Fax Number
  EMAIL String*255 Email
  COMMENT1 String*250 Comment 1
  COMMENT2 String*250 Comment 2
  WEBSITE String*100 Web Site
  CRMPRSNID Long CRM Person ID
  VALUES Long Optional Fields

## MTCONCF - Contact Forms (view MT0105)
Keys (first = PK; D=dups allowed, M=modifiable): IDAPP+IDFORM
Fields (NAME type description [values]):
  IDAPP String*2 Source Application
  IDFORM Integer Form ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*32 Description
  IDRESOURCE Long Resource ID
  SWARCUS Integer Customer Related [0=No,1=Yes]
  SWAPVEN Integer Vendor Related [0=No,1=Yes]
  SWARNAT Integer National Account Related [0=No,1=Yes]

## MTCONCO - Contact Optional Field Values (view MT0110)
Keys (first = PK; D=dups allowed, M=modifiable): IDCONTACT+OPTFIELD; OPTFIELD+IDCONTACT
Fields (NAME type description [values]):
  IDCONTACT String*24 Contact Code
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUE String*60 Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes,99=Not Applicable]

## MTOFD - Optional Fields (view MT0405)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION+OPTFIELD
Fields (NAME type description [values]):
  LOCATION Integer Location [0=Contacts]
  OPTFIELD String*12 Optional Field
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DEFVAL String*60 Default Value
  TYPE Integer Type [1=Text,100=Amount,6=Number,8=Integer,9=Yes/No,3=Date,4=Time]
  LENGTH Integer Length
  DECIMALS Integer Decimals
  ALLOWNULL Boolean Allow Blank [0=No,1=Yes]
  VALIDATE Boolean Validate [0=No,1=Yes]
  INITFLAG Integer Auto Insert [0=No,1=Yes]
  SWREQUIRED Integer Required [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes]

## MTOFH - Optional Field Locations (view MT0410)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION
Fields (NAME type description [values]):
  LOCATION Integer Location [0=Contacts]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUES Long Number of Values

#change because of prob in holder table
import sqlite3

conn = sqlite3.connect('assetmanage.db')

# create cursor
c = conn.cursor()

# create tables
c.execute(""" CREATE TABLE Holder (
    HolderID int NOT NULL,
    Holder_Password varchar(255),
    Holder_Email varchar(255),
    Holder_Name varchar(255),
    Holder_Type varchar(255),
    PRIMARY KEY (HolderID)

)""")

c.execute("""CREATE TABLE Asset (
    AssetID int,
    Asset_Type varchar(255),
    Asset_Name varchar(255),
    HeldBy int,
    PRIMARY KEY (AssetID),
   FOREIGN KEY (HeldBy) REFERENCES Holder(HolderID)

)""")

c.execute("""CREATE TABLE AssetDescription (
    AssetID int,
    Current_Valuation float(10),
    Date_Added date,
    Address varchar(255),
    AssetPerformance varchar(255),
    PRIMARY KEY (AssetID),                  
    FOREIGN KEY (AssetID) REFERENCES Asset(AssetID)

)""")

c.execute("""CREATE TABLE Details (
    AssetID int,
    PrimaryDetail varchar(255),
    SecondaryDetail varchar(255),
    ThirdDetail varchar(255),
    PRIMARY KEY (AssetID),
    FOREIGN KEY (AssetID) REFERENCES Asset(AssetID)

)""")

c.execute("""CREATE TABLE AssetBehaviour (
    AssetID int,
    Total_Appreciation_Deprecation varchar(255),
    YoY_Change float(10),
    Liquidity varchar(255),
    Tangibility varchar(255),
    Risk_Level varchar(255),
    PRIMARY KEY (AssetID),
    FOREIGN KEY (AssetID) REFERENCES Asset(AssetID)

)""")



c.execute("""CREATE TABLE TradeListing (
    ListingID int,
    Listing_Date date,
    ListedBy int,
    AssetListed int,
    ListedByName varchar(255),
    List_Price float(10),
    PRIMARY KEY (ListingID),
    FOREIGN KEY (AssetListed) REFERENCES Asset(AssetID),
    FOREIGN KEY (ListedBy) REFERENCES Holder(HolderID)

)


""")

conn.commit()
conn.close()


CREATE TABLE Renter (
    RenterNumber INT PRIMARY KEY,
    FirstName VARCHAR(50),
    MiddleInitial CHAR(1),
    LastName VARCHAR(50),
    Address VARCHAR(100),
    City VARCHAR(50),
    State CHAR(2),
    PostalCode CHAR(10),
    TelephoneNumber VARCHAR(15),
    EmailAddress VARCHAR(100)
);


CREATE TABLE Property (
    CondoLocationNumber INT PRIMARY KEY,
    CondoLocationName VARCHAR(100),
    Address VARCHAR(100),
    City VARCHAR(50),
    State CHAR(2),
    PostalCode CHAR(10),
    CondoUnitNumber VARCHAR(20),
    SquareFootage DECIMAL(10, 2),
    NumberOfBedrooms INT,
    NumberOfBathrooms INT,
    MaxSleepCapacity INT,
    BaseWeeklyRate DECIMAL(10, 2)
);


CREATE TABLE RentalAgreement (
    AgreementID INT PRIMARY KEY,
    RenterNumber INT,
    FirstName VARCHAR(50),
    MiddleInitial CHAR(1),
    LastName VARCHAR(50),
    Address VARCHAR(100),
    City VARCHAR(50),
    State CHAR(2),
    PostalCode CHAR(10),
    TelephoneNumber VARCHAR(15),
    StartDate DATE,
    EndDate DATE,
    WeeklyRentalAmount DECIMAL(10, 2),
    FOREIGN KEY (RenterNumber) REFERENCES Renter(RenterNumber)
);

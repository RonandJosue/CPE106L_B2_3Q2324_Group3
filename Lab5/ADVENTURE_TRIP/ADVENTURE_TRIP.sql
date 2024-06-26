CREATE TABLE ADVENTURE_TRIP (
    TRIP_ID INTEGER PRIMARY KEY,
    TRIP_NAME VARCHAR,
    START_LOCATION VARCHAR,
    STATE VARCHAR,
    DISTANCE NUMBER,
    MAX_GRP_SIZE NUMBER,
    TYPE VARCHAR,
    SEASON VARCHAR
);

PRAGMA table_info(ADVENTURE_TRIP);


INSERT INTO ADVENTURE_TRIP (TRIP_ID, TRIP_NAME, START_LOCATION, STATE, DISTANCE, MAX_GRP_SIZE, TYPE, SEASON)
VALUES (45, 'Jay Peak', 'Jay', 'VT', 8, 8, 'Hiking', 'Summer');

SELECT * FROM ADVENTURE_TRIP;

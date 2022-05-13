PRAGMA foreign_keys = ON;

CREATE TABLE BOOK(
    ID    INTEGER PRIMARY KEY AUTOINCREMENT, 
    TITLE TEXT NOT NULL,
    IMG BLOB
);

CREATE TABLE PAGES(
    ID      INTEGER PRIMARY KEY AUTOINCREMENT,
    NUM     INTEGER NOT NULL,
    IMG     BLOB,
    BOOK    INTEGER NOT NULL,
    FOREIGN KEY(BOOK) REFERENCES BOOK(ID)
    ON DELETE CASCADE
);

CREATE TABLE PAGE_CONTENTS(
    ID      INTEGER PRIMARY KEY AUTOINCREMENT,  
    PT      TEXT,
    EN      TEXT,
    PAGEID  INTEGER NOT NULL,
    FOREIGN KEY(PAGEID) REFERENCES PAGES(ID)
);


CREATE TABLE WORDS(
    WORD_EN    TEXT PRIMARY KEY,
    WORD_PT    TEXT,
    FIGURE     BLOB
);



-- INSERT INTO PAGES (NUM, BOOK) VALUES(1, 1)
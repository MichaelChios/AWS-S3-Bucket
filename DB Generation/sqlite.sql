DROP TABLE IF EXISTS superhero;
CREATE TABLE superhero (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(255) NOT NULL,
    description varchar(255) NOT NULL,
    powers varchar(255) NOT NULL,
    appearance varchar(255) NOT NULL,
    quote varchar(255) NOT NULL,
    ally varchar(255) NOT NULL,
    enemy varchar(255) NOT NULL,
    affiliation varchar(255) NOT NULL,
    first_appearance varchar(255) NOT NULL,
    creator varchar(255) NOT NULL,
    aka varchar(255) NOT NULL
);
DROP TABLE IF EXISTS superhero;
CREATE TABLE superhero (
    id INTEGER PRIMARY KEY NOT NULL,
    name varchar(255) NOT NULL,
    description varchar(255) NOT NULL,
    powers varchar(255) NOT NULL,
    quotes varchar(255) NOT NULL,
    affiliation varchar(255) NOT NULL,
    creators varchar(255) NOT NULL,
    aka varchar(255) NOT NULL
);

DROP INDEX IF EXISTS index_id;
CREATE INDEX index_id ON superhero (id);
DROP INDEX IF EXISTS index_name;
CREATE INDEX index_name ON superhero (name);
DROP INDEX IF EXISTS index_description;
CREATE INDEX index_description ON superhero (description);
DROP INDEX IF EXISTS index_powers;
CREATE INDEX index_power ON superhero (powers);
DROP INDEX IF EXISTS index_quotes;
CREATE INDEX index_quote ON superhero (quotes);
DROP INDEX IF EXISTS index_affiliation;
CREATE INDEX index_affiliation ON superhero (affiliation);
DROP INDEX IF EXISTS index_creators;
CREATE INDEX index_creator ON superhero (creators);
DROP INDEX IF EXISTS index_aka;
CREATE INDEX index_aka ON superhero (aka);
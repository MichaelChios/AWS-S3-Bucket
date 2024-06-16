DROP TABLE IF EXISTS superhero;
CREATE TABLE superhero (
    id INTEGER PRIMARY KEY NOT NULL,
    name varchar(255) NOT NULL,
    description varchar(255) NOT NULL,
    power varchar(255) NOT NULL,
    appearance varchar(255) NOT NULL,
    quote varchar(255) NOT NULL,
    ally varchar(255) NOT NULL,
    enemy varchar(255) NOT NULL,
    affiliation varchar(255) NOT NULL,
    first_appearance varchar(255) NOT NULL,
    creator varchar(255) NOT NULL,
    aka varchar(255) NOT NULL
);

DROP INDEX IF EXISTS index_id;
CREATE INDEX index_id ON superhero (id);
DROP INDEX IF EXISTS index_name;
CREATE INDEX index_name ON superhero (name);
DROP INDEX IF EXISTS index_description;
CREATE INDEX index_description ON superhero (description);
DROP INDEX IF EXISTS index_power;
CREATE INDEX index_power ON superhero (power);
DROP INDEX IF EXISTS index_appearance;
CREATE INDEX index_appearance ON superhero (appearance);
DROP INDEX IF EXISTS index_quote;
CREATE INDEX index_quote ON superhero (quote);
DROP INDEX IF EXISTS index_ally;
CREATE INDEX index_ally ON superhero (ally);
DROP INDEX IF EXISTS index_enemy;
CREATE INDEX index_enemy ON superhero (enemy);
DROP INDEX IF EXISTS index_affiliation;
CREATE INDEX index_affiliation ON superhero (affiliation);
DROP INDEX IF EXISTS index_first_appearance;
CREATE INDEX index_first_appearance ON superhero (first_appearance);
DROP INDEX IF EXISTS index_creator;
CREATE INDEX index_creator ON superhero (creator);
DROP INDEX IF EXISTS index_aka;
CREATE INDEX index_aka ON superhero (aka);
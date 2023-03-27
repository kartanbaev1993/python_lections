# Slash commands
* \l - spisok vseh bazy dannyh
* \c - pokazyvaet cherez kakogo usera i k kakoi baze dannyh my podklyucheny
* \c name_of_db - podklyuchenie k kakoi-to baze dannyh
* \du - spisok vseh userov v postges
* \dt - spisok vseh tablic v tekushei baze dannyh
* \d+ - bolee podrobnaya informaciya o tablicah v tekushei baze dannyh
* \d+ name_of_table - bolee podrobnaya informaciya o tablice
* \q - vyhod iz subd(psql)

# Sozdanie bazy dannyh i tablic
```sql
CREATE DATABASE name_of_db;
-- sozdanie bazy dannyh
```

```sql
CREATE TABLE name_of_table(
    column1 data_type1,
    column2 data_type2,
    ...
);
-- sozdanie tablicy s polyami
```
# Udalenie bazu dannyh i tablic
```sql
DROP DATABASE name_of_db;
-- udalenie bazu dannyh
```
```sql
DROP TABLE name_of_table;
-- udalenie tablicy
```

# Zapolnenie tablic
```sql
INSERT INTO name_of_db VALUES
(val1, val2),
(val1.2, val2.2);
-- zapis' dannyh v tablicu (zapolnenie vseh polei)
```


# Vyvod dannyh iz tablicy
```sql
SELECT * FROM name_of_table;
-- vyvod vseh zapisei so vsemi polyami
```

```sql
SELECT column1, column3 FROM name_of_table;
-- vyvod konkretnyh polei
```

# Usloviya
```sql
DELETE FROM name_of_table WHERE condition;
-- udalenie vseh zapisei iz tablicy sootvetstvuyushih dannomu usloviyu
```
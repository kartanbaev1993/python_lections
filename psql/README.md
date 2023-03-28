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

```sql
SELECT * FROM name_of_table WHERE column = 'hello';
-- strogoe ravenstvo
```

```sql
SELECT * FROM name_of_table WHERE column LIKE '%hello%';
-- zapisi vklyuchayushie v sebya dannuyu stroku s uchetom registra
-- aaahello
-- hello world
-- hello
-- Hello world - ne proidet (potomu chto registr drugoi)
```

```sql
SELECT * FROM name_of_table WHERE column ILIKE '%hello%';
-- zapisi vklyuchayushie v sebya dannuyu stroku bez ucheta registra
-- aaahello
-- hello world
-- hello
-- Hello world
-- HeLLo
```

```sql
SELECT * FROM name_of_table ORDER BY column;
-- sortirovka zapisei po dannomu polyu v poryadke vozrastaniya
```


```sql
SELECT * FROM name_of_table ORDER BY column DESC;
-- sortirovka zapisei po dannomu polyu v poryadke ubyvaniya
```


```sql
SELECT * FROM name_of_table LIMIT 10;
-- vyvod pervyx 10 zapisei
```


```sql
SELECT * FROM name_of_table OFFSET 10;
-- propuskaem pervye 10 zapisei
```


```sql
SELECT * FROM name_of_table LIMIT 10 OFFSET 5;
-- propuskaem pervye 5 zapisei
-- vytaskivaem 10 zapisei
```

# Obnovlenie tablicy
```sql
ALTER TABLE name_of_table ADD COLUMN col_name col_type constraint;
-- dobavlyaem novuyu kolonku v tablicy
```

```sql
ALTER TABLE name_of_table DROP COLUMN col_name;
-- udalyaem kolonku iz tablicy
```

```sql
ALTER TABLE name_of_table RENAME COLUMN col_type TO new_col_name;
-- pereimennovyvanie kolonki
```

```sql
ALTER TABLE name_of_table ALTER COLUMN col_name SET DATA TYPE new_type;
-- izmenenie tipa dannyh u polya
```


# Ogranicheniya (constraints)
* UNIQUE - ne razreshaet dublikaty
* NOT NULL - trebuet obyazatel'nogo zapolneniya polya



# Svyazi
## Vidy svyazei
> Odin k odnomu (one to one)
* odin chelovek - odin profil'
* odin avtor - odna avtobiografiya

> Odin ko mnogim (one to many)
* odin blogger - mnogo postov
* odna marka - mnogo modelei
* odna strana - mnogo oblastei
* odin produkt - mnogo komentariev

> Mnogie ko mnogim (many to many)
* odin razrabotchik - mnogo proektov. odin proekt - mnogo razrabotchikov



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
* `UNIQUE` - ne razreshaet dublikaty
* `NOT NULL` - trebuet obyazatel'nogo zapolneniya polya
* `PRIMARY KEY` - kak UNIQUE i NOT NULL + stroit binary tree dlya bystrogo poiska
* `FOREIGN KEY` - ssylaetysa na pk v drugoi tablice i proveryaet sushestvuet li takoi id



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


## Realizaciya one2many v postgres
```sql
CREATE TABLE blogger (
    id serial PRIMARY KEY,
    name varchar(50),
    age int
);

CREATE TABLE post (
    id serial PRIMARY KEY,
    title varchar(100),
    body text,
    blogger_id int.

    CONSTRAINT fk_post_blogger
    FOREIGN KEY (blogger_id) REFERENCES blogger (id)
);
```

# JOINS
> **JOIN** - instrukciya, kotoraya pozvolyaet odnim SELECTom, brat' 
dannye iz dvuh tablic (u kotoryh est' svyazannye polya)

> **INNER JOIN (JOIN)** - dostayutsya tol'ko te zapisi u kotoryh est' 
dannye v oboih tablicah
> **FULL JOIN** - dostayutsya vse zapisi i s pervoi tablicy i so vtoroi

## реализация one2one в postgres
```sql
CREATE TABLE author (
    id serial PRIMARY KEY,
    name varchar(50),
    last_name varchar(70)
);
CREATE TABLE autobiography (
    id serial PRIMARY KEY,
    published date,
    body text,
    author_id int UNIQUE, -- чтобы создать one - one, добавляем unique
    CONSTRAINT fk_author_bio
    FOREIGN KEY (author_id) REFERENCES author (id)
);
```

## реализация many2many в postgres
```sql
CREATE TABLE developer (
    id serial PRIMARY KEY,
    name varchar(50),
    age int,
    experience int
);
CREATE TABLE project (
    id serial PRIMARY KEY,
    title varchar(100),
    tz text,
    deadline date
);
CREATE TABLE dev_proj (
    dev_id int,
    proj_id int,
    CONSTRAINT fk_dev_m2m
    FOREIGN KEY (dev_id) REFERENCES developer (id),
    CONSTRAINT fk_proj_m2m
    FOREIGN KEY (proj_id) REFERENCES project (id)
);
```


# JOINS
> **JOIN** - инструкция, которая позволяет одним SELECT, брать данные из двух таблиц (у которых есть связанные поля)
> **INNER JOIN (JOIN)** - достаются только те записи у которых есть данные в обоих таблицах
> **FULL JOIN** - достаются все записи и с первой таблицы и со второй
> **FULL JOIN** - достаются все записи и с первой таблицы и со второй
```sql
-- one2one / one2many
SELECT * FROM blogger 
JOIN post ON blogger.id = post.blogger_id;
```

```sql
-- many2many
SELECT * FROM developer
JOIN dev_proj ON developer.id = dev_proj.dev_id
JOIN project ON project.id = dev_proj.proj_id;
```


# Agregatnye funkcii
> vse agregatnye funkcii ispol'zuyutsya s `group by`

> **SUN** - schitaet summu vseh zapisei v sgruppirovannom pole

```sql
SELECT customer.name, SUM(product.price) 
FROM customer 
JOIN cart ON customer.id = cart.customer_id
JOIN product ON product.id = cart.product_id
GROUP BY (customer.id);
--    name    | sum  
------------+------
-- customer 2 |  470
-- customer 3 |  688
-- customer 1 | 1079


```

> **AVG** - schitaet srednee znachenie vseh zapisei v sgruppirovannom pole

```sql
SELECT customer.name, AVG(product.price) 
FROM customer 
JOIN cart ON customer.id = cart.customer_id
JOIN product ON product.id = cart.product_id
GROUP BY (customer.id);
--    name    | avg 
------------+------
-- customer 2 |  470.00
-- customer 3 |  688.00
-- customer 1 | 1079.67
```


> **ARRAY_AGG** - sobiraet znachenie vseh zpisei v sgruppirovannom pole v massiv (spisok)

```sql
SELECT blogger.name, ARRAY_AGG(post.body) FROM blogger 
JOIN post ON blogger.id = post.blogger_id
GROUP BY (blogger.id);
--   name    |                         array_agg                         
-----------+-----------------------------------------------------------
-- blogger 1 | {"my first blog","today is a good day","it is my b-day!"}
-- blogger 2 | {"my first post","some post"}
-- blogger 3 | {"i am not a blogger"}
```

> **MIN/MAX** - vybiraet minimal'noe/maksimal'noe znachenie iz vseh
zapisei v sgruppirovannom pole

```sql
SELECT blogger.name, MAX(post.created_at), MIN(post.created_at) FROM blogger JOIN post ON blogger.id = post.blogger_id
GROUP BY (blogger.id);
--   name    |    max     |    min     
-----------+------------+------------
-- blogger 2 | 2022-06-23 | 2013-05-10
-- blogger 3 | 2022-08-15 | 2022-08-15
-- blogger 1 | 2021-09-30 | 2020-08-01
```

> **COUNT** - schitaet kol-vo zapisei v sgruppirovannom pole

```sql
SELECT blogger.name, COUNT(post.id) FROM blogger 
JOIN post ON blogger.id = post.blogger_id
GROUP BY (blogger.id)
--   name    | count 
-----------+-------
-- blogger 2 |     2
-- blogger 3 |     1
-- blogger 1 |     3
```


# Import/Export baz dannyh

write from file to db
```bash
psql db_name < file.sql
# pri etom db_name doljna sushestvovat'
```

write from db to file
```bash
pg_dump db_name > file.sql
```
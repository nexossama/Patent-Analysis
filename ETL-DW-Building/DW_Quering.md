## 1D Analysis

##### Count of Selected Patents Inventors

```sql
-- Retrieve count of (seleceted) patents inventors
SELECT SUM(count)
FROM
(SELECT DISTINCT code_patent, Count(*) FROM "FactPublication"
-- WHERE code_patent IN ('', '', '')
GROUP BY code_patent, id_time 
ORDER BY count DESC)
```

##### Count of Selected Patents Countries

```sql
-- Retrieve count of (seleceted) patents countries
SELECT COUNT(DISTINCT country_name)
FROM "DimCountry" as dc
JOIN "DimPatent" as dp ON dp.id_country=dc.id_country
 -- WHERE code_patent IN ('', '', '');
```

##### Count of Selected Patents Title Keywords

```sql
-- Retrieve count of (seleceted) patents title keywords
SELECT SUM(count)
FROM
(SELECT DISTINCT code_patent, COUNT(id_keyword) FROM "FactKeyword" as fk
JOIN "DimTitle" as dt ON dt.id_title=fk.id_title
JOIN "DimPatent" as dp ON dp.id_title=dt.id_title
-- WHERE code_patent IN ('', '', '')
GROUP BY code_patent, id_inventor, id_assignee);
```

##### TOP 5 Keywords of Selected Patents

```sql
-- Retrieve top 5 keywords of the selected patents
SELECT DISTINCT keyword, Count(*) FROM "DimKeyword" as dk
JOIN "FactKeyword" as fk ON fk.id_keyword=dk.id_keyword
JOIN "DimTitle" as dt ON dt.id_title=fk.id_title
JOIN "DimPatent" as dp ON dp.id_title=dt.id_title
-- WHERE code_patent IN ('', '', '')
GROUP BY keyword, id_inventor, id_assignee
ORDER BY count DESC LIMIT 5;
```

##### Countries Frequency Of The Selected Patents

```sql
-- Retrieve Countries Frequency Of The Selected Patents
SELECT country_name, Count(*) total FROM "DimCountry" as dc
JOIN "DimPatent" as dp ON dp.id_country=dc.id_country
-- WHERE code_patent IN ('', '', '')
GROUP BY country_name;
```


## 2D Analysis


##### TOP 3 Keywords Of The Selected Patents For Each Country

```sql
-- Retrieve top 5 keywords of selected patents for each country
SELECT DISTINCT country_name, keyword, Count(*) key_occurrence FROM "DimKeyword" as dk
JOIN "FactKeyword" as fk ON fk.id_keyword=dk.id_keyword
JOIN "DimCountry" as dc ON dc.id_country=fk.id_country
JOIN "DimPatent" as dp ON dp.id_title = fk.id_title
-- WHERE code_patent IN ('', '', '')
GROUP BY country_name, keyword, id_assignee, id_inventor, fk.id_title, id_time
ORDER BY key_occurrence DESC LIMIT 5;
```

##### TOP 3 Keywords Of The Selected Patents For Each Country

```sql
-- Retrieve top 5 keywords of selected patents for each country
SELECT DISTINCT country_name, keyword, Count(*) key_occurrence FROM "DimKeyword" as dk
JOIN "FactKeyword" as fk ON fk.id_keyword=dk.id_keyword
JOIN "DimCountry" as dc ON dc.id_country=fk.id_country
JOIN "DimPatent" as dp ON dp.id_title = fk.id_title
-- WHERE code_patent IN ('', '', '')
GROUP BY country_name, keyword, id_assignee, id_inventor, fk.id_title, id_time
ORDER BY key_occurrence DESC LIMIT 5;
```

##### Number Of Patent Publications By Year

```sql
-- Retrieve number of patents by year
SELECT year, Count(*) as total_patents
FROM
(SELECT "year" FROM "FactPublication" as fp
JOIN "DimPatent" as dp ON dp.code_patent=fp.code_patent
JOIN "DimTime" as dt ON dt.id_time=fp.id_time
-- WHERE code_patent IN ('', '', '')
GROUP BY "year", id_inventor)
GROUP BY year
ORDER BY total_patents DESC;
```
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

##### Top 5 Keywords of Selected Patents

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

```sql
-- Retrieve employees with high salaries
SELECT * FROM employees
WHERE salary > 50000;
```

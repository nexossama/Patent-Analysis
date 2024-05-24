## 1D Analysis

##### Count of Selected Patents Inventors

```sql
-- Retrieve count of (seleceted) patents inventors
SELECT SUM(count)
FROM
(SELECT DISTINCT code_patent, Count(*) FROM "FactGrant"
-- WHERE code_patent IN ('', '', '')
GROUP BY code_patent, id_time, id_assignee
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

## 2D Analysis

```sql
-- Retrieve employees with high salaries
SELECT * FROM employees
WHERE salary > 50000;
```

## 3D Analysis

```sql
-- Retrieve employees with high salaries
SELECT * FROM employees
WHERE salary > 50000;
```

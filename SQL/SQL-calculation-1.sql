SELECT ticker, date_trunc('month', day) AS date_month, avg(price) as price
FROM imported_closes
WHERE day BETWEEN '2008-01-01' AND '2018-12-31'
GROUP BY ticker, date_month
SELECT ticker, date_trunc('month', day) AS date_month, avg(price) as price, max(price) as max_price, min(price) as min_price
FROM imported_closes
WHERE day BETWEEN '2008-01-01' AND '2018-12-31'
AND ticker LIKE '%.HK'
GROUP BY ticker, date_month
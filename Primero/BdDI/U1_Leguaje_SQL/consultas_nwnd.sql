-- 1 --

SELECT C.CustomerID, C.CompanyName
FROM Orders AS O
JOIN Customers AS C ON C.CustomerID = O.CustomerID
GO

-- 2 --

SELECT C.CompanyName, COUNT(*) AS Cantidad_Pedidos
FROM Orders AS O
JOIN Customers AS C ON C.CustomerID = O.CustomerID
GROUP BY C.CompanyName
GO

-- 3 --

SELECT E.EmployeeID, E.FirstName, E.LastName, SUM(OD.Quantity * (OD.UnitPrice - (OD.UnitPrice * OD.Discount))) AS VENTA_TOTAL, AVG(OD.Quantity * (OD.UnitPrice - (OD.UnitPrice * OD.Discount))) AS PROMEDIO_VENTAS
FROM Employees AS E
JOIN Orders AS O ON O.EmployeeID = E.EmployeeID
JOIN [Order Details] AS OD ON OD.OrderID = O.OrderID
GROUP BY E.EmployeeID, E.FirstName, E.LastName
GO

-- 4 --

SELECT 
	P.ProductID, 
	P.ProductName, 
	SUM(OD.Quantity * (OD.UnitPrice - (OD.UnitPrice * OD.Discount))) AS VENTA_TOTAL
FROM 
	Products AS P
JOIN 
	[Order Details] AS OD ON OD.ProductID = P.ProductID
GROUP BY 
	P.ProductID, 
	P.ProductName
HAVING 
	SUM(OD.Quantity * (OD.UnitPrice - (OD.UnitPrice * OD.Discount))) > 10000
GO

-- 5 --

SELECT
    C.CustomerID,
    C.CompanyName,
    MIN(O.OrderDate) AS FechaPrimerPedido,
    MAX(O.OrderDate) AS FechaUltimoPedido
FROM
    Customers AS C
JOIN
    Orders AS O ON C.CustomerID = O.CustomerID
GROUP BY
    C.CustomerID, C.CompanyName
ORDER BY
    C.CompanyName
GO

-- 6 --

SELECT
	C.CustomerID, 
	C.CompanyName,
	COUNT(*) AS CantidadPedidos
FROM
	Customers AS C
JOIN
	Orders AS O ON O.CustomerID = C.CustomerID
GROUP BY
	C.CustomerID, 
	C.CompanyName
HAVING
	COUNT(*) > 20

-- 7 --

SELECT
	P.ProductName,
	C.CategoryName,
	AVG(O.Quantity) AS AVG_ORDERS
FROM 
	[Order Details] AS O
JOIN 
	Products AS P ON O.ProductID = P.ProductID
JOIN 
	Categories AS C ON C.CategoryID = P.CategoryID
GROUP BY 
	C.CategoryName,
	P.ProductName
GO

-- 8 --

SELECT
	O.ShipCountry, 
	SUM(OD.Quantity * (OD.UnitPrice - (OD.UnitPrice * OD.Discount))) AS VENTAS_PAIS
FROM
	Orders AS O
JOIN
	[Order Details] AS OD ON OD.OrderID = O.OrderID
GROUP BY
	O.ShipCountry
GO

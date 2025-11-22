-- 2.a

SELECT C.nombre, C.numero
FROM cliente AS C
WHERE C.estado IN (10, 20)
GO

-- 2.b

SELECT C.nombre, C.numero 
FROM cliente AS C
JOIN pedido AS P ON P.pedido_clave = C.pedido_clave
WHERE P.pedido_clave = 'PED2'
GO

-- 2.c

SELECT * 
FROM tipo_movimiento AS TM
WHERE TM.descripcion IS NULL 
OR 
	TM.descripcion = ''
GO

-- 2.d

SELECT * 
FROM tipo_movimiento AS TM
WHERE TM.descripcion IS NOT NULL
GO

-- 2.e

SELECT P.numero, P.nombre
FROM producto AS P
WHERE P.precio BETWEEN 20 AND 50
AND
	P.color = 'blanco'

-- 2.f y g

SELECT C.numero, C.nombre, COUNT(*) AS Cantidad_Pedidos
FROM cliente AS C
JOIN orden AS O ON C.numero = O.cliente_numero
GROUP BY C.numero, C.nombre
GO


-- 2.h

SELECT C.numero, C.nombre, AVG(CU.saldo) as SALDOPROMEDIO
FROM cliente AS C
JOIN cuenta AS CU ON C.numero = CU.cliente_numero
GROUP BY C.numero, C.nombre
GO


-- 2.i

SELECT P.numero, P.nombre, COUNT(*) AS Cantidad_Ordenes
FROM producto AS P
JOIN orden AS O ON O.producto_numero = P.numero
GROUP BY P.numero, P.nombre
GO

-- 2.j

SELECT P.numero, P.nombre, COUNT(*) AS Cantidad_Ordenes
FROM producto AS P
JOIN orden AS O ON O.producto_numero = P.numero
GROUP BY P.numero, P.nombre
HAVING COUNT(*) > 2
GO
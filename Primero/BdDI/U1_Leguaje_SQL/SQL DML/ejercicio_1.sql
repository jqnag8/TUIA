-- 1.a 

SELECT nombre, apellido1, apellido2 FROM DIRECTOR d
WHERE d.dni = 33193456
GO

-- 1.b

SELECT COUNT(*) FROM  PROYECTO AS P
JOIN DPTO AS D
ON D.dptoid = P.dptoid
WHERE D.nombre = 'Investigacion'
GO

-- 1.c

SELECT TOP(1) DIR.dni FROM DIRECTOR AS DIR
JOIN DPTO AS D
ON DIR.directorid = D.directorid
WHERE D.nombre = 'Sede Central'
ORDER BY DIR.sueldo DESC
GO

-- 1.d

SELECT AVG(DIR.sueldo) 
FROM DIRECTOR AS DIR
JOIN DPTO AS D ON DIR.directorid = D.directorid
WHERE D.nombre = 'Sede Central'
GO

-- 1.e

SELECT COUNT(*)
FROM PROYECTO_EMPLEADO AS PE
JOIN PROYECTO AS P ON P.proyectoid = PE.proyectoid
JOIN DPTO AS D ON D.dptoid = P.dptoid
WHERE
    D.nombre = 'Investigacion'
AND
    P.nombre = 'ProductoX'
AND
    PE.horas >= 3; 
GO

-- 1.f

SELECT COUNT(*)
FROM EMPLEADO AS E
WHERE YEAR(E.fechanac) BETWEEN 1960 AND 1980
GO

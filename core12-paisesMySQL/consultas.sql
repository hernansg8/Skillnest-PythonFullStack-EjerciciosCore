/*	1)
¿Qué consulta ejecutarías para obtener todos los países que hablan español? 
Tu consulta debe devolver el nombre del país, el idioma y el porcentaje de habla del idioma.  
Tu consulta debe ordenar el resultado por porcentaje de habla del idioma en orden descendente. (1)
*/
SELECT 	paises.nombre, idioma, porcentage
FROM	idiomas 
JOIN	paises
ON  pais_id = paises.id
WHERE idioma = 'Español'
ORDER BY porcentage DESC;

/*	2)
¿Qué consulta ejecutarías para mostrar el número total de ciudades de cada país?
Tu consulta debe devolver el nombre del país, el idioma y el número total de ciudades. 
Tu consulta debe ordenar el resultado por el número de ciudades en orden descendente. (3)
*/
SELECT p.nombre, i.idioma, count(*) total_ciudades
FROM paises p
JOIN idiomas i ON i.pais_id = p.id
JOIN ciudades c ON c.pais_id = p.id
GROUP BY p.nombre, i.idioma
ORDER BY total_ciudades DESC;

SELECT p.nombre, count(*) total_ciudades
FROM paises p
JOIN ciudades c ON c.pais_id = p.id
GROUP BY p.nombre
ORDER BY total_ciudades DESC;

/*	3)
¿Qué consulta ejecutarías para obtener todos ciudades de Chile con una población mayor a 200,000? 
Tu consulta debe ordenar el resultado por población en orden descendente. (1)
*/
SELECT c.nombre, c.poblacion
FROM ciudades c
JOIN paises p ON p.id = c.pais_id
WHERE p.nombre = 'Chile' AND c.poblacion > 200000
ORDER BY c.poblacion DESC; 

/*	4)
¿Qué consulta ejecutarías para obtener todos los idiomas en cada país con un porcentaje de habla mayor a 89%?
 Tu consulta debe ordenar el resultado por porcentaje de habla en orden descendente. 
*/
SELECT p.nombre, i.idioma, i.porcentage
FROM paises p
JOIN idiomas i ON p.id = i.pais_id
WHERE i.porcentage > 89
ORDER BY i.porcentage DESC;

/*	5)
¿Qué consulta ejecutarías para obtener todos los países con un área de superficie menor a 501 y población mayor a 100,000?
*/
SELECT nombre, area_superficie, poblacion
FROM paises
WHERE area_superficie < 501 AND poblacion > 100000;

/*	6)
¿Qué consulta ejecutarías para obtener países en el que el tipo de gobierno es República, un capital superior a 2000
y una esperanza de vida mayor a 78 años?  (1)
*/
SELECT nombre, tipo_gobierno, capital, esperanza_vida
FROM paises
WHERE tipo_gobierno = 'República' AND capital > 2000 AND esperanza_vida > 78;

/*	7)
¿Qué consulta ejecutarías para obtener todas las ciudades de Colombia dentro del distrito de Valle con una población 
mayor a 200,000 habitantes?
La consulta debe devolver el nombre del país, el nombre de la ciudad, el distrito y la población.  (2)
*/
SELECT p.nombre, c.nombre, c.distrito, c.poblacion
FROM paises p
JOIN ciudades c ON c.pais_id = p.id
WHERE p.nombre = 'Colombia' AND c.distrito = 'Valle' AND c.poblacion > 200000;

/*	8)
¿Qué consulta ejecutarías para resumir el número de países en cada región? 
Tu consulta debe mostrar el nombre de la región y el número de países. 
Además, debe ordenar el resultado por el número de países en orden descendente. (2)
*/
SELECT region, count(*) numero_paises
FROM paises
GROUP BY region
ORDER BY numero_paises DESC;

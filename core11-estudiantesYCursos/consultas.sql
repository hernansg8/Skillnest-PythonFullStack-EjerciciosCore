--	Consulta: Crea 3 cursos nuevos:
INSERT INTO cursos (nombre,created_at) VALUES 
	('En busca del cinturon Amarillo', now()),
    ('En busca del cinturon Naranja', now()),
    ('En busca del cinturon Rojo', now());

--	Consulta: Elimina los 3 cursos que creaste:
DELETE FROM cursos ORDER BY id DESC LIMIT 3;

--	Consulta: Crea otros 3 cursos nuevos:
INSERT INTO cursos (nombre,created_at) VALUES 
	('Por el cinturon Amarillo', now()),
    ('Por el cinturon Naranja', now()),
    ('Por el cinturon Rojo', now());
    
--	Consulta: Crea 3 estudiantes que estén inscritos en el primer curso:
INSERT INTO estudiantes (nombre, apellido, edad, created_at, curso_id) VALUES
	('Andres', 'Perez', 20, now(),4),
    ('Bastián', 'Diaz', 25, now(),4),
    ('Carlos', 'Gonzalez', 30, now(),4);

--	Consulta: Crea 3 estudiantes que estén inscritos en el segundo curso:
INSERT INTO estudiantes (nombre, apellido, edad, created_at, curso_id) VALUES
	('Diego', 'Soto', 30, now(),5),
    ('Esteban', 'Flores', 25, now(),5),
    ('Fabián', 'Gonzalez', 35, now(),5);

--	Consulta: Crea 3 estudiantes que estén inscritos en el tercer curso:
INSERT INTO estudiantes (nombre, apellido, edad, created_at, curso_id) VALUES
	('Gustavo', 'Jimenez', 30, now(),6),
    ('Hector', 'Herrera', 25, now(),6),
    ('Ivan', 'Trolazo', 35, now(),6);

--	Consulta: Recupera todos los estudiantes que estén inscritos en el primer curso:
SELECT id, nombre, apellido
FROM	estudiantes
WHERE	curso_id = (select min(id) from cursos);

--	Consulta: Recupera todos los estudiantes que estén inscritos en el último curso:
SELECT id, nombre, apellido
FROM	estudiantes
WHERE	curso_id = (select max(id) from cursos);

--	Consulta: Recupera el curso del último estudiante:
SELECT c.id, c.nombre
FROM cursos c, estudiantes e
WHERE e.curso_id = c.id AND e.id = ( select max(id) from estudiantes);


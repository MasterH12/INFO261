INSERT INTO persona(Nombre,Edad) VALUES	("Gonzalo Silva",20),
										("Angelo Escobar",20),
										("Alexander Oses",20),
										("Francisco Antilef",20),
										("Rodrigo Stevenson",20);
INSERT INTO lugar_de_interes(lugar,descripcion,categoria,latitud,longitud) VALUES
	("Escuela de informática - Miraflores","Escuela de Informática de UACH Campus Miraflores - Valdivia","Educación",-39.833551, -73.245171),
	("Biblioteca - Miraflores","Biblioteca de UACH Campus Miraflores - Valdivia", "Educación",-39.831685, -73.244783),
	("Casino - Miraflores","Casino de UACH Campus Miraflores - Valdivia","Educación",-39.832245, -73.252274),
	("Gimnasio - Miraflores","Gimnasio de UACH Campus Miraflores - Valdivia", "Deporte",-39.832576, -73.251735),
	("Cancha de Football - Miraflores","Cancha de Football Campus Miraflores","Deporte",-39.834691, -73.245395);
INSERT INTO desplazarse(RUT,latitud,longitud) VALUES	(1,-39.833551, -73.245171),
														(2,-39.833551, -73.245171),
                                                        (3,-39.833551, -73.245171),
                                                        (4,-39.833551, -73.245171),
                                                        (5,-39.833551, -73.245171);
dump Valdivia > backup-file.sql
                                                        
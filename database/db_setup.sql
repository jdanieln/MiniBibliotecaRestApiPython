CREATE TABLE Editoriales (
                             EditorialID INT PRIMARY KEY IDENTITY(1, 1),
                             Nombre NVARCHAR(100) NOT NULL,
                             Pais NVARCHAR(50)
);

CREATE TABLE Autores (
                         AutorID INT PRIMARY KEY IDENTITY(1 , 1),
                         Nombre NVARCHAR(50) NOT NULL,
                         Apellido NVARCHAR(50) NOT NULL
);


CREATE TABLE Libros(
                       LibroID INT PRIMARY KEY IDENTITY(1 , 1),
                       Titulo NVARCHAR(255) NOT NULL,
                       AnioPublicacion INT,
                       AutorID INT,
                       EditorialID INT,
                       FOREIGN KEY (AutorID) REFERENCES Autores(AutorID),
                       FOREIGN KEY (EditorialID) REFERENCES Editoriales(EditorialID)
);


SELECT
    L.Titulo,
    l.AnioPublicacion,
    A.Nombre as AutorNombre,
    A.Apellido as AutorApellido,
    E.Nombre as EditorialNombre
FROM LIBROS AS L
         JOIN Autores AS A
              ON L.AutorID = A.AutorID
         JOIN Editoriales AS E
              on e.EditorialID = l.EditorialID


    INSERT INTO Editoriales (Nombre, Pais) VALUES ('Planeta', 'España'), ('Anagrama', 'España');


INSERT INTO Autores (Nombre, Apellido) VALUES ('Gabriel', 'García Márquez'), ('Isabel', 'Allende');


INSERT INTO Libros (Titulo, AnioPublicacion, AutorID, EditorialID) VALUES ('Cien años de soledad', 1967, 1, 1), ('La casa de los espíritus', 1982, 2, 1);

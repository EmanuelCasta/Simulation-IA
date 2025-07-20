-- PostgreSQL migration script

CREATE TABLE revista (
    idRevista SERIAL PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL UNIQUE,
    Q VARCHAR(45) NOT NULL
);

CREATE TABLE articulo (
    idArticulo SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL UNIQUE,
    Fecha VARCHAR(45) NOT NULL,
    Link_Descarga VARCHAR(255) NOT NULL,
    idRevista INTEGER NOT NULL REFERENCES revista(idRevista) ON DELETE CASCADE,
    authors VARCHAR(255) NOT NULL,
    pagestart VARCHAR(45),
    pageend VARCHAR(45),
    doi VARCHAR(100),
    resumen TEXT,
    llaves TEXT,
    volume VARCHAR(45),
    issue VARCHAR(45)
);

CREATE TABLE basesdedatos (
    idBasesDeDatos SERIAL PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL UNIQUE,
    link VARCHAR(255) NOT NULL
);

CREATE TABLE operadorlogico (
    idOperadorLogico SERIAL PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL UNIQUE
);

CREATE TABLE palabracomplementaria (
    idPalabraComplementaria SERIAL PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL UNIQUE
);

CREATE TABLE logicocomplementaria (
    idLogicoComplementaria SERIAL PRIMARY KEY,
    idPalabraComplementaria INTEGER NOT NULL REFERENCES palabracomplementaria(idPalabraComplementaria) ON DELETE CASCADE,
    idOperadorLogico INTEGER NOT NULL REFERENCES operadorlogico(idOperadorLogico) ON DELETE CASCADE
);

CREATE TABLE palabraclave (
    idPalabraClave SERIAL PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL UNIQUE
);

CREATE TABLE logicoclave (
    idLogicoClave SERIAL PRIMARY KEY,
    idOperadorLogico INTEGER NOT NULL REFERENCES operadorlogico(idOperadorLogico) ON DELETE CASCADE,
    idPalabraClave INTEGER NOT NULL REFERENCES palabraclave(idPalabraClave) ON DELETE CASCADE
);

CREATE TABLE palabracaracteristica (
    idPalabraCaracteristica SERIAL PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL UNIQUE
);

CREATE TABLE logicocaracteristica (
    idLogicoCaracteristica SERIAL PRIMARY KEY,
    idOperadorLogico INTEGER NOT NULL REFERENCES operadorlogico(idOperadorLogico) ON DELETE CASCADE,
    idPalabraCaracteristica INTEGER NOT NULL REFERENCES palabracaracteristica(idPalabraCaracteristica) ON DELETE CASCADE
);

CREATE TABLE palabracondicional (
    idPalabraCondicional SERIAL PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL UNIQUE
);

CREATE TABLE logicocondicional (
    idLogicoCondicional SERIAL PRIMARY KEY,
    idOperadorLogico INTEGER NOT NULL REFERENCES operadorlogico(idOperadorLogico) ON DELETE CASCADE,
    idPalabraCondicional INTEGER NOT NULL REFERENCES palabracondicional(idPalabraCondicional) ON DELETE CASCADE

);

CREATE TABLE busqueda (
    idBusqueda SERIAL PRIMARY KEY,
    idLogicoClave INTEGER NOT NULL REFERENCES logicoclave(idLogicoClave) ON DELETE CASCADE,
    idLogicoCaracteristica INTEGER NOT NULL REFERENCES logicocaracteristica(idLogicoCaracteristica) ON DELETE CASCADE,
    idLogicoComplementaria INTEGER NOT NULL REFERENCES logicocomplementaria(idLogicoComplementaria) ON DELETE CASCADE

);

CREATE TABLE basesdatosbusqueda (
    idBasesDatosBusqueda SERIAL PRIMARY KEY,
    idBasesDeDatos INTEGER REFERENCES basesdedatos(idBasesDeDatos) ON DELETE CASCADE,
    idBusqueda INTEGER REFERENCES busqueda(idBusqueda) ON DELETE CASCADE,
    numeroArticulos INTEGER
);

CREATE TABLE busquedaarticulo (
    idBusquedaArticulo SERIAL PRIMARY KEY,
    idBusqueda INTEGER NOT NULL REFERENCES busqueda(idBusqueda) ON DELETE CASCADE,
    idArticulo INTEGER NOT NULL REFERENCES articulo(idArticulo) ON DELETE CASCADE
);

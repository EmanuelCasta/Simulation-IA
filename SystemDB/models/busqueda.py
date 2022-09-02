import __init__ 
from models.ConnectionDB import ConnectionDB

class BusquedaArticles():

    def __init__(self):
        self.db = ConnectionDB()

    def get_combination(self,id):
        process = self.db.connect()
        try: 
            process.query(f"""SELECT  idBasesDeDatos, b.idBusqueda, pclave.nombre as NombreClave,operadorClave.nombre as LogicaClave ,
                            pcara.nombre as Nombrecaracteristica,operadorCaracteristicas.nombre as LogicaCaracteristica ,
                            pcomple.nombre as NombreComplementario,operadorComplementario.nombre as LogicaComplementaria,
                            numeroArticulos 
                            FROM  basesdatosbusqueda natural inner join  busqueda as b natural inner join (
                            (logicocaracteristica natural inner join ((palabracaracteristica as pcara),(operadorlogico as operadorCaracteristicas))),
                            (logicocomplementaria natural inner join ((palabracomplementaria as pcomple),(operadorlogico as operadorComplementario))),
                            (logicoclave natural inner join ((palabraclave as pclave),(operadorlogico as operadorClave)))) where idBasesDeDatos={id} and numeroArticulos is null;""")
            return process.use_result().fetch_row(maxrows=0,how=1)
           
        except Exception:
            pass
        process.close()


    def get_palabra(self,nombreClave,operadorClave,nombreCaracteristica,operadorCaracteristica,nombreComplemento, operadorComplemetp):
        process = self.db.connect()
        try: 
            process.query(f"""SELECT bb.idBasesDatosBusqueda,idBasesDeDatos, b.idBusqueda, pclave.nombre as NombreClave,operadorClave.nombre as LogicaClave ,
                pcara.nombre as Nombrecaracteristica,operadorCaracteristicas.nombre as LogicaCaracteristica ,
                pcomple.nombre as NombreComplementario,operadorComplementario.nombre as LogicaComplementaria,
                numeroArticulos 
                FROM  basesdatosbusqueda as bb natural inner join  busqueda as b natural inner join (
                (logicocaracteristica natural inner join ((palabracaracteristica as pcara),(operadorlogico as operadorCaracteristicas))),
                (logicocomplementaria natural inner join ((palabracomplementaria as pcomple),(operadorlogico as operadorComplementario))),
                (logicoclave natural inner join ((palabraclave as pclave),(operadorlogico as operadorClave)))) 
                where pclave.nombre={nombreClave}
                and operadorClave.nombre ="{operadorClave}"
                and pcara.nombre={nombreCaracteristica}
                and operadorCaracteristicas.nombre ="{operadorCaracteristica}"
                and pcomple.nombre={nombreComplemento}
                and operadorComplementario.nombre ="{operadorComplemetp}";""")
            return process.use_result().fetch_row(maxrows=0,how=1)
           
        except Exception:
            pass
        process.close()

    def insertar_articulos(self,num,idBasesDatosBusqueda):
        process = self.db.connect()
        try: 
            process.query(f"""update basesdatosbusqueda set numeroArticulos ={num} where idBasesDatosBusqueda={idBasesDatosBusqueda};""")
            return process.use_result().fetch_row(maxrows=0,how=1)
           
        except Exception:
            pass
        process.close()




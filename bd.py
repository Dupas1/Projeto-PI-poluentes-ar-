import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"D:\instantclient_21_9")

dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XEPDB1")

connection = cx_Oracle.connect(
    user="PI2",
    password="102030",
    dsn=dsn)

print("Successfully connected to Oracle ")

cursor = connection.cursor()

# cria tabela se não criada
try:
    cursor.execute("""
        create table amostras (
        id number generated always as identity,
        mp10 number(*),mp25 number(*),o3 number(*), co number(*),no2 number(*),so2 number(*),
        primary key (id))""")
    print("Table created")
except:
    print("Table already created\n")

# altera dados
    def alteradados(id, co, so2, no2, o3, mp25, mp10):
        try:
            comand = (
                f'UPDATE amostras set co={co}, so2={so2}, no2={no2}, o3={o3}, mp25={mp25}, mp10={mp10} where id={id}')
            cursor.execute(comand)
            connection.commit()
        except Exception as err:
            print({err})

# insere dados
    def inseredados(co, so2, no2, o3, mp25, mp10):
        query = (
            f"insert into amostras(co, so2, no2, o3, mp25, mp10) values ({co}, {so2}, {no2}, {o3}, {mp25},{ mp10})")
        try:
            cursor.execute(query)
            connection.commit()
        except Exception as err:
            print({err})

# deleta dados
    def deletadados(id):
        try:
            comand = (f'DELETE from amostras where ID={id}')
            cursor.execute(comand)
            connection.commit()
            return "Sucess"
        except Exception as err:
            print({err})

# Mostra os dados
    def printdados():
        amostrasBD = []
        for i in cursor.execute('SELECT * from amostras order by id asc'):
            amostrasBD.append(i)
        return amostrasBD

# media dos dados
    def classificacao():
        cursor.execute(
            "select round(avg(MP10),2),round(avg(MP25),2),round(avg(O3),2),round(avg(CO),2),round(avg(NO2),2),round(avg(SO2),2) from AMOSTRAS")
        media = cursor.fetchone()
        return media

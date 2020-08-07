import psycopg2

isConnect = False

try:
    connect = psycopg2.connect('user=postgres password=password dbname=learnPsycopgDB host=127.0.0.1 port=5432')
    isConnect = True
except:
    print("Koneksi ke database gagal")

if isConnect:
    try: 
        cursor = connect.cursor()
        sql = "SELECT * FROM mahasiswa"
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            name = row[1]
            address = row[2]

            print("id: %d \t nama: %s \t alamat: %s" % (id, name, address))

    except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    finally:
        if connect is not None:
            connect.close()
            print("Koneksi database ditutup")

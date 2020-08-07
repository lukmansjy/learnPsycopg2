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

        sql = """CREATE TABLE IF NOT EXISTS mahasiswa(
                id serial PRIMARY KEY,
                nama VARCHAR(30) NOT NULL,
                alamat VARCHAR(30) NOT NULL
            )"""

        cursor.execute(sql)
        connect.commit()
        print("Database berhasil dibuat")

    except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    finally:
        if connect is not None:
            connect.close()
            print("Koneksi database ditutup")

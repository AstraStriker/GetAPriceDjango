class Scraper:
    import mysql.connector
    from scrapper_amazon import scrapper_amazon
    from scrapper_elitehub import scrapper_elitehub
    from scrapper_flipkart import scrapper_flipkart
    from mysql.connector import Error

    db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'admin',
        database = 'getaprice',
        options = {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }
    )

    cur = db.cursor()
    cur.execute('SELECT * FROM product1')

    products = cur.fetchall()
    
    for product in products:
        tuple = product
        id = tuple[0]
        name = tuple[1]
        amazon = tuple[2]
        elitehub = tuple[3]
        flipkart = tuple[4]
        image = tuple[5]
        aprice = tuple[6]
        eprice = tuple[7]
        fprice = tuple[8]
        


        a = scrapper_amazon.__price__(amazon)
        e = scrapper_elitehub.__price__(elitehub)
        f = scrapper_flipkart.__price__(flipkart)

        cur.execute("UPDATE product1 SET a = '{{a}}' WHERE ('id' = '{{id}}');")
        cur.execute("UPDATE product1 SET e = '{{a}}' WHERE ('id' = '{{id}}');")
        cur.execute("UPDATE product1 SET f = '{{a}}' WHERE ('id' = '{{id}}');")

        
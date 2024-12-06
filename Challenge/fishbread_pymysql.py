import pymysql
from datetime import datetime

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='990924', # 자신의 패스워드를 넣어서 실행
    db='db_test',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:
    # # 문제1: 새로운 사용자 “8ki joa”를 추가해주세요. (이름 외 정보는 임의로 정해주세요)
    # sql = "INSERT INTO users (first_name, last_name, email, password, address, contact, gender, is_active, is_staff) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    # cursor.execute(sql, ('8ki', 'joa', '8ki_joa@email.com', '123456789', 'seoul', '010-1234-5678', 'MALE', True, False))
    # connection.commit()
    
    # # 문제2: 사용자 “8ki joa”의 주소를 변경해주세요.
    # sql = "update users set address=%s where id=%s"
    # cursor.execute(sql, ('busan', 11))
    # connection.commit()
    
    # # 문제3: 1번 store에서 사용자 “8ki joa”의 주문을 생성해주세요. (팥 붕어빵 3개, 크림 붕어빵 2개, 시그니처 메뉴 5개)
    # sql = "INSERT INTO sales_records (user_id, store_id, is_refund, created_at) VALUES (%s, %s, %s, %s)"
    # cursor.execute(sql, ('11', '1', '0', datetime.now()))
    # connection.commit()
    # sql = "INSERT INTO sales_items (sales_record_id, product_id, quantity, created_at) VALUES (%s, %s, %s, %s)"
    # cursor.execute(sql, ('11', '2', '3', datetime.now()))
    # connection.commit()
    # sql = "INSERT INTO sales_items (sales_record_id, product_id, quantity, created_at) VALUES (%s, %s, %s, %s)"
    # cursor.execute(sql, ('11', '1', '2', datetime.now()))
    # connection.commit()
    # sql = "INSERT INTO sales_items (sales_record_id, product_id, quantity, created_at) VALUES (%s, %s, %s, %s)"
    # cursor.execute(sql, ('11', '10', '5', datetime.now()))
    # connection.commit()
    
    # # 문제4: order_records 테이블에 발주이력을 3건 생성해주세요. (재료는 자유롭게 정해주세요)
    # sql = "INSERT INTO order_records (employee_id, supplier_id, raw_material_id, quantity) VALUES (%s, %s, %s, %s)"
    # cursor.execute(sql, ('3', '1', '1', '10'))
    # connection.commit()
    # sql = "INSERT INTO order_records (employee_id, supplier_id, raw_material_id, quantity) VALUES (%s, %s, %s, %s)"
    # cursor.execute(sql, ('3', '1', '2', '15'))
    # connection.commit()
    # sql = "INSERT INTO order_records (employee_id, supplier_id, raw_material_id, quantity) VALUES (%s, %s, %s, %s)"
    # cursor.execute(sql, ('3', '1', '9', '20'))
    # connection.commit()
    # # change_date과 create_at은 DEFAULT가 있어서 따로 데이터를 넣지않음
    
    # # 문제5: stocks 테이블에 원재료 사용이력을 3건 추가하고, 최근 사용이력 3건을 조회해주세요.
    # sql = "INSERT INTO stocks (raw_material_id, pre_quantity, quantity, change_type, store_id) VALUES (%s, %s, %s, %s, %s)"
    # cursor.execute(sql, ('1', '100', '10', 'OUT', '1'))
    # connection.commit()
    # sql = "INSERT INTO stocks (raw_material_id, pre_quantity, quantity, change_type, store_id) VALUES (%s, %s, %s, %s, %s)"
    # cursor.execute(sql, ('2', '100', '15', 'OUT', '1'))
    # connection.commit()
    # sql = "INSERT INTO stocks (raw_material_id, pre_quantity, quantity, change_type, store_id) VALUES (%s, %s, %s, %s, %s)"
    # cursor.execute(sql, ('9', '100', '20', 'OUT', '1'))
    # connection.commit()
    # sql = "select * from stocks order by create_at desc limit 3"
    # cursor.execute(sql)
    # for i in cursor.fetchall():
    #     print(i)
    
    # 문제6: 유저 “8ki joa”가 주문한 내역을 조회해주세요. (단, 비싼 금액의 상품순으로 나열해주세요)
    sql = '''
    SELECT u.first_name, u.last_name, p.name AS product_name, p.price, si.quantity, (p.price * si.quantity) AS total_price, sr.created_at
    FROM users u
    JOIN sales_records sr ON u.id = sr.user_id
    JOIN sales_items si ON sr.id = si.sales_record_id
    JOIN products p ON si.product_id = p.id
    WHERE u.id = %s
    ORDER BY p.price DESC;
    '''
    cursor.execute(sql, (11))
    for i in cursor.fetchall():
        print(i)
        
    cursor.close()
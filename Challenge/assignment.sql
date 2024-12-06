use db_test;

-- 문제1: 이름에 s가 들어간 사용자와 y로 끝나는 사용자 확인
SELECT * FROM users where first_name like '%s%' or last_name like '%s%' or last_name like '%y';

-- 문제2: 매장 id 5번에 소속된 직원의 전화번호 확인
SELECT u.contact FROM employees e join users u on e.user_id = u.id where store_id=5;

-- 문제3: 공급처와 매장을 이름순으로 출력
SELECT * FROM suppliers ORDER BY name asc;
SELECT * FROM stores ORDER BY name asc;

-- 문제4: 스태프와 매니저로 소속된 모든 employee 수 출력
SELECT type, COUNT(*) AS count FROM employees WHERE type IN ('STAFF', 'MANAGER') GROUP BY type;

-- 문제5: MANAGER 직급을 가진 직원들의 이름과 소속 매장 이름을 출력
SELECT u.first_name, u.last_name, e.store_id FROM users u join employees e on u.id = e.user_id where e.type = 'MANAGER';

-- 문제6: 매장별로 가장 많이 팔린 상품의 이름과 판매 수량을 출력
SELECT store_name, product_name, total_quantity AS best_seller 
FROM (
    SELECT store_name, product_name, total_quantity,
           RANK() OVER (PARTITION BY store_name ORDER BY total_quantity DESC) AS sale_rank
    FROM (
        SELECT s.name AS store_name, p.name AS product_name, SUM(si.quantity) AS total_quantity 
        FROM stores s 
        JOIN sales_records sr ON s.id = sr.store_id 
        JOIN sales_items si ON sr.id = si.sales_record_id 
        JOIN products p ON si.product_id = p.id 
        GROUP BY s.name, p.name
    ) AS subquery
) AS ssubquery 
WHERE sale_rank = 1;

-- 문제7: 원재료별로 공급업체 수를 출력
SELECT rm.name AS raw_material_name, COUNT(DISTINCT orr.supplier_id) AS supplier_count
FROM raw_materials rm
JOIN order_records orr ON rm.id = orr.raw_material_id
GROUP BY rm.name;
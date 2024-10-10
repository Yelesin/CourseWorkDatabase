CREATE ROLE login LOGIN
GRANT SELECT on employee to login 
GRANT EXECUTE on FUNCTION employee_info(id integer) to login;


CREATE ROLE vet LOGIN
-- таблицы
GRANT SELECT, DELETE on clarification_to_app to vet;
GRANT SELECT on type_animal to vet;
GRANT SELECT on feed to vet;
GRANT SELECT on dynamic_growth to vet;
GRANT SELECT, UPDATE on animal to vet;
GRANT SELECT, DELETE, INSERT on application to vet;
-- представления
GRANT SELECT on info_animals_healthy to vet;
GRANT SELECT on info_animals_sick to vet;
GRANT SELECT on all_app_inspection to vet;
--функции
GRANT EXECUTE on FUNCTION animal_info(id integer) to vet;
GRANT EXECUTE on FUNCTION add_application(type_application varchar(50), animals integer[], employee_name varchar(100)) to vet;
GRANT EXECUTE on FUNCTION get_applications(type_application varchar(100)) to vet;
GRANT EXECUTE on FUNCTION inspection(employee_name varchar(100), num_application int, numAnimals int[], statusAnimals varchar[]) to vet;
GRANT EXECUTE on FUNCTION change_feed(vet varchar(100), num_application int, numAnimals int[], animalFeed varchar[]) to vet;


CREATE ROLE worker LOGIN
--таблицы
GRANT SELECT on animal to worker;
GRANT SELECT on type_animal to worker;
GRANT SELECT on feed to worker;
GRANT SELECT on dynamic_growth to worker;
--представления
GRANT SELECT ON info_animals_hungry TO worker
GRANT SELECT ON info_animals_not_hungry TO worker
--функции
GRANT EXECUTE ON FUNCTION animal_info(id integer) to worker;
GRANT EXECUTE ON FUNCTION get_weighing_history(id integer) to worker;
GRANT EXECUTE ON FUNCTION current_weight(idAnimal integer) to worker;
GRANT EXECUTE ON FUNCTION feed_animal(worker varchar(100), animals int[]) to worker;
GRANT EXECUTE ON function weight_animal(employeeID varchar(100), numAnimal int, weight int) to worker;
GRANT EXECUTE ON FUNCTION add_application(type_application varchar(50), animals integer[], employee_name varchar(100)) to worker;
GRANT EXECUTE ON FUNCTION insert_animal(workerName varchar(100), typeanimal_name varchar(20), feed_name varchar(10), gender varchar(10), age int, weight int) to worker;



CREATE ROLE administrator LOGIN
--таблицы
GRANT SELECT ON employee TO administrator;
GRANT SELECT on clarification_to_app to administrator;
--представления
GRANT SELECT ON all_applications TO administrator;
GRANT SELECT ON all_app_inspection TO administrator;
GRANT SELECT ON all_app_change_feed TO administrator;
GRANT SELECT ON all_app_write_off TO administrator;
--функции
GRANT EXECUTE ON FUNCTION rm_application(numApp int) to administrator;
GRANT EXECUTE ON FUNCTION animal_info(id integer) to administrator;
GRANT EXECUTE ON FUNCTION updateInfoEmployee(idEmployee int, loginEmployee varchar(100), passwrd varchar(100), full_name varchar(100), positionEmployee varchar(100), salaryEmployee int) to administrator;
GRANT EXECUTE ON FUNCTION update_application(num_application int, numAnimals int[]) TO administrator;


CREATE ROLE head_household LOGIN
-- таблицы
GRANT SELECT,UPDATE,DELETE ON employee TO head_household; 
--представления
GRANT SELECT ON all_app_write_off TO head_household;
GRANT SELECT ON info_animals TO head_household;
GRANT SELECT ON employees TO head_household;
--функции
GRANT EXECUTE on FUNCTION get_applications(type_application varchar(100)) to head_household;
GRANT EXECUTE ON FUNCTION animal_info(id integer) to head_household;
GRANT EXECUTE on FUNCTION employee_info(id integer) to head_household;
GRANT EXECUTE ON FUNCTION rm_employee(idEmployee integer) to head_household;
GRANT EXECUTE ON FUNCTION write_off_animals(numAnimals int[], num_application int, employee_name varchar(100)) to head_household;
GRANT EXECUTE ON function add_employee(log varchar(50), passwrd varchar(50), full_name varchar (100), posit varchar(30), salary int) to head_household;
--1) добавить животное
CREATE OR REPLACE FUNCTION insert_animal(workerName varchar(100), typeanimal_name varchar(20), feed_name varchar(10), gender varchar(10), age int, weight int) RETURNS void
AS $$
DECLARE
	number_an int;
	worker int;
	vet int;
	
	
	type_animal_int int;
	feed_int int;

	substr text;
	type_list text = '';
	feed_list text = '';
	
begin
	-- записываем список допустимых типов животных и корма в соответсвующие переменные
	-- Нужно для отображения в ошибке
	
		for substr in (select name_of_type FROM type_animal) loop
			type_list  := type_list  || substr || ' ';
		end loop;
	
		for substr  in (SELECT title FROM feed) loop
			feed_list := feed_list || substr  || ' ';
		end loop;
	
	-- Проверка каждого переданного параметра
		IF lower(workerName) IN (SELECT lower(fullname) FROM employee) THEN
			worker:= (SELECT id_employee FROM employee WHERE lower(fullname) = lower(workerName));
		ELSE
			RAISE EXCEPTION 'Не существует такого сотрудника !';
		END IF;
		IF lower(typeanimal_name) NOT IN (SELECT lower(name_of_type) FROM type_animal)
			THEN RAISE EXCEPTION 'Не найдено такого типа животного. Допустимые типы: %', type_list;
		ELSEIF lower(feed_name) NOT IN (SELECT lower(title) FROM feed)
			THEN RAISE EXCEPTION 'Неизвестный тип корма. Допустимые значения: %', feed_list;
		ELSEIF age < 0
			THEN RAISE EXCEPTION 'Возраст не может быть отрицательным !';
		ELSEIF lower(gender) NOT IN ('мужской','женский')
			THEN RAISE EXCEPTION 'Неизвестный пол животного. Допустимые значения: Мужской, Женский';
		ELSEIF weight < 0
			THEN RAISE EXCEPTION 'Вес не может быть отрицательным !';
		END IF;
		
		-- переведим в тип животного и корма в соответствующее число
		type_animal_int := (SELECT typeanimal_key FROM type_animal WHERE name_of_type = typeanimal_name);
		feed_int := (SELECT key_feed FROM feed WHERE title = feed_name);
		
	-- Выбираем случайного ветеринара
		vet := (SELECT id_employee from (select * from  employee where  position = 'Ветеринар' and status  = 'Работает') as employee
					  ORDER BY RANDOM()
					  LIMIT 1);
		
		
		RAISE NOTICE 'Worker - %', worker ;
		RAISE NOTICE 'Vet - %', vet;
		
		INSERT INTO animal(ReceiptDate, Key_Feed, TypeAnimal_key, Age, Gender) VALUES (CURRENT_DATE, feed_int, type_animal_int, age, gender) RETURNING numberanimal INTO number_an;
		INSERT INTO Dynamic_growth(NumberAnimal, Date_in, Weight, ID_employee) VALUES (number_an, CURRENT_DATE, weight, worker);
		INSERT INTO Satiety_Animal(NumberAnimal, ID_employee, Feeding_time) VALUES (number_an, worker , NOW());
		INSERT INTO Inspection_history(NumberAnimal, ID_employee, Date_inspection, Status) VALUES (number_an, vet, CURRENT_DATE, 'Здоровое');
		
		RAISE NOTICE 'Number new animal %', number_an;
END;
$$ LANGUAGE plpgsql
SECURITY DEFINER;








-- 2) добавить заявку
CREATE OR REPLACE FUNCTION add_application(type_application varchar(50), animals integer[], employee_name varchar(100)) RETURNS void
AS $$
DECLARE
	number_app int;
	employeeID int;
    appID int;
	numAnimal int := 0; -- счётчик в цикле
begin
-- проверки

	-- проверка на существование типа заявки
	IF lower(type_application) IN (SELECT lower(name_of_app) FROM application_type) THEN
		number_app := (SELECT application_type_key FROM application_type WHERE lower(name_of_app) = lower(type_application));
		--RAISE NOTICE 'number_app %', number_app; 
	ELSE
		RAISE EXCEPTION 'Не существует такого типа заявки !';
	END IF;

	-- проверка на существование сотрудника
	IF lower(employee_name) IN (SELECT lower(fullname) FROM employee) THEN
		employeeID:= (SELECT id_employee FROM employee WHERE lower(fullname) = lower(employee_name));
        --RAISE NOTICE 'employee ID = %', employeeID;
    ELSE
        RAISE EXCEPTION 'Не существует такого сотрудника !';
    END IF;
    
    -- проверка должности сотрудника
    IF number_app = 1 AND (SELECT position FROM employee WHERE id_employee = employeeID) != 'Ветеринар' THEN
        RAISE EXCEPTION 'Заявку на списание может подать только ветеринар !';
    ELSEIF number_app = 2 AND (SELECT position FROM employee WHERE id_employee = employeeID) != 'Рабочий' THEN
        RAISE EXCEPTION 'Заявку на осмотр может подать только рабочий !';
    ELSEIF number_app = 3 AND (SELECT position FROM employee WHERE id_employee = employeeID) != 'Рабочий' THEN
        RAISE EXCEPTION 'Заявку на изменение типа корма может подать только рабочий !'; 
    END IF;
    
    
    -- проверка существует(списано) ли каждое животное
	FOREACH numAnimal IN ARRAY animals LOOP
        IF  (SELECT gender FROM animal WHERE numberanimal = numAnimal) IS NULL OR (SELECT write_off FROM animal WHERE numberanimal = numAnimal) IS NOT NULL THEN
            RAISE EXCEPTION 'Животного с номером % не существует или оно списано !', numAnimal;
        END IF;
	END LOOP;
    
    -- создаём заявку
    INSERT INTO Application(DateOfApp, ID_employee, Application_type_key) VALUES (CURRENT_DATE, employeeID, number_app) RETURNING keyapplication INTO appID;
    numAnimal := 0;
    FOREACH numAnimal IN ARRAY animals LOOP
        INSERT INTO clarification_to_app(KeyApplication, numberanimal) VALUES (appID, numAnimal);
	END LOOP;

END;
$$ language plpgsql
SECURITY DEFINER;




--3) Функция добавления нового сотрудника
create or replace function add_employee(log varchar(50), passwrd varchar(50), full_name varchar (100), posit varchar(30), salary int)
returns void
as $$
declare 
	employee_list text = '';
	substr text;
	number_employee int;
begin 
	for substr  in (select distinct position from employee)
	loop
		employee_list := employee_list || substr || '; ';
	end loop;

	if log in (select login from employee)
		then raise exception 'Такой логин уже существует !';
	elseif lower(posit) not in (select distinct lower(position) from employee)
		then raise  exception 'Не существует такой должности. Доступные варианты: %', employee_list;
	elseif salary <= 0
		then raise  exception  'Зарплата не может быть меншьше или равна 0 !';
	end if;
	
	
	insert  into employee(login, password, fullname, startdate, position, status, salary) values (log, passwrd, full_name, CURRENT_DATE, posit, 'Работает', salary) returning id_employee into number_employee ;
	raise notice 'ID new employee - %', number_employee;
end;
$$ language plpgsql
SECURITY DEFINER;



-- 4) Функция кормления
create or replace function feed_animal(worker varchar(100), animals int[])
returns void
as $$
declare 
	animalID int = 0;
	workerID int = 0;
begin 
	IF lower(worker) IN (SELECT lower(fullname) FROM employee WHERE status = 'Работает') AND (SELECT position FROM employee WHERE lower(fullname) = lower(worker)) = 'Рабочий' THEN
			workerID:= (SELECT id_employee FROM employee WHERE lower(fullname) = lower(worker));
    	ELSE
        	RAISE EXCEPTION 'Не существует такого действующего рабочего !';
    	END IF;

    -- проверка существует ли каждое животное
	FOREACH animalID IN ARRAY animals LOOP
        IF  (SELECT gender FROM animal WHERE numberanimal = animalID) IS NULL THEN
            RAISE EXCEPTION 'Животного с номером % не существует !', animalID;
        END IF;
	END LOOP;

	FOREACH animalID IN ARRAY animals LOOP
        INSERT INTO Satiety_Animal(NumberAnimal, ID_employee, Feeding_time) VALUES (animalID, workerID , NOW());
	END LOOP;
end;
$$ language plpgsql
SECURITY DEFINER;




--5) функция взвешивания
create or replace function weight_animal(employeeID varchar(100), numAnimal int, weight int)
returns void
as $$
declare 
	workerID int;
begin 
    IF lower(employeeID) IN (SELECT lower(fullname) FROM employee WHERE status = 'Работает') AND (SELECT position FROM employee WHERE lower(fullname) = lower(employeeID)) = 'Рабочий' THEN
			workerID:= (SELECT id_employee FROM employee WHERE lower(fullname) = lower(employeeID));
    ELSE
        RAISE EXCEPTION 'Не существует такого действующего рабочего !';
    END IF;
    
    IF weight <= 0 THEN
         RAISE EXCEPTION 'Вес не может быть меньше 0 !';
    END IF;
    
    IF  (SELECT gender FROM animal WHERE numberanimal = numAnimal) IS NULL OR (SELECT write_off FROM animal WHERE numberanimal = numAnimal) IS NOT NULL THEN
        RAISE EXCEPTION 'Животного с номером % не существует или оно списано !', numAnimal;
    ELSE
        INSERT INTO Dynamic_growth(NumberAnimal, Date_in, Weight, ID_employee) VALUES (numAnimal, CURRENT_DATE, weight, workerID);
    END IF;
end;
$$ language plpgsql
SECURITY DEFINER;





-- 6) удаление заявки
create or replace function rm_application(numApp int)
returns void
as $$
declare 
    appID int;
begin 
    IF (select id_employee from application where keyapplication = numApp) IS NOT NULL THEN
        DELETE FROM clarification_to_app WHERE keyapplication = numApp;
        DELETE FROM application WHERE keyapplication = numApp;
    ELSE
        RAISE EXCEPTION 'Неверный номер заявки !';
    END IF;
end;
$$ language plpgsql
SECURITY DEFINER;





--7) информация о животном по номеру
CREATE OR REPLACE FUNCTION animal_info(id integer)
RETURNS table("Номер" int, "Тип" varchar(100), "Пол" varchar(100), "Возраст" int, "Корм" varchar(100))
AS $$
begin
 IF  (SELECT gender FROM animal WHERE numberanimal = id) IS NULL OR (SELECT write_off FROM animal WHERE numberanimal = id) IS NOT NULL THEN
        RAISE EXCEPTION 'Животного с номером % не существует или оно списано !', id;
 END IF;

	RETURN QUERY SELECT numberanimal, name_of_type, gender, age, title
				 from animal
			     JOIN type_animal ON animal.typeanimal_key = type_animal.typeanimal_key
				 JOIN feed ON animal.key_feed = feed.key_feed
                 where numberanimal = id
				 order by numberanimal;
                 
end;
$$ LANGUAGE plpgsql
SECURITY DEFINER;




-- 8) заявка по типу
CREATE OR REPLACE FUNCTION get_applications(type_application varchar(100))
RETURNS table(application varchar(100), numApplication int)
AS $$
DECLARE
	number_app int;
begin
 -- проверка на существование типа заявки
	IF lower(type_application) IN (SELECT lower(name_of_app) FROM application_type) THEN
		number_app := (SELECT application_type_key FROM application_type WHERE lower(name_of_app) = lower(type_application));
		--RAISE NOTICE 'number_app %', number_app; 
	ELSE
		RAISE EXCEPTION 'Не существует такого типа заявки !';
	END IF;
    

	RETURN QUERY select name_of_app, keyapplication
				FROM application
				JOIN application_type ON application.application_type_key = application_type.application_type_key
                WHERE application.application_type_key = number_app;
                 
end;
$$ LANGUAGE plpgsql
SECURITY DEFINER;




--t1) хеширование пароля
CREATE OR REPLACE FUNCTION hash_password()
RETURNS trigger AS
$$
    BEGIN
        IF(TG_TABLE_NAME = 'employee')
        THEN
            IF (TG_OP = 'INSERT' OR NEW.password NOT LIKE OLD.password)
                THEN
                    NEW.password = encode(digest(NEW.password, 'sha256'), 'hex');
                END IF;
            END IF;
    RETURN NEW;
    END;
$$
LANGUAGE 'plpgsql';




-- 9) информация про сотрудника

CREATE OR REPLACE FUNCTION employee_info(id integer)
RETURNS table(name varchar(100), "Зарплата" int, "Начало работы" date, "Должность" varchar(100), "заявки на осмотр" bigint, "заявки на списание" bigint, "количество осмотров" bigint)
AS $$
BEGIN
		
		IF id NOT IN (SELECT id_employee FROM employee)
		THEN RAISE EXCEPTION 'not found!'; 
		END IF;
		RETURN QUERY SELECT  employee.fullname, 
				employee.salary, 
				employee.startdate, 
				employee.position,

				(SELECT COUNT(*) FROM application WHERE application.id_employee = id
				 AND dateofapp > CURRENT_DATE - interval'1 year' AND application_type_key = 2) as "заявки на осмотр",

				(SELECT COUNT(*) FROM application WHERE application.id_employee = id
				 AND dateofapp > CURRENT_DATE - interval'1 year' AND application_type_key = 1) as "заявки на списание",

				(SELECT COUNT(*) FROM inspection_history WHERE inspection_history.id_employee = id) as "количество осмотров"
		FROM employee
		WHERE id_employee = id;
END;
$$ LANGUAGE plpgsql
SECURITY DEFINER;




-- 10) возвращает динамику роста животного

CREATE OR REPLACE FUNCTION get_weighing_history(id integer)
RETURNS table(date_in date, weight integer)
AS $$
BEGIN
 IF  id NOT IN (SELECT numberanimal FROM animal) THEN
        RAISE EXCEPTION 'Животного с номером % не существует !', id;
 END IF;
 	RETURN QUERY SELECT dynamic_growth.date_in, dynamic_growth.weight FROM dynamic_growth
				WHERE numberanimal = id;
END;
$$ LANGUAGE plpgsql
SECURITY DEFINER;








-- 11) осмотр
CREATE OR REPLACE FUNCTION inspection(employee_name varchar(100), num_application int, numAnimals int[], feedForAnimals varchar[])
RETURNS void
AS $$
DECLARE
	write_off_animals int[];
	index_write_off int := 0;
	employeeID int;
BEGIN
    -- проверка на существование сотрудника
	IF lower(employee_name) IN (SELECT lower(fullname) FROM employee) THEN
		employeeID:= (SELECT id_employee FROM employee WHERE lower(fullname) = lower(employee_name));
    ELSE
        RAISE EXCEPTION 'Не существует такого сотрудника !';
    END IF;
        
    -- проверка, существует ли такая заявка
    IF num_application NOT IN (SELECT keyapplication FROM all_app_inspection) THEN
        RAISE EXCEPTION 'Не существует такой заявки на осмотр !';
    END IF;
	
	-- проверка, совпадает ли длина массивов
	IF array_length(numAnimals, 1) != array_length(statusAnimals,1) THEN
		RAISE EXCEPTION 'Не совпадает количество животных и их кормов !';
	END IF;
	
	-- совпадает ли количество животных в заявке с количеством животных поступающих в функцию
	IF array_length(numAnimals, 1) != (SELECT COUNT(numberanimal) FROM all_app_inspection WHERE keyapplication = num_application) THEN
		RAISE EXCEPTION 'Не совпадает количество животных в заявке !';
	END IF;
	
	--проверка каждого животного на нахождение в заявке
	FOR i IN 0..array_length(numAnimals, 1) LOOP
		IF numAnimals[i] NOT IN (SELECT numberanimal FROM all_app_inspection WHERE keyapplication=num_application) THEN
        	RAISE EXCEPTION 'Животное номер % не указано в заявке !', i;
    	END IF;
	END LOOP;
	
	-- правильно ли указаны состояния животных
	FOR i IN 0..array_length(statusAnimals, 1) LOOP
		IF statusAnimals[i] NOT IN ('Больное', 'Здоровое', 'В заявку на списание') THEN
        RAISE EXCEPTION 'Неправильно указано состояние одного из животных: %', statusAnimals[i];
    	END IF;
	END LOOP;
	
	-- заполняем массив списанных животных
	FOR i IN 1..array_length(statusAnimals,1) LOOP
		IF statusAnimals[i] IN ('В заявку на списание') THEN
			write_off_animals[index_write_off] = numAnimals[i];
			index_write_off := index_write_off + 1;
		END IF;
	END LOOP;
	
	--если массив списанных животных не пустой, составляем заявку на списание
	IF array_length(write_off_animals,1) IS NOT NULL THEN
		PERFORM add_application('Заявка на списание', write_off_animals, employee_name);
	END IF;
	
	-- проверяем наличие не списанных животных и обновляем их состояния
	FOR i IN 0..array_length(numAnimals,1) LOOP
		IF statusAnimals[i] NOT IN ('В заявку на списание') THEN
			INSERT INTO Inspection_history(NumberAnimal, ID_employee, Date_inspection, Status) VALUES (numAnimals[i], employeeID, CURRENT_DATE, statusAnimals[i]);
		END IF;
	END LOOP;
	
	--удаляем заявку
	PERFORM rm_application(num_application);
	
END;
$$ LANGUAGE plpgsql
SECURITY DEFINER





--12) изменение корма
CREATE OR REPLACE FUNCTION change_feed(vet varchar(100), num_application int, numAnimals int[], animalFeed varchar[])
RETURNS void
AS $$
DECLARE
	employeeID int;
	feedID int[];
BEGIN
    -- проверка на существование сотрудника
	IF lower(vet) IN (SELECT lower(fullname) FROM employee WHERE status = 'Работает') AND (SELECT position FROM employee WHERE lower(fullname) = lower(vet)) = 'Ветеринар' THEN
        employeeID := (SELECT id_employee FROM employee WHERE lower(fullname) = lower(vet));
    ELSE
        RAISE EXCEPTION 'Не существует такого действующего ветеринара !';
    END IF;
        
    -- проверка, существует ли такая заявка
    IF num_application NOT IN (SELECT keyapplication FROM all_app_change_feed) THEN
        RAISE EXCEPTION 'Не существует такой заявки на изменение типа корма !';
    END IF;
	
	-- проверка, совпадает ли длина массивов
	IF array_length(numAnimals, 1) != array_length(animalFeed,1) THEN
		RAISE EXCEPTION 'Не совпадает количество животных и их кормов !';
	END IF;
	
	-- совпадает ли количество животных в заявке с количеством животных поступающих в функцию
	IF array_length(numAnimals, 1) != (SELECT COUNT(numberanimal) FROM all_app_change_feed WHERE keyapplication = num_application) THEN
		RAISE EXCEPTION 'Не совпадает количество животных в заявке !';
	END IF;
	
	--проверка каждого животного на нахождение в заявке
	FOR i IN 0..array_length(numAnimals, 1) LOOP
		IF numAnimals[i] NOT IN (SELECT numberanimal FROM all_app_change_feed WHERE keyapplication=num_application) THEN
        	RAISE EXCEPTION 'Животное номер % не указано в заявке !',  numAnimals[i];
    	END IF;
	END LOOP;
	
	-- правильно ли указаны корма животных и запоминаем ключи
	FOR i IN 1..array_length(animalFeed, 1) LOOP
		IF animalFeed[i] NOT IN (SELECT title FROM feed) THEN
        	RAISE EXCEPTION 'Неправильно указан корм одного из животных: %', animalFeed[i];
    	END IF;
    	feedID[i] = (SELECT key_feed FROM feed WHERE title = animalFeed[i]);
	END LOOP;
	
	RAISE INFO 'ID`s = %', feedID;

	
	-- обновляем корма
	FOR i IN 1..array_length(feedID,1) LOOP
		UPDATE animal
		SET key_feed = feedID[i]
		WHERE numberanimal = numAnimals[i];
	END LOOP;
	
	--удаляем заявку
	PERFORM rm_application(num_application);
END;
$$ language plpgsql
SECURITY DEFINER;




--13) Возращает текущий вес животного
CREATE OR REPLACE FUNCTION current_weight(idAnimal int)
RETURNS int
AS $$
BEGIN
 IF idAnimal NOT IN (SELECT numberanimal FROM animal) OR idAnimal IN (SELECT numberanimal FROM animal WHERE write_off IS NOT NULL) THEN
        RAISE EXCEPTION 'Животного с номером % не существует или оно списано!', idAnimal;
 END IF;
 	RETURN (SELECT weight FROM get_weighing_history(idAnimal) WHERE date_in IN (SELECT MAX(date_in) FROM get_weighing_history(idAnimal)));
END;
$$ LANGUAGE plpgsql
SECURITY DEFINER;



--14) Обновить зарплату
CREATE OR REPLACE FUNCTION updateSalary(idEmployee int, salaryEmployee int)
RETURNS void
AS $$
BEGIN
	 IF idEmployee NOT IN (SELECT id_employee FROM employee) OR (SELECT status FROM employee WHERE id_employee = idEmployee) = 'Не работает' THEN
			RAISE EXCEPTION 'Сотрудника с номером % не существует или он не работает!', idEmployee;
	 END IF;
 	IF salaryEmployee == 0 THEN
		RAISE EXCEPTION 'Зарплата не может быть равно 0 !';
	END IF;
	
	UPDATE employee SET salary = salaryEmployee WHERE id_employee = idEmployee; 
END;
$$ LANGUAGE plpgsql
SECURITY DEFINER;



--15) Обновить данные сотрудника
CREATE OR REPLACE FUNCTION updateInfoEmployee(idEmployee int, loginEmployee varchar(100), passwrd varchar(100), full_name varchar(100), positionEmployee varchar(100), salaryEmployee int)
RETURNS void
AS $$
BEGIN
	IF idEmployee NOT IN (SELECT id_employee FROM employee) OR (SELECT status FROM employee WHERE id_employee = idEmployee) = 'Не работает' THEN
		RAISE EXCEPTION 'Сотрудника с номером % не существует или он не работает!', idEmployee;
	 END IF;

	 IF loginEmployee NOT IN (SELECT login FROM employee WHERE id_employee = idEmployee) THEN
	 	IF loginEmployee IN (SELECT login FROM employee) THEN
	 		RAISE EXCEPTION 'Такой логин уже существует у другого сотрудника!';
	 	END IF;
	 END IF;

	 IF salaryEmployee <= 0 THEN
	 	RAISE EXCEPTION 'Зарплата не может быть меншьше или равна нулю !';
	 END IF;

	 IF positionEmployee NOT IN ('Ветеринар', 'Рабочий', 'Администратор', 'Заведующий хозяйством') THEN
	 	RAISE EXCEPTION 'Не существует такой должности !';
	 END IF;

	 UPDATE employee SET
	 	login = loginEmployee,
	 	password = passwrd,
	 	fullname = full_name,
	 	salary = salaryEmployee
	 WHERE id_employee = idEmployee;

END;
$$ LANGUAGE plpgsql
SECURITY DEFINER;



--16) удаление сотрудника
CREATE OR REPLACE FUNCTION rm_employee(idEmployee int)
RETURNS void
AS $$
DECLARE
	positionEmployee varchar(100);
BEGIN
	IF idEmployee NOT IN (SELECT id_employee FROM employee) OR (SELECT status FROM employee WHERE id_employee = idEmployee) = 'Не работает' THEN
		RAISE EXCEPTION 'Сотрудника с номером % не существует или он не работает!', idEmployee;
	 END IF;
	 
	 positionEmployee := (SELECT position FROM employee WHERE id_employee = idEmployee);
	 
	 IF (SELECT COUNT(status) FROM employee WHERE position = positionEmployee AND status = 'Работает') <= 1 THEN
	 	RAISE EXCEPTION 'Невозможно уволить единственного сотрудника на должности %', positionEmployee;
	 END IF;

	 UPDATE employee SET status = 'Не работает' WHERE id_employee = idEmployee;

END;
$$ LANGUAGE plpgsql
SECURITY DEFINER;


--17) Обновление заявки
CREATE OR REPLACE FUNCTION update_application(num_application int, numAnimals int[])
RETURNS void
AS $$
BEGIN
	-- проверка, существует ли такая заявка
    IF num_application NOT IN (SELECT keyapplication FROM all_applications) THEN
        RAISE EXCEPTION 'Не существует такой заявки !';
    END IF;

    -- проверка каждого животного на существование
    FOR i IN 0..array_length(numAnimals, 1) LOOP
		IF numAnimals[i] IN (SELECT номер FROM info_animals_writeoff) THEN
        	RAISE EXCEPTION 'Животное номер % не существует или списано !', numAnimals[i];
    	END IF;
	END LOOP;

	-- удаляем всех животных
	DELETE FROM clarification_to_app WHERE keyapplication = num_application;

	-- добавляем тех, которые переданы в функцию
	FOR i IN 0..array_length(numAnimals, 1) LOOP
		INSERT INTO clarification_to_app(KeyApplication, numberanimal) VALUES (num_application, numAnimals[i]);
	END LOOP;

END;
$$ LANGUAGE plpgsql
SECURITY DEFINER;



--19) функция списания животных
CREATE OR REPLACE FUNCTION write_off_animals(numAnimals int[], num_application int, employee_name varchar(100))
RETURNS void
AS $$
DECLARE
	employeeID int;
BEGIN

	-- проверка на существование сотрудника
	IF lower(employee_name) IN (SELECT lower(fullname) FROM employee) THEN
		employeeID:= (SELECT id_employee FROM employee WHERE lower(fullname) = lower(employee_name));
    ELSE
        RAISE EXCEPTION 'Не существует такого сотрудника !';
    END IF;
	
	-- проверка, существует ли такая заявка
    IF num_application NOT IN (SELECT keyapplication FROM all_app_write_off) THEN
        RAISE EXCEPTION 'Не существует такой заявки на списание !';
    END IF;
	
	-- совпадает ли количество животных в заявке с количеством животных поступающих в функцию
	IF array_length(numAnimals, 1) != (SELECT COUNT(numberanimal) FROM all_app_write_off WHERE keyapplication = num_application) THEN
		RAISE EXCEPTION 'Не совпадает количество животных в заявке !';
	END IF;
	
	--проверка каждого животного на нахождение в заявке
	FOR i IN 0..array_length(numAnimals, 1) LOOP
		IF numAnimals[i] NOT IN (SELECT numberanimal FROM all_app_write_off WHERE keyapplication=num_application) THEN
        	RAISE EXCEPTION 'Животное номер % не указано в заявке !', i;
    	END IF;
	END LOOP;
	
	-- обновляем состояния животных
	FOR i IN 1..array_length(numAnimals, 1) LOOP
		UPDATE animal SET write_off = CURRENT_DATE WHERE numberanimal = numAnimals[i];
		INSERT INTO Inspection_history(NumberAnimal, ID_employee, Date_inspection, Status) VALUES (numAnimals[i], employeeID, CURRENT_DATE, 'Списанное');
	END LOOP;
	
	--удаляем заявку
	PERFORM rm_application(num_application);
	
END;
$$ LANGUAGE plpgsql
SECURITY DEFINER;





-- не списанные животные
CREATE VIEW info_animals_not_writeOff AS
    SELECT DISTINCT animal.numberanimal AS номер, name_of_type AS тип_животного, date_inspection, title AS тип_корма, status, age, gender
    FROM animal
        JOIN type_animal ON animal.typeanimal_key = type_animal.typeanimal_key
        JOIN feed ON animal.key_feed = feed.key_feed
        JOIN inspection_history ON animal.numberanimal = inspection_history.numberanimal 
    WHERE status != 'Списанное' and date_inspection IN (select max(date_inspection) from inspection_history where inspection_history.numberanimal=animal.numberanimal)
    ORDER BY animal.numberanimal;




-- списанные
CREATE VIEW info_animals_writeOff AS
    SELECT DISTINCT animal.numberanimal AS номер, name_of_type AS тип_животного, date_inspection, title AS тип_корма, status, age, gender
    FROM animal
        JOIN type_animal ON animal.typeanimal_key = type_animal.typeanimal_key
        JOIN feed ON animal.key_feed = feed.key_feed
        JOIN inspection_history ON animal.numberanimal = inspection_history.numberanimal 
    WHERE status = 'Списанное' and date_inspection IN (select max(date_inspection) from inspection_history where inspection_history.numberanimal=animal.numberanimal)
    ORDER BY animal.numberanimal;




-- выборка голодных животных
CREATE OR REPLACE VIEW info_animals_hungry AS
	SELECT DISTINCT animal.numberanimal AS номер, name_of_type AS тип_животного, title AS тип_корма, age, gender
		FROM animal
			JOIN type_animal ON animal.typeanimal_key = type_animal.typeanimal_key
			JOIN feed ON animal.key_feed = feed.key_feed
			JOIN satiety_animal ON animal.numberanimal = satiety_animal.numberanimal 
		WHERE feeding_time < CURRENT_DATE - interval'1 day' AND animal.write_off IS NULL
		ORDER BY animal.numberanimal;




-- выборка сытых животных
CREATE OR REPLACE VIEW info_animals_not_hungry AS
    SELECT DISTINCT animal.numberanimal AS номер, name_of_type AS тип_животного, title AS тип_корма, age, gender
    FROM animal
        JOIN type_animal ON animal.typeanimal_key = type_animal.typeanimal_key
        JOIN feed ON animal.key_feed = feed.key_feed
        JOIN satiety_animal ON animal.numberanimal = satiety_animal.numberanimal 
    WHERE feeding_time > CURRENT_DATE - interval'1 day' AND animal.write_off IS NULL
    ORDER BY animal.numberanimal;



-- выборка больных животных
CREATE VIEW info_animals_sick AS
    SELECT DISTINCT animal.numberanimal AS номер, name_of_type AS тип_животного, date_inspection, title AS тип_корма, status, age, O
    FROM animal
        JOIN type_animal ON animal.typeanimal_key = type_animal.typeanimal_key
        JOIN feed ON animal.key_feed = feed.key_feed
        JOIN inspection_history ON animal.numberanimal = inspection_history.numberanimal 
    WHERE status = 'Больное' and date_inspection IN (select max(date_inspection) from inspection_history where inspection_history.numberanimal=animal.numberanimal)
    ORDER BY animal.numberanimal;



    -- выборка здоровых животных
    CREATE VIEW info_animals_healthy AS
    SELECT DISTINCT animal.numberanimal AS номер, name_of_type AS тип_животного, date_inspection, title AS тип_корма, status, age, gender
    FROM animal
        JOIN type_animal ON animal.typeanimal_key = type_animal.typeanimal_key
        JOIN feed ON animal.key_feed = feed.key_feed
        JOIN inspection_history ON animal.numberanimal = inspection_history.numberanimal 
    WHERE status = 'Здоровое' and date_inspection IN (select max(date_inspection) from inspection_history where inspection_history.numberanimal=animal.numberanimal)
    ORDER BY animal.numberanimal;




-- все животные
    CREATE VIEW info_animals AS
SELECT numberanimal, name_of_type, title, receiptdate, age, gender, write_off
from animal
JOIN type_animal ON animal.typeanimal_key = type_animal.typeanimal_key
JOIN feed ON animal.key_feed = feed.key_feed
order by numberanimal;


--заявки на осмотр
CREATE OR REPLACE VIEW all_app_inspection AS
SELECT application.keyapplication, clarification_to_app.numberanimal, (SELECT status FROM inspection_history
																	WHERE numberanimal = clarification_to_app.numberanimal AND date_inspection IN 
																	(SELECT MAX(date_inspection) FROM inspection_history 
												   					WHERE numberanimal = clarification_to_app.numberanimal GROUP BY numberanimal) ) AS status
FROM application
     JOIN application_type ON application.application_type_key = application_type.application_type_key
     JOIN clarification_to_app ON application.keyapplication = clarification_to_app.keyapplication
WHERE application_type.name_of_app::text = 'Заявка на осмотр'::text
ORDER BY application_type.name_of_app;




-- заявки на изменение типа корма
CREATE OR REPLACE VIEW all_app_change_feed AS
	SELECT application.keyapplication, numberanimal, name_of_app FROM application
	JOIN application_type ON application.application_type_key = application_type.application_type_key
	JOIN clarification_to_app ON application.keyapplication = clarification_to_app.keyapplication
	WHERE name_of_app = 'Заявка на изменение типа корма'



-- заявки на списание
CREATE OR REPLACE VIEW all_app_write_off AS
	SELECT application.keyapplication, numberanimal, name_of_app FROM application
	JOIN application_type ON application.application_type_key = application_type.application_type_key
	JOIN clarification_to_app ON application.keyapplication = clarification_to_app.keyapplication
	WHERE name_of_app = 'Заявка на списание'
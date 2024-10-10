/* 1 Получить полную информацию о животных двух различных типов,
прибывших за последние полгода
(даты должны определяться автоматически, в зависимости от момента выполнения запроса). */

SELECT numberanimal AS Номер, animal.typeanimal_key AS Ключ_типа_животного, name_of_type AS Тип , gender AS Пол, age AS Возраст, title AS Тип_корма, receiptdate AS Дата_прибытия
FROM animal
LEFT OUTER JOIN type_animal ON animal.typeanimal_key = type_animal.typeanimal_key
	LEFT OUTER JOIN feed ON animal.key_feed = feed.key_feed
WHERE animal.receiptdate > (CURRENT_DATE - interval '6 month') AND (animal.typeanimal_key = 1 OR animal.typeanimal_key = 2)
ORDER BY receiptdate DESC;






/*2 Получить список голодных животных (номер, тип животного, статус, тип корма) на текущий момент. */

SELECT DISTINCT animal.numberanimal AS номер, name_of_type AS тип_животного, title AS тип_корма
FROM animal
	JOIN type_animal ON animal.typeanimal_key = type_animal.typeanimal_key
	JOIN feed ON animal.key_feed = feed.key_feed
	JOIN satiety_animal ON animal.numberanimal = satiety_animal.numberanimal 
WHERE feeding_time < CURRENT_DATE - interval'1 day'
ORDER BY animal.numberanimal



/*3 Получить информацию (номер, тип животного) о 5 самых старых больных животных. */

SELECT animal.numberanimal AS номер, name_of_type AS тип_животного, status AS статус, age AS возраст
FROM animal
LEFT OUTER JOIN type_animal ON animal.typeanimal_key = type_animal.typeanimal_key
		LEFT OUTER JOIN inspection_history ON animal.numberanimal = inspection_history.numberanimal
	
WHERE status = 'Больное' AND date_inspection IN (SELECT MAX(date_inspection)				
												FROM inspection_history
												GROUP BY numberanimal)
ORDER BY age DESC limit 5




/* 4 Получить максимальный зафиксированный вес каждого из типов животных. */
SELECT  name_of_type, MAX(weight)
FROM type_animal
LEFT OUTER JOIN animal ON animal.typeanimal_key = type_animal.typeanimal_key
	LEFT OUTER JOIN dynamic_growth ON animal.numberanimal = dynamic_growth.numberanimal
GROUP BY name_of_type


/*5 Подсчитать количество животных каждого типа, списанных за последний месяц.*/

SELECT  name_of_type, COUNT(numberanimal)
FROM animal
LEFT OUTER JOIN type_animal ON animal.typeanimal_key = type_animal.typeanimal_key
WHERE write_off IS NOT NULL AND write_off > CURRENT_DATE - interval '12 month'
GROUP BY name_of_type





/* 6 Получить прирост веса каждого из животных (разницу между весом в день поступления и весом при последнем взвешивании). */

SELECT numberanimal, name_of_type,
	(SELECT weight FROM dynamic_growth AS dg  WHERE date_in = (SELECT MAX(date_in) FROM dynamic_growth where dynamic_growth.numberanimal = dg.numberanimal) 
											AND dg.numberanimal = main_animal.numberanimal
	) - 
	
	(SELECT weight FROM dynamic_growth AS dg  WHERE date_in = (SELECT MIN(date_in) FROM dynamic_growth WHERE dynamic_growth.numberanimal = dg.numberanimal) 
											AND dg.numberanimal = main_animal.numberanimal
	) AS "Прирост"
	   
FROM animal as main_animal
	LEFT OUTER JOIN type_animal ON main_animal.typeanimal_key = type_animal.typeanimal_key
WHERE write_off IS NULL
 


/* 7. Для каждой заявки на списание животных, полученной за текущий день, вывести полную информацию о животных, подлежащих списанию. */
SELECT animal.numberanimal, name_of_type, receiptdate, age, gender, title
FROM clarification_to_app
LEFT OUTER JOIN application ON clarification_to_app.keyapplication = application.keyapplication
LEFT OUTER JOIN animal ON clarification_to_app.numberanimal = animal.numberanimal
LEFT OUTER JOIN feed ON animal.key_feed = feed.key_feed
LEFT OUTER JOIN type_animal ON animal.typeanimal_key = type_animal.typeanimal_key
WHERE dateofapp = '2021-12-15 09:45:00'

/*8. Для каждого типа животных, к которому относится более 20 животных, определить их средний возраст при поступлении.*/
SELECT AVG(age) FROM animal
GROUP BY typeanimal_key
HAVING COUNT(typeanimal_key) > 1


/* 9. Получить информацию о сотрудниках, работающих на должности рабочего и получающих одинаковую зарплату, находящуюся в заданном диапазоне значений. */
SELECT * FROM employee WHERE salary in(
	SELECT salary
	FROM employee
	WHERE position = 'Рабочий' AND salary BETWEEN 10000 AND 11000
	GROUP BY salary
	HAVING COUNT(*) > 1 AND salary IS NOT NULL
);


/* 9. Получить информацию о сотрудниках, работающих на должности рабочего и получающих одинаковую зарплату, находящуюся в заданном диапазоне значений. */

SELECT first.id_employee, first.login, first.password, first.fullname, first.salary FROM 
employee first, employee second
WHERE first.salary BETWEEN 10000 AND 11000 AND first.position = 'Рабочий' AND first.id_employee != second.id_employee AND first.salary = second.salary



/* 10.  Подсчитать количество заявок на осмотр животных указанного типа, поступивших за последние 3 дня. */

SELECT COUNT(*)
FROM Clarification_to_app 
LEFT OUTER JOIN animal ON Clarification_to_app.numberanimal = animal.numberanimal
LEFT OUTER JOIN type_animal ON animal.typeanimal_key = type_animal.typeanimal_key
LEFT OUTER JOIN application ON application.keyapplication = Clarification_to_app.keyapplication
WHERE application_type_key = 2 AND name_of_type = 'Кролик' AND dateofapp > CURRENT_DATE - interval '2 month'





/* 4.1 Составить представление, с помощью которого можно отобразить номер каждого животного, его тип, вес (при последнем взвешивании), 
максимальный вес среди всех животных, относящихся к тому же типу и количество животных этого типа (запрос необходимо выполнить с применением аналитических функций). */ 

CREATE VIEW info_animals AS

SELECT DISTINCT main_animal.numberanimal, name_of_type, 
	MAX(weight) OVER (PARTITION BY main_animal.numberanimal) AS "Вес животного",
	MAX(weight) OVER (PARTITION BY name_of_type) AS "Максимальный вес типа",
	count AS "Кол-во животных"
FROM animal as main_animal
JOIN type_animal ON main_animal.typeanimal_key = type_animal.typeanimal_key
LEFT OUTER JOIN dynamic_growth ON main_animal.numberanimal = dynamic_growth.numberanimal
JOIN (SELECT typeanimal_key, COUNT(*) FROM animal WHERE write_off IS NULL GROUP BY typeanimal_key) AS PID ON main_animal.typeanimal_key = PID.typeanimal_key
WHERE write_off IS NULL
ORDER BY numberanimal




  /*4.2 Для каждого рабочего, который работает на фирме в течение 5 лет, подсчитать среднее количество кормлений в день за последнюю неделю. */
	
SELECT id_employee, ROUND(AVG(PID.count), 2) as "Среднее кол-во кормлений"
	FROM 
	(SELECT satiety_animal.id_employee, COUNT(*), feeding_time, startdate
	FROM satiety_animal JOIN employee ON employee.id_employee = satiety_animal.id_employee
	WHERE feeding_time > CURRENT_DATE - interval'7 days'
	GROUP BY satiety_animal.id_employee, feeding_time, startdate) as PID
WHERE startdate > CURRENT_DATE - interval'5 year'
GROUP BY id_employee
ORDER BY id_employee

  


/* 4.3 Увеличить на 20% зарплату сотруднику (или сотрудникам, если таковых несколько), который работает на фирме дольше всех.*/
UPDATE employee
SET salary = salary * 1.2
WHERE startdate = (SELECT MIN(startdate) FROM employee WHERE status = 'Работает')










 /* 5.1 Составить триггер, который запрещает добавлять запись о кормлении для списанных животных. */

CREATE FUNCTION satiety_func() 
RETURNS TRIGGER 
AS $$
BEGIN
        IF (SELECT write_off FROM animal WHERE animal.numberanimal = NEW.numberanimal) IS NOT NULL THEN
            RAISE EXCEPTION 'Животное не может быть списано !';
        END IF;
        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER satiety_trg 
BEFORE INSERT ON satiety_animal
FOR EACH ROW 
EXECUTE PROCEDURE satiety_func();




/* 5.2 Составить хранимую процедуру для добавления в БД информации о прибывшем животном (с указанием его веса). Все необходимые данные передавать в качестве параметров процедуры.*/

CREATE OR REPLACE FUNCTION insert_animal(typeanimal_name varchar(20), feed_name varchar(10), gender varchar(10), age int, weight int) RETURNS void
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
		
	-- Выбираем случайного рабочего и ветеринара
		worker := (SELECT id_employee from (select * from  employee where  position = 'Рабочий' and status  = 'Работает') as employee
					  ORDER BY RANDOM()
					  LIMIT 1);
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
$$ LANGUAGE plpgsql;



/* 5.3 Составить функцию для отображения информации о конкретном работнике (идентификатор работника следует передавать в качестве параметра функции): 
ФИО, зарплата, дата приема на работу, должность, количество заявок на осмотр животных за последний год, количество заявок на списание животных за последний год,
 количество проведенных осмотров животных за последний год (если сотрудник работает на должности ветеринара).
*/

CREATE OR REPLACE FUNCTION employee_info(id integer)
RETURNS table(name varchar(100), "Зарплата" int, "Начало работы" date, "Должность" varchar(100), "заявки на осмотр" bigint, "заявки на списание" bigint, "количество осмотров" bigint)
AS $$
DECLARE
	max_employee_val int;
	min_employee_val int;
BEGIN
	max_employee_val := (SELECT MAX(id_employee) FROM employee);
	min_employee_val := (SELECT MIN(id_employee) FROM employee);
		
		IF id > max_employee_val OR id < min_employee_val
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
$$ LANGUAGE plpgsql;




--------------------------------------------------------------------------

-- Мои новые штуки




-- Функция добавления нового сотрудника
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
$$ language plpgsql;








--13) осмотр

CREATE OR REPLACE FUNCTION inspect(num_application int, num_animal int, status varchar(10), id_vet int)
RETURNS void
AS $$
DECLARE
    count_animals int;
BEGIN
    -- проверка ветеринара
    IF id_vet NOT IN(SELECT id_employee FROM employee WHERE status='Работает' AND position='Ветеринар') THEN
        RAISE EXCEPTION 'Не существует такого действующего ветеринара !';
    END IF;
        
    -- проверка, существует ли такая заявка
    IF num_application NOT IN (SELECT keyapplication FROM all_app_inspection) THEN
        RAISE EXCEPTION 'Не существует такой заявки на осмотр !';
    END IF;
    
    -- проверка, указано ли данное существо в заявке
    IF num_animal NOT IN (SELECT numberanimal FROM all_app_inspection WHERE keyapplication=num_application) THEN
        RAISE EXCEPTION 'Данное животное не указано в заявке !';
    END IF;
    
    -- проверка, правильно ли указано состояние животного
    IF status NOT IN ('Больное', 'Здоровое') THEN
        RAISE EXCEPTION 'Неправильно указано состояние животного. Возможные варианты:  "Больное", "Здоровое" !';
    END IF;
    
    count_animals := (SELECT COUNT(*) FROM clarification_to_app WHERE keyapplication=num_application);
    
    -- проверяем, является ли животное единственным в заявке
    IF count_animals == 1 THEN
        DELETE FROM clarification_to_app WHERE keyapplication = num_application;
        DELETE FROM application WHERE keyapplication = num_application;
    ELSEIF count_animals >= 1 THEN
        DELETE FROM clarification_to_app WHERE keyapplication = num_application AND numberanimal = num_animal;
    END IF;
    
    -- обновляем состояние
    INSERT INTO Inspection_history(NumberAnimal, ID_employee, Date_inspection, Status) VALUES (num_animal, id_vet, CURRENT_DATE, status);
END;
$$ LANGUAGE plpgsql
SECURITY DEFINER;







-- 6) функция осмотра
create or replace function check_animal(vet varchar(100), numAnimal int, statusAn varchar(10))
returns void
as $$
declare 
    vetID int;

begin 
    --проверка ветеринара
    IF lower(vet) IN (SELECT lower(fullname) FROM employee WHERE status = 'Работает') AND (SELECT position FROM employee WHERE lower(fullname) = lower(vet)) = 'Ветеринар' THEN
        vetID:= (SELECT id_employee FROM employee WHERE lower(fullname) = lower(vet));
    ELSE
        RAISE EXCEPTION 'Не существует такого действующего ветеринара !';
    END IF;
    
    IF statusAn not in ('Больное', 'Здоровое') THEN
        RAISE EXCEPTION 'Недопустимый статус животного. Доступные статусы: Больное, Здоровое !';
    END IF;
    
    IF  (SELECT gender FROM animal WHERE numberanimal = numAnimal) IS NULL OR (SELECT write_off FROM animal WHERE numberanimal = numAnimal) IS NOT NULL THEN
        RAISE EXCEPTION 'Животного с номером % не существует или оно списано !', numAnimal;
    ELSE
        INSERT INTO Inspection_history(NumberAnimal, ID_employee, Date_inspection, Status) VALUES (numAnimal, vetID, CURRENT_DATE, statusAn);
    END IF;
    
end;
$$ language plpgsql
SECURITY DEFINER;








CREATE OR REPLACE FUNCTION change_feed(vet varchar(100), num_application int, numAnimals int[], animalFeed varchar[])
RETURNS void
AS $$
DECLARE
	employeeID int;
	feedID int[];
BEGIN
    -- проверка на существование сотрудника
	IF lower(vet) IN (SELECT lower(fullname) FROM employee WHERE status = 'Работает') AND (SELECT position FROM employee WHERE lower(fullname) = lower(vet)) = 'Ветеринар' THEN
        vetID:= (SELECT id_employee FROM employee WHERE lower(fullname) = lower(vet));
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
	FOR i IN 0..array_length(statusAnimals, 1) LOOP
		IF animalFeed[i] NOT IN (SELECT title FROM feed) THEN
        	RAISE EXCEPTION 'Неправильно указан корм одного из животных: %', animalFeed[i];
    	END IF;
    	feedID[i] = SELECT key_feed FROM feed WHERE title = animalFeed[i]
	END LOOP;
	
	RAISE INFO 'ID = %', feedID;

	
	-- проверяем наличие не списанных животных и обновляем их состояния
	--FOR i IN 0..array_length(numAnimals,1) LOOP
	--	UPDATE animal
	--	SET 
	--END LOOP;
	
	--удаляем заявку
	--PERFORM rm_application(num_application);
END;
$$ language plpgsql
SECURITY DEFINER;




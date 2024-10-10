CREATE TABLE Employee(
    ID_employee serial not null PRIMARY KEY,
    Login varchar(100) not null UNIQUE,
    Password varchar(100) not null,
    FullName varchar(100) not null,
    StartDate date not null CHECK(StartDate <= CURRENT_DATE),
    Position varchar(40) not null CHECK(Position in ('Ветеринар', 'Рабочий', 'Администратор', 'Заведующий хозяйством')),
    Status varchar(12) not null CHECK(Status in ('Работает', 'Не работает'))
);

CREATE TABLE Feed(
    Key_Feed serial not null PRIMARY KEY,
    Title varchar(100) not null CHECK(Title in ('Овёс', 'Пшеница', 'Морковка', 'Биокорм', 'Комбикорм')),
    Calorie_content int not null CHECK(Calorie_content > 50)
);

CREATE TABLE Type_Animal(
    TypeAnimal_key serial not null PRIMARY KEY,
    Name_of_type varchar(10) not null CHECK(Name_of_type in ('Хрюша', 'Корова', 'Курица', 'Страус', 'Кролик', 'Индейка'))
);

CREATE TABLE Animal(
    NumberAnimal serial not null PRIMARY KEY,
    ReceiptDate date not null CHECK(ReceiptDate <= CURRENT_DATE),
    Key_Feed serial not null,
    TypeAnimal_key serial not null,
    Age int not null CHECK(Age > 0 and Age >= ReceiptDate-CURRENT_DATE),
    Write_off date CHECK(Write_off <= CURRENT_DATE),
    Gender varchar(10) not null CHECK(Gender in ('Мужской','Женский')),

    FOREIGN KEY(Key_Feed) REFERENCES Feed(Key_Feed) 
    ON UPDATE CASCADE ON DELETE RESTRICT,

    FOREIGN KEY(TypeAnimal_key) REFERENCES Type_Animal(TypeAnimal_key) 
    on update cascade on delete restrict
);

CREATE TABLE Satiety_Animal(
    NumberAnimal serial not null,
    ID_employee serial not null,
    Satiety_key serial not null PRIMARY KEY,
    Feeding_time timestamp not null,

    FOREIGN KEY(ID_employee) REFERENCES Employee(ID_employee)
    on update cascade on delete restrict,

    FOREIGN KEY(NumberAnimal) REFERENCES Animal(NumberAnimal) 
    on update cascade on delete restrict
);


CREATE TABLE Dynamic_growth(
    Dynamic_key serial not null PRIMARY KEY,
    NumberAnimal serial not null,
    Date_in date not null CHECK(Date_in <= CURRENT_DATE),
    Weight int not null CHECK(Weight > 0),
    ID_employee serial not null,

    FOREIGN KEY(ID_employee) REFERENCES Employee(ID_employee)
    on update cascade on delete restrict,

    FOREIGN KEY(NumberAnimal) REFERENCES Animal(NumberAnimal)
    on update cascade on delete restrict
);

CREATE TABLE Inspection_history(
    Inspection_key serial not null PRIMARY KEY,
    NumberAnimal serial not null,
    ID_employee serial not null,
    Date_inspection date not null,
    Status varchar(10) not null CHECK(Status in ('Списанное', 'Больное', 'Здоровое')),

    FOREIGN KEY(NumberAnimal) REFERENCES Animal(NumberAnimal)
    on update cascade on delete restrict,

    FOREIGN KEY(ID_employee) REFERENCES Employee(ID_employee)
    on update cascade on delete restrict
);

CREATE TABLE Application_type(
    Application_type_key serial not null PRIMARY KEY,
    Name_of_app varchar(50) not null CHECK( Name_of_app in ('Заявка на списание', 'Заявка на осмотр', 'Заявка на изменение типа корма'))
);

CREATE TABLE Application(
    KeyApplication serial not null PRIMARY KEY,
    DateOfApp timestamp not null CHECK(DateOfApp <= CURRENT_DATE),
    ID_employee serial not null,
    Application_type_key serial not null,

    FOREIGN KEY(Application_type_key) REFERENCES Application_type(Application_type_key)
    on update cascade on delete restrict,

    FOREIGN KEY(ID_employee) REFERENCES Employee(ID_employee) 
    on update cascade on delete restrict
);


CREATE TABLE Clarification_to_app(
    Clarification_key serial not null PRIMARY KEY,
    NumberAnimal serial not null,
    KeyApplication serial not null,

    FOREIGN KEY(NumberAnimal) REFERENCES Animal(NumberAnimal)
    on update cascade on delete restrict,

    FOREIGN KEY(KeyApplication) REFERENCES Application(KeyApplication)
    on update cascade on delete restrict
);


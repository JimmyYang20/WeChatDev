create table test_patient(
    patient_id char(20),
    cardNo char(20),
    certification char(20),
    name char(10),
    gender char(1),
    birthdate date,
    address varchar(100),
    telephone char(20)
) engine ndb; 

create table test_doctor(
    code char(10),
    name char(10),
    birthday date,
    department1 char(20),
    department2 char(20),
    rank char(10),
    post char(10),
    profession char(10),
    right = char(10) 
) engine ndb; 

create table test_patient_chronicdisease(
    certification char(20),
    name char(10),
    code char(10),
    disease char(100),
    region char(20),
    catelog char(10)
) engine ndb; 

CREATE DATABASE mq_db default charset utf8 collate utf8_general_ci;
grant all PRIVILEGES on mq_db.* to dbusr@localhost identified by "123456" WITH GRANT OPTION;
FLUSH PRIVILEGES;

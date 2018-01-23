## 备份数据库

- 备份数据库
`mysqldump -u root -p gh_db > gh_db.backup.sql`

- 创建数据库
`mysql -u root -p -h dbserver -e "CREATE DATABASE gh_db_old default charset utf8 collate utf8_general_ci;"`

- 导入数据到新数据库
`mysql -u root -p -h dbserver gh_db_old < gh_db.backup.sql`

- 删除原来的数据库
`mysql -u root -p -h dbserver -e "DROP DATABASE gh_db"`

- 还原数据，这一步有可能会失败,失败是再根据错误信息手动导入出差错的数据
```
python manage.py makemigrations mainapp mngapp webapp parameters
python manage.py migrate
mysql -u root -p -h dbserver gh_db < gh_db.backup.sql
```

## 从旧数据库中导入数据
例子:
```
insert into gh_db.mainapp_sometable select * from gh_db_old.mainapp_sometable;
```


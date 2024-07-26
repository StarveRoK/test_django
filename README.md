# test_django
Test django

Были созданы 5 таблиц:

1. Organization - Название организаций
![image](https://github.com/user-attachments/assets/2bb58f09-7e71-48b3-a87c-eed7d36aa041)

2. User - Данные пользователя
![image](https://github.com/user-attachments/assets/0eff93e7-2e0b-447e-8be1-96992bcbeb3e)

3. Line - Линии месячных форм молодых специалистов
![image](https://github.com/user-attachments/assets/55e70da0-faaa-438b-bebe-aa79c6bce723)

4. Header - Шапка месячных форм молодых специалистов
![image](https://github.com/user-attachments/assets/52e34f79-b4b4-4fbe-8a57-01f463f845b3)
   
5. Indicator - Показатели молодых специалистов
![image](https://github.com/user-attachments/assets/293319dc-1531-414b-b257-0d23e6ac1271)


Колонки таблиц были созданы по ТЗ. В таблице indicator была добавлена дополнительная колонка "code"

На главной странице возможен выбор за какой период получить информацию. По дефолту Январь в обоих случаях
![image](https://github.com/user-attachments/assets/7f646fc0-0082-497d-9ee4-6f0cc1e1a17e)

При скачивании отчета:
  - Если за выбранный период нет данных, то Excel выглядит следующим образом:
![image](https://github.com/user-attachments/assets/197251c2-8f7b-4be0-b0a8-8f9e2d9e1687)

  - Если есть, то выбираются и добавляются статьи в Excel, которые есть за этот период:
![image](https://github.com/user-attachments/assets/63fc1f71-cc6e-4127-914b-3772d3e9be76)

Swagger:
![image](https://github.com/user-attachments/assets/a16fafda-c589-46fd-bd0b-723029da3132)

Other:
![image](https://github.com/user-attachments/assets/33d3ecff-7437-4efe-b560-6d4915df21bf)

Добавил view для объеденения всех таблиц:
```
CREATE VIEW indicator_line_head_view AS
            SELECT           
                i.date_valid_until,
                i.article_name,
                i.article_code,
                i.order,
                i.last_updated as last_updated_indicator,
                ui.username as username_indicator,
            
                h.start_date,
                h.end_date,
                o.name,
                h.created_at,
            
                l.distribution_count,
                l.targeted_distribution_count,
                l.last_updated as last_updated_line,
                ul.username as username_line
            FROM
                example_app_line AS l
            JOIN
                example_app_indicator AS i ON l.indicator_id = i.id
            JOIN
                example_app_header AS h ON l.header_id = h.id
            JOIN
                example_app_user AS ui ON i.updated_by_id = ui.id
            JOIN
                example_app_user AS ul ON l.updated_by_id = ul.id
            JOIN
                example_app_organization AS o ON l.header_id = h.id;
```

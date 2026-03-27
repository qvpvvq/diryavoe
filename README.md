# diryavoe
1. Создайте файл .env в корне проекта и скопируйте туда содержимое .env.example
2. Соберите образ:
docker build -t sqli-app
3. Запустите контейнер:
docker run -p 5000:5000 sqli-app
4. Чек адрес
http://127.0.0.1:5000

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Task+FastAPI+Redis)](https://git.io/typing-svg)

Данный проект разработан для осуществления взаимодействия между FastAPI и Redis. В проекте присутствует Dockerfile, который позволяет собрать проект в docker и начать взаимодействие с сервисом.

## Запуск

В проекте использовался FastAPI версии 0.78.0. Для запуска через докер воспользуйтесь командой сборки image следующей командой:

```
docker build -t fastapi:v.0.1 .
```

После сборки воспользуйтесь командой для запуска:

```
docker run -it -d  -p 80:80 fastapi:v.0.1
```


## Запросы по SQL

Ниже приведены 3 варианта для решения задачи по SQL

```
UPDATE full_names
SET status = short_names.status
FROM short_names
WHERE full_names.name = CONCAT(short_names.name, '.mp3') 
OR full_names.name = CONCAT(short_names.name, '.wav');
```

```
UPDATE full_names
SET status = short_names.status
FROM short_names
WHERE short_names.name = SUBSTRING(full_names.name, 0, POSITION('.' IN full_names.name) );
```

```
UPDATE full_names AS f
SET status = s.status
FROM short_names AS s
WHERE f.name = CONCAT(s.name, '.', SUBSTRING(f.name, POSITION('.' IN f.name) + 1));
```



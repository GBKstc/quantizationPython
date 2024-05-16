# 一个用来练习python的项目

在阿里云服务器中启动项目
ps aux | grep gunicorn 查找PID
kill [PID]             关闭进程
gunicorn -w 4 -b 0.0.0.0:8000 run:app  在db目录下重新启动

gunicorn -c gunicorn_config.py run:app

                       
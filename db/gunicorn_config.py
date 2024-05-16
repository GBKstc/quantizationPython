# gunicorn_config.py
bind = "0.0.0.0:8000"  # 监听的 IP 和端口
workers = 4             # 工作进程数量
accesslog = '-'         # 访问日志文件，'-' 表示标准输出
errorlog = '-'          # 错误日志文件，'-' 表示标准输出
capture_output = True   # 重定向标准输出/错误输出到指定的日志文件
timeout = 120           # 超时设置
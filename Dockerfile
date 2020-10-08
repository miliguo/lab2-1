#拉取镜像
FROM python:3.7-alpine
#指定工作目录，目录名称自己定义，如果当前指定的目录不存在的话，这个目录会自动被创建
WORKDIR /demoapp

#复制当前文件夹下的所有项目文件到docker的工作目录，也就是我们上面指定的目录
COPY . .

#根据requirements.txt文件，安装相关依赖包
RUN pip install -r requirements.txt

#CMD gunicorn -w 2 app:app
#指定docker运行的时候默认执行的命令，我们想让flask网站随docker启动时就运行
CMD ["python", "app.py"]
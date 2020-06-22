# github_avatar_fixer
生成hosts配置，解决github头像无法显示问题
## 使用方法
运行python3 fixer.py命令后，目录下会生成avatar_conf.txt文件，将文件中的内容复制到hosts配置文件中。如果hosts中已存在失效的github hosts配置信息，将其替换即可

## hosts文件路径
#### Mac/Linux
/etc/hosts
#### Windows
C:\WINDOWS\system32\drivers\etc\hosts
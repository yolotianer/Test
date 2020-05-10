import yaml

file=open('ppp.yml',encoding='UTF-8')
res=yaml.load(file,Loader=yaml.FullLoader)
# 打印出字典形式
print(res)
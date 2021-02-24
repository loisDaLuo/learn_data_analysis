import pandas as pd
import matplotlib.pyplot as plt
# 读取数据
data = pd.read_csv('E:/BaiduNetdiskDownload/最近数据分析15期/第七章 Python/第七章/20200831数据源/20200831数据源.csv',encoding="ISO-8859-1")
# print(data)
# 清洗数据
#1.不合理的数据
## 1.1跟据业务需要提取数据，发货日期早于下单日期  不合理值
data['OrderDate'] = pd.to_datetime(data['OrderDate'])
data['ShipDate'] = pd.to_datetime(data['ShipDate'])
# 时间差
data['interval'] = (data.ShipDate - data.OrderDate).dt.total_seconds()
# print(data.info())
# data[data.interval < 0]
data.drop(index = data[data.interval < 0].index,inplace=True)
# print(data.info())
# data['interval'] = data.ShipDate - data.OrderDate
# 没有售价为负的数据
# print(data[data.Sales < 0])
## 1.3 查看数据
# print(data.info())
# print(data.isna().sum())
## (1)清洗PostalCode列 40000+为空
## (2)清洗ShipMode列 11为空
# print(data.describe()) ## 可以查看某一列的数据情况 最大最小值、均值、众数
# print(data.head())
# print(data.count())
## 1.4 清洗RowID 重复值

###  1111
####  333

# print(data['RowID'])
# print(data.RowID.size)
# print(data.RowID.unique().size)
# print(data[data.RowID.duplicated()])
data.drop(index=data[data.RowID.duplicated()].index,inplace=True)
# print(data.RowID.size)

## 1.5 清洗ShipMode
# print(data.ShipMode.size)
# print(data[data.ShipMode.isnull()])
# 众数填充空值
# print(data.ShipMode.mode()[0])
data['ShipMode'].fillna(value=data.ShipMode.mode()[0],inplace=True)
# print(data[data.ShipMode.isnull()])
## 1.6 清洗Discount 折扣 用平均值填充
# print(data[data.Discount > 1]) ## 有数据
# print(data[data.Discount < 0]) ## 无数据
print(data[data['Discount'] > 1])

data['Discount']=data.Discount.mask(data.Discount > 1,None)
# print(data[data['Discount'].isna()])
# 平均折扣
discount_mean = data[data.Discount.notnull()].Discount.mean()
print(discount_mean)
data.fillna(value=data.Discount,)
## 1.7 清洗PostalCode列


#2.重复的数据
#3.为空的数据

## 缺失数据 PostalCode ShipMode
# 分析数据
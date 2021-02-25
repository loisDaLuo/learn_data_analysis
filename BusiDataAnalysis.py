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
# mark 把符合条件的数据置为指定数值
data['Discount']=data.Discount.mask(data.Discount > 1,None)
# print(data[data['Discount'].isna()])
# 平均折扣
discount_mean = data[data.Discount.notnull()].Discount.mean()
# print(discount_mean)
# print(data[data['Discount'].isna()].Discount.size)
data['Discount'].fillna(value=discount_mean,inplace=True)
# print(data[data['Discount'].isna()].Discount.size)

## 1.7 清洗PostalCode列
data.drop(columns=['PostalCode'],inplace=True)
# print(data.info())
#2.重复的数据
#3.为空的数据
## 缺失数据 PostalCode ShipMode

# 分析数据
## 每年销售额增长情况
data["Order-year"] = data['OrderDate'].dt.year
data['Order-month'] = data['OrderDate'].dt.month
data['quarter'] = data['OrderDate'].dt.to_period('Q')
# print(data['quarter'])
year_sales = data.groupby(by='Order-year').Sales.sum()
## year-sales Series类型
# print(year_sales)
year_sale_12 = (year_sales[2012] - year_sales[2011])/year_sales[2011]
year_sale_13 = (year_sales[2013] - year_sales[2012])/year_sales[2012]
year_sale_14 = (year_sales[2014] - year_sales[2013])/year_sales[2013]
# print(year_sale_12)
# print(year_sale_13)
# print(year_sale_14)

sale_rate_12 = "%.2f%%" % (year_sale_12 * 100)
sale_rate_13 = "%.2f%%" % (year_sale_13 * 100)
sale_rate_14 = "%.2f%%" % (year_sale_14 * 100)
print(sale_rate_12)
print(sale_rate_13)
print(sale_rate_14)
## 各个地区分店销售额
## 销售淡旺季分析
## 新增用户
## 用户RFM模型分析

1111111
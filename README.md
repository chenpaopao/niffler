# niffler
quant 数据伺服系统，自动数据入库，并为后续流程提供数据接口

数据获取主要基于aksahre项目(https://akshare-4gize6tod19f2d2e-1252952517.tcloudbaseapp.com/data/stock/stock.html)

数据模块的规划如下：
- [ ] akshare封装模块：统一某些常用数据获取接口
- [ ] 数据质量模块：对数据获取后进行质量检查模块，是不是数据缺少严重
- [ ] 数据接口模块：实现insert_data(symbol, start_time, end_time), get_data(symbol, start_time, end_time)
- [ ] 数据仓库模块：数据经过下载，符合入库规则后可以入库
- [ ] 数据清洗模块：可以安装一定规则进行清洗再入库
- [ ] 数据映射表：akshare的数据字段太多太杂，需要统一变成一张大的kv格式的表进行数据入库，对照表存在谷歌文档
- [ ] 反爬模块： 对于akshare接口多次调用的，会可能被封ip
# 珠宝店的爬虫
__帮人写着玩的__

## 爬虫artron
爬取了名字和估价以及成交价，网站使用了浏览器头、封锁ip和登录来阻止爬虫
解决方法：请求头直接在setting中设置，封锁ip使用接口获取，登录直接使用cookies模拟登录

## 爬虫jiade(半成品)
爬取了编号，名称，成交日期以及成交价格，网站是全程动态生成的
解决方法：直接使用浏览器模拟
没解决：网站渲染时间的确定(__如果网页没刷新页面的元素获取不了__)暂时的解决方法(使用time模块的sleep方法,__使用selenium里面的显示等待还是隐式等待都没成功__)


## 简单谈一下爬虫
爬虫一般来说就是写数据提取式，反爬一般就是模拟登录，限制IP，浏览器请求头，验证码验证。
如果你觉得哪个网站反扒很厉害(__使用模拟浏览器万金油方法__)


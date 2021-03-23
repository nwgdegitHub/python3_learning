# 参考自：https://www.jianshu.com/p/cecb29c04cd2

# pip3 install Scrapy
#
# 创建项目：scrapy startproject xxx
# 进入项目：cd xxx
# 创建爬虫：scrapy genspider xxx（爬虫名） xxx.com （爬取域）
# 生成文件：scrapy crawl xxx -o xxx.json (生成某种类型的文件)
# 运行爬虫：scrapy crawl XXX
# 列出所有爬虫：scrapy list

# 爬虫能干什么？
# 举个例子，你打开电影天堂，上面很多电影数据，都是从豆瓣或别的地方爬来的，存在他的数据库中，
# 然后他只是简单做了一下梳理，整了一个界面。就做成一个流量几十万的网站，靠着广告费都能赚一大笔了

# 再比如天眼查，集数据采集，数据清洗，数据建模，数据产品化为一体的大数据
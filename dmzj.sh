#get dmzj home page 10 the data
#task config example
#40 16 * * * nohup /usr/bin/sh /weixin/scrapy-dmzj/dmzj.sh >> /weixin/scrapy-dmzj/log/$(date +"\%Y-\%m-\%d").log 2>&1 &
cd /weixin/scrapy-dmzj
scrapy crawl dmzj
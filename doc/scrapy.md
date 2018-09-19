# scrapy相关总结

## 一、scrapy安装：

```bash
sudo pip install Scrapy --upgrade --ignore-installed six
```

## 二、页面调试：

使用`scrapy shell`调试页面，并分析页面构成。

```bash
scrapy shell http://www.jycinema.com/html/default/index.html
```

```text
>>> scrapy shell http://www.jycinema.com/html/default/index.html
2018-09-20 00:29:59 [scrapy.utils.log] INFO: Scrapy 1.5.1 started (bot: scrapybot)
2018-09-20 00:29:59 [scrapy.utils.log] INFO: Versions: lxml 4.2.5.0, libxml2 2.9.8, cssselect 1.0.3, parsel 1.5.0, w3lib 1.19.0, Twisted 18.7.0, Python 2.7.10 (default, Oct  6 2017, 22:29:07) - [GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)], pyOpenSSL 18.0.0 (OpenSSL1.1.0i  14 Aug 2018), cryptography 2.3.1, Platform Darwin-17.6.0-x86_64-i386-64bit
2018-09-20 00:29:59 [scrapy.crawler] INFO: Overridden settings: {'LOGSTATS_INTERVAL': 0, 'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter'}
2018-09-20 00:29:59 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.corestats.CoreStats']
2018-09-20 00:29:59 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2018-09-20 00:29:59 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2018-09-20 00:29:59 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2018-09-20 00:29:59 [scrapy.extensions.telnet] DEBUG: Telnet console listening on 127.0.0.1:6023
2018-09-20 00:29:59 [scrapy.core.engine] INFO: Spider opened
2018-09-20 00:29:59 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://www.jycinema.com/html/default/index.html> (referer: None)
[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x10d20ab50>
[s]   item       {}
[s]   request    <GET http://www.jycinema.com/html/default/index.html>
[s]   response   <200 http://www.jycinema.com/html/default/index.html>
[s]   settings   <scrapy.settings.Settings object at 0x10d20a5d0>
[s]   spider     <DefaultSpider 'default' at 0x10de23dd0>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser
>>> response.body
'<!doctype html><html class="no-js"><head><meta charset="utf-8"><meta name="renderer" content="webkit"><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><title>\xe9\x87\x91\xe9\x80\xb8\xe7\x94\xb5\xe5\xbd\xb1</title><meta name="description" content="\xe5\x9c\xa8\xe7\xba\xbf\xe5\xbd\xb1\xe9\x99\xa2,\xe5\x9c\xa8\xe7\xba\xbf\xe8\xb4\xad\xe7\xa5\xa8,\xe5\xb9\xbf\xe5\xb7\x9e\xe7\x94\xb5\xe5\xbd\xb1,\xe6\x9c\x80\xe6\x96\xb0\xe7\x94\xb5\xe5\xbd\xb1,\xe6\x8a\x98\xe6\x89\xa3\xe7\x94\xb5\xe5\xbd\xb1"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="icon" href="images/logo-icon.ico" type="image/x-icon"><link rel="stylesheet" href="themes/default/default.css"><link rel="stylesheet" href="themes/default/member-center-yzl.css"><link rel="stylesheet" href="themes/default/unslider1.css"><script src="js/check.js"></script></head><body><style>#index-banner ul li{height:350px}#comingfilmlist ul li,#hotfilmlist ul li{height:700px}</style><div data-html="components/header/header.html"></div><div class="main"><div class="top-bg"></div><div class="bottom-bg"></div><div id="index-banner" class="banner"><ul></ul><a href="javascript:void(0);" class="index-slider-arrow prev" style="display:none"><img class="arrow" id="al" src="images/arrowl.png" alt="prev" width="20" height="35"></a><a href="javascript:void(0);" class="index-slider-arrow next" style="display:none"><img class="arrow" id="ar" src="images/arrowr.png" alt="next" width="20" height="37"></a></div><div id="fastSearch" class="box-shadow mb15"><div class="wrap"><form method="post" action="seat.html"><div class="fl"><span class="title f16 fb pr10 lh32"><i class="iconfont icon-shandian f20"></i>\xe5\xbf\xab\xe9\x80\x9f\xe8\xb4\xad\xe7\xa5\xa8</span></div><div class="col-22-5 pr" id="filmareachoose"><span class="cleanall" style="display:none">\xe6\xb8\x85\xe9\x99\xa4</span><div class="jy-input-group mt5"><span class="input" id="cinemaName" name="cinema" type="text">\xe8\xaf\xb7\xe9\x80\x89\xe6\x8b\xa9\xe5\xbd\xb1\xe9\x99\xa2</span> <span class="jy-input-group-addon"><i class="iconfont icon-sanjiao-copy"></i></span></div><div class="jy-dropdown cinemabox"><div class="arealist" id="area"></div></div></div><div class="col-22-5 pr" id="filmchoose"><span class="cleanall" style="display:none">\xe6\xb8\x85\xe9\x99\xa4</span><div class="jy-input-group mt5"><span class="input" id="filmName" name="filmName" type="text">\xe8\xaf\xb7\xe9\x80\x89\xe6\x8b\xa9\xe5\xbd\xb1\xe7\x89\x87</span> <span class="jy-input-group-addon"><i class="iconfont icon-sanjiao-copy"></i></span></div><div class="jy-dropdown filmbox"><ul id="films"></ul></div></div><div class="col-22-5 pr" id="timechoose"><div class="jy-input-group mt5 disable" id="sessionType"><span class="input" id="session" name="session" type="text">\xe8\xaf\xb7\xe9\x80\x89\xe6\x8b\xa9\xe5\x9c\xba\xe6\xac\xa1</span> <span class="jy-input-group-addon"><i class="iconfont icon-sanjiao-copy"></i></span></div><div class="jy-dropdown sessionbox"><div class="film-data tab-group"><header><ul class="tab" id="datechoose"></ul></header><div class="tab-body index-tab-body" id="ticketchoose"></div></div></div></div></form></div></div><div class="wrap"><div class="row"><div class="col-9"><div class="film-data tab-group"><header><span class="fr pr10 film-list-tip">\xe5\x85\xb1\xe6\x9c\x89 <span class="brand-warning" id="showNum"></span> \xe9\x83\xa8\xe7\x94\xb5\xe5\xbd\xb1\xe6\xad\xa3\xe5\x9c\xa8\xe7\x83\xad\xe6\x98\xa0\xe4\xb8\xad</span><ul class="tab"><li class="active"><a href="javascript:;">\xe6\xad\xa3\xe5\x9c\xa8\xe7\x83\xad\xe6\x98\xa0</a></li><li id="commingId"><a href="javascript:">\xe5\x8d\xb3\xe5\xb0\x86\xe4\xb8\x8a\xe6\x98\xa0</a></li></ul></header><div class="tab-body index-tab-body m20"><div class="tab-panel active"><div id="hotfilmlist" class="banner"><ul></ul></div><a href="javascript:void(0);" class="hot-arrow prev"style="display:none"><div class="arrow" id="hotal"></div></a><a href="javascript:void(0);" class="hot-arrow next" style="display:none"><div class="arrow" id="hotar"></div></a></div><div class="tab-panel"><div id="comingfilmlist" class="banner"><ul></ul></div><a href="javascript:void(0);" class="coming-arrow prev" style="display:none"><div class="arrow" id="comingal"></div></a><a href="javascript:void(0);" class="coming-arrow next" style="display:none"><div class="arrow" id="comingar"></div></a></div></div></div></div><div class="col-3"><div class="container"><div class="panel mt20 border-line white_bg"><span class="spirit spirit-top-right-vi-img abs-right-top"></span><header>\xe7\xbd\x91\xe7\xab\x99\xe5\x85\xac\xe5\x91\x8a</header><ul class="ul-list news" id="noticemessage"></ul><a href="noticemessage.html" class="ml160"><small>\xe6\x9b\xb4\xe5\xa4\x9a&nbsp;&raquo;</small></a></div><div class="border-line panel mt10 p0 white_bg"><span class="spirit spirit-top-right-vi-img abs-right-top"></span><header class="pl15 pt15">\xe8\xb4\xad\xe7\xa5\xa8\xe6\xb5\x81\xe7\xa8\x8b</header><div class="process"></div></div><div class="border-line panel mt10 oh white_bg"><span class="spirit spirit-top-right-vi-img abs-right-top"></span><header>APP&\xe5\xbe\xae\xe4\xbf\xa1\xe5\x85\xac\xe4\xbc\x97\xe5\x8f\xb7</header><div class="col-6 tc"><img src="images/qrAPP.png"> <span>\xe6\x89\xab\xe6\x8f\x8f\xe4\xb8\x8b\xe8\xbd\xbdAPP</span></div><div class="col-6 tc"><img src="images/qrwechat.jpg"> <span>\xe5\xbe\xae\xe4\xbf\xa1\xe5\x85\xac\xe4\xbc\x97\xe5\x8f\xb7</span></div></div><div class="mt10 oh"><div class="banner" id="ad-banner"><ul></ul></div></div></div></div></div><div id="articleId" class="row"><h3>\xe9\x87\x91\xe9\x80\xb8\xe6\x8e\xa8\xe8\x8d\x90</h3><div id="articleList" class="bt"></div><div class="row tc p10"><button id="moreBtn" class="btn btn-primary"><span class="iconfont m5">&#xe674;</span>\xe5\x8a\xa0\xe8\xbd\xbd\xe6\x9b\xb4\xe5\xa4\x9a</button></div></div></div></div><div data-html="components/footer/footer.html"></div><script src="js/plugs/require.min.js"data-main="js/ajax/index-3b11e452ed.min"></script></body></html>'
```

## scrapy框架生成：

* 生成项目（project）：

```bash
scrapy startproject today_movie
```

* 生成爬虫（spider）：

```bash
scrapy genspider hz_movie jycinema.com
```

* 框架目录结构：

```bash
today_movie
├── scrapy.cfg
└── today_movie
    ├── __init__.py
    ├── __init__.pyc
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    ├── settings.pyc
    └── spiders
        ├── __init__.py
        ├── __init__.pyc
        └── hz_movie.py
```

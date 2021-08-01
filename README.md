# learning-python-web-crawler

Python 網路爬蟲實作技術班

```
110/05/08(星期六) 09:00~12:00 認識網路爬蟲(1.認識HTML, 2.認識爬蟲的類型, 3.搜尋引擎與爬蟲原理, 4.網路爬蟲的搜尋方法)
110/05/08(星期六) 13:00~16:00 認識JSON(1.認識JSON資料格式, 2.將Python應用在JSON字串形式資料, 3.將Python應用在JSON檔案, 4.簡單的JSON檔案應用)
110/05/15(星期六) 09:00~12:00 認識CSV(1.認識CSF資料格式, 2.讀取CSV檔案, 3.寫入CSV檔案, 4.簡單的CSV檔案應用)
110/05/15(星期六) 13:00~16:00 網路爬蟲基礎實作(1.webbrowser模組, 2.requests模組, 3.檢視網頁原始碼, 4.使用開發人員工具分析網站, 5.urllib模組, 6.認識httpbin網站, 7.認識Cookie)
110/07/03(星期六) 09:00~12:00 表單(1.使出者互動與表單, 2.表單的驗證, 3.表單模型化)
110/07/03(星期六) 13:00~16:00 Cookies與Sessions(1.Cookies, 2.Sessions)
110/07/10(星期六) 09:00~12:00 Pandas模組一(1.Series, 2.DataFrame, 3.基本Pandas資料分析與處理)
110/07/10(星期六) 13:00~16:00 Pandas模組二(1.檔案的輸入與輸出, 2.Pandas繪圖, 3.時間序列)
110/07/17(星期六) 09:00~12:00 BeautifulSoup解析網頁(1.BeautifulSoup模組, 2.其它HTML文件解析)
110/07/17(星期六) 13:00~16:00 網頁自動化(1.hashlib模組, 2.工作排程與自動執行)
110/07/24(星期六) 09:00~12:00 Selenium一(1.安裝Selenium工具, 2.WebDriver, 3.擷取網頁, 4.尋找HTML文件的元素)
110/07/24(星期六) 13:00~16:00 Selenium二(1.XPath語法, 2.控制點選超連結, 3.處理使用網頁的特殊按鍵, 4.處理瀏覽器的運作)
110/07/31(星期六) 09:00~12:00 股市數據爬取與分析(1.證券櫃檯買賣中心, 2.台灣證券交易所, 3.台灣股市資料讀取與圖表製作)
110/07/31(星期六) 13:00~16:00 Requests-HTML模組(1.安裝模組, 2.使用者請求Session, 3.數據清洗與爬取, 4.Ajax動態數據加載)
```


## week1

```
PS D:\ws\python-web-crawler> pip install requests
Requirement already satisfied: requests in c:\python38-32\lib\site-packages (2.25.0)
Requirement already satisfied: idna<3,>=2.5 in c:\python38-32\lib\site-packages (from requests) (2.10)
Requirement already satisfied: chardet<4,>=3.0.2 in c:\python38-32\lib\site-packages (from requests) (3.0.4)
Requirement already satisfied: certifi>=2017.4.17 in c:\python38-32\lib\site-packages (from requests) (2020.11.8)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\python38-32\lib\site-packages (from requests) (1.26.2)
PS D:\ws\python-web-crawler>

PS D:\ws\python-web-crawler> pip list | grep requests
requests            2.25.0
```


```
PS D:\ws\python-web-crawler> & c:/python38-32/python.exe d:/ws/python-web-crawler/week1/lab03_requests.py
<!DOCTYPE HTML>
<html lang="en-US">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1" />
  <meta name="robots" content="noindex, nofollow" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Just a moment...</title>
  <style type="text/css">
    html, body {width: 100%; height: 100%; margin: 0; padding: 0;}
    body {background-color: #ffffff; color: #000000; font-family:-apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, "Helvetica Neue",Arial, sans-serif; font-size: 16px; line-height: 1.7em;-webkit-font-smoothing: antialiased;}
    h1 { text-align: center; font-weight:700; margin: 16px 0; font-size: 32px; color:#000000; line-height: 1.25;}
    p {font-size: 20px; font-weight: 400; margin: 8px 0;}
    p, .attribution, {text-align: center;}
    #spinner {margin: 0 auto 30px auto; display: block;}
    .attribution {margin-top: 32px;}
    @keyframes fader     { 0% {opacity: 0.2;} 50% {opacity: 1.0;} 100% {opacity: 0.2;} }
    @-webkit-keyframes fader { 0% {opacity: 0.2;} 50% {opacity: 1.0;} 100% {opacity: 0.2;} }
    #cf-bubbles > .bubbles { animation: fader 1.6s infinite;}
    #cf-bubbles > .bubbles:nth-child(2) { animation-delay: .2s;}
    #cf-bubbles > .bubbles:nth-child(3) { animation-delay: .4s;}
    .bubbles { background-color: #f58220; width:20px; height: 20px; margin:2px; border-radius:100%; display:inline-block; }
    a { color: #2c7cb0; text-decoration: none; -moz-transition: color 0.15s ease; -o-transition: color 0.15s ease; -webkit-transition: color 0.15s ease; transition: color 0.15s ease; }
    a:hover{color: #f4a15d}
    .attribution{font-size: 16px; line-height: 1.5;}
    .ray_id{display: block; margin-top: 8px;}
    #cf-wrapper #challenge-form { padding-top:25px; padding-bottom:25px; }
    #cf-hcaptcha-container { text-align:center;}
    #cf-hcaptcha-container iframe { display: inline-block;}
  </style>

      <meta http-equiv="refresh" content="12">
  <script type="text/javascript">
    //<![CDATA[
    (function(){

      window._cf_chl_opt={
        cvId: "2",
        cType: "non-interactive",
        cNounce: "30602",
        cRay: "64bf86be495d56e8",
        cHash: "c7082f39cc34b5a",
        cFPWv: "b",
        cTTimeMs: "4000",
        cRq: {
          ru: "aHR0cHM6Ly93d3cubW9iaWxlMDEuY29tLw==",
          ra: "TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgNi4xOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTAuMC40NDMwLjkzIFNhZmFyaS81MzcuMzY=",
          rm: "R0VU",
          d: "WmnWSI0PringpMZwqDXtm6gJ6IaMdTfK8kVgmkh7yHLGOnX9kY4thOOWww34Hjrf5IDNt3l2qlFb4E2vSdVue65IKKnberJS8hhNZ28CyuNEUQLFeBcqNJ+vxC2qPG5NZ4p8QryeMwUNRwFWx6/PDyh50seOz+4WEpsT8zmIl7L87F94rU88zWXDFuz0TOqHOi0+sEAJOb5ikW5QQzA9QmQYlBUhTotIxxGvU1ElCwY4KxYHshKLbgt8ETikTKkhLcvOCiG3QxgMnHBgbAZOKjQz5QWtbAJTkOLay5k9BzGEZLCfQTolpO0PoP/McWNu0jf49jSR64hOTAHQpRqE5VOdDabYdA50q5LSOGJ4x245LgWO/OlM2GNwzhRTusCGqrj4uJObIGvDWYdXedUmfSW2nEDqKsCs4JNLrKEqYD11+l1hT6FLA6EqxT3PsHHHf/TvfsEkIc4h9Ol/cNscweS1S3jrffGHBUKifuxnY42BKT7ZQW9RbIVI06YyKGlSejsv53fMxutq0wFCKb+6o8hH0/VOxQcTPeWyVxYNmHLaJw0k2R7BCUQJABpDZ7O98AKkC5bLwZcP3X1DOjSzhrtg3B6CuGWtRU4uL7zy7JtTi9rYmZ420B4RlSI20YrCIbX3A5eokE17Pc3OHOgiYpVxlbP5lPeEgp0do75/Db1DQowkQsz4r/tjdkfBHO+pykQABQG9vPBXg2H6K+BydoVY9arh6+QBngRA2FMtsM0=",
          t: "MTYyMDQ0Mzc1NS4yNTEwMDA=",
          m: "9wEg7jkDV3TV3DkktqhRgUD7WMk6suR6g0uZY8ONhI0=",
          i1: "4zkfABw4djpZwKCfwA3AqA==",
          i2: "m8SMQLNCTDTtoGxCNwt4LA==",
          zh: "5X3p6t0UbHOY6QW6HWeBG6UtAANlCDXbnwapfzxXMdc=",
          uh: "55ytQTm0lZTNUFKjFBZ4OT4w+2zzyykOhp8qUNXa02w=",
          hh: "9j8dRtubWPXtyIkysxuk+pQSkSk6XFRftOEhDRuC/Zg=",
        }
      }
      window._cf_chl_enter = function(){window._cf_chl_opt.p=1};

    })();
    //]]>
  </script>


</head>
<body>
  <table width="100%" height="100%" cellpadding="20">
    <tr>
      <td align="center" valign="middle">
          <div class="cf-browser-verification cf-im-under-attack">
  <noscript>
    <h1 data-translate="turn_on_js" style="color:#bd2426;">Please turn JavaScript on and reload the page.</h1>
  </noscript>
  <div id="cf-content" style="display:none">

    <div id="cf-bubbles">
      <div class="bubbles"></div>
      <div class="bubbles"></div>
      <div class="bubbles"></div>
    </div>
    <h1><span data-translate="checking_browser">Checking your browser before accessing</span> mobile01.com.</h1>

    <div id="no-cookie-warning" class="cookie-warning" data-translate="turn_on_cookies" style="display:none">
      <p data-translate="turn_on_cookies" style="color:#bd2426;">Please enable Cookies and reload the page.</p>
    </div>
    <p data-translate="process_is_automatic">This process is automatic. Your browser will redirect to your requested content shortly.</p>
    <p data-translate="allow_5_secs" id="cf-spinner-allow-5-secs" >Please allow up to 5 seconds&hellip;</p>
    <p data-translate="redirecting" id="cf-spinner-redirecting" style="display:none">Redirecting&hellip;</p>
  </div>
	...
	..
	.
```

網站有防止爬蟲頻繁刷站: `Please allow up to 5 seconds`

透過 cloudscraper (須付費) 可以嘗試解決

```
PS D:\ws\python-web-crawler> pip install cloudscraper
Collecting cloudscraper
  Downloading cloudscraper-1.2.58-py2.py3-none-any.whl (96 kB)
     |████████████████████████████████| 96 kB 397 kB/s
Requirement already satisfied: pyparsing>=2.4.7 in c:\python38-32\lib\site-packages (from cloudscraper) (2.4.7)
Collecting requests-toolbelt>=0.9.1
  Downloading requests_toolbelt-0.9.1-py2.py3-none-any.whl (54 kB)
     |████████████████████████████████| 54 kB 616 kB/s
Requirement already satisfied: requests>=2.9.2 in c:\python38-32\lib\site-packages (from cloudscraper) (2.25.0)
Requirement already satisfied: certifi>=2017.4.17 in c:\python38-32\lib\site-packages (from requests>=2.9.2->cloudscraper) (2020.11.8)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\python38-32\lib\site-packages (from requests>=2.9.2->cloudscraper) (1.26.2)
Requirement already satisfied: idna<3,>=2.5 in c:\python38-32\lib\site-packages (from requests>=2.9.2->cloudscraper) (2.10)
Requirement already satisfied: chardet<4,>=3.0.2 in c:\python38-32\lib\site-packages (from requests>=2.9.2->cloudscraper) (3.0.4)
Installing collected packages: requests-toolbelt, cloudscraper
Successfully installed cloudscraper-1.2.58 requests-toolbelt-0.9.1
```

beautifulsoup4 - 幫我們解析網頁 HTML 元素的套件

```
PS D:\ws\python-web-crawler> pip install beautifulsoup4
Collecting beautifulsoup4
  Downloading beautifulsoup4-4.9.3-py3-none-any.whl (115 kB)
     |████████████████████████████████| 115 kB 437 kB/s
Collecting soupsieve>1.2
  Downloading soupsieve-2.2.1-py3-none-any.whl (33 kB)
Installing collected packages: soupsieve, beautifulsoup4
Successfully installed beautifulsoup4-4.9.3 soupsieve-2.2.1
PS D:\ws\python-web-crawler>
```

```
PS D:\ws\python-web-crawler> & c:/python38-32/python.exe d:/ws/python-web-crawler/week1/lab05_beautifulsoup4.py
d:/ws/python-web-crawler/week1/lab05_beautifulsoup4.py:11: GuessedAtParserWarning: No parser was explicitly specified, so I'm using
the best available HTML parser for this system ("html.parser"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 11 of the file d:/ws/python-web-crawler/week1/lab05_beautifulsoup4.py. To get rid of this warning, pass the additional argument 'features="html.parser"' to the BeautifulSoup constructor.

  soup = bs4.BeautifulSoup(response.text)
<title>國內投資 - Mobile01</title>
PS D:\ws\python-web-crawler>
```

If you can, I recommend you install and use lxml for speed

```
PS D:\ws\python-web-crawler> pip install lxml
Collecting lxml
  Downloading lxml-4.6.3-cp38-cp38-win32.whl (3.2 MB)
     |████████████████████████████████| 3.2 MB 939 kB/s
Installing collected packages: lxml
Successfully installed lxml-4.6.3
PS D:\ws\python-web-crawler>
```

Test in 偵錯主控台，先設定中斷


```
soup.find('header')
soup.find_all('div')
```

`soup.find('div', class_='l-listTable__tbody')`

HTML 寫的是 class='l-listTable__tbody', 但是 class 是 python 的保留字，所以程式用 `class_` 替代。

Ref: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class

否則:

```
soup.find('div', class='l-listTable__tbody')
                     ^
SyntaxError: invalid syntax
```


find 的使用方式通常是需要一層層找，例如: 先找到 table body, 再找下面的 tr

所以 bs4 有另一種方式 -- select

<tag id="id_name">
<tag2 id="id_name">
`soup.select('#id_name')` --> 只會回傳第一筆 <tag>

<tag class="class_name">
`soup.select('tag.class_name')`

當 class_name 只出現在特定的 tag 可省略 tag --> `soup.select('.class_name')`

小心下面這兩種差異:


階層:

```
<p>
	<div class="intro" />
</p>
```

`soup.select('p .intro')`


屬性關係

```
<p class="intro" />
```

`soup.select('p.intro')`


cloudscraper 的限制 = =

```
cloudscraper.exceptions.CloudflareChallengeError: Detected a Cloudflare version 2 challenge, This feature is not available
in the opensource (free) version.
```

斷點: link_a = row.select_one('a')

```
len(row.select('div'))
11
len(row.select('div.l-listTable__td'))
4

row.select('div.l-listTable__td')[0].text
'\n\n\n外資買160億 台股登萬七\n\n\n\n\n'
row.select('div.l-listTable__td')[1].text
'\n\nCharlesPA\n\n2021-05-08 15:17\n'
row.select('div.l-listTable__td')[2].text
'\n\nCharlesPA\n\n2021-05-08 15:17\n'
row.select('div.l-listTable__td')[3].text
'\n0\n'
```


## week2

```
resp = requests.get('http://18.183.200.66/samples/sample1.html')
#print(resp.text)

soup = bs4.BeautifulSoup(resp.text, 'lxml')
```

```
soup.select('div')
[<div>[新聞] 阿中急命關機師重挫華...　衝擊晶</div>, <div>Re: [心得] 老實說傳產比...好操作吧</div>, <div>[標的] 2330. TW 多</div>, <div>[請益] 當沖的人是比較不擔心...或大漲？</div>, <div>[新聞] 誰想污名化股市？</div>, <div>[新聞] 美團、拼多多遭上海市... 要求摒</div>, <div>[標的] 2103 台橡 多</div>, <div>[心得] 2021/11/6。...達上35</div>, <div>[閒聊] 2021/05/11...盤中閒聊</div>, <div>[標的] 美股TSLA空</div>]
```

```
soup.select('div')[4]
<div>[新聞] 誰想污名化股市？</div>
```

```
soup.select('div')[-1]
<div>[標的] 美股TSLA空</div>
```

```
soup.select('div')[2:8]
[<div>[標的] 2330. TW 多</div>, <div>[請益] 當沖的人是比較不擔心...或大漲？</div>, <div>[新聞] 誰想污名化股市？</div>, <div>[新聞] 美團、拼多多遭上海市... 要求摒</div>, <div>[標的] 2103 台橡 多</div>, <div>[心得] 2021/11/6。...達上35</div>]
```


https://try.jsoup.org/ 可以用來測試 Select


jieba 詞彙區別套件

```
PS D:\ws\python-web-crawler> pip install jieba
Collecting jieba
  Downloading jieba-0.42.1.tar.gz (19.2 MB)
     |████████████████████████████████| 19.2 MB 1.7 MB/s
Building wheels for collected packages: jieba
  Building wheel for jieba (setup.py) ... done
  Created wheel for jieba: filename=jieba-0.42.1-py3-none-any.whl size=19314482 sha256=a51f9e081529765e58c52a0da70bcd53cfbed921c16c98e92ea65c172c32e0c9
  Stored in directory: c:\users\andrew\appdata\local\pip\cache\wheels\ca\38\d8\dfdfe73bec1d12026b30cb7ce8da650f3f0ea2cf155ea018ae
Successfully built jieba
Installing collected packages: jieba
Successfully installed jieba-0.42.1
PS D:\ws\python-web-crawler>
```

https://github.com/APCLab/jieba-tw


盤後零股交易行情單
TWT53U_ALLBUT0999_20210514.csv

="0050"  加 = 是為了讓 excel 打開後不會變成 50


## week3

PK: Primary Key
NN: Not NULL (一定要有值)
AI: Auto Increment (自動累加值)

SQL 語法:

* 不分大小寫
* 字串一定要用單引號，不可用雙引號
* SQL 的資料格式沒有日期，所以只能用文字格式。但若文字使用 iso 日期格式，SQL 還是能做某種程度的處理。

CRUD

### SQL 新增 (C)

```
INSERT INTO topic(title, issuer, created, keyworks)
          VALUES ('this is title', 'Andrew', '2021-07-03', NULL)
```

上面跟下面等效，只要欄位名稱順序跟value對應關係一樣即可。

```
INSERT INTO topic(created, title, issuer, keyworks)
          VALUES ('2021-07-03', 'this is title', 'Andrew', NULL)
```

一次新增多筆

```
INSERT INTO article(content, issuer, created, keywords)
          VALUES ('ABC', 'alice', '2021-07-04', NULL),
				 ('XYZ', 'zoe', '2021-07-04', NULL)
```

### SQL 查詢(R)


```
SELECT * FROM topic
```

```
SELECT * FROM topic
WHERE title='李紫彤'
```

```
SELECT title, issuer FROM topic
```

順序可換

```
SELECT issuer, title FROM topic
```

WHERE 用法

```
SELECT created, issuer, title FROM topic
WHERE created='2021-07-04'
```

```
SELECT created, issuer, title FROM topic
WHERE created >= '2021-07-04'
```

```
SELECT created, issuer, title FROM topic
WHERE created >= '2021-07-04' and created < '2021-08-03'
```

```
SELECT created, issuer, title FROM topic
WHERE (created >= '2021-07-04' and created < '2021-08-03') OR issuer = 'Alice'
```

```
SELECT created, issuer, title FROM topic
WHERE (created >= '2021-07-04' and created < '2021-08-03') AND issuer = 'Lu'
```

### SQL 註解

使用 `--`


### SQL 異動(U)

UPDATE 一定要加 WHERE，否則異動會套用到 '所有資料' !!!

```
UPDATE topic
	SET created='2021-07-02'
```

```
UPDATE topic
	SET created='2021-07-02'
	WHERE id=6
```

```
UPDATE topic
	SET created='2021-07-03', issuer='Lee', title='8AM'
	WHERE id=2
```

```
UPDATE topic
	SET issuer='Sabrina', title='時差書寫'
	WHERE created='2021-07-02' AND id=5
```

### SQL 刪除(D)

跟 update 一樣，建議一定要加 WHERE

更新和刪除測試時，盡量使用 PK(id) 測試。因為那至少只會限制在一個單一資料範圍內


```
DELETE FROM topic
	WHERE issuer='Zoe'
```

### 老師的設計經驗


* PK 可以使用複合欄位，意思是多個欄位組合成一個 PK。但實務上不建議這樣使用，可以建立一個索引值(index) -- 使用單一欄位當作 PK 會比較好。
* 建立一個欄位當作資料是否有被刪除。ex: deleted。刪除真正的意義是 "標註"，而不是真正的刪除。在一般的搜尋中，不會出現該筆資料。
	* 好處: 保存資料歷史。查詢時若資料遺失可能會影響查詢功能。
	* 壞處: 占空間
* 建議增加的欄位
	* 資料被建立的時間(包含時分秒)
	* created_user: 資料由誰建立的
	* 異動的時間
	* 異動的人員


資料表的欄位名稱可以改，但是資料類型修改可能會造成現有的資料損毀。

### Sqlite Datatype

https://www.sqlite.org/datatype3.html

* sqlite 不支援 boolean，但建議使用 integer 0 和 1
* 日期支援三種格式 (本質是字串，但 SQL 會將之視為日期格式)
	* **TEXT** as ISO8601 strings (`"YYYY-MM-DD HH:MM:SS.SSS"`).
	* **REAL** 
	* **INTEGER** as Unix Time 

### RDBMS 術語

* Master(有PK) <-- 關聯性 --> Detail(有FK, FK 對應 Master 的 PK)
* 參照完整性: 不允許引用不存在的實體
	* 發票刪除時，發票所對應的品項該如何處理參照?
		* 是否連動需要刪除品項?
		* 或是品項需要全部刪除才能刪除發票?
	* 早期需要自己寫程式處理，目前的 DB 都能夠自行處理這個部分
* 資料正規化
	* 去除重複的部分，拆成不同的表單
		* ex: 部門表單、員工表單
		* 一個部門下有多個員工 ==> 員工表單需要有 FK 來自部門表單


一對一關聯:
	* FK 對應 PK 也只會找到一筆。
	* 適合處理公開資料和隱私資料
一對多關聯:
	* 多個 FK 對應同一個 PK
	* 學生 --> 系所


ER Model:

* 一個顧客可以有多個訂單，但一個訂單只會屬於一個顧客
* [顧客 PK]-|-------o<[訂單 FK]



### 資料表合成產生報表

下兩次查詢，很不方便

```
SELECT * FROM topic WHERE id=1;
SELECT * FROM article WHERE topic_id=1;
```

使用 JOIN

```
SELECT * FROM topic
	JOIN article
```

PK(topic.id) --> FK(article.topic_id)

```
SELECT * FROM topic
	JOIN article ON topic.id=article.topic_id
```

```
SELECT * FROM topic
	JOIN article ON topic.id=article.topic_id
	WHERE topic.id=1
```


## week4

注意轉換字串的處理細節:

* SQL 語法的字串用單引號
* Json 語法的字串用雙引號

函數

* json.dump()
* json.dumps()
* json.load()
* json.loads()

轉換

* JSON 的 array 只能轉換 python 的 list
* JSON 的 object 只能轉換 python 的 dict

實作建議: 把資料表寫成 class 物件。可以另外寫在 models.py 中。

爬蟲寫資料的時候，需要判斷資料是否已經在 db 了。判斷依據是?
* 日期標題發佈人都一樣，表示已經存在了


insert DB 後，把 insert 資料的物件回傳? 用意:

```
    def isExistedTopic(self, topicObj):
        sql = "SELECT * FROM topic WHERE title=:sql_title AND issuer=:sql_issuer AND created=:sql_created"
        val = { 'sql_title':    topicObj.title,
                'sql_issuer':   topicObj.issuer,
                'sql_created':  topicObj.created }
        cur = self.connection.cursor()
        cur.execute(sql, val)
        results = cur.fetchall()
        cur.close()
        return None if len(results) == 0 
			else Topic(results[0][0],
				results[0][1],
				results[0][2],
				results[0][3],
				results[0][4])

    def insertTopic(self, topicObj):
        sql = "INSERT INTO topic(title, issuer, created, keywords) VALUES (:sql_title, :sql_issuer, :sql_created, :sql_keywords)"
        val = { 'sql_title':    topicObj.title,
                'sql_issuer':   topicObj.issuer,
                'sql_created':  topicObj.created,
                'sql_keywords': topicObj.keywords }
        cur = self.connection.cursor()
        cur.execute(sql, val)
        self.connection.commit()
        cur.close()
        return topicObj  # <== 這裡
```


```
tObj = Topic(0, 
	title, 
	issuer, 
	created, 
	None if len(keywords) == 0 else json.dumps(keywords, ensure_ascii=False))
```

```
tObj_new = db.isExistedTopic(tObj)
if tObj_new is None:
    tObj_new = db.insertTopic(tObj)
```

為了把上面三行寫成一行

``` 
tObj_new = db.isExistedTopic(tObj) or db.insertTopic(tObj)
```

F12 測試抓日期


```
# https://www.ptt.cc/bbs/Stock/M.1625885629.A.4E7.html

$('.article-meta-value')[3].innerText
"Sat Jul 10 10:53:46 2021"
```


```
PS D:\ws\python-web-crawler> pip install wordcloud
Collecting wordcloud
  Downloading wordcloud-1.8.1-cp38-cp38-win32.whl (145 kB)
     |████████████████████████████████| 145 kB 1.3 MB/s
Requirement already satisfied: pillow in c:\python38-32\lib\site-packages (from wordcloud) (8.0.1)
Requirement already satisfied: matplotlib in c:\python38-32\lib\site-packages (from wordcloud) (3.3.3)
Requirement already satisfied: numpy>=1.6.1 in c:\python38-32\lib\site-packages (from wordcloud) (1.19.4)
Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3 in c:\python38-32\lib\site-packages (from matplotlib->wordcloud) (2.4.7)
Requirement already satisfied: cycler>=0.10 in c:\python38-32\lib\site-packages (from matplotlib->wordcloud) (0.10.0)
Requirement already satisfied: python-dateutil>=2.1 in c:\python38-32\lib\site-packages (from matplotlib->wordcloud) (2.8.1)
Requirement already satisfied: kiwisolver>=1.0.1 in c:\python38-32\lib\site-packages (from matplotlib->wordcloud) (1.3.1)
Requirement already satisfied: six in c:\python38-32\lib\site-packages (from cycler>=0.10->matplotlib->wordcloud) (1.15.0)
Installing collected packages: wordcloud
Successfully installed wordcloud-1.8.1
WARNING: You are using pip version 21.1.1; however, version 21.1.3 is available.
You should consider upgrading via the 'c:\python38-32\python.exe -m pip install --upgrade pip' command.
PS D:\ws\python-web-crawler>
```


## Week5


```
pip install pandas
```


[台灣證券交易所](https://www.twse.com.tw/)太頻繁讀取會鎖定 ip，但是 [聚財網](https://stock.wearn.com/) 不會。所以從 台灣證券交易所讀取股票名稱和代號清單，然後用代號去聚財網撈資料回來分析。

```
<a href="/exchangeReport/BFT41U?response=csv&amp;date=20210716&amp;selectType=01" class="csv" data-et="盤後定價交易">CSV 下載</a>
```

```
https://www.twse.com.tw/exchangeReport/BFT41U?response=csv&date=20210401&selectType=0099P
```


```
import requests

url = 'https://www.twse.com.tw/exchangeReport/BFT41U?response=csv&date=20210716&selectType=ALLBUT0999'
resp = requests.get(url)
print(resp.text)
```

```
PS D:\ws\python-web-crawler> & c:/python38-32/python.exe d:/ws/python-web-crawler/week5/lab07_twse.py
"110年07月16日盤後定價交易"
"證券代號","證券名稱","成交數量","成交筆數","成交金額","成交價","最後揭示買量","最後揭示賣量",
="0050","元大台灣50","7","7","979,300","139.90","12","0",
="0051","元大中型100","0","0","0","59.00","1","0",
="0052","富邦科技","4","3","505,800","126.45","0","8",
="0053","元大電子","0","0","0","67.65","1","0",
="0054","元大台商50","0","0","0","32.67","0","0",
="0055","元大MSCI金融","1","1","22,360","22.36","0","1",
="0056","元大高股息","19","12","667,280","35.12","18","0",
="0057","富邦摩台","0","0","0","95.70","0","0",
="0061","元大寶滬深","0","0","0","23.58","0","0",
="006203","元大MSCI台灣","0","0","0","66.85","0","0",
="006204","永豐臺灣加權","0","0","0","94.10","0","0",
="006205","富邦上証","0","0","0","37.88","0","0",
="006206","元大上證50","0","0","0","37.32","0","0",
="006207","FH滬深","0","0","0","31.00","0","0",
="006208","富邦台50","0","0","0","80.15","8","0",
="00631L","元大台灣50正2","5","5","678,000","135.60","0","7",
="00632R","元大台灣50反1","251","31","1,365,440","5.44","10","0",
="00633L","富邦上証正2","4","4","254,400","63.60","0","2,572",
="00634R","富邦上証反1","0","0","0","3.91","20","0",
="00635U","期元大S&P黃金","0","0","0","24.43","0","0",
...
"9941","裕融","0","0","0","166.50","46","0",
"9941A","裕融甲特","0","0","0","51.50","0","0",
"9942","茂順","1","1","99,400","99.40","0","1",
"9943","好樂迪","0","0","0","65.70","1","0",
"9944","新麗","1","1","22,850","22.85","0","2",
"9945","潤泰新","191","36","12,529,600","65.60","33","0",
"9946","三發地產","0","0","0","14.75","0","1",
"9955","佳龍","1","1","18,700","18.70","2","0",
"9958","世紀鋼","3","3","384,000","128.00","24","0",
"　","合計","19,113","11,375","1,380,324,570","","77,232","54,752",
"說明:"
"除境外指數股票型基金及外國股票第二上市外，餘交易單位皆為千股。"
"成交及最後揭示欄位無內容表示無成交、無委託或暫停交易(僅存託憑證及認購(售)權證有暫停交易機制)。"
"暫停交易證券明細可連結
基本市況報導網站
「五檔揭示」查詢。"
"ETF證券代號第六碼為K、M、S、C者，表示該ETF以外幣交易。"
"不加計外幣交易證券交易金額。"
```


## Week6


從 stock 把 stock_name 關連到 stock_history 中

```
SELECT stock_history.stock_id, stock_name, trad_date, open_price, high_price, low_price, close_price, total_volume 
FROM stock_history
JOIN stock ON stock.stock_id == stock_history.stock_id
```

```
SELECT stock_history.stock_id, stock_name, trad_date, open_price, high_price, low_price, close_price, total_volume 
FROM stock_history
JOIN stock ON stock.stock_id == stock_history.stock_id
WHERE stock_history.stock_id = '4906' AND trad_date >= '2021-07-10' AND trad_date <= '2021-07-20'
```

```
PS D:\ws\python-web-crawler> pip install bar_chart_race
Collecting bar_chart_race
  Downloading bar_chart_race-0.1.0-py3-none-any.whl (156 kB)
     |████████████████████████████████| 156 kB 1.3 MB/s
Requirement already satisfied: matplotlib>=3.1 in c:\python38-32\lib\site-packages (from bar_chart_race) (3.3.3)
Requirement already satisfied: pandas>=0.24 in c:\python38-32\lib\site-packages (from bar_chart_race) (1.3.0)
Requirement already satisfied: cycler>=0.10 in c:\python38-32\lib\site-packages (from matplotlib>=3.1->bar_chart_race) (0.10.0)
Requirement already satisfied: numpy>=1.15 in c:\python38-32\lib\site-packages (from matplotlib>=3.1->bar_chart_race) (1.19.4)
Requirement already satisfied: kiwisolver>=1.0.1 in c:\python38-32\lib\site-packages (from matplotlib>=3.1->bar_chart_race) (1.3.1)
Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3 in c:\python38-32\lib\site-packages (from matplotlib>=3.1->bar_chart_race) (2.4.7)
Requirement already satisfied: pillow>=6.2.0 in c:\python38-32\lib\site-packages (from matplotlib>=3.1->bar_chart_race) (8.0.1)
Requirement already satisfied: python-dateutil>=2.1 in c:\python38-32\lib\site-packages (from matplotlib>=3.1->bar_chart_race) (2.8.1)
Requirement already satisfied: six in c:\python38-32\lib\site-packages (from cycler>=0.10->matplotlib>=3.1->bar_chart_race) (1.15.0)
Requirement already satisfied: pytz>=2017.3 in c:\python38-32\lib\site-packages (from pandas>=0.24->bar_chart_race) (2020.1)
Installing collected packages: bar-chart-race
Successfully installed bar-chart-race-0.1.0
WARNING: You are using pip version 21.1.1; however, version 21.1.3 is available.
You should consider upgrading via the 'c:\python38-32\python.exe -m pip install --upgrade pip' command.
PS D:\ws\python-web-crawler>
```


## Week7


處理需要登入的頁面:

* Cookie
	* server 送給 client (browser) 的一小段資料 (幾KB)
	* 追蹤使用者的行為
	* key-value pair
* Session
* From


### Cookie

F12 > Applications > 左側 Cookies > 

* Http Only 是後端才能修改的，前端無法更動
* Expires 時間標明 session 表示瀏覽器關閉 cookie 就消失
* 許多瀏覽器都會限制 Cookie


### Session

* Session 裡面的 key 也是存在 cookie 裡面
	* cookie 能不能被使用是瀏覽器設定的
* 紀錄是誰 request
* 流程
	* server 產生 sesssion (server 端的記憶體)，回傳 sessionID 並放在 cookie 回給 client
	* client request 時，帶入 sessionID 給 server
	* server 用 sessionID 反查 session 裡的資料


Cookie 和 Session 的差異似乎在於 -- 真正的敏感資料放在哪?

* Cookie: client 端
* Session: server 端

比較新的技術會使用 jwt 取代 Cookie-Session 機制


* session_req = request.session()
* result = session_req.get(LOGIN_URL)



```
<form class="_9vtf" data-testid="royal_login_form" 
	action="/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjI3Njk2NDg2LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D" 
	method="post" onsubmit="" id="u_0_i_q2">

	<input type="hidden" name="jazoest" value="2850" autocomplete="off">
	<input type="hidden" name="lsd" value="AVoY36mAANM" autocomplete="off">

	<input type="text" class="inputtext _55r1 _6luy" name="email" id="email" data-testid="royal_email" 
		placeholder="電子郵件地址或手機號碼" autofocus="1" aria-label="電子郵件地址或手機號碼">

	<input type="password" class="inputtext _55r1 _6luy _9npi" name="pass" id="pass" 
		data-testid="royal_pass" placeholder="密碼" aria-label="密碼">

	<input type="hidden" autocomplete="off" name="login_source" value="comet_headerless_login">
	<input type="hidden" autocomplete="off" name="next" value="">

	<button value="1" class="_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy" name="login" data-testid="royal_login_button" 
		type="submit" id="u_0_l_Ix">登入</button>

	<a href="https://www.facebook.com/recover/initiate/?ars=facebook_login&amp;privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjI3Njk2NDg2LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D">忘記密碼？</a>

	<a role="button" class="_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy" href="#" ajaxify="/reg/spotlight/" id="u_0_2_ow" data-testid="open-registration-form-button" rel="async">建立新帳號</a>
</form>
```


![](images/fb.png)


### XPath

* xml 的根節點標籤只能有一個，補不可重複
* xml 標籤大小寫有區別
* css 的搜尋方式叫做 selector，而 xml 就稱為 Xpath
	* 使用 Xpath 選擇: 查詢 xml 格式


測試: http://xpather.com/

```
<?xml version="1.0" encoding="UTF-8"?>

<bookstore>

    <book category="cooking">
        <title lang="en">Everyday Italian</title>
        <author>Giada De Laurentiis</author>
        <year>2005</year>
        <price>30.00</price>
    </book>

    <book category="children">
        <title lang="en">Harry Potter</title>
        <author>J K. Rowling</author>
        <year>2005</year>
        <price>29.99</price>
    </book>

    <book category="web">
        <title lang="en">XQuery Kick Start</title>
        <author>James McGovern</author>
        <author>Per Bothner</author>
        <author>Kurt Cagle</author>
        <author>James Linn</author>
        <author>Vaidyanathan Nagarajan</author>
        <year>2003</year>
        <price>49.99</price>
    </book>

    <book category="web">
        <title lang="en">Learning XML</title>
        <author>Erik T. Ray</author>
        <year>2003</year>
        <price>39.95</price>
    </book>

</bookstore>
```

取到第一本書的作者，index 是從 1 開始。

* `//book[1]/author`
* `/bookstore/book[1]/author`
* 上面兩種的結果都是: Giada De Laurentiis，差別在是不是從根結點開始
* 使用 @ 取得屬性。第三本書的 category: `//book[3]/@category` ==> 結果: web
* 第三本書的第一位作者: `//book[3]/author[1]`
* 最後一本書: `//book[last()]`
* 倒數第二本: `//book[last()-1]`

這裡可以查所有 xpath functions: https://way2tutorial.com/xml/xpath-functions.php


* 前兩本書: `//book[position()<3]`
* 前三本書: `//book[position()<=3]`
* web 類的書籍: `//book[@category="web"]`
* 所有 lang = en 的書: `//book/title[@lang="en"]` 或 `//title[@lang="en"]`
* 價格大於 35 的書: `//book[price>35]`
* 價格大於 35 的第二本: `//book[price>35][2]`
* 價格大於 35 的書標題: `//book[price>35]/title`
* 列出書本標題和價格: `//book/title | //book/price`
* 價格區間: `//book[price >= 30 and price < 40]`
* 屬性選擇: `//book[@category="web" or @category="cooking"]`


**xpath_axes:**

w3schools 文件: https://www.w3schools.com/xml/xpath_axes.asp

Examples 的內容前面加 // 就可以測試，ex:


`//ancestor::book//child::text()`

```

Everyday Italian
Giada De Laurentiis
2005
30.00
Harry Potter
J K. Rowling
2005
29.99
XQuery Kick Start
James McGovern
Per Bothner
Kurt Cagle
James Linn
Vaidyanathan Nagarajan
2003
49.99
Learning XML
Erik T. Ray
2003
39.95
```

F12 console 測試 fb 登入頁:

* `$x("//input[@name='email']")`
* `$x('//form/input[@name="lsd"]/attribute::value')[0].value` ==> "AVoY36mAh48"
* `$x('//form//input[@name="email"]')[0].value` ==> "dyuamdl@yahoo.com.tw"
* `$x('//form//input[@name="pass"]')[0].value`


### selenium

single page app 已經被大量使用，因為一次載入部分 page 而 python 無法呼叫 javescript 的 function。所以以前的 request 的方式就變得無法使用。

selenium 的做法就是模擬人的使用情況，把瀏覽器載入，並且執行網頁的 javascript 程式。


```
PS D:\ws\python-web-crawler> pip install selenium
Collecting selenium
  Downloading selenium-3.141.0-py2.py3-none-any.whl (904 kB)
     |████████████████████████████████| 904 kB 1.6 MB/s
Requirement already satisfied: urllib3 in c:\python38-32\lib\site-packages (from selenium) (1.26.2)
Installing collected packages: selenium
Successfully installed selenium-3.141.0
WARNING: You are using pip version 21.1.1; however, version 21.1.3 is available.
You should consider upgrading via the 'c:\python38-32\python.exe -m pip install --upgrade pip' command.
PS D:\ws\python-web-crawler>
```

因為 selenium 會載入瀏覽器，所以需要針對個別瀏覽器安裝 webdriver


* https://www.selenium.dev/documentation/en/webdriver/ 
* https://pypi.org/project/selenium/
* [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
	* 版本 92.0.4515.107 (正式版本) (64 位元)

```
D:\ws\python-web-crawler\week7
λ .\chromedriver.exe --help
Usage: .\chromedriver.exe [OPTIONS]

Options
  --port=PORT                     port to listen on
  --adb-port=PORT                 adb server port
  --log-path=FILE                 write server log to file instead of stderr, increases log level to INFO
  --log-level=LEVEL               set log level: ALL, DEBUG, INFO, WARNING, SEVERE, OFF
  --verbose                       log verbosely (equivalent to --log-level=ALL)
  --silent                        log nothing (equivalent to --log-level=OFF)
  --append-log                    append log file instead of rewriting
  --replayable                    (experimental) log verbosely and don't truncate long strings so that the log can be replayed.
  --version                       print the version number and exit
  --url-base                      base URL path prefix for commands, e.g. wd/url
  --readable-timestamp            add readable timestamps to log
  --enable-chrome-logs            show logs from the browser (overrides other logging options)
  --allowed-ips                   comma-separated allowlist of remote IP addresses which are allowed to connect to ChromeDriver

D:\ws\python-web-crawler\week7
```

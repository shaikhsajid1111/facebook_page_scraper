<h1> Facebook Page Scraper </h1>

[![Maintenance](https://img.shields.io/badge/Maintained-Yes-green.svg)](https://github.com/shaikhsajid1111/facebook_page_scraper/graphs/commit-activity)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://opensource.org/licenses/MIT) [![Python >=3.6.9](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-360/)

<p> No need of API key, No limitation on number of requests. Import the library and <b> Just Do It !<b> </p>

<!--TABLE of contents-->
<h2> Table of Contents </h2>
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#">Getting Started</a>
      <ul>
        <li><a href="#Prerequisites">Prerequisites</a></li>
        <li><a href="#Installation">Installation</a>
        <ul>
        <li><a href="#sourceInstallation">Installing from source</a></li>
        <li><a href="#pypiInstallation">Installing with PyPI</a></li>
        </ul>
        </li>
      </ul>
    </li>
    <li><a href="#Usage">Usage</a></li>
    <ul>
    <li><a href="#instantiation">How to instantiate?</a></li>
    <ul>
    <li><a href="#scraperParameters">Parameters for <code>Facebook_scraper()</code></a></li>
    <li><a href="#JSONWay">Scrape in JSON format</a>
    <ul><li><a href="#jsonOutput">JSON Output Format</a></li></ul>
    </li>
    <li><a href="#CSVWay">Scrape in CSV format</a>
    <ul><li><a href="#csvParameter">Parameters for scrape_to_csv() method</a></li></ul>
    </li>
    <li><a href="#outputKeys">Keys of the output data</a></li>
    </ul>
    </ul>
    <li><a href="#tech">Tech</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!--TABLE of contents //-->

<h2 id="Prerequisites"> Prerequisites </h2>

- Internet Connection
- Python 3.7+
- Chrome or Firefox browser installed on your machine
<br>

<hr>
<h2 id="Installation">Installation:</h2>

<h3 id="sourceInstallation"> Installing from source: </h3>

```
git clone https://github.com/shaikhsajid1111/facebook_page_scraper
```

<h4> Inside project's directory </h4>

```
python3 setup.py install
```
<br>
<p id="pypiInstallation">Installing with pypi</p>

```
pip3 install facebook-page-scraper
```
<br>
<hr>
<h2 id="instantiation"> How to use? </h2>



```python
#import Facebook_scraper class from facebook_page_scraper
from facebook_page_scraper import Facebook_scraper

#instantiate the Facebook_scraper class

page_name = "metaai"
posts_count = 10
browser = "firefox"
proxy = "IP:PORT" #if proxy requires authentication then user:password@IP:PORT
timeout = 600 #600 seconds
headless = True
meta_ai = Facebook_scraper(page_name, posts_count, browser, proxy=proxy, timeout=timeout, headless=headless)

```

<h3 id="scraperParameters"> Parameters for  <code>Facebook_scraper(page_name, posts_count, browser, proxy, timeout, headless) </code> class </h3>
<table>
<th>
<tr>
<td> Parameter Name </td>
<td> Parameter Type </td>
<td> Description </td>
</tr>
</th>

<tr>
<td>
page_name
</td>
<td>
String
</td>
<td>
Name of the facebook page
</td>
</tr>

<tr>
<td>
posts_count
</td>
<td>
Integer
</td>
<td>
Number of posts to scrap, if not passed default is 10
</td>
</tr>

<tr>
<td>
browser
</td>
<td>
String
</td>
<td>
Which browser to use, either chrome or firefox. if not passed,default is chrome
</td>
</tr>

<tr>
<td>
proxy(optional)
</td>
<td>
String
</td>
<td>
Optional argument, if user wants to set proxy, if proxy requires authentication then the format will be <code> user:password@IP:PORT </code>
</td>
</tr>
<tr>
<td>
timeout
</td>
<td>
Integer
</td>
<td>
The maximum amount of time the bot should run for. If not passed, the default timeout is set to 10 minutes
 </code>
</td>
</tr>
<tr>
<td>
headless
</td>
<td>
Boolean
</td>
<td>
Whether to run browser in headless mode?. Default is True
 </code>
</td>
</tr>


</table>
<br>
<hr>
<br>

<h3> Done with instantiation?. <b>Let the scraping begin!</b> </h3>
<br

>
<h3 id="JSONWay"> For post's data in <b>JSON</b> format:</h3>

```python
#call the scrap_to_json() method

json_data = meta_ai.scrap_to_json()
print(json_data)

```

Output:

```javascript

{
  "2024182624425347": {
    "name": "Meta AI",
    "shares": 0,
    "reactions": {
      "likes": 154,
      "loves": 19,
      "wow": 0,
      "cares": 0,
      "sad": 0,
      "angry": 0,
      "haha": 0
    },
    "reaction_count": 173,
    "comments": 2,
    "content": "We’ve built data2vec, the first general high-performance self-supervised algorithm for speech, vision, and text. We applied it to different modalities and found it matches or outperforms the best self-supervised algorithms. We hope this brings us closer to a world where computers can learn to solve many different tasks without supervision. Learn more and get the code:  https://ai.facebook.com/…/the-first-high-performance-self-s…",
    "posted_on": "2022-01-20T22:43:35",
    "video": [],
    "image": [
      "https://scontent-bom1-2.xx.fbcdn.net/v/t39.30808-6/s480x480/272147088_2024182621092014_6532581039236849529_n.jpg?_nc_cat=100&ccb=1-5&_nc_sid=8024bb&_nc_ohc=j4_1PAndJTIAX82OLNq&_nc_ht=scontent-bom1-2.xx&oh=00_AT9us__TvC9eYBqRyQEwEtYSit9r2UKYg0gFoRK7Efrhyw&oe=61F17B71"
    ],
    "post_url": "https://www.facebook.com/MetaAI/photos/a.360372474139712/2024182624425347/?type=3&__xts__%5B0%5D=68.ARBoSaQ-pAC_ApucZNHZ6R-BI3YUSjH4sXsfdZRQ2zZFOwgWGhjt6dmg0VOcmGCLhSFyXpecOY9g1A94vrzU_T-GtYFagqDkJjHuhoyPW2vnkn7fvfzx-ql7fsBYxL5DgQVSsiC1cPoycdCvHmi6BV5Sc4fKADdgDhdFvVvr-ttzXG1ng2DbLzU-XfSes7SAnrPs-gxjODPKJ7AdqkqkSQJ4HrsLgxMgcLFdCsE6feWL7rXjptVWegMVMthhJNVqO0JHu986XBfKKqB60aBFvyAzTSEwJD6o72GtnyzQ-BcH7JxmLtb2_A&__tn__=-R"
  }, ...

}
```
<div id="jsonOutput">
Output Structure for JSON format:


``` javascript
{
    "id": {
        "name": string,
        "shares": integer,
        "reactions": {
            "likes": integer,
            "loves": integer,
            "wow": integer,
            "cares": integer,
            "sad": integer,
            "angry": integer,
            "haha": integer
        },
        "reaction_count": integer,
        "comments": integer,
        "content": string,
        "video" : list,
        "image" : list,
        "posted_on": datetime,  //string containing datetime in ISO 8601
        "post_url": string
    }
}

```
</div>
<br>
<hr>
<br>

<h3 id="CSVWay"> For saving post's data directly to <b>CSV</b> file</h3>

``` python
#call scrap_to_csv(filename,directory) method


filename = "data_file"  #file name without CSV extension,where data will be saved
directory = "E:\data" #directory where CSV file will be saved
meta_ai.scrap_to_csv(filename, directory)

```

content of ```data_file.csv```:
```csv
id,name,shares,likes,loves,wow,cares,sad,angry,haha,reactions_count,comments,content,posted_on,video,image,post_url
2024182624425347,Meta AI,0,154,19,0,0,0,0,0,173,2,"We’ve built data2vec, the first general high-performance self-supervised algorithm for speech, vision, and text. We applied it to different modalities and found it matches or outperforms the best self-supervised algorithms. We hope this brings us closer to a world where computers can learn to solve many different tasks without supervision. Learn more and get the code:  https://ai.facebook.com/…/the-first-high-performance-self-s…",2022-01-20T22:43:35,,https://scontent-bom1-2.xx.fbcdn.net/v/t39.30808-6/s480x480/272147088_2024182621092014_6532581039236849529_n.jpg?_nc_cat=100&ccb=1-5&_nc_sid=8024bb&_nc_ohc=j4_1PAndJTIAX82OLNq&_nc_ht=scontent-bom1-2.xx&oh=00_AT9us__TvC9eYBqRyQEwEtYSit9r2UKYg0gFoRK7Efrhyw&oe=61F17B71,https://www.facebook.com/MetaAI/photos/a.360372474139712/2024182624425347/?type=3&__xts__%5B0%5D=68.ARAse4eiZmZQDOZumNZEDR0tQkE5B6g50K6S66JJPccb-KaWJWg6Yz4v19BQFSZRMd04MeBmV24VqvqMB3oyjAwMDJUtpmgkMiITtSP8HOgy8QEx_vFlq1j-UEImZkzeEgSAJYINndnR5aSQn0GUwL54L3x2BsxEqL1lElL7SnHfTVvIFUDyNfAqUWIsXrkI8X5KjoDchUj7aHRga1HB5EE0x60dZcHogUMb1sJDRmKCcx8xisRgk5XzdZKCQDDdEkUqN-Ch9_NYTMtxlchz1KfR0w9wRt8y9l7E7BNhfLrmm4qyxo-ZpA&__tn__=-R
...
```

<br>

<hr>
<br>

<h3 id="csvParameter"> Parameters for  <code> scrap_to_csv(filename, directory) </code> method. </h3>

<table>
<th>
<tr>
<td> Parameter Name </td>
<td> Parameter Type </td>
<td> Description </td>
</tr>
</th>

<tr>
<td>
filename
</td>
<td>
String
</td>

<td>
Name of the CSV file where post's data will be saved
</td>

</tr>

<tr>
<td>
directory
</td>
<td>
String
</td>

<td>
Directory where CSV file have to be stored.
</td>

</tr>

</table>

<br>
<hr>
<br>



<h3 id="outputKeys">Keys of the outputs:</h3>
<table>
<th>
<tr>

<td>
Key
</td>



<td>
Type
</td>

<td>
Description
</td>

<tr>
</th>


<td>
<tr>

<td>
id
</td>
<td>
String
</td>
<td>
Post Identifier(integer casted inside string)
</td>
</tr>

</td>

<tr>
<td>
name
</td>
<td>
String
</td>
<td>
Name of the page
</td>
</tr>

<tr>
<td>
shares
</td>
<td>
Integer
</td>
<td>
Share count of post
</td>
</tr>

<tr>
<td>
reactions
</td>
<td>
Dictionary
</td>
<td>
Dictionary containing reactions as keys and its count as value. Keys => <code> ["likes","loves","wow","cares","sad","angry","haha"] </code>
</td>
</tr>

<tr>
<td>
reaction_count
</td>
<td>
Integer
</td>
<td>
Total reaction count of post
</td>
</tr>


<tr>
<td>
comments
</td>
<td>
Integer
</td>
<td>
Comments count of post
</td>
</tr>

<tr>
<td>
content
</td>
<td>
 String
</td>
<td>
Content of post as text
</td>
</tr>

<tr>
<td>
video
</td>
<td>
 List
</td>
<td>
URLs of video present in that post
</td>
</tr>


<tr>
<td>
image
</td>
<td>
 List
</td>
<td>
List containing URLs of all images present in the post
</td>
</tr>

<tr>
<td>
posted_on
</td>
<td>
Datetime
</td>
<td>
Time at which post was posted(in ISO 8601 format)
</td>
</tr>

<tr>
<td>
post_url
</td>
<td>
String
</td>
<td>
URL for that post
</td>
</tr>


</table>
<br>

<hr>
<h2 id="tech"> Tech </h2>
<p>This project uses different libraries to work properly.</p>
<ul>
<li> <a href="https://www.selenium.dev/" target='_blank'>Selenium</a></li>
<li> <a href="https://pypi.org/project/webdriver-manager/" target='_blank'>Webdriver Manager</a></li>
<li> <a href="https://pypi.org/project/python-dateutil/" target='_blank'>Python Dateutil</a></li>
<li> <a href="https://pypi.org/project/selenium-wire/" target='_blank'>Selenium-wire</a></li>
</ul>
<br>

<hr>
If you encounter anything unusual please feel free to create issue <a href='https://github.com/shaikhsajid1111/facebook_page_scraper/issues'>here</a>
<hr>

<h2 id="license"> LICENSE </h2>
MIT

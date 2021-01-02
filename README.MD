<h1> Facebook Page Scraper </h1>

[![Maintenance](https://img.shields.io/badge/Maintained-Yes-green.svg)](https://github.com/shaikhsajid1111/facebook_page_scraper/graphs/commit-activity)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://opensource.org/licenses/MIT) [![Python >=3.6.9](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/)

<p> No registration, No need of API key, No limitation on number of requests. Import the library and <b> Just Do It !<b> </p>

<h2> Prerequisites </h2>

- Internet Connection
- Python 3.6+
- Chrome or Firefox browser installed on your machine
<br>

<hr>
<h2>Installation:</h2>

<h3> Installing from source: </h3>

```
git clone https://github.com/shaikhsajid1111/facebook_page_scraper 
```

<h4> Inside project's directory </h4>

```
python3 setup.py install
```
<br>
<p>Installing with pypi</p>

```
pip3 install facebook-page-scraper
```
<br>
<hr>
<h2> How to use? </h2>



```python
#import Facebook_scraper class from facebook_page_scraper
from facebook_page_scraper import Facebook_scraper

#instantiate the Facebook_scraper class

page_name = "facebookai"
posts_count = 10
browser = "firefox"

facebook_ai = Facebook_scraper(page_name,posts_count,browser)

```

<h3> Parameters for  <code>Facebook_scraper(page_name,posts_count,browser) </code> class </h3>
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
string
</td>
<td>
name of the facebook page
</td>
</tr>

<tr>
<td>
posts_count
</td>
<td>
integer
</td>
<td>
number of posts to scrap, if not passed default is 10
</td>
</tr>

<tr>
<td>
browser
</td>
<td>
string
</td>
<td>
which browser to use, either chrome or firefox. if not passed,default is chrome
</td>
</tr>

</table>
<br>
<hr>
<br>

<h3> Done with instantiation?. <b>Let the scraping begin!</b> </h3>
<br

>
<h3> For post's data in <b>JSON</b> format:</h3>

```python
#call the scrap_to_json() method

json_data = facebook_ai.scrap_to_json()
print(json_data)

```
Output:
```javascript

{
    "1730063790503900": {
        "name": "Facebook AI",
        "shares": 65,
        "reactions": {
            "likes": 305,
            "loves": 31,
            "wow": 7,
            "cares": 0,
            "sad": 0,
            "angry": 0,
            "haha": 0
        },
        "reaction_count": 343,
        "comments": 11,
        "content": "We\u2019re training computer vision models that leverage Transformers, a deep neural network architecture. Data-efficient image Transformers (DeiT) use less data and computing resources to produce high-performance image classification AI models.  We hope to advance the field of computer vision by sharing this work with the broader community, making large-scale systems that train AI models more accessible to researchers and engineers.",
        "posted_on": "2020-12-24T04:05:27",
        "video": "",
        "image": [
            "https://scontent-bom1-2.xx.fbcdn.net/v/t39.2365-6/p540x282/131570013_988138305044034_3894567585410559092_n.png?_nc_cat=109&ccb=2&_nc_sid=eaa83b&_nc_ohc=mAeDelparrEAX-3Mk7E&_nc_ht=scontent-bom1-2.xx&_nc_tp=30&oh=3fedb0e3cea6ad6f934ca20f77bec624&oe=600CB4C9"
        ],
        "post_url": "https://www.facebook.com/facebookai/posts/1730063790503900"
    },    ...

}


```
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
        "video" : string,
        "image" : list,
        "posted_on": datetime,  //string containing datetime in ISO 8601
        "post_url": string
    }
}

```

<br>
<hr>
<br>

<h3> For saving post's data directly to <b>CSV</b> file</h3>

``` python
#call scrap_to_csv(filename,directory) method


filename = "data_file"  #file name without CSV extension,where data will be saved
directory = "E:\data" #directory where CSV file will be saved
facebook_ai.scrap_to_csv(filename,directory)

```

content of ```data_file.csv```:
```csv
id,name,shares,likes,loves,wow,cares,sad,angry,haha,reactions_count,comments,content,video,image,post_url
1730063790503900,Facebook AI,62,295,30,6,0,0,0,0,331,10,"We�re training computer vision models that leverage Transformers, a deep neural network architecture. Data-efficient image Transformers (DeiT) use less data and computing resources to produce high-performance image classification AI models.  We hope to advance the field of computer vision by sharing this work with the broader community, making large-scale systems that train AI models more accessible to researchers and engineers.",,https://scontent-bom1-2.xx.fbcdn.net/v/t39.2365-6/p540x282/131570013_988138305044034_3894567585410559092_n.png?_nc_cat=109&ccb=2&_nc_sid=eaa83b&_nc_ohc=mAeDelparrEAX9CTY7c&_nc_ht=scontent-bom1-2.xx&_nc_tp=30&oh=c54502f6b0d2063cf455d88d20fe8c57&oe=600CB4C9,https://www.facebook.com/facebookai/posts/1730063790503900

...
```

<br>

<hr>
<br>

<h3> Parameters for  <code> scrap_to_csv(filename,directory) </code> method. </h3>

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
string
</td>

<td>
name of the CSV file where post's data will be saved
</td>

</tr>

<tr>
<td>
directory
</td>
<td>
string
</td>

<td>
directory where CSV file have to be stored.
</td>

</tr>

</table>

<br>
<hr>
<br>



<h3>Keys of the outputs:</h3>
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
string
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
string
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
integer
</td>
<td>
share count of post
</td>
</tr>

<tr>
<td>
reactions
</td>
<td>
dictionary
</td>
<td>
dictionary containing reactions as keys and its count as value. Keys => <code> ["likes","loves","wow","cares","sad","angry","haha"] </code> 
</td>
</tr>

<tr>
<td>
reaction_count
</td>
<td>
integer
</td>
<td>
total reaction count of post
</td>
</tr>


<tr>
<td>
comments
</td>
<td>
integer
</td>
<td>
comments count of post
</td>
</tr>

<tr>
<td>
content
</td>
<td>
 string
</td>
<td>
content of post as text
</td>
</tr>

<tr>
<td>
video
</td>
<td>
 string
</td>
<td>
URL of video present in that post
</td>
</tr>


<tr>
<td>
image
</td>
<td>
 list
</td>
<td>
python's list containing URLs of all images present in the post
</td>
</tr>

<tr>
<td>
posted_on
</td>
<td>
datetime
</td>
<td>
time at which post was posted(in ISO 8601 format)
</td>
</tr>

<tr>
<td>
post_url
</td>
<td>
string
</td>
<td>
URL for that post
</td>
</tr>


</table>
<br>
<hr>
<h2> Privacy </h2>

<p> This scraper only scrapes public data available to unauthenticated user and does not holds the capability to scrap anything private. </p>

<br>
<hr>
<h2> Tech </h2>
<p>This project uses different libraries to work properly.</p>
<ul>
<li> <a href="https://www.selenium.dev/" target='_blank'>selenium</a>
<li> <a href="https://pypi.org/project/webdriver-manager/" target='_blank'>webdriver manager</a>
</ul>
<br>
<hr>


<h2> LICENSE </h2>
MIT

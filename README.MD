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
    "1739843239525955": {
        "name": "Facebook AI",
        "shares": 43,
        "reactions": {
            "likes": 129,
            "loves": 11,
            "wow": 8,
            "cares": 0,
            "sad": 0,
            "angry": 0,
            "haha": 0
        },
        "reaction_count": 148,
        "comments": 3,
        "content": "We’re transitioning the Visdom project to the team at FOSSASIA. Visdom is a flexible tool for creating, organizing, and sharing visualizations of live, rich data. It aims to facilitate visualization of remote data with an emphasis on supporting scientific experimentation. We’re excited to see where the team, in collaboration with the developer and user community, take the project.",
        "posted_on": "2021-01-05T17:22:54",
        "video": "https://www.facebook.com/facebookai/videos/1739843239525955",
        "image": [
            "https://scontent-bom1-2.xx.fbcdn.net/v/t1.0-0/s526x296/135871741_1739843246192621_8564947121610203331_o.png?_nc_cat=108&ccb=2&_nc_sid=da1649&_nc_ohc=Hk7peLe8e-cAX_xLejp&_nc_ht=scontent-bom1-2.xx&_nc_tp=30&oh=856a17109cbc4a6657dbb68564dfc568&oe=60291FC7"
        ],
        "post_url": "https://www.facebook.com/facebookai/posts/1739843239525955"
    }, ...

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
id,name,shares,likes,loves,wow,cares,sad,angry,haha,reactions_count,comments,content,posted_on,video,image,post_url
1791700921006853,Facebook AI,45,150,19,5,0,0,0,0,174,8,"Facebook AI has built TimeSformer, an entirely new architecture for video understanding. It’s the first that’s based exclusively on the self-attention mechanism used in Transformers.  TimeSformer outperforms the state of the art while being more efficient than 3D ConvNets for video.",2021-03-15T17:14:30,,https://scontent-bom1-2.xx.fbcdn.net/v/t39.2365-6/p540x282/156274680_471569777206221_706631440205169419_n.jpg?_nc_cat=110&ccb=1-3&_nc_sid=eaa83b&_nc_ohc=eyfETEUuHzQAX8DqwMU&_nc_ht=scontent-bom1-2.xx&tp=6&oh=2e9c6490fe3ad19a398905b3b615c88b&oe=6075FFE4,https://www.facebook.com/FacebookAI/posts/1791700921006853?__xts__%5B0%5D=68.ARCfsjOoZa0yc0TPws1koBr9ezS44Xf6Up04CqOhWnoDqrO35NdIdgjNSTWBrsUtm_y7MamZTjc_-p2rTobXe5WvxWd_eywuSzt98B7Vaj5hobF4OTZhe7VRgVJJY1wxEeAJf4nCZSs1tF1gWJJ0s5pPUGMmJsfD1UM5a3eERo-2t1JnTBHOSYs9Xsj5fV0iL-FiWAms_2-9KNRGqoojg9KfSAlffh_qxL8ztgznqC1sxfcU6MwAqdPN2va_T8cez29ZvJ1Er1j26VR7pnpWGyTMuW5wMrNxC-pz_8pVls8uk0iDramIOA&__tn__=-R
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
If you encounter anything unusual please feel free to create issue <a href='https://github.com/shaikhsajid1111/facebook_page_scraper/issues'>here</a>
<hr>

<h2> LICENSE </h2>
MIT

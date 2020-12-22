<h1> Facebook Page Scraper </h1>

[![Maintenance](https://img.shields.io/badge/Maintained-Yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) [![Python >=3.6.9](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-376/)

<p> No registration, No need of API key, No limitation on number of requests. Import the library and <b> Just Do It !<b> </p>

<h2> Prerequisites </h2>

- Internet Connection
- Python 3.6+

<h2> How to use? </h2>



```python
Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

>>> #import Facebook_scraper class from the package
>>> from facebook_page_scraper import Facebook_scraper
>>>
>>> #instantiate the class with parameters
>>> scraper = Facebook_scraper("facebookai",20,"firefox")
>>>
>>> #call the scrap() method 
>>> posts_data = scraper.scrap()
>>>
>>> print(type(posts_data))
<class 'dict'>
>>>
>>> print(posts_data)
{
    "1719932218183724": {
        "name": "Facebook AI",
        "shares": 32,
        "reactions": {
            "likes": 171,
            "loves": 15,
            "wow": 0,
            "cares": 0,
            "sad": 0,
            "angry": 0,
            "haha": 27
        },
        "reaction_count": 213,
        "comments": 11,
        "content": "Hate speech can come in many forms, including memes that combine text and images. We launched the Hateful Memes Challenge, a first-of-its-kind competition, to help the AI community find new ways to detect multimodal hate speech. Learn about the winners here: https://ai.facebook.com/blog/hateful-memes-challenge-winners",
        "posted_on": "Friday, 11 December 2020 at 09:15",
        "post_url": "https://www.facebook.com/facebookai/posts/1719932218183724"
    }, ...
}
```

<h3> Parameters </h3>
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

<hr>
<br>
<br>
Output Structure:

It returns a dictionary of dictionaries containing post's details.

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
        "posted_on": datetime,  //string containing datetime
        "post_url": string
    }
}

```


Keys of the dictionary:
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
posted_on
</td>
<td>
datetime
</td>
<td>
time at which post was posted
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
<li> <a href="https://www.selenium.dev/">selenium</a>
<li> <a href="https://pypi.org/project/webdriver-manager/">webdriver manager</a>
</ul>
<br>
<hr>


<h2> LICENSE </h2>
MIT
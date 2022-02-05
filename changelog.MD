<h1> Changelog </h1>
<section>
<h2> 2.0.0 </h2>
<h3>Added</h3>
<li>Timeout argument to set the maximum amount of time the bot should run in case if no post were found.</li>
<h3>Changes</h3>
<li>Updated selenium from version <code>3.141.0</code> to <code>4.1.0</code> </li>
<h3>Fixed</h3>
<li>Fixed issue of browser keep on scrolling above despite calling scroll down method, happening due to different multiple functions call  </li>
<br>
<section>
<h2> 0.1.10 </h2>
<h3>Added</h3>
<li>Support for new Facebook Layout</li>

<br>
<h1> Changelog </h1>
<section>
<h2> 0.1.9 </h2>
<h3>Added</h3>
<li>Added feature for using proxy while scraping</li>

<br>


<section>
<h2> 0.1.8 </h2>
<h3>Fixed</h3>
<li>Fixed error "name element not found" occuring to some specific users.</li>
<li>Fixed CSV file missing <code> posted_on </code> column</li>
<br>


<h2> 0.1.7 </h2>
<h3>Fixed</h3>
<li>Only scrolling once while scraping, which created problem that only top few posts were scrapped. If user wants want more than 27 posts, it use to get strucked.</li>

<br>


<h2> 0.1.6 </h2>
<h3>Added</h3>
<li>Added feature to read long paragraph that lies inside "Continue reading" button. For e.g posts like <a href="https://www.facebook.com/permalink.php?story_fbid=174993781068849&id=109867790914782&__tn__=K-R" target="_blank">this</a></li>
<h3>Fixed</h3>
<li>Scrolling down directly to the bottom of the page during on start leads to login page, now it scroll down to half of the page and closes the login popup</li>
<br>

<h2> 0.1.5 <h2>
<h3>Fixed</h3>
<li>Fixed feature to scrap id from different URL pattern</li>

<br>

<h2> 0.1.4 <h2>
<h3>Added</h3>
<li> Support for emoji and other different languages(other than english) in output. It is no longer shown as a Unicode string.</li>

<br>

<h3> Fixed </h3>
<li> Total <code> reactions_count </code> getting 0 as a output. </li>

</section>
<section>

<h2> 0.1.6 </h2>
<h3>Added</h3>
<li>Added feature to read long paragraph that lies inside "Continue reading" button. For e.g posts like <a href="https://www.facebook.com/permalink.php?story_fbid=174993781068849&id=109867790914782&__tn__=K-R" target="_blank">this</a></li>
<h3>Fixed</h3>
<li>Scrolling down directly to the bottom of the page during on start leads to login page, now it scroll down to half of the page and closes the login popup</li>
<br>

<h2> 0.1.5 <h2>
<h3>Fixed</h3>
<li>Fixed feature to scrap id from different URL pattern</li>

<br>

<h2> 0.1.4 <h2>
<h3>Added</h3>
<li> Support for emoji and other different languages(other than english) in output. It is no longer shown as a Unicode string.</li>

<br>

<h3> Fixed </h3>
<li> Total <code> reactions_count </code> getting 0 as a output. </li>

</section>


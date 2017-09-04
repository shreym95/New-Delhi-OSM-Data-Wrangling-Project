<div>

<span class="c15 c36 c30"></span>

</div>

<span class="c38">Project: Wrangle OpenStreetMap Data</span>

* * *

<span class="c15 c36 c30"></span>

<span class="c15 c30 c36"></span>

<span class="c33">1.0</span> <span class="c12">INTRODUCTION</span>

<span class="c15 c2 c30"></span>

<span class="c2">AIM :</span> <span class="c11">To wrangle OpenStreetMap data for region of one’s choice, using MongoDB, in a python environment.</span>

<span class="c11"></span>

<span class="c15 c2 c30">Dataset Chosen : New-Delhi from Mapzen Metro Extracts    </span>

<span class="c15 c2 c30"></span>

<span class="c2">Link :</span> <span class="c32 c45 c23">[https://mapzen.com/data/metro-extracts/metro/new-delhi_india](https://www.google.com/url?q=https://mapzen.com/data/metro-extracts/metro/new-delhi_india/&sa=D&ust=1504538921904000&usg=AFQjCNEWRcgWQMD_LQeEQxo1MMq7B6Qg2A)</span><span class="c23 c24">/</span>

<span class="c24 c23"></span>

<span class="c2">Dataset size :         </span><span class="c6">Compressed XML: 44 MB</span>

<span class="c6">                        Uncompressed XML: 718 MB</span>

<span class="c6"></span>

<span class="c2">Environment :</span> <span class="c6">Python v3.6.2</span>

<span class="c6">                        MongoDB v3.4</span>

<span class="c6">                        IDE: PyCharm</span>

* * *

<span class="c6"></span>

<span class="c6"></span>

<span class="c33">2.0</span> <span class="c12 c15">WRANGLING</span>

<span class="c12 c15"></span>

<span class="c28 c34">Issues Encountered Found During Auditing Phase</span>

<span class="c15 c2 c30"></span>

*   <span class="c2">Abbreviated Street/Location Names</span> <span class="c11">: There were many instances of locations and streets being abbreviated such ‘St’ for ‘Street’, ‘Mkt’ for ‘Market’, ‘Extn’ for ‘Extension’, ‘Sec’ for ‘Sector’ and so on. Apparently, hindi connotations for these words were found to be mostly correct, such ‘Marg’, ‘Path’, ‘Sadak’ etc..</span>
*   <span class="c2">Incorrect phone number format</span><span class="c11">: While divided into mobile and landline, the formats followed were highly inconsistent and all over the place. The standard national format in India is as follows:</span>

*   <span class="c11">Mobile : +91 XXXX NNNNNN</span>
*   <span class="c11">Landline: +91 11 XXXXYYYY (For Delhi only)</span>

*   <span class="c2">State Names :</span> <span class="c32"> It was found that the included areas from the surrounding regions as well. This included Gurgaon, Noida, Faridabad and Ghaziabad. Their state names were not proper such as Hryana (</span><span class="c14">Haryana</span><span class="c32">), U.P.(</span><span class="c14">Uttar Pradesh</span><span class="c11">) etc.</span>
*   <span class="c2">Sources :</span> <span class="c11">Many sources such Bing, Yahoo, Survey etc. were either incorrectly spelled, or in a bad format.</span>
*   <span class="c2">Postal Code :</span> <span class="c11">Delhi and surrounding areas postal code is of six digits only, and many such codes were encountered where the length was not six.</span>

<span class="c11"></span>

<span class="c28 c34">Cleaning the Dataset</span>

*   <span class="c32">The mentioned street types were cleaned using</span> <span class="c2">regex</span> <span class="c11">functions, as it was not necessary that the word to be amended was the last word.</span>
*   <span class="c32">Mobile number formats were corrected to a very high degree through</span> <span class="c2">formatting and regex</span><span class="c11">, while landline number could not be done due to a large number of inconsistencies.</span>
*   <span class="c32">Correct state names were stored in a</span> <span class="c2">dictionary</span> <span class="c11">against the wrong ones, and were corrected through it.</span>
*   <span class="c11">An approach similar to the States was followed for sources as well.</span>
*   <span class="c32">Postal codes not having length equal to six were assigned the value</span> <span class="c2">NaN</span><span class="c11">.</span>

<span class="c32"></span> <span class="c2"> </span>

* * *

<span class="c15 c2 c30"></span>

<span class="c33">3.0</span> <span class="c12 c15">DATA OVERVIEW</span>

<span class="c28 c34"></span>

<span class="c2">Initial dataset size (Uncompressed):</span> <span class="c6">718 MB (delhi_map.osm)</span>

<span class="c15 c2 c30"></span>

<span class="c2">Converted JSON File size:          </span><span class="c14">832 MB (delhi_map.osm.json)</span>

<span class="c11"></span>

<span class="c34 c31">Database Queries</span>

<span class="c32 c30 c46"></span>

<a id="t.e3e6bbd3c20c73a4c6886966db2ca267b536891a"></a><a id="t.0"></a>

<table class="c8">

<tbody>

<tr class="c20">

<td class="c21" colspan="1" rowspan="1">

<span class="c32 c30 c47">Total number of records:</span>

</td>

</tr>

</tbody>

</table>

<span class="c27"></span>

<a id="t.5e7fb150e015794c367ab24e224351384731f3ca"></a><a id="t.1"></a>

<table class="c52">

<tbody>

<tr class="c20">

<td class="c48" colspan="1" rowspan="1">

<span class="c18">> db.delhi.find().count()</span>

<span class="c18"></span>

<span class="c25">4110208</span>

</td>

</tr>

</tbody>

</table>

<span class="c27"></span>

<a id="t.963063af575e47ef1961b678eee400066b2b1ab5"></a><a id="t.2"></a>

<table class="c8">

<tbody>

<tr class="c20">

<td class="c21" colspan="1" rowspan="1">

<span class="c22">Total number of “Node” entries:</span>

</td>

</tr>

</tbody>

</table>

<span class="c27"></span>

<a id="t.d5a5b82b5774177a2c7e81d4d6bb38ddfc92b905"></a><a id="t.3"></a>

<table class="c8">

<tbody>

<tr class="c20">

<td class="c16" colspan="1" rowspan="1">

<span class="c5">> db.delhi.find({element_type:"node"}).count()</span>

<span class="c5"></span>

<span class="c25">3415074</span>

</td>

</tr>

</tbody>

</table>

<span class="c27"></span>

<span class="c27"></span>

<span class="c27"></span>

<span class="c27"></span>

<span class="c27"></span>

<a id="t.40631666c6b6c8c2e55790b96bbbae37456d775e"></a><a id="t.4"></a>

<table class="c8">

<tbody>

<tr class="c20">

<td class="c21" colspan="1" rowspan="1">

<span class="c22">Total number of “Way” entries:</span>

</td>

</tr>

</tbody>

</table>

<span class="c41 c42 c30"></span>

<a id="t.7db698207eaf108b10338530b9c99bbac4a5d1ae"></a><a id="t.5"></a>

<table class="c8">

<tbody>

<tr class="c20">

<td class="c16" colspan="1" rowspan="1">

<span class="c5">> db.delhi.find({element_type:"way"}).count()</span>

<span class="c5"></span>

<span class="c25">695134</span>

</td>

</tr>

</tbody>

</table>

<span class="c27"></span>

<a id="t.4bf52a86536999cffee488c6cafa634874e2cfbb"></a><a id="t.6"></a>

<table class="c8">

<tbody>

<tr class="c20">

<td class="c21" colspan="1" rowspan="1">

<span class="c22">Total unique users:</span>

</td>

</tr>

</tbody>

</table>

<span class="c15 c42 c30"></span>

<a id="t.15e6bd575afe95d1e15228242ea807c843453c8f"></a><a id="t.7"></a>

<table class="c8">

<tbody>

<tr class="c20">

<td class="c16" colspan="1" rowspan="1">

<span class="c5">> db.delhi.distinct("creation_info.uid").length</span>

<span class="c5"></span>

<span class="c5">1498</span>

</td>

</tr>

</tbody>

</table>

<span class="c27"></span>

<a id="t.dc0252bc7b2df96d3e89f95aca2cf56d08c463c9"></a><a id="t.8"></a>

<table class="c8">

<tbody>

<tr class="c20">

<td class="c21" colspan="1" rowspan="1">

<span class="c22">Total five contributors:</span>

</td>

</tr>

</tbody>

</table>

<span class="c27 c53"></span>

<a id="t.a449fa119f6ee0c0cf066147370a8f4ef3b10c4d"></a><a id="t.9"></a>

<table class="c8">

<tbody>

<tr class="c20">

<td class="c16" colspan="1" rowspan="1">

<span class="c5">> db.delhi.aggregate([{$group:{"_id":"$creation_info.user", count:{"$sum":1}}},{ $sort:{"count":-1}},{$limit:5}])</span>

<span class="c5"></span>

<span class="c5">{ "_id" : "Oberaffe", "count" : 268668 }</span>

<span class="c5">{ "_id" : "premkumar", "count" : 164032 }</span>

<span class="c5">{ "_id" : "saikumar", "count" : 159906 }</span>

<span class="c5">{ "_id" : "Naresh08", "count" : 136335 }</span>

<span class="c5">{ "_id" : "anushap", "count" : 133391 }</span>

</td>

</tr>

</tbody>

</table>

<span class="c25 c37 c30"></span>

<a id="t.e22cc742572deb17b914992b00fa217a617bb53b"></a><a id="t.10"></a>

<table class="c8">

<tbody>

<tr class="c20">

<td class="c21" colspan="1" rowspan="1">

<span class="c22">Average number of posts per user:</span>

</td>

</tr>

</tbody>

</table>

<span class="c15 c30 c42"></span>

<a id="t.95bae42fde59e2cb927d9ce1a6123d04578bc6c9"></a><a id="t.11"></a>

<table class="c8">

<tbody>

<tr class="c20">

<td class="c16" colspan="1" rowspan="1">

<span class="c5">> db.delhi.aggregate([{$group:{"_id":"$creation_info.user", count:{"$sum":1}}},{ $group:{"_id":"Average Posts Per User", average:{"$avg":"$count"}}}])</span>

<span class="c5"></span>

<span class="c5">{ "_id" : "Average Posts Per User", "average" : 2743.7970627503337 }</span>

</td>

</tr>

</tbody>

</table>

<span class="c27"></span>

<a id="t.7a4cb979a4b6aaef3868f6195b26c1eba4efe738"></a><a id="t.12"></a>

<table class="c8">

<tbody>

<tr class="c20">

<td class="c21" colspan="1" rowspan="1">

<span class="c22">Top five amenities:</span>

</td>

</tr>

</tbody>

</table>

<span class="c25 c30 c37"></span>

<a id="t.0f42355d5cdef19afe231e9cd59d70e5c73c453a"></a><a id="t.13"></a>

<table class="c8">

<tbody>

<tr class="c20">

<td class="c16" colspan="1" rowspan="1">

<span class="c5">> db.delhi.aggregate({$match:{"amenity":{$exists:1}}}, {$group:{"_id":"$amenity",count:{$sum:1}}},{$sort: {"count":-1}},{$limit:5})</span>

<span class="c5"></span>

<span class="c5">{ "_id" : "school", "count" : 954 }</span>

<span class="c5">{ "_id" : "place_of_worship", "count" : 407 }</span>

<span class="c5">{ "_id" : "parking", "count" : 353 }</span>

<span class="c5">{ "_id" : "restaurant", "count" : 249 }</span>

<span class="c5">{ "_id" : "fuel", "count" : 246 }</span>

</td>

</tr>

</tbody>

</table>

<span class="c5"></span>

<a id="t.0aa7c9ca259c24c726043248eaab0c21fe701985"></a><a id="t.14"></a>

<table class="c8">

<tbody>

<tr class="c20">

<td class="c21" colspan="1" rowspan="1">

<span class="c22">Top five roadways:</span>

</td>

</tr>

</tbody>

</table>

<span class="c27"></span>

<a id="t.b46b74d46bc56cce7b8d8c1f65515829a7129df6"></a><a id="t.15"></a>

<table class="c8">

<tbody>

<tr class="c20">

<td class="c16" colspan="1" rowspan="1">

<span class="c5">> db.delhi.aggregate({$match:{"highway":{$exists:1}}}, {$group:{"_id":"$highway",count:{$sum:1}}},{$sort: {"count":-1}},{$limit:5})</span>

<span class="c5"></span>

<span class="c5">{ "_id" : "residential", "count" : 106059 }</span>

<span class="c5">{ "_id" : "service", "count" : 13178 }</span>

<span class="c5">{ "_id" : "living_street", "count" : 5958 }</span>

<span class="c5">{ "_id" : "tertiary", "count" : 4533 }</span>

<span class="c5">{ "_id" : "unclassified", "count" : 3117 }</span>

</td>

</tr>

</tbody>

</table>

<span class="c25 c37 c30"></span>

<a id="t.401c8803985b8a86fb4fff8a889a1a3768f94b0f"></a><a id="t.16"></a>

<table class="c8">

<tbody>

<tr class="c20">

<td class="c21" colspan="1" rowspan="1">

<span class="c22">Top five data sources:</span>

</td>

</tr>

</tbody>

</table>

<span class="c25 c37 c30"></span>

<a id="t.853788297985fefec2772c9b84612c9ad9827def"></a><a id="t.17"></a>

<table class="c8">

<tbody>

<tr class="c49">

<td class="c16" colspan="1" rowspan="1">

<span class="c5">> db.delhi.aggregate({$match:{"source":{$exists:1}}}, {$group:{"_id":"$source",count:{$sum:1}}},{$sort: {"count":-1}},{$limit:5})</span>

<span class="c5"></span>

<span class="c5">{ "_id" : "Bing", "count" : 649 }</span>

<span class="c5">{ "_id" : "Yahoo", "count" : 315 }</span>

<span class="c5">{ "_id" : "Survey", "count" : 57 }</span>

<span class="c5">{ "_id" : "GPS", "count" : 39 }</span>

<span class="c5">{ "_id" : "AND", "count" : 39 }</span>

</td>

</tr>

</tbody>

</table>

<span class="c27"></span>

<a id="t.20a1e1057381d6e37e6ea15260adb902fa0e5d65"></a><a id="t.18"></a>

<table class="c8">

<tbody>

<tr class="c20">

<td class="c21" colspan="1" rowspan="1">

<span class="c22">Top five areas, ranked using postal code</span>

</td>

</tr>

</tbody>

</table>

<span class="c27"></span>

<a id="t.a196719c0afedbd4ac0c494b3f64f483f333e4ec"></a><a id="t.19"></a>

<table class="c8">

<tbody>

<tr class="c20">

<td class="c16" colspan="1" rowspan="1">

<span class="c5">> db.delhi.aggregate({$match:{"addr.postcode":{$exists:1}}}, {$group:{"_id":"$addr.postcode",count:{$sum:1}}},{$sort: {"count":-1}},{$limit:5})</span>

<span class="c5"></span>

<span class="c5">{ "_id" : "110087", "count" : 509 }</span>

<span class="c5">{ "_id" : "122001", "count" : 100 }</span>

<span class="c5">{ "_id" : "110092", "count" : 65 }</span>

<span class="c5">{ "_id" : "100006", "count" : 59 }</span>

<span class="c5">{ "_id" : "110075", "count" : 55 }</span>

</td>

</tr>

</tbody>

</table>

<span class="c5"></span>

* * *

<span class="c15 c2 c30"></span>

<span class="c15 c2 c30"></span>

<span class="c33">4.0</span> <span class="c12 c15">ADDITIONAL IDEAS</span>

<span class="c12 c15"></span>

*   <span class="c11">The data has a lot of inconsistencies in the address format, which either could be hardcoded in the cleaning file, during further cleaning, or can be corrected through online directories taken as standards.</span>

*   <span class="c11">Postal Codes on the other hand, can be cleaned manually as well, because of a very high degree of format accuracy.</span>

<span class="c27"></span>

<a id="t.244abe4f7a58211efac960d09c3d8ead731ae159"></a><a id="t.20"></a>

<table class="c19">

<tbody>

<tr class="c20">

<td class="c43" colspan="1" rowspan="1">

<span class="c18">> db.delhi.aggregate({$match:{$and:[{"addr.postcode":</span>

<span class="c18">{$exists:1}},{"addr.postcode":"NaN"}]}},{$group:</span>

<span class="c18">{"_id":"$addr.postcode", count:{$sum:1}}})</span>

<span class="c18"></span>

<span class="c44">{ "_id" : "NaN", "count" : 22 }</span>

</td>

</tr>

</tbody>

</table>

<span class="c11"></span>

*   <span class="c32">While not being used presently, I think the phone number related fields can be cleaned using Python repositories available on Github for this purpose, such as</span> <span class="c32 c45 c23">[this one](https://www.google.com/url?q=https://github.com/daviddrysdale/python-phonenumbers&sa=D&ust=1504538921924000&usg=AFQjCNHnlwS6jhvmAy1gjYtgOi7EVS0NUQ)</span><span class="c11">( https://github.com/daviddrysdale/python-phonenumbers). This will help in cleaning of landline number as well, which are not being done presently.</span>
*   <span class="c32">Finally, as this data is not limited to Delhi only and has some of the surrounding regions as well, it should be renamed to NCR-Map, signifying the</span> <span class="c28 c2">National Capital Region.</span>

<span class="c2 c31">        </span>

<a id="t.921895783dfcba3f0b8c8ba8c5b64a57d2fd7201"></a><a id="t.21"></a>

<table class="c19">

<tbody>

<tr class="c20">

<td class="c43" colspan="1" rowspan="1">

<span class="c18">> db.delhi.distinct("addr.state")</span>

<span class="c18">[</span>

<span class="c18">        "Delhi",</span>

<span class="c18">        "NCR",</span>

<span class="c18">        "Uttar Pradesh",</span>

<span class="c18">        "Haryana"</span>

<span class="c44">]</span>

</td>

</tr>

</tbody>

</table>

<span class="c28 c2"></span>

<span class="c2 c28"></span>

<span class="c6">It should be kept in mind, that the above suggested improvements are not absolute, and may lead to some issues during implementation. So as a best practise, and also a precautionary measure, it may prove worthwhile to anticipate such problems. These are documented as follows, as well as some additional ideas.</span>

<span class="c6"></span>

1.  <span class="c11">Due to future changes in street names or addresses, the present dataset may become obsolete. This will make cleaning harder as directories taken as standard will have updated data, and corresponding older names may be rendered invalid. One example of this is the city of Gurugram, which was previously named as Gurgaon. Gurugram is the official name, while Gurgaon is still being used in most unofficial documents.</span>
2.  <span class="c11">Phone numbers can be formatted through the mentioned library, but as was seen in this dataset, a string containing multiple numbers with some digits replaced will be very difficult to correct. There is no standard for splitting such strings. One way that I think can be implemented to solve this Machine learning. Since we do have a large dataset for PAN India, an ML algorithm may be trained, to at the least, identify the issue which can later be cleaned manually.</span>
3.  <span class="c11">For a large portion of this data, it was observed the address data was generally inconsistent across fields, i.e. Street names also had house numbers, or house numbers included area identifiers, and such data could not be cleaned as there was no pattern. Hard-coding would be a waste of resources in this case. So, the solution stated before, of training an ML algorithm, could also be applied here.</span>
4.  <span class="c32">As a lot of data seemed to be manually entered, it may pose a problem if this data isn’t actually accurate especially in the case of address. And that may even lead to wrong cleaning methods being applied. So, after a</span><span class="c14"> cleaned</span><span class="c32"> </span><span class="c14">address</span> <span class="c32">is built through whatever methods, the same can be validated using the location tags, as it seems to be highly accurate (more number of decimal places). The address can then be verified using latitude and longitude. A very good website</span> <span class="c32 c23 c45">[http://www.latlong.net](https://www.google.com/url?q=http://www.latlong.net/Show-Latitude-Longitude.html&sa=D&ust=1504538921927000&usg=AFQjCNF75tqRY057KgjGealb6gK4WC0Q-g)</span><span class="c11">, can be used for comparison.</span>

<span class="c11"></span>

* * *

<span class="c11"></span>

<span class="c11"></span>

<span class="c33">5.0</span> <span class="c12 c15">CONCLUSION</span>

<span class="c12 c15"></span>

<span class="c11">After three to four iterations of auditing and cleaning the data using several samples, it’s clear that the data has been manually entered, as well as gathered through GPS.</span>

<span class="c11"></span>

<span class="c11">Manually entered data, if not from a credible source, cannot be relied upon a 100%. So, a robust mechanism to verify the data is needed, alongside cleaning practises such as those demonstrated by me in this project. The cleaning done by me only represents a small fraction of the requirements for this dataset.</span>

<span class="c28 c29"></span>

<span class="c28 c29"></span>

<span class="c28 c29">REFERENCES:</span>

*   <span class="c2 c31"> </span><span class="c10">[https://en.wikipedia.org/wiki/National_Capital_Region_(India)](https://www.google.com/url?q=https://en.wikipedia.org/wiki/National_Capital_Region_(India)&sa=D&ust=1504538921929000&usg=AFQjCNGbKQ_SMV2nKfOYW1qEz2nfYNmF6w)</span>
*   <span class="c10">[https://docs.mongodb.com/manual/](https://www.google.com/url?q=https://docs.mongodb.com/manual/&sa=D&ust=1504538921929000&usg=AFQjCNHZfev_-zf4iWIyIivzrhdoCdJl2A)</span>
*   <span class="c10">[https://streets.openalfa.in/](https://www.google.com/url?q=https://streets.openalfa.in/&sa=D&ust=1504538921930000&usg=AFQjCNEHu5khNFxA2WpzsHY2g2BC4v1mcA)</span>
*   <span class="c10">[https://www.openstreetmap.org/](https://www.google.com/url?q=https://www.openstreetmap.org/&sa=D&ust=1504538921930000&usg=AFQjCNE1d6H9T5nwhphDPPNaEfYGnigl5Q)</span>
*   <span class="c10">[http://www.callingdelhi.com/delhi-landline-and-mobile-phone-numbers](https://www.google.com/url?q=http://www.callingdelhi.com/delhi-landline-and-mobile-phone-numbers&sa=D&ust=1504538921931000&usg=AFQjCNEAzrOfzjKO2Yl4xkeaaRanV6WCog)</span>
*   <span class="c10">[https://mapzen.com/data/metro-extracts/metro/new-delhi_india](https://www.google.com/url?q=https://mapzen.com/data/metro-extracts/metro/new-delhi_india/&sa=D&ust=1504538921931000&usg=AFQjCNEmMN1peXUXkulnPHaDWfj-A1jepw)</span><span class="c10 c50">/</span>
*   <span class="c10">[https://stackoverflow.com/](https://www.google.com/url?q=https://stackoverflow.com/&sa=D&ust=1504538921931000&usg=AFQjCNFxmdco5eG6e2_LNPtNQ9dWh2tNWw)</span>

<span class="c11"></span>

<span class="c32">Author : Shrey Marwaha</span>

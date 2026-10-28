**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/application-abuse/>

<div class=" switcher-67   taskPanel-65 "><div style="width: 100%; height: 100%;"><div style="text-align: center;"><img src="/static/svg/XtremeLogo19.svg" style="max-width: 360px; margin-bottom: -10px;"></div><div class="text-center"><h1>Application Abuse</h1><div>Time limit: <em>2500 ms</em><br>Memory limit: <em>256 MB</em><br><br></div><div></div></div><div><h2> IEEE Xplore 
</h2><p>Warm greetings to all IEEExtreme Participants from the Xplore API Team! 
</p><p>
</p><p>As part of the IEEExtreme Competition, you will face a programming challenge where you'll need to analyze web application logs to identify potential instances of application misuse.
</p><p>
</p><p>For a full dynamic database search IEEE Xplore API is available for your IEEE research needs. Xplore API provides metadata on 4.9mm academic works and is now delivering full-text content on 50k 'Open Access' articles. Xplore API will make your research needs fast and easy. The Xplore API Portal supports PHP, Python and Java as well as providing output in JSON and XML formats. Many API use cases are listed within the API Portal. 
</p><p>
</p><p>Xplore API registration is free. To learn more about IEEE Xplore API please visit <a href="developer.ieee.org/" class=" Link-container-31">developer.ieee.org/</a> and register for an API key TODAY! 
</p><p>
</p><h2> Challenge
</h2><p>
</p><p>Users log into the IEEE document repository application to search for articles, download PDFs, view abstracts, and perform various other tasks. To access the application, users must agree to the acceptable usage terms. Your task is to identify users who are violating these terms.
</p><p>
</p><p>
</p><p>
</p><h2> Standard input
</h2><p>
</p><p>The input consists of three parts: a web log descriptor, rules of abuse, and web log entries. The first row specifies the total number of rows in the file. The second row outlines the rules of abuse, which detail five potential ways individuals can misuse the system:
</p><p>
</p><p>
</p><ol><li>Using <strong>X</strong> or more different user agents in a single day, indicated by <code>agent=X</code>. 
</li><li>Using <strong>X</strong> or more different IP addresses in a single day, indicated by <code>ip=X</code>.
</li><li>Downloading PDFs at least <strong>X</strong> times, indicated by <code>pdf=X</code>. 
</li><li>Initiating <strong>X</strong> or more sessions, indicated by <code>session=X</code>.
</li><li>Engaging in <strong>X</strong> or more crawling activities in a single day, indicated by <code>crawl=X</code>.
</li></ol><p>
</p><p>The settings can be listed in any order. For example:
</p><ol><li><code>agent=3, ip=4, pdf=10, session=20, crawl=30</code>.
</li><li><code>session=20, pdf=100</code>.
</li></ol><p>
</p><p>
</p><p>Not every situation requires a comprehensive set of rules. For example, you may only need to check for the existence of <em>session</em> and <em>pdf</em> abuse, without the need for additional rules.
</p><p>
</p><p>To determine if an individual is using a robot to download PDFs sequentially, examine the order of the PDF downloads. For example, if the user downloads the PDFs in the following order: <code>1.pdf</code>, <code>2.pdf</code>, <code>3.pdf</code>, ..., <code>10.pdf</code>, this indicates they are likely using a robot.  There can be other page requests in between PDF requests.  For example: <code>1.pdf</code>, <code>/search/criteria</code>, <code>2.pdf</code>, <code>/search/results</code>, ..., <code>10.pdf</code>.  This is still considered abuse.
</p><p>
</p><p>If the user downloads more than the specified number of PDFs sequentially  (set by the parameter <code>crawl=X</code>), report this in the output. The downloads must be in sequential order by date and time to be considered part of the same robot-driven download session. 
</p><p>
</p><p>For instance, if the user downloads the PDFs in the order <code>1.pdf</code>, <code>4.pdf</code>, <code>2.pdf</code>, <code>3.pdf</code>, this is not considered sequential and would not reach the limit of <code>crawl=4</code> downloads sequentially, even though <code>x=4</code> PDFs were downloaded.
</p><p>
</p><p>Keep track of the ids and check if the number of sessions for each id is equal to or greater than a specified setting. For instance, if a certain individual has 10 sessions and the setting is set to <code>session=5</code>, then in the output, print <code>{Id} session=10</code>.
</p><p>
</p><p>When considering the rules, remember that the settings are based on a <strong>daily</strong> timeframe. So, if the log entries cover multiple days, you may not identify any abuse when looking at individual days, even though there might be abuse when considering the entire set of log entries.
</p><p>
</p><p>The third row contains the log file descriptor.  The log file contains the following fields:
</p><p>
</p><ol><li><strong>Host</strong> – Domain name.  For example, <code>documents.ieee.org</code>.  
</li><li><strong>Client IP</strong> – IP address of the client that is making a request to the server.
</li><li><strong>Id</strong> – Unique string identifying the individual.
</li><li><strong>Date</strong> – Date of the request.  The format will be [dd/Mmm/YYYY:HH24:mm:ss] . Example: <code>[07/Oct/2025:14:26:41]</code>.
</li><li><strong>Request</strong> – The URL requested.  For example:  <code>"GET /article/abstract?id=XYZ HTTP/1.1"</code>
</li><li><strong>HTTP Status</strong> – Standard list of HTTP Status codes.  See <a href="https://en.wikipedia.org/wiki/List_of_HTTP_status_codes" class=" Link-container-31">Wikipedia - List of HTTP status codes</a>.
</li><li><strong>User Agent</strong> – A string of text that identifies the client software originating a request.
</li><li><strong>Session Cookie</strong> – A string used to track a user's interactions during a single session.
</li></ol><p>
</p><p>
</p><p>All fields will be present.  However, the order is not always the same.  Examples:
</p><p>
</p><ol><li>Host, Client IP, Id, Date, Request, HTTP Status, User Agent, Session Cookie
</li><li>Host, Client IP, Date, Request, HTTP Status, User Agent, Session Cookie, Id
</li></ol><p>
</p><p>The remaining rows will be the log entries.  If a field has no value, it will be set to a dash <code>"-"</code>.  
</p><p>
</p><ol><li><code>documents.ieee.org 131.155.125.139 XYZ  [07/Feb/2024:12:26:41] "GET /document/abstract?id=123 HTTP/1.1" 200 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36" "ABC123"</code>
</li><li><code>documents.ieee.org 121.135.110.122 - [18/Mar/2025:18:20:33] "GET /document/123.pdf HTTP/1.1" 200 "Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36 Edge/40.15254.603" "456LLL"</code>
</li></ol><p>
</p><p>The Date will always be enclosed by square brackets and the User Agent, Request and Session Cookie will always be enclosed by double quotes.
</p><p>
</p><p>Lastly any HTTP Status code other than <strong>200</strong> should be ignored and not counted towards a violation.
</p><p>
</p><p>
</p><h2> Standard output
</h2><p>
</p><p>For each violation write out the id followed by the abuse type and the value.  Sort by id with a secondary sort of abuse type.
</p><p>
</p><h2> Constraints and notes
</h2><p>
</p><ul><li><span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mtext>Number&nbsp;of&nbsp;records</mtext><mo>≤</mo><mn>10</mn><mo separator="true">,</mo><mn>000</mn></mrow><annotation encoding="application/x-tex">\text{Number of records} \leq 10,000</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.83041em;vertical-align:-0.13597em;"></span><span class="mord text"><span class="mord">Number&nbsp;of&nbsp;records</span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.8388800000000001em;vertical-align:-0.19444em;"></span><span class="mord">1</span><span class="mord">0</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord">0</span><span class="mord">0</span><span class="mord">0</span></span></span></span></span>.
</li><li>A request for a PDF download will always take the form <code>"GET /document/{XXX}.pdf HTTP/1.1"</code> where {XXX} is a string containing numbers only.
</li><li>Valid log entries are in date order.
</li><li>If there are no ids that have abuse simple print <code>N/A</code> in the output.
</li><li>There will not be duplicate abuse of the same type for the same id over multiple days.  For instance, if the pdf abuse is set as 10 and there are two days contained in the file, you will never have the case <code>XYZ pdf=11</code> for 01/01/2025 and <code>XYZ pdf=12</code> for 01/02/2025.
</li></ul><p>
</p><p>
</p><p><table class=" Table-container-81" style="table-layout: fixed; break-inside: avoid;"><thead class="thead-79"><tr><th>Input</th><th>Output</th><th>Explanation</th></tr></thead><tbody><tr class="tableRow-80"><td style="break-before: avoid;"><pre>agent=2, ip=2, pdf=2, session=2, crawl=3
Host, Client IP, Id, Date, Request, HTTP Status, User Agent, Session Cookie
documents.ieee.org 116.84.105.37 ABCABC [01/Oct/2025:10:00:03] "GET /document/779.pdf HTTP/1.1" 200 "Mozilla/5.0 (Linux; Android 10; ELS-NX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 OPR/58.2.2878.53403" "JKXclXx22zMrHRxx"
documents.ieee.org 116.84.105.37 ABCABC [01/Oct/2025:10:00:04] "GET /document/780.pdf HTTP/1.1" 200 "11 Mozilla/5.0 (Linux; Android 10; ELS-NX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 OPR/58.2.2878.53403" "JKXclXx22zMrHRxx"
documents.ieee.org 116.84.105.37 FVNYKW [01/Oct/2025:10:23:03] "GET /document/779.pdf HTTP/1.1" 200 "Mozilla/5.0 (Linux; Android 10; ELS-NX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 OPR/58.2.2878.53403" "JKXclXx22zMrHR"
documents.ieee.org 188.155.4.245 - [01/Oct/2025:10:23:05] "GET /document/issue?id=664 HTTP/1.1" 200 "Mozilla/5.0 (Linux; Android 10; LIO-L29 Build/HUAWEILIO-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36" ""
documents.ieee.org 38.206.21.104 PKTJVG [01/Oct/2025:10:23:21] "GET /document/issue?id=714 HTTP/1.1" 200 "Mozilla/5.0 (Linux; arm; Android 7.1.1; SM-J510FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 YaBrowser/20.2.5.120.00 Mobile SA/1 Safari/537.36" "#yHigR#edH0WA*"
documents.ieee.org 93.30.209.202 - [01/Oct/2025:10:23:23] "GET /document/abstract?id=852 HTTP/1.1" 200 "Mozilla/5.0 (Linux; Android 10; LIO-L29 Build/HUAWEILIO-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36" ""
documents.ieee.org 111.116.84.105.37 FVNYKW [01/Oct/2025:10:23:25] "GET /document/714.pdf HTTP/1.1" 200 "1111 Mozilla/5.0 (Linux; Android 10; ELS-NX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 OPR/58.2.2878.53403" "111 JKXclXx22zMrHR"
documents.ieee.org 4.236.187.49 - [01/Oct/2025:10:23:27] "GET /book/chapter?id=979 HTTP/1.1" 200 "Mozilla/5.0 (Linux; Android 10; LIO-L29 Build/HUAWEILIO-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36" ""
documents.ieee.org 58.109.163.186 - [01/Oct/2025:10:23:29] "GET /document/publication?id=293 HTTP/1.1" 200 "Mozilla/5.0 (Linux; Android 10; LIO-L29 Build/HUAWEILIO-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36" ""
documents.ieee.org 103.37.68.141 - [01/Oct/2025:10:23:33] "GET /site/login HTTP/1.1" 200 "Mozilla/5.0 (Linux; Android 10; LIO-L29 Build/HUAWEILIO-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36" ""
documents.ieee.org 98.209.252.152 HTRXVC [01/Oct/2025:10:23:37] "GET /document/622.pdf HTTP/1.1" 200 "Mozilla/5.0 (Windows NT 6.3; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 YaBrowser/20.6.1.151 Yowser/2.5 Yptp/1.23 Safari/537.36" "5vnkAHpJx0Wo4D"
documents.ieee.org 188.155.4.245 - [01/Oct/2025:10:23:39] "GET /book/chapter?id=627 HTTP/1.1" 200 "Mozilla/5.0 (Linux; Android 10; LIO-L29 Build/HUAWEILIO-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36" ""
documents.ieee.org 98.209.252.152 HTRXVC [01/Oct/2025:10:23:40] "GET /document/625.pdf HTTP/1.1" 200 "Mozilla/5.0 (Windows NT 6.3; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 YaBrowser/20.6.1.151 Yowser/2.5 Yptp/1.23 Safari/537.36" "5vnkAHpJx0Wo4D"</pre></td><td style="break-before: avoid;"><pre>ABCABC agent=2
ABCABC pdf=2
FVNYKW agent=2
FVNYKW ip=2
FVNYKW pdf=2
FVNYKW session=2
HTRXVC pdf=2</pre></td><td style="break-before: avoid;"><div><p>The queries go as follows:
</p><p>
</p><p>Query 1 - Valid.
</p><ul><li>Id: <code>ABCABC</code>
</li><li>Date: <code>01/Oct/2025</code>
</li><li>Request: 779.pdf
</li><li>User Agent: <code>"Mozilla/5.0 (Linux; Android 10; ELS-NX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 OPR/58.2.2878.53403"</code>
</li><li>Session Cookie: <code>"JKXclXx22zMrHRxx"</code>
</li><li>Ip: <code>"JKXclXx22zMrHRxx"</code>
</li></ul><p>Query 2 - Valid.
</p><ul><li>Id: <code>ABCABC</code>
</li><li>Date: <code>01/Oct/2025</code>
</li><li>Request: 780.pdf
</li><li>User Agent: <code>"11 Mozilla/5.0 (Linux; Android 10; ELS-NX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 OPR/58.2.2878.53403"</code>
</li><li>Session Cookie: <code>"JKXclXx22zMrHRxx"</code>
</li><li>Ip: <code>"JKXclXx22zMrHRxx"</code>
</li></ul><p>Query 3 - Valid.
</p><ul><li>Id: <code>FVNYKW</code>
</li><li>Date: <code>01/Oct/2025</code>
</li><li>Request: 779.pdf
</li><li>User Agent: <code>"Mozilla/5.0 (Linux; Android 10; ELS-NX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 OPR/58.2.2878.53403"</code>
</li><li>Session Cookie: <code>"JKXclXx22zMrHR"</code>
</li><li>Ip: <code>"JKXclXx22zMrHR"</code>
</li></ul><p>Query 4 - Invalid. No Id
</p><p>Query 5 - Valid.
</p><ul><li>Id: <code>PKTJVG</code>
</li><li>Date: <code>01/Oct/2025</code>
</li><li>Request: non-pdf
</li><li>User Agent: <code>"Mozilla/5.0 (Linux; arm; Android 7.1.1; SM-J510FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 YaBrowser/20.2.5.120.00 Mobile SA/1 Safari/537.36"</code>
</li><li>Session Cookie: <code>"#yHigR#edH0WA*"</code>
</li><li>Ip: <code>"#yHigR#edH0WA*"</code>
</li></ul><p>Query 6 - Invalid. No Id
</p><p>Query 7 - Valid.
</p><ul><li>Id: <code>FVNYKW</code>
</li><li>Date: <code>01/Oct/2025</code>
</li><li>Request: 714.pdf
</li><li>User Agent: <code>"1111 Mozilla/5.0 (Linux; Android 10; ELS-NX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 OPR/58.2.2878.53403"</code>
</li><li>Session Cookie: <code>"111 JKXclXx22zMrHR"</code>
</li><li>Ip: <code>"111 JKXclXx22zMrHR"</code>
</li></ul><p>Query 8 - Invalid. No Id
</p><p>Query 9 - Invalid. No Id
</p><p>Query 10 - Invalid. No Id
</p><p>Query 11 - Valid.
</p><ul><li>Id: <code>HTRXVC</code>
</li><li>Date: <code>01/Oct/2025</code>
</li><li>Request: 622.pdf
</li><li>User Agent: <code>"Mozilla/5.0 (Windows NT 6.3; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 YaBrowser/20.6.1.151 Yowser/2.5 Yptp/1.23 Safari/537.36"</code>
</li><li>Session Cookie: <code>"5vnkAHpJx0Wo4D"</code>
</li><li>Ip: <code>"5vnkAHpJx0Wo4D"</code>
</li></ul><p>Query 12 - Invalid. No Id
</p><p>Query 13 - Valid.
</p><ul><li>Id: <code>HTRXVC</code>
</li><li>Date: <code>01/Oct/2025</code>
</li><li>Request: 625.pdf
</li><li>User Agent: <code>"Mozilla/5.0 (Windows NT 6.3; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 YaBrowser/20.6.1.151 Yowser/2.5 Yptp/1.23 Safari/537.36"</code>
</li><li>Session Cookie: <code>"5vnkAHpJx0Wo4D"</code>
</li><li>Ip: <code>"5vnkAHpJx0Wo4D"</code>
</li></ul><p>
</p><p>So the final abuse contains:
</p><p>
</p><ul><li>ABCABC agent=2, since it has 2 different agents on day <code>01/Oct/2025</code> (Requests 1 and 2).
</li><li>ABCABC pdf=2, since it has downloaded the pdf files <code>779.pdf</code> and <code>780.pdf</code> on day <code>01/Oct/2025</code> (Requests 1 and 2).
</li><li>FVNYKW agent=2, since since it has 2 different agents on day <code>01/Oct/2025</code> (Requests 3 and 7).
</li><li>FVNYKW ip=2, since it has 2 different ips on day <code>01/Oct/2025</code> (Requests 3 and 7).
</li><li>FVNYKW pdf=2, since it has downloaded the pdf files <code>779.pdf</code> and <code>714.pdf</code> on day <code>01/Oct/2025</code> (Requests 3 and 7).
</li><li>FVNYKW session=2, since it has used 2 different session cookies on day <code>01/Oct/2025</code> (Requests 3 and 7).
</li><li>HTRXVC pdf=2, since it has downloaded the pdf files <code>622.pdf</code> and <code>625.pdf</code> on day <code>01/Oct/2025</code> (Requests 11 and 13).</li></ul></div></td></tr></tbody></table></p></div></div></div>
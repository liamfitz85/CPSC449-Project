# CPSC449-Project
project2-specification: https://docs.google.com/document/d/1U-Ykn7igJtpRoRr86te6jA0t0TmBvTWMHdR1lGqjvmo <br />
<b>Team Members</b><br />
Wellson Pan - WellsonPan@csu.fullerton.edu - Dev 1<br />
Liam Fitzpatrick - lfitzpatrick0@csu.fullerton.edu - Dev 2<br />
Duy Do - duy.ado@csu.fullerton.edu - Ops<br />

<b>Usage:<br /></b> 
&nbsp;&nbsp;if first run then:<br />
&nbsp;&nbsp;&nbsp;&nbsp;./first_run <br /> 
&nbsp;&nbsp;&nbsp;&nbsp;./curl_requests <br />
&nbsp;&nbsp;else:<br />
&nbsp;&nbsp;&nbsp;&nbsp;foreman start <br />

<b>To configure kong:<br /></b>
&nbsp;&nbsp;sudo kong start
&nbsp;&nbsp;./add_services.sh

<b>To populate all microservices:<br /></b>
&nbsp;&nbsp;./curl_requests.sh

<b>To start MinIO bucket:<br /></b>
&nbsp;&nbsp;sudo ./minio server /data 

<b>Schema File:</b><br />
&nbsp;&nbsp;queries/initQueries/init_db.sql<br />

<b>Notes:</b></br>
&nbsp;&nbsp;<b>./first_run</b> will install pip3 so it asks for sudo. It then installs the packages in requirements.txt.

&nbsp;&nbsp;<b>./first_run</b> XSPF generator code is taken from here: https://github.com/alastair/xspf

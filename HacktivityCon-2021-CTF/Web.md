# Web

## Confidentiality
### Problem Type: Linux Command Injection
Given a text box, where you can input a payload.
The webpage will display the results of `ls [input]` 

From `ls`, we know that there is a `flag.txt` file within the current directory. Hence, we simply pipe the command `| cat flag.txt` to obtain the flag. 

![](https://i.imgur.com/t6xYQg2.png)

## Integrity
### Problem Type: Linux Command Injection
Similar to Confidentiality, we are given a text box where we can input a payload. However, the webpage will now display the results of `sha256sum [input]`. 

Furthermore, it had strict input filtering, where there were limited symbols available: `?, ~` 

We intercept the request and response with Burp Proxy, and repeat the requests through Burp Repeater. We note that the input is url-encoded, and hence, we can craft the payload to use a newline character, %0A.

![](https://i.imgur.com/3Vm3O1N.png)

The payload is: %0A cat flag.

## Titanic
### Problem Type: ???
Source code of the web page tells us there is a hidden `/server-status` directory we should visit. However, we do not have permissions to visit the page. 

![](https://i.imgur.com/MapiZre.png)

It is likely we require the admin credentials to obtain permissions to visit this `/server-status` page.
![Uploading file..._lusaacpa3]()

While usual credentials such as root/root or admin/admin did not work, we noticed there was a `/urlcapture.php` in the source code.

![](https://i.imgur.com/ISM4bBD.png)

In this page, it takes a screenshot of a url and displays it to the user as an image. We tried many URLs, but eventually the payload that worked was: `localhost/server-status`

We obtain the GET history of login requests, and amongst the wild history of login attempts we saw, we notes some credentials which looked more legit.  

![](https://i.imgur.com/nV1xhmc.png)

`uname = root and psw = EYNDR4NhadwX9rtef`

Upon logging in through the admin login page, we obtain the flag. 

![](https://i.imgur.com/mFNLfml.png)

## Swaggy
### Problem Type: Authentication Bypass (?)
The webpage was mock *swagger API documentation*

![](https://i.imgur.com/MV2ljYk.png)

The API GET endpoint prints out the flag. However, in order to execute this GET call, we require admin authentication. 

There's a button at the top of the webpage to authenticate, and we try the usual username and password combinations. Turns out - `admin/admin` gives us admin access. Not sure if this is the intended solution. 

![](https://i.imgur.com/VLEJSQJ.png)

We then get the flag for this challenge. 

###### tags: `H@cktivityCon 2021 CTF`, `web`






# Feraidon AbdulRahimzai
## CS338 - Computer Security
## October 25, 2025


## Part 1: Cookies

### a. 
Yes there are two visible cookies for cs338.jeffondich.com. 

1. _dd_s -> logs=1&id=93c987cc-d397-4fde-80eb-5eea3823e094&created=1761419209542&expire=1761420409548

2. theme -> default


### b. 
Yes, the cookies for name value pairs have changed.

1. _dd_s -> logs=1&id=93c987cc-d397-4fde-80eb-5eea3823e094&created=1761419209542&expire=1761420554668

2. theme -> blue


### c. 

Cookie: theme=default
Set-Cookie: theme=blue

And yes, I do see the same cookie values as the inspector.

### d. 
Yes, the theme is still the same color as I set it earlier despite the re-launch of the browser.


### e. 
We can see that the theme is a cookie and both the server and the local browser knows that. It's set to dafault, meaning no changes have been made to it and it will continue to play out like that until the cookie is changed by the change of the theme.

### f. 
Initialy we can see that the browser adds on to it url as so /?theme=blue, once this happened the cookie was saved in my local browser to then redirect me to my saved preferences.

### g. 
Like I mentioned above, we can use the url itself to communicate that we can change this for example one way is to go to the url and change the /?theme= from blue to red. This will also change it in the inspector as well.

### h.
In burpsuite we can use the intercept feature which allows us to change the headers right from the proxy tool. I went into the request headers and changed it from red to blue, then I pressed forward for the request, and it indeed change the theme without doing it on the drop down.

### i.
Burp Suite has it own sort of cookie container called a cookie jar which is stored in the project file and not in the browser profile. As for the OS itself, I read that it doesn't keep a single cookie and that all of the cookies as stored in the brower's profile on the desk. 


## Part 2: Cross-Site Scripting (XSS)

### a. 

- Reflected XSS Attacks
- Stored XSS Attacks
- Blind Cross-site Scripting
- DOM-based XSS 

Link: https://owasp.org/www-community/attacks/xss/


### b.

Look at me with my fancy Javascript. 
```bash
<script>alert('Mwah-ha-ha-ha!');</script>
```

- This is a Stored XSS attack. This is stored on the FDF's server and is later served to any user who views the page containinf Moriarty's post.

[Moriarty ]
       |
       | 1. POST request with malicious payload:
       |    "<script>alert(...)</script>"
       V
[FDF Server ]
       |
       | 2. VULNERABILITY: Server fails to clear it.
       |
       V
 [Database ]
       |
       | 3. Malicious script is STORED.
       |
[Victim ]
       |
       | 4. Normal GET request to view the FDF page.
       |
       V
[FDF Server ]
       |
       | 5. Server retrieves page content,
       |    including the malicious script
       |    from the database.
       |
       V
  [Victim ]
       |
       | 6. Server sends the full HTML
       |    (with the <script>) to the victim's browser.
       |
       V
[Victim's Browser]
       |
       | 7. Browser renders HTML and EXECUTES
       |    the malicious script.
       |
       V
  (Popup Alert!)







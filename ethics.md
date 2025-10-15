Feraidon AbdulRahimzai
CS338 - Computer Security
October 14, 2025



===== Scenario #2 - Beerz2.0 =====


A. The main ethical questions faced by me as the main character in this scenario are as follows:

1. How will this data be stored and kept safe from unwanted acess?
2. Which information to keep from the data? All of the raw data or custom parameters, or minimized?
3. Who are we selling this data to and how safe is this in protecting our users privacy?
4. If we do save the data for more than our one week phase, how long are we archiving it for? And how much space will this take to keep historical data of every single user and their every single move?
5. What should I do? (I do care about peoples privacy and I do want to keep my job.)

Now these are just a few things I could list and I know that this could go on further with it's own ethical implications. But this is sort of a hard decision to make knowing you have so much power in your hand. I could be replaced with someone just as good as me. And we know that there are big companies out there doing the same sort of information archiving/stealing. We know that anthropic was non-legaly scraping websites and the list could go on.



B.

List of Stakeholders and their relevant rights:

- Users/Customers: Expect thier location data to remain private and short-lived

- Development team: Build a privacy-respecting product, maintain professional integrity, and avoid ethical violations that could hurt their careers. A potential harm could be that of mine-Being pressured to violate user trust and/or privacy principles.

- CTO: Protect brand reputation through privacy, ensure legal compliance with privacy laws, most importantly uphold ethical commitments

- CEO: Generate revenue, attract investors, see new business models like selling anonymized data as opportunities

- Investors: Maximize their return on the investmetn

- Breweries: Attract customers, recieve accurate metrics for popularity


C. Some of information that would be useful to me as the developer of Beerz2.0 that is missing from the scenario would be:

- Who we're selling this data to?
- If we do archive this data, how long are we keeping it? 
- Which information are we tokenizing (changing the value to)? Their names? Location history? 
- Are we going to keep a 24hr location history from their phones location sharing?



D. Some actions that I would take to help the app succeed and prevent any sort of information disclosure would be as follows:

1. The very first thing I would do as the ethical/developer person is to expalin the issues that could arise from implementing a feature that stores data. The app/company could collapse if the trust between them and users is broken. This is also good for transparency and decision making for the company despite their short term gains. If this doesn't work then the actions below:
2. Disassociate the users actual identification.
3. If the above does not work, then work on a system that anonymizes the users and generates usernames for them just like reddit, remove device Ids, removes IP addresses, and timestamp patterns that can re-identify user.
4. Create an archiving system that is very secure and no one is able to access it except the admin. 
5. Switch from GET to POST so that the data isn't in the url or logs.



E. The ACM Code of Ethics offers some relevant guidance such as follow:

- Avoid Harm: In our case this could mean that sharing the location data could possibly be associated with people using patterns even if anonymized. Could lead to physical and emotional harm such as stalking, and re-identification.


- Be Honest and trustworthy: If the users figure out that their information is leaked and being misused it could lead to the fall of Beerz and receive backlash from the public. Honesty is an essential part of trustwortiness especially if stated to the user.


- Respect privacy: Location data is deeply personal and users only share it for a single purpose: to find nearby breweries. Selling this data violates the ethical principles of respecting the users proivacy.


- Evaluate risks: Analyze what could go wrong if the data was to be leaked or misused. Write risk reports to the CTO outlining the potencial risks of sellig data.


F. My recommended action to get user data and to be able to sell it without hurting the business and the customers is by sort of making a system which allows location data from the phone only when they are close to each physical brewery. Specifically, instead of constantly tracking user GPS, the Beerz app detects when a user’s phone connects to or is near a brewery’s Wi-Fi network. If they remain in that area for at least 5 minutes, then the app records a “visit” for aggregate analytics. 






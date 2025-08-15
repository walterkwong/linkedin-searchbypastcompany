# linkedin-searchbypastcompany
Just a small little project, intended to populate a database for 180 alumnis on linkedin using Unipile.

## Accessing Unipile: 
1) Sign up on https://dashboard.unipile.com/login.
2) Login to linkedin and copy your `li_at` value in cookies.
3) Link your linkedin account to Unipile's dashboard.
4) Generate a token (no requirements for this). Remember to copy this. 

## Config file: 
There are 5 parameters you will have to fill in on `config.py` before working it works: 
1) **Number**: this is the 5 last digit number in DSN.
2) **Account_id**: this is your linkedin id shown on Unipile's dashboard.
3) **Api_keys**: This is your token generated from Unipile.
4) **Past_Compnay**: this is the company id from linkedin.
5) **Pages**: Number of pages you wish this app to search for. (note: defaulted to 10 searches per page)

Yes I know there's lot more stuff I can do to make this better, I'm just lazy. lmk if u r interested. 
I also have no idea why tf u r here reading this or stalking at me, but sure whatever. 

More links: \
https://www.unipile.com/linkedin-api-a-comprehensive-guide-to-integration/ \
https://developer.unipile.com/reference/linkedincontroller_search

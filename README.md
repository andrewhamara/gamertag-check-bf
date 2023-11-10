A simple python script that checks for the availability of Xbox gamertags.

The site being scraped for gamertags is not guaranteed to be accurate, so you will have to double check whether the gamertags are actually available. 

The script will brute-force it's way through all of the 6-digit (lowercase) combinations.
Or at least try. (See bottom)
The sleep statements, added for assurance, will greatly slow down this process but will likely make sure that the program doesn't crash.

While interesting, solving this with Selenium is somewhat impractical given the need for sleep statements.

The script will calculate all 4, 5, and 6 lowercase permutations of a-z, with repetition.
This means that it will have to check 26^4 + 26^5 + 26^6 = 321,254,128 gamertags for availability.
With the current (seemingly necessary) sleep statements, this means that the script will sleep for 321,254,128 * 7 = 2248778896 seconds = 26027 days = 71 years (that's just the sleeps!). Good things take time.

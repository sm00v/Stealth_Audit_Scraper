# Stealth_Audit_Scraper
This tool was created to scrape the <a href ="https://stealthbits.com/stealthaudit-for-active-directory-product/">StealthAUDIT Active Directory Auditing Tool</a>. Currently, it scrapes the users name and NT account name from `Active Directory > Users > User Token`. I wrote this because I had no foothold on a network and came across this gem. I immedately scraped all AD users then started spraying passwords! Right now this tool only works with passwordless StealthAUDIT instances. Good luck, have fun!

## stealth_scrape.py usage:
```
usage: stealth_audit_scraper.py [-h] [-o OUTFILE] [-u URL] [-p PROXY] [-pp PROXY_PORT]

StealthAUDIT Scraper >:D

optional arguments:
  -h, --help            show this help message and exit
  -o OUTFILE, --outfile OUTFILE
                        The file to write users to.
  -u URL, --url URL     The webserver in format {http://10.0.0.1:80}.
  -p PROXY, --proxy PROXY
                        The proxy ip in format {10.0.0.1}.
  -pp PROXY_PORT, --proxy_port PROXY_PORT
                        The proxy port in format {1080}.
```

   Basic usage of script:
   
    python3 stealth_scrape.py -u http://10.20.8.85 -p 127.0.0.1 -pp 1080 -o accounts.txt

   Advanced usage of linkedin_email_scraper.py:
   
    $ python3 linkedin_email_scraper.py scraper.py -u http://10.15.8.20
    [+] Attempting to visit http://10.15.8.20
    [+] Clearing all cookies...
    [+] Dropping down menu
    NT_Account:contoso\administrator	Name:Administrator
    NT_Account:contoso\susanb	Name:Barin, Susan
    
   Example output of ad_users.txt:
   
    contoso\swilliams:Williams, Susan
    contoso\thawk:Hawk, Tony
    contoso\batman:Man, Bat
    contoso\dnutz:Nutz, Deez
    contoso\kmitnick:Mitnick, Kevin
    contoso\rmudge:Mudge, Raphael
    contoso\tmutton:Mutton, Tim

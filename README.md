# vinted-datadome-solver

## Requeriments
1. Read https://www.capsolver.com/blog/All/how-to-solve-datadome and https://www.capsolver.com/blog/The-other-captcha/datadome-Interstitial-solver
2. Capsolver.com api key
3. Proxy

## We must check the API Endpoint
https://www.vinted.es/api/v2/captchas
https://www.vinted.com/api/v2/captchas

Where says .es or .com will be other country


This API will return 403 and also a url in the response that is called "geo-captcha url"

You must submit this to capsolver.

**CHANGE THIS IN THE CODE**

capsolver.api_key = "your api key of capsolver.com"

PAGE_URL = "https://www.vinted.com/" # Check your country domain, could be vinted.fi or other

CAPTCHA_URL = "GEO CAPTCHA URL OBTAINED FROM https://www.vinted.com/api/v2/captchas / https://www.vinted.es/api/v2/captchas  , vinted.es or vinted.com will change, please check your country"

PROXY = "your proxy"

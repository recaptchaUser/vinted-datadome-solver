import capsolver

capsolver.api_key = "your api key of capsolver.com"
PAGE_URL = "https://www.vinted.com/" # Check your country domain, could be vinted.fi or other
CAPTCHA_URL = "GEO CAPTCHA URL OBTAINED FROM https://www.vinted.com/api/v2/captchas / https://www.vinted.es/api/v2/captchas  , vinted.es or vinted.com will change, please check your country"
PROXY = "your proxy"

def solver_datadome(url, captchaURL, proxy):
    solution = capsolver.solve({
        "type": "DatadomeSliderTask",
        "websiteURL": url,
        "captchaURL": captchaURL,
        "proxy": proxy,
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    })
    
    return solution

def main():
    print("Solving DataDome Vinted")
    # Remember Captcha_URL, the query params must be obtained dynamic, you can't use the same captcha url over and over. Please read our blog to understand how.
    solution = solver_datadome(PAGE_URL, CAPTCHA_URL, PROXY)
    print("Solution: ", solution)
    
    
main()

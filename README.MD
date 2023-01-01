# No more pain with iframes ... 


```python
# Tested with:
# https://github.com/ultrafunkamsterdam/undetected-chromedriver
# Python 3.9.13
# Windows 10

$pip install a-selenium-iframes-crawler


# Here is one example

from a_selenium_iframes_crawler import Iframes
from auto_download_undetected_chromedriver import download_undetected_chromedriver
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    folderchromedriver = "f:\\seleniumdriver2"
    path = download_undetected_chromedriver(
        folder_path_for_exe=folderchromedriver, undetected=True
    )
    driver = uc.Chrome(driver_executable_path=path)
    driver.get(r"https://demo.guru99.com/test/guru99home/")
    getiframes = lambda: Iframes(
        driver,
        By,
        WebDriverWait,
        expected_conditions,
        seperator_for_duplicated_iframe="Ç",
        ignore_google_ads=True,
    )

    driver.switch_to.default_content()
    iframes = getiframes()
    for iframe in iframes.iframes:
        try:
            iframes.switch_to(iframe)
            elemethods = driver.find_elements(By.CSS_SELECTOR, "*")
            print(f"Iframe: {iframe}")
            print(f"{repr(elemethods)[:130]}...")
        except Exception as fe:
            print(fe)
            continue


Iframe: mainframe
[<selenium.webdriver.remote.webelement.WebElement (session="8a063acdf98ac2adab089e34a8ace420", element="78712d03-5629-4518-9609-24...
Iframe: iframe[name="googlefcPresent"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"]
[<selenium.webdriver.remote.webelement.WebElement (session="8a063acdf98ac2adab089e34a8ace420", element="251bc994-ef06-4b19-a0c5-fe...
Iframe: iframe[name="googlefcPresent"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][name="__ccpaLocator"][style="display: none;"]
[<selenium.webdriver.remote.webelement.WebElement (session="8a063acdf98ac2adab089e34a8ace420", element="befaa87e-29be-4184-b9c0-77...
Iframe: iframe[name="googlefcPresent"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][name="__ccpaLocator"][style="display: none;"][name="__uspapiLocator"][style="display: none;"]
[<selenium.webdriver.remote.webelement.WebElement (session="8a063acdf98ac2adab089e34a8ace420", element="c70545fc-68f4-4e87-97aa-1d...
Iframe: iframe[name="googlefcPresent"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][name="__ccpaLocator"][style="display: none;"][name="__uspapiLocator"][style="display: none;"][width="560"][height="315"][wmode="transparent"][src="https://www.youtube.com/embed/RbSlW8jZFe8"][frameborder="0"][allowfullscreen=""]
[<selenium.webdriver.remote.webelement.WebElement (session="8a063acdf98ac2adab089e34a8ace420", element="b28a1c56-1efe-40a3-962b-9c...
Iframe: iframe[name="googlefcPresent"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][name="__ccpaLocator"][style="display: none;"][name="__uspapiLocator"][style="display: none;"][width="560"][height="315"][wmode="transparent"][src="https://www.youtube.com/embed/RbSlW8jZFe8"][frameborder="0"][allowfullscreen=""][id="a077aa5e"][name="a077aa5e"][src="ads.html"][width="750px;"][height="110px;"][scrolling="no"]
[<selenium.webdriver.remote.webelement.WebElement (session="8a063acdf98ac2adab089e34a8ace420", element="80079f87-2c12-488e-9405-29...
Iframe: iframe[name="googlefcPresent"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][name="__ccpaLocator"][style="display: none;"][name="__uspapiLocator"][style="display: none;"][width="560"][height="315"][wmode="transparent"][src="https://www.youtube.com/embed/RbSlW8jZFe8"][frameborder="0"][allowfullscreen=""][id="a077aa5e"][name="a077aa5e"][src="ads.html"][width="750px;"][height="110px;"][scrolling="no"][name="__tcfapiLocator"][src="about:blank"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"]
[<selenium.webdriver.remote.webelement.WebElement (session="8a063acdf98ac2adab089e34a8ace420", element="d88af627-b551-4fd3-8b1e-f7...
Iframe: iframe[name="googlefcPresent"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][name="__ccpaLocator"][style="display: none;"][name="__uspapiLocator"][style="display: none;"][width="560"][height="315"][wmode="transparent"][src="https://www.youtube.com/embed/RbSlW8jZFe8"][frameborder="0"][allowfullscreen=""][id="a077aa5e"][name="a077aa5e"][src="ads.html"][width="750px;"][height="110px;"][scrolling="no"][name="__tcfapiLocator"][src="about:blank"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][name="googlefcInactive"][src="about:blank"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"]
[<selenium.webdriver.remote.webelement.WebElement (session="8a063acdf98ac2adab089e34a8ace420", element="8e187b45-f88f-4013-a979-6a...
Iframe: iframe[name="googlefcPresent"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][name="__ccpaLocator"][style="display: none;"][name="__uspapiLocator"][style="display: none;"][width="560"][height="315"][wmode="transparent"][src="https://www.youtube.com/embed/RbSlW8jZFe8"][frameborder="0"][allowfullscreen=""][id="a077aa5e"][name="a077aa5e"][src="ads.html"][width="750px;"][height="110px;"][scrolling="no"][name="__tcfapiLocator"][src="about:blank"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][name="googlefcInactive"][src="about:blank"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][name="googlefcLoaded"][src="about:blank"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"]
[<selenium.webdriver.remote.webelement.WebElement (session="8a063acdf98ac2adab089e34a8ace420", element="0c34c6b7-a1e7-42e2-93c4-17...
Iframe: iframe[name="googlefcPresent"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][name="__ccpaLocator"][style="display: none;"][name="__uspapiLocator"][style="display: none;"][width="560"][height="315"][wmode="transparent"][src="https://www.youtube.com/embed/RbSlW8jZFe8"][frameborder="0"][allowfullscreen=""][id="a077aa5e"][name="a077aa5e"][src="ads.html"][width="750px;"][height="110px;"][scrolling="no"][name="__tcfapiLocator"][src="about:blank"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][name="googlefcInactive"][src="about:blank"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][name="googlefcLoaded"][src="about:blank"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][src="https://1efcbdddb1978ef4ac56c7131dfaf376.safeframe.googlesyndication.com/safeframe/1-0-40/html/container.html"][style="visibility: hidden; display: none;"]
[<selenium.webdriver.remote.webelement.WebElement (session="8a063acdf98ac2adab089e34a8ace420", element="cb0a7001-1e46-4822-b54b-fb...
Iframe: iframe[name="googlefcPresent"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][name="__ccpaLocator"][style="display: none;"][name="__uspapiLocator"][style="display: none;"][width="560"][height="315"][wmode="transparent"][src="https://www.youtube.com/embed/RbSlW8jZFe8"][frameborder="0"][allowfullscreen=""][id="a077aa5e"][name="a077aa5e"][src="ads.html"][width="750px;"][height="110px;"][scrolling="no"][name="__tcfapiLocator"][src="about:blank"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][name="googlefcInactive"][src="about:blank"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][name="googlefcLoaded"][src="about:blank"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][src="https://1efcbdddb1978ef4ac56c7131dfaf376.safeframe.googlesyndication.com/safeframe/1-0-40/html/container.html"][style="visibility: hidden; display: none;"][src="https://google-bidout-d.openx.net/w/1.0/pd?plm=5"][width="0"][height="0"][style="display:none;"]
[<selenium.webdriver.remote.webelement.WebElement (session="8a063acdf98ac2adab089e34a8ace420", element="91428059-8136-48fc-850b-cc...
Iframe: iframe[name="googlefcPresent"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][name="__ccpaLocator"][style="display: none;"][name="__uspapiLocator"][style="display: none;"][width="560"][height="315"][wmode="transparent"][src="https://www.youtube.com/embed/RbSlW8jZFe8"][frameborder="0"][allowfullscreen=""][id="a077aa5e"][name="a077aa5e"][src="ads.html"][width="750px;"][height="110px;"][scrolling="no"][name="__tcfapiLocator"][src="about:blank"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][name="googlefcInactive"][src="about:blank"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][name="googlefcLoaded"][src="about:blank"][style="display: none; width: 0px; height: 0px; border: none; z-index: -1000; left: -1000px; top: -1000px;"][src="https://1efcbdddb1978ef4ac56c7131dfaf376.safeframe.googlesyndication.com/safeframe/1-0-40/html/container.html"][style="visibility: hidden; display: none;"][src="https://google-bidout-d.openx.net/w/1.0/pd?plm=5"][width="0"][height="0"][style="display:none;"][src="https://gum.criteo.com/syncframe?origin=publishertagids&topUrl=demo.guru99.com&gdpr=0&gdpr_consent=#{"uid":{"origin":0},"lwid":{"origin":0},"bundle":{"origin":0},"optout":{"value":false,"origin":0},"sid":{"origin":0},"tld":"guru99.com","topUrl":"demo.guru99.com","version":132,"cw":true,"lsw":true,"origin":"publishertagids","requestId":"0.1821370865580214"}"][width="0"][height="0"][frameborder="0"][title="Criteo GUM iframe"][style="border-width: 0px; margin: 0px; display: none;"]
[<selenium.webdriver.remote.webelement.WebElement (session="8a063acdf98ac2adab089e34a8ace420", element="692af50d-20a0-435f-a991-1b...


```


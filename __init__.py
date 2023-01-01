import regex


class Iframes:
    iframes = {}
    alltagsonpage = {}

    def __init__(
        self,
        driver,
        By,
        WebDriverWait,
        expected_conditions,
        seperator_for_duplicated_iframe="Ç",
        ignore_google_ads=True,
    ):
        self.By = By
        self.WebDriverWait = WebDriverWait
        self.expected_conditions = expected_conditions
        self.driver = driver
        self.seperator_for_duplicated_iframe = seperator_for_duplicated_iframe
        self.iframes = {}

        self.driver.switch_to.default_content()
        self.ignore_google_ads = ignore_google_ads
        self.iframes["mainframe"] = ""
        self.mainframegemacht = True
        self.__map__([])
        self.driver.switch_to.default_content()

    def __map__(self, path):

        iframesn = self.driver.find_elements(self.By.TAG_NAME, "iframe")
        iframesn = [("iframe", x) for x in iframesn]
        iframes2 = self.driver.find_elements(self.By.TAG_NAME, "frame")
        iframes2 = [("frame", x) for x in iframes2]
        iframesn.extend(iframes2)
        allatributes = []

        for tagname, iframe in iframesn:
            try:
                for attr in iframe.get_property("attributes"):
                    allat = rf"""[{attr['name']}="{attr['value']}"]"""
                    allatributes.append(allat)
            except Exception as Fehler:
                print(Fehler)

            try:
                key = tagname + "".join(allatributes)
                if self.ignore_google_ads:
                    if "google_ads_iframe" in key:
                        continue
                tempnummer = 0
                tempkey = key
                while key in self.iframes:
                    key = (
                        tempkey
                        + self.seperator_for_duplicated_iframe
                        + str(tempnummer).zfill(6)
                    )
                    tempnummer = tempnummer + 1
                if not self.mainframegemacht:
                    self.iframes["mainframe"] = path + [iframe]
                    self.mainframegemacht = True
                elif self.mainframegemacht:
                    self.iframes[key] = path + [iframe]
                self.driver.switch_to.frame(iframe)
                self.__map__(self.iframes[key])
            except Exception as Fehler:
                print(Fehler)
        self.driver.switch_to.parent_frame()

    def switch_to(self, key):
        self.driver.switch_to.default_content()
        if key == "mainframe":
            self.driver.switch_to.default_content()

        if key not in self.iframes:
            self.__map__([])

        if key not in self.iframes:
            try:
                wait = self.WebDriverWait(self.driver, 20)
                regex.sub(rf"{self.seperator_for_duplicated_iframe}\d{{6}}$", "", key)
                wait.until(
                    self.expected_conditions.frame_to_be_available_and_switch_to_it(
                        (self.By.CSS_SELECTOR, key)
                    )
                )
            except Exception as Fehler:
                print(Fehler)

        else:
            for iframe in self.iframes[key]:
                try:
                    self.driver.switch_to.frame(iframe)
                except Exception as Fehler:
                    print(Fehler)

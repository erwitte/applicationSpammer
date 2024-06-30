import re
import Json_Extractor
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def extract_email_and_name(titel_arbeitgeber_refnr):
    driver = webdriver.Firefox()
    url = "https://www.arbeitsagentur.de/jobsuche/jobdetail/"
    for index in range(len(titel_arbeitgeber_refnr)):
        refnr = titel_arbeitgeber_refnr[index][2]
        driver.get(url + str(refnr))
        driver.implicitly_wait(4)
        titel_arbeitgeber_ansprechpartner_email = []
        try:
            if driver.find_element(By.ID, "kontaktdaten-captcha-image"):
                input("captcha")
        except:
            try:
                email = driver.find_element(By.ID, "detail-bewerbung-mail").text
            except:
                continue
            ansprechparner = extract_name(driver.find_element(By.ID, "detail-bewerbung-adresse"))

            print(ansprechparner)


def extract_name(element):
    inner_html = element.get_attribute("innerHTML")
    lines = inner_html.split("<br>")
    unternehmen_pattern = re.compile(r"\b(GmbH|KG|AG|UG|OHG|GbR|e\.V\.|KGaA|PartG|mbH)\b")
    if unternehmen_pattern.search(lines[0]):
        return lines[1]
    else:
        return lines[0]


extract_email_and_name(Json_Extractor.get_relevant_data())

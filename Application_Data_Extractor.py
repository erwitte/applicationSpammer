import re
import Json_Extractor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def extract_email_and_name(titel_arbeitgeber_refnr):
    driver = webdriver.Firefox()
    driver.get("https://www.arbeitsagentur.de/jobsuche/suche?angebotsart=1&was=Backend&wo=Osnabr%C3%BCck&umkreis=50&id=10000-1197601056-S")
    input("captcha")
    titel_arbeitgeber_ansprechpartner_email = []
    email = driver.find_element(By.ID, "detail-bewerbung-mail").text
    ansprechparner = extract_name(driver.find_element(By.ID, "detail-bewerbung-adresse"))
    print(ansprechparner)


def extract_name(element):
    inner_html = element.get_attribute("innerHTML")
    lines = inner_html.split("<br>")
    unternehmen_pattern = re.compile(r"\b(GmbH|KG|AG|UG|OHG|GbR|e\.V\.|KGaA|PartG|mbH)\b")
    if unternehmen_pattern.search(lines[0]):
        name_array = lines[1].split(" ")
        return filter_salutation(name_array)
    else:
        name_array = lines[0].split(" ")
        return filter_salutation(name_array)


def filter_salutation(salutation):
    if salutation[0] == "Frau" or salutation[0] == "Herr":
        return " ".join(salutation[1:])
    else:
        return " ".join(salutation)


extract_email_and_name("a")

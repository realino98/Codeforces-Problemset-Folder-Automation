from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import configparser
import os
from sys import exit

config = configparser.ConfigParser()
config.read("config.ini")
codeforcesfolderpath = config['system']['pathtocodeforces'].replace("\\", "/")

#Global Variables
os.system("cls")
print("Initializing")
root = os.getcwd()
PATH = os.getcwd() + '/webdriver/chromedriver.exe'
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-logging'])
driver_service = Service(executable_path=PATH)
# driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service, service_log_path=None, options=option)
driver.minimize_window()

def menu():
    print("Code forces Parser")
    print("Enter problemset link: ")
    print()

def create(link):
    driver.get(link)
    text_title = driver.find_element(By.CSS_SELECTOR, '#pageContent > div.problemindexholder > div.ttypography > div > div.header > div.title').text
    text_problem = driver.find_element(By.CSS_SELECTOR, '#pageContent > div.problemindexholder > div.ttypography > div > div:nth-child(2)').text
    text_input = driver.find_element(By.CSS_SELECTOR, '#pageContent > div.problemindexholder > div.ttypography > div > div.input-specification').text
    text_output = driver.find_element(By.CSS_SELECTOR, '#pageContent > div.problemindexholder > div.ttypography > div > div.output-specification').text
    text_examples = driver.find_element(By.CSS_SELECTOR, '#pageContent > div.problemindexholder > div.ttypography > div > div.sample-tests > div.sample-test').text
    text_examples = text_examples.split("\n")
    text_examples = [i for i in text_examples if i != "Copy"]
    # print(text_examples)
    print(text_title)
    directory_path = f"{codeforcesfolderpath}/{text_title}"
    os.mkdir(directory_path)
    #Create Folder
    f = open(f'{directory_path}/main.py', "x")
    f.write("#Problem Link:"+link)
    f.close()
    print("Folder generated succesfully at", directory_path)
    driver.close()

def main():
    menu()
    link = input()
    create(link)
    exit()
main()
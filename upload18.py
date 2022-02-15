import tkinter
import subprocess
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font
from turtle import width
from PIL import ImageTk, Image
import urllib.request
from io import BytesIO
import os
import io
import sys
import pickle
import time
from decimal import *
import webbrowser
# from click import command
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from datetime import timedelta  
from dateutil.relativedelta import relativedelta
from datetime import timedelta, date
import locale
import json 
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#check local date format
locale.setlocale(locale.LC_ALL, '')
lastdate = date(date.today().year, 12, 31)

root = Tk()
root.geometry('750x850')
root.resizable(False, False)
root.title("NFTs Upload to OpenSea v1.8.1")
  
input_save_list = ["NFTs folder :", 0, 0, 0, 0, 0, 0, 0, 0, 0]
main_directory = os.path.join(sys.path[0])


def supportURL():
    webbrowser.open_new("https://www.infotrex.net/opensea/support.asp?r=app")

def coffeeURL():
    webbrowser.open_new("https://github.com/infotrex/bulk-upload-to-opensea/#thanks")

class WebImage:
    def __init__(self, url):
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
        #self.image = tk.PhotoImage(data=base64.encodebytes(raw_data))
        image = Image.open(io.BytesIO(raw_data))
        self.image = ImageTk.PhotoImage(image)

    def get(self):
        return self.image
imageurl = "https://www.infotrex.net/opensea/header.png"
img = WebImage(imageurl).get()
imagelab = tk.Label(root, image=img)
imagelab.grid(row=0, columnspan=2)
imagelab.bind("<Button-1>", lambda e:supportURL())

is_polygon = BooleanVar()
is_polygon.set(True)

is_listing = BooleanVar()
is_listing.set(True) 

is_numformat = BooleanVar()
is_numformat.set(False) 


def save_duration():
    duration_value.set(value=duration_value.get())
    # print(duration_value.get())

def open_chrome_profile():
    subprocess.Popen(
        [
            "start",
            "chrome",
            "--remote-debugging-port=8989",
            "--user-data-dir=" + main_directory + "/chrome_profile",
        ],
        shell=True,
    )


def save_file_path():
    return os.path.join(sys.path[0], "Save_gui.cloud") 


# ask for directory on clicking button, changes button name.
def upload_folder_input():
    global upload_path
    upload_path = filedialog.askdirectory()
    Name_change_img_folder_button(upload_path)

def Name_change_img_folder_button(upload_folder_input):
    upload_folder_input_button["text"] = upload_folder_input

def is_numeric(val):
	if str(val).isdigit():
		return True
	elif str(val).replace('.','',1).isdigit():
		return True
	else:
		return False


class InputField:
    def __init__(self, label, row_io, column_io, pos,  master=root):
        self.master = master
        self.input_field = Entry(self.master, width=60)
        self.input_field.grid(ipady=3)
        self.input_field.label = Label(master, text=label, anchor="w", width=20, height=1 )
        self.input_field.label.grid(row=row_io, column=column_io, padx=12, pady=2)
        self.input_field.grid(row=row_io, column=column_io + 1, padx=12, pady=2)
        
        try:
            with open(save_file_path(), "rb") as infile:
                new_dict = pickle.load(infile)
                self.insert_text(new_dict[pos])
        except FileNotFoundError:
            pass
        
    def insert_text(self, text):
        self.input_field.delete(0, "end")
        self.input_field.insert(0, text)

    def save_inputs(self, pos):
        #messagebox.showwarning("showwarning", "Warning")
        input_save_list.insert(pos, self.input_field.get())
        #print(self.input_field.get())
        with open(save_file_path(), "wb") as outfile:
            pickle.dump(input_save_list, outfile)
            
    def validate_inputs(self, maxlen, type, message):

        if type == 0 and (len(self.input_field.get()) == 0 or (self.input_field.get()).isdigit() != True or len(self.input_field.get()) > maxlen):
            messagebox.showwarning("showwarning", message)
                
        elif type == 1 and (len(self.input_field.get()) == 0 or is_numeric(self.input_field.get()) == False or len(self.input_field.get()) >= maxlen):
            messagebox.showwarning("showwarning", message)       
                
        elif type == 2 and ( len(self.input_field.get()) == 0 or len(self.input_field.get()) > maxlen):
            messagebox.showwarning("showwarning", message)
               
        else:
            return True     
        

###input objects###
collection_link_input = InputField("OpenSea Collection Link:", 2, 0, 1)
start_num_input = InputField("Start Number:", 3, 0, 2)
end_num_input = InputField("End Number:", 4, 0, 3)
price = InputField("Default Price:", 5, 0, 4)
title = InputField("Title:", 6, 0, 5)
description = InputField("Description:", 7, 0, 6)
file_format = InputField("NFT Image Format:", 8, 0, 7)
external_link = InputField("External link:", 9, 0, 8)


def save():

    if len(start_num_input.input_field.get()) == 0 or len(end_num_input.input_field.get()) == 0 or (int(end_num_input.input_field.get()) < int(start_num_input.input_field.get())):
        #messagebox.showwarning("showwarning", "End number should greater than start number!")
        print ("true")
    elif len( start_num_input.input_field.get()) == 0 or len(end_num_input.input_field.get()) > 5 :
        #messagebox.showwarning("showwarning", "Start / end number range 0 - 99999")
        print ("true")
    else:
        collection_link_input.validate_inputs(200, 2, 'Collection link required')
        price.validate_inputs(100, 1, 'Price required')
        title.validate_inputs(100, 2, 'title required')
        description.validate_inputs(200, 2, 'description required')
        file_format.validate_inputs(100, 2, 'file format required - png, jpg, jpeg')
        external_link.validate_inputs(100, 3, '')
     

    input_save_list.insert(0, upload_path)
    collection_link_input.save_inputs(1)
    start_num_input.save_inputs(2)
    end_num_input.save_inputs(3)
    price.save_inputs(4)
    title.save_inputs(5)
    description.save_inputs(6)
    file_format.save_inputs(7)
    external_link.save_inputs(8)
    

    

def main_program_loop():

    if len(end_num_input.input_field.get()) > 5 :
        messagebox.showwarning("showwarning", "Start / end number range 0 - 99999")
        sys.exit()

    project_path = main_directory
    file_path = upload_path
    collection_link = collection_link_input.input_field.get()
    start_num = int(start_num_input.input_field.get())
    end_num = int(end_num_input.input_field.get())
    loop_price = float(price.input_field.get())
    loop_title = title.input_field.get()
    loop_file_format = file_format.input_field.get()
    loop_external_link = str(external_link.input_field.get())
    loop_description = description.input_field.get()

    ##chromeoptions
    opt = Options()
    opt.add_argument('--headless')
    opt.add_experimental_option("debuggerAddress", "localhost:8989")
    # driver = webdriver.Chrome(
    #     executable_path=project_path + "/chromedriver.exe",
    #     chrome_options=opt,
    # )
    driver = webdriver.Chrome( service=Service(project_path + "/chromedriver.exe"), options=opt, )
    wait = WebDriverWait(driver, 60)

    ###wait for methods
    def wait_css_selector(code):
        wait.until(
            ExpectedConditions.presence_of_element_located((By.CSS_SELECTOR, code))
        )
        
    def wait_css_selectorTest(code):
        wait.until(
            ExpectedConditions.elementToBeClickable((By.CSS_SELECTOR, code))
        )    

    def wait_xpath(code):
        wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, code)))


    while end_num >= start_num:
        if is_numformat.get():
            start_numformat = f"{ start_num:04}"
        else:
             start_numformat = f"{ start_num:01}"

        print("Start creating NFT " +  loop_title + str(start_numformat))
        print('number ',  start_numformat)
        driver.get(collection_link)
        
        
        wait_xpath('//*[@id="media"]')
        imageUpload = driver.find_element(By.XPATH, '//*[@id="media"]')
        imagePath = os.path.abspath(file_path + "\\images\\" + str(start_numformat) + "." + loop_file_format)  # change folder here
        imageUpload.send_keys(imagePath)
        time.sleep(0.8)

        name = driver.find_element(By.XPATH, '//*[@id="name"]')
        name.send_keys(loop_title + str(start_numformat))  # +1000 for other folders #change name before "#"
        time.sleep(0.8)

        ext_link = driver.find_element(By.XPATH, '//*[@id="external_link"]')
        ext_link.send_keys(loop_external_link)
        time.sleep(0.8)

        desc = driver.find_element(By.XPATH, '//*[@id="description"]')
        desc.send_keys(loop_description)
        time.sleep(0.8)

        jsonFile = file_path + "/json/"+ str(start_numformat) + ".json"
        if os.path.isfile(jsonFile) and os.access(jsonFile, os.R_OK):
           
            #print(str(jsonMetaData))
            wait_css_selector("button[aria-label='Add properties']")
            properties = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Add properties']")
            driver.execute_script("arguments[0].click();", properties)
            time.sleep(0.8)

            # checks if file exists
            jsonData = json.loads(open(file_path + "\\json\\"+ str(start_numformat) + ".json").read())
            
            if "attributes" in jsonData:
                jsonMetaData = jsonData['attributes']

                for key in jsonMetaData:
                    input1 = driver.find_element(By.XPATH, '//tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[1]/div/div/input')
                    input2 = driver.find_element(By.XPATH, '//tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[2]/div/div/input')
                    #print(str(key['trait_type']))
                    #print(str(key['value']))
                    input1.send_keys(str(key['trait_type']))
                    input2.send_keys(str(key['value']))
                    addmore_button = driver.find_element(By.XPATH, '//button[text()="Add more"]')
                    driver.execute_script("arguments[0].click();", addmore_button)
                time.sleep(0.9)

                driver.find_element(By.XPATH, '//button[text()="Save"]').click()
                time.sleep(0.8)

            elif "properties" in jsonData:
                jsonMetaData = jsonData['properties']
                
                for key in jsonMetaData:
                    input1 = driver.find_element(By.XPATH, '//tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[1]/div/div/input')
                    input2 = driver.find_element(By.XPATH, '//tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[2]/div/div/input')
                    #print(str(key['type']))
                    #print(str(key['name']))
                    input1.send_keys(str(key['type']))
                    input2.send_keys(str(key['name']))
                    addmore_button = driver.find_element(By.XPATH, '//button[text()="Add more"]')
                    driver.execute_script("arguments[0].click();", addmore_button)
                time.sleep(0.9)

                driver.find_element(By.XPATH, '//button[text()="Save"]').click()
                time.sleep(0.8)

            else:
                print("keys not found!") 

        # Select Polygon blockchain if applicable
        #if is_polygon.get():

        create = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/div/div[1]/span/button')
        driver.execute_script("arguments[0].click();", create)
        time.sleep(0.8)

        try:
            time.sleep(10)
            cross = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]/button/i')
            cross.click()
            time.sleep(0.8)
        except:
            wait_xpath('/html/body/div[5]/div/div/div/div[2]/button/i')
            cross = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/button/i')
            cross.click()
            time.sleep(0.8)

        main_page = driver.current_window_handle

        if is_listing.get():
            
            wait_xpath('//a[text()="Sell"]')
            sell = driver.find_element(By.XPATH, '//a[text()="Sell"]')
            driver.execute_script("arguments[0].click();", sell)
            
            wait_css_selector("input[placeholder='Amount']")
            amount = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Amount']")
            amount.send_keys(str(loop_price))
            time.sleep(1)

            #duration
            duration_date = duration_value.get()
            #print(duration_date)
            # time.sleep(60)
            if duration_date == 1 : 
                endday = (date.today() + timedelta(days=1)).day
                endmonth = (date.today() + timedelta(days=1)).month
                #print(endday, endmonth)
            if duration_date == 3 : 
                endday = (date.today() + timedelta(days=3)).day
                endmonth = (date.today() + timedelta(days=3)).month
                #print(endday, endmonth)
            if duration_date == 7 : 
                endday = (date.today() + timedelta(days=7)).day
                endmonth = (date.today() + timedelta(days=7)).month   
                #print(endday, endmonth)       
            if duration_date == 30:
                endday = (date.today() + relativedelta(months=+1)).day
                endmonth = (date.today() + relativedelta(months=+1)).month
                #print(endday, endmonth)
            if duration_date == 60:
                endday = (date.today() + relativedelta(months=+2)).day
                endmonth = (date.today() + relativedelta(months=+2)).month
                #print(endday, endmonth)
            if duration_date == 90:
                endday = (date.today() + relativedelta(months=+3)).day
                endmonth = (date.today() + relativedelta(months=+3)).month
                #print(endday, endmonth)
            if duration_date == 120:
                endday = (date.today() + relativedelta(months=+4)).day
                endmonth = (date.today() + relativedelta(months=+4)).month  
                #print(endday, endmonth) 
            if duration_date == 150:
                endday = (date.today() + relativedelta(months=+5)).day
                endmonth = (date.today() + relativedelta(months=+5)).month  
                #print(endday, endmonth)  
            if duration_date == 180:
                endday = (date.today() + relativedelta(months=+6)).day
                endmonth = (date.today() + relativedelta(months=+6)).month   
                #print(endday, endmonth)

            #if duration_date != 30:
            amount.send_keys(Keys.TAB)
            time.sleep(0.8)
            # wait_xpath('//*[@id="duration"]')
            # driver.find_element_by_xpath('//*[@id="duration"]').click()
            
            wait_xpath('//*[@role="dialog"]/div[2]/div[2]/div/div[2]/input')
            select_durationday = driver.find_element(By.XPATH, '//*[@role="dialog"]/div[2]/div[2]/div/div[2]/input')
            driver.execute_script("arguments[0].click();", select_durationday)
            time.sleep(0.8)
            
            if lastdate.strftime('%x')[:2] == "12":
                #print("is month first")
                select_durationday.send_keys(str(endmonth))
                select_durationday.send_keys(str(endday))
                select_durationday.send_keys(Keys.ENTER)
                time.sleep(1)
            elif lastdate.strftime('%x')[:2] == "31":
                #print("is day first")
                select_durationday.send_keys(str(endday))
                select_durationday.send_keys(str(endmonth))
                select_durationday.send_keys(Keys.ENTER)
                time.sleep(1)
            else:
                print("invalid date format: change date format to MM/DD/YYYY or DD/MM/YYYY")

            wait_css_selector("button[type='submit']")
            listing = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            driver.execute_script("arguments[0].click();", listing)
            time.sleep(10)
            
            if is_polygon.get():
                driver.find_element(By.XPATH, '//button[text()="Sign"]').click()
                time.sleep(1)

            for handle in driver.window_handles:
                if handle != main_page:
                    login_page = handle
                    #break
            # change the control to signin page
            driver.switch_to.window(login_page)
            wait_css_selector("button[data-testid='request-signature__sign']")
            sign = driver.find_element(By.CSS_SELECTOR, "button[data-testid='request-signature__sign']")
            driver.execute_script("arguments[0].click();", sign)
            time.sleep(1)

  
        #change control to main page
        driver.switch_to.window(main_page)
        time.sleep(0.7)

        start_num = start_num + 1
        print('NFT creation completed!')
    
    driver.get("https://www.opensea.io")
    


duration_value = IntVar()
duration_value.set(value=180)

duration_date = Frame(root, padx=0, pady=1)
duration_date.grid(row=10, column=1, sticky=(N, W, E, S))
tk.Radiobutton(duration_date, text='1 day', variable=duration_value, value=1, anchor="w", command=save_duration, width=8,).grid(row=0, column=1)
tk.Radiobutton(duration_date, text="3 days", variable=duration_value, value=3, anchor="w", command=save_duration, width=8, ).grid(row=0, column=2)
tk.Radiobutton(duration_date, text="7 days", variable=duration_value, value=7, anchor="w", command=save_duration, width=8,).grid(row=0, column=3)
tk.Radiobutton(duration_date, text="30 days", variable=duration_value, value=30, anchor="w", command=save_duration, width=8,).grid(row=0, column=4)
tk.Radiobutton(duration_date, text="60 days", variable=duration_value, value=60, anchor="w", command=save_duration, width=8,).grid(row=0,  column=5)
tk.Radiobutton(duration_date, text="90 days", variable=duration_value, value=90, anchor="w",command=save_duration,  width=8,).grid(row=1, columnspan=1, column=1)
tk.Radiobutton(duration_date, text="120 days", variable=duration_value, value=120, anchor="w", command=save_duration, width=8).grid(row=1, columnspan=1, column=2)
tk.Radiobutton(duration_date, text="150 days", variable=duration_value, value=150, anchor="w", command=save_duration, width=8).grid(row=1, columnspan=1, column=3)
tk.Radiobutton(duration_date, text="180 days", variable=duration_value, value=180, anchor="w", command=save_duration, width=8).grid(row=1, columnspan=1, column=4)
duration_date.label = Label(root, text="Duration:", anchor="w", width=20, height=1 )
duration_date.label.grid(row=10, column=0, padx=12, pady=2)


# isnumFormat = tkinter.Checkbutton(root, text='Number format 0001 ~ 99999', var=is_numformat,   width=49, anchor="w")
# isnumFormat.grid(row=18, column=1)
isCreate = tkinter.Checkbutton(root, text='Complete Listing', var=is_listing, width=49, anchor="w")
isCreate.grid(row=19, column=1)
isPolygon = tkinter.Checkbutton(root, text='Polygon Blockchain',  var=is_polygon, width=49, anchor="w")
isPolygon.grid(row=20, column=1)
upload_folder_input_button = tkinter.Button(root, width=50, height=1,  text="Add NFTs Upload Folder", command=upload_folder_input)
upload_folder_input_button.grid(row=21, column=1, padx=2)
open_browser = tkinter.Button(root, width=50, height=1,  text="Open Chrome Browser", command=open_chrome_profile)
open_browser.grid(row=23, column=1, pady=2)
button_save = tkinter.Button(root, width=50, height=1,  text="Save This Form", command=save) 
button_save.grid(row=22, column=1, pady=2)
button_start = tkinter.Button(root, width=44, height=2, bg="green", fg="white", text="Start", command=main_program_loop)
button_start['font'] = font.Font(size=10, weight='bold')
button_start.grid(row=25, column=1, pady=2)
footer = tkinter.Button(root, height=3, width=60, text='Do you you want to show support? \n Now you have the chance to buy me a coffee. Thank you.',  command=coffeeURL, relief=GROOVE  )
footer.grid(row=31, columnspan=2, padx=31, pady=31)

try:
    with open(save_file_path(), "rb") as infile:
        new_dict = pickle.load(infile)
        global upload_path
        Name_change_img_folder_button(new_dict[0])
        upload_path = new_dict[0]
except FileNotFoundError:
    pass
#####BUTTON ZONE END#######
root.mainloop()

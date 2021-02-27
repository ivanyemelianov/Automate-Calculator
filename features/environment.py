from appium import webdriver
from app.application import Application

def before_scenario(context, scenario):

    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "9",
        "deviceName": "Android Emulator",
        "app": "/Users/dariasamarets/Workspace/Appium-Automation/Automate-Calculator/app_binaries/Calculator_v7.8 (271241277)_apkpure.com.apk",
    }
    context.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_capabilities)
    context.app = Application(context.driver)
    context.driver.implicitly_wait(10)

def after_scenario(context, scenario):
    context.driver.quit()

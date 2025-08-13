options = webdriver.ChromeOptions()
prefs = {"download.default_directory": "C:/Downloads"}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)
driver.get("https://file-examples.com/index.php/sample-documents-download/")

#Paqueterias y herramientas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import statistics as st

#driver y herramienta para el uso de selenium
path = 'C:/Users/chay9/OneDrive/Desktop/chromedriver.exe'
options = webdriver.ChromeOptions()
options.headless = True

#Pagina donde se esta sacando información
driver = webdriver.Chrome(path)
driver.get('https://ciudadjuarez.locanto.com.mx/Autos/902/')

#Elementos que se sacan de la pagina
servicios_title = driver.find_elements(By.XPATH,"//h3[@class='bp_ad__title']") 
servicios_title = [ serv.text for serv in servicios_title ]

servicios_price = driver.find_elements(By.XPATH, "//div[@class='bp_ad__price']")
servicios_price = [ pri.text for pri in servicios_price ] 

servicios_info = driver.find_elements(By.XPATH, "//a[@class='bp_ad__desc_link']")
servicios_info = [ inf.text for inf in servicios_info ]


#if len(servicios_title) != len(servicios_price):
 #   if len(servicios_title) > len(servicios_price):
  #      mean_width = st.mean(servicios_price)
   #     servicios_price += (len(servicios_title)-len(servicios_price)) * [mean_width]
    #elif len(servicios_title) < len(servicios_price):
     #   mean_width = st.mean(servicios_title)
      #  servicios_title += (len(servicios_price)-len(servicios_title)) * [mean_width]

#Verificar quelas cadenas tengan el mismo tamaño
print(len(servicios_info), len(servicios_price), len(servicios_title))


#Generacion del archivo CSV
Publicaciones = {
    "Titulo": servicios_title,
    "Precio": servicios_price,
    "Informacion": servicios_info
}
#Genera el archivo CSV
df = pd.DataFrame.from_dict(Publicaciones, orient='index')
df.to_csv("Publicaciones.csv")



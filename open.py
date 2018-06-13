import webbrowser
import time

data = ["https://weather.com/weather/today/l/USMS0175:1:US", "https://climate.nasa.gov/vital-signs/sea-level/", "http://www.cnn.com/", 
            "https://www.warsintheworld.com/?page=static1258254223" ]

g = webbrowser.get('chrome')

def open_tabs(url_list):
    for tabs in url_list:
        g.open_new_tab(tabs)

def main():
    g.open("http://www.worldometers.info/world-population/", new=1, autoraise=False)
    time.sleep(1)
    open_tabs(data) 

main()


# If new is 0, the url is opened in the same browser window if possible.
# If new is 1, a new browser window is opened if possible. 
# If new is 2, a new browser page (“tab”) is opened if possible.
# If autoraise is True, the window is raised if possible

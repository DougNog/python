import webbrowser

#informe a URL do site que deseja abrir
url = "....................."

download = url [:12] + "ss"  + url [12:]

webbrowser.open(download)

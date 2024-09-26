import urllib.request as URL
import zipfile
import re

url = "https://www.aozora.gr.jp/cards/000081/files/456_ruby_145.zip"
zip = "gingatetsudo.zip"

URL.urlretrieve(url, zip)

with zipfile.ZipFile(zip, "r") as myzip:
    myzip.extractall()

    for myfile in myzip.infolist():
        filename = myfile.filename

        with open(filename, encoding="sjis") as file:
            text = file.read()

text = re.split("\\-{5,}",text)[2]
text = re.split("底本：",text)[0]
text = text.replace("|", "")
text = re.sub("《.+?》","",text)
text = re.sub("［＃.+?］", "", text)
text = re.sub("\n\n", "\n", text)
text = re.sub("\r", "", text)

print(text[:100])
print()
print()
print(text[-100:])
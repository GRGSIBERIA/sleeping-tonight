import bz2, io, sys
from lxml import etree 

if __name__ == "__main__":
    path = sys.argv[1]

    """
    with-open-as構文で書こうと思ったけど
    エラーが発生するため仕方なくxmlのハンドルは握ったままにする
    """
    try:
        xml = etree.parse(path)
        root = xml.getroot()
    except:
        print("Invalid Reading XML")
        sys.exit()

    print(root.tag)

    try:
        export_date = xml.xpath("/HealthData/ExportDate")[0].attrib["value"]
    except:
        print("HealthData has not ExportDate")
    
    print(export_date)
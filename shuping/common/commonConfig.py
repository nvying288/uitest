import configparser
import os


class CommonConfig:

    def getPath(self):
        try:
            root_path = os.path.dirname(os.path.abspath('.') + '/config/chromedriver/chromedriver')
            return root_path
        except:
            print("获取path失败!")


    def getUrl(TypeUrl, urlName):
        try:
            config = configparser.ConfigParser()
            urlconfig = os.path.dirname(os.path.abspath('.') + '/config/config.ini/config.ini')
            config.read(urlconfig)
            url = config.get(TypeUrl, urlName)
        except:
            print("获取url失败!")
        return url




if __name__ == '__main__':
    CommonConfig.getUrl("TypeUrl", "baiduUrl")



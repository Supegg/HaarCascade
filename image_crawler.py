from icrawler.builtin import BingImageCrawler

# we are building cats image detection that's why we put cat here
# if you want some other images then put that name in classes list
classes = ['cats', 'dogs']
number = 100

# here root directory is find your root directory there u will find
# new file name data in which all images are saved.
for c in classes:
    bing_crawler = BingImageCrawler(downloader_threads=4, storage={
                                    'root_dir': f'p/{c.replace(" ",".")}'})  # p means positive
    bing_crawler.crawl(keyword=c, filters=None, max_num=number, offset=0)

# download negative images
classes = ['trees', 'roads', 'Human faces']
number = 100
for c in classes:
    bing_crawler = BingImageCrawler(
        storage={'root_dir': f'n/{c.replace(" ",".")}'})  # n means negative
    bing_crawler.crawl(keyword=c, filters=None, max_num=number, offset=0)


# icrawler usage: https://blog.csdn.net/zaf0516/article/details/115374438

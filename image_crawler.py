from icrawler import ImageDownloader
from icrawler.builtin import GoogleImageCrawler

MBTI = "ISTJ"
IMAGE_NUBMER = 6

# get query input from txt file
with open('query_'+MBTI+'.txt', 'r') as f:
    query = f.read().splitlines()

# download images labeled with increasing numbers
for i, q in enumerate(query):
    q+= " front face"
    google_crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4,
        storage={'root_dir': MBTI +'/'})
    filters = dict(
        type="face",
        size="medium",
    )
    google_crawler.crawl(
        keyword=q,
        filters=filters,
        max_num=IMAGE_NUBMER,
        file_idx_offset=i*IMAGE_NUBMER)

    print('done with ' + q)

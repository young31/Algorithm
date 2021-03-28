## 미해결
# input
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
# pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
# answer: 

# algo
from html.parser import HTMLParser
class CustomParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.bodies = []

    def handle_starttag(self, tag, attrs):
        # print("start tag:", tag)
        # if tag == 'body':
        #     print(self.handle_data(attrs))
        for a, contents in attrs:
            if a == 'content':
                self.url = contents[8:]
                # print(self.url)
            elif a == 'href':
                self.links.append(contents[8:])
            # print(a, contents)

    def handle_endtag(self, tag):
        # print("Encountered an end tag :", tag)
        pass

    def handle_data(self, data):
        data = data.strip()
        if data != '\n' and data:
            self.bodies.append(data)
        # return data
        pass

print(pages[0].split('\n'))
print(pages[1].split('\n'))

print("(!?k<!=k[k^!ak-kz!A!-kZk]k)k{!mkukzki!}k[k^ka!-kzkAk-!Z!]k".replace("!","").replace("k",""))
# for page in pages:
#     parser = CustomParser()
#     parser.feed(page)
#     print(parser.bodies)
#     print(parser.url)
#     print(parser.links)
#     print()
    # break

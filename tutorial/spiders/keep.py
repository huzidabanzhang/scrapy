import scrapy


class KeepSpider(scrapy.Spider):
    name = 'keep'
    # allowed_domains = ['api.gotokeep.com']
    # start_urls = ['https://api.gotokeep.com/course/v1/discover?category=yoga&courseRank=1']

    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1Y2FjNDgxMjc5MGI5MzAzYWE5NTc5OTciLCJ1c2VybmFtZSI6IuWPm-mAhueahOeroOiDluiDliIsImF2YXRhciI6Imh0dHA6Ly9zdGF0aWMxLmdvdG9rZWVwLmNvbS9hdmF0YXIvMjAxOS8wNS8xNi8wOS9iY2UxMjlmYjY3NjJhZTdlNzY1MDliYTY2OWY2OTcxYzQ5MWRiNGIyLmpwZyIsIl92IjoiMSIsIl9lZCI6IllZVlJ4bkZUaTRIZTZZOHhIdDlKN0VLWlU5M3FiZ2VuVkR0SjArL1NuVjVaMEFIRFlscEdjYkpPbldsSVEvMDAiLCJnZW5kZXIiOiJNIiwiZGV2aWNlSWQiOiIiLCJpc3MiOiJodHRwOi8vd3d3LmdvdG9rZWVwLmNvbS8iLCJleHAiOjE2NDAzOTU2MTYsImlhdCI6MTYxNzA2NzYxNn0.u77Ec2fQ3je1m0V2oj3WCM8q2AZyNiEJtucdmMvbgjo'
    }

    def start_requests(self):
        url = 'https://api.gotokeep.com/course/v1/discover?category=yoga&courseRank=1'
        yield scrapy.Request(url, method='GET', callback=self.parse_type, headers=self.headers)

    def parse_type(self, response):
        print(response.body)

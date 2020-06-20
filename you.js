var request = require('request'),
    cheerio = require('cheerio');

var url = "http://codenamu.org/blog/";

request(url, function (err, res, html) {
    if (!err) {
        var $ = cheerio.load(html);
        
        // 블로그 title 정보 가져오기
        $(".entry-title > a").each(function () {
            var post = {"title": "", "link": "", "summary": "", "category": []};
            var data = $(this);
            
            post["title"] = data.text();
            post["link"] = data.attr("href");
        });
        
        // 블로그 요약 정보 가져오기
        $(".entry-summary > p").each(function (i) {
            // do something
        })
 
        // 블로그 카테고리 가져오기
        $(".entry-categories").each(function (i) {
            $(this).children('a').each(function () {
                // do something
            });
        })
    }
})

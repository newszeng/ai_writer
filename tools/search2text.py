# from libs import TerrySearch
import libs
import fun
import tqbm
ARTICLE_PATH ="./data/wikitext/"
# PATH ="/media/terry/65F33762C14D581B/tdata/wiki_zh/"

#开始运行
# libs.TerrySearch().start(path='/home/terry/pan/github/terry_search_web/terry_search_web/data/article/')
# libs.TerrySearch().init_search()

# libs.TerrySearch().start(path='/home/terry/pan/github/terry_search_web/terry_search_web/data/article/')
#搜索

# import jieba
text ="犬"
# seg_list = jieba.cut_for_search(text)  # 搜索引擎模式
# # print(", ".join(seg_list))
# text=" ".join(seg_list)
r= libs.TerrySearch().search(text=text,limit=10)
# print(len(r))
to =ARTICLE_PATH
for item in r:
    print(item['data']['path'])
    copyfile(item['data']['path'], to)



# from whoosh.index import create_in
# from whoosh.fields import *
# schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
# ix = create_in("indexdir", schema)
# writer = ix.writer()
# writer.add_document(title=u"First document", path=u"/a",
#                      content=u"柯基犬 就是 牛 This is the first document we've added!")
# writer.add_document(title=u"Second document", path=u"/b",
#                      content=u"The second one is even more interesting!")
# writer.commit()
# from whoosh.qparser import QueryParser
# with ix.searcher() as searcher:
#      query = QueryParser("content", ix.schema).parse("柯基犬")
#      results = searcher.search(query)
#      if len(results)>0:
#         print(results[0])
#      print(results[0])


# # from whoosh.query import *

# # myquery = parser.parse(u"柯基犬 牛")
# # # myquery = And([Term("content", u"柯基犬"), Term("content",u"牛")])

# # results = searcher.search(myquery)
# # print(len(results))
# # print(results[0])

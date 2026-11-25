import yfinance as yf
from pymongo import MongoClient
import os
import json
from datetime import datetime, timezone

stocknames = [
    "AAPL", "MSFT", "NVDA", "AVGO", "CSCO", "ADBE", "CRM", "ORCL", 
    # "INTC", "QCOM", "AMD", "ADP", "CDNS", 
    # "SNPS", "KLAC", "LRCX", "AMAT", "V", "MA", "HPQ", "DELL", "FFIV",
    # "JPM", "BAC", "WFC", "GS", "MS", "AXP", "SPGI", "CME", 
    # "ICE", "BLK", "PNC", "XOM", "CVX", "FCX"
    # "JNJ", "UNH", "LLY", "PFE", "ABT", "DHR", "ISRG", 
    # "BIIB", "AMGN", "GILD", "MDT",  "CI",
    # "AMZN", "TSLA", "HD", "MCD", "NKE", "SBUX", "LOW", "BKNG", "MAR", 
    # "TJX", "PG", "KO", "CL", "KMB", "KR", "MDLZ",
    "GE", "HON", "BA", "NEE", "DUK", "SO", "EIX", "PLD",
]

class NewsItem:
    def __init__(self,title:str,content:str):
        self.title:str = title
        self.content:str = content
        self.date:datetime = datetime.now(timezone.utc)

def getNews(tickerName:str) -> list[dict]:
    ticker = yf.Ticker(tickerName)
    news = []
    try:
        newsData = ticker.get_news(10,tab="press releases")
        
        for n in newsData:
            content = n["content"]
            title = content["title"]
            summary = content["summary"]
            news.append(transformToDoc(NewsItem(title,summary)))
    except Exception as e:
        print(e)
    return news

def transformToDoc(newsItem:NewsItem) -> dict:
    return {
        "content":newsItem.content,
        "title":newsItem.title,
        "date":newsItem.date
            }

def main():
    NEWS_COL_NAME = "news"
    print("[LOG] Adding initial articles, the rest should be fetched by a cron job or something")
    with open("appsettings.json","r",encoding="utf-8") as f:
        config = json.load(f)
        conn_str = config["MongoSettings"]["ConnectionString"]
        client = MongoClient(conn_str)
        db_name = config["MongoSettings"]["DatabaseName"];
        db = client[db_name]
        db.create_collection(NEWS_COL_NAME)
        coll = db[NEWS_COL_NAME]
        for tname in stocknames:
            newsList: list[dict] = getNews(tname)
            if not newsList:
                continue
            coll.insert_many(newsList)

main()




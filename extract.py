import csv
from scholarly import scholarly

def search_scholarly(query, max_results=50):
    pubs = scholarly.search_pubs(query)
    articles = []
    for i, pub in enumerate(pubs):
        if i >= max_results:
            break
        title = pub.get('bib', {}).get('title', '')
        abstract = pub.get('bib', {}).get('abstract', '')
        articles.append({'title': title, 'introduction': abstract})
    return articles

def main():
    query = '(("domain identification" OR "domain extraction" OR "bounded context discovery" OR "microservice extraction") AND ("source code" OR "legacy system" OR "monolith" OR "software artifacts" OR "service logs") AND ("LLM" OR "large language model" OR "generative AI" OR "prompt engineering"))'
    articles = search_scholarly(query, 100)
    print(f"Retrieved {len(articles)} articles")
    
    if len(articles) > 0:
        with open('articles.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'introduction']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for article in articles:
                writer.writerow(article)
        
        print("Articles saved to articles.csv")
    else:
        print("No articles found, CSV not created.")

if __name__ == "__main__":
    main()

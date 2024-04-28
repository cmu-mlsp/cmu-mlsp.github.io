import scholarly
import pickle
import yaml


if __name__ == "__main__":
    with open('/Users/kashu/Downloads/main.pkl', 'rb') as f:
        data = pickle.load(f)
        
    # format web clawed data into a list of dictionaries
    publications = []
    for pub in data:
        title = pub["bib"]["title"]
        authors = pub["bib"]["author"]
        try:
            year = pub["bib"]["pub_year"]
        except:
            year = None      
        pub_type = 0
        if "journal" in pub["bib"].keys():
            venue = pub["bib"]["journal"]
            pub_type = 1
        elif "conference" in pub["bib"].keys():
            venue = pub["bib"]["conference"]
            pub_type = 2
        try:
            url = pub["pub_url"]
        except:
            url = None        
        publications.append({
            "title": title,
            "authors": authors,
            "url": url,
            "type": pub_type,
            "venue": venue,
            "year": year,
        })
    
    # save the publication data into a yaml file
    with open("_data/publist.yaml", "w") as f:
        yaml.dump(publications, f)
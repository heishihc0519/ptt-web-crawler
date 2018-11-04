import argparse
import pandas
import json

class Json2CSV(object):
    def __init__(self, filename):
        csvName = filename[:-4] + 'csv'
        with open(filename, 'r') as data_file:    
            data = json.load(data_file)
            output = list()
            for i in data.get('articles'):
                info = {
                    'article_id': i.get('article_id'),
                    'article_title': i.get('article_title'),
                    'author': i.get('author'),
                    'board': i.get('board'),
                    'date': i.get('date'),
                }
                output.append(info)
        
        df = pandas.DataFrame(output)
        df.to_csv(csvName)
                

    


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-f', dest='FILE', default=None, required=True, help='Access token')
    args = argparser.parse_args()
    Json2CSV(args.FILE)
    
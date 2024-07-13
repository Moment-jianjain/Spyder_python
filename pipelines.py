# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from turtle import pd

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


def create_engine(param):
    pass


class NewsmallexpressionPipeline:
    def __int__(self):

     self.engine = create_engine('mysql+pymysql://root:jianjian@127.0.0.1:3306/tipdm')

    def process_item(self, item, spider):
        data = pd.DataFrame(dict(item))
        data.to_sql('tipdm_data', self.engine, if_exists='append', index=False)
        data.to_csv('TipDM_data.csv', mode='a+', index=False, sep='|', header=False)

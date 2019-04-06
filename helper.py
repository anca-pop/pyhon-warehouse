import repository_product as prod
import pygal
import lxml

class Helper:

    def get_all_products(self, connectionObject):
        productInstance = prod.Product(connectionObject)
        products = productInstance.get_all_products()
        result = {}
        for product in products:
            result[product['denp']] = product['idp']
        return result

    def process_data_for_graphic(self, graphic_param, product_name):
        date_range = []
        graphic_data = []
        for list_item in graphic_param:
            date_range.append(list_item['data'])
            graphic_data.append((list_item['data'], list_item['cant']))

        dateline = pygal.DateLine(x_label_rotation=25)
        dateline.x_labels = date_range
        print(graphic_data,date_range)
        dateline.add(product_name, graphic_data)
        dateline.render_in_browser()

class Category:
    """ Класс категорий продуктов"""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product):
        """Метод, принимающий на вход продукт product, добавляющий его в категорию и увеличивающий счетчик продуктов
        product_count на единицу"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер, возвращающий строку со всеми продуктами"""
        product_str = ''
        for product in self.__products:
            product_str += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return product_str

    def __str__(self):
        """Магический метод; возвращает строку с информацией о количестве продуктов категории"""
        product_in_category_quantity = 0
        for product in self.__products:
            product_in_category_quantity += product.quantity
        return f'{self.name}, количество продуктов: {product_in_category_quantity} шт.'

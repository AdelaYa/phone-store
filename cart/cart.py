from decimal import Decimal
from django.conf import settings
from store.models import Phone


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, phone, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        phone_id = str(phone.id)
        if phone_id not in self.cart:
            self.cart[phone_id] = {'quantity': 0,
                                   'price': str(phone.price)}
        if update_quantity:
            self.cart[phone_id]['quantity'] = quantity
        else:
            self.cart[phone_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, phone):
        """
        Удаление товара из корзины.
        """
        phone_id = str(phone.id)
        if phone_id in self.cart:
            del self.cart[phone_id]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        phone_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        phones = Phone.objects.filter(id__in=phone_ids)
        for phone in phones:
            self.cart[str(phone.id)]['phone'] = phone

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
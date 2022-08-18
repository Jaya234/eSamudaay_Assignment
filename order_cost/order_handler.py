from numbers import Number


class OrderHandler():
    def get_delivery_cost(self, distance):
        print(distance)
        if distance >0 and distance <=10:
            return 5000
        elif distance >10 and distance <=20:
            return 10000
        elif distance >20 and distance <50:
            return 50000
        else:
            return 100000

    def get_items_value(self, order_items):
        cost = 0
        for order_item in order_items:
            cost += order_item['quantity'] * order_item['price']
        
        return cost
    
    def get_discount_value(self, offer: object, delivery_cost: Number):
        if offer['offer_type'] == 'FLAT':
            return offer['offer_val']
        elif offer['offer_type'] == 'DELIVERY':
            return delivery_cost
        return 0

    def calculate_order_value(self, order_items, distance, offer):
        items_value = self.get_items_value(order_items)
        delivery_cost = self.get_delivery_cost(distance/1000)
        discount_value = self.get_discount_value(offer, delivery_cost) if offer else 0
        print(f"items value : {items_value}\n")
        print(f"delivery_cost : {delivery_cost}\n")
        print(f"discount_value : {discount_value}\n")
        if discount_value:
            return items_value + delivery_cost - discount_value
        else:
            return items_value + delivery_cost

    def get_order_value(self, data):
        offer = data['offer'] if 'offer' in data else None
        order_items = data['order_items']
        distance = data['distance']

        order_value = self.calculate_order_value(order_items, distance, offer)

        return {
            'order_total' : order_value
        }
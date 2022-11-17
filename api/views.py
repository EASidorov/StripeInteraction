import stripe
import environ
from django.http import HttpResponseRedirect, JsonResponse
from django.views import generic
from .models import *
from requests import request


env = environ.Env()
environ.Env.read_env()
stripe.api_key = env('STRIPE_KEY')


class AllItemsView(generic.ListView):
    template_name = 'api/index.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.all()


class DetailsView(generic.DetailView):
    model = Item
    template_name = 'api/details.html'
    context_object_name = 'item'


def buy(request, pk):
    item = Item.objects.get(pk=pk)
    print(item)
    session = stripe.checkout.Session.create(success_url="https://www.reddit.com/r/funny/",
                                       cancel_url="https://www.reddit.com/r/sadmemes/",
                                       line_items=[{
                                                    'price_data': {
                                                        'currency': item.currency,
                                                        'product_data': {
                                                            'name': item.name,
                                                            'description': item.description,
                                                        },
                                                    'unit_amount': item.price * 100
                                                    },
                                                    'quantity': 1,
                                                }],
                                       mode="payment",
                                       )
    print('test')
    return JsonResponse({'session_id': session.id})

def buy_order(request, pk):
    order = Order.objects.get(pk=pk)
    items = order.items
    try:
        session = stripe.checkout.Session.create(success_url="https://www.reddit.com/r/funny/",
                                       cancel_url="https://www.reddit.com/r/sadmemes/",
                                       line_items=[{
                                                    'price_data': {
                                                        'currency': item.currency,
                                                        'product_data': {
                                                            'name': item.name,
                                                            'description': item.description,
                                                        },
                                                        'unit_amount': item.price*100
                                                    },
                                                    'quantity': 1,
                                                } for item in items],
                                       mode="payment",
                                       )
    except:
        return HttpResponseRedirect('')

    return JsonResponse({'session_id': session.id})

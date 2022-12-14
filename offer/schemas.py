from ninja import ModelSchema

from offer.models import PurchaseDone, SaleDone, PurchaseOffer, SaleOffer


class SaleOfferOut(ModelSchema):
    class Config:
        model = SaleOffer
        model_fields = ['id', 'trader', 'price', 'timestamp', 'state', 'product_kit']


class SaleOfferPlace(ModelSchema):
    product_kit_id: int

    class Config:
        model = SaleOffer
        model_fields = ['price']


class PurchaseOfferOut(ModelSchema):
    class Config:
        model = PurchaseOffer
        model_fields = ['id', 'trader', 'price', 'timestamp', 'state', 'product', 'count']


class PurchaseOfferPlace(ModelSchema):
    product_id: int

    class Config:
        model = PurchaseOffer
        model_fields = ['price', 'count']


class SaleDoneOut(ModelSchema):  # todo add addition fields
    class Config:
        model = SaleDone
        model_fields = ['offer', 'transaction']


class PurchaseDoneOut(ModelSchema):  # todo add addition fields
    class Config:
        model = PurchaseDone
        model_fields = ['offer', 'transaction']

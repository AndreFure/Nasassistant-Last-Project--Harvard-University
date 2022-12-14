from django.forms import ModelForm, Textarea, HiddenInput
from .models import Listing, User, Bid, Comment


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['maker', 'title', 'description',
                  'start_bid', 'url_img', 'category']
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
            'maker': HiddenInput(),
        }


class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['listing', 'price', 'bid_user']
        widgets = {'listing': HiddenInput(),
                   'bid_user': HiddenInput(),
                   }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['listing', 'information', 'author']
        widgets = {
            'information': Textarea(attrs={'cols': 20, 'rows': 10}),
            'listing': HiddenInput(),
            'author': HiddenInput(),
        }

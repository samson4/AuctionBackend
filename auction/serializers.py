from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from .models import Auction,Lot
from Users.serializers import UserSerializer


class AuctionSerializer(ModelSerializer):
    lot_count = SerializerMethodField()
    subscribers = UserSerializer(many=True)
    auction_subscriber = SerializerMethodField()
    lots = serializers.HyperlinkedIdentityField(view_name='lots-list',lookup_field='id')
    class Meta:
        model = Auction
        fields = ('id','lot_count','lots','title','status','subscribers','auction_subscriber') 

    def get_lot_count(self,obj):
        # print('obj',obj.count())
        return obj.lot_set.count()  
    # def get_auction_subscriber(self,obj):
    #     request = self.context.get('request')
    #     a = self.context.get('a')
    #     print(a)
        # if a:
        #     return True
        # else:
        #     return False
        # auction_subscriber = self.context.get('auction_subscriber')
        # print('request_user',dir(request))
        # print('subscribers',auction_subscriber)      
        # if request.user.id in self.subscribers.id:
        #     return True
        # else:
        #     return False
    def get_auction_subscriber(self,obj):
        request = self.context.get('request')
        
        queryset = Auction.objects.filter(subscribers__id = request.user.id) 
        print(queryset)
        if queryset:
            return True
        else:
            return False    
    #     request = self.context.get('request')
    #     print('request_user',(request))
    #     print('value',value)
    #     if request.user in self.subscribers:
    #         self.auction_subscriber=True
class AuctionDetailSerializer(ModelSerializer):
        lot_count = SerializerMethodField()    
        lots = serializers.HyperlinkedIdentityField(view_name='lots-list',lookup_field='id') 
        auction_subscriber = SerializerMethodField()
        class Meta:
            model = Auction
            fields = ('id','lot_count','lots','title','status','auction_subscriber')

        def get_auction_subscriber(self,obj):
            request = self.context.get('request')
        
            queryset = Auction.objects.filter(subscribers__id = request.user.id) 
            print(queryset)
            if queryset:
                return True
            else:
                return False 
        
        def get_lot_count(self,obj):
            # print('obj',obj.count())
            return obj.lot_set.count()        
    
class SubscribedAuctionsSerializer(ModelSerializer):
    lot_count = SerializerMethodField()
    # subscribers = UserSerializer(many=True)
    # auction_subscriber = SerializerMethodField()
    lots = serializers.HyperlinkedIdentityField(view_name='lots-list',lookup_field='id')
    class Meta:
        model = Auction
        fields = ('id','lot_count','lots','title','status',) 

    def get_lot_count(self,obj):
        # print('obj',obj.count())
        return obj.lot_set.count()      


    
class LotSerializer(ModelSerializer):
    
  
    class Meta:
        model = Lot
        fields = ('id','title','description','condition','Price',)

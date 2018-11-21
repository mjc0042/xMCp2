from rest_framework import serializers
from .models import Member, RegisteredUser, Address, CreditCard

#
#   Serializer Class for Member Table
#
class MemberSerializer(serializers.ModelSerializer):
		class Meta:
				model = Member
				fields = '__all__'

#
#   Serializer Class for Registered User Table
#
class RegisteredUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = RegisteredUser
		fields = '__all__'
		
#
#   Serializer Class for Address Table
#
class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = '__all__'
		
#
#   Serializer Class for Credit Card Table
#
class CreditCardSerializer(serializers.ModelSerializer):
	class Meta:
		model = CreditCard
		fields = '__all__'
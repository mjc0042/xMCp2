import logging
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Member, RegisteredUser
from .serializers import RegisteredUserSerializer
from utilities.hashers.PasswordHasher import PasswordHasher

# Logger
logger = logging.getLogger(__name__)

class MemberView(GenericAPIView):
    #authentication_class = (JSONWebTokenAuthentication,)

    @api_view(['GET', 'PUT', 'DELETE'])
    @permission_classes((AllowAny,))
    def get_member(self, request, *args, **kargs):
        """
        Retrieve, update or delete a member instance.
        """
        try:
            member_id = Member.objects.get(member_id=member_id)
        except Member.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = MemberSerializer(product,context={'request': request})
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = MemberSerializer(member_id, data=request.data,context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    @api_view(['POST'])
    @permission_classes((AllowAny,))
    def create_member(self, request, *args, **kargs):
        """
        Create new member instance.
        """
        memberId = request.data.get("member_id")
        
        try:
            member = Member.objects.get(member_id=memberId)
            if (member != None):
                return Response(status="Member already exists.")
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except MemberDoesNotExist:
            serializer = MemberSerializer(product,context={'request': request})
            self.writeMember(request.data)
            self.writeRegisteredUser(request.data)
            self.writeAddress(request.data)
            self.writeCreditCard(request.data)
            return Response(serializer.data, status.HTTP_201_CREATED)
        
    @api_view(['GET'])
    @permission_classes((AllowAny,))
    def login(request, username, password):
        """
        Fetch member instance on login.
        """
        logger.info("Received login request:" + username)
        logger.info(request)
        try:
            user = RegisteredUser.objects.get(username=username)
        except RegisteredUser.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

        if request.method == 'GET':
            serializer = RegisteredUserSerializer(user,context={'request': request})
            logger.info(password)
            logger.info(serializer.data.get("password"))
            if (PasswordHasher.verifyPassword(password, serializer.data.get("password"))):
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(status=status.HTTP_204_NO_CONTENT)

                
    #
    #   Parse Member Data from request
    #
    def parseMemberData(reqData):
        data = {}
        data['member_id'] = reqData.get('member_id')
        data['phone_number'] = reqData.get('phone_number')
        return data
        
    #
    #   Parse Registered User Data from request
    #
    def parseRegisteredUserData(reqData):
        data = {}
        data['id'] = reqData.get('member_id')
        data['username'] = reqData.get('username')
        data['password'] = PasswordHasher.hashPassword(reqData.get('password'))
        data['age'] = reqData.get('age')
        data['gender'] = reqData.get('gender')
        data['income'] = reqData.get('income')
        return data
    
    #
    #   Parse Address Data from request
    #
    def parseAddressData(reqData):
        data = {}
        data['id'] = reqData.get('member_id')
        data['street'] = reqData.get('street')
        data['zipcode'] = reqData.get('zipcode')
        data['city'] = reqData.get('city')
        data['state'] = reqData.get('state')
        return data

    #
    #   Parse Credit Card Data from request
    #
    def parseCreditCardData(reqData):
        data = {}
        data['username'] = reqData.get('username')
        data['name'] = reqData.get('name')
        data['number'] = reqData.get('number')
        data['cardtype'] = reqData.get('cardtype')
        data['expiration'] = reqData.get('expiration')
        return data

    #
    #   Write Member Data
    #
    def writeMember(self, data):
        write(MemberSerializer(member=data))
    
    #
    #   Write Registered User Data
    #
    def writeRegisteredUser(self, data):
        write(RegisteredUserSerializer(registereduser=data))

    #
    #   Write Address Data
    #
    def writeAddress(self, data):
        write(AddressSerializer(address=data))

    #
    #   Write Credit Card Data
    #
    def writeCreditCard(self, data):
        write(CreditCardSerializer(creditcard=data))
    
    #
    #   Run serializer to write to database
    #
    def write(serializer):
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
from django.db import models


# Member Schema
#
# CREATE TABLE Member
# (
#   memberid CHAR(20) NOT NULL,
#   phone CHAR(10),
#   PRIMARY KEY(memberid)
# )
class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=10)

# User schema
#
# CREATE TABLE RegisteredUser
# (
#   memberid CHAR(20),
#   username CHAR(20) NOT NULL,
#   name CHAR(50),
#   password CHAR(16),
#   email CHAR(50),
#   age INTEGER,
#   gender CHAR(6),
#   income REAL,
#   PRIMARY KEY(memberid),
#   FOREIGN KEY(memberid) REFERENCES Member ON DELETE CASCADE,
#   UNIQUE(username)
# )
class RegisteredUser(models.Model):
		username = models.CharField(max_length=20, blank=False, unique=True)
		name = models.CharField(max_length=50)
		password = models.CharField(max_length=16)
		email = models.CharField(max_length=50)
		age = models.IntegerField() 
		gender = models.CharField(max_length=6)
		income = models.FloatField()
		member_id = models.ForeignKey(Member, on_delete=models.CASCADE)    


# Address Schema
#
# CREATE TABLE Address
# (
#   memberid CHAR(20),
#   street CHAR(50),
#   city CHAR(20),
#   state CHAR(2),
#   zipcode INTEGER,
#   PRIMARY KEY(memberid, street, zipcode),
#   FOREIGN KEY(memberid) REFERENCES Member
# )
class Address(models.Model):
		street = models.CharField(max_length=50)
		city = models.CharField(max_length=20) 
		state = models.CharField(max_length=2)
		zipcode = models.CharField(max_length=10)
		member_id= models.ForeignKey(Member, on_delete=models.CASCADE) 
		class Meta:
				unique_together = (("member_id","street","zipcode"),)

# Credit Card Schema
#
# CREATE TABLE CreditCard
# (
#   username CHAR(20),
#   cardtype CHAR(10),
#   name CHAR(20),
#   number CHAR(16) NOT NULL,
#   expiration CHARD(5),
#   PRIMARY KEY(username, number),
#   FOREIGN KEY(username) REFERENCES RegisteredUser ON DELETE CASCADE
# )
class CreditCard(models.Model):
		cardtype = models.CharField(max_length=20)
		name = models.CharField(max_length=20)
		number = models.CharField(max_length=16, blank=False)
		expiration = models.CharField(max_length=5)
		username = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
		class Meta:
				unique_together = (("username", "number"),)

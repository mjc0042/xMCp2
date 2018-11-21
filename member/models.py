from django.db import models

#
# CREATE TABLE Member
# (
#   member_id CHAR(20) NOT NULL,
#   phone CHAR(10),
#   PRIMARY KEY(member_idid)
# )
class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=10)

# User schema
#
# CREATE TABLE RegisteredUser
# (
#   member_id CHAR(20),
#   username CHAR(20) NOT NULL,
#   name CHAR(50),
#   password CHAR(72),
#   email CHAR(50),
#   age INTEGER,
#   gender CHAR(6),
#   income REAL,
#   PRIMARY KEY(member_id),
#   FOREIGN KEY(member_id) REFERENCES Member ON DELETE CASCADE,
#   UNIQUE(username)
# )
class RegisteredUser(models.Model):
    username = models.CharField(max_length=20, blank=False, unique=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=72)
    email = models.CharField(max_length=50)
    age = models.IntegerField() 
    gender = models.CharField(max_length=6)
    income = models.FloatField()
    member = models.ForeignKey(Member, on_delete=models.CASCADE)    


# Address Schema
#
# CREATE TABLE Address
# (
#   member_id CHAR(20),
#   street CHAR(50),
#   city CHAR(20),
#   state CHAR(2),
#   zipcode INTEGER,
#   PRIMARY KEY(member_id, street, zipcode),
#   FOREIGN KEY(member_id) REFERENCES Member
# )
class Address(models.Model):
		street = models.CharField(max_length=50)
		city = models.CharField(max_length=20) 
		state = models.CharField(max_length=2)
		zipcode = models.CharField(max_length=10)
		member = models.ForeignKey(Member, on_delete=models.CASCADE) 
		class Meta:
				unique_together = (("member","street","zipcode"),)

# Credit Card Schema
#
# CREATE TABLE CreditCard
# (
#   username CHAR(20),
#   cardtype CHAR(10),
#   name CHAR(20),
#   number CHAR(16) NOT NULL,
#   expiration CHARD(5),
#   PRIMARY KEY(member_id, number),
#   FOREIGN KEY(member_id) REFERENCES Member ON DELETE CASCADE
# )
class CreditCard(models.Model):
		cardtype = models.CharField(max_length=20)
		name = models.CharField(max_length=20)
		number = models.CharField(max_length=16, blank=False)
		expiration = models.CharField(max_length=5)
		member = models.ForeignKey(Member, on_delete=models.CASCADE)
		class Meta:
				unique_together = (("member", "number"),)

#Q1
'''An access token is an object that describes the security context of a process or thread.
The information in a token includes the identity and privileges of the user account associated with the process or thread.
When a user logs on, the system verifies the user's password by comparing it with information stored in a security database.
If the password is authenticated, the system produces an access token. Every process executed
on behalf of this user has a copy of this access token.

Consumer Key (API Key)	F3evGdFG3mC7O5xOa6EzASMSZ
Consumer Secret (API Secret)	Dyuv6aSbLKtLSFC2JGpZKDPuIa07VIrMBhgje94KD0hWAuVw1AS'''

#Q2
'''Default Server:  UnKnown
Address:  192.168.43.1

> www.google.com
Server:  UnKnown
Address:  192.168.43.1

Non-authoritative answer:
Name:    www.google.com
Addresses:  2404:6800:4007:810::2004
          74.125.68.106
          74.125.68.104
          74.125.68.105
          74.125.68.103
          74.125.68.99
          74.125.68.147

> www.facebook.com
Server:  UnKnown
Address:  192.168.43.1

Non-authoritative answer:
Name:    star-z-mini.c10r.facebook.com
Addresses:  2a03:2880:f137:87:face:b00c:0:50fb
          157.240.23.39
Aliases:  www.facebook.com'''

#Q3
'''import tweepy
import textblob
from textblob import TextBlob
consumer_key='F3evGdFG3mC7O5xOa6EzASMSZ'
consumer_secret='Dyuv6aSbLKtLSFC2JGpZKDPuIa07VIrMBhgje94KD0hWAuVw1AS'
access_token='203946177374955739-62kpUoahhS761dkfheytbcCMPxc99'
access_token_secret='WECGzg3JnO36AXhEyNjDpEIELExBwz1qmvPiIYntM1044'
oauth=tweepy.OAuthHandler(consumer_key, consumer_secret)
oauth.set_access_token(access_token, access_token_secret)
api=tweepy.API(oauth)
public_tweets= api.search("#FIFA")
print(public_tweets)'''

#Q4
'''difference between library and API :
A library is a collection of functions / objects that serves one particular purpose. 
you could use a library in a variety of projects. (Various specialized services in our case).
An API is an interface for other programs to interact with your program or library  without having direct access.
( giving specifications for our need to various vendors in our case).
Example:
lib :JQuery library, is a library of prewritten, cross-browser Javascript animations and
 functions which you will need while making a website. 
Api:Google Map APIs you can show maps for different places without writing/hosting the
 whole code on your server, and just use it, usually this
 data transfer is in form of JSON i.e JavaScript Object Notation.'''

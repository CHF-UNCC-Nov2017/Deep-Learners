
# coding: utf-8

# In[65]:

import requests
import json


# In[68]:

def get_yodlee_account_info(loginName="sbMemd3b2a45891f45d525106513de8eb5851ba1",password="sbMemd3b2a45891f45d525106513de8eb5851ba1#123",locale="en_US"):
    yodlee_url = 'https://developer.api.yodlee.com/ysl/restserver/v1/cobrand/login'
    #loginName = "sbMemd3b2a45891f45d525106513de8eb5851ba1"
    #password = "sbMemd3b2a45891f45d525106513de8eb5851ba1#123"
    #locale = "en_US"


    yodlee_login ='{"cobrand":{"cobrandLogin":"sbCobd3b2a45891f45d525106513de8eb5851ba","cobrandPassword":"d4ca4677-a1d3-437d-82c3-210dc9915292"}}'

    response = requests.post(yodlee_url, data=yodlee_login)

    resp_dict = json.loads(response.content)

    cobSesssion = resp_dict['session']['cobSession']

    user_link = 'https://developer.api.yodlee.com/ysl/restserver/v1/user/login'

    head ={'Authorization': '{cobSession=' +cobSesssion }

    
    body = '{"user":{"loginName":"' + loginName + '","password":"' + password + '","locale":"' +locale + '"}}'

    response = requests.post(user_link, headers=head, data=body)

    resp_dict = json.loads(response.content)

    

    userSession = dict(resp_dict)['user'][ 'session']['userSession']

    head ={'Authorization': '{cobSession=' +cobSesssion  +', userSession=' +userSession  }

    ylink ='https://developer.api.yodlee.com:443/ysl/restserver/v1/accounts'

    response = requests.get(ylink,headers = head  )

    resp_dict = json.loads(response.content)

    
    return resp_dict
    


# In[ ]:




# In[69]:

user1_info  = str(get_yodlee_account_info(loginName="sbMemd3b2a45891f45d525106513de8eb5851ba1",password="sbMemd3b2a45891f45d525106513de8eb5851ba1#123"))


# In[70]:

user2_info  = str(get_yodlee_account_info(loginName="sbMemd3b2a45891f45d525106513de8eb5851ba2",password="sbMemd3b2a45891f45d525106513de8eb5851ba2#123"))


# In[71]:

user3_info =str(get_yodlee_account_info(loginName="sbMemd3b2a45891f45d525106513de8eb5851ba3",password="sbMemd3b2a45891f45d525106513de8eb5851ba3#123"))


# In[72]:

user4_info=str(get_yodlee_account_info(loginName="sbMemd3b2a45891f45d525106513de8eb5851ba4",password="sbMemd3b2a45891f45d525106513de8eb5851ba4#123"))


# In[73]:

user5_info=str(get_yodlee_account_info(loginName="sbMemd3b2a45891f45d525106513de8eb5851ba5",password="sbMemd3b2a45891f45d525106513de8eb5851ba5#123"))


# In[74]:

out_file = user1_info + user2_info +user3_info +user4_info +user5_info


# In[75]:

with open('json_out.txt', 'a') as f:
    f.write(out_file)


# {'account': [{'refreshinfo': {'statusCode': 0, 'lastRefreshAttempt': '2017-11-05T01:11:37Z', 'lastRefreshed': '2017-11-05T01:11:37Z', 'nextRefreshScheduled': '2017-11-06T08:53:26Z', 'statusMessage': 'OK'}, 'CONTAINER': 'bank', 'isManual': False, 'isAsset': True, 'lastUpdated': '2017-11-05T01:11:37Z', 'currentBalance': {'amount': 9044.78, 'currency': 'USD'}, 'availableBalance': {'amount': 65454.78, 'currency': 'USD'}, 'id': 10975464, 'balance': {'amount': 9044.78, 'currency': 'USD'}, 'accountName': 'TESTDATA1', 'accountNumber': '503-5623xxx', 'aggregationSource': 'USER', 'providerName': 'Dag Site', 'accountStatus': 'ACTIVE', 'accountType': 'SAVINGS', 'providerId': '16441', 'includeInNetWorth': True, 'holderProfile': [{'name': {'displayed': 'accountHolder'}}], 'createdDate': '2017-11-05T01:11:41Z', 'providerAccountId': 10468516}, {'refreshinfo': {'statusCode': 0, 'lastRefreshAttempt': '2017-11-05T01:11:37Z', 'lastRefreshed': '2017-11-05T01:11:37Z', 'nextRefreshScheduled': '2017-11-06T08:53:26Z', 'statusMessage': 'OK'}, 'CONTAINER': 'bank', 'isManual': False, 'isAsset': True, 'lastUpdated': '2017-11-05T01:11:37Z', 'currentBalance': {'amount': 44.78, 'currency': 'USD'}, 'availableBalance': {'amount': 54.78, 'currency': 'USD'}, 'id': 10975460, 'balance': {'amount': 44.78, 'currency': 'USD'}, 'accountName': 'TESTDATA', 'accountNumber': '503-1123xxx', 'aggregationSource': 'USER', 'providerName': 'Dag Site', 'accountStatus': 'ACTIVE', 'accountType': 'CHECKING', 'providerId': '16441', 'includeInNetWorth': True, 'holderProfile': [{'name': {'displayed': 'accountHolder'}}], 'createdDate': '2017-11-05T01:11:37Z', 'providerAccountId': 10468516}, {'refreshinfo': {'statusCode': 0, 'lastRefreshAttempt': '2017-11-05T01:11:37Z', 'lastRefreshed': '2017-11-05T01:11:37Z', 'nextRefreshScheduled': '2017-11-06T00:36:26Z', 'statusMessage': 'OK'}, 'CONTAINER': 'creditCard', 'isManual': False, 'isAsset': False, 'lastUpdated': '2017-11-05T01:11:37Z', 'id': 10975385, 'balance': {'amount': 1636.44, 'currency': 'USD'}, 'accountName': 'CREDIT CARD', 'accountNumber': '************8614', 'aggregationSource': 'USER', 'providerName': 'Dag Site', 'accountStatus': 'ACTIVE', 'accountType': 'OTHER', 'providerId': '16441', 'includeInNetWorth': True, 'createdDate': '2017-11-05T01:11:37Z', 'providerAccountId': 10468516, 'availableCredit': {'amount': 1363, 'currency': 'USD'}}, {'refreshinfo': {'statusCode': 0, 'lastRefreshAttempt': '2017-11-05T01:11:37Z', 'lastRefreshed': '2017-11-05T01:11:37Z', 'nextRefreshScheduled': '2017-11-06T08:53:26Z', 'statusMessage': 'OK'}, 'CONTAINER': 'bank', 'isManual': False, 'isAsset': True, 'lastUpdated': '2017-11-05T01:11:37Z', 'currentBalance': {'amount': 9044.78, 'currency': 'USD'}, 'availableBalance': {'amount': 65454.78, 'currency': 'USD'}, 'id': 10975384, 'balance': {'amount': 9044.78, 'currency': 'USD'}, 'accountName': 'TESTDATA1', 'accountNumber': '503-5623xxx', 'aggregationSource': 'USER', 'providerName': 'Dag Site', 'accountStatus': 'ACTIVE', 'accountType': 'SAVINGS', 'providerId': '16441', 'includeInNetWorth': True, 'holderProfile': [{'name': {'displayed': 'accountHolder'}}], 'createdDate': '2017-11-05T01:11:37Z', 'providerAccountId': 10468516}]}

# In[ ]:




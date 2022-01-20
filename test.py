#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import datetime
dt = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="microseconds")
print(str(dt))

import json

data = {'created': '2022-01-13T13:51:23.000+08:00', 'createdby': '暂无', 'updated': None, 'updatedby': None, 'orgUuid': None, 'orgId': 1, 'orgComments': '注释', 'orgName': '组织1', 'orgAbbr': None, 'email': '邮箱', 'phoneNumber': '手机号', 'contactPerson': None, 'addressLine1': None, 'addressLine2': None, 'city': '城市', 'province': None, 'country': None, 'postCode': None}
with open("apiTestCases/data/organization/allOrg/1.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
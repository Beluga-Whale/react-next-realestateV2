from fastapi import FastAPI
from pydantic import BaseModel

homeamerica_db = [
    {   
        "id": "1",
        "homepic":"https://images.unsplash.com/photo-1549517045-bc93de075e53?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTR8fGhvbWV8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60",
        "address":"9815 Copper Creek Dr, Unit 31925, Austin",
        "bed": "4",
        "baht": "2",
        "living": "2",
        "garage": "1",
        "year": "2007",
        "price": "231,123",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1523217582562-09d0def993a6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8aG9tZXxlbnwwfDJ8MHx8&auto=format&fit=crop&w=500&q=60",
        "images2":"https://images.unsplash.com/photo-1616047006789-b7af5afb8c20?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aG9tZXxlbnwwfDJ8MHx8&auto=format&fit=crop&w=500&q=60",
        "images3":"https://images.unsplash.com/photo-1618220048045-10a6dbdf83e0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8aG9tZXxlbnwwfDJ8MHx8&auto=format&fit=crop&w=500&q=60",
        "images4":"https://images.unsplash.com/photo-1615529182904-14819c35db37?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",

    },
    # *End1

    {
        "id": "2",
        "homepic":"https://images.unsplash.com/photo-1513584684374-8bab748fbf90?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mjl8fGhvbWV8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60",
        "address":"16 Greenwich Close, Crawley",
        "bed": "3",
        "baht": "3",
        "living": "1",
        "garage": "1",
        "year": "2013",
        "price": "174,523",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1522050212171-61b01dd24579?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images2":"https://images.unsplash.com/photo-1593604454703-20ecca9bb373?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images3":"https://images.unsplash.com/photo-1567016557389-5246a1940bdc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images4":"https://images.unsplash.com/photo-1565038941323-e5ceac0fcde2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
    },
    # *End2

    {   
        "id": "3",
        "homepic":"https://images.unsplash.com/photo-1570129477492-45c003edd2be?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mzl8fGhvbWV8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60",
        "address":"5519 Roanwood, San Antonio",
        "bed": "4",
        "baht": "3",
        "living": "3",
        "garage": "2",
        "year": "2021",
        "price": "500,000",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1533757114113-3e1d3e9d766c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=579&q=80",
        "images2":"https://images.unsplash.com/photo-1567016507665-356928ac6679?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images3":'https://images.unsplash.com/photo-1567016432779-094069958ea5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80',
        "images4":"https://images.unsplash.com/photo-1565791380709-49e529c8b073?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=581&q=80",

    },
    # *End3

    {
        "id": "4",
        "homepic":"https://images.unsplash.com/photo-1480074568708-e7b720bb3f09?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1174&q=80",
        "address":"5519 Roanwood, San Antonio",
        "bed": "4",
        "baht": "3",
        "living": "3",
        "garage": "2",
        "year": "2015",
        "price": "562,000",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1503011510-c0e00592713b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images2":"https://images.unsplash.com/photo-1499916078039-922301b0eb9b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images3":"https://images.unsplash.com/photo-1587094313669-faf7668ed8a8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images4":"https://images.unsplash.com/photo-1522107177-01884fcfa2bb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
    },
    # *End4

    {   
        "id": "5",
        "homepic":"https://images.unsplash.com/photo-1512917774080-9991f1c4c750?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
        "address":"3 Greenwich Close, Crawley",
        "bed": "6",
        "baht": "2",
        "living": "4",
        "garage": "2",
        "year": "2012",
        "price": "750,000",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1521783593447-5702b9bfd267?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=904&q=80",
        "images2":"https://images.unsplash.com/photo-1471623600634-4d04cfc56a27?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images3":"https://images.unsplash.com/photo-1464564531096-f0163633a18a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=894&q=80",
        "images4":"https://images.unsplash.com/photo-1501660034796-9860da6cb741?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",

    },
    # *End5

    {
        "id": "6",
        "homepic":"https://images.unsplash.com/photo-1449844908441-8829872d2607?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
        "address":"101a Cowley Road, Oxford",
        "bed": "4",
        "baht": "3",
        "living": "3",
        "garage": "2",
        "year": "2007",
        "price": "627,000",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1558769132-92e717d613cd?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images2":"https://images.unsplash.com/photo-1466637574441-749b8f19452f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images3":"https://images.unsplash.com/photo-1532490389938-2856e3f1560a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images4":"https://images.unsplash.com/photo-1615529182904-14819c35db37?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
    },
    # *End6
]

# !End home USA ************************************************************************************

homespain_db = [
    {   
        "id": "1",
        "homepic":"https://images.unsplash.com/photo-1523688471150-efdd09f0f312?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTR8fGhvdXNlfGVufDB8MnwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "address":"9815 Copper Creek Dr, Unit 31925, Austin",
        "bed": "7",
        "baht": "5",
        "living": "2",
        "garage": "7",
        "year": "2013",
        "price": "888,888",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1523217582562-09d0def993a6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8aG9tZXxlbnwwfDJ8MHx8&auto=format&fit=crop&w=500&q=60",
        "images2":"https://images.unsplash.com/photo-1616047006789-b7af5afb8c20?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aG9tZXxlbnwwfDJ8MHx8&auto=format&fit=crop&w=500&q=60",
        "images3":"https://images.unsplash.com/photo-1618220048045-10a6dbdf83e0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8aG9tZXxlbnwwfDJ8MHx8&auto=format&fit=crop&w=500&q=60",
        "images4":"https://images.unsplash.com/photo-1615529182904-14819c35db37?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",

    },
    # *End1

    {
        "id": "2",
        "homepic":"https://images.unsplash.com/photo-1552765063-31cfdea3d1e6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTF8fGhvdXNlfGVufDB8MnwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "address":"16 Greenwich Close, Crawley",
        "bed": "2",
        "baht": "4",
        "living": "6",
        "garage": "3",
        "year": "2000",
        "price": "424,663",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1522050212171-61b01dd24579?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images2":"https://images.unsplash.com/photo-1593604454703-20ecca9bb373?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images3":"https://images.unsplash.com/photo-1567016557389-5246a1940bdc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images4":"https://images.unsplash.com/photo-1565038941323-e5ceac0fcde2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
    },
    # *End2

    {   
        "id": "3",
        "homepic":"https://images.unsplash.com/photo-1517541866997-ea18e32ea9e9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8N3x8aG91c2V8ZW58MHwyfDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
        "address":"5519 Roanwood, San Antonio",
        "bed": "3",
        "baht": "3",
        "living": "3",
        "garage": "2",
        "year": "2021",
        "price": "234,000",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1533757114113-3e1d3e9d766c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=579&q=80",
        "images2":"https://images.unsplash.com/photo-1567016507665-356928ac6679?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images3":'https://images.unsplash.com/photo-1567016432779-094069958ea5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80',
        "images4":"https://images.unsplash.com/photo-1565791380709-49e529c8b073?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=581&q=80",

    },
    # *End3

    {
        "id": "4",
        "homepic":"https://images.unsplash.com/photo-1518889778-5111daad1bda?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjN8fGhvdXNlfGVufDB8MnwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "address":"5519 Roanwood, San Antonio",
        "bed": "4",
        "baht": "3",
        "living": "5",
        "garage": "2",
        "year": "2022",
        "price": "982,000",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1503011510-c0e00592713b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images2":"https://images.unsplash.com/photo-1499916078039-922301b0eb9b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images3":"https://images.unsplash.com/photo-1587094313669-faf7668ed8a8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images4":"https://images.unsplash.com/photo-1522107177-01884fcfa2bb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
    },
    # *End4

    {   
        "id": "5",
        "homepic":"https://images.unsplash.com/photo-1485541653056-e688bdf8319e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjJ8fGhvdXNlfGVufDB8MnwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "address":"3 Greenwich Close, Crawley",
        "bed": "3",
        "baht": "2",
        "living": "4",
        "garage": "2",
        "year": "2032",
        "price": "876,000",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1521783593447-5702b9bfd267?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=904&q=80",
        "images2":"https://images.unsplash.com/photo-1471623600634-4d04cfc56a27?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images3":"https://images.unsplash.com/photo-1464564531096-f0163633a18a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=894&q=80",
        "images4":"https://images.unsplash.com/photo-1501660034796-9860da6cb741?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",

    },
    # *End5

    {
        "id": "6",
        "homepic":"https://images.unsplash.com/photo-1498409454240-d9139b0430e7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mjl8fGhvdXNlfGVufDB8MnwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "address":"101a Cowley Road, Oxford",
        "bed": "6",
        "baht": "8",
        "living": "1",
        "garage": "2",
        "year": "2027",
        "price": "9627,000",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1558769132-92e717d613cd?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images2":"https://images.unsplash.com/photo-1466637574441-749b8f19452f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images3":"https://images.unsplash.com/photo-1532490389938-2856e3f1560a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images4":"https://images.unsplash.com/photo-1615529182904-14819c35db37?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
    },
    # *End6
]

# !End Spain #####################################################################

homelondon_db = [
    {   
        "id": "1",
        "homepic":"https://images.unsplash.com/photo-1609542101758-cf2bf6d3e6eb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mzd8fGhvdXNlfGVufDB8MnwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "address":"9815 Copper Creek Dr, Unit 31925, Austin",
        "bed": "2",
        "baht": "3",
        "living": "2",
        "garage": "4",
        "year": "2009",
        "price": "424,112",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1523217582562-09d0def993a6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8aG9tZXxlbnwwfDJ8MHx8&auto=format&fit=crop&w=500&q=60",
        "images2":"https://images.unsplash.com/photo-1616047006789-b7af5afb8c20?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aG9tZXxlbnwwfDJ8MHx8&auto=format&fit=crop&w=500&q=60",
        "images3":"https://images.unsplash.com/photo-1618220048045-10a6dbdf83e0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8aG9tZXxlbnwwfDJ8MHx8&auto=format&fit=crop&w=500&q=60",
        "images4":"https://images.unsplash.com/photo-1615529182904-14819c35db37?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",

    },
    # *End1

    {
        "id": "2",
        "homepic":"https://images.unsplash.com/photo-1637141765711-078dfc1dfac3?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mzh8fGhvdXNlfGVufDB8MnwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "address":"754 Greenwich Close, Crawley",
        "bed": "3",
        "baht": "3",
        "living": "4",
        "garage": "1",
        "year": "2023",
        "price": "524,663",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1522050212171-61b01dd24579?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images2":"https://images.unsplash.com/photo-1593604454703-20ecca9bb373?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images3":"https://images.unsplash.com/photo-1567016557389-5246a1940bdc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images4":"https://images.unsplash.com/photo-1565038941323-e5ceac0fcde2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
    },
    # *End2

    {   
        "id": "3",
        "homepic":"https://images.unsplash.com/photo-1588391778043-f414478c81ca?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDN8fGhvdXNlfGVufDB8MnwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "address":"59 Roanwood, San Antonio",
        "bed": "5",
        "baht": "1",
        "living": "1",
        "garage": "5",
        "year": "2011",
        "price": "246,000",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1533757114113-3e1d3e9d766c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=579&q=80",
        "images2":"https://images.unsplash.com/photo-1567016507665-356928ac6679?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images3":'https://images.unsplash.com/photo-1567016432779-094069958ea5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80',
        "images4":"https://images.unsplash.com/photo-1565791380709-49e529c8b073?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=581&q=80",

    },
    # *End3

    {
        "id": "4",
        "homepic":"https://images.unsplash.com/photo-1633602108759-40f528b59111?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDV8fGhvdXNlfGVufDB8MnwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "address":"5779 Roanwood, San Antonio",
        "bed": "2",
        "baht": "3",
        "living": "4",
        "garage": "2",
        "year": "2033",
        "price": "321,100",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1503011510-c0e00592713b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images2":"https://images.unsplash.com/photo-1499916078039-922301b0eb9b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images3":"https://images.unsplash.com/photo-1587094313669-faf7668ed8a8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images4":"https://images.unsplash.com/photo-1522107177-01884fcfa2bb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
    },
    # *End4

    {   
        "id": "5",
        "homepic":"https://images.unsplash.com/photo-1503915525326-1ac13d4c5e76?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NTZ8fGhvdXNlfGVufDB8MnwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "address":"36 Greenwich Close, Crawley",
        "bed": "3",
        "baht": "2",
        "living": "4",
        "garage": "2",
        "year": "2032",
        "price": "636,000",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1521783593447-5702b9bfd267?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=904&q=80",
        "images2":"https://images.unsplash.com/photo-1471623600634-4d04cfc56a27?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images3":"https://images.unsplash.com/photo-1464564531096-f0163633a18a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=894&q=80",
        "images4":"https://images.unsplash.com/photo-1501660034796-9860da6cb741?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",

    },
    # *End5

    {
        "id": "6",
        "homepic":"https://images.unsplash.com/photo-1566064282945-7d97dc617a9a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NjV8fGhvdXNlfGVufDB8MnwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "address":"123a Cowley Road, Oxford",
        "bed": "5",
        "baht": "3",
        "living": "2",
        "garage": "2",
        "year": "2012",
        "price": "369,000",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1558769132-92e717d613cd?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images2":"https://images.unsplash.com/photo-1466637574441-749b8f19452f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images3":"https://images.unsplash.com/photo-1532490389938-2856e3f1560a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images4":"https://images.unsplash.com/photo-1615529182904-14819c35db37?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
    },
    # *End6
]

# !End London

homefrance_db = [
    {   
        "id": "1",
        "homepic":"https://images.unsplash.com/photo-1623681179596-9ad81ffa2fb7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NjF8fGhvdXNlfGVufDB8MnwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "address":"222 Copper Creek Dr, Unit 31925, Austin",
        "bed": "5",
        "baht": "3",
        "living": "2",
        "garage": "4",
        "year": "2009",
        "price": "424,112",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1523217582562-09d0def993a6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8aG9tZXxlbnwwfDJ8MHx8&auto=format&fit=crop&w=500&q=60",
        "images2":"https://images.unsplash.com/photo-1616047006789-b7af5afb8c20?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aG9tZXxlbnwwfDJ8MHx8&auto=format&fit=crop&w=500&q=60",
        "images3":"https://images.unsplash.com/photo-1618220048045-10a6dbdf83e0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8aG9tZXxlbnwwfDJ8MHx8&auto=format&fit=crop&w=500&q=60",
        "images4":"https://images.unsplash.com/photo-1615529182904-14819c35db37?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",

    },
    # *End1

    {
        "id": "2",
        "homepic":"https://images.unsplash.com/photo-1562545712-e195c0dde7d6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NjN8fGhvdXNlfGVufDB8MnwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "address":"754 Greenwich Close, Crawley",
        "bed": "3",
        "baht": "3",
        "living": "4",
        "garage": "1",
        "year": "2023",
        "price": "524,663",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1522050212171-61b01dd24579?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images2":"https://images.unsplash.com/photo-1593604454703-20ecca9bb373?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images3":"https://images.unsplash.com/photo-1567016557389-5246a1940bdc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images4":"https://images.unsplash.com/photo-1565038941323-e5ceac0fcde2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
    },
    # *End2

    {   
        "id": "3",
        "homepic":"https://images.unsplash.com/photo-1638212319045-08665a6e6513?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NzF8fGhvdXNlfGVufDB8MnwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "address":"59 Roanwood, San Antonio",
        "bed": "5 ",
        "baht": "1",
        "living": "1",
        "garage": "5",
        "year": "2011",
        "price": "246,000",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1533757114113-3e1d3e9d766c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=579&q=80",
        "images2":"https://images.unsplash.com/photo-1567016507665-356928ac6679?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images3":'https://images.unsplash.com/photo-1567016432779-094069958ea5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80',
        "images4":"https://images.unsplash.com/photo-1565791380709-49e529c8b073?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=581&q=80",

    },
    # *End3

    {
        "id": "4",
        "homepic":"https://images.unsplash.com/photo-1542297849-dbb1db23e8f8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nzd8fGhvdXNlfGVufDB8MnwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "address":"5779 Roanwood, San Antonio",
        "bed": "2",
        "baht": "3",
        "living": "4",
        "garage": "2",
        "year": "2033",
        "price": "321,100",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1503011510-c0e00592713b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images2":"https://images.unsplash.com/photo-1499916078039-922301b0eb9b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images3":"https://images.unsplash.com/photo-1587094313669-faf7668ed8a8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images4":"https://images.unsplash.com/photo-1522107177-01884fcfa2bb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
    },
    # *End4

    {   
        "id": "5",
        "homepic":"https://images.unsplash.com/photo-1644501811072-03cc44118cae?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8ODB8fGhvdXNlfGVufDB8MnwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "address":"36 Greenwich Close, Crawley",
        "bed": "3",
        "baht": "2",
        "living": "4",
        "garage": "2",
        "year": "2032",
        "price": "636,000",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1521783593447-5702b9bfd267?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=904&q=80",
        "images2":"https://images.unsplash.com/photo-1471623600634-4d04cfc56a27?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images3":"https://images.unsplash.com/photo-1464564531096-f0163633a18a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=894&q=80",
        "images4":"https://images.unsplash.com/photo-1501660034796-9860da6cb741?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",

    },
    # *End5

    {
        "id": "6",
        "homepic":"https://images.unsplash.com/photo-1567421077856-620c98423ccb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8ODZ8fGhvdXNlfGVufDB8MnwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "address":"123a Cowley Road, Oxford",
        "bed": "5",
        "baht": "3",
        "living": "2",
        "garage": "2",
        "year": "2012",
        "price": "369,000",
        "description": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "description2": "19360 Murray Hill St, Detroit, MI 48235 is a single family home built in 1948. This property was last sold for $40,000 in 2021 and currently has an estimated value of $104,200. According to the Detroit public records, the property at 19360 Murray Hill St, Detroit, MI 48235 has approximately 956 square feet,  with a lot size of 4,792 square feet. Nearby schools include Detroit International Academy For Young Women, Bow Elementary-Middle School and Douglass Academy For Young Men.",
        "images1":"https://images.unsplash.com/photo-1558769132-92e717d613cd?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images2":"https://images.unsplash.com/photo-1466637574441-749b8f19452f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images3":"https://images.unsplash.com/photo-1532490389938-2856e3f1560a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        "images4":"https://images.unsplash.com/photo-1615529182904-14819c35db37?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
    },
    # *End6
]
# !End France

app = FastAPI()


@app.get("/America")
def read_root():
    return homeamerica_db


@app.get('/America/{id}')
async def america(id: int):
    america = homeamerica_db[id-1]
    return america

# *End America

@app.get("/Spain")
def read_root():
    return homespain_db


@app.get('/Spain/{id}')
async def america(id: int):
    spain = homespain_db[id-1]
    return spain

# *End Spain

@app.get("/London")
def read_root():
    return homelondon_db


@app.get('/London/{id}')
async def america(id: int):
    spain = homelondon_db[id-1]
    return spain

# *End London

@app.get("/France")
def read_root():
    return homefrance_db


@app.get('/France/{id}')
async def america(id: int):
    france = homefrance_db[id-1]
    return france

# *End France
import time
import asyncio
import requests
async def func1():
  URL = "https://th.bing.com/th/id/OIP.60nlpatndA3ytb7Y3bFT3gHaEK?pid=ImgDet&rs=1"
  response = requests.get(URL)
  open("instagram1.jpj", "wb").write(response.content)
  
  print("sujit")
  return "sakshi"
async def func2():
  URL = "https://th.bing.com/th/id/R.4f78175eb1a761b3337e6ffef1e5ca29?rik=KPLb738B6GPESA&riu=http%3a%2f%2frossstrategic.com%2fimg%2fsvc-placeholder1.jpg&ehk=UROUe6U8%2f58Xva7TsUi5okGnxJS7KmrOVLX8%2buq5avs%3d&risl=&pid=ImgRaw&r=0"
  response = requests.get(URL)
  open("instagram2.jpj", "wb").write(response.content)
  

    
  print("hiraj")
async def func3():
  URL = "https://hdqwalls.com/wallpapers/blue-water-mountains-image.jpg"
  response = requests.get(URL)
  open("instagram3.jpj", "wb").write(response.content)
  print("rishi")
async def main():
  L=await asyncio.gather(
    func1(),
    func2(),
    func3(),
  )
  print(L)
#     task=asyncio.create_task(func1())
  
    # await func1()
    # await func2()
    # await func3()
asyncio.run(main())
from openai import OpenAI
client = OpenAI(
     api_key = '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'
)

# response = client.images.generate(
#     model="dall-e-2",
#     prompt="cute golden retriever",
#     size="256x256",
#     n=2,
# )

# print(response)
# print(response.data[0].url)


# v2 "256x256" "512x512" "1024x1024"  v3"1024x1792" "1792x1024"
# "standard","hd",
# number of image quantity

# https://platform.openai.com/docs/guides/image-generation

# responses
# ImagesResponse(created=1745250206, data=[Image(b64_json=None, revised_prompt=None, url='https://oaidalleapiprodscus.blob.core.windows.net/private/org-vph1klcWeMDQihO4KhnRc49G/user-fZ5XcmQZfJeXvvkQ90e4MVq9/img-7DVU78mfIbi9QxRSk9WCs4pa.png?st=2025-04-21T14%3A43%3A26Z&se=2025-04-21T16%3A43%3A26Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=52f8f7b3-ca8d-4b21-9807-8b9df114d84c&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-21T00%3A41%3A55Z&ske=2025-04-22T00%3A41%3A55Z&sks=b&skv=2024-08-04&sig=CV27pT8mlzxJM5AW1RZtaIr95r8vp5veVGi0NrZk%2Bvw%3D')])

# ImagesResponse(created=1745250256, data=[Image(b64_json=None, revised_prompt=None, url='https://oaidalleapiprodscus.blob.core.windows.net/private/org-vph1klcWeMDQihO4KhnRc49G/user-fZ5XcmQZfJeXvvkQ90e4MVq9/img-KM5wfKplVC4F5bzvfBv9XaNB.png?st=2025-04-21T14%3A44%3A16Z&se=2025-04-21T16%3A44%3A16Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=52f8f7b3-ca8d-4b21-9807-8b9df114d84c&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-21T13%3A39%3A53Z&ske=2025-04-22T13%3A39%3A53Z&sks=b&skv=2024-08-04&sig=JruknxdNCwq%2BsJ1OCY4NeZzMisq8U8V9YHHoby0RD0U%3D')])

# ImagesResponse(created=1745250349, data=[Image(b64_json=None, revised_prompt=None, url='https://oaidalleapiprodscus.blob.core.windows.net/private/org-vph1klcWeMDQihO4KhnRc49G/user-fZ5XcmQZfJeXvvkQ90e4MVq9/img-tYWyprPMXshLulbGDpBrZwGT.png?st=2025-04-21T14%3A45%3A49Z&se=2025-04-21T16%3A45%3A49Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=52f8f7b3-ca8d-4b21-9807-8b9df114d84c&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-21T00%3A42%3A30Z&ske=2025-04-22T00%3A42%3A30Z&sks=b&skv=2024-08-04&sig=oO3IVPw8rb%2Bk0LSfH7ombBe4o%2B%2BGnUuqMfPFNTGcz34%3D')])

# ImagesResponse(created=1745250442, data=[Image(b64_json=None, revised_prompt=None, url='https://oaidalleapiprodscus.blob.core.windows.net/private/org-vph1klcWeMDQihO4KhnRc49G/user-fZ5XcmQZfJeXvvkQ90e4MVq9/img-izTFN0EqQQncbvfhe0uwws6R.png?st=2025-04-21T14%3A47%3A22Z&se=2025-04-21T16%3A47%3A22Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=52f8f7b3-ca8d-4b21-9807-8b9df114d84c&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-21T10%3A00%3A49Z&ske=2025-04-22T10%3A00%3A49Z&sks=b&skv=2024-08-04&sig=6EO1ILdPvnRJbNX59EKRjpZdP4HbFKYccUjmAWybOOw%3D'), Image(b64_json=None, revised_prompt=None, url='https://oaidalleapiprodscus.blob.core.windows.net/private/org-vph1klcWeMDQihO4KhnRc49G/user-fZ5XcmQZfJeXvvkQ90e4MVq9/img-yBfPB8qQ86FAB3lvrUS7mLmA.png?st=2025-04-21T14%3A47%3A22Z&se=2025-04-21T16%3A47%3A22Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=52f8f7b3-ca8d-4b21-9807-8b9df114d84c&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-21T10%3A00%3A49Z&ske=2025-04-22T10%3A00%3A49Z&sks=b&skv=2024-08-04&sig=eFrq/OEmBAQi0egLVZnLBB8nreZxdi04KdwuC%2B%2BEtFI%3D')])
# https://oaidalleapiprodscus.blob.core.windows.net/private/org-vph1klcWeMDQihO4KhnRc49G/user-fZ5XcmQZfJeXvvkQ90e4MVq9/img-izTFN0EqQQncbvfhe0uwws6R.png?st=2025-04-21T14%3A47%3A22Z&se=2025-04-21T16%3A47%3A22Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=52f8f7b3-ca8d-4b21-9807-8b9df114d84c&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-21T10%3A00%3A49Z&ske=2025-04-22T10%3A00%3A49Z&sks=b&skv=2024-08-04&sig=6EO1ILdPvnRJbNX59EKRjpZdP4HbFKYccUjmAWybOOw%3D


def generateimage(prompt,size="256x256",n=1):
     try:
          response = client.images.generate(
               model="dall-e-2",
               prompt=prompt,
               size=size,
               n=n,
          )

          return [ img.url for img in response.data]
     except Exception as e:
          print(f"Error found: {e}")
          return []


def main():
     print("Dell-E Image Generator Version 2, (type 'exit' to stop app)")

     while True:
          prompt = input("Enter your image prompt: ").strip()

          if prompt.lower() == 'exit':
               print("Exiting Image Generator")
               break

          getimageurls = generateimage(prompt,"256x256",2)
          if getimageurls:
               print(f"Generate Image Result")
               for i,getimageurl in enumerate(getimageurls,start=1):
                    print(f"{i}. {getimageurl}")
          else:
               print(f"Failed to generate image. Please try again")

if __name__ == "__main__":
     main()





# Dell-E Image Generator Version 2, (type 'exit' to stop app)
# Enter your image prompt: drunk dog with red blue T-shirt  
# Generate Image Result
# 1. https://oaidalleapiprodscus.blob.core.windows.net/private/org-vph1klcWeMDQihO4KhnRc49G/user-fZ5XcmQZfJeXvvkQ90e4MVq9/img-BDlnTJa6ZjEMtLD8P8I30u1m.png?st=2025-04-21T15%3A17%3A15Z&se=2025-04-21T17%3A17%3A15Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=52f8f7b3-ca8d-4b21-9807-8b9df114d84c&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-21T13%3A00%3A52Z&ske=2025-04-22T13%3A00%3A52Z&sks=b&skv=2024-08-04&sig=HJrmiRpAj9DedHQFwF1Lq11Z13HPAAt0/BUGC23OYwA%3D
# Enter your image prompt: Baby cats
# Error found: Error code: 429 - {'error': {'message': 'Error in request. Please check your input.', 'type': 'invalid_request_error', 'param': None, 'code': None}}
# Failed to generate image. Please try again
# Enter your image prompt: kitty
# Error found: Error code: 429 - {'error': {'message': 'Error in request. Please check your input.', 'type': 'invalid_request_error', 'param': None, 'code': None}}
# Failed to generate image. Please try again
# Enter your image prompt: cute dog
# Generate Image Result
# 1. https://oaidalleapiprodscus.blob.core.windows.net/private/org-vph1klcWeMDQihO4KhnRc49G/user-fZ5XcmQZfJeXvvkQ90e4MVq9/img-KQgycUobOwYDtWyYhW9vKZFW.png?st=2025-04-21T15%3A18%3A25Z&se=2025-04-21T17%3A18%3A25Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=52f8f7b3-ca8d-4b21-9807-8b9df114d84c&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-21T12%3A26%3A15Z&ske=2025-04-22T12%3A26%3A15Z&sks=b&skv=2024-08-04&sig=sWt9uLK1T89GzT7QU8pGew7U3G1eW9M7c%2BorrcruxY0%3D
# Enter your image prompt: exit
# Exiting Image Generator

# 21GN


# Enter your image prompt: blackpink members
# Generate Image Result
# 1. https://oaidalleapiprodscus.blob.core.windows.net/private/org-vph1klcWeMDQihO4KhnRc49G/user-fZ5XcmQZfJeXvvkQ90e4MVq9/img-EHbdPRk8iEdoVDCCoPNheaXt.png?st=2025-04-21T15%3A32%3A14Z&se=2025-04-21T17%3A32%3A14Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=8b33a531-2df9-46a3-bc02-d4b1430a422c&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-20T20%3A23%3A00Z&ske=2025-04-21T20%3A23%3A00Z&sks=b&skv=2024-08-04&sig=ecpOJc93kwREk02AndCKShgp9HMYdmlt7YJEuvCx6ys%3D
# 2. https://oaidalleapiprodscus.blob.core.windows.net/private/org-vph1klcWeMDQihO4KhnRc49G/user-fZ5XcmQZfJeXvvkQ90e4MVq9/img-xLHLUcocF3YXA3ncXZs6JMXl.png?st=2025-04-21T15%3A32%3A14Z&se=2025-04-21T17%3A32%3A14Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=8b33a531-2df9-46a3-bc02-d4b1430a422c&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-20T20%3A23%3A00Z&ske=2025-04-21T20%3A23%3A00Z&sks=b&skv=2024-08-04&sig=wwRKxXVLbBuK2UhpkvPPSAgV7W0m5sMljS3r/UKCtwU%3D
# Enter your image prompt: baby girls
# Generate Image Result
# 1. https://oaidalleapiprodscus.blob.core.windows.net/private/org-vph1klcWeMDQihO4KhnRc49G/user-fZ5XcmQZfJeXvvkQ90e4MVq9/img-i9S38x61IpciQRT6Ems4tW2z.png?st=2025-04-21T15%3A32%3A43Z&se=2025-04-21T17%3A32%3A43Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=8b33a531-2df9-46a3-bc02-d4b1430a422c&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-21T10%3A30%3A24Z&ske=2025-04-22T10%3A30%3A24Z&sks=b&skv=2024-08-04&sig=dNykTS30mXZy4koXEypENlEkbaKJTmtQ1Nti8j8csao%3D
# 2. https://oaidalleapiprodscus.blob.core.windows.net/private/org-vph1klcWeMDQihO4KhnRc49G/user-fZ5XcmQZfJeXvvkQ90e4MVq9/img-8ZZByqpRiF31FxqqSwiZDFUF.png?st=2025-04-21T15%3A32%3A43Z&se=2025-04-21T17%3A32%3A43Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=8b33a531-2df9-46a3-bc02-d4b1430a422c&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-21T10%3A30%3A24Z&ske=2025-04-22T10%3A30%3A24Z&sks=b&skv=2024-08-04&sig=KCdoiyFY15yr46e6Ui3uyoXYA82O%2BNZfnikV3djHigY%3D
# Enter your image prompt:


# Enter your image prompt: sunset
# Generate Image Result
# 1. https://oaidalleapiprodscus.blob.core.windows.net/private/org-vph1klcWeMDQihO4KhnRc49G/user-fZ5XcmQZfJeXvvkQ90e4MVq9/img-zDqOt01Xqog3ze4TL2JFC56W.png?st=2025-04-29T14%3A32%3A41Z&se=2025-04-29T16%3A32%3A41Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=475fd488-6c59-44a5-9aa9-31c4db451bea&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-28T22%3A55%3A20Z&ske=2025-04-29T22%3A55%3A20Z&sks=b&skv=2024-08-04&sig=otBX4ltgy7At7TG2Zpijt/QK4MJbL%2BxuwL2/zFCbi/g%3D
# 2. https://oaidalleapiprodscus.blob.core.windows.net/private/org-vph1klcWeMDQihO4KhnRc49G/user-fZ5XcmQZfJeXvvkQ90e4MVq9/img-MuzxbNNGRH7Lh6Nmxh1DENOZ.png?st=2025-04-29T14%3A32%3A41Z&se=2025-04-29T16%3A32%3A41Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=475fd488-6c59-44a5-9aa9-31c4db451bea&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-28T22%3A55%3A20Z&ske=2025-04-29T22%3A55%3A20Z&sks=b&skv=2024-08-04&sig=Jch9GHdiQjXUBsG4QVeRGzIaJwfWE%2BO8Qs4aK3c6Dcs%3D
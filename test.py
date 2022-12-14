import requests

# created this file to test requesting an image from url, opening it,
# saving it, and returning image url

def img_test0():
    image_url = 'https://res.cloudinary.com/sagacity/image/upload/c_crop,h_480,w_1084,x_0,y_0/c_limit,dpr_auto,f_auto,fl_lossy,q_80,w_1080/Pixabay_1_swmxbf.jpg'
    response = requests.get(image_url) # collect image data from url
    destination_url = 'images/image.png'
    with open(destination_url, 'wb') as file:
        file.write(response.content)
    return destination_url

url = img_test0()